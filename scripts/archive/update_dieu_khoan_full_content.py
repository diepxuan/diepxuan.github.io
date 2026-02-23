#!/usr/bin/env python3
"""
Script để update dieu_khoan.ten với nội dung đầy đủ từ HTML files
Hiện tại dieu_khoan.ten chỉ có tiêu đề, cần thêm nội dung từ pNoiDung
"""

import os
import re
import mysql.connector
from mysql.connector import Error
import html
import time
from pathlib import Path

# Database connection
DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'database': 'vbpl',
    'charset': 'utf8mb4'
}

# Path to HTML files
HTML_DIR = "/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/demuc"

def extract_full_content_from_html(html_content, mapc):
    """
    Extract full content for a specific MAPC from HTML
    Format: <p class='pDieu'><a name='MAPC'></a>Tiêu đề</p>...<p class='pNoiDung'>Nội dung</p>
    """
    try:
        # Find the Dieu element with this MAPC
        dieu_pattern = rf"<p class='pDieu'><a name='{re.escape(mapc)}'></a>(.*?)</p>"
        dieu_match = re.search(dieu_pattern, html_content, re.DOTALL)
        
        if not dieu_match:
            return None
        
        # Get the title
        title = dieu_match.group(1).strip()
        
        # Find the NoiDung section after this Dieu
        # Look for the next pNoiDung after this pDieu
        start_pos = dieu_match.end()
        
        # Find pNoiDung
        noidung_pattern = r"<p class='pNoiDung'>(.*?)</p>"
        noidung_match = re.search(noidung_pattern, html_content[start_pos:], re.DOTALL)
        
        if not noidung_match:
            # Try alternative pattern (sometimes content is wrapped in <p> inside)
            noidung_pattern = r"<p class='pNoiDung'><p>(.*?)</p></p>"
            noidung_match = re.search(noidung_pattern, html_content[start_pos:], re.DOTALL)
        
        if noidung_match:
            content = noidung_match.group(1).strip()
            # Clean HTML tags
            content = re.sub(r'<[^>]+>', '', content)
            content = html.unescape(content)
            content = re.sub(r'\s+', ' ', content).strip()
            
            # Combine title and content
            full_content = f"{title}\n\n{content}"
            return full_content
        else:
            # If no pNoiDung found, return just the title
            return title
    
    except Exception as e:
        print(f"Error extracting content for MAPC {mapc}: {e}")
        return None

def get_html_content_for_de_muc(de_muc_id):
    """Get HTML content for a de_muc from database"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        
        # Get the file name from de_muc (id is the file name without .html)
        cursor.execute("SELECT id, text FROM de_muc WHERE id = %s", (de_muc_id,))
        de_muc = cursor.fetchone()
        
        if not de_muc:
            print(f"De muc {de_muc_id} not found")
            return None
        
        # The id is the file name without .html, but need to add hyphens
        # Database id: 59750dbc0ac34d75928e18983dc7ecf6
        # File name: 59750dbc-0ac3-4d75-928e-18983dc7ecf6.html
        # Add hyphens at positions: 8, 12, 16, 20
        if len(de_muc_id) == 32:  # UUID without hyphens
            file_id = f"{de_muc_id[:8]}-{de_muc_id[8:12]}-{de_muc_id[12:16]}-{de_muc_id[16:20]}-{de_muc_id[20:]}"
        else:
            file_id = de_muc_id
        
        html_file = os.path.join(HTML_DIR, f"{file_id}.html")
        
        if not os.path.exists(html_file):
            print(f"HTML file not found: {html_file}")
            return None
        
        # Read HTML content
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        cursor.close()
        conn.close()
        
        return html_content
    
    except Error as e:
        print(f"Database error: {e}")
        return None

def update_dieu_khoan_for_de_muc(de_muc_id):
    """Update all dieu_khoan for a specific de_muc"""
    try:
        # Get HTML content
        html_content = get_html_content_for_de_muc(de_muc_id)
        if not html_content:
            print(f"No HTML content for de_muc {de_muc_id}")
            return 0
        
        # Connect to database
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        
        # Get all dieu_khoan for this de_muc
        cursor.execute("""
            SELECT id, chi_muc, ten, mapc, de_muc_id 
            FROM dieu_khoan 
            WHERE de_muc_id = %s
            ORDER BY mapc
        """, (de_muc_id,))
        
        dieu_khoan_list = cursor.fetchall()
        updated_count = 0
        
        print(f"Processing {len(dieu_khoan_list)} dieu_khoan for de_muc {de_muc_id}")
        
        for dk in dieu_khoan_list:
            current_content = dk['ten']
            mapc = dk['mapc']
            
            # Extract full content from HTML
            full_content = extract_full_content_from_html(html_content, mapc)
            
            if full_content and full_content != current_content:
                # Update the record
                update_cursor = conn.cursor()
                update_cursor.execute("""
                    UPDATE dieu_khoan 
                    SET ten = %s 
                    WHERE id = %s
                """, (full_content, dk['id']))
                
                updated_count += 1
                
                # Show preview of update
                print(f"  Updated Điều {dk['chi_muc']}:")
                print(f"    Old length: {len(current_content)} chars")
                print(f"    New length: {len(full_content)} chars")
                print(f"    Preview: {full_content[:100]}...")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"Updated {updated_count}/{len(dieu_khoan_list)} records for de_muc {de_muc_id}")
        return updated_count
    
    except Error as e:
        print(f"Database error for de_muc {de_muc_id}: {e}")
        return 0

def update_all_dieu_khoan():
    """Update all dieu_khoan for all de_muc"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        
        # Get all de_muc
        cursor.execute("SELECT id, text FROM de_muc ORDER BY text")
        de_muc_list = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        total_updated = 0
        total_processed = 0
        
        print(f"Found {len(de_muc_list)} de_muc to process")
        
        for de_muc in de_muc_list:
            print(f"\n{'='*60}")
            print(f"Processing: {de_muc['text']} ({de_muc['id']})")
            print(f"{'='*60}")
            
            updated = update_dieu_khoan_for_de_muc(de_muc['id'])
            total_updated += updated
            total_processed += 1
            
            # Small delay to avoid overwhelming the database
            time.sleep(0.1)
        
        print(f"\n{'='*60}")
        print(f"SUMMARY:")
        print(f"  Total de_muc processed: {total_processed}")
        print(f"  Total dieu_khoan updated: {total_updated}")
        print(f"{'='*60}")
        
        return total_updated
    
    except Error as e:
        print(f"Database error: {e}")
        return 0

def test_single_de_muc(de_muc_text):
    """Test with a single de_muc"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT id, text FROM de_muc WHERE text LIKE %s", (f"%{de_muc_text}%",))
        de_muc = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if de_muc:
            print(f"Testing with: {de_muc['text']} ({de_muc['id']})")
            update_dieu_khoan_for_de_muc(de_muc['id'])
        else:
            print(f"De muc not found: {de_muc_text}")
    
    except Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            if len(sys.argv) > 2:
                test_single_de_muc(sys.argv[2])
            else:
                # Test with "Công tác văn thư"
                test_single_de_muc("Công tác văn thư")
        elif sys.argv[1] == "--all":
            update_all_dieu_khoan()
        else:
            # Process specific de_muc by ID
            update_dieu_khoan_for_de_muc(sys.argv[1])
    else:
        print("Usage:")
        print("  python update_dieu_khoan_full_content.py --test [de_muc_text]")
        print("  python update_dieu_khoan_full_content.py --all")
        print("  python update_dieu_khoan_full_content.py [de_muc_id]")
        print("\nExample:")
        print("  python update_dieu_khoan_full_content.py --test 'Công tác văn thư'")
        print("  python update_dieu_khoan_full_content.py --all")
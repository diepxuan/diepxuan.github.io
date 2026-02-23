#!/usr/bin/env python3
"""
Batch update dieu_khoan.ten với nội dung đầy đủ
Xử lý theo batch để tránh timeout và monitor progress
"""

import os
import re
import mysql.connector
from mysql.connector import Error
import html
import time
import json
from pathlib import Path
from datetime import datetime

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

# Progress file
PROGRESS_FILE = "/root/.openclaw/workspace/projects/github-io/scripts/update_progress.json"

def load_progress():
    """Load progress from file"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "started_at": datetime.now().isoformat(),
        "completed": [],
        "failed": [],
        "total_updated": 0,
        "last_processed": None
    }

def save_progress(progress):
    """Save progress to file"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

def extract_full_content_from_html(html_content, mapc):
    """
    Extract full content for a specific MAPC from HTML
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
        # The id is the file name without .html, but need to add hyphens
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
        
        return html_content
    
    except Exception as e:
        print(f"Error reading HTML for {de_muc_id}: {e}")
        return None

def update_dieu_khoan_for_de_muc(de_muc_id, de_muc_name):
    """Update all dieu_khoan for a specific de_muc"""
    try:
        # Get HTML content
        html_content = get_html_content_for_de_muc(de_muc_id)
        if not html_content:
            print(f"No HTML content for de_muc {de_muc_id}")
            return 0, False
        
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
        
        print(f"Processing {len(dieu_khoan_list)} dieu_khoan for: {de_muc_name}")
        
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
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"  Updated {updated_count}/{len(dieu_khoan_list)} records")
        return updated_count, True
    
    except Error as e:
        print(f"Database error for de_muc {de_muc_id}: {e}")
        return 0, False

def process_batch(batch_size=10, start_from=0):
    """Process a batch of de_muc"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        
        # Get de_muc for this batch
        cursor.execute("""
            SELECT id, text 
            FROM de_muc 
            ORDER BY text
            LIMIT %s OFFSET %s
        """, (batch_size, start_from))
        
        de_muc_list = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        if not de_muc_list:
            print("No more de_muc to process")
            return 0, 0
        
        # Load progress
        progress = load_progress()
        
        total_updated = 0
        processed_count = 0
        
        print(f"\n{'='*60}")
        print(f"Processing batch: {start_from + 1} to {start_from + len(de_muc_list)}")
        print(f"{'='*60}")
        
        for de_muc in de_muc_list:
            if de_muc['id'] in progress['completed']:
                print(f"Skipping already processed: {de_muc['text']}")
                continue
            
            print(f"\n[{processed_count + 1}/{len(de_muc_list)}] ", end="")
            
            updated, success = update_dieu_khoan_for_de_muc(de_muc['id'], de_muc['text'])
            
            if success:
                progress['completed'].append(de_muc['id'])
                progress['total_updated'] += updated
                progress['last_processed'] = {
                    'id': de_muc['id'],
                    'name': de_muc['text'],
                    'updated': updated,
                    'timestamp': datetime.now().isoformat()
                }
                total_updated += updated
            else:
                progress['failed'].append({
                    'id': de_muc['id'],
                    'name': de_muc['text'],
                    'error': 'Failed to process',
                    'timestamp': datetime.now().isoformat()
                })
            
            processed_count += 1
            
            # Save progress after each de_muc
            save_progress(progress)
            
            # Small delay
            time.sleep(0.05)
        
        print(f"\n{'='*60}")
        print(f"Batch completed:")
        print(f"  Processed: {processed_count} de_muc")
        print(f"  Updated: {total_updated} dieu_khoan")
        print(f"  Total so far: {progress['total_updated']} dieu_khoan updated")
        print(f"{'='*60}")
        
        return processed_count, total_updated
    
    except Error as e:
        print(f"Database error: {e}")
        return 0, 0

def show_progress():
    """Show current progress"""
    progress = load_progress()
    
    print(f"\n{'='*60}")
    print(f"UPDATE PROGRESS")
    print(f"{'='*60}")
    print(f"Started at: {progress.get('started_at', 'N/A')}")
    print(f"Completed: {len(progress.get('completed', []))} de_muc")
    print(f"Failed: {len(progress.get('failed', []))} de_muc")
    print(f"Total dieu_khoan updated: {progress.get('total_updated', 0)}")
    
    if progress.get('last_processed'):
        last = progress['last_processed']
        print(f"Last processed: {last.get('name', 'N/A')}")
        print(f"  Updated: {last.get('updated', 0)} dieu_khoan")
        print(f"  At: {last.get('timestamp', 'N/A')}")
    
    # Get total count
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM de_muc")
        total_de_muc = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan")
        total_dieu_khoan = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
        
        print(f"\nTotal in database:")
        print(f"  de_muc: {total_de_muc}")
        print(f"  dieu_khoan: {total_dieu_khoan}")
        
        completed_pct = (len(progress.get('completed', [])) / total_de_muc * 100) if total_de_muc > 0 else 0
        print(f"\nProgress: {completed_pct:.1f}% ({len(progress.get('completed', []))}/{total_de_muc})")
        
    except Error as e:
        print(f"Error getting totals: {e}")
    
    print(f"{'='*60}")

def reset_progress():
    """Reset progress"""
    progress = {
        "started_at": datetime.now().isoformat(),
        "completed": [],
        "failed": [],
        "total_updated": 0,
        "last_processed": None
    }
    save_progress(progress)
    print("Progress reset")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--progress":
            show_progress()
        elif sys.argv[1] == "--reset":
            reset_progress()
        elif sys.argv[1] == "--batch":
            batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            start_from = int(sys.argv[3]) if len(sys.argv) > 3 else 0
            process_batch(batch_size, start_from)
        elif sys.argv[1] == "--all":
            # Process all in batches
            batch_size = 20
            start_from = 0
            
            while True:
                processed, updated = process_batch(batch_size, start_from)
                if processed == 0:
                    break
                start_from += batch_size
                
                # Show progress
                show_progress()
                
                # Ask to continue if not all processed
                try:
                    conn = mysql.connector.connect(**DB_CONFIG)
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM de_muc")
                    total = cursor.fetchone()[0]
                    cursor.close()
                    conn.close()
                    
                    if start_from >= total:
                        print("\nAll de_muc processed!")
                        break
                    
                    # Continue automatically
                    print("\nContinuing to next batch in 2 seconds...")
                    time.sleep(2)
                    
                except Error:
                    break
        else:
            # Process specific de_muc
            de_muc_id = sys.argv[1]
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT id, text FROM de_muc WHERE id = %s", (de_muc_id,))
                de_muc = cursor.fetchone()
                cursor.close()
                conn.close()
                
                if de_muc:
                    update_dieu_khoan_for_de_muc(de_muc['id'], de_muc['text'])
                else:
                    print(f"De muc not found: {de_muc_id}")
            
            except Error as e:
                print(f"Database error: {e}")
    else:
        print("Usage:")
        print("  python batch_update_dieu_khoan.py --progress")
        print("  python batch_update_dieu_khoan.py --reset")
        print("  python batch_update_dieu_khoan.py --batch [size] [start_from]")
        print("  python batch_update_dieu_khoan.py --all")
        print("  python batch_update_dieu_khoan.py [de_muc_id]")
        print("\nExample:")
        print("  python batch_update_dieu_khoan.py --progress")
        print("  python batch_update_dieu_khoan.py --batch 20 0")
        print("  python batch_update_dieu_khoan.py --all")
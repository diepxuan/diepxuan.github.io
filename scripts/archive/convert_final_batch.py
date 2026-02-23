#!/usr/bin/env python3
"""
Convert 76 files cuối cùng sang markdown
"""

import os
import re
import mysql.connector
from mysql.connector import Error
import sys
from datetime import datetime

DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

def html_to_markdown_simple(html_content):
    """Convert HTML sang Markdown đơn giản"""
    if not html_content:
        return ""
    
    html_content = html_content.replace('\ufeff', '')
    
    # Extract main content
    content_match = re.search(r"<div class='_content'>(.*?)</div>", html_content, re.DOTALL)
    if content_match:
        html_content = content_match.group(1)
    
    # Remove script/style
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
    
    # Simple conversions
    markdown = html_content
    markdown = re.sub(r'<h[1-4][^>]*>(.*?)</h[1-4]>', r'# \1\n\n', markdown)
    markdown = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    markdown = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', markdown)
    markdown = re.sub(r'<[^>]+>', '', markdown)
    
    # Clean up
    markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
    markdown = re.sub(r'[ \t]+', ' ', markdown)
    markdown = markdown.strip()
    
    return markdown

def main():
    print("=== CONVERT 76 FILES CUỐI CÙNG SANG MARKDOWN ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✓ Kết nối database thành công")
    except Error as e:
        print(f"✗ Lỗi kết nối: {e}")
        return
    
    cursor = connection.cursor()
    
    try:
        # Lấy files chưa convert
        cursor.execute("""
            SELECT dm.value, dm.id, dm.text, dmc.file_name, dmc.html_content
            FROM de_muc_content dmc
            JOIN de_muc dm ON dmc.de_muc_id = dm.id
            WHERE NOT EXISTS (
                SELECT 1 FROM de_muc_markdown dmm 
                WHERE dmm.de_muc_id = dm.id
            )
            ORDER BY dm.value
            LIMIT 76  -- Chỉ lấy 76 files còn lại
        """)
        
        files = cursor.fetchall()
        print(f"✓ Tìm thấy {len(files)} files cần convert")
        
        if len(files) == 0:
            print("✓ Tất cả files đã được convert!")
            return
        
        converted = 0
        errors = 0
        
        # Convert từng file
        for i, (uuid, de_muc_id, de_muc_name, file_name, html_content) in enumerate(files, 1):
            try:
                # Convert HTML sang Markdown
                markdown_content = html_to_markdown_simple(html_content)
                
                # Tạo ID
                record_id = f"md_{uuid.replace('-', '')[:30]}"
                
                # Insert vào database
                cursor.execute("""
                    INSERT INTO de_muc_markdown 
                    (id, de_muc_id, file_name, markdown_content, html_content, content_size)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    record_id, 
                    de_muc_id, 
                    file_name, 
                    markdown_content, 
                    html_content, 
                    len(markdown_content)
                ))
                
                converted += 1
                
                # Progress mỗi 10 files
                if converted % 10 == 0:
                    print(f"  Đã convert {converted}/{len(files)} files")
                    connection.commit()
                    
            except Exception as e:
                errors += 1
                print(f"  ✗ Lỗi convert file {file_name}: {e}")
        
        # Commit cuối
        connection.commit()
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Tổng files: {len(files)}")
        print(f"Đã convert: {converted}")
        print(f"Lỗi: {errors}")
        
        # Kiểm tra tổng số records
        cursor.execute("SELECT COUNT(*) FROM de_muc_markdown")
        total = cursor.fetchone()[0]
        print(f"Tổng records trong de_muc_markdown: {total}")
        
        # Kiểm tra coverage
        cursor.execute("SELECT COUNT(*) FROM de_muc")
        total_demuc = cursor.fetchone()[0]
        coverage = (total / total_demuc * 100) if total_demuc > 0 else 0
        print(f"Coverage: {coverage:.1f}% ({total}/{total_demuc})")
        
        # Kiểm tra files còn lại
        cursor.execute("""
            SELECT COUNT(*) as remaining_files
            FROM de_muc_content dmc
            WHERE NOT EXISTS (
                SELECT 1 FROM de_muc_markdown dmm 
                WHERE dmm.de_muc_id = dmc.de_muc_id
            )
        """)
        remaining = cursor.fetchone()[0]
        print(f"Files còn lại: {remaining}")
        
    except Exception as e:
        print(f"✗ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        cursor.close()
        connection.close()
        print("✓ Đã đóng kết nối database")
        print(f"Thời gian kết thúc: {datetime.now()}")

if __name__ == "__main__":
    main()
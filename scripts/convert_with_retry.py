#!/usr/bin/env python3
"""
Convert với retry logic và batch nhỏ (10 files/batch)
"""

import os
import re
import mysql.connector
from mysql.connector import Error
import sys
from datetime import datetime
import time

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

def get_connection():
    """Get database connection với retry"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            print(f"✓ Kết nối database thành công (attempt {attempt + 1})")
            return connection
        except Error as e:
            print(f"✗ Lỗi kết nối (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                print(f"  Đang thử lại sau 5 giây...")
                time.sleep(5)
            else:
                raise

def convert_batch(connection, files_batch, batch_num):
    """Convert một batch files"""
    cursor = connection.cursor()
    converted = 0
    errors = 0
    
    print(f"\n=== BATCH {batch_num} ({len(files_batch)} files) ===")
    
    for file_info in files_batch:
        uuid = file_info['uuid']
        de_muc_id = file_info['de_muc_id']
        file_name = file_info['file_name']
        html_content = file_info['html_content']
        
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
            
        except Exception as e:
            errors += 1
            print(f"  ✗ Lỗi convert file {file_name}: {e}")
    
    # Commit batch
    try:
        connection.commit()
        print(f"  ✓ Đã commit batch {batch_num}: {converted} converted, {errors} errors")
    except Error as e:
        print(f"  ✗ Lỗi commit batch {batch_num}: {e}")
        connection.rollback()
        converted = 0  # Reset vì commit failed
    
    cursor.close()
    return converted, errors

def main():
    print("=== CONVERT VỚI RETRY LOGIC ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    try:
        connection = get_connection()
    except Error as e:
        print(f"✗ Không thể kết nối database: {e}")
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
        """)
        
        files_data = cursor.fetchall()
        print(f"✓ Tìm thấy {len(files_data)} files cần convert")
        
        if len(files_data) == 0:
            print("✓ Tất cả files đã được convert!")
            return
        
        # Chuyển đổi dữ liệu
        files = []
        for uuid, de_muc_id, de_muc_name, file_name, html_content in files_data:
            files.append({
                'uuid': uuid,
                'de_muc_id': de_muc_id,
                'de_muc_name': de_muc_name,
                'file_name': file_name,
                'html_content': html_content
            })
        
        # Chia thành batch nhỏ (10 files/batch)
        batch_size = 10
        batches = [files[i:i + batch_size] for i in range(0, len(files), batch_size)]
        
        total_converted = 0
        total_errors = 0
        
        # Process từng batch
        for batch_num, batch_files in enumerate(batches, 1):
            print(f"\n--- Processing batch {batch_num}/{len(batches)} ---")
            
            # Thử convert batch này
            converted, errors = convert_batch(connection, batch_files, batch_num)
            total_converted += converted
            total_errors += errors
            
            # Chờ giữa các batch
            if batch_num < len(batches):
                print(f"  Đang chờ 3 giây trước batch tiếp theo...")
                time.sleep(3)
        
        print(f"\n=== KẾT QUẢ TỔNG ===")
        print(f"Tổng files: {len(files)}")
        print(f"Đã convert: {total_converted}")
        print(f"Lỗi: {total_errors}")
        
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
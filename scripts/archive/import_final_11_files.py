#!/usr/bin/env python3
"""
Import 11 files cuối cùng với strategy đặc biệt cho files lớn
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
    'charset': 'utf8mb4',
    'connection_timeout': 30,
    'buffered': True
}

def html_to_markdown_chunked(html_content, max_chunk_size=5000000):
    """
    Convert HTML sang Markdown với chunk processing cho files lớn
    """
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
    
    # Chunk processing cho files lớn
    if len(html_content) > max_chunk_size:
        print(f"  ⚠ File lớn ({len(html_content):,} bytes), đang xử lý theo chunks...")
        
        # Chia thành chunks
        chunks = []
        chunk_size = max_chunk_size // 2  # 2.5MB mỗi chunk
        for i in range(0, len(html_content), chunk_size):
            chunk = html_content[i:i + chunk_size]
            
            # Process chunk
            markdown_chunk = chunk
            markdown_chunk = re.sub(r'<h[1-4][^>]*>(.*?)</h[1-4]>', r'# \1\n\n', markdown_chunk)
            markdown_chunk = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', markdown_chunk)
            markdown_chunk = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', markdown_chunk)
            markdown_chunk = re.sub(r'<[^>]+>', '', markdown_chunk)
            
            chunks.append(markdown_chunk)
        
        # Combine chunks
        markdown = ''.join(chunks)
    else:
        # Process normally
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

def get_remaining_files(connection):
    """Lấy 11 files còn lại"""
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT dm.value, dm.id, dm.text, dmc.file_name, dmc.html_content,
               LENGTH(dmc.html_content) as html_size
        FROM de_muc_content dmc
        JOIN de_muc dm ON dmc.de_muc_id = dm.id
        WHERE NOT EXISTS (
            SELECT 1 FROM de_muc_markdown dmm 
            WHERE dmm.de_muc_id = dm.id
        )
        ORDER BY LENGTH(dmc.html_content) ASC  -- Xử lý files nhỏ trước
    """)
    
    files = []
    for row in cursor.fetchall():
        uuid, de_muc_id, de_muc_name, file_name, html_content, html_size = row
        files.append({
            'uuid': uuid,
            'de_muc_id': de_muc_id,
            'de_muc_name': de_muc_name,
            'file_name': file_name,
            'html_content': html_content,
            'html_size': html_size
        })
    
    cursor.close()
    return files

def import_file(connection, file_info, attempt=1, max_attempts=3):
    """Import một file với retry logic"""
    uuid = file_info['uuid']
    de_muc_id = file_info['de_muc_id']
    file_name = file_info['file_name']
    html_content = file_info['html_content']
    html_size = file_info['html_size']
    
    cursor = connection.cursor()
    
    try:
        print(f"  Processing: {file_name} ({html_size:,} bytes)")
        
        # Convert HTML sang Markdown
        markdown_content = html_to_markdown_chunked(html_content)
        md_size = len(markdown_content)
        
        if md_size == 0:
            print(f"    ⚠ Markdown rỗng, sử dụng placeholder")
            markdown_content = f"[Nội dung đề mục: {file_info['de_muc_name']}]"
            md_size = len(markdown_content)
        
        # Tạo ID
        record_id = f"md_{uuid.replace('-', '')[:30]}"
        
        # Strategy: Chỉ insert markdown, không insert HTML gốc để giảm kích thước
        print(f"    Inserting markdown ({md_size:,} bytes)...")
        
        cursor.execute("""
            INSERT INTO de_muc_markdown 
            (id, de_muc_id, file_name, markdown_content, html_content, content_size)
            VALUES (%s, %s, %s, %s, NULL, %s)
        """, (
            record_id, 
            de_muc_id, 
            file_name, 
            markdown_content, 
            md_size
        ))
        
        connection.commit()
        cursor.close()
        
        compression_rate = (md_size / html_size * 100) if html_size > 0 else 0
        print(f"    ✓ Đã import, compression: {compression_rate:.1f}%")
        return True
        
    except Error as e:
        cursor.close()
        
        if attempt < max_attempts:
            error_msg = str(e)
            print(f"    ✗ Lỗi (attempt {attempt}/{max_attempts}): {error_msg}")
            
            # Wait và retry
            wait_time = 5 * attempt  # Exponential backoff
            print(f"    Đang chờ {wait_time} giây trước khi retry...")
            time.sleep(wait_time)
            
            # Reconnect và retry
            connection.reconnect(attempts=3, delay=3)
            return import_file(connection, file_info, attempt + 1, max_attempts)
        else:
            print(f"    ✗ Failed after {max_attempts} attempts: {e}")
            return False
    
    except Exception as e:
        cursor.close()
        print(f"    ✗ Unexpected error: {e}")
        return False

def main():
    print("=== IMPORT 11 FILES CUỐI CÙNG ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    # Kết nối database
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✓ Kết nối database thành công")
    except Error as e:
        print(f"✗ Lỗi kết nối: {e}")
        return
    
    try:
        # Lấy files còn lại
        remaining_files = get_remaining_files(connection)
        print(f"✓ Tìm thấy {len(remaining_files)} files cần import")
        
        if len(remaining_files) == 0:
            print("✓ Tất cả files đã được import!")
            return
        
        # Hiển thị thông tin files
        print("\n=== DANH SÁCH FILES CÒN LẠI ===")
        for i, file_info in enumerate(remaining_files, 1):
            size_mb = file_info['html_size'] / 1024 / 1024
            print(f"{i:2d}. {file_info['de_muc_name']}")
            print(f"    File: {file_info['file_name']}")
            print(f"    Size: {file_info['html_size']:,} bytes ({size_mb:.2f} MB)")
        
        # Import từng file
        print(f"\n=== ĐANG IMPORT ===")
        imported = 0
        failed = 0
        
        for i, file_info in enumerate(remaining_files, 1):
            print(f"\n[{i}/{len(remaining_files)}] ", end="")
            
            success = import_file(connection, file_info)
            if success:
                imported += 1
            else:
                failed += 1
            
            # Chờ giữa các files để tránh overload
            if i < len(remaining_files):
                print(f"  Đang chờ 2 giây trước file tiếp theo...")
                time.sleep(2)
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Tổng files: {len(remaining_files)}")
        print(f"Đã import: {imported}")
        print(f"Failed: {failed}")
        
        # Kiểm tra tổng số records
        cursor = connection.cursor()
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
        
        if remaining == 0:
            print("🎉 HOÀN THÀNH 100% IMPORT!")
        
        cursor.close()
        
    except Exception as e:
        print(f"✗ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        connection.close()
        print("✓ Đã đóng kết nối database")
        print(f"Thời gian kết thúc: {datetime.now()}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Hoàn thành markdown conversion cho 166 đề mục còn lại
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
    """
    Convert HTML sang Markdown đơn giản, dễ đọc
    """
    if not html_content:
        return ""
    
    # Remove BOM và clean
    html_content = html_content.replace('\ufeff', '')
    
    # Extract main content từ div._content
    content_match = re.search(r"<div class='_content'>(.*?)</div>", html_content, re.DOTALL)
    if content_match:
        html_content = content_match.group(1)
    
    # Remove script và style tags
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
    
    # Convert các thẻ HTML sang Markdown
    markdown = html_content
    
    # Headers
    markdown = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n\n', markdown)
    markdown = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n', markdown)
    markdown = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n', markdown)
    markdown = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n', markdown)
    
    # Paragraphs với class đặc biệt
    markdown = re.sub(r'<p class="pChuong"[^>]*>(.*?)</p>', r'### \1\n\n', markdown)
    markdown = re.sub(r'<p class="pDieu"[^>]*>(.*?)</p>', r'#### \1\n\n', markdown)
    markdown = re.sub(r'<p class="pNoiDung"[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    markdown = re.sub(r'<p class="pKhoan"[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    markdown = re.sub(r'<p class="pDiem"[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    
    # General paragraphs
    markdown = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    
    # Lists
    markdown = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', markdown)
    markdown = re.sub(r'<ul[^>]*>', '', markdown)
    markdown = re.sub(r'</ul>', '\n', markdown)
    markdown = re.sub(r'<ol[^>]*>', '', markdown)
    markdown = re.sub(r'</ol>', '\n', markdown)
    
    # Links
    markdown = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', markdown)
    
    # Bold/Strong
    markdown = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', markdown)
    markdown = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', markdown)
    
    # Italic/Emphasis
    markdown = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', markdown)
    markdown = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', markdown)
    
    # Remove remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)
    
    # Clean up whitespace
    markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
    markdown = re.sub(r'[ \t]+', ' ', markdown)
    markdown = markdown.strip()
    
    return markdown

def get_remaining_demuc_files(connection):
    """
    Lấy danh sách files chưa được convert sang markdown
    """
    cursor = connection.cursor()
    
    # Lấy tất cả files từ de_muc_content
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
    
    remaining_files = []
    for row in cursor.fetchall():
        uuid, de_muc_id, de_muc_name, file_name, html_content = row
        remaining_files.append({
            'uuid': uuid,
            'de_muc_id': de_muc_id,
            'de_muc_name': de_muc_name,
            'file_name': file_name,
            'html_content': html_content
        })
    
    cursor.close()
    return remaining_files

def convert_and_import_batch(connection, files_batch, batch_num, total_batches):
    """Convert và import một batch files"""
    cursor = connection.cursor()
    converted = 0
    errors = 0
    
    print(f"\n=== BATCH {batch_num}/{total_batches} ({len(files_batch)} files) ===")
    
    for file_idx, file_info in enumerate(files_batch, 1):
        uuid = file_info['uuid']
        de_muc_id = file_info['de_muc_id']
        de_muc_name = file_info['de_muc_name']
        file_name = file_info['file_name']
        html_content = file_info['html_content']
        
        try:
            # Convert HTML sang Markdown
            markdown_content = html_to_markdown_simple(html_content)
            
            # Tạo ID cho record
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
            
            # Progress indicator mỗi 10 files
            if converted % 10 == 0:
                print(f"  Đã convert {converted}/{len(files_batch)} file trong batch này")
                
        except Exception as e:
            errors += 1
            print(f"  ✗ Lỗi convert file {file_name}: {e}")
    
    # Commit batch
    connection.commit()
    cursor.close()
    
    return converted, errors

def main():
    print("=== HOÀN THÀNH MARKDOWN CONVERSION ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    # Kết nối database
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✓ Kết nối database thành công")
    except Error as e:
        print(f"✗ Lỗi kết nối: {e}")
        return
    
    try:
        # Kiểm tra bảng markdown
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'de_muc_markdown'")
        if not cursor.fetchone():
            print("✗ Bảng de_muc_markdown chưa tồn tại")
            return
        
        # Lấy số records hiện có
        cursor.execute("SELECT COUNT(*) FROM de_muc_markdown")
        current_count = cursor.fetchone()[0]
        print(f"✓ Hiện có {current_count} records trong de_muc_markdown")
        
        # Lấy danh sách files cần convert
        print("Đang lấy danh sách files cần convert...")
        remaining_files = get_remaining_demuc_files(connection)
        print(f"  ✓ Còn {len(remaining_files)} files cần convert")
        
        if len(remaining_files) == 0:
            print("✓ Tất cả files đã được convert!")
            return
        
        # Chia thành batch (20 files mỗi batch)
        batch_size = 20
        batches = [remaining_files[i:i + batch_size] for i in range(0, len(remaining_files), batch_size)]
        total_batches = len(batches)
        
        total_converted = 0
        total_errors = 0
        
        # Process từng batch
        for batch_num, batch_files in enumerate(batches, 1):
            converted, errors = convert_and_import_batch(connection, batch_files, batch_num, total_batches)
            total_converted += converted
            total_errors += errors
            
            print(f"  Batch {batch_num} hoàn thành: {converted} converted, {errors} errors")
            
            # Pause giữa các batch để tránh overload
            if batch_num < total_batches:
                print(f"  Đang chờ 2 giây trước batch tiếp theo...")
                import time
                time.sleep(2)
        
        print(f"\n=== KẾT QUẢ TỔNG ===")
        print(f"Tổng files cần convert: {len(remaining_files)}")
        print(f"Đã convert: {total_converted}")
        print(f"Lỗi: {total_errors}")
        
        # Kiểm tra tổng số records
        cursor.execute("SELECT COUNT(*) FROM de_muc_markdown")
        final_count = cursor.fetchone()[0]
        print(f"Tổng records trong de_muc_markdown: {final_count}")
        print(f"Đã thêm: {final_count - current_count} records mới")
        
        # Thống kê kích thước
        cursor.execute("""
            SELECT 
                SUM(LENGTH(markdown_content)) as total_md_size,
                SUM(LENGTH(html_content)) as total_html_size,
                COUNT(*) as total_files
            FROM de_muc_markdown
        """)
        stats = cursor.fetchone()
        print(f"\n=== THỐNG KÊ KÍCH THƯỚC ===")
        print(f"Tổng files: {stats[2]}")
        print(f"Tổng kích thước Markdown: {stats[0]:,} bytes ({stats[0]/1024/1024:.1f} MB)")
        print(f"Tổng kích thước HTML: {stats[1]:,} bytes ({stats[1]/1024/1024:.1f} MB)")
        
        # Kiểm tra coverage
        cursor.execute("SELECT COUNT(*) FROM de_muc")
        total_demuc = cursor.fetchone()[0]
        coverage = (final_count / total_demuc * 100) if total_demuc > 0 else 0
        print(f"\n=== COVERAGE ===")
        print(f"Tổng đề mục: {total_demuc}")
        print(f"Đã convert: {final_count}")
        print(f"Coverage: {coverage:.1f}%")
        
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
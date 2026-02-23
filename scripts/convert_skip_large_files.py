#!/usr/bin/env python3
"""
Convert files còn lại, skip files quá lớn
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

def main():
    print("=== CONVERT FILES CÒN LẠI (SKIP LARGE FILES) ===")
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
            ORDER BY LENGTH(dmc.html_content) ASC  -- Xử lý files nhỏ trước
        """)
        
        files = cursor.fetchall()
        print(f"✓ Tìm thấy {len(files)} files cần convert")
        
        if len(files) == 0:
            print("✓ Tất cả files đã được convert!")
            return
        
        converted = 0
        errors = 0
        skipped_large = 0
        
        # Convert từng file
        for i, (uuid, de_muc_id, de_muc_name, file_name, html_content) in enumerate(files, 1):
            try:
                # Kiểm tra kích thước HTML
                html_size = len(html_content)
                if html_size > 5 * 1024 * 1024:  # Skip files > 5MB
                    print(f"  ⚠ Skip file lớn: {file_name} ({html_size:,} bytes)")
                    skipped_large += 1
                    continue
                
                # Convert HTML sang Markdown
                markdown_content = html_to_markdown_simple(html_content)
                
                # Kiểm tra kích thước markdown
                md_size = len(markdown_content)
                if md_size == 0:
                    print(f"  ⚠ Markdown rỗng: {file_name}")
                    markdown_content = "[Nội dung rỗng hoặc lỗi conversion]"
                    md_size = len(markdown_content)
                
                # Tạo ID
                record_id = f"md_{uuid.replace('-', '')[:30]}"
                
                # Chỉ insert markdown content, không insert HTML gốc (để tránh packet too large)
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
                
                converted += 1
                
                # Commit mỗi 5 files
                if converted % 5 == 0:
                    connection.commit()
                    print(f"  Đã convert {converted}/{len(files)} files")
                    time.sleep(1)  # Chờ 1 giây
                    
            except Error as e:
                if "max_allowed_packet" in str(e):
                    print(f"  ⚠ Skip file quá lớn: {file_name} (max_allowed_packet)")
                    skipped_large += 1
                else:
                    errors += 1
                    print(f"  ✗ Lỗi convert file {file_name}: {e}")
            except Exception as e:
                errors += 1
                print(f"  ✗ Lỗi convert file {file_name}: {e}")
        
        # Commit cuối
        connection.commit()
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Tổng files: {len(files)}")
        print(f"Đã convert: {converted}")
        print(f"Skipped (quá lớn): {skipped_large}")
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
        
        # Thống kê files lớn
        if skipped_large > 0:
            print(f"\n=== FILES LỚN ĐÃ SKIP ===")
            print(f"Tổng files lớn (>5MB): {skipped_large}")
            print(f"Giải pháp: Cần tăng max_allowed_packet trên MySQL server")
        
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
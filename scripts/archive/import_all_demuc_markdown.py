#!/usr/bin/env python3
"""
Import toàn bộ nội dung đề mục từ thư mục demuc và convert HTML sang Markdown
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

def get_demuc_mapping(connection):
    """Lấy mapping giữa value (UUID) và id trong database"""
    cursor = connection.cursor()
    cursor.execute("SELECT value, id, text FROM de_muc")
    mapping = {row[0]: {'id': row[1], 'name': row[2]} for row in cursor.fetchall()}
    cursor.close()
    return mapping

def import_all_demuc_markdown(connection, demuc_mapping):
    """Import toàn bộ nội dung từ thư mục demuc và convert sang Markdown"""
    demuc_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/demuc'
    
    if not os.path.exists(demuc_dir):
        print(f"✗ Thư mục không tồn tại: {demuc_dir}")
        return 0, 0
    
    files = [f for f in os.listdir(demuc_dir) if f.endswith('.html')]
    print(f"Tìm thấy {len(files)} file HTML trong thư mục demuc")
    
    cursor = connection.cursor()
    imported = 0
    errors = 0
    
    # Tạo bảng mới nếu chưa có
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS de_muc_markdown (
            id VARCHAR(50) PRIMARY KEY,
            de_muc_id VARCHAR(36) NOT NULL,
            file_name VARCHAR(255),
            markdown_content LONGTEXT,
            html_content LONGTEXT,
            content_size INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (de_muc_id) REFERENCES de_muc(id) ON DELETE CASCADE,
            INDEX idx_de_muc_id (de_muc_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    """)
    connection.commit()
    
    for file_idx, file_name in enumerate(files, 1):
        # Extract UUID từ tên file (bỏ .html)
        uuid = file_name.replace('.html', '')
        
        if uuid in demuc_mapping:
            de_muc_info = demuc_mapping[uuid]
            de_muc_id = de_muc_info['id']
            de_muc_name = de_muc_info['name']
            file_path = os.path.join(demuc_dir, file_name)
            
            try:
                # Đọc nội dung file
                with open(file_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Convert HTML sang Markdown
                markdown_content = html_to_markdown_simple(html_content)
                
                # Tạo ID cho record
                record_id = f"md_{uuid.replace('-', '')[:30]}"
                
                # Insert vào database
                cursor.execute("""
                    INSERT INTO de_muc_markdown 
                    (id, de_muc_id, file_name, markdown_content, html_content, content_size)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                    markdown_content = VALUES(markdown_content),
                    html_content = VALUES(html_content),
                    content_size = VALUES(content_size)
                """, (
                    record_id, 
                    de_muc_id, 
                    file_name, 
                    markdown_content, 
                    html_content, 
                    len(markdown_content)
                ))
                
                imported += 1
                
                # Progress indicator
                if imported % 20 == 0:
                    print(f"  Đã import {imported}/{len(files)} file")
                    connection.commit()
                    
            except Exception as e:
                errors += 1
                print(f"  ✗ Lỗi import file {file_name}: {e}")
        else:
            errors += 1
            print(f"  ⚠ Không tìm thấy mapping cho UUID: {uuid}")
    
    # Commit batch cuối
    connection.commit()
    cursor.close()
    
    return imported, errors

def main():
    print("=== IMPORT TOÀN BỘ NỘI DUNG ĐỀ MỤC (MARKDOWN) ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    # Kết nối database
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✓ Kết nối database thành công")
    except Error as e:
        print(f"✗ Lỗi kết nối: {e}")
        return
    
    try:
        # Lấy mapping
        print("Đang lấy mapping đề mục...")
        demuc_mapping = get_demuc_mapping(connection)
        print(f"  ✓ Đã lấy {len(demuc_mapping)} mapping")
        
        # Import nội dung và convert sang Markdown
        print("Đang import và convert sang Markdown...")
        imported, errors = import_all_demuc_markdown(connection, demuc_mapping)
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Tổng file: {len(demuc_mapping)}")
        print(f"Đã import: {imported}")
        print(f"Lỗi: {errors}")
        
        # Kiểm tra tổng số records
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM de_muc_markdown")
        total = cursor.fetchone()[0]
        print(f"Tổng records trong de_muc_markdown: {total}")
        
        # Sample data
        cursor.execute("""
            SELECT dmm.id, dm.text, dmm.file_name, 
                   LENGTH(dmm.markdown_content) as md_size,
                   LENGTH(dmm.html_content) as html_size
            FROM de_muc_markdown dmm 
            JOIN de_muc dm ON dmm.de_muc_id = dm.id 
            LIMIT 5
        """)
        print(f"\n=== 5 RECORDS ĐẦU TIÊN ===")
        for row in cursor.fetchall():
            print(f"  ID: {row[0]}, Đề mục: {row[1]}")
            print(f"    File: {row[2]}, Markdown: {row[3]:,} bytes, HTML: {row[4]:,} bytes")
        
        # Thống kê kích thước
        cursor.execute("""
            SELECT 
                SUM(LENGTH(markdown_content)) as total_md_size,
                SUM(LENGTH(html_content)) as total_html_size,
                AVG(LENGTH(markdown_content)) as avg_md_size,
                AVG(LENGTH(html_content)) as avg_html_size
            FROM de_muc_markdown
        """)
        stats = cursor.fetchone()
        print(f"\n=== THỐNG KÊ KÍCH THƯỚC ===")
        print(f"Tổng kích thước Markdown: {stats[0]:,} bytes ({stats[0]/1024/1024:.1f} MB)")
        print(f"Tổng kích thước HTML: {stats[1]:,} bytes ({stats[1]/1024/1024:.1f} MB)")
        print(f"Kích thước trung bình Markdown: {stats[2]:,.0f} bytes")
        print(f"Kích thước trung bình HTML: {stats[3]:,.0f} bytes")
        
        # So sánh với bảng cũ
        cursor.execute("SELECT COUNT(*) FROM de_muc_content")
        old_total = cursor.fetchone()[0]
        print(f"\n=== SO SÁNH VỚI BẢNG CŨ ===")
        print(f"de_muc_content (HTML): {old_total} records")
        print(f"de_muc_markdown (Markdown): {total} records")
        
        # Tạo view để dễ query
        cursor.execute("""
            CREATE OR REPLACE VIEW vw_de_muc_with_markdown AS
            SELECT 
                dm.id as de_muc_id,
                dm.text as de_muc_name,
                dm.stt,
                dm.chu_de_id,
                cd.text as chu_de_name,
                dmm.file_name,
                LENGTH(dmm.markdown_content) as markdown_size,
                LENGTH(dmm.html_content) as html_size,
                dmm.created_at,
                dmm.updated_at
            FROM de_muc dm
            LEFT JOIN chu_de cd ON dm.chu_de_id = cd.id
            LEFT JOIN de_muc_markdown dmm ON dm.id = dmm.de_muc_id
            ORDER BY CAST(cd.stt AS UNSIGNED), CAST(dm.stt AS UNSIGNED)
        """)
        connection.commit()
        print("✓ Đã tạo view vw_de_muc_with_markdown")
        
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
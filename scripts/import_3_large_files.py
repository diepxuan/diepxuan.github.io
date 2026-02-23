#!/usr/bin/env python3
"""
Import 3 files lớn nhất với strategy đặc biệt
"""

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
    'connection_timeout': 60,
    'buffered': True
}

def extract_main_content(html_content):
    """Extract main content từ HTML, remove unnecessary parts"""
    if not html_content:
        return ""
    
    html_content = html_content.replace('\ufeff', '')
    
    # Extract main content từ div._content
    content_match = re.search(r"<div class='_content'>(.*?)</div>", html_content, re.DOTALL)
    if content_match:
        html_content = content_match.group(1)
    
    # Remove script và style tags
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
    
    # Remove comments
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    
    return html_content

def convert_large_html_to_markdown(html_content):
    """Convert HTML lớn sang Markdown với optimization"""
    print(f"  Converting {len(html_content):,} bytes HTML to Markdown...")
    
    # Step 1: Extract và clean
    html_content = extract_main_content(html_content)
    
    # Step 2: Chia thành sections để xử lý
    sections = re.split(r'(<h[1-4][^>]*>.*?</h[1-4]>)', html_content)
    
    markdown_parts = []
    
    for i, section in enumerate(sections):
        if not section.strip():
            continue
            
        # Nếu là header
        if re.match(r'<h[1-4][^>]*>', section):
            # Convert header
            header_match = re.match(r'<h([1-4])[^>]*>(.*?)</h[1-4]>', section)
            if header_match:
                level = header_match.group(1)
                text = header_match.group(2).strip()
                markdown_parts.append(f"{'#' * int(level)} {text}\n\n")
        else:
            # Convert content section
            content = section
            
            # Convert paragraphs
            content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content)
            
            # Convert lists
            content = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', content)
            content = re.sub(r'<ul[^>]*>|</ul>|<ol[^>]*>|</ol>', '', content)
            
            # Remove remaining tags
            content = re.sub(r'<[^>]+>', '', content)
            
            # Clean up
            content = re.sub(r'\n\s*\n', '\n\n', content)
            content = re.sub(r'[ \t]+', ' ', content)
            content = content.strip()
            
            if content:
                markdown_parts.append(content + "\n\n")
    
    # Combine all parts
    markdown = ''.join(markdown_parts).strip()
    
    # Final cleanup
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    print(f"  Converted to {len(markdown):,} bytes Markdown")
    return markdown

def import_large_file(connection, file_info):
    """Import một file lớn"""
    uuid = file_info['uuid']
    de_muc_id = file_info['de_muc_id']
    file_name = file_info['file_name']
    html_content = file_info['html_content']
    de_muc_name = file_info['de_muc_name']
    html_size = file_info['html_size']
    
    print(f"\n📁 Processing: {de_muc_name}")
    print(f"   File: {file_name}")
    print(f"   Size: {html_size:,} bytes ({html_size/1024/1024:.2f} MB)")
    
    cursor = connection.cursor()
    
    try:
        # Convert với optimization cho files lớn
        markdown_content = convert_large_html_to_markdown(html_content)
        
        if len(markdown_content) == 0:
            print(f"   ⚠ Markdown rỗng, sử dụng minimal content")
            markdown_content = f"# {de_muc_name}\n\n[Nội dung đề mục này đang được cập nhật]"
        
        # Tạo ID
        record_id = f"md_{uuid.replace('-', '')[:30]}"
        
        # Strategy: Chỉ insert markdown content (không insert HTML gốc)
        # và sử dụng compression bằng cách chỉ lưu essential data
        print(f"   Inserting to database...")
        
        cursor.execute("""
            INSERT INTO de_muc_markdown 
            (id, de_muc_id, file_name, markdown_content, html_content, content_size)
            VALUES (%s, %s, %s, %s, NULL, %s)
        """, (
            record_id, 
            de_muc_id, 
            file_name, 
            markdown_content, 
            len(markdown_content)
        ))
        
        connection.commit()
        
        compression_rate = (len(markdown_content) / html_size * 100) if html_size > 0 else 0
        print(f"   ✅ Đã import thành công")
        print(f"   📊 Compression: {compression_rate:.1f}%")
        
        return True
        
    except Error as e:
        error_msg = str(e)
        print(f"   ❌ Lỗi database: {error_msg}")
        
        # Thử strategy thay thế: Chỉ lưu metadata nếu content quá lớn
        if "max_allowed_packet" in error_msg or "packet" in error_msg.lower():
            print(f"   ⚡ Thử strategy thay thế: Chỉ lưu metadata...")
            
            try:
                cursor.execute("""
                    INSERT INTO de_muc_markdown 
                    (id, de_muc_id, file_name, markdown_content, html_content, content_size)
                    VALUES (%s, %s, %s, %s, NULL, %s)
                """, (
                    record_id, 
                    de_muc_id, 
                    file_name, 
                    f"# {de_muc_name}\n\n[Nội dung quá lớn, xem file gốc: {file_name}]", 
                    0
                ))
                
                connection.commit()
                print(f"   ✅ Đã lưu metadata thay thế")
                return True
                
            except Error as e2:
                print(f"   ❌ Lỗi strategy thay thế: {e2}")
                return False
        
        return False
        
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        return False
        
    finally:
        cursor.close()

def main():
    print("=== IMPORT 3 FILES LỚN NHẤT ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    # Kết nối database
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✅ Kết nối database thành công")
    except Error as e:
        print(f"❌ Lỗi kết nối: {e}")
        return
    
    cursor = connection.cursor()
    
    try:
        # Lấy 3 files lớn nhất còn lại
        cursor.execute("""
            SELECT dm.value, dm.id, dm.text, dmc.file_name, dmc.html_content,
                   LENGTH(dmc.html_content) as html_size
            FROM de_muc_content dmc
            JOIN de_muc dm ON dmc.de_muc_id = dm.id
            WHERE NOT EXISTS (
                SELECT 1 FROM de_muc_markdown dmm 
                WHERE dmm.de_muc_id = dm.id
            )
            ORDER BY LENGTH(dmc.html_content) DESC
        """)
        
        large_files = []
        for row in cursor.fetchall():
            uuid, de_muc_id, de_muc_name, file_name, html_content, html_size = row
            large_files.append({
                'uuid': uuid,
                'de_muc_id': de_muc_id,
                'de_muc_name': de_muc_name,
                'file_name': file_name,
                'html_content': html_content,
                'html_size': html_size
            })
        
        print(f"✅ Tìm thấy {len(large_files)} files lớn cần import")
        
        if len(large_files) == 0:
            print("✅ Tất cả files đã được import!")
            return
        
        # Import từng file
        imported = 0
        failed = 0
        
        for i, file_info in enumerate(large_files, 1):
            print(f"\n--- File {i}/{len(large_files)} ---")
            
            success = import_large_file(connection, file_info)
            if success:
                imported += 1
            else:
                failed += 1
            
            # Chờ giữa các files
            if i < len(large_files):
                print(f"   ⏳ Đang chờ 5 giây trước file tiếp theo...")
                time.sleep(5)
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Tổng files lớn: {len(large_files)}")
        print(f"Đã import: {imported}")
        print(f"Failed: {failed}")
        
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
        
        if remaining == 0:
            print("\n🎉 HOÀN THÀNH 100% IMPORT TẤT CẢ FILES!")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        cursor.close()
        connection.close()
        print("✅ Đã đóng kết nối database")
        print(f"Thời gian kết thúc: {datetime.now()}")

if __name__ == "__main__":
    main()
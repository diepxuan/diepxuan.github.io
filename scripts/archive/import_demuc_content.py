#!/usr/bin/env python3
"""
Import nội dung HTML của đề mục từ thư mục demuc
"""

import os
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

def get_demuc_mapping(connection):
    """Lấy mapping giữa value (UUID) và id trong database"""
    cursor = connection.cursor()
    cursor.execute("SELECT value, id FROM de_muc")
    mapping = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.close()
    return mapping

def import_demuc_content(connection, demuc_mapping):
    """Import nội dung HTML từ thư mục demuc"""
    demuc_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/demuc'
    
    if not os.path.exists(demuc_dir):
        print(f"✗ Thư mục không tồn tại: {demuc_dir}")
        return 0
    
    files = [f for f in os.listdir(demuc_dir) if f.endswith('.html')]
    print(f"Tìm thấy {len(files)} file HTML trong thư mục demuc")
    
    cursor = connection.cursor()
    imported = 0
    errors = 0
    
    for file_name in files:
        # Extract UUID từ tên file (bỏ .html)
        uuid = file_name.replace('.html', '')
        
        if uuid in demuc_mapping:
            de_muc_id = demuc_mapping[uuid]
            file_path = os.path.join(demuc_dir, file_name)
            
            try:
                # Đọc nội dung file
                with open(file_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Tạo ID cho record
                record_id = f"dmc_{uuid.replace('-', '')[:32]}"
                
                # Insert vào database
                cursor.execute(
                    "INSERT INTO de_muc_content (id, de_muc_id, file_name, html_content, content_size) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE html_content = VALUES(html_content), content_size = VALUES(content_size)",
                    (record_id, de_muc_id, file_name, html_content, len(html_content))
                )
                
                imported += 1
                
                if imported % 50 == 0:
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
    print("=== IMPORT NỘI DUNG ĐỀ MỤC (demuc) ===")
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
        
        # Import nội dung
        print("Đang import nội dung HTML...")
        imported, errors = import_demuc_content(connection, demuc_mapping)
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Tổng file: {len(demuc_mapping)}")
        print(f"Đã import: {imported}")
        print(f"Lỗi: {errors}")
        
        # Kiểm tra tổng số records
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM de_muc_content")
        total = cursor.fetchone()[0]
        print(f"Tổng records trong de_muc_content: {total}")
        
        # Sample data
        cursor.execute("SELECT dmc.id, dm.text, dmc.file_name, dmc.content_size FROM de_muc_content dmc JOIN de_muc dm ON dmc.de_muc_id = dm.id LIMIT 5")
        print(f"\n=== 5 RECORDS ĐẦU TIÊN ===")
        for row in cursor.fetchall():
            print(f"  ID: {row[0]}, Đề mục: {row[1]}, File: {row[2]}, Size: {row[3]:,} bytes")
        
        cursor.close()
        
    except Exception as e:
        print(f"✗ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        connection.close()
        print("✓ Đã đóng kết nối database")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Import nội dung HTML đơn giản
"""

import os
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

def main():
    print("=== IMPORT NỘI DUNG ĐỀ MỤC ===")
    
    # Kết nối database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Lấy mapping
    cursor.execute("SELECT value, id FROM de_muc")
    mapping = {row[0]: row[1] for row in cursor.fetchall()}
    print(f"Đã lấy {len(mapping)} mapping")
    
    # Đếm file
    demuc_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/demuc'
    files = [f for f in os.listdir(demuc_dir) if f.endswith('.html')]
    print(f"Tổng file HTML: {len(files)}")
    
    # Import 10 file đầu tiên để test
    imported = 0
    for i, file_name in enumerate(files[:10]):
        uuid = file_name.replace('.html', '')
        
        if uuid in mapping:
            de_muc_id = mapping[uuid]
            file_path = os.path.join(demuc_dir, file_name)
            
            try:
                # Đọc file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read(50000)  # Chỉ đọc 50KB đầu
                
                # Insert
                record_id = f"dmc_{uuid.replace('-', '')[:32]}"
                cursor.execute(
                    "INSERT INTO de_muc_content (id, de_muc_id, file_name, html_content, content_size) VALUES (%s, %s, %s, %s, %s)",
                    (record_id, de_muc_id, file_name, content, len(content))
                )
                
                imported += 1
                print(f"  ✓ Đã import {file_name} ({len(content):,} bytes)")
                
            except Exception as e:
                print(f"  ✗ Lỗi {file_name}: {e}")
        else:
            print(f"  ⚠ Không có mapping: {uuid}")
    
    conn.commit()
    
    # Kiểm tra
    cursor.execute("SELECT COUNT(*) FROM de_muc_content")
    total = cursor.fetchone()[0]
    print(f"\nTổng records trong de_muc_content: {total}")
    
    cursor.close()
    conn.close()
    print("✓ Hoàn thành")

if __name__ == "__main__":
    main()
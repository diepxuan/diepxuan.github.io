#!/usr/bin/env python3
"""
Import bổ sung các đề mục thiếu content
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
    print("=== IMPORT BỔ SUNG ĐỀ MỤC THIẾU ===")
    
    # Các UUID thiếu
    missing_uuids = [
        'f5a43ce4-3b6e-4fc6-8c1e-eb7222d51d27',
        'ed278a00-f167-476a-8719-bffc8cb3a4c8',
        'e50cbcc9-5eb2-4a22-b6c4-2f08f2811fdb',
        '84a4b90e-6b07-41ca-919d-759cfb657f3f',
        '8b06986b-89cf-4a8d-8a2f-e14ff9e3123e',
        '6b4d44e7-dd9d-4879-bab2-c8c46de13d06'
    ]
    
    # Kết nối database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Lấy mapping
    cursor.execute("SELECT value, id FROM de_muc WHERE value IN (%s, %s, %s, %s, %s, %s)", tuple(missing_uuids))
    mapping = {row[0]: row[1] for row in cursor.fetchall()}
    print(f"Đã lấy {len(mapping)} mapping cho các UUID thiếu")
    
    # Import từng file
    demuc_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/demuc'
    imported = 0
    
    for uuid in missing_uuids:
        if uuid in mapping:
            de_muc_id = mapping[uuid]
            file_name = f"{uuid}.html"
            file_path = os.path.join(demuc_dir, file_name)
            
            if os.path.exists(file_path):
                try:
                    # Đọc file (giới hạn 10MB để tránh quá lớn)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read(10_000_000)  # 10MB max
                    
                    # Tạo ID
                    record_id = f"dmc_{uuid.replace('-', '')[:32]}"
                    
                    # Insert với ON DUPLICATE KEY UPDATE
                    cursor.execute(
                        "INSERT INTO de_muc_content (id, de_muc_id, file_name, html_content, content_size) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE html_content = VALUES(html_content), content_size = VALUES(content_size)",
                        (record_id, de_muc_id, file_name, content, len(content))
                    )
                    
                    imported += 1
                    print(f"  ✓ Đã import {file_name} ({len(content):,} bytes)")
                    
                except Exception as e:
                    print(f"  ✗ Lỗi {file_name}: {e}")
            else:
                print(f"  ⚠ File không tồn tại: {file_path}")
        else:
            print(f"  ⚠ Không có mapping cho UUID: {uuid}")
    
    conn.commit()
    
    # Kiểm tra lại
    cursor.execute("SELECT COUNT(*) FROM de_muc_content")
    total = cursor.fetchone()[0]
    print(f"\nTổng records trong de_muc_content: {total}")
    
    cursor.close()
    conn.close()
    print(f"✓ Đã import bổ sung {imported} đề mục")

if __name__ == "__main__":
    main()
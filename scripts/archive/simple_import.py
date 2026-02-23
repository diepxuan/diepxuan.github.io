#!/usr/bin/env python3
"""
Simple import script cho dữ liệu Pháp điển Điện tử
"""

import json
import mysql.connector
from mysql.connector import Error
import sys
from datetime import datetime

# Cấu hình database
DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

def parse_json_file(file_path):
    """Parse file JSON đơn giản"""
    print(f"Đang parse file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Tìm và parse từng biến
    data = {}
    
    # Parse jdChuDe
    start = content.find('var jdChuDe = [')
    if start != -1:
        start = content.find('[', start)
        end = find_matching_bracket(content, start)
        json_str = content[start:end+1]
        data['jdChuDe'] = json.loads(json_str)
        print(f"  ✓ jdChuDe: {len(data['jdChuDe'])} records")
    
    # Parse jdDeMuc
    start = content.find('var jdDeMuc = [')
    if start != -1:
        start = content.find('[', start)
        end = find_matching_bracket(content, start)
        json_str = content[start:end+1]
        data['jdDeMuc'] = json.loads(json_str)
        print(f"  ✓ jdDeMuc: {len(data['jdDeMuc'])} records")
    
    # Parse jdAllTree
    start = content.find('var jdAllTree = [')
    if start != -1:
        start = content.find('[', start)
        end = find_matching_bracket(content, start)
        json_str = content[start:end+1]
        data['jdAllTree'] = json.loads(json_str)
        print(f"  ✓ jdAllTree: {len(data['jdAllTree'])} records")
    
    return data

def find_matching_bracket(content, start_pos):
    """Tìm vị trí ']' tương ứng với '[' tại start_pos"""
    bracket_count = 0
    for i in range(start_pos, len(content)):
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                return i
    return len(content) - 1

def import_data(connection, data):
    """Import dữ liệu vào database"""
    cursor = connection.cursor()
    
    # Xóa dữ liệu cũ
    print("Đang xóa dữ liệu cũ...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE mapc_hierarchy")
    cursor.execute("TRUNCATE TABLE dieu_khoan")
    cursor.execute("TRUNCATE TABLE de_muc")
    cursor.execute("TRUNCATE TABLE chu_de")
    cursor.execute("TRUNCATE TABLE system_metadata")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    connection.commit()
    
    # Import chủ đề
    print("Đang import chủ đề...")
    chu_de_map = {}
    for item in data['jdChuDe']:
        record_id = item['Value'].replace('-', '')[:36]
        cursor.execute(
            "INSERT INTO chu_de (id, value, text, stt) VALUES (%s, %s, %s, %s)",
            (record_id, item['Value'], item['Text'], item['STT'])
        )
        chu_de_map[item['Value']] = record_id
    
    connection.commit()
    print(f"  ✓ Đã import {len(data['jdChuDe'])} chủ đề")
    
    # Import đề mục
    print("Đang import đề mục...")
    de_muc_map = {}
    for item in data['jdDeMuc']:
        record_id = item['Value'].replace('-', '')[:36]
        chu_de_id = chu_de_map.get(item['ChuDe'])
        if chu_de_id:
            cursor.execute(
                "INSERT INTO de_muc (id, value, text, chu_de_id, stt) VALUES (%s, %s, %s, %s, %s)",
                (record_id, item['Value'], item['Text'], chu_de_id, item['STT'])
            )
            de_muc_map[item['Value']] = record_id
    
    connection.commit()
    print(f"  ✓ Đã import {len(de_muc_map)} đề mục")
    
    # Import điều khoản
    print("Đang import điều khoản...")
    count = 0
    batch_size = 1000
    batch = []
    
    for item in data['jdAllTree']:
        if count % 10000 == 0 and count > 0:
            print(f"  Đã xử lý {count}/{len(data['jdAllTree'])} điều khoản")
        
        # Tạo ID unique từ MAPC và count (max 36 chars)
        mapc = item.get('MAPC', '')
        if mapc:
            # Sử dụng hash + count để đảm bảo unique
            import hashlib
            hash_obj = hashlib.md5(mapc.encode())
            record_id = f"dk_{hash_obj.hexdigest()[:24]}_{count:06d}"[:36]
        else:
            record_id = f"dk_{count:08d}"[:36]
        
        chu_de_id = chu_de_map.get(item.get('ChuDeID', ''))
        de_muc_id = de_muc_map.get(item.get('DeMucID', ''))
        
        if chu_de_id and de_muc_id:
            # Truncate mapc nếu quá dài (max 255)
            mapc_truncated = mapc[:255] if mapc else ''
            batch.append((
                record_id,
                item.get('ChiMuc', ''),
                mapc_truncated,
                item.get('TEN', ''),
                chu_de_id,
                de_muc_id
            ))
            
            if len(batch) >= batch_size:
                cursor.executemany(
                    "INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    batch
                )
                connection.commit()
                batch = []
        
        count += 1
    
    # Insert batch cuối
    if batch:
        cursor.executemany(
            "INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id) VALUES (%s, %s, %s, %s, %s, %s)",
            batch
        )
        connection.commit()
    
    print(f"  ✓ Đã import {count} điều khoản")
    
    # Cập nhật metadata
    cursor.execute(
        "INSERT INTO system_metadata (key_name, value, description) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE value = VALUES(value)",
        ('import_completed', datetime.now().isoformat(), 'Thời gian hoàn thành import')
    )
    connection.commit()
    
    cursor.close()
    return count

def main():
    """Main function"""
    print("=== PHÁP ĐIỂN ĐIỆN TỬ DATA IMPORT ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    # Parse dữ liệu
    file_path = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'
    data = parse_json_file(file_path)
    
    if not data:
        print("✗ Không có dữ liệu để import")
        sys.exit(1)
    
    # Kết nối database
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✓ Kết nối thành công đến database")
    except Error as e:
        print(f"✗ Lỗi kết nối database: {e}")
        sys.exit(1)
    
    try:
        # Import dữ liệu
        count = import_data(connection, data)
        
        print(f"\n=== HOÀN THÀNH ===")
        print(f"Thời gian kết thúc: {datetime.now()}")
        print(f"Tổng số điều khoản đã import: {count:,}")
        
    except Exception as e:
        print(f"✗ Lỗi trong quá trình import: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if connection.is_connected():
            connection.close()
            print("✓ Đã đóng kết nối database")

if __name__ == "__main__":
    main()
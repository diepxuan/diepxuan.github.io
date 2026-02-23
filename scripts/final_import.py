#!/usr/bin/env python3
"""
Final import script - đơn giản nhất
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

def parse_file():
    """Parse file JSON"""
    file_path = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'
    print(f"Đang parse file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
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
    """Tìm vị trí ']' tương ứng"""
    bracket_count = 0
    for i in range(start_pos, len(content)):
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                return i
    return len(content) - 1

def main():
    print("=== FINAL IMPORT ===")
    
    # Parse data
    data = parse_file()
    if not data:
        print("✗ Không có dữ liệu")
        return
    
    # Kết nối database
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("✓ Kết nối database thành công")
    except Error as e:
        print(f"✗ Lỗi kết nối: {e}")
        return
    
    try:
        # Xóa dữ liệu cũ
        print("Đang xóa dữ liệu cũ...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE mapc_hierarchy")
        cursor.execute("TRUNCATE TABLE dieu_khoan")
        cursor.execute("TRUNCATE TABLE de_muc")
        cursor.execute("TRUNCATE TABLE chu_de")
        cursor.execute("TRUNCATE TABLE system_metadata")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        conn.commit()
        
        # Import chủ đề
        print("Đang import chủ đề...")
        chu_de_map = {}
        for item in data['jdChuDe']:
            id_val = item['Value'].replace('-', '')[:36]
            cursor.execute(
                "INSERT INTO chu_de (id, value, text, stt) VALUES (%s, %s, %s, %s)",
                (id_val, item['Value'], item['Text'], item['STT'])
            )
            chu_de_map[item['Value']] = id_val
        conn.commit()
        print(f"  ✓ Đã import {len(data['jdChuDe'])} chủ đề")
        
        # Import đề mục
        print("Đang import đề mục...")
        de_muc_map = {}
        imported = 0
        for item in data['jdDeMuc']:
            id_val = item['Value'].replace('-', '')[:36]
            chu_de_id = chu_de_map.get(item['ChuDe'])
            if chu_de_id:
                cursor.execute(
                    "INSERT INTO de_muc (id, value, text, chu_de_id, stt) VALUES (%s, %s, %s, %s, %s)",
                    (id_val, item['Value'], item['Text'], chu_de_id, item['STT'])
                )
                de_muc_map[item['Value']] = id_val
                imported += 1
        conn.commit()
        print(f"  ✓ Đã import {imported} đề mục")
        
        # Import điều khoản
        print("Đang import điều khoản...")
        total = len(data['jdAllTree'])
        imported = 0
        errors = 0
        
        for idx, item in enumerate(data['jdAllTree']):
            if idx % 10000 == 0 and idx > 0:
                print(f"  Đã xử lý {idx}/{total} ({imported} imported, {errors} errors)")
            
            # Tạo ID đơn giản
            id_val = f"dk_{idx:08d}"
            
            chu_de_id = chu_de_map.get(item.get('ChuDeID', ''))
            de_muc_id = de_muc_map.get(item.get('DeMucID', ''))
            
            if chu_de_id and de_muc_id:
                try:
                    cursor.execute(
                        "INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id) VALUES (%s, %s, %s, %s, %s, %s)",
                        (
                            id_val,
                            item.get('ChiMuc', ''),
                            item.get('MAPC', '')[:255],
                            item.get('TEN', ''),
                            chu_de_id,
                            de_muc_id
                        )
                    )
                    imported += 1
                except Error as e:
                    errors += 1
                    # Bỏ qua lỗi, tiếp tục
                    pass
        
        conn.commit()
        print(f"  ✓ Đã import {imported} điều khoản")
        if errors > 0:
            print(f"  ⚠ Có {errors} lỗi")
        
        # Cập nhật metadata
        cursor.execute(
            "INSERT INTO system_metadata (key_name, value, description) VALUES (%s, %s, %s)",
            ('import_completed', datetime.now().isoformat(), 'Thời gian hoàn thành import')
        )
        conn.commit()
        
        print(f"\n=== HOÀN THÀNH ===")
        print(f"Tổng điều khoản đã import: {imported:,}")
        
    except Exception as e:
        print(f"✗ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()
        print("✓ Đã đóng kết nối")

if __name__ == "__main__":
    main()
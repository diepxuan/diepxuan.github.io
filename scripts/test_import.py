#!/usr/bin/env python3
"""
Test import với 1000 records đầu tiên
"""

import json
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

def test_parse():
    """Test parse 1000 records đầu tiên"""
    file_path = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read(500000)  # Đọc 500KB
    
    # Tìm jdAllTree
    start = content.find('var jdAllTree = [')
    if start == -1:
        print("Không tìm thấy jdAllTree")
        return []
    
    start = content.find('[', start)
    
    # Parse 1000 records đầu tiên
    records = []
    bracket_count = 0
    current_obj = ''
    in_string = False
    escape = False
    
    for i in range(start, len(content)):
        char = content[i]
        
        if escape:
            current_obj += char
            escape = False
            continue
            
        if char == '\\':
            escape = True
            current_obj += char
            continue
            
        if char == '"' and not escape:
            in_string = not in_string
            current_obj += char
            continue
            
        if not in_string:
            if char == '{':
                bracket_count += 1
                current_obj += char
            elif char == '}':
                bracket_count -= 1
                current_obj += char
                if bracket_count == 0:
                    # Kết thúc một object
                    try:
                        records.append(json.loads(current_obj))
                        current_obj = ''
                        if len(records) >= 1000:
                            break
                    except:
                        current_obj = ''
            elif char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0 and len(records) > 0:
                    break
            else:
                if bracket_count > 0:
                    current_obj += char
        else:
            current_obj += char
    
    print(f"Đã parse được {len(records)} records")
    if records:
        print(f"Sample record: {records[0]}")
        print(f"MAPC length: {len(records[0].get('MAPC', ''))}")
    
    return records

def main():
    print("=== TEST IMPORT 1000 RECORDS ===")
    
    # Parse data
    records = test_parse()
    if not records:
        print("Không có dữ liệu")
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
        # Lấy mapping
        cursor.execute("SELECT value, id FROM chu_de")
        chu_de_map = {row[0]: row[1] for row in cursor.fetchall()}
        
        cursor.execute("SELECT value, id FROM de_muc")
        de_muc_map = {row[0]: row[1] for row in cursor.fetchall()}
        
        print(f"Chu de map: {len(chu_de_map)}")
        print(f"De muc map: {len(de_muc_map)}")
        
        # Import thử 10 records đầu tiên
        imported = 0
        for idx, item in enumerate(records[:10]):
            print(f"\nRecord {idx}:")
            print(f"  MAPC: {item.get('MAPC')}")
            print(f"  ChuDeID: {item.get('ChuDeID')}")
            print(f"  DeMucID: {item.get('DeMucID')}")
            
            chu_de_id = chu_de_map.get(item.get('ChuDeID', ''))
            de_muc_id = de_muc_map.get(item.get('DeMucID', ''))
            
            print(f"  Found chu_de_id: {chu_de_id}")
            print(f"  Found de_muc_id: {de_muc_id}")
            
            if chu_de_id and de_muc_id:
                try:
                    cursor.execute(
                        "INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id) VALUES (%s, %s, %s, %s, %s, %s)",
                        (
                            f"test_{idx:04d}",
                            item.get('ChiMuc', ''),
                            item.get('MAPC', '')[:255],
                            item.get('TEN', ''),
                            chu_de_id,
                            de_muc_id
                        )
                    )
                    imported += 1
                    print(f"  ✓ Đã insert")
                except Error as e:
                    print(f"  ✗ Lỗi insert: {e}")
            else:
                print(f"  ⚠ Missing mapping")
        
        conn.commit()
        print(f"\n✓ Đã import {imported} records")
        
        # Kiểm tra
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan")
        count = cursor.fetchone()[0]
        print(f"Tổng records trong dieu_khoan: {count}")
        
    except Exception as e:
        print(f"✗ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Ultimate import script - xử lý file lớn
"""

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

def parse_and_import():
    """Parse và import trực tiếp từ file"""
    file_path = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'
    print(f"Đang xử lý file: {file_path}")
    
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
        
        # Parse và import từ file
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        print("Đang parse dữ liệu...")
        
        # Hàm parse một JSON array từ content
        def parse_array(var_name):
            start = content.find(f'var {var_name} = [')
            if start == -1:
                return []
            
            start = content.find('[', start)
            bracket_count = 0
            in_string = False
            escape = False
            json_str = ''
            
            for i in range(start, len(content)):
                char = content[i]
                
                if escape:
                    json_str += char
                    escape = False
                    continue
                
                if char == '\\':
                    escape = True
                    json_str += char
                    continue
                
                if char == '"' and not escape:
                    in_string = not in_string
                    json_str += char
                    continue
                
                json_str += char
                
                if not in_string:
                    if char == '[':
                        bracket_count += 1
                    elif char == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            break
            
            # Parse JSON
            import json
            try:
                return json.loads(json_str)
            except:
                # Thử fix trailing commas
                json_str = json_str.replace(',]', ']').replace(',}', '}')
                try:
                    return json.loads(json_str)
                except:
                    return []
        
        # Parse chủ đề
        print("Đang parse chủ đề...")
        chu_de_data = parse_array('jdChuDe')
        print(f"  ✓ Đã parse {len(chu_de_data)} chủ đề")
        
        # Import chủ đề
        chu_de_map = {}
        for item in chu_de_data:
            id_val = item['Value'].replace('-', '')[:36]
            cursor.execute(
                "INSERT INTO chu_de (id, value, text, stt) VALUES (%s, %s, %s, %s)",
                (id_val, item['Value'], item['Text'], item['STT'])
            )
            chu_de_map[item['Value']] = id_val
        conn.commit()
        
        # Parse đề mục
        print("Đang parse đề mục...")
        de_muc_data = parse_array('jdDeMuc')
        print(f"  ✓ Đã parse {len(de_muc_data)} đề mục")
        
        # Import đề mục
        de_muc_map = {}
        imported_dm = 0
        for item in de_muc_data:
            id_val = item['Value'].replace('-', '')[:36]
            chu_de_id = chu_de_map.get(item.get('ChuDe', ''))
            if chu_de_id:
                cursor.execute(
                    "INSERT INTO de_muc (id, value, text, chu_de_id, stt) VALUES (%s, %s, %s, %s, %s)",
                    (id_val, item['Value'], item['Text'], chu_de_id, item['STT'])
                )
                de_muc_map[item['Value']] = id_val
                imported_dm += 1
        conn.commit()
        print(f"  ✓ Đã import {imported_dm} đề mục")
        
        # Parse điều khoản
        print("Đang parse điều khoản...")
        dieu_khoan_data = parse_array('jdAllTree')
        print(f"  ✓ Đã parse {len(dieu_khoan_data)} điều khoản")
        
        # Import điều khoản
        print("Đang import điều khoản...")
        imported_dk = 0
        errors = 0
        batch_size = 1000
        batch = []
        
        for idx, item in enumerate(dieu_khoan_data):
            if idx % 10000 == 0 and idx > 0:
                print(f"  Đã xử lý {idx}/{len(dieu_khoan_data)}")
            
            id_val = f"dk_{idx:08d}"
            chu_de_id = chu_de_map.get(item.get('ChuDeID', ''))
            de_muc_id = de_muc_map.get(item.get('DeMucID', ''))
            
            if chu_de_id and de_muc_id:
                batch.append((
                    id_val,
                    item.get('ChiMuc', ''),
                    item.get('MAPC', '')[:255],
                    item.get('TEN', ''),
                    chu_de_id,
                    de_muc_id
                ))
                
                if len(batch) >= batch_size:
                    try:
                        cursor.executemany(
                            "INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id) VALUES (%s, %s, %s, %s, %s, %s)",
                            batch
                        )
                        conn.commit()
                        imported_dk += len(batch)
                        batch = []
                    except Error as e:
                        errors += len(batch)
                        batch = []
                        # Bỏ qua lỗi, tiếp tục
        
        # Insert batch cuối
        if batch:
            try:
                cursor.executemany(
                    "INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    batch
                )
                conn.commit()
                imported_dk += len(batch)
            except:
                errors += len(batch)
        
        print(f"  ✓ Đã import {imported_dk} điều khoản")
        if errors > 0:
            print(f"  ⚠ Có {errors} lỗi")
        
        # Cập nhật metadata
        cursor.execute(
            "INSERT INTO system_metadata (key_name, value, description) VALUES (%s, %s, %s)",
            ('import_completed', datetime.now().isoformat(), 'Thời gian hoàn thành import')
        )
        conn.commit()
        
        print(f"\n=== KẾT QUẢ ===")
        print(f"Chủ đề: {len(chu_de_data)}")
        print(f"Đề mục: {imported_dm}")
        print(f"Điều khoản: {imported_dk}")
        
    except Exception as e:
        print(f"✗ Lỗi: {e}")
        import traceback
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()
        print("✓ Đã đóng kết nối")

if __name__ == "__main__":
    parse_and_import()
#!/usr/bin/env python3
"""
Script import dữ liệu Pháp điển Điện tử vào MySQL database
Dữ liệu từ file jsonData.js (24MB) chứa 3 biến JSON
"""

import json
import re
import mysql.connector
from mysql.connector import Error
import os
import sys
from datetime import datetime
import time

# Cấu hình database
DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

# Đường dẫn đến file jsonData.js
JSON_FILE = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'

def parse_js_file(file_path):
    """Parse file JavaScript chứa JSON data"""
    print(f"Đang đọc file: {file_path}")
    
    # Import parser từ file riêng
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from parse_large_js import parse_large_js
    
    data = parse_large_js(file_path)
    
    if data:
        print(f"  ✓ Đã parse jdChuDe: {len(data.get('jdChuDe', []))} records")
        print(f"  ✓ Đã parse jdDeMuc: {len(data.get('jdDeMuc', []))} records")
        print(f"  ✓ Đã parse jdAllTree: {len(data.get('jdAllTree', []))} records")
    
    return data

def create_database_connection():
    """Tạo kết nối đến MySQL database"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print(f"✓ Kết nối thành công đến database: {DB_CONFIG['database']}")
            return connection
    except Error as e:
        print(f"✗ Lỗi kết nối database: {e}")
        sys.exit(1)

def create_tables(connection):
    """Tạo tables nếu chưa tồn tại"""
    cursor = connection.cursor()
    
    # Đọc file SQL
    sql_file = '/root/.openclaw/workspace/projects/github-io/scripts/create_phapdien_db_fixed.sql'
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_commands = f.read().split(';')
    
    for command in sql_commands:
        command = command.strip()
        if command and not command.startswith('--'):
            try:
                cursor.execute(command)
            except Error as e:
                print(f"  ⚠ Lỗi execute SQL: {e}")
                # Bỏ qua lỗi nếu table đã tồn tại
                if "already exists" not in str(e):
                    raise
    
    connection.commit()
    cursor.close()
    print("✓ Đã tạo/kiểm tra tables")

def parse_mapc_hierarchy(mapc):
    """Phân tích MAPC thành các cấp độ"""
    if len(mapc) != 20:
        return [None] * 10
    
    # MAPC dài 20 ký tự, phân tích thành 10 cấp độ (mỗi cấp 2 ký tự)
    levels = []
    for i in range(0, 20, 2):
        level = mapc[i:i+2]
        if level == '00':
            levels.append(None)
        else:
            levels.append(level)
    
    return levels

def import_chu_de(connection, data):
    """Import dữ liệu chủ đề"""
    cursor = connection.cursor()
    
    insert_sql = """
    INSERT INTO chu_de (id, value, text, stt)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    text = VALUES(text),
    stt = VALUES(stt),
    updated_at = CURRENT_TIMESTAMP
    """
    
    chu_de_list = data.get('jdChuDe', [])
    records = []
    
    for item in chu_de_list:
        # Tạo ID từ value hoặc tự generate
        record_id = item.get('Value', '').replace('-', '')[:36]
        if not record_id:
            record_id = f"chu_de_{item.get('STT', '0')}"
        
        records.append((
            record_id,
            item.get('Value', ''),
            item.get('Text', ''),
            item.get('STT', '')
        ))
    
    # Insert batch
    batch_size = 1000
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        cursor.executemany(insert_sql, batch)
        connection.commit()
        print(f"  Đã import {min(i+batch_size, len(records))}/{len(records)} chủ đề")
    
    cursor.close()
    print(f"✓ Đã import {len(records)} chủ đề")

def import_de_muc(connection, data):
    """Import dữ liệu đề mục"""
    cursor = connection.cursor()
    
    # Lấy mapping chu_de value -> id
    cursor.execute("SELECT value, id FROM chu_de")
    chu_de_map = {row[0]: row[1] for row in cursor.fetchall()}
    
    insert_sql = """
    INSERT INTO de_muc (id, value, text, chu_de_id, stt)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    text = VALUES(text),
    chu_de_id = VALUES(chu_de_id),
    stt = VALUES(stt),
    updated_at = CURRENT_TIMESTAMP
    """
    
    de_muc_list = data.get('jdDeMuc', [])
    records = []
    missing_chu_de = 0
    
    for item in de_muc_list:
        # Tạo ID từ value hoặc tự generate
        record_id = item.get('Value', '').replace('-', '')[:36]
        if not record_id:
            record_id = f"de_muc_{item.get('STT', '0')}"
        
        # Tìm chu_de_id tương ứng
        chu_de_value = item.get('ChuDe', '')
        chu_de_id = chu_de_map.get(chu_de_value)
        
        if not chu_de_id:
            missing_chu_de += 1
            continue
        
        records.append((
            record_id,
            item.get('Value', ''),
            item.get('Text', ''),
            chu_de_id,
            item.get('STT', '')
        ))
    
    # Insert batch
    batch_size = 1000
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        cursor.executemany(insert_sql, batch)
        connection.commit()
        print(f"  Đã import {min(i+batch_size, len(records))}/{len(records)} đề mục")
    
    cursor.close()
    if missing_chu_de > 0:
        print(f"⚠ {missing_chu_de} đề mục bị bỏ qua do không tìm thấy chủ đề")
    print(f"✓ Đã import {len(records)} đề mục")

def import_dieu_khoan(connection, data):
    """Import dữ liệu điều khoản"""
    cursor = connection.cursor()
    
    # Lấy mapping
    cursor.execute("SELECT value, id FROM chu_de")
    chu_de_map = {row[0]: row[1] for row in cursor.fetchall()}
    
    cursor.execute("SELECT value, id FROM de_muc")
    de_muc_map = {row[0]: row[1] for row in cursor.fetchall()}
    
    insert_sql = """
    INSERT INTO dieu_khoan (id, chi_muc, mapc, ten, chu_de_id, de_muc_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    chi_muc = VALUES(chi_muc),
    mapc = VALUES(mapc),
    ten = VALUES(ten),
    chu_de_id = VALUES(chu_de_id),
    de_muc_id = VALUES(de_muc_id),
    updated_at = CURRENT_TIMESTAMP
    """
    
    dieu_khoan_list = data.get('jdAllTree', [])
    records = []
    missing_chu_de = 0
    missing_de_muc = 0
    
    print(f"Đang xử lý {len(dieu_khoan_list)} điều khoản...")
    
    for idx, item in enumerate(dieu_khoan_list):
        # Tạo ID từ MAPC hoặc tự generate
        mapc = item.get('MAPC', '')
        record_id = f"dk_{mapc}" if mapc else f"dk_{idx}"
        
        # Tìm chu_de_id và de_muc_id
        chu_de_value = item.get('ChuDeID', '')
        de_muc_value = item.get('DeMucID', '')
        
        chu_de_id = chu_de_map.get(chu_de_value)
        de_muc_id = de_muc_map.get(de_muc_value)
        
        if not chu_de_id:
            missing_chu_de += 1
            continue
        
        if not de_muc_id:
            missing_de_muc += 1
            continue
        
        records.append((
            record_id,
            item.get('ChiMuc', ''),
            mapc,
            item.get('TEN', ''),
            chu_de_id,
            de_muc_id
        ))
        
        # Progress indicator
        if idx % 10000 == 0 and idx > 0:
            print(f"  Đã xử lý {idx}/{len(dieu_khoan_list)} điều khoản")
    
    # Insert batch
    batch_size = 5000
    total_inserted = 0
    
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        try:
            cursor.executemany(insert_sql, batch)
            connection.commit()
            total_inserted += len(batch)
            print(f"  Đã import {min(i+batch_size, len(records))}/{len(records)} điều khoản")
        except Error as e:
            print(f"  ✗ Lỗi insert batch {i}: {e}")
            connection.rollback()
            # Thử insert từng record
            for record in batch:
                try:
                    cursor.execute(insert_sql, record)
                except:
                    pass
            connection.commit()
    
    cursor.close()
    
    if missing_chu_de > 0:
        print(f"⚠ {missing_chu_de} điều khoản bị bỏ qua do không tìm thấy chủ đề")
    if missing_de_muc > 0:
        print(f"⚠ {missing_de_muc} điều khoản bị bỏ qua do không tìm thấy đề mục")
    
    print(f"✓ Đã import {total_inserted} điều khoản")
    return total_inserted

def import_mapc_hierarchy(connection):
    """Import phân cấp MAPC"""
    cursor = connection.cursor()
    
    # Lấy tất cả điều khoản
    cursor.execute("SELECT id, mapc FROM dieu_khoan")
    dieu_khoan_list = cursor.fetchall()
    
    insert_sql = """
    INSERT INTO mapc_hierarchy (mapc, level1, level2, level3, level4, level5, 
                               level6, level7, level8, level9, level10, dieu_khoan_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    dieu_khoan_id = VALUES(dieu_khoan_id)
    """
    
    records = []
    
    for dk_id, mapc in dieu_khoan_list:
        if len(mapc) == 20:
            levels = parse_mapc_hierarchy(mapc)
            records.append((mapc, *levels, dk_id))
    
    # Insert batch
    batch_size = 5000
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        cursor.executemany(insert_sql, batch)
        connection.commit()
        print(f"  Đã import {min(i+batch_size, len(records))}/{len(records)} phân cấp MAPC")
    
    cursor.close()
    print(f"✓ Đã import {len(records)} phân cấp MAPC")

def update_metadata(connection, stats):
    """Cập nhật metadata"""
    cursor = connection.cursor()
    
    update_sql = """
    INSERT INTO system_metadata (key_name, value, description)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE
    value = VALUES(value),
    updated_at = CURRENT_TIMESTAMP
    """
    
    metadata = [
        ('total_chu_de', str(stats['chu_de']), 'Tổng số chủ đề'),
        ('total_de_muc', str(stats['de_muc']), 'Tổng số đề mục'),
        ('total_dieu_khoan', str(stats['dieu_khoan']), 'Tổng số điều khoản'),
        ('import_completed', datetime.now().isoformat(), 'Thời gian hoàn thành import'),
        ('data_source', 'BoPhapDienDienTu/crawled', 'Nguồn dữ liệu')
    ]
    
    cursor.executemany(update_sql, metadata)
    connection.commit()
    cursor.close()
    print("✓ Đã cập nhật metadata")

def verify_import(connection):
    """Verify dữ liệu đã import"""
    cursor = connection.cursor()
    
    queries = [
        ("SELECT COUNT(*) FROM chu_de", "chủ đề"),
        ("SELECT COUNT(*) FROM de_muc", "đề mục"),
        ("SELECT COUNT(*) FROM dieu_khoan", "điều khoản"),
        ("SELECT COUNT(*) FROM mapc_hierarchy", "phân cấp MAPC")
    ]
    
    print("\n=== VERIFY IMPORT ===")
    for query, label in queries:
        cursor.execute(query)
        count = cursor.fetchone()[0]
        print(f"  {label}: {count:,}")
    
    # Kiểm tra sample data
    cursor.execute("SELECT mapc, ten FROM dieu_khoan LIMIT 5")
    print("\n=== SAMPLE DATA ===")
    for mapc, ten in cursor.fetchall():
        print(f"  {mapc}: {ten[:100]}...")
    
    cursor.close()

def main():
    """Main function"""
    print("=== PHÁP ĐIỂN ĐIỆN TỬ DATA IMPORT ===")
    print(f"Thời gian bắt đầu: {datetime.now()}")
    
    # Bước 1: Parse JSON data
    data = parse_js_file(JSON_FILE)
    
    if not data:
        print("✗ Không có dữ liệu để import")
        sys.exit(1)
    
    # Bước 2: Kết nối database
    connection = create_database_connection()
    
    try:
        # Bước 3: Import dữ liệu (tables đã được tạo)
        print("\n=== IMPORTING DATA ===")
        
        import_chu_de(connection, data)
        import_de_muc(connection, data)
        dieu_khoan_count = import_dieu_khoan(connection, data)
        import_mapc_hierarchy(connection)
        
        # Bước 5: Cập nhật metadata
        stats = {
            'chu_de': len(data.get('jdChuDe', [])),
            'de_muc': len(data.get('jdDeMuc', [])),
            'dieu_khoan': dieu_khoan_count
        }
        update_metadata(connection, stats)
        
        # Bước 6: Verify
        verify_import(connection)
        
        print(f"\n=== HOÀN THÀNH ===")
        print(f"Thời gian kết thúc: {datetime.now()}")
        print(f"Tổng số điều khoản đã import: {dieu_khoan_count:,}")
        
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
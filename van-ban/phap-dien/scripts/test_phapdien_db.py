#!/usr/bin/env python3
"""
Test thực tế database phapdien.db
Kiểm tra kết nối, query, và dữ liệu
"""

import sqlite3
import os
import sys
from pathlib import Path

def test_database_connection(db_path):
    """Test kết nối đến database"""
    print(f"🔗 Đang kết nối đến: {db_path}")
    
    if not os.path.exists(db_path):
        print(f"  ✗ Database không tồn tại: {db_path}")
        return False
    
    file_size = os.path.getsize(db_path) / (1024*1024)
    print(f"  ✓ Database tồn tại: {file_size:.2f} MB")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print(f"  ✓ Kết nối thành công")
        return conn, cursor
    except Exception as e:
        print(f"  ✗ Lỗi kết nối: {e}")
        return None, None

def test_table_counts(cursor):
    """Test số lượng records trong các tables"""
    print(f"\n📊 KIỂM TRA SỐ LƯỢNG RECORDS:")
    
    tables = ['chude', 'demuc', 'dieukhoan']
    expected_counts = {
        'chude': 45,
        'demuc': 306,
        'dieukhoan': 76303
    }
    
    all_ok = True
    
    for table in tables:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            expected = expected_counts.get(table, 0)
            
            if count == expected:
                print(f"  ✓ {table}: {count:,} records (đúng)")
            else:
                print(f"  ✗ {table}: {count:,} records (sai - mong đợi: {expected:,})")
                all_ok = False
                
        except Exception as e:
            print(f"  ✗ {table}: Lỗi query - {e}")
            all_ok = False
    
    return all_ok

def test_sample_queries(cursor):
    """Test các query mẫu"""
    print(f"\n🔍 KIỂM TRA QUERY MẪU:")
    
    queries = [
        ("SELECT * FROM chude LIMIT 3", "Lấy 3 chủ đề đầu tiên"),
        ("SELECT * FROM dieukhoan WHERE ten LIKE '%thông báo hàng hải%' LIMIT 2", "Tìm kiếm theo từ khóa"),
        ("SELECT c.text, COUNT(d.id) as count FROM chude c LEFT JOIN dieukhoan d ON c.id = d.chude_id GROUP BY c.id ORDER BY count DESC LIMIT 5", "Thống kê theo chủ đề")
    ]
    
    for sql, description in queries:
        print(f"\n  📝 {description}:")
        print(f"    SQL: {sql[:80]}...")
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            
            if results:
                print(f"    ✓ Trả về {len(results)} kết quả")
                for i, row in enumerate(results[:2]):  # Hiển thị 2 kết quả đầu
                    print(f"      {i+1}. {str(row)[:80]}...")
                if len(results) > 2:
                    print(f"      ... và {len(results)-2} kết quả khác")
            else:
                print(f"    ⚠️  Không có kết quả")
                
        except Exception as e:
            print(f"    ✗ Lỗi query: {e}")

def test_indexes(cursor):
    """Test indexes đã được tạo"""
    print(f"\n🔧 KIỂM TRA INDEXES:")
    
    try:
        cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='index' AND name LIKE 'idx_%'")
        indexes = cursor.fetchall()
        
        if indexes:
            print(f"  ✓ Tìm thấy {len(indexes)} indexes:")
            for name, sql in indexes:
                print(f"    • {name}")
        else:
            print(f"  ⚠️  Không tìm thấy indexes")
            
    except Exception as e:
        print(f"  ✗ Lỗi kiểm tra indexes: {e}")

def test_unique_ids(cursor):
    """Test xem tất cả IDs có unique không"""
    print(f"\n🎯 KIỂM TRA UNIQUE IDs:")
    
    try:
        # Kiểm tra dieukhoan table
        cursor.execute("SELECT COUNT(DISTINCT id) as unique_ids, COUNT(*) as total FROM dieukhoan")
        unique_ids, total = cursor.fetchone()
        
        if unique_ids == total:
            print(f"  ✓ dieukhoan: {unique_ids:,}/{total:,} IDs unique (100%)")
        else:
            print(f"  ✗ dieukhoan: {unique_ids:,}/{total:,} IDs unique (có trùng lặp)")
            return False
        
        # Kiểm tra duplicate mapc (có thể hợp lệ)
        cursor.execute("SELECT mapc, COUNT(*) as count FROM dieukhoan GROUP BY mapc HAVING count > 1 LIMIT 3")
        duplicates = cursor.fetchall()
        
        if duplicates:
            print(f"  ⚠️  Có {len(duplicates)} mapc bị trùng (có thể hợp lệ):")
            for mapc, count in duplicates[:3]:
                print(f"    • {mapc[:20]}...: {count} records")
        else:
            print(f"  ✓ Không có mapc trùng lặp")
            
        return True
        
    except Exception as e:
        print(f"  ✗ Lỗi kiểm tra unique IDs: {e}")
        return False

def compare_with_complete_db(main_db_path, complete_db_path):
    """So sánh với phapdien_complete.db"""
    print(f"\n📊 SO SÁNH VỚI phapdien_complete.db:")
    
    if not os.path.exists(complete_db_path):
        print(f"  ⚠️  phapdien_complete.db không tồn tại")
        return
    
    try:
        # Kết nối đến cả 2 databases
        conn_main = sqlite3.connect(main_db_path)
        conn_complete = sqlite3.connect(complete_db_path)
        
        cursor_main = conn_main.cursor()
        cursor_complete = conn_complete.cursor()
        
        # So sánh số lượng records
        tables = ['chude', 'demuc', 'dieukhoan']
        
        for table in tables:
            cursor_main.execute(f"SELECT COUNT(*) FROM {table}")
            count_main = cursor_main.fetchone()[0]
            
            cursor_complete.execute(f"SELECT COUNT(*) FROM {table}")
            count_complete = cursor_complete.fetchone()[0]
            
            if count_main == count_complete:
                print(f"  ✓ {table}: {count_main:,} records (giống nhau)")
            else:
                print(f"  ✗ {table}: main={count_main:,}, complete={count_complete:,} (khác nhau)")
        
        conn_main.close()
        conn_complete.close()
        
    except Exception as e:
        print(f"  ✗ Lỗi so sánh: {e}")

def main():
    base_dir = Path(__file__).parent.parent
    main_db = base_dir / "sqlite" / "phapdien.db"
    complete_db = base_dir / "sqlite" / "phapdien_complete.db"
    
    print("🚀 BẮT ĐẦU TEST DATABASE phapdien.db")
    print("=" * 60)
    
    # Test kết nối
    conn, cursor = test_database_connection(main_db)
    if not conn:
        return 1
    
    try:
        # Test các chức năng
        counts_ok = test_table_counts(cursor)
        test_sample_queries(cursor)
        test_indexes(cursor)
        ids_ok = test_unique_ids(cursor)
        
        # So sánh với complete db
        compare_with_complete_db(main_db, complete_db)
        
        print(f"\n" + "=" * 60)
        print("📈 KẾT QUẢ TỔNG HỢP:")
        
        if counts_ok and ids_ok:
            print("✅ DATABASE phapdien.db HOẠT ĐỘNG TỐT")
            print(f"   • Đầy đủ 76,303 điều khoản")
            print(f"   • Tất cả IDs unique")
            print(f"   • Indexes đã tạo")
            print(f"   • Sẵn sàng sử dụng")
            return 0
        else:
            print("❌ CÓ VẤN ĐỀ VỚI DATABASE")
            return 1
            
    finally:
        conn.close()
        print(f"\n🔒 Đã đóng kết nối database")

if __name__ == "__main__":
    sys.exit(main())
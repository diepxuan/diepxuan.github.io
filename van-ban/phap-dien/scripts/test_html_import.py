#!/usr/bin/env python3
"""
Test script để kiểm tra kết quả import HTML content
"""

import sqlite3
import os

def test_html_import():
    """Kiểm tra kết quả import HTML content"""
    
    db_path = "/root/.openclaw/workspace/projects/github-io/van-ban/phap-dien/sqlite/phapdien.db"
    
    if not os.path.exists(db_path):
        print("✗ Không tìm thấy database")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("=== KIỂM TRA KẾT QUẢ IMPORT HTML CONTENT ===")
        
        # 1. Kiểm tra table dieukhoan_content
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dieukhoan_content'")
        if not cursor.fetchone():
            print("✗ Table dieukhoan_content không tồn tại")
            return
        
        print("✓ Table dieukhoan_content đã được tạo")
        
        # 2. Kiểm tra số lượng records
        cursor.execute("SELECT COUNT(*) FROM dieukhoan_content")
        total_records = cursor.fetchone()[0]
        print(f"✓ Tổng số records trong dieukhoan_content: {total_records:,}")
        
        # 3. Kiểm tra schema
        cursor.execute("PRAGMA table_info(dieukhoan_content)")
        columns = cursor.fetchall()
        print("\nSchema của dieukhoan_content:")
        for col in columns:
            print(f"  {col[1]} ({col[2]}) - {'PRIMARY KEY' if col[5] else ''}")
        
        # 4. Kiểm tra sample data
        print("\nSample data (5 records đầu tiên):")
        cursor.execute("""
            SELECT id, dieukhoan_id, LENGTH(html_content) as html_len, 
                   LENGTH(markdown_content) as md_len, file_uuid
            FROM dieukhoan_content 
            LIMIT 5
        """)
        
        for row in cursor.fetchall():
            print(f"  ID: {row[0][:50]}...")
            print(f"    dieukhoan_id: {row[1]}")
            print(f"    HTML length: {row[2]:,} bytes")
            print(f"    Markdown length: {row[3]:,} bytes")
            print(f"    File UUID: {row[4]}")
            print()
        
        # 5. Thống kê theo file
        print("\nThống kê theo file (top 10):")
        cursor.execute('''
            SELECT file_uuid, COUNT(*) as count, 
                   SUM(LENGTH(html_content)) as total_html_size,
                   SUM(LENGTH(markdown_content)) as total_md_size
            FROM dieukhoan_content 
            GROUP BY file_uuid 
            ORDER BY count DESC
            LIMIT 10
        ''')
        
        for file_uuid, count, html_size, md_size in cursor.fetchall():
            print(f"  {file_uuid}:")
            print(f"    Số records: {count:,}")
            print(f"    Tổng HTML size: {html_size:,} bytes ({html_size/1024/1024:.2f} MB)")
            print(f"    Tổng Markdown size: {md_size:,} bytes ({md_size/1024/1024:.2f} MB)")
            print()
        
        # 6. Kiểm tra mapping với dieukhoan
        print("\nKiểm tra mapping với dieukhoan:")
        cursor.execute('''
            SELECT COUNT(DISTINCT dieukhoan_id) as unique_dieukhoan
            FROM dieukhoan_content
        ''')
        unique_dieukhoan = cursor.fetchone()[0]
        print(f"✓ Số dieukhoan unique có content: {unique_dieukhoan:,}")
        
        cursor.execute("SELECT COUNT(*) FROM dieukhoan")
        total_dieukhoan = cursor.fetchone()[0]
        print(f"✓ Tổng số dieukhoan trong database: {total_dieukhoan:,}")
        
        coverage = (unique_dieukhoan / total_dieukhoan * 100) if total_dieukhoan > 0 else 0
        print(f"✓ Coverage: {coverage:.1f}%")
        
        # 7. Kiểm tra content sample
        print("\nSample content (1 record):")
        cursor.execute('''
            SELECT d.id, d.ten, dc.raw_text
            FROM dieukhoan d
            JOIN dieukhoan_content dc ON d.id = dc.dieukhoan_id
            LIMIT 1
        ''')
        
        sample = cursor.fetchone()
        if sample:
            print(f"  ID: {sample[0]}")
            print(f"  Tên: {sample[1]}")
            print(f"  Content (first 200 chars): {sample[2][:200]}...")
        
        conn.close()
        
        print("\n✅ KIỂM TRA HOÀN TẤT")
        
    except Exception as e:
        print(f"✗ Lỗi kiểm tra: {e}")

if __name__ == "__main__":
    test_html_import()
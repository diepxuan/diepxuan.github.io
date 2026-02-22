#!/usr/bin/env python3
"""
Test build đơn giản với dữ liệu đã parse được
"""

import json
import sqlite3
from pathlib import Path
import shutil
from datetime import datetime

def main():
    base_dir = Path(__file__).parent.parent
    print(f"Base directory: {base_dir}")
    
    # Kiểm tra file parsed_entries.json
    parsed_file = base_dir / "output" / "parsed_entries.json"
    if not parsed_file.exists():
        print(f"File parsed_entries.json không tồn tại: {parsed_file}")
        return
    
    print(f"Đang đọc {parsed_file}...")
    with open(parsed_file, 'r', encoding='utf-8') as f:
        alltree_data = json.load(f)
    
    print(f"Đã đọc {len(alltree_data)} entries")
    
    # Đọc chủ đề và đề mục từ file gốc
    json_file = base_dir / "json" / "jsonData.js"
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    import re
    
    # Trích xuất jdChuDe
    pattern = r'var jdChuDe\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        pattern = r'var jdChuDe\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if match:
        chude_data = json.loads(match.group(1))
        print(f"Đã đọc {len(chude_data)} chủ đề")
    else:
        print("Không tìm thấy jdChuDe")
        chude_data = []
    
    # Trích xuất jdDeMuc
    pattern = r'var jdDeMuc\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        pattern = r'var jdDeMuc\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if match:
        demuc_data = json.loads(match.group(1))
        print(f"Đã đọc {len(demuc_data)} đề mục")
    else:
        print("Không tìm thấy jdDeMuc")
        demuc_data = []
    
    # Tạo SQLite database đơn giản
    sqlite_dir = base_dir / "sqlite"
    sqlite_dir.mkdir(exist_ok=True)
    
    db_path = sqlite_dir / "phapdien_simple.db"
    
    if db_path.exists():
        db_path.unlink()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Tạo bảng chủ đề
    cursor.execute('''
        CREATE TABLE chude (
            id TEXT PRIMARY KEY,
            ten TEXT NOT NULL,
            stt INTEGER
        )
    ''')
    
    # Tạo bảng đề mục
    cursor.execute('''
        CREATE TABLE demuc (
            id TEXT PRIMARY KEY,
            ten TEXT NOT NULL,
            chude_id TEXT NOT NULL,
            stt INTEGER
        )
    ''')
    
    # Tạo bảng điều khoản
    cursor.execute('''
        CREATE TABLE dieukhoan (
            id TEXT PRIMARY KEY,
            mapc TEXT,
            chimuc TEXT,
            ten TEXT NOT NULL,
            chude_id TEXT,
            demuc_id TEXT
        )
    ''')
    
    # Insert chủ đề
    for chude in chude_data:
        cursor.execute(
            'INSERT INTO chude (id, ten, stt) VALUES (?, ?, ?)',
            (chude['Value'], chude['Text'], int(chude['STT']) if chude['STT'].isdigit() else 0)
        )
    
    # Insert đề mục
    for demuc in demuc_data:
        cursor.execute(
            'INSERT INTO demuc (id, ten, chude_id, stt) VALUES (?, ?, ?, ?)',
            (demuc['Value'], demuc['Text'], demuc['ChuDe'], 
             int(demuc.get('STT', '0')) if demuc.get('STT', '0').isdigit() else 0)
        )
    
    # Insert điều khoản
    print(f"Đang insert {len(alltree_data)} điều khoản...")
    
    batch_size = 1000
    for i in range(0, len(alltree_data), batch_size):
        batch = alltree_data[i:i+batch_size]
        
        for entry in batch:
            cursor.execute('''
                INSERT INTO dieukhoan 
                (id, mapc, chimuc, ten, chude_id, demuc_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                entry.get('ID', ''),
                entry.get('MAPC', ''),
                entry.get('ChiMuc', ''),
                entry.get('TEN', ''),
                entry.get('ChuDeID', ''),
                entry.get('DeMucID', '')
            ))
        
        conn.commit()
        print(f"  Đã insert {min(i+batch_size, len(alltree_data))}/{len(alltree_data)}")
    
    # Tạo indexes
    cursor.execute('CREATE INDEX idx_dieukhoan_demuc ON dieukhoan(demuc_id)')
    cursor.execute('CREATE INDEX idx_dieukhoan_chude ON dieukhoan(chude_id)')
    
    conn.close()
    
    print(f"\n✓ Đã tạo SQLite database: {db_path}")
    print(f"  - {len(chude_data)} chủ đề")
    print(f"  - {len(demuc_data)} đề mục")
    print(f"  - {len(alltree_data)} điều khoản")
    
    # Tạo một vài file Markdown đơn giản
    markdown_dir = base_dir / "markdown_simple"
    if markdown_dir.exists():
        shutil.rmtree(markdown_dir)
    markdown_dir.mkdir(exist_ok=True)
    
    # Tạo file tổng hợp
    summary_file = markdown_dir / "README.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# BỘ PHÁP ĐIỂN ĐIỆN TỬ (PHIÊN BẢN ĐƠN GIẢN)\n\n")
        f.write(f"**Build date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Thống kê:**\n")
        f.write(f"- Chủ đề: {len(chude_data)}\n")
        f.write(f"- Đề mục: {len(demuc_data)}\n")
        f.write(f"- Điều khoản: {len(alltree_data)}\n\n")
        f.write(f"**Database:** `{db_path.relative_to(base_dir)}`\n\n")
        f.write(f"**Ghi chú:** Đây là phiên bản đơn giản với {len(alltree_data)} entries đầu tiên.\n")
    
    print(f"\n✓ Đã tạo Markdown files trong {markdown_dir}")
    print(f"✓ Hoàn thành!")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Rebuild database với toàn bộ 76,303 entries từ advanced parser.
"""

import json
import sqlite3
import os
from typing import List, Dict, Any

def load_parsed_entries() -> List[Dict[str, Any]]:
    """Load entries từ file advanced_parsed_entries.json"""
    input_file = '../json/advanced_parsed_entries.json'
    print(f"Loading entries from {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        entries = json.load(f)
    
    print(f"Loaded {len(entries)} entries")
    return entries

def create_database(entries: List[Dict[str, Any]]):
    """Tạo SQLite database mới với toàn bộ entries"""
    
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs('../sqlite', exist_ok=True)
    
    # Kết nối database
    db_path = '../sqlite/phapdien_complete.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"Creating database at {db_path}")
    
    # Xóa tables cũ nếu tồn tại
    cursor.execute('DROP TABLE IF EXISTS chude')
    cursor.execute('DROP TABLE IF EXISTS demuc')
    cursor.execute('DROP TABLE IF EXISTS dieukhoan')
    
    # Tạo tables
    cursor.execute('''
        CREATE TABLE chude (
            id TEXT PRIMARY KEY,
            value TEXT,
            text TEXT,
            stt TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE demuc (
            id TEXT PRIMARY KEY,
            value TEXT,
            text TEXT,
            stt TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE dieukhoan (
            id TEXT PRIMARY KEY,
            mapc TEXT,
            chimuc TEXT,
            ten TEXT,
            chude_id TEXT,
            demuc_id TEXT,
            FOREIGN KEY (chude_id) REFERENCES chude(id),
            FOREIGN KEY (demuc_id) REFERENCES demuc(id)
        )
    ''')
    
    # Tạo indexes
    cursor.execute('CREATE INDEX idx_dieukhoan_chude ON dieukhoan(chude_id)')
    cursor.execute('CREATE INDEX idx_dieukhoan_demuc ON dieukhoan(demuc_id)')
    cursor.execute('CREATE INDEX idx_dieukhoan_mapc ON dieukhoan(mapc)')
    
    print("Tables created successfully")
    
    # Load chude và demuc từ file gốc
    print("\nLoading chude and demuc data...")
    
    with open('../json/jsonData.js', 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Parse jdChuDe
    chude_start = content.find('jdChuDe = [')
    if chude_start == -1:
        chude_start = content.find('jdChuDe:[')
    
    if chude_start != -1:
        array_start = content.find('[', chude_start)
        array_end = content.find(']', array_start)
        chude_array_text = content[array_start:array_end+1]
        
        try:
            chude_entries = json.loads(chude_array_text)
            print(f"Loaded {len(chude_entries)} chude entries")
            
            for entry in chude_entries:
                cursor.execute(
                    'INSERT INTO chude (id, value, text, stt) VALUES (?, ?, ?, ?)',
                    (entry.get('Value'), entry.get('Value'), entry.get('Text'), entry.get('STT'))
                )
            
            print(f"Inserted {len(chude_entries)} chude records")
        except json.JSONDecodeError as e:
            print(f"Error parsing jdChuDe: {e}")
    
    # Parse jdDeMuc
    demuc_start = content.find('jdDeMuc = [')
    if demuc_start == -1:
        demuc_start = content.find('jdDeMuc:[')
    
    if demuc_start != -1:
        array_start = content.find('[', demuc_start)
        array_end = content.find(']', array_start)
        demuc_array_text = content[array_start:array_end+1]
        
        try:
            demuc_entries = json.loads(demuc_array_text)
            print(f"Loaded {len(demuc_entries)} demuc entries")
            
            for entry in demuc_entries:
                cursor.execute(
                    'INSERT INTO demuc (id, value, text, stt) VALUES (?, ?, ?, ?)',
                    (entry.get('Value'), entry.get('Value'), entry.get('Text'), entry.get('STT'))
                )
            
            print(f"Inserted {len(demuc_entries)} demuc records")
        except json.JSONDecodeError as e:
            print(f"Error parsing jdDeMuc: {e}")
    
    # Insert dieukhoan entries
    print(f"\nInserting {len(entries)} dieukhoan entries...")
    
    batch_size = 1000
    for i in range(0, len(entries), batch_size):
        batch = entries[i:i+batch_size]
        
        for entry in batch:
            cursor.execute(
                'INSERT INTO dieukhoan (id, mapc, chimuc, ten, chude_id, demuc_id) VALUES (?, ?, ?, ?, ?, ?)',
                (
                    entry.get('ID'),
                    entry.get('MAPC'),
                    entry.get('ChiMuc'),
                    entry.get('TEN'),
                    entry.get('ChuDeID'),
                    entry.get('DeMucID')
                )
            )
        
        conn.commit()
        print(f"  Inserted {min(i+batch_size, len(entries))}/{len(entries)} entries")
    
    # Tạo full-text search index (FTS5)
    print("\nCreating full-text search index...")
    cursor.execute('DROP TABLE IF EXISTS dieukhoan_fts')
    cursor.execute('''
        CREATE VIRTUAL TABLE dieukhoan_fts USING fts5(
            id, ten, mapc, chimuc, chude_id, demuc_id,
            content='dieukhoan',
            content_rowid='rowid'
        )
    ''')
    
    cursor.execute('INSERT INTO dieukhoan_fts(dieukhoan_fts) VALUES("rebuild")')
    conn.commit()
    
    print("Full-text search index created")
    
    # Thống kê
    cursor.execute('SELECT COUNT(*) FROM dieukhoan')
    total = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM chude')
    total_chude = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM demuc')
    total_demuc = cursor.fetchone()[0]
    
    print(f"\nDatabase statistics:")
    print(f"  chude: {total_chude} records")
    print(f"  demuc: {total_demuc} records")
    print(f"  dieukhoan: {total} records")
    
    # Kiểm tra entry cụ thể
    target_id = 'AA4C41EB-CC02-4629-8077-3691D02E64F2'
    cursor.execute('SELECT * FROM dieukhoan WHERE id = ?', (target_id,))
    target_entry = cursor.fetchone()
    
    if target_entry:
        print(f"\n✓ Target entry found in database:")
        print(f"  ID: {target_entry[0]}")
        print(f"  TEN: {target_entry[3][:80]}...")
    else:
        print(f"\n✗ Target entry NOT found in database")
    
    conn.close()
    print(f"\nDatabase created successfully at {db_path}")
    
    return db_path

def export_markdown(entries: List[Dict[str, Any]]):
    """Export entries sang markdown format"""
    
    os.makedirs('../markdown_complete', exist_ok=True)
    
    print(f"\nExporting to markdown format...")
    
    # Nhóm entries theo chude_id
    entries_by_chude = {}
    for entry in entries:
        chude_id = entry.get('ChuDeID')
        if chude_id not in entries_by_chude:
            entries_by_chude[chude_id] = []
        entries_by_chude[chude_id].append(entry)
    
    print(f"Grouped entries into {len(entries_by_chude)} chude categories")
    
    # Export mỗi chude thành một file
    for chude_id, chude_entries in entries_by_chude.items():
        filename = f'../markdown_complete/chude_{chude_id}.md'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'# Chủ đề: {chude_id}\n\n')
            f.write(f'Tổng số điều khoản: {len(chude_entries)}\n\n')
            
            for entry in chude_entries:
                f.write(f'## {entry.get("TEN")}\n\n')
                f.write(f'- **ID**: {entry.get("ID")}\n')
                f.write(f'- **Mã phân cấp (MAPC)**: {entry.get("MAPC")}\n')
                f.write(f'- **Chỉ mục (ChiMuc)**: {entry.get("ChiMuc")}\n')
                f.write(f'- **Chủ đề ID**: {entry.get("ChuDeID")}\n')
                f.write(f'- **Đề mục ID**: {entry.get("DeMucID")}\n\n')
    
    print(f"Exported {len(entries_by_chude)} markdown files to ../markdown_complete/")

def main():
    print("=== REBUILD PHAP DIEN DATABASE ===\n")
    
    # Load entries
    entries = load_parsed_entries()
    
    # Tạo database
    db_path = create_database(entries)
    
    # Export markdown
    export_markdown(entries)
    
    print("\n=== REBUILD COMPLETE ===")
    print(f"Total entries processed: {len(entries)}")
    print(f"Database: {db_path}")
    print(f"Markdown files: ../markdown_complete/")

if __name__ == "__main__":
    main()
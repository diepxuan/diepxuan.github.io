#!/usr/bin/env python3
"""
Script sửa trang chính index.md để hiển thị đúng số đề mục
"""

import sqlite3
import os
import re

def slugify(text):
    """Chuyển text thành slug cho URL"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.replace('đ', 'd')
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    return text.strip('-')

def fix_main_index():
    # Đường dẫn
    db_path = 'sqlite/phapdien_complete.db'
    output_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    # Kết nối database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("=== SỬA TRANG CHÍNH INDEX.MD ===")
    
    # Lấy danh sách chủ đề với số đề mục thực tế
    cursor.execute('''
        SELECT c.id, c.text, c.stt, 
               COUNT(DISTINCT d.id) as demuc_count,
               COUNT(dk.id) as dieukhoan_count
        FROM chude c
        LEFT JOIN dieukhoan dk ON c.id = dk.chude_id
        LEFT JOIN demuc d ON dk.demuc_id = d.id
        GROUP BY c.id, c.text, c.stt
        ORDER BY c.stt
    ''')
    chude_list = cursor.fetchall()
    
    # Đọc nội dung file index.md hiện tại
    index_file = os.path.join(output_dir, 'index.md')
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm và thay thế phần danh sách chủ đề
    start_marker = "## 📋 Danh sách Chủ đề Pháp luật"
    end_marker = "## 🔍 Cách sử dụng"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Tạo phần nội dung mới
        new_section = """## 📋 Danh sách Chủ đề Pháp luật

Nhấp vào tên chủ đề để xem danh sách đề mục:

"""
        
        for i, (chude_id, chude_text, stt, demuc_count, dieukhoan_count) in enumerate(chude_list, 1):
            slug = slugify(chude_text)
            new_section += f"{i}. **[{chude_text}](chu-de/{slug}/)** - {demuc_count} đề mục ({dieukhoan_count:,} điều khoản)\n"
        
        new_section += "\n"
        
        # Thay thế phần cũ
        old_section = content[start_idx:end_idx]
        content = content.replace(old_section, new_section)
        
        # Ghi lại file
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Đã sửa trang chính: {index_file}")
        print(f"✓ Hiển thị đúng: {len(chude_list)} chủ đề với số đề mục thực tế")
        
        # Hiển thị thống kê
        total_demuc = sum(demuc_count for _, _, _, demuc_count, _ in chude_list)
        total_dieukhoan = sum(dieukhoan_count for _, _, _, _, dieukhoan_count in chude_list)
        print(f"✓ Tổng số đề mục: {total_demuc}")
        print(f"✓ Tổng số điều khoản: {total_dieukhoan:,}")
    
    conn.close()

if __name__ == '__main__':
    fix_main_index()
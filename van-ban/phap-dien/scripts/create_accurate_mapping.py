#!/usr/bin/env python3
"""
Tạo mapping chính xác từ database thực tế
"""

import os
import re
import json
import sqlite3

def get_database_mapping():
    """Lấy mapping từ database bằng cách phân tích dữ liệu thực tế"""
    db_path = '/root/.openclaw/workspace/projects/github-io/van-ban/phap-dien/sqlite/phapdien_complete.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Lấy tất cả chủ đề
    cursor.execute("SELECT id, text FROM chude ORDER BY stt")
    chude_data = {}
    for row in cursor.fetchall():
        chude_id, chude_name = row
        # Tạo slug từ tên
        slug = create_slug(chude_name)
        chude_data[chude_id] = {
            'name': chude_name,
            'slug': slug
        }
    
    # Lấy tất cả đề mục với chủ đề tương ứng
    cursor.execute("SELECT id, text, chude_id FROM demuc ORDER BY stt")
    mapping = {}
    
    for row in cursor.fetchall():
        demuc_id, demuc_name, chude_id = row
        demuc_slug = create_slug(demuc_name)
        
        if chude_id in chude_data:
            chude_info = chude_data[chude_id]
            mapping[demuc_slug] = {
                'chude_slug': chude_info['slug'],
                'chude_name': chude_info['name'],
                'demuc_name': demuc_name
            }
    
    conn.close()
    return mapping

def create_slug(text):
    """Tạo slug từ text tiếng Việt"""
    if not text:
        return ''
    
    # Chuyển thành chữ thường
    slug = text.lower()
    
    # Thay thế ký tự tiếng Việt
    vietnamese_map = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'đ': 'd',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
        ' ': '-', '_': '-', '.': '-', ',': '-', ';': '-', ':': '-',
        '!': '-', '?': '-', '(': '-', ')': '-', '[': '-', ']': '-',
        '/': '-', '\\': '-', '@': '-', '#': '-', '$': '-', '%': '-',
        '^': '-', '&': '-', '*': '-', '+': '-', '=': '-', '|': '-',
        '~': '-', '`': '-', '"': '-', "'": '-', '<': '-', '>': '-'
    }
    
    for old, new in vietnamese_map.items():
        slug = slug.replace(old, new)
    
    # Xóa các ký tự không hợp lệ
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    
    # Xóa dấu gạch ngang liên tiếp
    slug = re.sub(r'\-+', '-', slug)
    
    # Xóa dấu gạch ngang ở đầu và cuối
    slug = slug.strip('-')
    
    return slug

def verify_mapping_with_files(mapping):
    """Verify mapping với files hiện có"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    
    # Lấy danh sách files thực tế
    chu_de_files = [f.replace('.md', '') for f in os.listdir(os.path.join(base_dir, 'chu-de')) if f.endswith('.md')]
    de_muc_files = [f.replace('.md', '') for f in os.listdir(os.path.join(base_dir, 'de-muc')) if f.endswith('.md')]
    
    print(f"Topic files: {len(chu_de_files)}")
    print(f"Subtopic files: {len(de_muc_files)}")
    
    # Check mapping coverage
    mapped_demucs = set(mapping.keys())
    actual_demucs = set(de_muc_files)
    
    missing_in_mapping = actual_demucs - mapped_demucs
    extra_in_mapping = mapped_demucs - actual_demucs
    
    print(f"\nMapping coverage:")
    print(f"  Mapped subtopics: {len(mapped_demucs)}")
    print(f"  Actual subtopics: {len(actual_demucs)}")
    print(f"  Missing in mapping: {len(missing_in_mapping)}")
    print(f"  Extra in mapping: {len(extra_in_mapping)}")
    
    if missing_in_mapping:
        print(f"\nFirst 10 missing subtopics:")
        for demuc in list(missing_in_mapping)[:10]:
            print(f"  - {demuc}")
    
    # Check topic coverage
    mapped_chudes = set(info['chude_slug'] for info in mapping.values())
    actual_chudes = set(chu_de_files)
    
    print(f"\nTopic coverage:")
    print(f"  Mapped topics: {len(mapped_chudes)}")
    print(f"  Actual topics: {len(actual_chudes)}")
    print(f"  Missing topics in mapping: {actual_chudes - mapped_chudes}")
    
    return mapping

def main():
    print("🔍 CREATING ACCURATE MAPPING FROM DATABASE")
    print("=" * 60)
    
    # Lấy mapping từ database
    mapping = get_database_mapping()
    print(f"✓ Loaded {len(mapping)} mappings from database")
    
    # Verify với files
    mapping = verify_mapping_with_files(mapping)
    
    # Lưu mapping
    output_file = '/root/.openclaw/workspace/projects/github-io/van-ban/accurate_mapping.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ MAPPING SAVED: {output_file}")
    
    # Hiển thị thống kê
    print(f"\n📊 MAPPING STATISTICS:")
    
    # Đếm subtopics per topic
    topic_counts = {}
    for demuc_slug, info in mapping.items():
        chude_slug = info['chude_slug']
        topic_counts[chude_slug] = topic_counts.get(chude_slug, 0) + 1
    
    print(f"\n📁 SUBTOPICS PER TOPIC:")
    for chude_slug, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {chude_slug}: {count} subtopics")
    
    print(f"\n🎯 READY FOR RESTRUCTURE")
    print(f"Use this mapping for accurate URL restructuring")

if __name__ == '__main__':
    main()
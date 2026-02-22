#!/usr/bin/env python3
"""
Tạo mapping chính xác từ database với relationships
"""

import os
import re
import json
import sqlite3

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

def get_final_mapping():
    """Lấy mapping chính xác từ database"""
    db_path = '/root/.openclaw/workspace/projects/github-io/van-ban/phap-dien/sqlite/phapdien_complete.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Lấy tất cả chủ đề
    cursor.execute("SELECT id, text FROM chude ORDER BY stt")
    chude_map = {}
    for row in cursor.fetchall():
        chude_id, chude_name = row
        chude_slug = create_slug(chude_name)
        chude_map[chude_id] = {
            'name': chude_name,
            'slug': chude_slug
        }
    
    # Lấy tất cả đề mục
    cursor.execute("SELECT id, text FROM demuc ORDER BY stt")
    demuc_map = {}
    for row in cursor.fetchall():
        demuc_id, demuc_name = row
        demuc_slug = create_slug(demuc_name)
        demuc_map[demuc_id] = {
            'name': demuc_name,
            'slug': demuc_slug
        }
    
    # Lấy relationships từ dieukhoan
    cursor.execute("""
        SELECT DISTINCT chude_id, demuc_id 
        FROM dieukhoan 
        WHERE chude_id IS NOT NULL AND demuc_id IS NOT NULL
        ORDER BY chude_id, demuc_id
    """)
    
    # Tạo mapping: demuc_slug → chude_slug
    mapping = {}
    relationships = cursor.fetchall()
    
    for chude_id, demuc_id in relationships:
        if chude_id in chude_map and demuc_id in demuc_map:
            chude_info = chude_map[chude_id]
            demuc_info = demuc_map[demuc_id]
            
            mapping[demuc_info['slug']] = {
                'chude_slug': chude_info['slug'],
                'chude_name': chude_info['name'],
                'demuc_name': demuc_info['name']
            }
    
    conn.close()
    return mapping

def verify_with_existing_files(mapping):
    """Verify mapping với files hiện có"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    
    # Lấy danh sách files thực tế
    chu_de_dir = os.path.join(base_dir, 'chu-de')
    de_muc_dir = os.path.join(base_dir, 'de-muc')
    
    if not os.path.exists(chu_de_dir) or not os.path.exists(de_muc_dir):
        print("Error: _pages directory structure not found")
        return mapping
    
    chu_de_files = [f.replace('.md', '') for f in os.listdir(chu_de_dir) if f.endswith('.md')]
    de_muc_files = [f.replace('.md', '') for f in os.listdir(de_muc_dir) if f.endswith('.md')]
    
    print(f"Found {len(chu_de_files)} topic files")
    print(f"Found {len(de_muc_files)} subtopic files")
    
    # Check coverage
    mapped_demucs = set(mapping.keys())
    actual_demucs = set(de_muc_files)
    
    missing = actual_demucs - mapped_demucs
    extra = mapped_demucs - actual_demucs
    
    print(f"\nMapping coverage:")
    print(f"  Mapped: {len(mapped_demucs)} subtopics")
    print(f"  Actual: {len(actual_demucs)} subtopics")
    print(f"  Missing: {len(missing)} subtopics")
    print(f"  Extra: {len(extra)} subtopics")
    
    if missing:
        print(f"\nFirst 10 missing subtopics:")
        for demuc in list(missing)[:10]:
            print(f"  - {demuc}")
    
    # Check topic coverage
    mapped_chudes = set(info['chude_slug'] for info in mapping.values())
    actual_chudes = set(chu_de_files)
    
    print(f"\nTopic coverage:")
    print(f"  Mapped topics: {len(mapped_chudes)}")
    print(f"  Actual topics: {len(actual_chudes)}")
    
    missing_topics = actual_chudes - mapped_chudes
    if missing_topics:
        print(f"  Missing topics: {missing_topics}")
    
    return mapping

def main():
    print("🎯 CREATING FINAL MAPPING FROM DATABASE")
    print("=" * 60)
    
    # Lấy mapping
    mapping = get_final_mapping()
    print(f"✓ Created mapping for {len(mapping)} subtopics")
    
    # Verify với files
    mapping = verify_with_existing_files(mapping)
    
    # Lưu mapping
    output_file = '/root/.openclaw/workspace/projects/github-io/van-ban/final_mapping.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ FINAL MAPPING SAVED: {output_file}")
    
    # Thống kê
    print(f"\n📊 MAPPING STATISTICS:")
    
    # Đếm subtopics per topic
    topic_counts = {}
    for demuc_slug, info in mapping.items():
        chude_slug = info['chude_slug']
        topic_counts[chude_slug] = topic_counts.get(chude_slug, 0) + 1
    
    print(f"\n📁 SUBTOPICS PER TOPIC (sorted by count):")
    for chude_slug, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {chude_slug}: {count} subtopics")
    
    print(f"\n🎯 READY FOR RESTRUCTURE")
    print(f"Total topics: {len(topic_counts)}")
    print(f"Total subtopics: {len(mapping)}")

if __name__ == '__main__':
    main()
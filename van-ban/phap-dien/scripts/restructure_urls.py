#!/usr/bin/env python3
"""
Restructure URLs từ:
- /van-ban/chu-de/<chude>/ → /van-ban/<chude>/
- /van-ban/de-muc/<demuc>/ → /van-ban/<chude>/<demuc>/

Dựa trên mapping từ database
"""

import os
import re
import sqlite3
import shutil
from pathlib import Path

def get_topic_subtopic_mapping():
    """Lấy mapping từ database: demuc_id → chude_slug"""
    db_path = '/root/.openclaw/workspace/projects/github-io/van-ban/phap-dien/sqlite/phapdien_complete.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Lấy mapping: demuc_slug → chude_slug
    cursor.execute("""
        SELECT 
            d.slug as demuc_slug,
            c.slug as chude_slug,
            c.name as chude_name,
            d.name as demuc_name
        FROM demuc d
        JOIN chude c ON d.chude_id = c.id
        ORDER BY c.slug, d.slug
    """)
    
    mapping = {}
    for row in cursor.fetchall():
        demuc_slug, chude_slug, chude_name, demuc_name = row
        mapping[demuc_slug] = {
            'chude_slug': chude_slug,
            'chude_name': chude_name,
            'demuc_name': demuc_name
        }
    
    conn.close()
    return mapping

def create_new_structure(mapping):
    """Tạo cấu trúc mới"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    backup_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages_backup'
    
    # Tạo backup
    print("1. Creating backup...")
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    shutil.copytree(base_dir, backup_dir)
    
    # Tạo thư mục mới
    new_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages_new'
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    
    os.makedirs(new_dir, exist_ok=True)
    
    print(f"2. Found {len(mapping)} subtopic mappings")
    
    # Copy và sửa topic files (chu-de/)
    chu_de_dir = os.path.join(base_dir, 'chu-de')
    chu_de_files = os.listdir(chu_de_dir)
    
    print(f"3. Processing {len(chu_de_files)} topic files...")
    
    for filename in chu_de_files:
        if not filename.endswith('.md'):
            continue
            
        old_path = os.path.join(chu_de_dir, filename)
        slug = filename.replace('.md', '')
        
        # Đọc file
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa permalink: /van-ban/chu-de/<slug>/ → /van-ban/<slug>/
        old_permalink = f'permalink: /van-ban/chu-de/{slug}/'
        new_permalink = f'permalink: /van-ban/{slug}/'
        content = content.replace(old_permalink, new_permalink)
        
        # Sửa internal links: /van-ban/de-muc/ → /van-ban/<chude>/
        # Cần mapping từ demuc_slug → chude_slug
        for demuc_slug, info in mapping.items():
            old_link = f'/van-ban/de-muc/{demuc_slug}/'
            new_link = f'/van-ban/{slug}/{demuc_slug}/'
            content = content.replace(old_link, new_link)
        
        # Lưu file mới (trực tiếp trong _pages/)
        new_path = os.path.join(new_dir, filename)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Copy và sửa subtopic files (de-muc/)
    de_muc_dir = os.path.join(base_dir, 'de-muc')
    de_muc_files = os.listdir(de_muc_dir)
    
    print(f"4. Processing {len(de_muc_files)} subtopic files...")
    
    processed = 0
    not_found = []
    
    for filename in de_muc_files:
        if not filename.endswith('.md'):
            continue
            
        old_path = os.path.join(de_muc_dir, filename)
        demuc_slug = filename.replace('.md', '')
        
        # Tìm chủ đề tương ứng
        if demuc_slug not in mapping:
            not_found.append(demuc_slug)
            continue
            
        info = mapping[demuc_slug]
        chude_slug = info['chude_slug']
        
        # Đọc file
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa permalink: /van-ban/de-muc/<demuc>/ → /van-ban/<chude>/<demuc>/
        old_permalink = f'permalink: /van-ban/de-muc/{demuc_slug}/'
        new_permalink = f'permalink: /van-ban/{chude_slug}/{demuc_slug}/'
        content = content.replace(old_permalink, new_permalink)
        
        # Sửa link về chủ đề: /van-ban/chu-de/<chude>/ → /van-ban/<chude>/
        old_chude_link = f'/van-ban/chu-de/{chude_slug}/'
        new_chude_link = f'/van-ban/{chude_slug}/'
        content = content.replace(old_chude_link, new_chude_link)
        
        # Tạo thư mục chủ đề nếu chưa có
        chude_new_dir = os.path.join(new_dir, chude_slug)
        os.makedirs(chude_new_dir, exist_ok=True)
        
        # Lưu file mới
        new_path = os.path.join(chude_new_dir, filename)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        processed += 1
    
    # Copy index.md
    index_file = os.path.join(base_dir, 'index.md')
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa links trong index: /van-ban/chu-de/ → /van-ban/
        content = re.sub(r'/van-ban/chu-de/([^)/]+)/', r'/van-ban/\1/', content)
        
        new_index_path = os.path.join(new_dir, 'index.md')
        with open(new_index_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"5. Processed {processed}/{len(de_muc_files)} subtopic files")
    
    if not_found:
        print(f"   Warning: {len(not_found)} subtopics not found in mapping")
        print(f"   First 5: {not_found[:5]}")
    
    return new_dir

def update_config():
    """Cập nhật _config.yml"""
    config_file = '/root/.openclaw/workspace/projects/github-io/van-ban/_config.yml'
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sửa collections configuration
    # Hiện tại: permalink: /van-ban/chu-de/:slug/
    # Mới: permalink: /van-ban/:slug/
    
    old_config = """  chu-de:
    output: true
    permalink: /van-ban/chu-de/:slug/
    
  de-muc:
    output: true
    permalink: /van-ban/de-muc/:slug/"""
    
    new_config = """  topics:
    output: true
    permalink: /van-ban/:slug/
    
  subtopics:
    output: true
    permalink: /van-ban/:parent/:slug/"""
    
    content = content.replace(old_config, new_config)
    
    # Sửa default permalink
    content = content.replace(
        'permalink: /van-ban/chu-de/:slug/',
        'permalink: /van-ban/:slug/'
    )
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("6. Updated _config.yml")

def create_redirects(mapping):
    """Tạo redirects cho URLs cũ"""
    redirects_file = '/root/.openclaw/workspace/projects/github-io/van-ban/_redirects_new'
    
    with open(redirects_file, 'w', encoding='utf-8') as f:
        f.write("# Redirects for restructured URLs\n")
        f.write("# Generated: " + str(os.path.getmtime(__file__)) + "\n\n")
        
        # Redirect topic pages
        f.write("# Topic pages\n")
        f.write("/van-ban/chu-de/* /van-ban/:splat 301\n\n")
        
        # Redirect subtopic pages
        f.write("# Subtopic pages\n")
        for demuc_slug, info in mapping.items():
            chude_slug = info['chude_slug']
            f.write(f"/van-ban/de-muc/{demuc_slug}/ /van-ban/{chude_slug}/{demuc_slug}/ 301\n")
        
        # Redirect wrong pattern (chu-de/de-muc/)
        f.write("\n# Wrong pattern redirect\n")
        f.write("/van-ban/chu-de/de-muc/* /van-ban/de-muc/:splat 301\n")
    
    print(f"7. Created redirects file: {redirects_file}")

def main():
    print("🚀 RESTRUCTURE URLs")
    print("=" * 60)
    print("Old: /van-ban/chu-de/<chude>/")
    print("New: /van-ban/<chude>/")
    print("")
    print("Old: /van-ban/de-muc/<demuc>/")
    print("New: /van-ban/<chude>/<demuc>/")
    print("=" * 60)
    
    # 1. Lấy mapping từ database
    mapping = get_topic_subtopic_mapping()
    print(f"✓ Loaded mapping for {len(mapping)} subtopics")
    
    # 2. Tạo cấu trúc mới
    new_dir = create_new_structure(mapping)
    
    # 3. Cập nhật config
    update_config()
    
    # 4. Tạo redirects
    create_redirects(mapping)
    
    print("\n" + "=" * 60)
    print("✅ RESTRUCTURE COMPLETE")
    print(f"New structure ready in: {new_dir}")
    print("\nNext steps:")
    print("1. Review new structure")
    print("2. Replace _pages/ with _pages_new/")
    print("3. Test URLs")
    print("4. Deploy redirects")

if __name__ == '__main__':
    main()
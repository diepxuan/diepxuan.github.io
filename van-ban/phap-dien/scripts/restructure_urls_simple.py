#!/usr/bin/env python3
"""
Restructure URLs đơn giản - dựa trên filenames hiện tại
"""

import os
import re
import shutil
import json

def extract_slug_from_permalink(content):
    """Trích xuất slug từ permalink trong front matter"""
    match = re.search(r'permalink:\s*(.+)', content)
    if match:
        permalink = match.group(1).strip()
        # Extract slug từ /van-ban/chu-de/<slug>/ hoặc /van-ban/de-muc/<slug>/
        parts = permalink.strip('/').split('/')
        if len(parts) >= 3:
            return parts[-2]  # Phần trước dấu / cuối
    return None

def get_chude_for_demuc(demuc_slug, chu_de_files):
    """Tìm chủ đề cho đề mục dựa trên nội dung file"""
    # Đọc file đề mục để tìm link đến chủ đề
    demuc_file = f'/root/.openclaw/workspace/projects/github-io/van-ban/_pages/de-muc/{demuc_slug}.md'
    
    if not os.path.exists(demuc_file):
        return None
    
    with open(demuc_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm link đến chủ đề trong nội dung
    # Pattern: /van-ban/chu-de/<chude_slug>/
    match = re.search(r'/van-ban/chu-de/([^)/]+)/', content)
    if match:
        return match.group(1)
    
    # Nếu không tìm thấy, thử tìm bằng cách so sánh tên
    # Ví dụ: "bao-hiem-y-te" → "bao-hiem"
    for chude_file in chu_de_files:
        chude_slug = chude_file.replace('.md', '')
        if demuc_slug.startswith(chude_slug):
            return chude_slug
    
    return None

def create_new_structure():
    """Tạo cấu trúc mới"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    new_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages_new'
    
    # Xóa thư mục cũ nếu tồn tại
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    os.makedirs(new_dir, exist_ok=True)
    
    print("1. Analyzing current structure...")
    
    # Lấy danh sách files
    chu_de_dir = os.path.join(base_dir, 'chu-de')
    de_muc_dir = os.path.join(base_dir, 'de-muc')
    
    chu_de_files = [f for f in os.listdir(chu_de_dir) if f.endswith('.md')]
    de_muc_files = [f for f in os.listdir(de_muc_dir) if f.endswith('.md')]
    
    print(f"   Found {len(chu_de_files)} topic files")
    print(f"   Found {len(de_muc_files)} subtopic files")
    
    # Tạo mapping demuc → chude
    mapping = {}
    
    print("2. Creating subtopic → topic mapping...")
    
    for demuc_file in de_muc_files:
        demuc_slug = demuc_file.replace('.md', '')
        chude_slug = get_chude_for_demuc(demuc_slug, chu_de_files)
        
        if chude_slug:
            mapping[demuc_slug] = chude_slug
        else:
            print(f"   Warning: Could not find topic for subtopic: {demuc_slug}")
            # Default to first topic if not found
            if chu_de_files:
                mapping[demuc_slug] = chu_de_files[0].replace('.md', '')
    
    print(f"   Created mapping for {len(mapping)} subtopics")
    
    # Xử lý topic files
    print("3. Processing topic files...")
    
    for chude_file in chu_de_files:
        chude_slug = chude_file.replace('.md', '')
        old_path = os.path.join(chu_de_dir, chude_file)
        
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa permalink: /van-ban/chu-de/<slug>/ → /van-ban/<slug>/
        old_permalink = f'permalink: /van-ban/chu-de/{chude_slug}/'
        new_permalink = f'permalink: /van-ban/{chude_slug}/'
        content = content.replace(old_permalink, new_permalink)
        
        # Sửa internal links: /van-ban/de-muc/<demuc>/ → /van-ban/<chude>/<demuc>/
        for demuc_slug, mapped_chude in mapping.items():
            if mapped_chude == chude_slug:
                old_link = f'/van-ban/de-muc/{demuc_slug}/'
                new_link = f'/van-ban/{chude_slug}/{demuc_slug}/'
                content = content.replace(old_link, new_link)
        
        # Lưu file mới
        new_path = os.path.join(new_dir, chude_file)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Xử lý subtopic files
    print("4. Processing subtopic files...")
    
    for demuc_file in de_muc_files:
        demuc_slug = demuc_file.replace('.md', '')
        old_path = os.path.join(de_muc_dir, demuc_file)
        
        # Lấy chủ đề từ mapping
        chude_slug = mapping.get(demuc_slug)
        if not chude_slug:
            print(f"   Skipping {demuc_slug} - no topic mapping")
            continue
        
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
        
        # Tạo thư mục chủ đề
        chude_dir = os.path.join(new_dir, chude_slug)
        os.makedirs(chude_dir, exist_ok=True)
        
        # Lưu file mới
        new_path = os.path.join(chude_dir, demuc_file)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Xử lý index.md
    print("5. Processing index.md...")
    
    index_file = os.path.join(base_dir, 'index.md')
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa links: /van-ban/chu-de/<chude>/ → /van-ban/<chude>/
        content = re.sub(r'/van-ban/chu-de/([^)/]+)/', r'/van-ban/\1/', content)
        
        new_index_path = os.path.join(new_dir, 'index.md')
        with open(new_index_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Lưu mapping để sử dụng sau
    mapping_file = os.path.join(new_dir, 'mapping.json')
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ NEW STRUCTURE CREATED")
    print(f"Location: {new_dir}")
    print(f"Mapping saved: {mapping_file}")
    
    # Hiển thị thống kê
    print(f"\n📊 STATISTICS:")
    print(f"  Topic files: {len(chu_de_files)}")
    print(f"  Subtopic files: {len(de_muc_files)}")
    
    # Đếm số subtopics per topic
    topic_counts = {}
    for demuc_slug, chude_slug in mapping.items():
        topic_counts[chude_slug] = topic_counts.get(chude_slug, 0) + 1
    
    print(f"\n📁 SUBTOPICS PER TOPIC:")
    for chude_slug, count in sorted(topic_counts.items()):
        print(f"  {chude_slug}: {count} subtopics")
    
    return new_dir, mapping

def update_config():
    """Cập nhật _config.yml cho cấu trúc mới"""
    config_file = '/root/.openclaw/workspace/projects/github-io/van-ban/_config.yml'
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm và sửa collections configuration
    # Tìm phần collections
    lines = content.split('\n')
    new_lines = []
    in_collections = False
    collections_processed = False
    
    for line in lines:
        if line.strip() == 'collections:' and not collections_processed:
            in_collections = True
            new_lines.append(line)
        elif in_collections and line.strip().startswith('  ') and not collections_processed:
            # Bỏ qua collections cũ
            if line.strip() in ['chu-de:', 'de-muc:']:
                continue
            elif line.strip() and not line.strip().startswith('  '):
                # Kết thúc collections
                in_collections = False
                collections_processed = True
                
                # Thêm collections mới
                new_lines.append('  topics:')
                new_lines.append('    output: true')
                new_lines.append('    permalink: /van-ban/:slug/')
                new_lines.append('')
                new_lines.append('  subtopics:')
                new_lines.append('    output: true')
                new_lines.append('    permalink: /van-ban/:parent/:slug/')
                new_lines.append('')
                new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    # Nếu chưa xử lý collections (không tìm thấy)
    if not collections_processed:
        # Thêm vào cuối file
        new_lines.append('')
        new_lines.append('collections:')
        new_lines.append('  topics:')
        new_lines.append('    output: true')
        new_lines.append('    permalink: /van-ban/:slug/')
        new_lines.append('')
        new_lines.append('  subtopics:')
        new_lines.append('    output: true')
        new_lines.append('    permalink: /van-ban/:parent/:slug/')
    
    new_content = '\n'.join(new_lines)
    
    # Backup config cũ
    backup_file = config_file + '.backup'
    shutil.copy2(config_file, backup_file)
    
    # Ghi config mới
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ UPDATED _config.yml")
    print(f"Backup saved: {backup_file}")

def main():
    print("🚀 RESTRUCTURE URLs - SIMPLE VERSION")
    print("=" * 60)
    print("Current: /van-ban/chu-de/<chude>/")
    print("New:     /van-ban/<chude>/")
    print("")
    print("Current: /van-ban/de-muc/<demuc>/")
    print("New:     /van-ban/<chude>/<demuc>/")
    print("=" * 60)
    
    # Tạo cấu trúc mới
    new_dir, mapping = create_new_structure()
    
    # Cập nhật config
    update_config()
    
    print("\n" + "=" * 60)
    print("✅ RESTRUCTURE COMPLETE")
    print(f"\nNext steps:")
    print(f"1. Review new structure in: {new_dir}")
    print(f"2. Replace _pages/ with _pages_new/")
    print(f"3. Test new URLs")
    print(f"4. Create redirects for old URLs")

if __name__ == '__main__':
    main()
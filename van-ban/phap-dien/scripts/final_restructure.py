#!/usr/bin/env python3
"""
Final restructure URLs với mapping chính xác
"""

import os
import re
import json
import shutil

def load_mapping():
    """Load mapping từ file"""
    mapping_file = '/root/.openclaw/workspace/projects/github-io/van-ban/final_mapping.json'
    with open(mapping_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def restructure_with_mapping(mapping):
    """Restructure với mapping chính xác"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    new_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages_restructured'
    
    # Xóa thư mục cũ nếu tồn tại
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    os.makedirs(new_dir, exist_ok=True)
    
    print("1. Loading mapping...")
    print(f"   Topics: {len(set(info['chude_slug'] for info in mapping.values()))}")
    print(f"   Subtopics: {len(mapping)}")
    
    # Xử lý topic files (chu-de/)
    chu_de_dir = os.path.join(base_dir, 'chu-de')
    chu_de_files = [f for f in os.listdir(chu_de_dir) if f.endswith('.md')]
    
    print(f"2. Processing {len(chu_de_files)} topic files...")
    
    for filename in chu_de_files:
        chude_slug = filename.replace('.md', '')
        old_path = os.path.join(chu_de_dir, filename)
        
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa permalink: /van-ban/chu-de/<slug>/ → /van-ban/<slug>/
        old_permalink = f'permalink: /van-ban/chu-de/{chude_slug}/'
        new_permalink = f'permalink: /van-ban/{chude_slug}/'
        content = content.replace(old_permalink, new_permalink)
        
        # Sửa internal links: /van-ban/de-muc/<demuc>/ → /van-ban/<chude>/<demuc>/
        for demuc_slug, info in mapping.items():
            if info['chude_slug'] == chude_slug:
                old_link = f'/van-ban/de-muc/{demuc_slug}/'
                new_link = f'/van-ban/{chude_slug}/{demuc_slug}/'
                content = content.replace(old_link, new_link)
        
        # Lưu file mới
        new_path = os.path.join(new_dir, filename)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Xử lý subtopic files (de-muc/)
    de_muc_dir = os.path.join(base_dir, 'de-muc')
    de_muc_files = [f for f in os.listdir(de_muc_dir) if f.endswith('.md')]
    
    print(f"3. Processing {len(de_muc_files)} subtopic files...")
    
    processed = 0
    errors = []
    
    for filename in de_muc_files:
        demuc_slug = filename.replace('.md', '')
        old_path = os.path.join(de_muc_dir, filename)
        
        # Kiểm tra mapping
        if demuc_slug not in mapping:
            errors.append(f"No mapping for: {demuc_slug}")
            continue
        
        info = mapping[demuc_slug]
        chude_slug = info['chude_slug']
        
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
        new_path = os.path.join(chude_dir, filename)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        processed += 1
    
    # Xử lý index.md
    print("4. Processing index.md...")
    
    index_file = os.path.join(base_dir, 'index.md')
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa links: /van-ban/chu-de/<chude>/ → /van-ban/<chude>/
        content = re.sub(r'/van-ban/chu-de/([^)/]+)/', r'/van-ban/\1/', content)
        
        new_index_path = os.path.join(new_dir, 'index.md')
        with open(new_index_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"5. Processed {processed}/{len(de_muc_files)} subtopic files")
    
    if errors:
        print(f"   Errors: {len(errors)}")
        for error in errors[:5]:
            print(f"     {error}")
    
    return new_dir

def update_config_for_new_structure():
    """Cập nhật _config.yml cho cấu trúc mới"""
    config_file = '/root/.openclaw/workspace/projects/github-io/van-ban/_config.yml'
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tạo config mới
    new_config = """# Jekyll configuration for van-ban
title: Bộ Pháp điển Điện tử
description: Hệ thống pháp luật chính thức của Việt Nam
baseurl: "/van-ban"
url: "https://docs.diepxuan.com"

# Build settings
markdown: kramdown
permalink: pretty

# Collections for new structure
collections:
  topics:
    output: true
    permalink: /van-ban/:slug/
  
  subtopics:
    output: true
    permalink: /van-ban/:parent/:slug/

# Defaults
defaults:
  - scope:
      path: ""
      type: "topics"
    values:
      layout: "default"
  
  - scope:
      path: ""
      type: "subtopics"
    values:
      layout: "default"
  
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "default"

# Exclude from processing
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor
  - .git
  - .github
  - .vscode
  - phap-dien/
  - crawled/
  - scripts/
"""
    
    # Backup config cũ
    backup_file = config_file + '.backup_restructure'
    shutil.copy2(config_file, backup_file)
    
    # Ghi config mới
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(new_config)
    
    print(f"✅ Updated _config.yml")
    print(f"   Backup: {backup_file}")

def create_redirects_file(mapping):
    """Tạo file redirects cho URLs cũ"""
    redirects_file = '/root/.openclaw/workspace/projects/github-io/van-ban/_redirects_restructure'
    
    with open(redirects_file, 'w', encoding='utf-8') as f:
        f.write("# Redirects for restructured URLs\n")
        f.write("# Generated by final_restructure.py\n\n")
        
        # Redirect topic pages
        f.write("# Topic pages (chu-de/ → root)\n")
        f.write("/van-ban/chu-de/* /van-ban/:splat 301\n\n")
        
        # Redirect subtopic pages
        f.write("# Subtopic pages (de-muc/ → parent/child)\n")
        for demuc_slug, info in mapping.items():
            chude_slug = info['chude_slug']
            f.write(f"/van-ban/de-muc/{demuc_slug}/ /van-ban/{chude_slug}/{demuc_slug}/ 301\n")
        
        # Redirect wrong pattern
        f.write("\n# Wrong pattern redirect\n")
        f.write("/van-ban/chu-de/de-muc/* /van-ban/de-muc/:splat 301\n")
        
        # Redirect index
        f.write("\n# Index redirect\n")
        f.write("/van-ban/chu-de/ /van-ban/ 301\n")
        f.write("/van-ban/de-muc/ /van-ban/ 301\n")
    
    print(f"✅ Created redirects file: {redirects_file}")

def create_test_script(new_dir):
    """Tạo script test URLs mới"""
    test_script = os.path.join(new_dir, 'test_urls.py')
    
    script_content = '''#!/usr/bin/env python3
"""
Test new URL structure
"""

import os
import re

def test_urls():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Testing new URL structure...")
    print("=" * 60)
    
    # Test topic files
    topic_files = [f for f in os.listdir(base_dir) if f.endswith('.md') and f != 'index.md']
    print(f"1. Found {len(topic_files)} topic files")
    
    for filename in topic_files[:3]:  # Test first 3
        with open(os.path.join(base_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check permalink
        match = re.search(r'permalink:\\s*(.+)', content)
        if match:
            permalink = match.group(1).strip()
            slug = filename.replace('.md', '')
            expected = f'/van-ban/{slug}/'
            
            if permalink == expected:
                print(f"   ✓ {filename}: {permalink}")
            else:
                print(f"   ✗ {filename}: {permalink} (expected: {expected})")
    
    # Test subtopic directories
    subtopic_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    print(f"\\n2. Found {len(subtopic_dirs)} topic directories")
    
    for dirname in subtopic_dirs[:3]:  # Test first 3
        dir_path = os.path.join(base_dir, dirname)
        subtopic_files = [f for f in os.listdir(dir_path) if f.endswith('.md')]
        
        print(f"   {dirname}: {len(subtopic_files)} subtopics")
        
        if subtopic_files:
            test_file = os.path.join(dir_path, subtopic_files[0])
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            match = re.search(r'permalink:\\s*(.+)', content)
            if match:
                permalink = match.group(1).strip()
                print(f"     Sample: {permalink}")
    
    print("\\n" + "=" * 60)
    print("URL Structure:")
    print("  Topic:      /van-ban/<chude>/")
    print("  Subtopic:   /van-ban/<chude>/<demuc>/")
    print("  Homepage:   /van-ban/")

if __name__ == '__main__':
    test_urls()
'''
    
    with open(test_script, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    os.chmod(test_script, 0o755)
    print(f"✅ Created test script: {test_script}")

def main():
    print("🚀 FINAL URL RESTRUCTURE")
    print("=" * 60)
    print("Current structure:")
    print("  /van-ban/chu-de/<chude>/")
    print("  /van-ban/de-muc/<demuc>/")
    print("")
    print("New structure:")
    print("  /van-ban/<chude>/")
    print("  /van-ban/<chude>/<demuc>/")
    print("=" * 60)
    
    # Load mapping
    mapping = load_mapping()
    
    # Restructure files
    new_dir = restructure_with_mapping(mapping)
    
    # Update config
    update_config_for_new_structure()
    
    # Create redirects
    create_redirects_file(mapping)
    
    # Create test script
    create_test_script(new_dir)
    
    print("\n" + "=" * 60)
    print("✅ RESTRUCTURE COMPLETE")
    print(f"New structure: {new_dir}")
    print(f"Total files: {sum(len(files) for _, _, files in os.walk(new_dir))}")
    print("\nNext steps:")
    print("1. Review new structure")
    print("2. Replace _pages/ with _pages_restructured/")
    print("3. Update _config.yml (already done)")
    print("4. Test new URLs")
    print("5. Deploy redirects")

if __name__ == '__main__':
    main()
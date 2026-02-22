#!/usr/bin/env python3
"""
Fix all links to use absolute paths instead of relative paths
"""

import os
import re
import glob

def fix_links_in_file(filepath, is_chu_de=False, is_de_muc=False):
    """Fix links in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern cho markdown links: [text](url)
    # Cần fix các relative paths
    
    # 1. Fix links từ chu-de/ đến de-muc/
    # Từ: ../de-muc/slug/
    # Thành: /van-ban/de-muc/slug/
    if is_chu_de:
        pattern = r'(\[([^\]]+)\]\(\.\./de-muc/([^)/]+)/\))'
        
        def replace_chu_de_link(match):
            full_match = match.group(1)
            text = match.group(2)
            slug = match.group(3)
            return f'[{text}](/van-ban/de-muc/{slug}/)'
        
        content = re.sub(pattern, replace_chu_de_link, content)
    
    # 2. Fix links từ de-muc/ đến chu-de/
    # Từ: ../chu-de/slug/
    # Thành: /van-ban/chu-de/slug/
    if is_de_muc:
        pattern = r'(\[([^\]]+)\]\(\.\./chu-de/([^)/]+)/\))'
        
        def replace_de_muc_link(match):
            full_match = match.group(1)
            text = match.group(2)
            slug = match.group(3)
            return f'[{text}](/van-ban/chu-de/{slug}/)'
        
        content = re.sub(pattern, replace_de_muc_link, content)
    
    # 3. Fix link "Quay lại danh sách chủ đề" trong chu-de/
    # Từ: ../ (hoặc [← Danh sách tất cả Chủ đề](../))
    # Thành: /van-ban/
    if is_chu_de:
        # Pattern cho link quay lại
        pattern1 = r'(\[←[^\]]+\]\(\.\./\))'
        content = re.sub(pattern1, r'[← Danh sách tất cả Chủ đề](/van-ban/)', content)
        
        pattern2 = r'(\[Quay lại[^\]]+\]\(\.\./\))'
        content = re.sub(pattern2, r'[Quay lại danh sách chủ đề](/van-ban/)', content)
    
    # 4. Fix link từ index.md đến chu-de/
    # File index.md đã có absolute paths: [text](chu-de/slug/)
    # Nhưng cần đảm bảo đúng: /van-ban/chu-de/slug/
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def fix_all_links():
    """Fix all links in all files"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== FIX ALL LINKS TO ABSOLUTE PATHS ===")
    
    # 1. Fix index.md
    index_file = os.path.join(base_dir, '_pages', 'index.md')
    print(f"1. Fixing index.md...")
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix links từ index đến chu-de/
    # Từ: [text](chu-de/slug/)
    # Thành: [text](/van-ban/chu-de/slug/)
    pattern = r'(\[([^\]]+)\]\(chu-de/([^)/]+)/\))'
    
    def replace_index_link(match):
        full_match = match.group(1)
        text = match.group(2)
        slug = match.group(3)
        return f'[{text}](/van-ban/chu-de/{slug}/)'
    
    new_content = re.sub(pattern, replace_index_link, content)
    
    if new_content != content:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("  ✓ Đã fix links trong index.md")
    else:
        print("  ✓ index.md đã đúng")
    
    # 2. Fix tất cả files trong chu-de/
    chu_de_dir = os.path.join(base_dir, '_pages', 'chu-de')
    chu_de_files = glob.glob(os.path.join(chu_de_dir, '*.md'))
    
    print(f"2. Fixing {len(chu_de_files)} files trong chu-de/...")
    fixed_chu_de = 0
    
    for filepath in chu_de_files:
        if fix_links_in_file(filepath, is_chu_de=True):
            fixed_chu_de += 1
    
    print(f"  ✓ Đã fix {fixed_chu_de}/{len(chu_de_files)} files trong chu-de/")
    
    # 3. Fix tất cả files trong de-muc/
    de_muc_dir = os.path.join(base_dir, '_pages', 'de-muc')
    de_muc_files = glob.glob(os.path.join(de_muc_dir, '*.md'))
    
    print(f"3. Fixing {len(de_muc_files)} files trong de-muc/...")
    fixed_de_muc = 0
    
    for filepath in de_muc_files:
        if fix_links_in_file(filepath, is_de_muc=True):
            fixed_de_muc += 1
    
    print(f"  ✓ Đã fix {fixed_de_muc}/{len(de_muc_files)} files trong de-muc/")
    
    # 4. Tạo redirect cho URL sai (tùy chọn)
    print(f"4. Tạo redirect cho URL sai...")
    
    redirect_file = os.path.join(base_dir, '_pages', 'redirects.md')
    redirect_content = """---
layout: default
title: Redirect
permalink: /van-ban/redirects/
redirect_from:
  - /van-ban/chu-de/de-muc/
---

# Redirect Page

Trang này chuyển hướng các URLs sai.

Nếu bạn đang tìm kiếm một đề mục pháp luật, vui lòng sử dụng URL đúng:

**URL SAI (404):** `/van-ban/chu-de/de-muc/[tên-đề-mục]/`

**URL ĐÚNG:** `/van-ban/de-muc/[tên-đề-mục]/`

Ví dụ:
- ❌ SAI: `/van-ban/chu-de/de-muc/bao-hiem-y-te/`
- ✅ ĐÚNG: `/van-ban/de-muc/bao-hiem-y-te/`

[← Quay lại trang chính van-ban](/van-ban/)
"""
    
    with open(redirect_file, 'w', encoding='utf-8') as f:
        f.write(redirect_content)
    
    print("  ✓ Đã tạo redirects.md")
    
    print("\n=== HOÀN THÀNH ===")
    print(f"Đã fix {fixed_chu_de + fixed_de_muc + 1} files:")
    print(f"- index.md: absolute links đến chu-de/")
    print(f"- chu-de/ files: absolute links đến de-muc/ và /van-ban/")
    print(f"- de-muc/ files: absolute links đến chu-de/")
    print(f"- redirects.md: hướng dẫn URLs đúng")

def verify_fixes():
    """Verify that all links are now absolute"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("\n=== VERIFY FIXES ===")
    
    # Kiểm tra index.md
    index_file = os.path.join(base_dir, '_pages', 'index.md')
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm relative links
    relative_links = re.findall(r'\[[^\]]+\]\([^)]*\.\./[^)]*\)', content)
    
    if relative_links:
        print(f"❌ index.md vẫn có relative links: {len(relative_links)}")
        for link in relative_links[:3]:
            print(f"  - {link}")
    else:
        print("✅ index.md: Tất cả links đều absolute")
    
    # Kiểm tra một file chu-de/
    chu_de_file = os.path.join(base_dir, '_pages', 'chu-de', 'bao-hiem.md')
    with open(chu_de_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    relative_links = re.findall(r'\[[^\]]+\]\([^)]*\.\./[^)]*\)', content)
    
    if relative_links:
        print(f"❌ bao-hiem.md vẫn có relative links: {len(relative_links)}")
        for link in relative_links:
            print(f"  - {link}")
    else:
        print("✅ bao-hiem.md: Tất cả links đều absolute")
    
    # Kiểm tra absolute links
    absolute_links = re.findall(r'\[[^\]]+\]\(/van-ban/[^)]+\)', content)
    print(f"✅ bao-hiem.md có {len(absolute_links)} absolute links")
    
    print("\n=== TEST URLs ===")
    print("Sau khi fix, các links sẽ hoạt động từ bất kỳ trang nào:")
    print("- Từ /van-ban/ → /van-ban/chu-de/bao-hiem/")
    print("- Từ /van-ban/chu-de/bao-hiem/ → /van-ban/de-muc/bao-hiem-y-te/")
    print("- Từ /van-ban/de-muc/bao-hiem-y-te/ → /van-ban/chu-de/bao-hiem/")
    print("- Từ bất kỳ đâu → /van-ban/ (trang chính)")

if __name__ == '__main__':
    fix_all_links()
    verify_fixes()
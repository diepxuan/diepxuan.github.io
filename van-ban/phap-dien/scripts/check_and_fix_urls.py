#!/usr/bin/env python3
"""
Script kiểm tra và sửa toàn bộ URLs trong markdown files
"""

import os
import re
import glob

def check_urls_in_file(filepath):
    """Kiểm tra URLs trong một file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm tất cả links markdown
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    
    errors = []
    for text, url in links:
        # Kiểm tra các loại URL sai
        if url.startswith('../'):
            # URL tương đối - cần kiểm tra xem file tồn tại không
            abs_url = os.path.normpath(os.path.join(os.path.dirname(filepath), url))
            if not os.path.exists(abs_url) and not url.startswith('../chu-de/') and not url.startswith('../de-muc/'):
                errors.append(f"  - [{text}]({url}) -> File không tồn tại: {abs_url}")
        
        elif url.startswith('chu-de/') or url.startswith('de-muc/'):
            # URL tương đối từ thư mục hiện tại
            abs_url = os.path.normpath(os.path.join(os.path.dirname(filepath), url))
            if not os.path.exists(abs_url):
                errors.append(f"  - [{text}]({url}) -> File không tồn tại: {abs_url}")
    
    return errors

def check_all_files():
    """Kiểm tra tất cả files"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== KIỂM TRA TOÀN BỘ URLs ===")
    
    all_errors = []
    
    # 1. Kiểm tra index.md
    index_file = os.path.join(base_dir, 'index.md')
    print(f"\n1. Kiểm tra {index_file}")
    errors = check_urls_in_file(index_file)
    if errors:
        all_errors.extend([(index_file, e) for e in errors])
        for error in errors:
            print(error)
    else:
        print("  ✓ OK")
    
    # 2. Kiểm tra tất cả files trong chu-de/
    chu_de_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
    print(f"\n2. Kiểm tra {len(chu_de_files)} files trong chu-de/")
    
    for filepath in chu_de_files:
        filename = os.path.basename(filepath)
        errors = check_urls_in_file(filepath)
        if errors:
            all_errors.extend([(filepath, e) for e in errors])
            print(f"  {filename}: {len(errors)} lỗi")
            for error in errors[:3]:  # Hiển thị 3 lỗi đầu
                print(f"    {error}")
            if len(errors) > 3:
                print(f"    ... và {len(errors)-3} lỗi khác")
        else:
            print(f"  {filename}: ✓ OK")
    
    # 3. Kiểm tra tất cả files trong de-muc/
    de_muc_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
    print(f"\n3. Kiểm tra {len(de_muc_files)} files trong de-muc/")
    
    error_count = 0
    for filepath in de_muc_files:
        filename = os.path.basename(filepath)
        errors = check_urls_in_file(filepath)
        if errors:
            all_errors.extend([(filepath, e) for e in errors])
            error_count += len(errors)
            if error_count <= 10:  # Hiển thị 10 files đầu có lỗi
                print(f"  {filename}: {len(errors)} lỗi")
    
    if error_count > 0:
        print(f"  Tổng: {error_count} lỗi trong {len([f for f in de_muc_files if check_urls_in_file(f)])} files")
    
    # Tổng kết
    print(f"\n=== TỔNG KẾT ===")
    print(f"Tổng số files: {1 + len(chu_de_files) + len(de_muc_files)}")
    print(f"Tổng số lỗi URL: {len(all_errors)}")
    
    if all_errors:
        print("\n=== CÁC LỖI PHỔ BIẾN ===")
        # Phân tích lỗi
        error_types = {}
        for filepath, error in all_errors:
            error_msg = error.split('->')[0].strip()
            error_types[error_msg] = error_types.get(error_msg, 0) + 1
        
        for error_msg, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"{count} lỗi: {error_msg}")
        
        return False
    else:
        print("✓ Tất cả URLs đều OK!")
        return True

def fix_url_structure():
    """Sửa cấu trúc URLs cho đúng"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("\n=== SỬA CẤU TRÚC URLs ===")
    
    # 1. Sửa index.md - đảm bảo links đến chu-de/ đúng
    index_file = os.path.join(base_dir, 'index.md')
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm và sửa links trong index.md
    # Links hiện tại: [text](chu-de/slug/)
    # Cần đảm bảo đúng: [text](chu-de/slug/)
    pattern = r'(\*\*\[([^\]]+)\]\(chu-de/([^)/]+)/\)\*\* - (\d+) đề mục)'
    
    def replace_index_link(match):
        full_match = match.group(1)
        text = match.group(2)
        slug = match.group(3)
        count = match.group(4)
        
        # Kiểm tra file tồn tại
        chu_de_file = os.path.join(base_dir, 'chu-de', f'{slug}.md')
        if os.path.exists(chu_de_file):
            return full_match  # Giữ nguyên
        else:
            # Tìm file đúng
            actual_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
            for file in actual_files:
                file_slug = os.path.splitext(os.path.basename(file))[0]
                if file_slug.replace('-', ' ') in text.lower() or text.lower().replace(' ', '-') in file_slug:
                    print(f"  Sửa: {text} -> {file_slug}")
                    return f'**[{text}](chu-de/{file_slug}/)** - {count} đề mục'
            
            print(f"  ❌ Không tìm thấy file cho: {text} (slug: {slug})")
            return full_match
    
    new_content = re.sub(pattern, replace_index_link, content)
    
    if new_content != content:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✓ Đã sửa index.md")
    else:
        print("✓ index.md đã đúng")
    
    # 2. Sửa files trong chu-de/ - đảm bảo links đến de-muc/ đúng
    chu_de_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
    fixed_chu_de = 0
    
    for filepath in chu_de_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm links đến de-muc/
        pattern = r'(\d+\. \*\*\[([^\]]+)\]\(\.\./de-muc/([^)/]+)/\)\*\*)'
        
        def replace_chu_de_link(match):
            full_match = match.group(1)
            number = match.group(1).split('.')[0]
            text = match.group(2)
            slug = match.group(3)
            
            # Kiểm tra file tồn tại
            de_muc_file = os.path.join(base_dir, 'de-muc', f'{slug}.md')
            if os.path.exists(de_muc_file):
                return full_match  # Giữ nguyên
            else:
                # Tìm file đúng
                actual_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
                for file in actual_files:
                    file_slug = os.path.splitext(os.path.basename(file))[0]
                    if file_slug.replace('-', ' ') in text.lower() or text.lower().replace(' ', '-') in file_slug:
                        print(f"  Sửa: {text} -> {file_slug}")
                        return f'{number}. **[{text}](../de-muc/{file_slug}/)**'
                
                print(f"  ❌ Không tìm thấy file cho: {text} (slug: {slug})")
                return full_match
        
        new_content = re.sub(pattern, replace_chu_de_link, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_chu_de += 1
    
    print(f"✓ Đã sửa {fixed_chu_de}/{len(chu_de_files)} files trong chu-de/")
    
    # 3. Sửa files trong de-muc/ - đảm bảo links đến chu-de/ đúng
    de_muc_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
    fixed_de_muc = 0
    
    for filepath in de_muc_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm link đến chu-de/ (trong phần Chủ đề)
        pattern = r'(\*\*Chủ đề:\*\* \[([^\]]+)\]\(\.\./chu-de/([^)/]+)/\)'
        
        def replace_de_muc_link(match):
            full_match = match.group(0)
            text = match.group(2)
            slug = match.group(3)
            
            # Kiểm tra file tồn tại
            chu_de_file = os.path.join(base_dir, 'chu-de', f'{slug}.md')
            if os.path.exists(chu_de_file):
                return full_match  # Giữ nguyên
            else:
                # Tìm file đúng
                actual_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
                for file in actual_files:
                    file_slug = os.path.splitext(os.path.basename(file))[0]
                    if file_slug.replace('-', ' ') in text.lower() or text.lower().replace(' ', '-') in file_slug:
                        print(f"  Sửa chủ đề: {text} -> {file_slug}")
                        return f'**Chủ đề:** [{text}](../chu-de/{file_slug}/)'
                
                print(f"  ❌ Không tìm thấy file chủ đề cho: {text} (slug: {slug})")
                return full_match
        
        new_content = re.sub(pattern, replace_de_muc_link, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_de_muc += 1
    
    print(f"✓ Đã sửa {fixed_de_muc}/{len(de_muc_files)} files trong de-muc/")
    
    print("\n=== HOÀN THÀNH SỬA URLs ===")

def main():
    # 1. Kiểm tra URLs
    all_ok = check_all_files()
    
    if not all_ok:
        # 2. Sửa URLs
        fix_url_structure()
        
        # 3. Kiểm tra lại
        print("\n=== KIỂM TRA LẠI SAU KHI SỬA ===")
        check_all_files()
    else:
        print("\n✓ Không cần sửa, tất cả URLs đều đúng!")

if __name__ == '__main__':
    main()
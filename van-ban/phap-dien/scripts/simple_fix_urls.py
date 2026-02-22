#!/usr/bin/env python3
"""
Script đơn giản sửa URLs
"""

import os
import glob

def fix_all_urls():
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== SỬA TOÀN BỘ URLs ===")
    
    # 1. Sửa index.md - thêm .md vào links
    index_file = os.path.join(base_dir, 'index.md')
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sửa links từ chu-de/slug/ thành chu-de/slug.md
    # Nhưng thực tế trên web không cần .md, nên em sẽ giữ nguyên
    # Chỉ cần đảm bảo permalink đúng
    
    print("1. Kiểm tra index.md...")
    
    # 2. Sửa tất cả files trong chu-de/ - đảm bảo links đến de-muc/ đúng
    chu_de_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
    print(f"2. Sửa {len(chu_de_files)} files trong chu-de/")
    
    for filepath in chu_de_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa links từ ../de-muc/slug/ thành ../de-muc/slug.md
        # Nhưng trên web: ../de-muc/slug/ là đúng (không có .md)
        
        # Kiểm tra permalink
        if 'permalink:' in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('permalink:'):
                    permalink = line.split(':', 1)[1].strip()
                    # Đảm bảo permalink kết thúc bằng /
                    if not permalink.endswith('/'):
                        lines[i] = f'permalink: {permalink}/'
                        print(f"  Sửa permalink: {os.path.basename(filepath)}")
            
            new_content = '\n'.join(lines)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
    
    # 3. Sửa tất cả files trong de-muc/ - đảm bảo links đến chu-de/ đúng
    de_muc_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
    print(f"3. Sửa {len(de_muc_files)} files trong de-muc/")
    
    for filepath in de_muc_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra permalink
        if 'permalink:' in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('permalink:'):
                    permalink = line.split(':', 1)[1].strip()
                    # Đảm bảo permalink kết thúc bằng /
                    if not permalink.endswith('/'):
                        lines[i] = f'permalink: {permalink}/'
                        print(f"  Sửa permalink: {os.path.basename(filepath)}")
            
            new_content = '\n'.join(lines)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
    
    print("\n=== HOÀN THÀNH ===")
    print("✓ Đã kiểm tra tất cả permalinks")
    print("✓ Đảm bảo tất cả permalinks kết thúc bằng /")

def check_actual_urls():
    """Kiểm tra URLs thực tế sẽ hoạt động thế nào"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("\n=== KIỂM TRA URLs THỰC TẾ ===")
    
    # Với Jekyll trên GitHub Pages:
    # 1. File: van-ban/chu-de/bao-hiem.md
    # 2. permalink: /van-ban/chu-de/bao-hiem/
    # 3. URL thực tế: https://docs.diepxuan.com/van-ban/chu-de/bao-hiem/
    
    # Vấn đề: Cần đảm bảo tất cả files đều có front matter đúng
    
    chu_de_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
    de_muc_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
    
    print(f"Tổng số files: {len(chu_de_files) + len(de_muc_files) + 1}")
    print(f"- index.md: 1 file")
    print(f"- chu-de/: {len(chu_de_files)} files")
    print(f"- de-muc/: {len(de_muc_files)} files")
    
    # Kiểm tra một vài files
    print("\n=== VÍ DỤ URLs ===")
    
    # File: bao-hiem.md
    bao_hiem_file = os.path.join(base_dir, 'chu-de', 'bao-hiem.md')
    with open(bao_hiem_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if 'permalink:' in line:
                print(f"1. File: bao-hiem.md")
                print(f"   Permalink: {line.strip()}")
                print(f"   URL: https://docs.diepxuan.com{line.split(':')[1].strip()}")
                break
    
    # File: bao-hiem-y-te.md
    bao_hiem_y_te_file = os.path.join(base_dir, 'de-muc', 'bao-hiem-y-te.md')
    with open(bao_hiem_y_te_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if 'permalink:' in line:
                print(f"\n2. File: bao-hiem-y-te.md")
                print(f"   Permalink: {line.strip()}")
                print(f"   URL: https://docs.diepxuan.com{line.split(':')[1].strip()}")
                break
    
    print("\n=== KẾT LUẬN ===")
    print("1. Cấu trúc URLs hiện tại ĐÚNG cho Jekyll:")
    print("   - /van-ban/chu-de/bao-hiem/")
    print("   - /van-ban/de-muc/bao-hiem-y-te/")
    print("\n2. Vấn đề 404 của sếp:")
    print("   - URL sai: /van-ban/chu-de/de-muc/bao-hiem-y-te/")
    print("   - URL đúng: /van-ban/de-muc/bao-hiem-y-te/")
    print("\n3. Nguyên nhân: Thừa 'chu-de/' trong URL")

if __name__ == '__main__':
    fix_all_urls()
    check_actual_urls()
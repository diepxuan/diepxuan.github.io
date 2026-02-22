#!/usr/bin/env python3
"""
Sửa cấu trúc cho Jekyll - Tạo folder _pages/ với đúng cấu trúc
"""

import os
import shutil
import glob

def create_jekyll_structure():
    """Tạo cấu trúc Jekyll đúng"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== TẠO CẤU TRÚC JEKYLL ĐÚNG ===")
    
    # 1. Tạo folder _pages nếu chưa có
    pages_dir = os.path.join(base_dir, '_pages')
    os.makedirs(pages_dir, exist_ok=True)
    
    # 2. Di chuyển và sửa tất cả files
    print("1. Xử lý index.md...")
    
    # Copy index.md vào _pages
    index_src = os.path.join(base_dir, 'index.md')
    index_dst = os.path.join(pages_dir, 'index.md')
    
    if os.path.exists(index_src):
        with open(index_src, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa front matter cho index
        if content.startswith('---'):
            # Đã có front matter, thêm layout
            lines = content.split('\n')
            new_lines = []
            in_front_matter = False
            front_matter_done = False
            
            for line in lines:
                if line.strip() == '---' and not in_front_matter:
                    in_front_matter = True
                    new_lines.append(line)
                elif line.strip() == '---' and in_front_matter and not front_matter_done:
                    front_matter_done = True
                    new_lines.append('layout: page')
                    new_lines.append(line)
                else:
                    new_lines.append(line)
            
            content = '\n'.join(new_lines)
        
        with open(index_dst, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("  ✓ Đã tạo _pages/index.md")
    
    # 3. Tạo folder _pages/chu-de và _pages/de-muc
    chu_de_pages_dir = os.path.join(pages_dir, 'chu-de')
    de_muc_pages_dir = os.path.join(pages_dir, 'de-muc')
    os.makedirs(chu_de_pages_dir, exist_ok=True)
    os.makedirs(de_muc_pages_dir, exist_ok=True)
    
    # 4. Xử lý files chu-de/
    print(f"2. Xử lý files chu-de/...")
    chu_de_files = glob.glob(os.path.join(base_dir, 'chu-de', '*.md'))
    
    for src_file in chu_de_files:
        filename = os.path.basename(src_file)
        dst_file = os.path.join(chu_de_pages_dir, filename)
        
        with open(src_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Đảm bảo có layout trong front matter
        if 'layout:' not in content:
            lines = content.split('\n')
            if lines[0].strip() == '---':
                # Tìm dòng thứ 2 của front matter
                for i in range(1, min(10, len(lines))):
                    if lines[i].strip() == '---':
                        lines.insert(i, 'layout: page')
                        break
            
            content = '\n'.join(lines)
        
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"  ✓ Đã tạo {len(chu_de_files)} files trong _pages/chu-de/")
    
    # 5. Xử lý files de-muc/
    print(f"3. Xử lý files de-muc/...")
    de_muc_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
    
    for src_file in de_muc_files:
        filename = os.path.basename(src_file)
        dst_file = os.path.join(de_muc_pages_dir, filename)
        
        with open(src_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Đảm bảo có layout trong front matter
        if 'layout:' not in content:
            lines = content.split('\n')
            if lines[0].strip() == '---':
                # Tìm dòng thứ 2 của front matter
                for i in range(1, min(10, len(lines))):
                    if lines[i].strip() == '---':
                        lines.insert(i, 'layout: page')
                        break
            
            content = '\n'.join(lines)
        
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"  ✓ Đã tạo {len(de_muc_files)} files trong _pages/de-muc/")
    
    # 6. Tạo _config.yml cho van-ban
    config_file = os.path.join(base_dir, '_config.yml')
    config_content = """# Jekyll configuration for van-ban
title: Bộ Pháp điển Điện tử
description: Hệ thống pháp luật chính thức của Việt Nam
baseurl: /van-ban
url: https://docs.diepxuan.com

# Permalinks
permalink: pretty

# Collections
collections:
  pages:
    output: true
    permalink: /:path/

# Defaults
defaults:
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "page"

# Exclude
exclude:
  - chu-de/
  - de-muc/
  - phap-dien/
  - crawled/
  - node_modules/
  - vendor/
  - Gemfile
  - Gemfile.lock
"""
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print("✓ Đã tạo _config.yml")
    
    # 7. Tạo layout file
    layout_dir = os.path.join(base_dir, '_layouts')
    os.makedirs(layout_dir, exist_ok=True)
    
    layout_file = os.path.join(layout_dir, 'default.html')
    layout_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} - Bộ Pháp điển Điện tử</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background: #1a237e;
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        h1 {
            margin-bottom: 0.5rem;
        }
        .breadcrumb {
            margin: 1rem 0;
            padding: 1rem;
            background: #f5f5f5;
            border-radius: 8px;
        }
        .breadcrumb a {
            color: #1a237e;
            text-decoration: none;
        }
        .breadcrumb a:hover {
            text-decoration: underline;
        }
        .content {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        footer {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #e0e0e0;
            text-align: center;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>📚 Bộ Pháp điển Điện tử</h1>
        <p>Hệ thống pháp luật chính thức của Việt Nam - Bộ Tư pháp</p>
    </header>
    
    <div class="breadcrumb">
        <a href="/van-ban/">Trang chủ</a>
        {% if page.url != '/' %}
            <span>→</span>
            <span>{{ page.title }}</span>
        {% endif %}
    </div>
    
    <div class="content">
        {{ content }}
    </div>
    
    <footer>
        <p>Dữ liệu từ Bộ Pháp điển Điện tử chính thức - Chỉ sử dụng cho tham khảo, nghiên cứu</p>
        <p>© 2026 - docs.diepxuan.com</p>
    </footer>
</body>
</html>"""
    
    with open(layout_file, 'w', encoding='utf-8') as f:
        f.write(layout_content)
    
    print("✓ Đã tạo _layouts/default.html")
    
    # 8. Tạo README với hướng dẫn
    readme_file = os.path.join(base_dir, 'README_JEKYLL.md')
    readme_content = """# CẤU TRÚC JEKYLL CHO VAN-BAN

## CẤU TRÚC MỚI
```
van-ban/
├── _config.yml           # Jekyll configuration
├── _layouts/             # Layout templates
│   └── default.html      # Main layout
├── _pages/               # Tất cả pages (Jekyll collection)
│   ├── index.md          # Trang chính
│   ├── chu-de/           # Chủ đề pages
│   │   ├── an-ninh-quoc-gia.md
│   │   ├── bao-hiem.md
│   │   └── ... (45 files)
│   └── de-muc/           # Đề mục pages
│       ├── an-ninh-quoc-gia.md
│       ├── bao-hiem-y-te.md
│       └── ... (306 files)
├── chu-de/               # Files cũ (backup)
├── de-muc/               # Files cũ (backup)
└── phap-dien/            # Database và scripts
```

## URLs ĐÚNG
Với cấu trúc Jekyll mới:

### 1. TRANG CHÍNH
```
https://docs.diepxuan.com/van-ban/
```

### 2. TRANG CHỦ ĐỀ
```
https://docs.diepxuan.com/van-ban/chu-de/[tên-chủ-đề]/
```

Ví dụ:
- https://docs.diepxuan.com/van-ban/chu-de/bao-hiem/
- https://docs.diepxuan.com/van-ban/chu-de/an-ninh-quoc-gia/

### 3. TRANG ĐỀ MỤC
```
https://docs.diepxuan.com/van-ban/de-muc/[tên-đề-mục]/
```

Ví dụ:
- https://docs.diepxuan.com/van-ban/de-muc/bao-hiem-y-te/
- https://docs.diepxuan.com/van-ban/de-muc/an-ninh-quoc-gia/

## CÁCH HOẠT ĐỘNG
1. Jekyll đọc `_config.yml` để biết cấu hình
2. Tất cả files trong `_pages/` được xử lý như collection
3. Mỗi file có `layout: page` trong front matter
4. Layout `default.html` được áp dụng cho tất cả pages
5. GitHub Pages tự động build và deploy

## FIX URLs SAI
URL sai: `https://docs.diepxuan.com/van-ban/chu-de/de-muc/bao-hiem-y-te/`

**Nguyên nhân**: Thừa `chu-de/` trong URL

**Giải pháp**: 
1. Truy cập URL đúng: `https://docs.diepxuan.com/van-ban/de-muc/bao-hiem-y-te/`
2. Hoặc từ trang chính: https://docs.diepxuan.com/van-ban/ → Bảo hiểm → Bảo hiểm y tế

## KIỂM TRA
1. Local test: `bundle exec jekyll serve`
2. GitHub Pages: Tự động build khi push
3. Check URLs: Tất cả phải kết thúc bằng `/`

## BACKUP
Files cũ được giữ trong:
- `chu-de/` (backup)
- `de-muc/` (backup)

Có thể xóa sau khi xác nhận hoạt động.

---
*Cập nhật: 2026-02-22*
"""
    
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✓ Đã tạo README_JEKYLL.md")
    
    print("\n=== HOÀN THÀNH ===")
    print("Đã tạo cấu trúc Jekyll đúng:")
    print(f"- _pages/index.md")
    print(f"- _pages/chu-de/ ({len(chu_de_files)} files)")
    print(f"- _pages/de-muc/ ({len(de_muc_files)} files)")
    print(f"- _config.yml")
    print(f"- _layouts/default.html")
    print("\nGitHub Pages sẽ tự động build với cấu trúc này.")

if __name__ == '__main__':
    create_jekyll_structure()
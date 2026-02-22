#!/usr/bin/env python3
"""
Tạo redirects cho các URLs sai
"""

import os
import glob
import json

def create_redirect_html():
    """Tạo file redirect.html cho các URLs sai"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== TẠO REDIRECTS CHO URLs SAI ===")
    
    # Tạo folder _redirects nếu chưa có
    redirects_dir = os.path.join(base_dir, '_redirects')
    os.makedirs(redirects_dir, exist_ok=True)
    
    # 1. Tạo redirect cho URL sai: /van-ban/chu-de/de-muc/* → /van-ban/de-muc/*
    redirects = []
    
    # Lấy tất cả files trong de-muc/
    de_muc_files = glob.glob(os.path.join(base_dir, 'de-muc', '*.md'))
    
    for filepath in de_muc_files:
        filename = os.path.basename(filepath)
        slug = os.path.splitext(filename)[0]
        
        # URL sai: /van-ban/chu-de/de-muc/{slug}/
        # URL đúng: /van-ban/de-muc/{slug}/
        
        wrong_url = f"/van-ban/chu-de/de-muc/{slug}/"
        correct_url = f"/van-ban/de-muc/{slug}/"
        
        redirects.append({
            'from': wrong_url,
            'to': correct_url,
            'status': 301
        })
    
    # 2. Tạo file _redirects (cho Netlify) hoặc .htaccess (cho Apache)
    # Nhưng với GitHub Pages + Jekyll, cần tạo HTML redirect pages
    
    # Tạo HTML redirect pages
    html_dir = os.path.join(base_dir, 'redirects')
    os.makedirs(html_dir, exist_ok=True)
    
    print(f"Tạo {len(redirects)} redirects...")
    
    for i, redirect in enumerate(redirects[:10]):  # Tạo 10 redirects đầu
        from_slug = redirect['from'].strip('/').split('/')[-1]
        html_file = os.path.join(html_dir, f"{from_slug}.html")
        
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; url={redirect['to']}">
    <link rel="canonical" href="{redirect['to']}">
    <script>
        window.location.href = "{redirect['to']}";
    </script>
</head>
<body>
    <p>Redirecting to <a href="{redirect['to']}">{redirect['to']}</a>...</p>
</body>
</html>"""
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    print(f"✓ Đã tạo {min(10, len(redirects))} redirect HTML files")
    
    # 3. Tạo JSON redirect map
    redirect_map = {
        'redirects': redirects[:50]  # Giới hạn 50 redirects
    }
    
    map_file = os.path.join(base_dir, 'redirects.json')
    with open(map_file, 'w', encoding='utf-8') as f:
        json.dump(redirect_map, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Đã tạo redirects.json với {len(redirect_map['redirects'])} redirects")
    
    # 4. Tạo README với hướng dẫn URLs đúng
    readme_file = os.path.join(base_dir, 'URLS_CORRECT.md')
    readme_content = """# URLs ĐÚNG cho Bộ Pháp điển Điện tử

## CẤU TRÚC URLs CHUẨN

### 1. TRANG CHÍNH
```
https://docs.diepxuan.com/van-ban/
```

### 2. TRANG CHỦ ĐỀ (45 chủ đề)
```
https://docs.diepxuan.com/van-ban/chu-de/[tên-chủ-đề]/
```

Ví dụ:
- https://docs.diepxuan.com/van-ban/chu-de/bao-hiem/
- https://docs.diepxuan.com/van-ban/chu-de/an-ninh-quoc-gia/
- https://docs.diepxuan.com/van-ban/chu-de/doanh-nghiep-hop-tac-xa/

### 3. TRANG ĐỀ MỤC (306 đề mục)
```
https://docs.diepxuan.com/van-ban/de-muc/[tên-đề-mục]/
```

Ví dụ:
- https://docs.diepxuan.com/van-ban/de-muc/bao-hiem-y-te/
- https://docs.diepxuan.com/van-ban/de-muc/an-ninh-quoc-gia/
- https://docs.diepxuan.com/van-ban/de-muc/doanh-nghiep/

## URLs SAI THƯỜNG GẶP

### ❌ SAI (404):
```
https://docs.diepxuan.com/van-ban/chu-de/de-muc/bao-hiem-y-te/
```

### ✅ ĐÚNG:
```
https://docs.diepxuan.com/van-ban/de-muc/bao-hiem-y-te/
```

## NGUYÊN TẮC CẤU TRÚC URL

1. **Chủ đề**: `/van-ban/chu-de/[slug]/`
2. **Đề mục**: `/van-ban/de-muc/[slug]/`
3. **KHÔNG BAO GIỜ** kết hợp `chu-de/de-muc/` trong cùng URL

## DANH SÁCH CHỦ ĐỀ CHÍNH

1. **Bảo hiểm** (2 đề mục)
   - Bảo hiểm y tế: `/van-ban/de-muc/bao-hiem-y-te/`
   - Kinh doanh bảo hiểm: `/van-ban/de-muc/kinh-doanh-bao-hiem/`

2. **An ninh quốc gia** (12 đề mục)
   - An ninh quốc gia: `/van-ban/de-muc/an-ninh-quoc-gia/`
   - An ninh mạng: `/van-ban/de-muc/an-ninh-mang/`

3. **Doanh nghiệp, hợp tác xã** (3 đề mục)
   - Doanh nghiệp: `/van-ban/de-muc/doanh-nghiep/`
   - Hợp tác xã: `/van-ban/de-muc/hop-tac-xa/`

## CÁCH SỬ DỤNG

1. **Từ trang chính**: https://docs.diepxuan.com/van-ban/
2. **Click chủ đề** → đến trang chủ đề
3. **Click đề mục** → đến trang đề mục với nội dung đầy đủ

## LƯU Ý

- Tất cả URLs kết thúc bằng `/`
- Không có `.html` hoặc `.md` trong URL
- URLs sử dụng slug (chữ thường, dấu gạch ngang)

---

*Cập nhật: 2026-02-22*
"""
    
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Đã tạo hướng dẫn URLs: {readme_file}")
    
    print("\n=== HOÀN THÀNH ===")
    print("Đã tạo redirects và hướng dẫn URLs đúng.")

if __name__ == '__main__':
    create_redirect_html()
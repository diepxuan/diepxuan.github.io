#!/usr/bin/env python3
"""
Script tạo cấu trúc markdown phân cấp cho Pháp điển
Cấu trúc:
  van-ban/index.md              # Danh sách 45 chủ đề
  van-ban/chu-de/[slug].md      # Trang chủ đề: danh sách đề mục
  van-ban/de-muc/[slug].md      # Trang đề mục: nội dung đầy đủ
"""

import sqlite3
import os
import re
from urllib.parse import quote

def slugify(text):
    """Chuyển text thành slug cho URL"""
    # Chuyển thành chữ thường
    text = text.lower()
    # Thay thế khoảng trắng và ký tự đặc biệt
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    # Loại bỏ dấu tiếng Việt
    text = text.replace('đ', 'd')
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    return text.strip('-')

def create_chu_de_page(chu_de_id, chu_de_text, demuc_list, output_dir):
    """Tạo trang cho một chủ đề"""
    slug = slugify(chu_de_text)
    filename = os.path.join(output_dir, 'chu-de', f'{slug}.md')
    
    content = f"""---
layout: default
title: {chu_de_text}
permalink: /van-ban/chu-de/{slug}/
---

# {chu_de_text}

**Chủ đề:** {chu_de_text}  
**Số đề mục:** {len(demuc_list)}  
**Cập nhật:** {{% raw %}}{{{{ site.time | date: \"%Y-%m-%d\" }}}}{{% endraw %}}

## 📋 Danh sách Đề mục

"""
    
    for i, (demuc_id, demuc_text, stt) in enumerate(demuc_list, 1):
        demuc_slug = slugify(demuc_text)
        content += f"{i}. **[{demuc_text}](../de-muc/{demuc_slug}/)**\n"
    
    content += f"""

## 🔙 Quay lại
[← Danh sách tất cả Chủ đề](../)

## 📊 Thống kê
- **Tổng số đề mục:** {len(demuc_list)}
- **ID chủ đề:** {chu_de_id}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản trong chủ đề này.

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{% raw %}}{{{{ site.time | date: \"%Y-%m-%d %H:%M\" }}}}{{% endraw %}}*
"""
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return slug, filename

def create_de_muc_page(demuc_id, demuc_text, chude_text, dieukhoan_list, output_dir):
    """Tạo trang cho một đề mục"""
    slug = slugify(demuc_text)
    filename = os.path.join(output_dir, 'de-muc', f'{slug}.md')
    
    # Lấy chủ đề slug để tạo link back
    chude_slug = slugify(chude_text)
    
    content = f"""---
layout: default
title: {demuc_text}
permalink: /van-ban/de-muc/{slug}/
---

# {demuc_text}

**Đề mục:** {demuc_text}  
**Chủ đề:** [{chude_text}](../chu-de/{chude_slug}/)  
**Số điều khoản:** {len(dieukhoan_list)}  
**Cập nhật:** {{% raw %}}{{{{ site.time | date: \"%Y-%m-%d\" }}}}{{% endraw %}}

## 📜 Nội dung Điều khoản

"""
    
    for i, (dieukhoan_id, mapc, chimuc, ten) in enumerate(dieukhoan_list, 1):
        content += f"### {ten}\n\n"
        if chimuc and chimuc.strip():
            content += f"**Chỉ mục:** {chimuc}\n\n"
        if mapc and mapc.strip():
            content += f"**Mã phân cấp:** {mapc}\n\n"
        content += f"**ID:** {dieukhoan_id}\n\n"
        content += "---\n\n"
    
    content += f"""

## 🔙 Quay lại
[← Danh sách đề mục của {chude_text}](../chu-de/{chude_slug}/)  
[← Danh sách tất cả Chủ đề](../../)

## 📊 Thống kê
- **Tổng số điều khoản:** {len(dieukhoan_list)}
- **ID đề mục:** {demuc_id}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{% raw %}}{{{{ site.time | date: \"%Y-%m-%d %H:%M\" }}}}{{% endraw %}}*
"""
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return slug, filename

def create_main_index(chude_list, output_dir):
    """Tạo trang chính với danh sách chủ đề"""
    filename = os.path.join(output_dir, 'index.md')
    
    content = """---
layout: default
title: Bộ Pháp điển Điện tử
permalink: /van-ban/
---

# 📚 Bộ Pháp điển Điện tử

**Nguồn:** Bộ Tư pháp Việt Nam  
**Cập nhật:** {% raw %}{{ site.time | date: "%Y-%m-%d" }}{% endraw %}  
**Phiên bản:** 1.0

## 📊 Tổng quan

Bộ Pháp điển Điện tử là hệ thống pháp luật chính thức của Việt Nam, được Bộ Tư pháp công bố. Hệ thống này bao gồm toàn bộ các văn bản pháp luật được hệ thống hóa theo cấu trúc phân cấp rõ ràng.

### Thống kê
- **45 Chủ đề** pháp luật
- **306 Đề mục** chuyên sâu  
- **76,303 Điều khoản** (chương, điều, khoản, điểm)
- **Database hoàn chỉnh**: `phap-dien/sqlite/phapdien_complete.db` (36MB)
- **Cập nhật** theo quy định pháp luật

## 📋 Danh sách Chủ đề Pháp luật

Nhấp vào tên chủ đề để xem danh sách đề mục:

"""
    
    for i, (chude_id, chude_text, stt, demuc_count) in enumerate(chude_list, 1):
        slug = slugify(chude_text)
        content += f"{i}. **[{chude_text}](chu-de/{slug}/)** - {demuc_count} đề mục\n"
    
    content += """

## 🔍 Cách sử dụng

### 1. Tra cứu theo cấp độ
1. **Chọn chủ đề** từ danh sách trên
2. **Xem danh sách đề mục** thuộc chủ đề
3. **Nhấp vào đề mục** để xem nội dung đầy đủ

### 2. Tìm kiếm nhanh
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

### 3. Query Database
```sql
-- Kết nối database hoàn chỉnh
sqlite3 phap-dien/sqlite/phapdien_complete.db

-- Tìm các điều khoản theo từ khóa
SELECT * FROM dieukhoan WHERE ten LIKE '%thông báo hàng hải%';
```

## 📁 Cấu trúc Dữ liệu

### Database Formats
| Định dạng | Mục đích | Đường dẫn | Số records |
|-----------|----------|-----------|------------|
| **SQLite (Complete)** | Database hoàn chỉnh | `phap-dien/sqlite/phapdien_complete.db` | 76,303 |
| **Markdown** | Hiển thị web | `chu-de/`, `de-muc/` | - |

### Cấu trúc Phân cấp
```
Chủ đề (45)
  ├── Đề mục (306)
  │     ├── Điều khoản (76,303)
  │     │     ├── Chương (I, II, III...)
  │     │     ├── Điều (1, 2, 3...)
  │     │     ├── Khoản (1.1, 1.2...)
  │     │     └── Điểm (1.1.1, 1.1.2...)
```

## 📋 Văn bản Khác

### Hướng dẫn Sử dụng Dịch vụ Internet
- **File**: [WEBHD_INTERNET_UM_v1.0.docx](WEBHD_INTERNET_UM_v1.0.docx)
- **Loại**: Tài liệu Microsoft Word
- **Dung lượng**: 1.05 MB

### Văn bản Tự động Crawl
- **Source**: [vanban.chinhphu.vn](https://vanban.chinhphu.vn)
- **Số lượng**: 10+ documents
- **Tự động cập nhật**: Weekly
- **Xem tại**: [crawled/README.md](crawled/README.md)

## ⚖️ Lưu ý Pháp lý

- Dữ liệu được trích xuất từ **Bộ Pháp điển Điện tử chính thức**
- Chỉ sử dụng cho mục đích **tham khảo, nghiên cứu**
- **Không thay thế** văn bản pháp luật chính thức
- Luôn **kiểm tra** với nguồn chính thức khi áp dụng

## 📞 Liên hệ & Hỗ trợ

- **Vấn đề kỹ thuật**: Mở issue trên GitHub
- **Cập nhật dữ liệu**: Theo dõi Bộ Tư pháp
- **Đề xuất tính năng**: Gửi pull request

## 🔗 Liên kết

- [Bộ Pháp điển Điện tử](https://phapdien.moj.gov.vn/) - Nguồn chính thức
- [GitHub Repository](https://github.com/diepxuan/github-io) - Mã nguồn
- [Website chính](https://docs.diepxuan.com/) - Trang chủ

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {% raw %}{{ site.time | date: "%Y-%m-%d %H:%M" }}{% endraw %}*
"""
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename

def main():
    # Đường dẫn
    db_path = 'sqlite/phapdien_complete.db'
    output_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    # Kết nối database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("=== BẮT ĐẦU TẠO CẤU TRÚC MARKDOWN ===")
    
    # 1. Lấy danh sách chủ đề với số đề mục
    cursor.execute('''
        SELECT c.id, c.text, c.stt, COUNT(d.id) as demuc_count
        FROM chude c
        LEFT JOIN dieukhoan dk ON c.id = dk.chude_id
        LEFT JOIN demuc d ON dk.demuc_id = d.id
        GROUP BY c.id, c.text, c.stt
        ORDER BY c.stt
    ''')
    chude_list = cursor.fetchall()
    
    print(f"Tìm thấy {len(chude_list)} chủ đề")
    
    # 2. Tạo folder structure
    os.makedirs(os.path.join(output_dir, 'chu-de'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'de-muc'), exist_ok=True)
    
    # 3. Tạo trang chính
    main_index = create_main_index(chude_list, output_dir)
    print(f"✓ Đã tạo trang chính: {main_index}")
    
    # 4. Tạo trang cho từng chủ đề
    chude_slugs = {}
    for chude_id, chude_text, stt, demuc_count in chude_list:
        # Lấy danh sách đề mục thuộc chủ đề này
        cursor.execute('''
            SELECT DISTINCT d.id, d.text, d.stt
            FROM demuc d
            JOIN dieukhoan dk ON d.id = dk.demuc_id
            WHERE dk.chude_id = ?
            ORDER BY d.stt
        ''', (chude_id,))
        demuc_list = cursor.fetchall()
        
        # Tạo trang chủ đề
        slug, filename = create_chu_de_page(chude_id, chude_text, demuc_list, output_dir)
        chude_slugs[chude_id] = (slug, chude_text)
        print(f"✓ Đã tạo trang chủ đề: {chude_text} ({len(demuc_list)} đề mục)")
        
        # 5. Tạo trang cho từng đề mục
        for demuc_id, demuc_text, demuc_stt in demuc_list:
            # Lấy danh sách điều khoản thuộc đề mục này
            cursor.execute('''
                SELECT id, mapc, chimuc, ten
                FROM dieukhoan
                WHERE demuc_id = ?
                ORDER BY mapc
            ''', (demuc_id,))
            dieukhoan_list = cursor.fetchall()
            
            # Tạo trang đề mục
            demuc_slug, demuc_filename = create_de_muc_page(
                demuc_id, demuc_text, chude_text, dieukhoan_list, output_dir
            )
            print(f"  ✓ Đã tạo trang đề mục: {demuc_text} ({len(dieukhoan_list)} điều khoản)")
    
    conn.close()
    
    print("\n=== HOÀN THÀNH ===")
    print(f"✓ Đã tạo: 1 trang chính (index.md)")
    print(f"✓ Đã tạo: {len(chude_list)} trang chủ đề (chu-de/)")
    print(f"✓ Đã tạo: ~306 trang đề mục (de-muc/)")
    print(f"✓ Tổng số files: ~352 markdown files")
    print(f"\nOutput directory: {output_dir}")
    print("Cấu trúc:")
    print(f"  {output_dir}/index.md")
    print(f"  {output_dir}/chu-de/[45 files].md")
    print(f"  {output_dir}/de-muc/[306 files].md")

if __name__ == '__main__':
    main()
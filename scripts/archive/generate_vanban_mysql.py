#!/usr/bin/env python3
"""
Generate markdown pages from MySQL vbpl database
URL structure:
- Topic pages: /van-ban/<slug>/
- Subtopic pages: /van-ban/<parent>/<slug>/
"""

import os
import re
from pathlib import Path
import mysql.connector
from mysql.connector import Error

# Đường dẫn tuyệt đối tới file hiện tại
SCRIPT_DIR = Path(__file__).resolve().parent

# Thư mục gốc của repo (vì script nằm trong ./scripts/)
BASE_DIR = SCRIPT_DIR.parent

VB_PATH = os.path.join(BASE_DIR, "van-ban")

# MySQL database configuration
DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

def slugify(text):
    """Convert text to URL-friendly slug"""
    if not text:
        return ''
    
    text = str(text).lower()
    
    # Remove accents and special characters
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    
    # Replace spaces and special chars with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    
    return text

def get_database_connection():
    """Connect to MySQL database"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"✗ Lỗi kết nối database: {e}")
        return None

def get_content_stats():
    """Get statistics about content coverage"""
    conn = get_database_connection()
    if not conn:
        return {'total_provisions': 0, 'subtopics_with_content': 0, 'total_subtopics': 0, 'coverage': 0}
    
    cursor = conn.cursor()
    
    try:
        # Total provisions
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan")
        total_provisions = cursor.fetchone()[0] or 0
        
        # Provisions with content (from de_muc_content)
        cursor.execute("SELECT COUNT(DISTINCT dmc.de_muc_id) FROM de_muc_content dmc")
        subtopics_with_content = cursor.fetchone()[0] or 0
        
        # Content coverage percentage (based on subtopics)
        cursor.execute("SELECT COUNT(*) FROM de_muc")
        total_subtopics = cursor.fetchone()[0] or 0
        coverage = (subtopics_with_content / total_subtopics * 100) if total_subtopics > 0 else 0
        
        return {
            'total_provisions': total_provisions,
            'subtopics_with_content': subtopics_with_content,
            'total_subtopics': total_subtopics,
            'coverage': coverage
        }
        
    except Error as e:
        print(f"✗ Lỗi get_content_stats: {e}")
        return {'total_provisions': 0, 'subtopics_with_content': 0, 'total_subtopics': 0, 'coverage': 0}
    finally:
        cursor.close()
        conn.close()

def get_topics():
    """Get all topics from database"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT id, text, stt 
            FROM chu_de 
            ORDER BY CAST(stt AS UNSIGNED)
        """)
        
        topics = []
        for row in cursor.fetchall():
            topic_id, name, stt = row
            
            # Get subtopic count
            cursor.execute("""
                SELECT COUNT(DISTINCT id) 
                FROM de_muc 
                WHERE chu_de_id = %s
            """, (topic_id,))
            subtopic_count = cursor.fetchone()[0] or 0
            
            # Get provision count
            cursor.execute("SELECT COUNT(*) FROM dieu_khoan WHERE chu_de_id = %s", (topic_id,))
            provision_count = cursor.fetchone()[0] or 0
            
            slug = slugify(name)
            topics.append({
                'id': topic_id,
                'name': name,
                'stt': stt,
                'slug': slug,
                'subtopic_count': subtopic_count,
                'provision_count': provision_count
            })
        
        return topics
        
    except Error as e:
        print(f"✗ Lỗi get_topics: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_subtopics_by_topic(topic_id):
    """Get all subtopics for a topic"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT id, text, stt
            FROM de_muc 
            WHERE chu_de_id = %s
            ORDER BY CAST(stt AS UNSIGNED)
        """, (topic_id,))
        
        subtopics = []
        for row in cursor.fetchall():
            subtopic_id, name, stt = row
            
            # Get provision count
            cursor.execute("SELECT COUNT(*) FROM dieu_khoan WHERE de_muc_id = %s", (subtopic_id,))
            provision_count = cursor.fetchone()[0] or 0
            
            # Check if has content
            cursor.execute("SELECT COUNT(*) FROM de_muc_content WHERE de_muc_id = %s", (subtopic_id,))
            has_content = cursor.fetchone()[0] > 0
            
            slug = slugify(name)
            subtopics.append({
                'id': subtopic_id,
                'name': name,
                'stt': stt,
                'slug': slug,
                'provision_count': provision_count,
                'has_content': has_content
            })
        
        return subtopics
        
    except Error as e:
        print(f"✗ Lỗi get_subtopics_by_topic: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_provisions_by_subtopic(subtopic_id):
    """Get all provisions for a subtopic"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT id, ten, chi_muc, mapc
            FROM dieu_khoan 
            WHERE de_muc_id = %s
            ORDER BY mapc
        """, (subtopic_id,))
        
        provisions = []
        for row in cursor.fetchall():
            provision_id, name, index, mapc = row
            
            provisions.append({
                'id': provision_id,
                'name': name,
                'index': index or '',
                'mapc': mapc or ''
            })
        
        return provisions
        
    except Error as e:
        print(f"✗ Lỗi get_provisions_by_subtopic: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_subtopic_content(subtopic_id):
    """Get HTML content for a subtopic"""
    conn = get_database_connection()
    if not conn:
        return None
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT html_content 
            FROM de_muc_content 
            WHERE de_muc_id = %s
            LIMIT 1
        """, (subtopic_id,))
        
        result = cursor.fetchone()
        content = result[0] if result else None
        
        return content
        
    except Error as e:
        print(f"✗ Lỗi get_subtopic_content: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def html_to_markdown(html_content):
    """Convert HTML to Markdown (simplified version)"""
    if not html_content:
        return ""
    
    # Simple HTML to Markdown conversion
    markdown = html_content
    
    # Replace headers
    markdown = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', markdown)
    markdown = re.sub(r'<p class="pChuong"[^>]*>(.*?)</p>', r'## \1\n', markdown)
    markdown = re.sub(r'<p class="pDieu"[^>]*>(.*?)</p>', r'### \1\n', markdown)
    markdown = re.sub(r'<p class="pNoiDung"[^>]*>(.*?)</p>', r'\1\n', markdown)
    
    # Remove HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)
    
    # Clean up whitespace
    markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
    
    return markdown.strip()

def generate_topic_page(topic, subtopics):
    """Generate markdown for a topic page"""
    content = f"""---
layout: default
title: {topic['name']}
permalink: /van-ban/{topic['slug']}/
collection: topics
slug: {topic['slug']}
---

# {topic['name']}

**Chủ đề:** {topic['name']}  
**STT:** {topic['stt']}  
**Số đề mục:** {topic['subtopic_count']}  
**Số điều khoản:** {topic['provision_count']:,}  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 📋 Danh sách Đề mục

"""
    
    for i, subtopic in enumerate(subtopics, 1):
        content_icon = "📄" if subtopic['has_content'] else "📝"
        content += f"{i}. **[{subtopic['name']}](/van-ban/{topic['slug']}/{subtopic['slug']}/)** {content_icon} - {subtopic['provision_count']:,} điều khoản\n"
    
    footer = '''---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}'''
    
    content += f"""

## 🔙 Quay lại
[← Danh sách tất cả Chủ đề](/van-ban/)

## 📊 Thống kê
- **Tổng số đề mục:** {topic['subtopic_count']}
- **Tổng số điều khoản:** {topic['provision_count']:,}
- **ID chủ đề:** {topic['id']}

## 🔍 Cách sử dụng
1. **Chọn đề mục** từ danh sách trên
2. **Xem nội dung đầy đủ** của đề mục
3. **Sử dụng tìm kiếm** để tìm văn bản cụ thể

{footer}"""
    
    return content

def generate_subtopic_page(topic, subtopic, provisions, html_content):
    """Generate markdown for a subtopic page WITH CONTENT"""
    # Convert HTML to Markdown
    markdown_content = html_to_markdown(html_content) if html_content else "*Nội dung chưa có sẵn*"
    
    content = f"""---
layout: default
title: {subtopic['name']}
permalink: /van-ban/{topic['slug']}/{subtopic['slug']}/
collection: subtopics
slug: {subtopic['slug']}
parent: {topic['slug']}
---

# {subtopic['name']}

**Đề mục:** {subtopic['name']}  
**STT:** {subtopic['stt']}  
**Chủ đề:** [{topic['name']}](/van-ban/{topic['slug']}/)  
**Số điều khoản:** {subtopic['provision_count']}  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 📊 Danh sách Điều khoản

"""
    
    # List all provisions
    for i, provision in enumerate(provisions, 1):
        index_display = provision['index'] if provision['index'] else f"Điều {i}"
        content += f"{i}. **{provision['name']}** - Chỉ mục: {index_display}\n"
    
    content += f"""

## 📜 Nội dung Đề mục

{markdown_content}

## 🔙 Quay lại
[← Danh sách đề mục của {topic['name']}](/van-ban/{topic['slug']}/)  
[← Danh sách tất cả Chủ đề](/van-ban/)

## 📊 Thống kê
- **Tổng số điều khoản:** {subtopic['provision_count']}
- **ID đề mục:** {subtopic['id']}
- **Có nội dung:** {'Có' if html_content else 'Không'}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_index_page(topics, stats):
    """Generate main index page"""
    content = f"""---
layout: default
title: Bộ Pháp điển Điện tử
permalink: /van-ban/
---

# 📚 Bộ Pháp điển Điện tử

**Nguồn:** Bộ Tư pháp Việt Nam  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}
**Database:** MySQL vbpl

## 📊 Tổng quan

Bộ Pháp điển Điện tử là hệ thống pháp luật chính thức của Việt Nam, được Bộ Tư pháp công bố. Hệ thống này bao gồm toàn bộ các văn bản pháp luật được hệ thống hóa theo cấu trúc phân cấp rõ ràng.

### Thống kê Nội dung
- **{len(topics)} Chủ đề** pháp luật
- **{stats['total_subtopics']} Đề mục** chuyên sâu  
- **{stats['total_provisions']:,} Điều khoản** (chương, điều, khoản, điểm)
- **{stats['subtopics_with_content']} Đề mục có nội dung** ({stats['coverage']:.1f}%)
- **Database:** MySQL `vbpl` (với nội dung HTML đầy đủ)

## 📋 Danh sách Chủ đề Pháp luật

Nhấp vào tên chủ đề để xem danh sách đề mục:

"""
    
    for i, topic in enumerate(topics, 1):
        content += f"{i}. **[{topic['name']}]({{{{ site.baseurl }}}}/{topic['slug']}/)** - {topic['subtopic_count']} đề mục ({topic['provision_count']:,} điều khoản)\n"
    
    content += """

## 🔍 Cách sử dụng

### 1. Tra cứu theo cấp độ
1. **Chọn chủ đề** từ danh sách trên
2. **Xem danh sách đề mục** thuộc chủ đề
3. **Nhấp vào đề mục** để xem nội dung đầy đủ

### 2. Tìm kiếm nhanh
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

### 3. Query Database với Nội dung
```sql
-- Kết nối MySQL database
mysql -h mysql.diepxuan.corp -u vbpl -p'G]9E9S_TahIFVbq-' vbpl

-- Tìm các đề mục theo nội dung
SELECT dm.text, dmc.html_content 
FROM de_muc dm
JOIN de_muc_content dmc ON dm.id = dmc.de_muc_id
WHERE dmc.html_content LIKE '%thông báo hàng hải%';
```

## 📁 Cấu trúc Dữ liệu

### Database Structure
| Bảng | Mục đích | Số records |
|------|----------|------------|
| **chu_de** | Chủ đề | {len(topics)} |
| **de_muc** | Đề mục | {stats['total_subtopics']} |
| **dieu_khoan** | Điều khoản | {stats['total_provisions']:,} |
| **de_muc_content** | Nội dung HTML đề mục | {stats['subtopics_with_content']} |

### Cấu trúc Phân cấp
```
Chủ đề ({len(topics)})
  ├── Đề mục ({stats['total_subtopics']})
  │     ├── Điều khoản ({stats['total_provisions']:,})
  │     │     ├── Chương (I, II, III...)
  │     │     ├── Điều (1, 2, 3...)
  │     │     ├── Khoản (1.1, 1.2...)
  │     │     └── Điểm (1.1.1, 1.1.2...)
```

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

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_vanban_index_page(topics, stats):
    """Generate van-ban/index.md page (main website index)"""
    content = f"""---
layout: default
title: Văn bản Pháp luật
permalink: /van-ban/
---

# 📚 Văn bản Pháp luật

## Bộ Pháp điển Điện tử

Hệ thống pháp luật chính thức của Việt Nam, được Bộ Tư pháp công bố.

### Thống kê Nội dung
- **{len(topics)} Chủ đề** pháp luật
- **{stats['total_subtopics']} Đề mục** chuyên sâu  
- **{stats['total_provisions']:,} Điều khoản** (chương, điều, khoản, điểm)
- **{stats['subtopics_with_content']} Đề mục có nội dung** ({stats['coverage']:.1f}%)

## 📋 Danh sách Chủ đề Pháp luật

Nhấp vào tên chủ đề để xem danh sách đề mục:

"""
    
    for i, topic in enumerate(topics, 1):
        content += f"{i}. **[{topic['name']}](/van-ban/{topic['slug']}/)** - {topic['subtopic_count']} đề mục ({topic['provision_count']:,} điều khoản)\n"
    
    content += """

## 🔍 Cách sử dụng

### 1. Tra cứu theo cấp độ
1. **Chọn chủ đề** từ danh sách trên
2. **Xem danh sách đề mục** thuộc chủ đề
3. **Nhấp vào đề mục** để xem nội dung đầy đủ

### 2. Tìm kiếm nhanh
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

## ⚖️ Lưu ý Pháp lý

- Dữ liệu được trích xuất từ **Bộ Pháp điển Điện tử chính thức**
- Chỉ sử dụng cho mục đích **tham khảo, nghiên cứu**
- **Không thay thế** văn bản pháp luật chính thức
- Luôn **kiểm tra** với nguồn chính thức khi áp dụng

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_all_pages():
    """Generate all pages with new URL structure"""
    output_dir = VB_PATH
    vanban_dir = VB_PATH
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Get data from database
    print("📊 Loading data from MySQL database (vbpl)...")
    topics = get_topics()
    
    if not topics:
        print("✗ Không có dữ liệu từ database")
        return
    
    print(f"✅ Found {len(topics)} topics")
    
    # Get content statistics
    stats = get_content_stats()
    print(f"📊 Content coverage: {stats['subtopics_with_content']}/{stats['total_subtopics']} đề mục có nội dung ({stats['coverage']:.1f}%)")
    
    # Generate van-ban/index.md (main website index)
    print("\n📄 Generating van-ban/index.md (main website index)...")
    vanban_index_content = generate_vanban_index_page(topics, stats)
    vanban_index_path = os.path.join(vanban_dir, "index.md")
    
    with open(vanban_index_path, 'w', encoding='utf-8') as f:
        f.write(vanban_index_content)
    print(f"✅ van-ban/index.md saved: {vanban_index_path}")
    
    total_subtopics = 0
    subtopics_with_content = 0
    
    # Generate topic pages and subtopic pages
    for topic in topics:
        print(f"\n📁 Processing topic: {topic['name']}")
        
        # Get subtopics for this topic
        subtopics = get_subtopics_by_topic(topic['id'])
        
        # Create topic directory
        topic_dir = os.path.join(output_dir, topic['slug'])
        Path(topic_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate topic page
        topic_content = generate_topic_page(topic, subtopics)
        topic_path = os.path.join(output_dir, f"{topic['slug']}.md")
        
        with open(topic_path, 'w', encoding='utf-8') as f:
            f.write(topic_content)
        print(f"  ✅ Topic page: {topic['slug']}.md")
        
        # Generate subtopic pages
        for subtopic in subtopics:
            # Get provisions for this subtopic
            provisions = get_provisions_by_subtopic(subtopic['id'])
            
            # Get HTML content
            html_content = get_subtopic_content(subtopic['id'])
            
            # Generate subtopic page
            subtopic_content = generate_subtopic_page(topic, subtopic, provisions, html_content)
            subtopic_path = os.path.join(topic_dir, f"{subtopic['slug']}.md")
            
            with open(subtopic_path, 'w', encoding='utf-8') as f:
                f.write(subtopic_content)
            
            total_subtopics += 1
            if html_content:
                subtopics_with_content += 1
        
        print(f"  ✅ {len(subtopics)} subtopic pages in {topic['slug']}/")
    
    # Calculate overall coverage
    overall_coverage = (subtopics_with_content / total_subtopics * 100) if total_subtopics > 0 else 0
    
    print(f"\n🎉 GENERATION COMPLETE!")
    print(f"📊 Statistics:")
    print(f"  - Topics: {len(topics)}")
    print(f"  - Subtopics: {total_subtopics}")
    print(f"  - Subtopics with content: {subtopics_with_content} ({overall_coverage:.1f}%)")
    print(f"  - Total pages: {len(topics) + total_subtopics + 1}")
    print(f"📁 Output directory: {output_dir}")
    print(f"🔗 URL Structure:")
    print(f"  - Homepage: /van-ban/")
    print(f"  - Topic pages: /van-ban/<slug>/")
    print(f"  - Subtopic pages: /van-ban/<topic>/<subtopic>/")

if __name__ == "__main__":
    generate_all_pages()
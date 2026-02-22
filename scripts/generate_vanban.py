#!/usr/bin/env python3
"""
Generate markdown pages from database with NEW URL structure
NEW STRUCTURE:
- Topic pages: /van-ban/<slug>/
- Subtopic pages: /van-ban/<parent>/<slug>/
"""

import sqlite3
import os
import re
from pathlib import Path

# Đường dẫn tuyệt đối tới file hiện tại
SCRIPT_DIR = Path(__file__).resolve().parent

# Thư mục gốc của repo (vì script nằm trong ./scripts/)
BASE_DIR = SCRIPT_DIR.parent

VB_PATH = os.path.join(BASE_DIR, "van-ban")
DB_PATH = os.path.join (VB_PATH, "phap-dien/sqlite/phapdien_complete.db")

def slugify(text):
    """Convert text to URL-friendly slug"""
    # Remove accents and special characters
    text = text.lower()
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
    """Connect to SQLite database"""
    db_path = DB_PATH
    return sqlite3.connect(db_path)

def get_topics():
    """Get all topics from database"""
    conn = get_database_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, text, stt 
        FROM chude 
        ORDER BY CAST(SUBSTR(stt, 1, 2) AS INTEGER)
    """)
    
    topics = []
    for row in cursor.fetchall():
        topic_id, name, stt = row
        
        # Get subtopic count - count distinct demuc_id from dieukhoan for this chude
        cursor.execute("""
            SELECT COUNT(DISTINCT demuc_id) 
            FROM dieukhoan 
            WHERE chude_id = ?
        """, (topic_id,))
        subtopic_count = cursor.fetchone()[0] or 0
        
        # Get provision count
        cursor.execute("SELECT COUNT(*) FROM dieukhoan WHERE chude_id = ?", (topic_id,))
        provision_count = cursor.fetchone()[0] or 0
        
        slug = slugify(name)
        topics.append({
            'id': topic_id,
            'name': name,
            'slug': slug,
            'subtopic_count': subtopic_count,
            'provision_count': provision_count
        })
    
    conn.close()
    return topics

def get_subtopics_by_topic(topic_id):
    """Get all subtopics for a topic"""
    conn = get_database_connection()
    cursor = conn.cursor()
    
    # Get distinct demuc_id from dieukhoan for this chude
    cursor.execute("""
        SELECT DISTINCT dk.demuc_id, dm.text
        FROM dieukhoan dk
        JOIN demuc dm ON dk.demuc_id = dm.id
        WHERE dk.chude_id = ?
        ORDER BY dm.text
    """, (topic_id,))
    
    subtopics = []
    for row in cursor.fetchall():
        subtopic_id, name = row
        
        # Get provision count
        cursor.execute("SELECT COUNT(*) FROM dieukhoan WHERE demuc_id = ?", (subtopic_id,))
        provision_count = cursor.fetchone()[0] or 0
        
        slug = slugify(name)
        subtopics.append({
            'id': subtopic_id,
            'name': name,
            'slug': slug,
            'provision_count': provision_count
        })
    
    conn.close()
    return subtopics

def get_provisions_by_subtopic(subtopic_id):
    """Get all provisions for a subtopic"""
    conn = get_database_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, ten, chimuc, mapc
        FROM dieukhoan 
        WHERE demuc_id = ?
        ORDER BY chimuc
    """, (subtopic_id,))
    
    provisions = []
    for row in cursor.fetchall():
        provision_id, name, index, mapc = row
        provisions.append({
            'id': provision_id,
            'name': name,
            'index': index,
            'mapc': mapc,
            'content': ""  # No content column in this database
        })
    
    conn.close()
    return provisions

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
**Số đề mục:** {topic['subtopic_count']}  
**Số điều khoản:** {topic['provision_count']:,}  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 📋 Danh sách Đề mục

"""
    
    for i, subtopic in enumerate(subtopics, 1):
        content += f"{i}. **[{subtopic['name']}](/van-ban/{topic['slug']}/{subtopic['slug']}/)** - {subtopic['provision_count']:,} điều khoản\n"
    
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

def generate_subtopic_page(topic, subtopic, provisions):
    """Generate markdown for a subtopic page"""
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
**Chủ đề:** [{topic['name']}](/van-ban/{topic['slug']}/)  
**Số điều khoản:** {subtopic['provision_count']}  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 📜 Nội dung Điều khoản

"""
    
    current_chapter = None
    
    for provision in provisions:
        # Check if this is a chapter
        if provision['index'].isdigit() or ('.' not in provision['index'] and provision['index'].isalpha()):
            # This is likely a chapter
            if current_chapter != provision['name']:
                current_chapter = provision['name']
                content += f"\n### {current_chapter}\n\n"
                content += f"**Chỉ mục:** {provision['index']}\n\n"
                content += f"**Mã phân cấp:** {provision['mapc']}\n\n"
                content += f"**ID:** {provision['id']}\n\n"
                content += "---\n\n"
        else:
            # This is a provision
            content += f"### {provision['name']}\n\n"
            content += f"**Chỉ mục:** {provision['index']}\n\n"
            content += f"**Mã phân cấp:** {provision['mapc']}\n\n"
            content += f"**ID:** {provision['id']}\n\n"
            
            if provision['content']:
                content += f"{provision['content']}\n\n"
            
            content += "---\n\n"
    
    footer = '''---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}'''
    
    content += f"""

## 🔙 Quay lại
[← Danh sách đề mục của {topic['name']}](/van-ban/{topic['slug']}/)  
[← Danh sách tất cả Chủ đề](/van-ban/)

## 📊 Thống kê
- **Tổng số điều khoản:** {subtopic['provision_count']}
- **ID đề mục:** {subtopic['id']}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

{footer}"""
    
    return content

def generate_index_page(topics):
    """Generate main index page"""
    content = """---
layout: default
title: Bộ Pháp điển Điện tử
permalink: /van-ban/
---

# 📚 Bộ Pháp điển Điện tử

**Nguồn:** Bộ Tư pháp Việt Nam  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}
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
| **Markdown** | Hiển thị web | `pages/` | - |

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

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_vanban_index_page(topics):
    """Generate van-ban/index.md page (main website index)"""
    content = """---
layout: default
title: Văn bản Pháp luật
permalink: /van-ban/
---

# 📚 Văn bản Pháp luật

## Bộ Pháp điển Điện tử

Hệ thống pháp luật chính thức của Việt Nam, được Bộ Tư pháp công bố.

### Thống kê
- **45 Chủ đề** pháp luật
- **306 Đề mục** chuyên sâu  
- **76,303 Điều khoản** (chương, điều, khoản, điểm)

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

## 📁 Văn bản Khác

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
    print("📊 Loading data from database...")
    topics = get_topics()
    
    print(f"✅ Found {len(topics)} topics")
    
    # Generate index page for _pages collection
    # print("\n📄 Generating index page for _pages collection...")
    # index_content = generate_index_page(topics)
    # index_path = os.path.join(output_dir, "index.md")
    
    # with open(index_path, 'w', encoding='utf-8') as f:
    #     f.write(index_content)
    # print(f"✅ Index page saved: {index_path}")
    
    # Generate van-ban/index.md (main website index)
    print("\n📄 Generating van-ban/index.md (main website index)...")
    vanban_index_content = generate_vanban_index_page(topics)
    vanban_index_path = os.path.join(vanban_dir, "index.md")
    
    with open(vanban_index_path, 'w', encoding='utf-8') as f:
        f.write(vanban_index_content)
    print(f"✅ van-ban/index.md saved: {vanban_index_path}")
    
    total_subtopics = 0
    
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
            
            # Generate subtopic page
            subtopic_content = generate_subtopic_page(topic, subtopic, provisions)
            subtopic_path = os.path.join(topic_dir, f"{subtopic['slug']}.md")
            
            with open(subtopic_path, 'w', encoding='utf-8') as f:
                f.write(subtopic_content)
            
            total_subtopics += 1
        
        print(f"  ✅ {len(subtopics)} subtopic pages in {topic['slug']}/")
    
    print(f"\n🎉 GENERATION COMPLETE!")
    print(f"📊 Statistics:")
    print(f"  - Topics: {len(topics)}")
    print(f"  - Subtopics: {total_subtopics}")
    print(f"  - Total pages: {len(topics) + total_subtopics + 2} (including both indexes)")
    print(f"📁 Output directories:")
    print(f"  - _pages/: {output_dir}")
    print(f"  - van-ban/: {vanban_dir}")
    print(f"🔗 URL Structure:")
    print(f"  - Homepage: /van-ban/")
    print(f"  - Topic pages: /van-ban/<slug>/")
    print(f"  - Subtopic pages: /van-ban/<topic>/<subtopic>/")

if __name__ == "__main__":
    generate_all_pages()
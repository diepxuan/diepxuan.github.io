#!/usr/bin/env python3
"""
Generate FULL markdown pages from MySQL vbpl database
Generate all 45 topics and 306 subtopics
"""

import os
import re
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import time

# Đường dẫn
SCRIPT_DIR = Path(__file__).resolve().parent
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
    
    # Remove accents
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[đ]', 'd', text)
    
    # Replace spaces and special chars
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    
    return text

def get_database_connection():
    """Connect to MySQL database"""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"✗ Lỗi kết nối: {e}")
        return None

def get_stats():
    """Get database statistics"""
    conn = get_database_connection()
    if not conn:
        return {}
    
    cursor = conn.cursor()
    stats = {}
    
    try:
        # Total counts
        cursor.execute("SELECT COUNT(*) FROM chu_de")
        stats['total_topics'] = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM de_muc")
        stats['total_subtopics'] = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan")
        stats['total_provisions'] = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(DISTINCT de_muc_id) FROM de_muc_content")
        stats['subtopics_with_content'] = cursor.fetchone()[0] or 0
        
        # Coverage
        if stats['total_subtopics'] > 0:
            stats['coverage'] = (stats['subtopics_with_content'] / stats['total_subtopics'] * 100)
        else:
            stats['coverage'] = 0
        
        return stats
        
    except Error as e:
        print(f"✗ Lỗi get_stats: {e}")
        return {}
    finally:
        cursor.close()
        conn.close()

def get_all_topics():
    """Get all topics from database"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    topics = []
    
    try:
        cursor.execute("SELECT id, text, stt FROM chu_de ORDER BY CAST(stt AS UNSIGNED)")
        
        for row in cursor.fetchall():
            topic_id, name, stt = row
            
            # Get counts
            cursor.execute("SELECT COUNT(*) FROM de_muc WHERE chu_de_id = %s", (topic_id,))
            subtopic_count = cursor.fetchone()[0] or 0
            
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
        print(f"✗ Lỗi get_all_topics: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_all_subtopics_by_topic(topic_id):
    """Get all subtopics for a topic"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    subtopics = []
    
    try:
        cursor.execute("""
            SELECT id, text, stt 
            FROM de_muc 
            WHERE chu_de_id = %s 
            ORDER BY CAST(stt AS UNSIGNED)
        """, (topic_id,))
        
        for row in cursor.fetchall():
            subtopic_id, name, stt = row
            
            # Get provision count
            cursor.execute("SELECT COUNT(*) FROM dieu_khoan WHERE de_muc_id = %s", (subtopic_id,))
            provision_count = cursor.fetchone()[0] or 0
            
            # Check content
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
        print(f"✗ Lỗi get_all_subtopics_by_topic: {e}")
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
        cursor.execute("SELECT html_content FROM de_muc_content WHERE de_muc_id = %s LIMIT 1", (subtopic_id,))
        result = cursor.fetchone()
        return result[0] if result else None
        
    except Error as e:
        print(f"✗ Lỗi get_subtopic_content: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def html_to_markdown_better(html):
    """Better HTML to Markdown conversion"""
    if not html:
        return "*Nội dung chưa có sẵn*"
    
    # Extract main content
    import re
    
    # Remove BOM and clean
    html = html.replace('\ufeff', '')
    
    # Extract content between <div class='_content'> tags
    content_match = re.search(r"<div class='_content'>(.*?)</div>", html, re.DOTALL)
    if content_match:
        content = content_match.group(1)
    else:
        content = html
    
    # Remove script and style tags
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?</style>', '', content, flags=re.DOTALL)
    
    # Convert headers
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'## \1\n', content)
    content = re.sub(r'<p class="pChuong"[^>]*>(.*?)</p>', r'### \1\n', content)
    content = re.sub(r'<p class="pDieu"[^>]*>(.*?)</p>', r'#### \1\n', content)
    content = re.sub(r'<p class="pNoiDung"[^>]*>(.*?)</p>', r'\1\n', content)
    
    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = content.strip()
    
    # Limit length
    if len(content) > 50000:
        content = content[:50000] + "\n\n... (nội dung còn tiếp)"
    
    return content

def generate_index_page(stats):
    """Generate main index page"""
    content = f"""---
layout: default
title: Văn bản Pháp luật
permalink: /van-ban/
---

# 📚 Văn bản Pháp luật

## Bộ Pháp điển Điện tử

Hệ thống pháp luật chính thức của Việt Nam, được Bộ Tư pháp công bố.

### Thống kê Đầy đủ
- **{stats['total_topics']} Chủ đề** pháp luật
- **{stats['total_subtopics']} Đề mục** chuyên sâu  
- **{stats['total_provisions']:,} Điều khoản** (chương, điều, khoản, điểm)
- **{stats['subtopics_with_content']} Đề mục có nội dung** ({stats['coverage']:.1f}%)
- **Database:** MySQL `vbpl` (với nội dung HTML đầy đủ)

## 📋 Danh sách Chủ đề Pháp luật

Nhấp vào tên chủ đề để xem danh sách đề mục:

"""
    
    # Get topics for listing
    topics = get_all_topics()
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

### 3. Query Database
```sql
-- Kết nối MySQL database
mysql -h mysql.diepxuan.corp -u vbpl -p'G]9E9S_TahIFVbq-' vbpl

-- Tìm đề mục theo nội dung
SELECT dm.text, dmc.html_content 
FROM de_muc dm
JOIN de_muc_content dmc ON dm.id = dmc.de_muc_id
WHERE dmc.html_content LIKE '%thông báo hàng hải%';
```

## 📁 Cấu trúc Dữ liệu

### Database Structure
| Bảng | Mục đích | Số records |
|------|----------|------------|
| **chu_de** | Chủ đề | {stats['total_topics']} |
| **de_muc** | Đề mục | {stats['total_subtopics']} |
| **dieu_khoan** | Điều khoản | {stats['total_provisions']:,} |
| **de_muc_content** | Nội dung HTML đề mục | {stats['subtopics_with_content']} |

## ⚖️ Lưu ý Pháp lý

- Dữ liệu được trích xuất từ **Bộ Pháp điển Điện tử chính thức**
- Chỉ sử dụng cho mục đích **tham khảo, nghiên cứu**
- **Không thay thế** văn bản pháp luật chính thức
- Luôn **kiểm tra** với nguồn chính thức khi áp dụng

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_topic_page(topic, subtopics):
    """Generate markdown for a topic page"""
    content = f"""---
layout: default
title: {topic['name']}
permalink: /van-ban/{topic['slug']}/
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

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_subtopic_page(topic, subtopic, html_content):
    """Generate markdown for a subtopic page WITH CONTENT"""
    markdown_content = html_to_markdown_better(html_content) if html_content else "*Nội dung chưa có sẵn*"
    
    content = f"""---
layout: default
title: {subtopic['name']}
permalink: /van-ban/{topic['slug']}/{subtopic['slug']}/
---

# {subtopic['name']}

**Đề mục:** {subtopic['name']}  
**STT:** {subtopic['stt']}  
**Chủ đề:** [{topic['name']}](/van-ban/{topic['slug']}/)  
**Số điều khoản:** {subtopic['provision_count']:,}  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 📜 Nội dung Đề mục

{markdown_content}

## 🔙 Quay lại
[← Danh sách đề mục của {topic['name']}](/van-ban/{topic['slug']}/)  
[← Danh sách tất cả Chủ đề](/van-ban/)

## 📊 Thống kê
- **Tổng số điều khoản:** {subtopic['provision_count']:,}
- **ID đề mục:** {subtopic['id']}
- **Có nội dung:** {'Có' if html_content else 'Không'}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def main():
    print("=== GENERATE FULL VAN-BAN PAGES ===")
    start_time = time.time()
    
    # Create output directory
    Path(VB_PATH).mkdir(parents=True, exist_ok=True)
    
    # Get statistics
    print("📊 Loading database statistics...")
    stats = get_stats()
    print(f"✅ Statistics: {stats['total_topics']} topics, {stats['total_subtopics']} subtopics, {stats['total_provisions']:,} provisions")
    print(f"   Content coverage: {stats['subtopics_with_content']}/{stats['total_subtopics']} ({stats['coverage']:.1f}%)")
    
    # Generate index page
    print("\n📄 Generating index page...")
    index_content = generate_index_page(stats)
    index_path = os.path.join(VB_PATH, "index.md")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✅ Index page: {index_path}")
    
    # Get all topics
    print("\n📊 Loading all topics...")
    topics = get_all_topics()
    print(f"✅ Loaded {len(topics)} topics")
    
    total_subtopics = 0
    subtopics_with_content = 0
    
    # Generate topic and subtopic pages
    for topic_idx, topic in enumerate(topics, 1):
        print(f"\n📁 Processing topic {topic_idx}/{len(topics)}: {topic['name']}")
        
        # Get all subtopics for this topic
        subtopics = get_all_subtopics_by_topic(topic['id'])
        
        # Create topic directory
        topic_dir = os.path.join(VB_PATH, topic['slug'])
        Path(topic_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate topic page
        topic_content = generate_topic_page(topic, subtopics)
        topic_path = os.path.join(VB_PATH, f"{topic['slug']}.md")
        
        with open(topic_path, 'w', encoding='utf-8') as f:
            f.write(topic_content)
        print(f"  ✅ Topic page: {topic['slug']}.md")
        
        # Generate subtopic pages
        for subtopic_idx, subtopic in enumerate(subtopics, 1):
            # Get content
            html_content = get_subtopic_content(subtopic['id'])
            
            # Generate page
            subtopic_content = generate_subtopic_page(topic, subtopic, html_content)
            subtopic_path = os.path.join(topic_dir, f"{subtopic['slug']}.md")
            
            with open(subtopic_path, 'w', encoding='utf-8') as f:
                f.write(subtopic_content)
            
            total_subtopics += 1
            if html_content:
                subtopics_with_content += 1
            
            # Progress indicator
            if subtopic_idx % 10 == 0 or subtopic_idx == len(subtopics):
                print(f"    ✅ {subtopic_idx}/{len(subtopics)} subtopic pages")
        
        print(f"  ✅ Completed: {len(subtopics)} subtopic pages")
    
    # Calculate final statistics
    elapsed_time = time.time() - start_time
    overall_coverage = (subtopics_with_content / total_subtopics * 100) if total_subtopics > 0 else 0
    
    print(f"\n🎉 GENERATION COMPLETE!")
    print(f"⏱️  Time elapsed: {elapsed_time:.1f} seconds")
    print(f"📊 Final Statistics:")
    print(f"  - Topics: {len(topics)}")
    print(f"  - Subtopics: {total_subtopics}")
    print(f"  - Subtopics with content: {subtopics_with_content} ({overall_coverage:.1f}%)")
    print(f"  - Total pages generated: {1 + len(topics) + total_subtopics}")
    print(f"📁 Output directory: {VB_PATH}")
    print(f"🔗 URL Structure:")
    print(f"  - Homepage: /van-ban/")
    print(f"  - Topic pages: /van-ban/<slug>/")
    print(f"  - Subtopic pages: /van-ban/<topic>/<subtopic>/")

if __name__ == "__main__":
    main()
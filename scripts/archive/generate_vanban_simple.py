#!/usr/bin/env python3
"""
Generate markdown pages đơn giản - chỉ 2 chủ đề đầu tiên
"""

import os
import re
from pathlib import Path
import mysql.connector
from mysql.connector import Error

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

def get_topics(limit=2):
    """Get first few topics"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    topics = []
    
    try:
        cursor.execute("SELECT id, text, stt FROM chu_de ORDER BY CAST(stt AS UNSIGNED) LIMIT %s", (limit,))
        
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
        print(f"✗ Lỗi: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_subtopics_by_topic(topic_id, limit=3):
    """Get first few subtopics for a topic"""
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
            LIMIT %s
        """, (topic_id, limit))
        
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
        print(f"✗ Lỗi: {e}")
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
        print(f"✗ Lỗi: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def html_to_markdown_simple(html):
    """Simple HTML to Markdown conversion"""
    if not html:
        return "*Nội dung chưa có sẵn*"
    
    # Extract text between <p class="pNoiDung"> tags
    import re
    content = html
    
    # Get first 5000 characters
    content = content[:5000]
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()
    
    if len(content) > 1000:
        content = content[:1000] + "..."
    
    return content

def generate_index_page(topics):
    """Generate main index page"""
    content = f"""---
layout: default
title: Văn bản Pháp luật
permalink: /van-ban/
---

# 📚 Văn bản Pháp luật

## Bộ Pháp điển Điện tử

Hệ thống pháp luật chính thức của Việt Nam.

### Thống kê (Sample)
- **{len(topics)} Chủ đề** (sample)
- **Database:** MySQL `vbpl`

## 📋 Danh sách Chủ đề (Sample)

"""
    
    for i, topic in enumerate(topics, 1):
        content += f"{i}. **[{topic['name']}](/van-ban/{topic['slug']}/)** - {topic['subtopic_count']} đề mục ({topic['provision_count']:,} điều khoản)\n"
    
    content += """

*Đây là trang demo với 2 chủ đề đầu tiên.*

## 🔍 Cách sử dụng

1. **Chọn chủ đề** từ danh sách trên
2. **Xem danh sách đề mục** thuộc chủ đề
3. **Nhấp vào đề mục** để xem nội dung

---

*Trang demo - chỉ hiển thị 2 chủ đề đầu tiên*
"""
    
    return content

def generate_topic_page(topic, subtopics):
    """Generate topic page"""
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

## 📋 Danh sách Đề mục (Sample)

"""
    
    for i, subtopic in enumerate(subtopics, 1):
        icon = "📄" if subtopic['has_content'] else "📝"
        content += f"{i}. **[{subtopic['name']}](/van-ban/{topic['slug']}/{subtopic['slug']}/)** {icon} - {subtopic['provision_count']:,} điều khoản\n"
    
    content += f"""

*Chỉ hiển thị {len(subtopics)} đề mục đầu tiên*

## 🔙 Quay lại
[← Danh sách tất cả Chủ đề](/van-ban/)

---

*Trang demo - chỉ hiển thị {len(subtopics)} đề mục đầu tiên*
"""
    
    return content

def generate_subtopic_page(topic, subtopic, html_content):
    """Generate subtopic page"""
    markdown_content = html_to_markdown_simple(html_content)
    
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

## 📜 Nội dung (Sample)

{markdown_content}

## 🔙 Quay lại
[← Danh sách đề mục của {topic['name']}](/van-ban/{topic['slug']}/)  
[← Danh sách tất cả Chủ đề](/van-ban/)

---

*Trang demo - chỉ hiển thị phần đầu nội dung*
"""
    
    return content

def main():
    print("=== GENERATE VAN-BAN PAGES (SAMPLE) ===")
    
    # Create output directory
    Path(VB_PATH).mkdir(parents=True, exist_ok=True)
    
    # Get topics
    print("📊 Loading topics...")
    topics = get_topics(limit=2)
    print(f"✅ Found {len(topics)} topics")
    
    # Generate index page
    print("\n📄 Generating index page...")
    index_content = generate_index_page(topics)
    index_path = os.path.join(VB_PATH, "index.md")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✅ Index page: {index_path}")
    
    # Generate topic and subtopic pages
    for topic in topics:
        print(f"\n📁 Processing topic: {topic['name']}")
        
        # Get subtopics
        subtopics = get_subtopics_by_topic(topic['id'], limit=3)
        
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
        for subtopic in subtopics:
            # Get content
            html_content = get_subtopic_content(subtopic['id'])
            
            # Generate page
            subtopic_content = generate_subtopic_page(topic, subtopic, html_content)
            subtopic_path = os.path.join(topic_dir, f"{subtopic['slug']}.md")
            
            with open(subtopic_path, 'w', encoding='utf-8') as f:
                f.write(subtopic_content)
            print(f"    ✅ Subtopic page: {topic['slug']}/{subtopic['slug']}.md")
    
    print(f"\n🎉 COMPLETE!")
    print(f"📁 Output directory: {VB_PATH}")
    print(f"📄 Total pages: {1 + len(topics) + sum(len(get_subtopics_by_topic(t['id'], 3)) for t in topics)}")

if __name__ == "__main__":
    main()
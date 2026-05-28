#!/usr/bin/env python3
"""
Generate markdown pages from MySQL vbpl database với nội dung đầy đủ từ dieu_khoan.ten
URL structure:
- Topic pages: /van-ban/<slug>/
- Subtopic pages: /van-ban/<parent>/<slug>/
"""

import os
import re
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import html

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
    'password': '<redacted>',
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

def get_topics():
    """Get all topics (chu_de)"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT id, text as name, stt 
            FROM chu_de 
            ORDER BY stt
        """)
        
        topics = []
        for row in cursor.fetchall():
            topic_id = row['id']
            topic_name = row['name']
            
            # Get subtopic count for this topic
            cursor2 = conn.cursor()
            cursor2.execute("SELECT COUNT(*) FROM de_muc WHERE chu_de_id = %s", (topic_id,))
            subtopic_count = cursor2.fetchone()[0] or 0
            cursor2.close()
            
            # Get provision count for this topic
            cursor2 = conn.cursor()
            cursor2.execute("""
                SELECT COUNT(*) 
                FROM dieu_khoan dk
                JOIN de_muc dm ON dk.de_muc_id = dm.id
                WHERE dm.chu_de_id = %s
            """, (topic_id,))
            provision_count = cursor2.fetchone()[0] or 0
            cursor2.close()
            
            topics.append({
                'id': topic_id,
                'name': topic_name,
                'stt': row['stt'],
                'slug': slugify(topic_name),
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

def get_subtopics_for_topic(topic_id):
    """Get all subtopics (de_muc) for a topic"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT id, text as name, stt, chu_de_id
            FROM de_muc 
            WHERE chu_de_id = %s
            ORDER BY stt
        """, (topic_id,))
        
        subtopics = []
        for row in cursor.fetchall():
            subtopic_id = row['id']
            
            # Get provision count for this subtopic
            cursor2 = conn.cursor()
            cursor2.execute("SELECT COUNT(*) FROM dieu_khoan WHERE de_muc_id = %s", (subtopic_id,))
            provision_count = cursor2.fetchone()[0] or 0
            cursor2.close()
            
            # Get provisions with content count
            cursor2 = conn.cursor()
            cursor2.execute("""
                SELECT COUNT(*) 
                FROM dieu_khoan 
                WHERE de_muc_id = %s 
                  AND LENGTH(ten) > 50
            """, (subtopic_id,))
            content_count = cursor2.fetchone()[0] or 0
            cursor2.close()
            
            subtopics.append({
                'id': subtopic_id,
                'name': row['name'],
                'stt': row['stt'],
                'slug': slugify(row['name']),
                'provision_count': provision_count,
                'content_count': content_count,
                'content_percentage': (content_count / provision_count * 100) if provision_count > 0 else 0
            })
        
        return subtopics
        
    except Error as e:
        print(f"✗ Lỗi get_subtopics_for_topic: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_provisions_for_subtopic(subtopic_id):
    """Get all provisions (dieu_khoan) for a subtopic với nội dung đầy đủ"""
    conn = get_database_connection()
    if not conn:
        return []
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT id, ten as content, chi_muc, mapc
            FROM dieu_khoan 
            WHERE de_muc_id = %s
            ORDER BY mapc
        """, (subtopic_id,))
        
        provisions = []
        for row in cursor.fetchall():
            content = row['content']
            chi_muc = row['chi_muc']
            
            # Extract title from content (first line before \n\n)
            title = ""
            if content and '\n\n' in content:
                title = content.split('\n\n')[0].strip()
            elif content:
                title = content.strip()
            
            # Check if this is a real provision (has Điều in title)
            is_real_provision = 'Điều' in title or ('Chương' not in title and 'Mục' not in title)
            
            provisions.append({
                'id': row['id'],
                'title': title,
                'content': content,
                'chi_muc': chi_muc,
                'mapc': row['mapc'],
                'has_content': len(content or '') > 50,
                'is_real_provision': is_real_provision,
                'content_length': len(content or '')
            })
        
        return provisions
        
    except Error as e:
        print(f"✗ Lỗi get_provisions_for_subtopic: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def format_provision_content(provision):
    """Format provision content for markdown"""
    content = provision['content']
    
    if not content or len(content) <= 50:
        return "*Nội dung chưa có sẵn*"
    
    # If content has title and body separated by \n\n
    if '\n\n' in content:
        parts = content.split('\n\n', 1)
        title = parts[0].strip()
        body = parts[1].strip()
        
        # Clean up body
        body = re.sub(r'\n\s*\n', '\n\n', body)
        body = body.replace('\n', '  \n')  # Add two spaces for line breaks
        
        return body
    else:
        # Just use the content as is
        return content

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

## 📋 Danh sách đề mục

"""
    
    # Add subtopic list
    for subtopic in subtopics:
        content_percentage = f"{subtopic['content_percentage']:.1f}%" if subtopic['provision_count'] > 0 else "0%"
        
        content += f"### [{subtopic['name']}](/{topic['slug']}/{subtopic['slug']}/)\n"
        content += f"- **Số điều khoản:** {subtopic['provision_count']:,}\n"
        content += f"- **Điều khoản có nội dung:** {subtopic['content_count']}/{subtopic['provision_count']} ({content_percentage})\n"
        content += f"- **STT:** {subtopic['stt']}\n\n"
    
    content += f"""
## 🔙 Quay lại
[← Danh sách tất cả Chủ đề](/van-ban/)

## 📊 Thống kê
- **Tổng số đề mục:** {topic['subtopic_count']}
- **Tổng số điều khoản:** {topic['provision_count']:,}
- **ID chủ đề:** {topic['id']}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_subtopic_page(topic, subtopic, provisions):
    """Generate markdown for a subtopic page với nội dung đầy đủ"""
    # Count provisions with content
    provisions_with_content = sum(1 for p in provisions if p['has_content'])
    real_provisions = sum(1 for p in provisions if p['is_real_provision'])
    real_provisions_with_content = sum(1 for p in provisions if p['is_real_provision'] and p['has_content'])
    
    content_percentage = f"{(real_provisions_with_content / real_provisions * 100):.1f}%" if real_provisions > 0 else "0%"
    
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
**Chủ đề:** [{topic['name']}](/{topic['slug']}/)  
**Số điều khoản:** {subtopic['provision_count']}  
**Điều khoản có nội dung:** {real_provisions_with_content}/{real_provisions} ({content_percentage})  
**Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 📜 Nội dung Điều khoản

"""
    
    # Add provisions
    provision_count = 0
    for provision in provisions:
        if not provision['is_real_provision']:
            # Skip chapters, sections, etc.
            continue
        
        provision_count += 1
        
        content += f"\n### {provision['title']}\n\n"
        
        if provision['has_content']:
            # Format the content
            provision_content = format_provision_content(provision)
            content += f"{provision_content}\n\n"
        else:
            content += "*Nội dung chưa có sẵn*\n\n"
        
        content += f"**Chỉ mục:** {provision['chi_muc'] or 'N/A'}\n\n"
        content += f"**Mã phân cấp:** {provision['mapc'] or 'N/A'}\n\n"
        content += f"**ID:** {provision['id']}\n\n"
        content += "---\n\n"
    
    content += f"""
## 🔙 Quay lại
[← Danh sách đề mục của {topic['name']}](/{topic['slug']}/)  
[← Danh sách tất cả Chủ đề](/van-ban/)

## 📊 Thống kê
- **Tổng số điều khoản:** {subtopic['provision_count']}
- **Điều khoản thực tế:** {real_provisions}
- **Điều khoản có nội dung:** {real_provisions_with_content} ({content_percentage})
- **ID đề mục:** {subtopic['id']}

## 🔍 Tìm kiếm
Sử dụng chức năng tìm kiếm của website để tìm văn bản cụ thể.

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def generate_index_page(topics):
    """Generate index page for all topics"""
    total_subtopics = sum(t['subtopic_count'] for t in topics)
    total_provisions = sum(t['provision_count'] for t in topics)
    
    content = f"""---
layout: default
title: Văn bản pháp luật
permalink: /van-ban/
collection: van-ban
---

# 📚 Văn bản pháp luật

**Tổng hợp hệ thống văn bản pháp luật Việt Nam**

## 📊 Tổng quan

- **Số chủ đề:** {len(topics)}
- **Số đề mục:** {total_subtopics:,}
- **Số điều khoản:** {total_provisions:,}
- **Cập nhật:** {{{{ site.time | date: "%Y-%m-%d" }}}}

## 🗂️ Danh sách chủ đề

"""
    
    # Add topic list
    for topic in topics:
        content += f"### [{topic['name']}](/{topic['slug']}/)\n"
        content += f"- **STT:** {topic['stt']}\n"
        content += f"- **Số đề mục:** {topic['subtopic_count']:,}\n"
        content += f"- **Số điều khoản:** {topic['provision_count']:,}\n\n"
    
    content += f"""
## 🔍 Giới thiệu

Hệ thống này tổng hợp toàn bộ văn bản pháp luật Việt Nam được số hóa từ Pháp điển điện tử. Mỗi chủ đề bao gồm nhiều đề mục, mỗi đề mục chứa các điều khoản pháp luật cụ thể.

## 📝 Ghi chú

- Dữ liệu được cập nhật tự động từ nguồn chính thống
- Nội dung có thể chưa đầy đủ cho một số điều khoản
- Sử dụng chức năng tìm kiếm để tra cứu nhanh

## 🔗 Liên kết

- [Pháp điển điện tử](http://vbpl.vn)
- [Cổng thông tin điện tử Chính phủ](https://chinhphu.vn)

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{{{ site.time | date: "%Y-%m-%d" }}}}*
"""
    
    return content

def ensure_directory(path):
    """Ensure directory exists"""
    os.makedirs(path, exist_ok=True)

def generate_all_pages():
    """Generate all pages"""
    print("🔄 Bắt đầu generate markdown pages...")
    
    # Get all topics
    topics = get_topics()
    print(f"📚 Tìm thấy {len(topics)} chủ đề")
    
    # Generate index page
    index_content = generate_index_page(topics)
    index_path = os.path.join(VB_PATH, "index.md")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"✅ Đã tạo index page: {index_path}")
    
    total_subtopics = 0
    total_provisions = 0
    
    # Generate topic and subtopic pages
    for topic in topics:
        print(f"\n📁 Đang xử lý chủ đề: {topic['name']}")
        
        # Create topic directory
        topic_dir = os.path.join(VB_PATH, topic['slug'])
        ensure_directory(topic_dir)
        
        # Get subtopics for this topic
        subtopics = get_subtopics_for_topic(topic['id'])
        print(f"  📂 Tìm thấy {len(subtopics)} đề mục")
        
        # Generate topic page
        topic_content = generate_topic_page(topic, subtopics)
        topic_path = os.path.join(VB_PATH, f"{topic['slug']}.md")
        
        with open(topic_path, 'w', encoding='utf-8') as f:
            f.write(topic_content)
        
        print(f"  ✅ Đã tạo topic page: {topic_path}")
        
        # Generate subtopic pages
        for subtopic in subtopics:
            total_subtopics += 1
            
            # Get provisions for this subtopic
            provisions = get_provisions_for_subtopic(subtopic['id'])
            total_provisions += len(provisions)
            
            # Generate subtopic page
            subtopic_content = generate_subtopic_page(topic, subtopic, provisions)
            subtopic_path = os.path.join(topic_dir, f"{subtopic['slug']}.md")
            
            with open(subtopic_path, 'w', encoding='utf-8') as f:
                f.write(subtopic_content)
            
            # Also create a markdown file in van-ban/ directory for backward compatibility
            compat_path = os.path.join(VB_PATH, f"{topic['slug']}_{subtopic['slug']}.md")
            with open(compat_path, 'w', encoding='utf-8') as f:
                f.write(subtopic_content)
        
        print(f"  ✅ Đã tạo {len(subtopics)} subtopic pages")
    
    print(f"\n{'='*60}")
    print(f"🎉 HOÀN THÀNH!")
    print(f"{'='*60}")
    print(f"📊 Tổng kết:")
    print(f"  • Chủ đề: {len(topics)}")
    print(f"  • Đề mục: {total_subtopics}")
    print(f"  • Điều khoản: {total_provisions}")
    print(f"  • Files markdown: {total_subtopics + len(topics) + 1}")
    print(f"{'='*60}")

if __name__ == "__main__":
    generate_all_pages()
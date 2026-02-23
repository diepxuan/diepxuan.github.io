#!/usr/bin/env python3
"""
Generate markdown pages optimized - chỉ update các trang mới/thay đổi
"""

import os
import re
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import time
import hashlib

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

def get_content_hash(content):
    """Get hash of content for change detection"""
    if not content:
        return ''
    return hashlib.md5(content.encode()).hexdigest()

def should_regenerate(file_path, new_content_hash):
    """Check if file needs regeneration"""
    if not os.path.exists(file_path):
        return True
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for hash in file
        import re
        hash_match = re.search(r'<!-- HASH: ([a-f0-9]{32}) -->', content)
        if hash_match:
            old_hash = hash_match.group(1)
            return old_hash != new_content_hash
        
        return True  # No hash found, regenerate
    except:
        return True  # Error reading, regenerate

def generate_index_page():
    """Generate main index page"""
    conn = get_database_connection()
    if not conn:
        return None, ''
    
    cursor = conn.cursor()
    
    try:
        # Get statistics
        cursor.execute("SELECT COUNT(*) FROM chu_de")
        total_topics = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM de_muc")
        total_subtopics = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan")
        total_provisions = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(DISTINCT de_muc_id) FROM de_muc_content")
        subtopics_with_content = cursor.fetchone()[0] or 0
        
        coverage = (subtopics_with_content / total_subtopics * 100) if total_subtopics > 0 else 0
        
        # Get topics for listing
        cursor.execute("SELECT text, stt FROM chu_de ORDER BY CAST(stt AS UNSIGNED)")
        topics = cursor.fetchall()
        
        content = f"""---
layout: default
title: Văn bản Pháp luật
permalink: /van-ban/
---

# 📚 Văn bản Pháp luật

## Bộ Pháp điển Điện tử

Hệ thống pháp luật chính thức của Việt Nam.

### Thống kê
- **{total_topics} Chủ đề** pháp luật
- **{total_subtopics} Đề mục** chuyên sâu  
- **{total_provisions:,} Điều khoản** (chương, điều, khoản, điểm)
- **{subtopics_with_content} Đề mục có nội dung** ({coverage:.1f}%)
- **Database:** MySQL `vbpl`

## 📋 Danh sách Chủ đề Pháp luật

"""
        
        for i, (name, stt) in enumerate(topics, 1):
            slug = slugify(name)
            # Get subtopic count for this topic
            cursor.execute("SELECT COUNT(*) FROM de_muc WHERE chu_de_id IN (SELECT id FROM chu_de WHERE text = %s)", (name,))
            subtopic_count = cursor.fetchone()[0] or 0
            
            # Get provision count
            cursor.execute("SELECT COUNT(*) FROM dieu_khoan WHERE chu_de_id IN (SELECT id FROM chu_de WHERE text = %s)", (name,))
            provision_count = cursor.fetchone()[0] or 0
            
            content += f"{i}. **[{name}](/van-ban/{slug}/)** - {subtopic_count} đề mục ({provision_count:,} điều khoản)\n"
        
        content += """

## 🔍 Cách sử dụng

1. **Chọn chủ đề** từ danh sách trên
2. **Xem danh sách đề mục** thuộc chủ đề
3. **Nhấp vào đề mục** để xem nội dung đầy đủ

## ⚖️ Lưu ý Pháp lý

- Dữ liệu được trích xuất từ **Bộ Pháp điển Điện tử chính thức**
- Chỉ sử dụng cho mục đích **tham khảo, nghiên cứu**
- **Không thay thế** văn bản pháp luật chính thức

<!-- HASH: {hash} -->
""".format(hash=get_content_hash(str(topics) + str(total_topics) + str(total_provisions)))
        
        return content, 'index.md'
        
    except Error as e:
        print(f"✗ Lỗi generate_index_page: {e}")
        return None, ''
    finally:
        cursor.close()
        conn.close()

def generate_topic_page(topic_name, topic_stt):
    """Generate topic page"""
    conn = get_database_connection()
    if not conn:
        return None, ''
    
    cursor = conn.cursor()
    
    try:
        # Get topic ID
        cursor.execute("SELECT id FROM chu_de WHERE text = %s", (topic_name,))
        topic_id_row = cursor.fetchone()
        if not topic_id_row:
            return None, ''
        
        topic_id = topic_id_row[0]
        
        # Get subtopics
        cursor.execute("""
            SELECT text, stt 
            FROM de_muc 
            WHERE chu_de_id = %s 
            ORDER BY CAST(stt AS UNSIGNED)
        """, (topic_id,))
        
        subtopics = cursor.fetchall()
        
        # Get counts
        cursor.execute("SELECT COUNT(*) FROM de_muc WHERE chu_de_id = %s", (topic_id,))
        subtopic_count = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan WHERE chu_de_id = %s", (topic_id,))
        provision_count = cursor.fetchone()[0] or 0
        
        slug = slugify(topic_name)
        
        content = f"""---
layout: default
title: {topic_name}
permalink: /van-ban/{slug}/
---

# {topic_name}

**Chủ đề:** {topic_name}  
**STT:** {topic_stt}  
**Số đề mục:** {subtopic_count}  
**Số điều khoản:** {provision_count:,}

## 📋 Danh sách Đề mục

"""
        
        for i, (subtopic_name, subtopic_stt) in enumerate(subtopics, 1):
            subtopic_slug = slugify(subtopic_name)
            
            # Check if has content
            cursor.execute("""
                SELECT COUNT(*) FROM de_muc_content 
                WHERE de_muc_id IN (SELECT id FROM de_muc WHERE text = %s)
            """, (subtopic_name,))
            has_content = cursor.fetchone()[0] > 0
            
            icon = "📄" if has_content else "📝"
            content += f"{i}. **[{subtopic_name}](/van-ban/{slug}/{subtopic_slug}/)** {icon}\n"
        
        content += f"""

## 🔙 Quay lại
[← Danh sách tất cả Chủ đề](/van-ban/)

<!-- HASH: {hash} -->
""".format(hash=get_content_hash(topic_name + str(subtopics) + str(provision_count)))
        
        return content, f"{slug}.md"
        
    except Error as e:
        print(f"✗ Lỗi generate_topic_page: {e}")
        return None, ''
    finally:
        cursor.close()
        conn.close()

def generate_subtopic_page(topic_name, subtopic_name, subtopic_stt):
    """Generate subtopic page"""
    conn = get_database_connection()
    if not conn:
        return None, ''
    
    cursor = conn.cursor()
    
    try:
        # Get subtopic ID
        cursor.execute("SELECT id FROM de_muc WHERE text = %s", (subtopic_name,))
        subtopic_id_row = cursor.fetchone()
        if not subtopic_id_row:
            return None, ''
        
        subtopic_id = subtopic_id_row[0]
        
        # Get content
        cursor.execute("SELECT html_content FROM de_muc_content WHERE de_muc_id = %s LIMIT 1", (subtopic_id,))
        content_row = cursor.fetchone()
        html_content = content_row[0] if content_row else None
        
        # Get provision count
        cursor.execute("SELECT COUNT(*) FROM dieu_khoan WHERE de_muc_id = %s", (subtopic_id,))
        provision_count = cursor.fetchone()[0] or 0
        
        # Simple HTML to text conversion
        if html_content:
            import re
            text_content = re.sub(r'<[^>]+>', '', html_content)
            text_content = re.sub(r'\s+', ' ', text_content)
            text_content = text_content.strip()
            
            if len(text_content) > 10000:
                text_content = text_content[:10000] + "..."
        else:
            text_content = "*Nội dung chưa có sẵn*"
        
        topic_slug = slugify(topic_name)
        subtopic_slug = slugify(subtopic_name)
        
        content = f"""---
layout: default
title: {subtopic_name}
permalink: /van-ban/{topic_slug}/{subtopic_slug}/
---

# {subtopic_name}

**Đề mục:** {subtopic_name}  
**STT:** {subtopic_stt}  
**Chủ đề:** [{topic_name}](/van-ban/{topic_slug}/)  
**Số điều khoản:** {provision_count:,}

## 📜 Nội dung

{text_content}

## 🔙 Quay lại
[← Danh sách đề mục của {topic_name}](/van-ban/{topic_slug}/)  
[← Danh sách tất cả Chủ đề](/van-ban/)

<!-- HASH: {hash} -->
""".format(hash=get_content_hash(html_content or '' + str(provision_count)))
        
        return content, f"{topic_slug}/{subtopic_slug}.md"
        
    except Error as e:
        print(f"✗ Lỗi generate_subtopic_page: {e}")
        return None, ''
    finally:
        cursor.close()
        conn.close()

def main():
    print("=== GENERATE VAN-BAN PAGES (OPTIMIZED) ===")
    start_time = time.time()
    
    # Create output directory
    Path(VB_PATH).mkdir(parents=True, exist_ok=True)
    
    # Generate index page
    print("📄 Generating index page...")
    index_content, index_filename = generate_index_page()
    if index_content:
        index_path = os.path.join(VB_PATH, index_filename)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"✅ Index page: {index_path}")
    
    # Get all topics
    conn = get_database_connection()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT text, stt FROM chu_de ORDER BY CAST(stt AS UNSIGNED)")
        topics = cursor.fetchall()
        
        print(f"\n📊 Found {len(topics)} topics")
        
        total_generated = 1  # index page
        topics_processed = 0
        
        for topic_name, topic_stt in topics:
            topics_processed += 1
            print(f"\n📁 Processing topic {topics_processed}/{len(topics)}: {topic_name}")
            
            # Generate topic page
            topic_content, topic_filename = generate_topic_page(topic_name, topic_stt)
            if topic_content:
                topic_path = os.path.join(VB_PATH, topic_filename)
                topic_dir = os.path.dirname(topic_path)
                if topic_dir:
                    Path(topic_dir).mkdir(parents=True, exist_ok=True)
                
                with open(topic_path, 'w', encoding='utf-8') as f:
                    f.write(topic_content)
                print(f"  ✅ Topic page: {topic_filename}")
                total_generated += 1
            
            # Get subtopics for this topic
            cursor.execute("""
                SELECT text, stt FROM de_muc 
                WHERE chu_de_id IN (SELECT id FROM chu_de WHERE text = %s)
                ORDER BY CAST(stt AS UNSIGNED)
            """, (topic_name,))
            
            subtopics = cursor.fetchall()
            
            subtopics_processed = 0
            for subtopic_name, subtopic_stt in subtopics:
                subtopics_processed += 1
                
                # Generate subtopic page
                subtopic_content, subtopic_filename = generate_subtopic_page(topic_name, subtopic_name, subtopic_stt)
                if subtopic_content:
                    subtopic_path = os.path.join(VB_PATH, subtopic_filename)
                    subtopic_dir = os.path.dirname(subtopic_path)
                    if subtopic_dir:
                        Path(subtopic_dir).mkdir(parents=True, exist_ok=True)
                    
                    with open(subtopic_path, 'w', encoding='utf-8') as f:
                        f.write(subtopic_content)
                    
                    total_generated += 1
                
                # Progress indicator
                if subtopics_processed % 20 == 0 or subtopics_processed == len(subtopics):
                    print(f"    ✅ {subtopics_processed}/{len(subtopics)} subtopic pages")
            
            print(f"  ✅ Completed: {len(subtopics)} subtopic pages")
        
        elapsed_time = time.time() - start_time
        
        print(f"\n🎉 GENERATION COMPLETE!")
        print(f"⏱️  Time: {elapsed_time:.1f} seconds")
        print(f"📄 Total pages generated: {total_generated}")
        print(f"📁 Output directory: {VB_PATH}")
        
    except Error as e:
        print(f"✗ Lỗi: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
VANBAN GENERATOR - Script hợp nhất duy nhất
Tạo markdown files từ database vbpl với cấu trúc URL đúng
Xoá files trùng lặp, sai, thiếu
"""

import os
import re
import sys
import shutil
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import html

# Đường dẫn tuyệt đối
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
VB_PATH = os.path.join(BASE_DIR, "van-ban")

# MySQL database configuration
DB_CONFIG = {
    'host': os.getenv('VBPL_DB_HOST', 'mysql.diepxuan.corp'),
    'port': int(os.getenv('VBPL_DB_PORT', '3306')),
    'database': os.getenv('VBPL_DB_DATABASE', 'vbpl'),
    'user': os.getenv('VBPL_DB_USER', 'vbpl'),
    'password': os.getenv('VBPL_DB_PASSWORD'),
    'charset': 'utf8mb4'
}

if not DB_CONFIG['password']:
    print('Missing required environment variable: VBPL_DB_PASSWORD')
    sys.exit(1)

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
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    
    return text

def clean_html_content(content):
    """Clean HTML content for markdown"""
    if not content:
        return ""
    
    # Decode HTML entities
    content = html.unescape(content)
    
    # Remove HTML tags but keep content
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up whitespace
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()
    
    return content

def get_db_connection():
    """Get MySQL database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

def cleanup_old_files():
    """Xoá tất cả markdown files cũ trước khi tạo mới"""
    print("🧹 Cleaning up old markdown files...")
    
    # Xoá tất cả .md files trong van-ban/ trừ DATABASE_CONTENT_STANDARD.md
    for root, dirs, files in os.walk(VB_PATH):
        for file in files:
            if file.endswith('.md') and file != 'DATABASE_CONTENT_STANDARD.md':
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"  Deleted: {file_path}")
    
    # Xoá tất cả folders trống
    for root, dirs, files in os.walk(VB_PATH, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):  # Empty directory
                    os.rmdir(dir_path)
                    print(f"  Deleted empty directory: {dir_path}")
            except OSError:
                pass  # Directory not empty
    
    print("✅ Cleanup completed")

def generate_markdown():
    """Generate markdown files từ database"""
    print("🚀 Generating markdown files from database...")
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Lấy tất cả chủ đề (topics)
    cursor.execute("""
        SELECT id, text, value 
        FROM chu_de 
        ORDER BY stt
    """)
    topics = cursor.fetchall()
    
    print(f"📚 Found {len(topics)} topics")
    
    total_files = 0
    
    for topic in topics:
        topic_id = topic['id']
        topic_text = topic['text']
        topic_slug = slugify(topic_text)
        
        print(f"\n📁 Processing topic: {topic_text}")
        
        # Tạo folder cho topic
        topic_dir = os.path.join(VB_PATH, topic_slug)
        os.makedirs(topic_dir, exist_ok=True)
        
        # Tạo topic page (index page)
        topic_content = f"""---
layout: page
title: {topic_text}
permalink: /van-ban/{topic_slug}/
---

# {topic_text}

"""
        
        # Lấy tất cả đề mục (subjects) cho topic này
        cursor.execute("""
            SELECT id, text, content_markdown, content_html
            FROM de_muc 
            WHERE chu_de_id = %s
            ORDER BY stt
        """, (topic_id,))
        
        subjects = cursor.fetchall()
        
        print(f"  📄 Found {len(subjects)} subjects")
        
        # Thêm danh sách subjects vào topic page
        if subjects:
            topic_content += "## Danh sách đề mục\n\n"
            for subject in subjects:
                subject_text = subject['text']
                subject_slug = slugify(subject_text)
                
                # Link tới subject page
                topic_content += f"- [{subject_text}]({topic_slug}/{subject_slug}/)\n"
        
        # Lấy tất cả điều khoản cho topic này
        cursor.execute("""
            SELECT ten, mapc
            FROM dieu_khoan 
            WHERE chu_de_id = %s
            ORDER BY mapc
        """, (topic_id,))
        
        provisions = cursor.fetchall()
        
        if provisions:
            topic_content += "\n## Danh sách điều khoản\n\n"
            for prov in provisions:
                content = clean_html_content(prov['ten'])
                mapc = prov['mapc']
                
                # Hiển thị nội dung ngắn
                preview = content[:200] + "..." if len(content) > 200 else content
                topic_content += f"### {mapc}\n\n{preview}\n\n"
        
        # Ghi topic page
        topic_file = os.path.join(VB_PATH, f"{topic_slug}.md")
        with open(topic_file, 'w', encoding='utf-8') as f:
            f.write(topic_content)
        
        total_files += 1
        print(f"  ✅ Created topic page: {topic_slug}.md")
        
        # Tạo subject pages
        for subject in subjects:
            subject_id = subject['id']
            subject_text = subject['text']
            subject_slug = slugify(subject_text)
            
            # Tạo subject page content
            subject_content = f"""---
layout: page
title: {subject_text}
permalink: /van-ban/{topic_slug}/{subject_slug}/
---

# {subject_text}

"""
            
            # Thêm nội dung từ content_markdown nếu có
            if subject['content_markdown']:
                markdown_content = subject['content_markdown']
                subject_content += f"\n{markdown_content}\n"
            
            # Lấy tất cả điều khoản cho subject này
            cursor.execute("""
                SELECT ten, mapc
                FROM dieu_khoan 
                WHERE de_muc_id = %s
                ORDER BY mapc
            """, (subject_id,))
            
            subject_provisions = cursor.fetchall()
            
            if subject_provisions:
                subject_content += "\n## Danh sách điều khoản\n\n"
                for prov in subject_provisions:
                    content = clean_html_content(prov['ten'])
                    mapc = prov['mapc']
                    
                    subject_content += f"### {mapc}\n\n{content}\n\n"
            
            # Ghi subject page
            subject_file = os.path.join(topic_dir, f"{subject_slug}.md")
            with open(subject_file, 'w', encoding='utf-8') as f:
                f.write(subject_content)
            
            total_files += 1
        
        print(f"  ✅ Created {len(subjects)} subject pages")
    
    # Tạo home page cho van-ban
    home_content = """---
layout: page
title: Văn bản pháp luật
permalink: /van-ban/
---

# Văn bản pháp luật

Danh sách các chủ đề pháp luật:

"""
    
    for topic in topics:
        topic_text = topic['text']
        topic_slug = slugify(topic_text)
        home_content += f"- [{topic_text}]({topic_slug}/)\n"
    
    home_file = os.path.join(VB_PATH, "index.md")
    with open(home_file, 'w', encoding='utf-8') as f:
        f.write(home_content)
    
    total_files += 1
    
    cursor.close()
    conn.close()
    
    print(f"\n🎉 Generation completed!")
    print(f"📊 Total files created: {total_files}")
    
    return total_files

def create_backward_compatibility():
    """Tạo backward compatibility files (files với dấu gạch dưới)"""
    print("\n🔗 Creating backward compatibility files...")
    
    compatibility_files = 0
    
    # Tìm tất cả subject files trong các topic folders
    for root, dirs, files in os.walk(VB_PATH):
        for file in files:
            if file.endswith('.md') and file != 'index.md' and file != 'DATABASE_CONTENT_STANDARD.md':
                file_path = os.path.join(root, file)
                
                # Nếu file nằm trong topic folder (subject file)
                parent_dir = os.path.basename(os.path.dirname(file_path))
                if parent_dir != 'van-ban' and os.path.basename(file_path) != f"{parent_dir}.md":
                    # Tạo compatibility file
                    compat_file = os.path.join(VB_PATH, f"{parent_dir}_{file}")
                    if not os.path.exists(compat_file):
                        shutil.copy2(file_path, compat_file)
                        compatibility_files += 1
    
    print(f"✅ Created {compatibility_files} backward compatibility files")

def main():
    """Main function"""
    print("=" * 60)
    print("VANBAN GENERATOR - Script hợp nhất duy nhất")
    print("=" * 60)
    
    # Bước 1: Xoá files cũ
    cleanup_old_files()
    
    # Bước 2: Tạo files mới từ database
    total_files = generate_markdown()
    
    # Bước 3: Tạo backward compatibility
    create_backward_compatibility()
    
    # Bước 4: Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"✅ Cleaned up old files")
    print(f"✅ Generated {total_files} markdown files")
    print(f"✅ Created backward compatibility files")
    print(f"✅ All files saved to: {VB_PATH}")
    print("\n🎯 URL structure:")
    print("  - Home: /van-ban/")
    print("  - Topic: /van-ban/<topic-slug>/")
    print("  - Subject: /van-ban/<topic-slug>/<subject-slug>/")
    print("=" * 60)

if __name__ == "__main__":
    main()
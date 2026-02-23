#!/usr/bin/env python3
"""
Test HTML to Markdown conversion với một vài file đầu tiên
"""

import os
import re
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

def html_to_markdown_simple(html_content):
    """
    Convert HTML sang Markdown đơn giản, dễ đọc
    """
    if not html_content:
        return ""
    
    # Remove BOM và clean
    html_content = html_content.replace('\ufeff', '')
    
    # Extract main content từ div._content
    content_match = re.search(r"<div class='_content'>(.*?)</div>", html_content, re.DOTALL)
    if content_match:
        html_content = content_match.group(1)
    
    # Remove script và style tags
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
    
    # Convert các thẻ HTML sang Markdown
    markdown = html_content
    
    # Headers
    markdown = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n\n', markdown)
    markdown = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n', markdown)
    markdown = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n', markdown)
    markdown = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n', markdown)
    
    # Paragraphs với class đặc biệt
    markdown = re.sub(r'<p class="pChuong"[^>]*>(.*?)</p>', r'### \1\n\n', markdown)
    markdown = re.sub(r'<p class="pDieu"[^>]*>(.*?)</p>', r'#### \1\n\n', markdown)
    markdown = re.sub(r'<p class="pNoiDung"[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    markdown = re.sub(r'<p class="pKhoan"[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    markdown = re.sub(r'<p class="pDiem"[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    
    # General paragraphs
    markdown = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', markdown)
    
    # Lists
    markdown = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', markdown)
    markdown = re.sub(r'<ul[^>]*>', '', markdown)
    markdown = re.sub(r'</ul>', '\n', markdown)
    markdown = re.sub(r'<ol[^>]*>', '', markdown)
    markdown = re.sub(r'</ol>', '\n', markdown)
    
    # Links
    markdown = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', markdown)
    
    # Bold/Strong
    markdown = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', markdown)
    markdown = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', markdown)
    
    # Italic/Emphasis
    markdown = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', markdown)
    markdown = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', markdown)
    
    # Remove remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)
    
    # Clean up whitespace
    markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
    markdown = re.sub(r'[ \t]+', ' ', markdown)
    markdown = markdown.strip()
    
    return markdown

def test_conversion():
    """Test conversion với 5 file đầu tiên"""
    demuc_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/demuc'
    
    if not os.path.exists(demuc_dir):
        print(f"✗ Thư mục không tồn tại: {demuc_dir}")
        return
    
    files = [f for f in os.listdir(demuc_dir) if f.endswith('.html')]
    print(f"Tìm thấy {len(files)} file HTML")
    
    # Test với 5 file đầu tiên
    for i, file_name in enumerate(files[:5], 1):
        print(f"\n=== TEST FILE {i}: {file_name} ===")
        file_path = os.path.join(demuc_dir, file_name)
        
        try:
            # Đọc nội dung file
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            print(f"  HTML size: {len(html_content):,} bytes")
            
            # Convert sang Markdown
            markdown_content = html_to_markdown_simple(html_content)
            
            print(f"  Markdown size: {len(markdown_content):,} bytes")
            print(f"  Compression: {len(markdown_content)/len(html_content)*100:.1f}%")
            
            # Show preview
            preview = markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content
            print(f"\n  Preview (first 500 chars):")
            print(f"  {'='*50}")
            print(f"  {preview}")
            print(f"  {'='*50}")
            
        except Exception as e:
            print(f"  ✗ Lỗi: {e}")

def create_markdown_table():
    """Tạo bảng markdown trong database"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        print("=== TẠO BẢNG MARKDOWN ===")
        
        # Tạo bảng mới
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS de_muc_markdown (
                id VARCHAR(50) PRIMARY KEY,
                de_muc_id VARCHAR(36) NOT NULL,
                file_name VARCHAR(255),
                markdown_content LONGTEXT,
                html_content LONGTEXT,
                content_size INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (de_muc_id) REFERENCES de_muc(id) ON DELETE CASCADE,
                INDEX idx_de_muc_id (de_muc_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)
        connection.commit()
        print("✓ Đã tạo bảng de_muc_markdown")
        
        # Kiểm tra bảng
        cursor.execute("SHOW TABLES LIKE 'de_muc_markdown'")
        if cursor.fetchone():
            print("✓ Bảng de_muc_markdown tồn tại")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"✗ Lỗi: {e}")

def main():
    print("=== TEST HTML TO MARKDOWN CONVERSION ===")
    
    # Test conversion
    test_conversion()
    
    # Tạo bảng markdown
    create_markdown_table()

if __name__ == "__main__":
    main()
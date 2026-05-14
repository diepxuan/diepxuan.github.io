#!/usr/bin/env python3
"""
Metadata updater for van-ban/ files.
Searches vanban.chinhphu.vn for each legal document and updates metadata table.
"""

import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN_DIR = os.path.join(BASE_DIR, "van-ban")
LOG_FILE = os.path.join(BASE_DIR, "scripts", "metadata_crawl_log.md")

# Brave Search API via a simple subprocess call
def brave_search(query, count=5):
    """Search using Brave Search API via web_search concept - we'll use curl."""
    # We'll use the Firecrawl search approach or a direct HTTP search
    # Actually, let's use a simple web_fetch approach
    search_url = f"https://www.google.com/search?q={urllib.parse.quote('vanban.chinhphu.vn ' + query)}"
    req = urllib.request.Request(
        search_url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='replace')
            # Extract URLs containing docid=
            docid_urls = re.findall(r'(https?://vanban\.chinhphu\.vn/[^"\s]*docid=\d+[^"\s]*)', html)
            return docid_urls
    except Exception as e:
        return []

def search_vanban(title):
    """Search vanban.chinhphu.vn for a given title. Returns docid URL or None."""
    # Try multiple search strategies
    queries = [
        f'vanban.chinhphu.vn "{title}"',
    ]
    
    # Try direct Bing search (more reliable for Vietnamese)
    for query in queries:
        try:
            search_url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
            req = urllib.request.Request(
                search_url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='replace')
                # Extract URLs containing docid=
                docid_urls = re.findall(r'(https?://vanban\.chinhphu\.vn/[^"\s]*docid=\d+[^"\s]*)', html)
                if docid_urls:
                    return docid_urls[0]
        except Exception as e:
            print(f"  search error: {e}")
            time.sleep(1)
    
    return None

def fetch_metadata_page(url):
    """Fetch and parse metadata from a vanban.chinhphu.vn page."""
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='replace')
            return html
    except Exception as e:
        print(f"  fetch error: {e}")
        return None

def parse_metadata_from_html(html):
    """Extract metadata from the chinhphu.vn HTML page."""
    metadata = {}
    
    # The metadata is in a table-like structure
    patterns = {
        'so_hieu': r'Số ký hiệu\s*\|\s*(.+?)\s*(?:\||<)',
        'loai_van_ban': r'Loại văn bản\s*\|\s*(.+?)\s*(?:\||<)',
        'co_quan_ban_hanh': r'Cơ quan ban hành\s*\|\s*(.+?)\s*(?:\||<)',
        'nguoi_ky': r'Người ký\s*\|\s*(.+?)\s*(?:\||<)',
        'ngay_ban_hanh': r'Ngày ban hành\s*\|\s*(.+?)\s*(?:\||<)',
        'ngay_hieu_luc': r'Ngày hiệu lực\s*\|\s*(.+?)\s*(?:\||<)',
        'trich_yeu': r'Trích yếu\s*\|\s*(.+?)\s*(?:\||<)',
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, html, re.DOTALL)
        if match:
            value = match.group(1).strip()
            # Clean HTML tags
            value = re.sub(r'<[^>]+>', '', value).strip()
            if value:
                metadata[key] = value
    
    return metadata

def get_title_from_file(filepath):
    """Extract title from markdown file front matter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for title in front matter
        match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def update_file_metadata(filepath, metadata, source_url):
    """Update metadata in the markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Map metadata keys to display names
        key_map = {
            'so_hieu': 'Số hiệu',
            'loai_van_ban': 'Loại văn bản',
            'co_quan_ban_hanh': 'Nơi ban hành',
            'nguoi_ky': 'Người ký',
            'ngay_ban_hanh': 'Ngày ban hành',
            'ngay_hieu_luc': 'Ngày hiệu lực',
        }
        
        new_content = content
        
        for key, display_name in key_map.items():
            if key in metadata:
                # Replace the "Đang cập nhật" with actual value
                old_pattern = f'**{display_name}** |'
                new_value = f'**{display_name}** | {metadata[key]}'
                
                # Only replace if current value is "Đang cập nhật"
                if re.search(re.escape(old_pattern) + r'\s*Đang cập nhật', new_content):
                    new_content = re.sub(
                        re.escape(old_pattern) + r'\s*Đang cập nhật',
                        new_value,
                        new_content
                    )
        
        # Update the Nguồn (Source) line with the chinhphu.vn URL
        if source_url:
            source_pattern = r'\*\*Nguồn\*\*\s*\|.*'
            new_source = f'**Nguồn** | [Chinhphu.vn]({source_url})'
            # Only add if source is currently a search link
            if 'Tìm kiếm' not in new_source and any(k in metadata for k in ['so_hieu', 'loai_van_ban']):
                new_content = re.sub(source_pattern, new_source, new_content, count=1)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def process_single_file(filepath):
    """Process a single van-ban file."""
    rel_path = os.path.relpath(filepath, BASE_DIR)
    title = get_title_from_file(filepath)
    
    if not title:
        print(f"  SKIP: No title found in {rel_path}")
        return False, "No title"
    
    print(f"  TITLE: {title}")
    
    # First try: search by full title
    url = search_vanban(title)
    
    if not url:
        print(f"  NOT FOUND on first search, trying alternative...")
        # Try searching with just document type and number if present
        alt_match = re.search(r'(Luật|Nghị định|Thông tư|Quyết định|Pháp lệnh)\s+\S+', title, re.IGNORECASE)
        if alt_match:
            alt_query = alt_match.group(0)
            print(f"  ALT QUERY: {alt_query}")
            url = search_vanban(alt_query)
    
    if not url:
        print(f"  NOT FOUND on chinhphu.vn")
        return False, "Not found on chinhphu.vn"
    
    print(f"  FOUND URL: {url}")
    
    # Fetch metadata from the page
    html = fetch_metadata_page(url)
    if not html:
        print(f"  FAILED to fetch metadata page")
        return False, "Failed to fetch page"
    
    # Parse metadata
    metadata = parse_metadata_from_html(html)
    
    if not metadata:
        print(f"  NO metadata parsed from page")
        return False, "No metadata parsed"
    
    print(f"  METADATA: {metadata}")
    
    # Update file
    updated = update_file_metadata(filepath, metadata, url)
    
    if updated:
        print(f"  UPDATED successfully")
        return True, f"Updated with {url}"
    else:
        print(f"  No changes needed")
        return False, "No changes needed"

def get_files_to_process():
    """Get all files that need metadata updating."""
    files = []
    skip_files = ['index.md', 'DATABASE_CONTENT_STANDARD.md']
    
    for root, dirs, filenames in os.walk(VAN_BAN_DIR):
        for fname in filenames:
            if fname in skip_files:
                continue
            if not fname.endswith('.md'):
                continue
            if 'crawled' in root:
                continue
            
            filepath = os.path.join(root, fname)
            
            # Check if file needs updating (has "Đang cập nhật")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if 'Đang cập nhật' in content:
                    # Check if it's a content file (has "Điều" or content beyond just the table)
                    if 'Điều ' in content or 'VĂN BẢN' in content:
                        files.append(filepath)
            except:
                continue
    
    return sorted(files)

if __name__ == '__main__':
    # Just print the files to process for now
    files = get_files_to_process()
    print(f"Found {len(files)} files to process")
    for f in files[:10]:
        print(f"  - {os.path.relpath(f, BASE_DIR)}")
    print(f"  ...")

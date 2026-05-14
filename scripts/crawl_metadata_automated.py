#!/usr/bin/env python3
"""
Crawl metadata từ vanban.chinhphu.vn tự động cho các file van-ban/.
Dùng Brave Search API để tìm docid, sau đó scrape metadata.
"""

import os
import re
import sys
import json
import urllib.parse
import subprocess
import time

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN_DIR = os.path.join(WORKSPACE, "van-ban")
LOG_ENTRIES = []


def run_brave_search(query):
    """Search dùng Brave Search API qua openclaw CLI."""
    cmd = f"openclaw web search --query '{urllib.parse.quote(query)}' --count 3 2>/dev/null"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
    return result.stdout


def extract_docid_from_search(query):
    """Search và trích docid từ kết quả."""
    # Thử search trực tiếp qua vanban.chinhphu.vn
    search_url = f"https://vanban.chinhphu.vn/?pageid=27159&q={urllib.parse.quote(query)}"
    
    # Dùng curl để search
    cmd = f"curl -s -L -A 'Mozilla/5.0' '{search_url}' 2>/dev/null | head -c 5000"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
    
    # Tìm docid trong kết quả
    match = re.search(r'docid=(\d+)', result.stdout)
    if match:
        return match.group(1)
    
    # Thử tìm trong các link
    matches = re.findall(r'docid=(\d+)', result.stdout)
    if matches:
        return matches[0]
    
    return None


def scrape_metadata(docid):
    """Scrape metadata từ vanban.chinhphu.vn."""
    url = f"https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid={docid}"
    cmd = f"curl -s -L -A 'Mozilla/5.0' '{url}' 2>/dev/null | head -c 10000"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
    
    # Trích metadata từ HTML
    html = result.stdout
    metadata = {}
    
    # Tìm số hiệu
    sh_match = re.search(r'L[ƯU]?\s*?[SỐ\s]*([\d/]+\w+)', html)
    
    # Cách khác: tìm trong bảng thông tin
    # Tìm pattern: Số hiệu | xxx
    table_match = re.search(r'<table[^>]*>(.*?)</table>', html, re.DOTALL)
    if table_match:
        table_html = table_match.group(1)
        # Parse các rows
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        for row in rows:
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
            if len(cells) >= 2:
                key = re.sub(r'<[^>]+>', '', cells[0]).strip()
                val = re.sub(r'<[^>]+>', '', cells[1]).strip()
                metadata[key] = val
    
    return metadata, html


def get_frontmatter(filepath):
    """Đọc front matter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, content
    
    fm = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    
    return fm, content


def main():
    # Tìm files
    result = subprocess.run(
        f"grep -rl 'Đang cập nhật' {VAN_BAN_DIR}/ --include='*.md' 2>/dev/null | "
        f"grep -v '/an-ninh-quoc-gia/' | grep -v '/index.md$' | sort",
        shell=True, capture_output=True, text=True
    )
    files = [f for f in result.stdout.strip().split('\n') if f]
    
    print(f"Tìm thấy {len(files)} file")
    
    # Thử vài file đầu
    for i, filepath in enumerate(files[:3]):
        print(f"\n=== File {i+1}: {filepath} ===")
        fm, content = get_frontmatter(filepath)
        if fm:
            title = fm.get('title', '')
            print(f"Title: {title}")
            
            # Thử tìm docid
            docid = extract_docid_from_search(title)
            print(f"DocID: {docid}")
            
            if docid:
                meta, html = scrape_metadata(docid)
                print(f"Metadata: {meta}")


if __name__ == "__main__":
    main()

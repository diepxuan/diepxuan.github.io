#!/usr/bin/env python3
"""
Crawl metadata từ vanban.chinhphu.vn cho các file van-ban/ còn lại.
Tự động hóa: đọc file -> tìm docid -> scrape metadata -> update file -> log.
"""

import os
import re
import sys
import json
import subprocess
import time
import glob

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN_DIR = os.path.join(WORKSPACE, "van-ban")
LOG_FILE = os.path.join(WORKSPACE, "scripts", "metadata_crawl_log.md")

# Bỏ qua
SKIP_PATTERNS = [
    "an-ninh-quoc-gia/",  # đã xử lý
]
SKIP_FILES = [
    "van-ban/index.md",
    "DATABASE_CONTENT_STANDARD.md",
]


def run_exec(cmd, timeout=30):
    """Chạy shell command và return stdout."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return result.stdout.strip()


def search_docid(title, filename):
    """Search vanban.chinhphu.vn để tìm docid."""
    # Thử 1: search với title
    query = f'"vanban.chinhphu.vn" "{title}"'
    query_safe = query.replace('"', '\\"')
    result = run_exec(f"curl -s 'https://api.search.brave.com/res/v1/web/search?q={__import__(\"urllib.parse\").quote(query)}' -H 'Accept: application/json' 2>/dev/null | head -c 2000")
    
    # Thay vì dùng raw API, dùng web_search tool qua subprocess không khả thi
    # Sẽ dùng cách khác: search trực tiếp trên vanban.chinhphu.vn
    return None


def search_chinhphu(title, filename):
    """Tìm document trên vanban.chinhphu.vn bằng cách search website."""
    # Clean title for URL
    title_clean = title.strip()
    
    # Thử search trên vanban.chinhphu.vn
    search_url = f"https://vanban.chinhphu.vn/?pageid=27159&q={__import__('urllib.parse').quote(title_clean)}"
    
    return search_url


def extract_frontmatter(filepath):
    """Đọc front matter từ file markdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    fm = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    
    return fm


def find_files_to_update():
    """Tìm tất cả file cần cập nhật."""
    result = run_exec(
        f"grep -rl 'Đang cập nhật' {VAN_BAN_DIR}/ --include='*.md' 2>/dev/null | "
        f"grep -v '/an-ninh-quoc-gia/' | "
        f"grep -v '/index.md$' | "
        f"sort"
    )
    files = [f for f in result.split('\n') if f and not f.endswith('/index.md')]
    return files


def main():
    files = find_files_to_update()
    print(f"Tìm thấy {len(files)} file cần cập nhật")
    
    # Xử lý từng file
    for i, filepath in enumerate(files):
        rel_path = os.path.relpath(filepath, WORKSPACE)
        print(f"\n[{i+1}/{len(files)}] {rel_path}")
        
        fm = extract_frontmatter(filepath)
        if not fm:
            print(f"  SKIP: Không có front matter")
            continue
        
        title = fm.get('title', '')
        print(f"  Title: {title}")
        
        # TODO: Ở đây sẽ gọi API search để tìm docid
        # Vì giới hạn tool, sẽ dùng firecrawl_scrape/web_search
        
        break  # Chỉ test file đầu tiên
    
    print(f"\nTổng: {len(files)} files cần xử lý")


if __name__ == "__main__":
    main()

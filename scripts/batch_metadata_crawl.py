#!/usr/bin/env python3
"""
Batch crawl metadata từ vanban.chinhphu.vn.
Dùng Brave Search API để tìm docid, scrape metadata, update file.
"""
import os, re, sys, time, json, subprocess, urllib.parse
from pathlib import Path

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN = os.path.join(WORKSPACE, "van-ban")
LOG_FILE = os.path.join(WORKSPACE, "scripts", "metadata_crawl_log.md")

# Title mapping: file relative path -> title already extracted
SKIP_PATTERNS = ["an-ninh-quoc-gia/", "/index.md"]

def get_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m: return None, content
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip()
    return fm, content

def find_files():
    """Find all .md files with 'Đang cập nhật'"""
    result = subprocess.run(
        f"grep -rl 'Đang cập nhật' {VAN_BAN}/ --include='*.md' 2>/dev/null | sort",
        shell=True, capture_output=True, text=True
    )
    files = []
    for f in result.stdout.strip().split('\n'):
        if f and not any(p in f for p in SKIP_PATTERNS):
            files.append(f)
    return files

def search_chinhphu_title(title):
    """Search vanban.chinhphu.vn for a title, return docid if found."""
    # Use grep on cached search or just return None - we need brave search
    # For now, return None and let the caller use firecrawl
    return None

def scrape_chinhphu_page(docid):
    """Scrape a chinhphu.vn document page"""
    url = f"https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid={docid}"
    try:
        import requests
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=15)
        return r.text
    except:
        return ""

def extract_metadata_from_html(html):
    """Extract metadata from chinhphu.vn HTML"""
    if not html: return {}
    
    # Remove tags for text extraction
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    
    metadata = {}
    
    # Try to find key info in the HTML
    # Look for: Số/luật/Nghị định patterns
    number_patterns = [
        r'L[ƯU]ật?\s*s[ốỐ]\s*([\d]+/\d+/[\w-]+)',
        r'Ngh[ịị]\s*[đĐ][ịị]nh\s*s[ốỐ]\s*([\d]+/\d+/[A-Z-]+)',
        r'Thông\s*t[ưư]\s*s[ốỐ]\s*([\d]+/\d+/[A-Z-]+)',
        r'#([\d]+/\d+/[\w-]+)',
    ]
    
    for pat in number_patterns:
        m = re.search(pat, text)
        if m:
            metadata['so_hieu'] = m.group(1)
            break
    
    # Look for dates
    date_patterns = [
        r'ngày\s*[\d]+\s*tháng\s*[\d]+\s*năm\s*([\d]{4})',
    ]
    
    # Look for signing authority
    authority_patterns = [
        r'(Quốc\s* hội|Chính\s*phủ|Bộ\s*trưởng|Thủ\s*tướng)[\s,]',
    ]
    
    return metadata

def update_file(filepath, metadata):
    """Update file with new metadata"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not metadata:
        return content, False
    
    changed = False
    for key, val in metadata.items():
        old_val = f"| Đang cập nhật |"  
        # This needs specific row matching
        pass
    
    return content, changed

def main():
    files = find_files()
    print(f"Found {len(files)} files to process")
    
    for i, f in enumerate(files[:10]):
        rel = os.path.relpath(f, WORKSPACE)
        fm, content = get_frontmatter(f)
        if fm:
            print(f"[{i+1}] {rel}: title={fm.get('title','?')}")

if __name__ == "__main__":
    main()

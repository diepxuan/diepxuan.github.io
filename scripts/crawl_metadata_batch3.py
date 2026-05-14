#!/usr/bin/env python3
"""
Batch crawl & update metadata cho van-ban/ files.
Dùng firecrawl_search để tìm docid, firecrawl_scrape để lấy metadata, edit để update file.
"""
import os, re, sys, json, time, urllib.parse

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN_DIR = os.path.join(WORKSPACE, "van-ban")
LOG_FILE = os.path.join(WORKSPACE, "scripts", "metadata_crawl_log.md")

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def get_title(content):
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m: return None
    for line in m.group(1).split('\n'):
        if line.startswith('title:'):
            return line.split(':', 1)[1].strip()
    return None

def get_permalink(content):
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m: return None
    for line in m.group(1).split('\n'):
        if line.startswith('permalink:'):
            return line.split(':', 1)[1].strip()
    return None

def find_files():
    """Find files with 'Đang cập nhật' excluding specific ones."""
    result = os.popen(
        f"grep -rl 'Đang cập nhật' {VAN_BAN_DIR}/ --include='*.md' 2>/dev/null | sort"
    ).read().strip().split('\n')
    files = []
    for f in result:
        if not f or not f.endswith('.md'): continue
        if '/an-ninh-quoc-gia/' in f: continue
        if f.endswith('/index.md'): continue
        if f.endswith('DATABASE_CONTENT_STANDARD.md'): continue
        # Skip files containing already-known docid patterns
        try:
            raw = read_file(f)
        except: continue
        if any(p in raw for p in ['24/2018', '32/2019', '14/2019', '19/2012']):
            continue
        files.append(f)
    return files

def update_metadata_table(content, metadata, chinhphu_url):
    """Replace 'Đang cập nhật' with actual values in the metadata table."""
    replacements = {}
    field_map = {
        'so_hieu': 'Số hiệu',
        'loai_vb': 'Loại văn bản',
        'noi_ban_hanh': 'Nơi ban hành',
        'nguoi_ky': 'Người ký',
        'ngay_ban_hanh': 'Ngày ban hành',
        'ngay_hieu_luc': 'Ngày hiệu lực',
        'trang_thai': 'Trạng thái',
        'linh_vuc': 'Lĩnh vực',
        'ngay_cong_bo': 'Ngày công bố',
    }
    
    changes = []
    for key, label in field_map.items():
        if key in metadata:
            pat = rf'(\*\*{re.escape(label)}\*\*\s*\|)\s*Đang cập nhật\s*\|'
            if re.search(pat, content):
                content = re.sub(pat, rf'| {metadata[key]} |', content)
                changes.append(f"{label}={metadata[key]}")
    
    # Update source line - add Chinhphu link
    if chinhphu_url and 'vanban.chinhphu.vn' not in content.split('**Nguồn**', 1)[-1][:200] if '**Nguồn**' in content else True:
        # Find the Nguồn line
        patng = r'(\*\*Nguồn\*\*\s*\|)([^\|]+)(\|[^\|]+\|)'
        m = re.search(patng, content)
        if m and 'Chinhphu.vn' not in m.group(2) and 'vanban.chinhphu.vn' not in m.group(2):
            cp_link = f" [Chinhphu.vn]({chinhphu_url}) |"
            content = content.replace(m.group(2), cp_link + m.group(2), 1)
            changes.append("source=chinhphu")
    
    return content, changes

def main():
    files = find_files()
    print(f"Found {len(files)} files to process")
    
    logs = []
    success = 0
    fail = 0
    skip = 0
    
    for i, filepath in enumerate(files):
        rel_path = os.path.relpath(filepath, WORKSPACE)
        content = read_file(filepath)
        title = get_title(content)
        
        print(f"\n[{i+1}/{len(files)}] {rel_path}")
        print(f"  Title: {title}")
        
        # Generate search query based on title
        if not title:
            fail += 1
            logs.append(f"- ❌ `{rel_path}`: Không có title")
            continue
        
        # Search on vanban.chinhphu.vn
        search_query = f"site:vanban.chinhphu.vn {title}"
        
        # Use Brave Search (the one that works)
        import subprocess
        result = subprocess.run(
            ['python3', '-c', f'''
import urllib.request, json, re
url = "https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(search_query)}&count=3"
# Use web_fetch via curl instead
'''],
            capture_output=True, text=True
        )
        
        # Actually, let me use firecrawl_search for each batch
        # For now, just print what we need
        print(f"  SEARCH: {search_query}")
        break  # Test one
    
    print(f"\nTotal: {len(files)} files")

if __name__ == "__main__":
    main()

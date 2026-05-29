#!/usr/bin/env python3
"""
Crawl metadata từ vanban.chinhphu.vn cho các file van-ban/ còn lại.
Dùng requests + BeautifulSoup với session để search và scrape.
"""

import os
import re
import sys
import json
import time
import subprocess
import urllib.parse
import requests
from bs4 import BeautifulSoup

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN_DIR = os.path.join(WORKSPACE, "van-ban")
LOG_FILE = os.path.join(WORKSPACE, "scripts", "metadata_crawl_log.md")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
}

s = requests.Session()
s.headers.update(HEADERS)

def read_frontmatter(filepath):
    """Read frontmatter from md file, return (fm_dict, full_content)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None, content
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip()
    return fm, content

def find_files_to_update():
    """Find all .md files with 'Đang cập nhật' that need processing."""
    result = subprocess.run(
        f"grep -rl 'Đang cập nhật' {VAN_BAN_DIR}/ --include='*.md' 2>/dev/null | sort",
        shell=True, capture_output=True, text=True
    )
    files = []
    for f in result.stdout.strip().split('\n'):
        if not f or not f.endswith('.md'):
            continue
        if '/an-ninh-quoc-gia/' in f or f.endswith('/index.md'):
            continue
        files.append(f)
    return files

def search_docid_on_chinhphu(query):
    """Search vanban.chinhphu.vn and return first docid found."""
    url = f"https://vanban.chinhphu.vn/?pageid=27159&q={urllib.parse.quote(query)}"
    try:
        r = s.get(url, timeout=15, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Look for docid in links
        for a in soup.find_all('a', href=True):
            href = a['href']
            match = re.search(r'docid=(\d+)', href)
            if match:
                return match.group(1), href
    except Exception as e:
        print(f"    Search error: {e}")
    return None, None

def scrape_metadata(docid):
    """Scrape metadata table from chinhphu document page."""
    url = f"https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid={docid}"
    try:
        r = s.get(url, timeout=15, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        metadata = {}
        
        # Method 1: Parse HTML tables
        for table in soup.find_all('table'):
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 2:
                    key_text = cells[0].get_text(strip=True).lower()
                    val_text = cells[1].get_text(strip=True)
                    
                    if 'số hiệu' in key_text or 'so hieu' in key_text:
                        metadata['so_hieu'] = val_text
                    elif 'loại văn bản' in key_text or 'loai' in key_text:
                        metadata['loai_vb'] = val_text
                    elif 'cơ quan' in key_text or 'co quan' in key_text or 'nơi ban hành' in key_text:
                        metadata['noi_ban_hanh'] = val_text
                    elif 'người ký' in key_text or 'nguoi ky' in key_text:
                        metadata['nguoi_ky'] = val_text
                    elif 'ngày ban hành' in key_text or 'ngay ban hanh' in key_text:
                        metadata['ngay_ban_hanh'] = val_text
                    elif 'hiệu lực' in key_text or 'hieu luc' in key_text:
                        metadata['ngay_hieu_luc'] = val_text
                    elif 'trạng thái' in key_text or 'trang thai' in key_text:
                        metadata['trang_thai'] = val_text
        
        # Method 2: Regex fallback on full text
        if not metadata:
            text = soup.get_text()
            text = re.sub(r'\s+', ' ', text)
            
            patterns = {
                'so_hieu': r'[Ss]ố hiệu[:\s|]+(\d+/\d+/[\w-]+)',
                'loai_vb': r'[Ll]oại văn bản[:\s|]+([^\n|,]+)',
                'noi_ban_hanh': r'[Cc]ơ quan[:\s|]+([^\n|,]+)',
                'nguoi_ky': r'[Nn]gười ký[:\s|]+([^\n|,]+)',
                'ngay_ban_hanh': r'[Nn]gày ban hành[:\s|]+([^\n|,]+)',
                'ngay_hieu_luc': r'[Nn]gày hiệu lực[:\s|]+([^\n|,]+)',
            }
            for key, pat in patterns.items():
                m = re.search(pat, text)
                if m:
                    metadata[key] = m.group(1).strip()
        
        return metadata
    except Exception as e:
        print(f"    Scrape error: {e}")
        return {}

def update_file_md(filepath, metadata, source_url):
    """Update markdown file metadata table with new values."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # Mapping from metadata keys to table rows
    field_map = [
        ('so_hieu', r'\*\*Số hiệu\*\*'),
        ('loai_vb', r'\*\*Loại văn bản\*\*'),
        ('noi_ban_hanh', r'\*\*Nơi ban hành\*\*'),
        ('nguoi_ky', r'\*\*Người ký\*\*'),
        ('ngay_ban_hanh', r'\*\*Ngày ban hành\*\*'),
        ('ngay_hieu_luc', r'\*\*Ngày hiệu lực\*\*'),
    ]
    
    for meta_key, table_row_pattern in field_map:
        if meta_key in metadata and metadata[meta_key]:
            # Replace "Đang cập nhật" next to the field
            pat = rf'({table_row_pattern}\s*\|)\s*Đang cập nhật\s*\|'
            if re.search(pat, content):
                content = re.sub(pat, rf'\1 {metadata[meta_key]} |', content)
                changes.append(f"{meta_key}={metadata[meta_key]}")
    
    # Update source line - add Chinhphu link
    if source_url:
        old_source = re.search(r'\| \*\*Nguồn\*\*.*\|', content)
        if old_source:
            old_line = old_source.group(0)
            if 'Chinhphu.vn' not in old_line and 'vanban.chinhphu.vn' not in old_line:
                chinhphu_link = f"[Chinhphu.vn]({source_url})"
                new_line = old_line.replace('| [Thư Viện', f'| {chinhphu_link} | [Thư Viện', 1)
                content = content.replace(old_line, new_line)
                changes.append("source_updated")
    
    return content, changes

def get_log_entry(rel_path, metadata, success):
    """Generate log entry."""
    if success and metadata:
        so_hieu = metadata.get('so_hieu', 'N/A')
        return f"- ✅ `{rel_path}`: Số hiệu={so_hieu}"
    else:
        return f"- ❌ `{rel_path}`: Không tìm thấy metadata"

def main():
    files = find_files_to_update()
    print(f"Found {len(files)} files to process")
    
    all_logs = []
    success_count = 0
    fail_count = 0
    skip_count = 0
    
    for i, filepath in enumerate(files):
        rel_path = os.path.relpath(filepath, WORKSPACE)
        print(f"\n[{i+1}/{len(files)}] {rel_path}")
        
        # Skip known patterns
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                raw = f.read()
        except:
            fail_count += 1
            all_logs.append(f"- ❌ `{rel_path}`: Cannot read file")
            continue
        
        skip_patterns = ['24/2018', '32/2019', '14/2019', '19/2012']
        if any(p in raw for p in skip_patterns):
            print(f"    SKIP: Contains known pattern")
            skip_count += 1
            all_logs.append(f"- ⏭️ `{rel_path}`: Skipped (known pattern)")
            time.sleep(0.5)
            continue
        
        # Get frontmatter
        fm, content = read_frontmatter(filepath)
        if not fm:
            print(f"    FAIL: No frontmatter")
            fail_count += 1
            all_logs.append(f"- ❌ `{rel_path}`: No frontmatter")
            continue
        
        title = fm.get('title', '')
        permalink = fm.get('permalink', '')
        print(f"    Title: {title}")
        
        # Try to find docid
        docid = None
        doc_url = None
        
        # Strategy 1: Search with title
        docid, doc_url = search_docid_on_chinhphu(title)
        
        # Strategy 2: Search with filename-based query
        if not docid:
            stem = os.path.splitext(os.path.basename(filepath))[0]
            query = stem.replace('-', ' ')
            docid, doc_url = search_docid_on_chinhphu(query)
        
        if not docid:
            print(f"    FAIL: No docid found")
            fail_count += 1
            all_logs.append(f"- ❌ `{rel_path}`: Không tìm thấy docid")
            time.sleep(1)
            continue
        
        print(f"    DocID: {docid}")
        full_url = f"https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid={docid}"
        
        # Scrape metadata
        time.sleep(1.5)
        metadata = scrape_metadata(docid)
        
        if not metadata:
            print(f"    FAIL: No metadata extracted")
            fail_count += 1
            all_logs.append(f"- ❌ `{rel_path}`: Không trích xuất được metadata")
            continue
        
        print(f"    Metadata: {metadata}")
        
        # Update file
        time.sleep(1)
        new_content, field_changes = update_file_md(filepath, metadata, full_url)
        
        if field_changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"    UPDATED: {field_changes}")
            success_count += 1
            all_logs.append(f"- ✅ `{rel_path}`: {', '.join(field_changes)}")
        else:
            print(f"    FAIL: Could not update file")
            fail_count += 1
            all_logs.append(f"- ❌ `{rel_path}`: Không cập nhật được file format")
        
        time.sleep(1.5)
    
    # Write log
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write('# Metadata Crawl Log\n\n')
        f.write('## Batch 2 (2026-05-14)\n\n')
        for entry in all_logs:
            f.write(entry + '\n')
        f.write(f'\n---\n**Summary:** {success_count} success, {fail_count} fail, {skip_count} skipped\n')
    
    print(f"\n{'='*60}")
    print(f"COMPLETE: {success_count} updated, {fail_count} failed, {skip_count} skipped")
    print(f"Log: {LOG_FILE}")

if __name__ == "__main__":
    main()

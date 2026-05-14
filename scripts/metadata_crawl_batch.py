#!/usr/bin/env python3
"""
Auto-crawl metadata từ vanban.chinhphu.vn cho các van-ban/.md files.
Dùng requests + BeautifulSoup để search và scrape.
"""

import os
import re
import requests
import json
import time
import urllib.parse
from bs4 import BeautifulSoup
from pathlib import Path

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"
VAN_BAN_DIR = os.path.join(WORKSPACE, "van-ban")
LOG_FILE = os.path.join(WORKSPACE, "scripts", "metadata_crawl_log.md")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}

session = requests.Session()
session.headers.update(HEADERS)

SKIP_PATTERNS = ["an-ninh-quoc-gia/"]

def get_frontmatter(filepath):
    """Extract title from markdown frontmatter."""
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

def search_docid(query, max_retries=2):
    """Search vanban.chinhphu.vn for docid."""
    search_url = f"https://vanban.chinhphu.vn/?pageid=27159&q={urllib.parse.quote(query)}"
    for attempt in range(max_retries + 1):
        try:
            r = session.get(search_url, timeout=15, allow_redirects=True)
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Find links to documents that contain docid
            for link in soup.find_all('a', href=True):
                href = link.get('href', '')
                if 'docid=' in href:
                    match = re.search(r'docid=(\d+)', href)
                    if match:
                        docid = match.group(1)
                        # Check if this is likely the right document
                        title_el = link.find_parent('h2') or link.find_next_sibling(re.compile(r'^h[2-6]'))
                        if title_el or link.text.strip():
                            return docid
            return None
        except Exception as e:
            if attempt < max_retries:
                time.sleep(2 ** attempt)
            else:
                print(f"Search failed for '{query}': {e}")
                return None

def extract_metadata_from_page(docid):
    """Scrape metadata from vanban.chinhphu.vn document page."""
    url = f"https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid={docid}"
    try:
        r = session.get(url, timeout=15, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        metadata = {}
        
        # Look for metadata table
        for table in soup.find_all('table'):
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    key = cells[0].get_text(strip=True)
                    val = cells[1].get_text(strip=True)
                    # Map to standard keys
                    key_lower = key.lower()
                    if 'số hiệu' in key_lower or 'so hieu' in key_lower:
                        metadata['so_hieu'] = val
                    elif 'loại' in key_lower or 'loai' in key_lower:
                        metadata['loai_vb'] = val
                    elif 'cơ quan' in key_lower or 'co quan' in key_lower or 'nơi' in key_lower or 'noi' in key_lower:
                        metadata['noi_ban_hanh'] = val
                    elif 'người ký' in key_lower or 'nguoi ky' in key_lower:
                        metadata['nguoi_ky'] = val
                    elif 'ngày ban hành' in key_lower or 'ngay ban hanh' in key_lower:
                        metadata['ngay_ban_hanh'] = val
                    elif 'ngày hiệu lực' in key_lower or 'ngay hieu luc' in key_lower:
                        metadata['ngay_hieu_luc'] = val
                    elif 'trạng thái' in key_lower or 'trang thai' in key_lower:
                        metadata['trang_thai'] = val
                    elif 'lĩnh vực' in key_lower or 'linh vuc' in key_lower:
                        metadata['linh_vuc'] = val
                    elif 'ngày công bố' in key_lower or 'ngay cong bo' in key_lower:
                        metadata['ngay_cong_bo'] = val
        
        # If table approach fails, try extracting from text
        if not metadata:
            text = soup.get_text()
            text = re.sub(r'\s+', ' ', text)
            
            # Try regex patterns
            patterns = {
                'so_hieu': r'(?:Số|So) hiệu\s*[|:]\s*([^\n|,]+)',
                'loai_vb': r'(?:Loại|Loai) văn bản\s*[|:]\s*([^\n|,]+)',
                'noi_ban_hanh': r'(?:Cơ quan|Co quan) ban hành\s*[|:]\s*([^\n|,]+)',
                'nguoi_ky': r'(?:Người ký|Nguoi ky)\s*[|:]\s*([^\n|,]+)',
                'ngay_ban_hanh': r'(?:Ngày ban hành|Ngay ban hanh)\s*[|:]\s*([^\n|,]+)',
                'ngay_hieu_luc': r'(?:Ngày hiệu lực|Ngay hieu luc)\s*[|:]\s*([^\n|,]+)',
                'trang_thai': r'(?:Trạng thái|Trang thai)\s*[|:]\s*([^\n|,]+)',
            }
            
            for key, pat in patterns.items():
                m = re.search(pat, text, re.IGNORECASE)
                if m:
                    metadata[key] = m.group(1).strip()
        
        return metadata
    except Exception as e:
        print(f"Failed to extract metadata for docid {docid}: {e}")
        return {}

def update_file_metadata(filepath, metadata):
    """Update the markdown file with new metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not metadata:
        return content, False, []
    
    changes = []
    # Replace "Đang cập nhật" with actual values
    replacements = {
        'Đang cập nhật': {  # Will be handled individually per field
            'so_hieu': metadata.get('so_hieu'),
            'loai_vb': metadata.get('loai_vb'),
            'noi_ban_hanh': metadata.get('noi_ban_hanh'),
            'nguoi_ky': metadata.get('nguoi_ky'),
            'ngay_ban_hanh': metadata.get('ngay_ban_hanh'),
            'ngay_hieu_luc': metadata.get('ngay_hieu_luc'),
        }
    }
    
    # Find the metadata table and update it
    # Pattern: | **Số hiệu** | Đang cập nhật |
    table_pattern = r'(\*\*Số hiệu\*\*\s*\|)\s*Đang cập nhật\s*\|'
    if 'so_hieu' in metadata and metadata['so_hieu']:
        new_content = re.sub(table_pattern, r' ' + metadata['so_hieu'] + ' |', content)
        if new_content != content:
            changes.append(('Số hiệu', metadata['so_hieu']))
            content = new_content
    
    # Similar for other fields...
    field_patterns = {
        'loai_vb': (r'(\*\*Loại văn bản\*\*\s*\|)\s*Đang cập nhật\s*\|', metadata.get('loai_vb')),
        'noi_ban_hanh': (r'(\*\*Nơi ban hành\*\*\s*\|)\s*Đang cập nhật\s*\|', metadata.get('noi_ban_hanh')),
        'nguoi_ky': (r'(\*\*Người ký\*\*\s*\|)\s*Đang cập nhật\s*\|', metadata.get('nguoi_ky')),
        'ngay_ban_hanh': (r'(\*\*Ngày ban hành\*\*\s*\|)\s*Đang cập nhật\s*\|', metadata.get('ngay_ban_hanh')),
        'ngay_hieu_luc': (r'(\*\*Ngày hiệu lực\*\*\s*\|)\s*Đang cập nhật\s*\|', metadata.get('ngay_hieu_luc')),
    }
    
    for field, (pattern, value) in field_patterns.items():
        if value:
            new_content = re.sub(pattern, rf'| {value} |', content)
            if new_content != content:
                changes.append((field, value))
                content = new_content
    
    return content, len(changes) > 0, changes

def find_skip_files():
    """Find files to skip."""
    skip = set()
    for root, dirs, files in os.walk(VAN_BAN_DIR):
        for f in files:
            if 'an-ninh-quoc-gia' in root:
                skip.add(os.path.join(root, f))
            if f == 'index.md':
                skip.add(os.path.join(root, f))
    return skip

def main():
    skip_files = find_skip_files()
    
    # Find files that need updating
    files_to_update = []
    for root, dirs, files in os.walk(VAN_BAN_DIR):
        for f in files:
            if f.endswith('.md') and f != 'index.md':
                filepath = os.path.join(root, f)
                if filepath in skip_files:
                    continue
                # Check if file contains "Đang cập nhật"
                try:
                    with open(filepath, 'r', encoding='utf-8') as fh:
                        content = fh.read()
                    if 'Đang cập nhật' in content:
                        files_to_update.append(filepath)
                except:
                    continue
    
    print(f"Found {len(files_to_update)} files to update")
    
    # Process files in batches
    batch_size = 10
    logs = []
    
    for i in range(0, len(files_to_update), batch_size):
        batch = files_to_update[i:i+batch_size]
        print(f"\n=== Processing batch {i//batch_size + 1} ({len(batch)} files) ===")
        
        for idx, filepath in enumerate(batch):
            rel_path = os.path.relpath(filepath, WORKSPACE)
            print(f"[{i+idx+1}/{len(files_to_update)}] {rel_path}")
            
            # Skip if already has 24/2018, 32/2019, etc (task instructions)
            with open(filepath, 'r') as f:
                content = f.read()
            if any(pattern in content for pattern in ['24/2018', '32/2019', '14/2019', '19/2012']):
                print(f"  SKIP: Contains known patterns")
                logs.append(f"- ⚠️ `{rel_path}`: Contains known patterns, skipped")
                continue
            
            fm, original_content = get_frontmatter(filepath)
            if not fm:
                print(f"  SKIP: No front matter")
                logs.append(f"- ❌ `{rel_path}`: Không có front matter")
                continue
            
            title = fm.get('title', '')
            print(f"  Title: {title}")
            
            # Extract a searchable identifier from the filename
            filename_stem = os.path.splitext(os.path.basename(filepath))[0]
            
            # Search for docid
            search_query = title  # Try title first
            
            # If title search fails, try filename-based query
            docid = search_docid(search_query)
            
            if not docid:
                # Try filename-based search
                filename_search = filename_stem.replace('-', ' ').title()
                docid = search_docid(filename_search)
            
            if not docid:
                print(f"  WARNING: Could not find docid")
                logs.append(f"- ❌ `{rel_path}`: Không tìm thấy docid")
                time.sleep(1)
                continue
            
            print(f"  DocID: {docid}")
            
            # Extract metadata
            time.sleep(1)  # Be polite
            metadata = extract_metadata_from_page(docid)
            
            if not metadata:
                print(f"  WARNING: Could not extract metadata")
                logs.append(f"- ❌ `{rel_path}`: Không trích xuất được metadata")
                continue
            
            print(f"  Metadata: {metadata}")
            logs.append(f"- ✅ `{rel_path}`: Số hiệu={metadata.get('so_hieu', 'N/A')}")
            
            # Update file
            time.sleep(1)  # Be polite
            new_content, changed, field_changes = update_file_metadata(filepath, metadata)
            
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  UPDATED: {field_changes}")
            else:
                print(f"  NO CHANGES: Could not match metadata table format")
            
            time.sleep(1)  # Rate limiting
        
        # Commit after each batch
        subprocess.call(['git', 'add', 'van-ban/'], cwd=WORKSPACE)
        subprocess.call(['git', 'commit', '-m', f'feat: update metadata batch {i//batch_size + 1}'], cwd=WORKSPACE)
    
    # Write log
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write('# Metadata Crawl Log\n\n')
        for entry in logs:
            f.write(entry + '\n')
    
    print(f"\nDone! Processed {len(files_to_update)} files")
    print(f"Log written to {LOG_FILE}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script tự động thêm bảng THÔNG TIN VĂN BẢN cho tất cả file van-ban/.
- Files có số hiệu cụ thể: tìm metadata qua web search
- Files compilation/index: "Đang cập nhật" + URL tra cứu
"""
import os
import re
import sys
import json
import subprocess
import time

VANBAN_DIR = "/root/.openclaw/workspace/projects/github-io/van-ban"
LOG_FILE = "/root/.openclaw/workspace/projects/github-io/scripts/metadata_update_log.md"
BATCH_SIZE = 50

# Files đã có bảng (list from command)
HAS_TABLE_FILES = set()
NO_TABLE_FILES = []

def load_files():
    global HAS_TABLE_FILES, NO_TABLE_FILES
    with open("/tmp/vanban_has_table.txt") as f:
        HAS_TABLE_FILES = set(line.strip() for line in f if line.strip())
    with open("/tmp/vanban_all.txt") as f:
        all_files = [line.strip() for line in f if line.strip()]
    NO_TABLE_FILES = [f for f in all_files if f not in HAS_TABLE_FILES]
    
def extract_title(filepath):
    """Extract title from YAML front matter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if m:
        fm = m.group(1)
        title_m = re.search(r'^title:\s*(.+)$', fm, re.MULTILINE)
        if title_m:
            return title_m.group(1).strip()
    return None

def extract_body(filepath):
    """Extract everything after the front matter (body content)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if m:
        return m.group(2)
    return ""

def extract_body_after_vanban(filepath):
    """Extract body starting from ## VĂN BẢN section"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Check if body already has ## VĂN BẢN
    m_vanban = re.search(r'\n## VĂN BẢN\s*\n(.*)', content, re.DOTALL)
    if m_vanban:
        return m_vanban.group(1)
    # Otherwise get everything after front matter
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if m:
        return m.group(2)
    return ""

def build_search_url(title):
    """Build search URL for tra cứu"""
    # Use thuvienphapluat.vn search
    return f"https://thuvienphapluat.vn/Search.aspx?keyword={title.replace(' ', '+')}"

def build_vbpl_search(title):
    """Build vbpl.vn search URL"""
    return f"https://vbpl.vn/TW/Pages/vbsearch.aspx?ItemID=&Type=all&txtKeyword={title.replace(' ', '+')}"

def build_luatvietnam_search(title):
    """Build luatvietnam search URL"""
    return f"https://luatvietnam.vn/search?q={title.replace(' ', '+')}"

def web_search(query):
    """Use web_search via openclaw CLI to search"""
    try:
        result = subprocess.run(
            ['openclaw', 'tools', 'web_search', '--query', query, '--count', '3'],
            capture_output=True, text=True, timeout=15
        )
        return result.stdout
    except:
        return None

def search_metadata(title, filename):
    """Try to find metadata for a document using web search"""
    # This is a placeholder - we'll use web_fetch for actual lookups
    return None

def is_specific_document(filename):
    """Check if file name contains specific document number pattern"""
    patterns = [
        r'nghi-dinh-\d+',
        r'thong-tu-\d+',
        r'luat-\d+',
        r'quyet-dinh-\d+',
        r'phap-lenh-\d+',
        r'chi-thi-\d+',
    ]
    basename = os.path.basename(filename).lower()
    for p in patterns:
        if re.search(p, basename):
            return True
    return False

def extract_number_from_filename(filename):
    """Extract document number patterns like 'nghi-dinh-68-2026-nd-cp' from filename"""
    basename = os.path.basename(filename).lower().replace('.md', '')
    # Pattern: type-number-year-...
    m = re.search(r'(nghi-dinh|thong-tu|luat|quyet-dinh|phap-lenh|chi-thi)[-_](\d+)[-_](\d+)[-_](.+)', basename)
    if m:
        return {
            'type': m.group(1),
            'number': m.group(2),
            'year': m.group(3),
            'suffix': m.group(4)
        }
    return None

def generate_info_table(file_path, title, metadata=None):
    """Generate the THÔNG TIN VĂN BẢN table"""
    if metadata:
        so_hieu = metadata.get('so_hieu', 'Đang cập nhật')
        loai = metadata.get('loai', 'Đang cập nhật')
        noi = metadata.get('noi', 'Đang cập nhật')
        nguoi_ky = metadata.get('nguoi_ky', 'Đang cập nhật')
        ngay_ban_hanh = metadata.get('ngay_ban_hanh', 'Đang cập nhật')
        ngay_hieu_luc = metadata.get('ngay_hieu_luc', 'Đang cập nhật')
        trang_thai = metadata.get('trang_thai', 'Còn hiệu lực')
        source_url = metadata.get('source_url', '')
    else:
        so_hieu = 'Đang cập nhật'
        loai = 'Đang cập nhật'
        noi = 'Đang cập nhật'
        nguoi_ky = 'Đang cập nhật'
        ngay_ban_hanh = 'Đang cập nhật'
        ngay_hieu_luc = 'Đang cập nhật'
        trang_thai = 'Đang cập nhật'
        source_url = ''
    
    # Build source URLs
    sources = []
    if source_url:
        sources.append(f'[{source_url}]({source_url})')
    else:
        search_q = title.replace(' ', '+') if title else 'phap+luat'
        sources.append(f'[Thư Viện Pháp Luật](https://thuvienphapluat.vn/Search.aspx?keyword={title.replace(" ", "+")})')
        sources.append(f'[VBPL](https://vbpl.vn/TW/Pages/vbsearch.aspx?txtKeyword={title.replace(" ", "+")})')
        sources.append(f'[LuatVietnam](https://luatvietnam.vn/search?q={title.replace(" ", "+")})')
    
    source_str = ' • '.join(sources)
    
    table = f"""## THÔNG TIN VĂN BẢN

| Thuộc tính | Nội dung |
|---|---|
| **Số hiệu** | {so_hieu} |
| **Loại văn bản** | {loai} |
| **Nơi ban hành** | {noi} |
| **Người ký** | {nguoi_ky} |
| **Ngày ban hành** | {ngay_ban_hanh} |
| **Ngày hiệu lực** | {ngay_hieu_luc} |
| **Trạng thái** | {trang_thai} |
| **Nguồn** | {source_str} |

---

## VĂN BẢN
"""
    return table

def update_file(filepath, status, log_entries):
    """Update a single file"""
    title = extract_title(filepath)
    if not title:
        log_entries.append(f"- **BỎ QUA** (không có title): `{filepath}`\n")
        return False
    
    filename = os.path.basename(filepath)
    
    # Check if the file already has a table (in HAS_TABLE_FILES)
    if filepath in HAS_TABLE_FILES:
        log_entries.append(f"- **ĐÃ CÓ BẢNG**: `{filepath}` → Cập nhật nguồn\n")
        # Still need to add source URLs - handled separately
        return False
    
    # Try to extract specific doc number from filename
    doc_info = extract_number_from_filename(filename)
    
    metadata = None
    if doc_info:
        # Has specific document number - mark for manual lookup later
        status['pending'].append(filename)
    
    # Get body content
    body = extract_body(filepath)
    
    # Check if body already has "## VĂN BẢN"
    has_vanban = "## VĂN BẢN" in body
    
    if has_vanban:
        # Replace from ## THÔNG TIN VĂN BẢN to end with new version
        # Find position of first ## after front matter
        table = generate_info_table(filepath, title, metadata)
        
        # Remove any existing ## sections before ## VĂN BẢN  
        # (like "## Danh sách đề mục", "## Danh sách điều khoản")
        new_body = re.sub(
            r'(##(?! VĂN BẢN).+\n(?:[-#\s*].*\n)*(?=\n))',
            '',
            body[:body.index('## VĂN BẢN')]
        )
        remaining = body[body.index('## VĂN BẢN'):]
        # Remove the ## VĂN BẢN header from remaining since table already includes it
        remaining = remaining[len('## VĂN BẢN'):].lstrip()
        
        new_content = body[:body.index('## VĂN BẢN')] + table + remaining
    else:
        table = generate_info_table(filepath, title, metadata)
        new_content = table + body

    # Update front matter lastedit
    front_matter_end = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    fm_match = re.search(r'^(---\s*\n(?:.*?)\n---\s*\n)', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        if 'lastedit:' in fm:
            new_fm = re.sub(r'lastedit:\s*\S+', 'lastedit: 2026-05-13', fm)
        else:
            new_fm = fm.rstrip()[:-4] + 'lastedit: 2026-05-13\n---\n'
        new_content = new_fm + body[:len(body)]
        # Actually, rebuild from clean parts
        fm_content = content[:fm_match.end()]
        body_content = content[fm_match.end():]
        new_fm = re.sub(r'lastedit:\s*\S+', 'lastedit: 2026-05-13', fm_content)
        
        has_vanban2 = "## VĂN BẢN" in body_content
        if has_vanban2:
            before_vanban = body_content[:body_content.index('## VĂN BẢN')]
            after_vanban = body_content[body_content.index('## VĂN BẢN'):]
            after_vanban = after_vanban[len('## VĂN BẢN'):].lstrip()
            new_content = new_fm + table + after_vanban
        else:
            new_content = new_fm + table + body_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    status['done'] += 1
    log_entries.append(f"- **CẬP NHẬT**: `{filepath}` - Table added\n")
    return True

def update_existing_table(filepath):
    """Update existing table to add URL nguồn"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    fm_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    title = fm_match.group(1).strip() if fm_match else ""
    
    # Check if already has **Nguồn** row
    if re.search(r'\|\s*\*\*Nguồn\*\*\s*\|', content):
        # Has Nguồn row but might lack URLs
        # Check if the source cell has URLs
        src_match = re.search(r'\|\s*\*\*Nguồn\*\*\s*\|\s*(.+?)\s*\|', content)
        if src_match:
            src_text = src_match.group(1)
            # Check if it already has markdown links
            if '[' in src_text and ']' in src_text and '(' in src_text and ')' in src_text:
                return False  # Already has URLs
    
    # Update lastedit
    content = re.sub(r'lastedit:\s*\S+', 'lastedit: 2026-05-13', content)
    
    # Extract the table section
    table_match = re.search(r'(## THÔNG TIN VĂN BẢN\s*\n\|.*?\|[\s\S]*?---)', content)
    if not table_match:
        return False
    
    # If has Nguồn without URLs, add them
    if "## THÔNG TIN VĂN BẢN" in content and "**Nguồn**" in content:
        # Find the nguồn line and add URLs if missing
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if '**Nguồn**' in line:
                # Extract current source text
                src_m = re.search(r'\|\s*\*\*Nguồn\*\*\s*\|\s*(.+?)\s*\|', line)
                if src_m:
                    current = src_m.group(1).strip()
                    if not ('[' in current and '(' in current):
                        # Add search URLs
                        search_q = title.replace(' ', '+')
                        urls = f'[Thư Viện Pháp Luật](https://thuvienphapluat.vn/Search.aspx?keyword={search_q})'
                        new_line = line.replace(current, urls)
                        line = new_line
            new_lines.append(line)
        content = '\n'.join(new_lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    load_files()
    
    status = {
        'done': 0,
        'pending': [],
        'skipped': 0,
        'errors': []
    }
    
    log_entries = []
    log_entries.append(f"# Metadata Update Log\n\n")
    log_entries.append(f"Ngày: 2026-05-13\n")
    log_entries.append(f"Tổng file (không có table): {len(NO_TABLE_FILES)}\n")
    log_entries.append(f"Files đã có table: {len(HAS_TABLE_FILES)}\n\n")
    log_entries.append("## Kết quả xử lý\n\n")
    
    # Process files without table
    for i, filepath in enumerate(NO_TABLE_FILES):
        try:
            update_file(filepath, status, log_entries)
            if (i + 1) % 50 == 0:
                log_entries.append(f"\n--- Batch {i+1} files processed ---\n")
                # Write log periodically
                with open(LOG_FILE, 'w', encoding='utf-8') as f:
                    f.write(''.join(log_entries))
                print(f"Processed {i+1}/{len(NO_TABLE_FILES)} files...")
        except Exception as e:
            status['errors'].append(f"`${filepath}` - Error: {e}")
            log_entries.append(f"- **LỖI**: `{filepath}` - {e}\n")
    
    # Process existing tables - add URLs
    updated_tables = 0
    for filepath in HAS_TABLE_FILES:
        try:
            if update_existing_table(filepath):
                updated_tables += 1
        except Exception as e:
            status['errors'].append(f"`{filepath}` - Error: {e}")
    
    log_entries.append(f"\n## Tóm tắt\n\n")
    log_entries.append(f"- Files đã cập nhật thêm table: **{status['done']}**\n")
    log_entries.append(f"- Files đã cập nhật URL cho table có sẵn: **{updated_tables}**\n")
    log_entries.append(f"- Files pending (có số hiệu cụ thể, cần tìm metadata): **{len(status['pending'])}**\n")
    log_entries.append(f"- Files lỗi: **{len(status['errors'])}**\n")
    
    if status['pending']:
        log_entries.append(f"\n## Files Pending (cần tìm metadata thủ công)\n\n")
        for p in status['pending'][:100]:
            log_entries.append(f"- {p}\n")
    
    if status['errors']:
        log_entries.append(f"\n## Lỗi\n\n")
        for e in status['errors']:
            log_entries.append(f"- {e}\n")
    
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(''.join(log_entries))
    
    print(f"\nDone! Processed {status['done']} new tables, {updated_tables} updated tables")
    print(f"Pending: {len(status['pending'])}, Errors: {len(status['errors'])}")
    print(f"Log: {LOG_FILE}")

if __name__ == '__main__':
    main()

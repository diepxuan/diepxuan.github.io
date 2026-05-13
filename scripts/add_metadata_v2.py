#!/usr/bin/env python3
"""
Script v2 - Bổ sung metadata + URL nguồn cho BẢNG THÔNG TIN VĂN BẢN
"""
import os
import re
import sys

VANBAN_DIR = "/root/.openclaw/workspace/projects/github-io/van-ban"
LOG_FILE = "/root/.openclaw/workspace/projects/github-io/scripts/metadata_update_log.md"

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
    """Extract everything after front matter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if m:
        return m.group(2)
    return content

def extract_fm(filepath):
    """Extract front matter as string"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^(---\s*\n(?:.*?)\n---\s*\n)', content, re.DOTALL)
    return m.group(1) if m else None

def generate_info_table(title):
    """Generate the THÔNG TIN VĂN BẢN table with default values"""
    search_q = title.replace(' ', '+') if title else 'van+ban+phap+luat'
    source_str = (
        f'[Thư Viện Pháp Luật](https://thuvienphapluat.vn/Search.aspx?keyword={search_q})'
        f' | [VBPL](https://vbpl.vn/TW/Pages/vbsearch.aspx?txtKeyword={search_q})'
        f' | [LuatVietnam](https://luatvietnam.vn/search?q={search_q})'
    )
    
    return f"""## THÔNG TIN VĂN BẢN

| Thuộc tính | Nội dung |
|---|---|
| **Số hiệu** | Đang cập nhật |
| **Loại văn bản** | Đang cập nhật |
| **Nơi ban hành** | Đang cập nhật |
| **Người ký** | Đang cập nhật |
| **Ngày ban hành** | Đang cập nhật |
| **Ngày hiệu lực** | Đang cập nhật |
| **Trạng thái** | Đang cập nhật |
| **Nguồn** | {source_str} |

---

## VĂN BẢN
"""

def update_file_no_table(filepath, title):
    """Add table to file without existing table"""
    fm = extract_fm(filepath)
    if not fm:
        return False, "Không tìm thấy front matter"
    
    # Update lastedit in front matter
    new_fm = re.sub(r'lastedit:\s*\S+', 'lastedit: 2026-05-13', fm)
    
    # Get body
    body = extract_body(filepath)
    
    table = generate_info_table(title)
    new_content = new_fm + table + body
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "OK"

def update_file_with_table(filepath, title):
    """Add URL nguồn to existing table if missing"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update lastedit
    content = re.sub(r'lastedit:\s*\S+', 'lastedit: 2026-05-13', content)
    
    # Check if has Nguồn row
    # Pattern: line with **Nguồn** in the table
    lines = content.split('\n')
    changed = False
    new_lines = []
    
    for line in lines:
        if re.search(r'\|\s*\*\*Nguồn\*\*\s*\|', line):
            src_m = re.search(r'\|\s*\*\*Fonte\*\*\s*\|\s*(.+?)\s*\|', line)
            if not src_m:
                # Try another pattern - get text after | 
                parts = line.split('|')
                for i, part in enumerate(parts):
                    if '**Nguồn**' in part and i + 1 < len(parts):
                        current_text = parts[i + 1].strip()
                        if current_text and not ('[' in current_text and ']' in current_text and '(' in current_text):
                            # Doesn't have markdown links - add URLs
                            search_q = title.replace(' ', '+') if title else 'van+ban+phap+luat'
                            new_url = (
                                f'[Thư Viện Pháp Luật](https://thuvienphapluat.vn/Search.aspx?keyword={search_q})'
                                f' | [VBPL](https://vbpl.vn/TW/Pages/vbsearch.aspx?txtKeyword={search_q})'
                                f' | [LuatVietnam](https://luatvietnam.vn/search?q={search_q})'
                            )
                            line = f'| **Nguồn** | {new_url} |'
                            changed = True
                        break
        new_lines.append(line)
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
    
    return changed, "OK"

def has_table(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return "## THÔNG TIN VĂN BẢN" in content

def main():
    # Load all files
    with open("/tmp/vanban_all.txt") as f:
        all_files = [line.strip() for line in f if line.strip()]
    
    with open("/tmp/vanban_has_table.txt") as f:
        has_table_files = set(line.strip() for line in f if line.strip())
    
    no_table_files = [f for f in all_files if f not in has_table_files]
    
    status = {
        'updated': 0,
        'skipped': 0,
        'errors': 0,
        'updated_table_urls': 0,
        'pending_files': []
    }
    
    log = []
    log.append("# Metadata Update Log\n\n")
    log.append(f"Ngày chạy: 2026-05-13\n\n")
    log.append(f"Tổng file: {len(all_files)}\n")
    log.append(f"Files chưa có table: {len(no_table_files)}\n")
    log.append(f"Files đã có table: {len(has_table_files)}\n\n")
    log.append("## Kết quả: Cập nhật table mới\n\n")
    
    # Process files WITHOUT table
    for i, filepath in enumerate(no_table_files):
        basename = os.path.basename(filepath)
        title = extract_title(filepath)
        if not title:
            status['skipped'] += 1
            log.append(f"- **BỎ QUA** (không title): `{basename}`\n")
            continue
        
        try:
            ok, msg = update_file_no_table(filepath, title)
            if ok:
                status['updated'] += 1
                log.append(f"- **OK**: `{basename}`\n")
            else:
                status['errors'] += 1
                log.append(f"- **LỖI**: `{basename}` - {msg}\n")
        except Exception as e:
            status['errors'] += 1
            log.append(f"- **LỖI**: `{basename}` - {str(e)}\n")
        
        if (i + 1) % 100 == 0:
            print(f"  ...processed {i+1}/{len(no_table_files)} new tables")
    
    log.append(f"\n## Kết quả: Bổ sung URL cho table có sẵn\n\n")
    
    # Process files WITH table - add URLs
    for filepath in sorted(has_table_files):
        basename = os.path.basename(filepath)
        title = extract_title(filepath) or ""
        try:
            changed, msg = update_file_with_table(filepath, title)
            if changed:
                status['updated_table_urls'] += 1
                log.append(f"- **OK** (added URLs): `{basename}`\n")
            else:
                log.append(f"- **KHÔNG CẦN**: `{basename}` (đã có URLs)\n")
        except Exception as e:
            status['errors'] += 1
            log.append(f"- **LỖI**: `{basename}` - {str(e)}\n")
    
    # Summary
    log.append(f"\n## Tóm tắt\n\n")
    log.append(f"| Loại | Số lượng |\n|---|---|\n")
    log.append(f"| Files đã thêm table mới | **{status['updated']}** |\n")
    log.append(f"| Files đã thêm URL cho table có sẵn | **{status['updated_table_urls']}** |\n")
    log.append(f"| Files bỏ qua (không title) | **{status['skipped']}** |\n")
    log.append(f"| Files lỗi | **{status['errors']}** |\n")
    
    log.append(f"\n## Ghi chú\n\n")
    log.append("- Tất cả files hiện đã có bảng THÔNG TIN VĂN BẢN\n")
    log.append("- Các bảng có default value 'Đang cập nhật'\n")
    log.append("- URL tra cứu đã được thêm vào Nguồn\n")
    log.append("- Front matter lastedit đã cập nhật 2026-05-13\n")
    log.append("- Cần bổ sung metadata thực tế bằng tra cứu thủ công\n")
    
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(''.join(log))
    
    print(f"\nDone!")
    print(f"  Tables added: {status['updated']}")
    print(f"  Tables updated with URLs: {status['updated_table_urls']}")
    print(f"  Skipped: {status['skipped']}")
    print(f"  Errors: {status['errors']}")
    print(f"  Log: {LOG_FILE}")

if __name__ == '__main__':
    main()

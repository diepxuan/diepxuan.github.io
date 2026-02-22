#!/usr/bin/env python3
"""
Parse toàn bộ 76,303 entries bằng cách bỏ qua entry bị lỗi
"""

import re
import json
import sys
from pathlib import Path

def parse_json_array_robust(json_str):
    """
    Parse JSON array robustly, bỏ qua entries bị lỗi
    """
    entries = []
    pos = 0
    length = len(json_str)
    entry_count = 0
    error_count = 0
    
    print(f"Đang parse JSON string, độ dài: {length:,} chars")
    
    # Skip whitespace và dấu [
    while pos < length and json_str[pos] in ' \t\n\r[':
        pos += 1
    
    while pos < length:
        # Skip whitespace và dấu phẩy
        while pos < length and json_str[pos] in ' \t\n\r,':
            pos += 1
        
        if pos >= length:
            break
        
        # Check for array end
        if json_str[pos] == ']':
            break
        
        # Parse object
        if json_str[pos] == '{':
            entry_start = pos
            entry_str, new_pos = extract_json_object(json_str, pos)
            
            if entry_str:
                # Try to parse this entry
                try:
                    entry = json.loads(entry_str)
                    entries.append(entry)
                    entry_count += 1
                    
                    # Progress report
                    if entry_count % 5000 == 0:
                        print(f"  Đã parse {entry_count:,} entries, errors: {error_count}")
                    
                    pos = new_pos
                except json.JSONDecodeError as e:
                    error_count += 1
                    print(f"  ⚠ Entry {entry_count+1} bị lỗi: {e}")
                    print(f"    Context: {json_str[pos:pos+200]}...")
                    
                    # Skip to next entry
                    # Tìm dấu } tiếp theo hoặc dấu , tiếp theo
                    next_brace = json_str.find('}', pos)
                    next_comma = json_str.find(',', pos)
                    
                    if next_brace != -1:
                        pos = next_brace + 1
                    elif next_comma != -1:
                        pos = next_comma + 1
                    else:
                        # Không tìm thấy, có thể đã hết
                        break
            else:
                # Cannot extract object, skip
                error_count += 1
                print(f"  ⚠ Không thể extract object tại vị trí {pos}")
                
                # Tìm dấu { tiếp theo
                next_brace = json_str.find('{', pos + 1)
                if next_brace != -1:
                    pos = next_brace
                else:
                    break
        else:
            # Unexpected character, skip
            pos += 1
    
    print(f"\n✓ Parse hoàn tất:")
    print(f"  - Tổng entries: {entry_count:,}")
    print(f"  - Lỗi bỏ qua: {error_count}")
    
    return entries

def extract_json_object(json_str, start_pos):
    """
    Trích xuất JSON object từ string
    """
    if start_pos >= len(json_str) or json_str[start_pos] != '{':
        return None, start_pos
    
    brace_count = 0
    in_string = False
    escape = False
    
    for i in range(start_pos, len(json_str)):
        char = json_str[i]
        
        if escape:
            escape = False
            continue
        
        if char == '\\':
            escape = True
            continue
        
        if char == '"' and not escape:
            in_string = not in_string
            continue
        
        if not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    # Found complete object
                    return json_str[start_pos:i+1], i+1
    
    # Object không đóng
    return None, start_pos

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    if not json_file.exists():
        print(f"File không tồn tại: {json_file}")
        return
    
    print(f"Đang đọc file: {json_file}")
    print(f"Kích thước: {json_file.stat().st_size:,} bytes")
    
    # Đọc file với BOM handling
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    print(f"Đã đọc {len(content):,} chars")
    
    # Tìm jdAllTree
    print("\nTìm jdAllTree...")
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("✗ Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    print(f"✓ Tìm thấy jdAllTree, độ dài: {len(json_str):,} chars")
    
    # Parse toàn bộ entries
    print("\nBắt đầu parse toàn bộ entries (có thể mất vài phút)...")
    all_entries = parse_json_array_robust(json_str)
    
    # Lưu kết quả
    output_file = base_dir / "output" / "all_entries_parsed.json"
    output_file.parent.mkdir(exist_ok=True)
    
    print(f"\nĐang lưu {len(all_entries):,} entries vào {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Đã lưu thành công!")
    
    # Thống kê
    print(f"\n📊 THỐNG KÊ:")
    print(f"  - Tổng entries parsed: {len(all_entries):,}")
    
    if all_entries:
        # Sample entries
        print(f"\n📝 SAMPLE ENTRIES:")
        
        # Entry đầu tiên
        first = all_entries[0]
        print(f"  Entry #1:")
        print(f"    ID: {first.get('ID')}")
        print(f"    TEN: {first.get('TEN')[:80]}..." if first.get('TEN') and len(first.get('TEN')) > 80 else f"    TEN: {first.get('TEN')}")
        
        # Entry ở giữa
        middle_idx = len(all_entries) // 2
        middle = all_entries[middle_idx]
        print(f"\n  Entry #{middle_idx:,}:")
        print(f"    ID: {middle.get('ID')}")
        print(f"    TEN: {middle.get('TEN')[:80]}..." if middle.get('TEN') and len(middle.get('TEN')) > 80 else f"    TEN: {middle.get('TEN')}")
        
        # Entry cuối cùng
        last = all_entries[-1]
        print(f"\n  Entry #{len(all_entries):,} (cuối cùng):")
        print(f"    ID: {last.get('ID')}")
        print(f"    TEN: {last.get('TEN')[:80]}..." if last.get('TEN') and len(last.get('TEN')) > 80 else f"    TEN: {last.get('TEN')}")
    
    # Tạo summary
    summary_file = base_dir / "output" / "parse_all_summary.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# PARSE ALL ENTRIES - SUMMARY\n\n")
        f.write(f"**Date**: {Path(__file__).parent.parent.name}\n")
        f.write(f"**Total Entries Parsed**: {len(all_entries):,}\n")
        f.write(f"**Output File**: `{output_file.relative_to(base_dir)}`\n")
        f.write(f"**File Size**: {output_file.stat().st_size:,} bytes\n\n")
        
        if all_entries:
            f.write("## Sample Entries\n\n")
            f.write("### First Entry\n")
            f.write(f"- ID: {all_entries[0].get('ID')}\n")
            f.write(f"- TEN: {all_entries[0].get('TEN')}\n")
            f.write(f"- MAPC: {all_entries[0].get('MAPC')}\n\n")
            
            f.write("### Last Entry\n")
            f.write(f"- ID: {all_entries[-1].get('ID')}\n")
            f.write(f"- TEN: {all_entries[-1].get('TEN')}\n")
            f.write(f"- MAPC: {all_entries[-1].get('MAPC')}\n")
    
    print(f"\n✓ Đã tạo summary: {summary_file}")

if __name__ == "__main__":
    main()
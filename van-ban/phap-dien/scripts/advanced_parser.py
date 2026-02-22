#!/usr/bin/env python3
"""
Advanced parser cho Phap Dien JSON data.
Parser này có thể bỏ qua các entry bị broken và tiếp tục parse các entry hợp lệ sau đó.
"""

import json
import re
from typing import List, Dict, Any

def parse_jdalltree_advanced(content: str) -> List[Dict[str, Any]]:
    """
    Parse jdAllTree từ content với khả năng bỏ qua entry bị broken.
    
    Args:
        content: Toàn bộ nội dung file jsonData.js
        
    Returns:
        List các entry đã parse được
    """
    
    # Tìm jdAllTree
    tree_start = content.find('jdAllTree = [')
    if tree_start == -1:
        tree_start = content.find('jdAllTree:[')
    
    if tree_start == -1:
        raise ValueError("Could not find jdAllTree in content")
    
    # Tìm vị trí bắt đầu thực sự của array
    array_start = content.find('[', tree_start)
    if array_start == -1:
        raise ValueError("Could not find array start")
    
    # Parse bằng cách duyệt từng ký tự để tìm các entry
    entries = []
    pos = array_start + 1  # Bắt đầu sau '['
    depth = 0
    entry_start = -1
    
    print(f"Starting advanced parse from position {pos}")
    print(f"Total content length: {len(content)}")
    
    while pos < len(content):
        char = content[pos]
        
        if char == '{':
            if depth == 0:
                entry_start = pos
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0 and entry_start != -1:
                # Tìm thấy kết thúc của một entry
                entry_text = content[entry_start:pos+1]
                
                # Thử parse entry
                try:
                    entry = json.loads(entry_text)
                    entries.append(entry)
                    
                    # Log progress
                    if len(entries) % 1000 == 0:
                        print(f"  Parsed {len(entries)} entries...")
                        
                except json.JSONDecodeError as e:
                    print(f"  WARNING: Failed to parse entry at position {entry_start}: {e}")
                    print(f"  Entry text (first 200 chars): {entry_text[:200]}...")
                    print(f"  Entry text (last 100 chars): ...{entry_text[-100:]}")
                    
                    # Vẫn thêm entry text để debug
                    entries.append({
                        '_parse_error': True,
                        '_error': str(e),
                        '_position': entry_start,
                        '_text': entry_text[:500] + '...' if len(entry_text) > 500 else entry_text
                    })
                
                entry_start = -1
        elif char == ']' and depth == 0:
            # Kết thúc array
            print(f"Reached end of array at position {pos}")
            break
        
        pos += 1
    
    print(f"\nAdvanced parse completed. Total entries parsed: {len(entries)}")
    
    # Phân tích kết quả
    valid_entries = [e for e in entries if not isinstance(e, dict) or '_parse_error' not in e]
    error_entries = [e for e in entries if isinstance(e, dict) and '_parse_error' in e]
    
    print(f"Valid entries: {len(valid_entries)}")
    print(f"Error entries: {len(error_entries)}")
    
    if error_entries:
        print("\nError entries details:")
        for i, err_entry in enumerate(error_entries[:5]):  # Chỉ hiển thị 5 lỗi đầu tiên
            print(f"  Error {i+1}:")
            print(f"    Position: {err_entry['_position']}")
            print(f"    Error: {err_entry['_error']}")
            print(f"    Text preview: {err_entry['_text'][:100]}...")
    
    return valid_entries

def find_specific_entry(entries: List[Dict[str, Any]], entry_id: str) -> Dict[str, Any]:
    """Tìm entry cụ thể bằng ID"""
    for entry in entries:
        if isinstance(entry, dict) and entry.get('ID') == entry_id:
            return entry
    return None

def main():
    # Đọc file
    input_file = '../json/jsonData.js'
    print(f"Reading file: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    print(f"File size: {len(content)} characters")
    
    # Parse với advanced parser
    entries = parse_jdalltree_advanced(content)
    
    # Tìm entry cụ thể mà sếp tìm thấy
    target_id = 'AA4C41EB-CC02-4629-8077-3691D02E64F2'
    target_entry = find_specific_entry(entries, target_id)
    
    if target_entry:
        print(f"\n✓ FOUND target entry with ID {target_id}:")
        print(f"  TEN: {target_entry.get('TEN')}")
        print(f"  MAPC: {target_entry.get('MAPC')}")
        print(f"  ChuDeID: {target_entry.get('ChuDeID')}")
        print(f"  DeMucID: {target_entry.get('DeMucID')}")
    else:
        print(f"\n✗ Target entry with ID {target_id} NOT FOUND in parsed entries")
        
        # Kiểm tra xem có trong error entries không
        for entry in entries:
            if isinstance(entry, dict) and '_parse_error' in entry:
                if target_id in entry.get('_text', ''):
                    print(f"  But found in error entry at position {entry['_position']}")
                    print(f"  Error: {entry['_error']}")
    
    # Lưu kết quả
    output_file = '../json/advanced_parsed_entries.json'
    print(f"\nSaving {len(entries)} entries to {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    
    print("Done!")

if __name__ == "__main__":
    main()
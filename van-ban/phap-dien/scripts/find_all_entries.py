#!/usr/bin/env python3
"""
Script để tìm tất cả entries trong jsonData.js và xác định vị trí của entry bị broken
và entry hợp lệ mà sếp tìm thấy.
"""

import json
import re

def find_all_entries():
    """Tìm tất cả entries trong file jsonData.js"""
    
    with open('../json/jsonData.js', 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    print(f"Total file size: {len(content)} characters")
    
    # Tìm jdAllTree bằng cách tìm từ "jdAllTree:[" đến "],jdDeMuc"
    start_marker = "jdAllTree:["
    end_marker = "],jdDeMuc"
    
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("ERROR: Could not find jdAllTree")
        return
    
    start_pos += len(start_marker)
    end_pos = content.find(end_marker, start_pos)
    
    if end_pos == -1:
        print("ERROR: Could not find end of jdAllTree")
        return
    
    tree_content = content[start_pos:end_pos]
    print(f"\njdAllTree content length: {len(tree_content)} characters")
    print(f"Tree start position: {start_pos}")
    print(f"Tree end position: {end_pos}")
    
    # Tìm tất cả entries bằng regex
    # Pattern để tìm mỗi entry: bắt đầu bằng {, kết thúc bằng }, theo sau là , hoặc kết thúc chuỗi
    entries = []
    pos = 0
    
    while pos < len(tree_content):
        # Tìm { tiếp theo
        start = tree_content.find('{', pos)
        if start == -1:
            break
        
        # Tìm } tương ứng
        depth = 0
        i = start
        while i < len(tree_content):
            if tree_content[i] == '{':
                depth += 1
            elif tree_content[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i
                    break
            i += 1
        else:
            # Không tìm thấy } đóng
            print(f"WARNING: Unclosed {{ at position {start} (relative: {start})")
            break
        
        entry_text = tree_content[start:end+1]
        entries.append({
            'start': start_pos + start,
            'end': start_pos + end + 1,
            'text': entry_text,
            'relative_start': start,
            'relative_end': end + 1
        })
        
        pos = end + 1
    
    print(f"\nFound {len(entries)} entries")
    
    # Tìm entry hợp lệ mà sếp tìm thấy
    search_id = "AA4C41EB-CC02-4629-8077-3691D02E64F2"
    valid_entry_idx = -1
    
    for i, entry in enumerate(entries):
        if search_id in entry['text']:
            valid_entry_idx = i
            print(f"\nFound valid entry at index {i}:")
            print(f"  Absolute position: {entry['start']}")
            print(f"  Relative position: {entry['relative_start']}")
            print(f"  Entry length: {len(entry['text'])}")
            
            # Thử parse
            try:
                parsed = json.loads(entry['text'])
                print(f"  Successfully parsed: ID={parsed.get('ID')}, TEN={parsed.get('TEN')[:50]}...")
            except json.JSONDecodeError as e:
                print(f"  JSON parse error: {e}")
            break
    
    # Tìm entry bị broken (ở vị trí 5,568,331)
    broken_pos = 5568331
    broken_entry_idx = -1
    
    for i, entry in enumerate(entries):
        if entry['start'] <= broken_pos < entry['end']:
            broken_entry_idx = i
            print(f"\nFound broken entry at index {i}:")
            print(f"  Absolute position: {entry['start']} to {entry['end']}")
            print(f"  Entry length: {len(entry['text'])}")
            print(f"  First 200 chars: {entry['text'][:200]}...")
            print(f"  Last 100 chars: ...{entry['text'][-100:]}")
            
            # Thử parse
            try:
                parsed = json.loads(entry['text'])
                print(f"  Successfully parsed (unexpected!)")
            except json.JSONDecodeError as e:
                print(f"  JSON parse error (expected): {e}")
                print(f"  Error position in entry: {e.pos}")
                print(f"  Error message: {e.msg}")
            break
    
    # Phân tích số entries trước/sau broken entry
    if broken_entry_idx != -1:
        print(f"\nEntries before broken entry: {broken_entry_idx}")
        print(f"Entries after broken entry: {len(entries) - broken_entry_idx - 1}")
        
        # Kiểm tra xem có entries hợp lệ sau broken entry không
        if valid_entry_idx > broken_entry_idx:
            print(f"\nVALID entry is AFTER broken entry (difference: {valid_entry_idx - broken_entry_idx} entries)")
            print(f"Number of valid entries after broken entry: {len(entries) - broken_entry_idx - 1}")
        else:
            print(f"\nVALID entry is BEFORE broken entry")
    
    # Lưu thông tin về entries
    with open('../json/entries_analysis.json', 'w', encoding='utf-8') as f:
        analysis = {
            'total_entries': len(entries),
            'valid_entry_index': valid_entry_idx,
            'broken_entry_index': broken_entry_idx,
            'entries_before_broken': broken_entry_idx if broken_entry_idx != -1 else None,
            'entries_after_broken': len(entries) - broken_entry_idx - 1 if broken_entry_idx != -1 else None,
            'entry_positions': [
                {
                    'index': i,
                    'start': entry['start'],
                    'end': entry['end'],
                    'length': len(entry['text'])
                }
                for i, entry in enumerate(entries[:100])  # Chỉ lưu 100 entries đầu tiên
            ]
        }
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    
    print(f"\nAnalysis saved to ../json/entries_analysis.json")

if __name__ == "__main__":
    find_all_entries()
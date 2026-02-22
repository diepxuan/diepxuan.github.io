#!/usr/bin/env python3
"""
Phân tích vấn đề JSON chi tiết
"""

import re
from pathlib import Path

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    # Đọc file với BOM handling
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    # Tìm jdAllTree
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    
    # Tìm entry có vấn đề (entry 18650)
    # Tìm entry thứ 18650
    print("Tìm entry có vấn đề...")
    
    # Đếm số lượng dấu ngoặc nhọn mở
    entries = []
    pos = 0
    entry_start = 0
    
    while pos < len(json_str):
        if json_str[pos] == '{':
            entry_start = pos
            brace_count = 0
            in_string = False
            escape = False
            
            for i in range(pos, len(json_str)):
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
                            entry = json_str[pos:i+1]
                            entries.append((pos, i+1, entry))
                            pos = i + 1
                            break
            
            if brace_count != 0:
                print(f"Entry không đóng tại vị trí {pos}")
                break
        else:
            pos += 1
        
        if len(entries) >= 18660:  # Lấy thêm 10 entries sau entry có vấn đề
            break
    
    print(f"Đã tìm thấy {len(entries)} entries")
    
    # Kiểm tra entry 18649 (index 18648 vì bắt đầu từ 0)
    if len(entries) > 18648:
        start, end, entry = entries[18648]
        print(f"\nEntry 18650 (index 18648):")
        print(f"Vị trí: {start} - {end}")
        print(f"Độ dài: {len(entry)} chars")
        print(f"\nNội dung entry:")
        print(entry[:500] + "..." if len(entry) > 500 else entry)
        
        # Tìm trường TEN
        ten_match = re.search(r'"TEN"\s*:\s*"([^"]*)"', entry)
        if ten_match:
            ten_value = ten_match.group(1)
            print(f"\nGiá trị TEN: {ten_value}")
            print(f"Độ dài TEN: {len(ten_value)} chars")
            
            # Kiểm tra ký tự đặc biệt
            print(f"\nKiểm tra ký tự đặc biệt trong TEN:")
            for i, char in enumerate(ten_value):
                if ord(char) > 127 or char in '[]{}':
                    print(f"  Position {i}: {repr(char)} (ord={ord(char)})")
    
    # Kiểm tra entry trước và sau
    print(f"\n\nKiểm tra entry 18649 và 18651...")
    for idx in [18647, 18648, 18649]:
        if idx < len(entries):
            start, end, entry = entries[idx]
            ten_match = re.search(r'"TEN"\s*:\s*"([^"]*)"', entry)
            if ten_match:
                ten_value = ten_match.group(1)
                print(f"Entry {idx+1}: TEN = {ten_value[:50]}...")
            else:
                print(f"Entry {idx+1}: Không tìm thấy TEN hoặc format sai")
                
                # Tìm thủ công
                ten_pos = entry.find('"TEN":')
                if ten_pos != -1:
                    print(f"  Có \"TEN\": tại vị trí {ten_pos}")
                    # Lấy 100 ký tự sau đó
                    context = entry[ten_pos:ten_pos+100]
                    print(f"  Context: {context}")

if __name__ == "__main__":
    main()
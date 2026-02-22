#!/usr/bin/env python3
"""
Kiểm tra chính xác vị trí lỗi
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
    
    # Vị trí lỗi: 5568466
    error_pos = 5568466
    
    print(f"Kiểm tra vị trí chính xác {error_pos}...")
    print(f"Độ dài JSON string: {len(json_str)}")
    
    if error_pos >= len(json_str):
        print(f"Vị trí lỗi {error_pos} vượt quá độ dài string {len(json_str)}")
        return
    
    # Hiển thị 50 ký tự trước và sau vị trí lỗi
    start = max(0, error_pos - 100)
    end = min(len(json_str), error_pos + 100)
    
    print(f"\nContext từ {start} đến {end}:")
    print("-" * 80)
    context = json_str[start:end]
    print(context)
    print("-" * 80)
    
    # Đánh dấu vị trí lỗi trong context
    marker_pos = error_pos - start
    print(f"\nVị trí lỗi (ký tự {marker_pos} trong context trên):")
    print(" " * marker_pos + "↑")
    
    # Hiển thị các ký tự xung quanh
    print(f"\nKý tự tại vị trí lỗi và xung quanh:")
    for i in range(max(0, error_pos-10), min(len(json_str), error_pos+11)):
        char = json_str[i]
        marker = "←" if i == error_pos else " "
        print(f"  {i:8}: {repr(char)} {marker}")
    
    # Tìm xem chúng ta đang ở đâu trong JSON structure
    print(f"\nPhân tích cấu trúc xung quanh vị trí lỗi:")
    
    # Tìm dấu ngoặc kép mở gần nhất trước vị trí lỗi
    quote_pos = error_pos - 1
    while quote_pos >= 0 and json_str[quote_pos] != '"':
        quote_pos -= 1
    
    if quote_pos >= 0 and json_str[quote_pos] == '"':
        print(f"  Dấu ngoặc kép mở gần nhất tại vị trí: {quote_pos}")
        
        # Kiểm tra xem có phải là giá trị của TEN không
        # Tìm xem trước đó có "TEN": không
        ten_search = json_str[max(0, quote_pos-20):quote_pos]
        if '"TEN"' in ten_search or '"TEN":' in ten_search:
            print(f"  Có vẻ đang ở trong giá trị của trường TEN")
            
            # Tìm dấu ngoặc kép đóng
            next_quote = json_str.find('"', quote_pos + 1)
            if next_quote != -1:
                print(f"  Dấu ngoặc kép đóng tiếp theo tại: {next_quote}")
                print(f"  Giá trị TEN: {json_str[quote_pos+1:next_quote]}")
            else:
                print(f"  KHÔNG TÌM THẤY dấu ngoặc kép đóng!")
                
                # Tìm xem kết thúc ở đâu (dấu phẩy hoặc dấu ngoặc nhọn)
                comma_pos = json_str.find(',', quote_pos + 1)
                brace_pos = json_str.find('}', quote_pos + 1)
                
                end_pos = min(comma_pos, brace_pos) if comma_pos != -1 and brace_pos != -1 else \
                         comma_pos if comma_pos != -1 else brace_pos
                
                if end_pos != -1:
                    print(f"  Có thể kết thúc tại: {end_pos} (ký tự: {json_str[end_pos]})")
                    print(f"  Giá trị TEN (không có dấu ngoặc kép đóng): {json_str[quote_pos+1:end_pos]}")
    
    # Tìm entry bắt đầu gần nhất
    print(f"\nTìm entry chứa vị trí lỗi...")
    
    # Tìm dấu { gần nhất trước vị trí lỗi
    brace_pos = error_pos - 1
    while brace_pos >= 0 and json_str[brace_pos] != '{':
        brace_pos -= 1
    
    if brace_pos >= 0 and json_str[brace_pos] == '{':
        print(f"  Entry bắt đầu tại: {brace_pos}")
        
        # Tìm dấu } tương ứng
        brace_count = 0
        in_string = False
        escape = False
        
        for i in range(brace_pos, len(json_str)):
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
                        print(f"  Entry kết thúc tại: {i}")
                        print(f"  Độ dài entry: {i - brace_pos + 1} chars")
                        
                        # Hiển thị entry
                        entry = json_str[brace_pos:i+1]
                        print(f"\nEntry (first 500 chars):")
                        print(entry[:500] + "..." if len(entry) > 500 else entry)
                        break

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Tìm entry bị lỗi chính xác
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
    
    # Tìm vị trí lỗi (5568466)
    error_pos = 5568466
    
    print(f"Tìm kiếm xung quanh vị trí lỗi {error_pos}...")
    
    # Tìm entry bắt đầu gần vị trí lỗi
    # Tìm dấu ngoặc nhọn mở gần nhất trước vị trí lỗi
    pos = error_pos - 1000  # Tìm trong phạm vi 1000 ký tự trước lỗi
    
    while pos > 0 and json_str[pos] != '{':
        pos -= 1
    
    if json_str[pos] == '{':
        print(f"\nTìm thấy dấu {{ tại vị trí {pos}")
        
        # Tìm dấu ngoặc nhọn đóng tương ứng
        brace_count = 0
        in_string = False
        escape = False
        entry_end = -1
        
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
                        entry_end = i
                        break
        
        if entry_end != -1:
            entry = json_str[pos:entry_end+1]
            print(f"\nEntry từ {pos} đến {entry_end} (độ dài: {len(entry)} chars):")
            print("-" * 80)
            print(entry)
            print("-" * 80)
            
            # Phân tích entry
            # Tìm trường TEN
            ten_match = re.search(r'"TEN"\s*:\s*"([^"]*)', entry)
            if ten_match:
                ten_value = ten_match.group(1)
                print(f"\nTrường TEN (có thể không đầy đủ): {ten_value}")
                
                # Tìm xem TEN kết thúc ở đâu
                # Tìm dấu phẩy hoặc dấu ngoặc nhọn đóng sau TEN
                ten_start = ten_match.start(1)
                ten_content_start = ten_match.start(0) + len('"TEN":')
                
                # Tìm từ vị trí bắt đầu của giá trị TEN
                search_pos = ten_content_start
                while search_pos < len(entry) and entry[search_pos] != '"':
                    search_pos += 1
                
                if search_pos < len(entry) and entry[search_pos] == '"':
                    # Đã tìm thấy dấu ngoặc kép mở
                    search_pos += 1
                    
                    # Tìm dấu ngoặc kép đóng
                    while search_pos < len(entry):
                        if entry[search_pos] == '\\':
                            search_pos += 2  # Skip escape sequence
                            continue
                        elif entry[search_pos] == '"':
                            print(f"\nTEN đầy đủ: {entry[ten_content_start:search_pos+1]}")
                            break
                        search_pos += 1
                    else:
                        print(f"\nKhông tìm thấy dấu ngoặc kép đóng cho TEN")
                        
                        # Hiển thị phần còn lại của entry sau TEN
                        print(f"Phần sau TEN: {entry[ten_content_start:ten_content_start+200]}...")
            
            # Kiểm tra toàn bộ entry có hợp lệ không
            print(f"\nKiểm tra cấu trúc entry:")
            
            # Đếm số lượng dấu ngoặc kép
            quote_count = entry.count('"')
            print(f"  Số lượng dấu \": {quote_count} (phải là số chẵn)")
            
            # Đếm số lượng dấu hai chấm
            colon_count = entry.count(':')
            print(f"  Số lượng : (colon): {colon_count}")
            
            # Kiểm tra các trường bắt buộc
            required_fields = ['ID', 'ChiMuc', 'MAPC', 'TEN', 'ChuDeID', 'DeMucID']
            for field in required_fields:
                if f'"{field}"' in entry:
                    print(f"  ✓ Có trường {field}")
                else:
                    print(f"  ✗ Thiếu trường {field}")
    
    # Tìm entry tiếp theo sau vị trí lỗi
    print(f"\n\nTìm entry tiếp theo sau vị trí lỗi ({error_pos})...")
    
    next_pos = error_pos + 1
    while next_pos < len(json_str) and json_str[next_pos] != '{':
        next_pos += 1
    
    if next_pos < len(json_str) and json_str[next_pos] == '{':
        print(f"Tìm thấy dấu {{ tiếp theo tại vị trí {next_pos}")
        
        # Lấy 500 ký tự sau đó để xem
        context = json_str[next_pos:next_pos+500]
        print(f"Context (500 chars):")
        print(context)

if __name__ == "__main__":
    main()
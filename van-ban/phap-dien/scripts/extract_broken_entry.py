#!/usr/bin/env python3
"""
Trích xuất entry bị lỗi và fix nó
"""

import re
import json
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
    
    # Entry bắt đầu tại 5568331
    entry_start = 5568331
    
    print(f"Entry bắt đầu tại: {entry_start}")
    
    # Tìm entry kết thúc (tìm dấu } đóng)
    # Nhưng vì entry bị lỗi, chúng ta cần tìm thủ công
    # Tìm dấu phẩy tiếp theo hoặc dấu ngoặc nhọn đóng
    
    # Tìm từ entry_start
    pos = entry_start
    
    # Tìm dấu } đóng (nhưng có thể không có vì entry bị lỗi)
    # Thay vào đó, tìm pattern của entry tiếp theo
    next_entry_pattern = r'\},\s*\{'
    next_match = re.search(next_entry_pattern, json_str[pos:pos+1000])
    
    if next_match:
        entry_end = pos + next_match.start() + 1  # Vị trí của } trước dấu phẩy
        entry = json_str[pos:entry_end+1]
        print(f"\nTìm thấy entry tiếp theo, entry hiện tại kết thúc tại: {entry_end}")
    else:
        # Không tìm thấy entry tiếp theo, có thể đây là entry cuối cùng
        # Tìm dấu ] đóng mảng
        array_end = json_str.find(']', pos)
        if array_end != -1:
            # Tìm dấu } cuối cùng trước ]
            last_brace = json_str.rfind('}', pos, array_end)
            if last_brace != -1:
                entry_end = last_brace
                entry = json_str[pos:entry_end+1]
                print(f"\nĐây là entry cuối cùng, kết thúc tại: {entry_end}")
            else:
                # Không tìm thấy dấu } đóng
                print(f"\nKhông tìm thấy dấu }} đóng trước ]")
                return
        else:
            print(f"\nKhông tìm thấy ] đóng mảng")
            return
    
    print(f"\nEntry (độ dài: {len(entry)} chars):")
    print("-" * 80)
    print(entry)
    print("-" * 80)
    
    # Phân tích entry
    print(f"\nPhân tích entry:")
    
    # Tìm các trường
    fields = ['ID', 'ChiMuc', 'MAPC', 'TEN', 'ChuDeID', 'DeMucID']
    
    for field in fields:
        field_pattern = f'"{field}"\\s*:\\s*"([^"]*)'
        match = re.search(field_pattern, entry)
        if match:
            value = match.group(1)
            print(f"  {field}: {value[:50]}..." if len(value) > 50 else f"  {field}: {value}")
        else:
            print(f"  {field}: KHÔNG TÌM THẤY hoặc format sai")
    
    # Kiểm tra xem TEN có bị thiếu dấu ngoặc kép đóng không
    ten_pattern = r'"TEN"\s*:\s*"([^"]*)'
    ten_match = re.search(ten_pattern, entry)
    
    if ten_match:
        ten_value = ten_match.group(1)
        print(f"\nGiá trị TEN (có thể không đầy đủ): {ten_value}")
        
        # Tìm xem TEN kết thúc ở đâu trong entry
        ten_start = ten_match.start(1)
        ten_str_start = ten_match.start(0)
        
        # Tìm từ vị trí bắt đầu của TEN trong entry
        entry_pos = ten_str_start + len('"TEN":')
        
        # Tìm dấu ngoặc kép đóng
        quote_pos = -1
        for i in range(entry_pos, len(entry)):
            if entry[i] == '"':
                # Kiểm tra xem có bị escape không
                if i > 0 and entry[i-1] == '\\':
                    continue
                quote_pos = i
                break
        
        if quote_pos != -1:
            print(f"  Tìm thấy dấu ngoặc kép đóng tại vị trí {quote_pos} trong entry")
            print(f"  TEN đầy đủ: {entry[entry_pos:quote_pos+1]}")
        else:
            print(f"  KHÔNG TÌM THẤY dấu ngoặc kép đóng cho TEN!")
            
            # Tìm dấu phẩy hoặc dấu ngoặc nhọn đóng tiếp theo
            comma_pos = entry.find(',', entry_pos)
            brace_pos = entry.find('}', entry_pos)
            
            end_pos = min(comma_pos, brace_pos) if comma_pos != -1 and brace_pos != -1 else \
                     comma_pos if comma_pos != -1 else brace_pos
            
            if end_pos != -1:
                print(f"  Có thể kết thúc tại vị trí {end_pos} (ký tự: {entry[end_pos]})")
                print(f"  TEN không có dấu ngoặc kép đóng: {entry[entry_pos:end_pos]}")
                
                # Fix entry: thêm dấu ngoặc kép đóng trước dấu phẩy/dấu ngoặc nhọn
                fixed_entry = entry[:end_pos] + '"' + entry[end_pos:]
                print(f"\nEntry đã fix:")
                print("-" * 80)
                print(fixed_entry)
                print("-" * 80)
                
                # Thử parse entry đã fix
                try:
                    parsed = json.loads(fixed_entry)
                    print(f"\n✓ Entry đã fix parse thành công!")
                    print(f"  ID: {parsed.get('ID')}")
                    print(f"  TEN: {parsed.get('TEN')}")
                    
                    # Thay thế entry bị lỗi bằng entry đã fix trong json_str
                    fixed_json_str = json_str[:pos] + fixed_entry + json_str[entry_end+1:]
                    
                    # Test parse toàn bộ
                    print(f"\nThử parse toàn bộ JSON đã fix...")
                    try:
                        data = json.loads(fixed_json_str)
                        print(f"✓ Toàn bộ JSON đã fix parse thành công!")
                        print(f"  Tổng số entries: {len(data)}")
                        
                        # Lưu JSON đã fix
                        output_file = base_dir / "json" / "jsonData_fixed_final.js"
                        
                        # Tạo file mới với JSON đã fix
                        new_content = content.replace(json_str, fixed_json_str)
                        
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"\nĐã lưu file đã fix: {output_file}")
                        
                    except json.JSONDecodeError as e:
                        print(f"✗ Vẫn có lỗi parse toàn bộ JSON: {e}")
                        
                except json.JSONDecodeError as e:
                    print(f"✗ Không thể parse entry đã fix: {e}")

if __name__ == "__main__":
    main()
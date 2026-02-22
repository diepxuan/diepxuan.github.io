#!/usr/bin/env python3
"""
Fix JSON issue by adding missing quotes
"""

import re
from pathlib import Path

def fix_json_string(json_str):
    """Sửa lỗi JSON bằng cách thêm dấu ngoặc kép đóng bị thiếu"""
    
    # Pattern tìm các chuỗi bắt đầu với "TEN":"
    # và kết thúc không phải với dấu ngoặc kép trước khi gặp ","
    pattern = r'("TEN"\s*:\s*")([^"]*(?:\[[^\]]*\][^"]*)*)'
    
    def fix_ten_string(match):
        prefix = match.group(1)
        content = match.group(2)
        
        # Nếu content không kết thúc với dấu ngoặc kép
        # và tiếp theo là dấu phẩy hoặc dấu ngoặc nhọn đóng
        # thì thêm dấu ngoặc kép
        if not content.endswith('"'):
            # Tìm vị trí kết thúc thực sự
            # Tìm dấu phẩy tiếp theo không trong ngoặc
            pos = 0
            in_bracket = 0
            
            while pos < len(content):
                char = content[pos]
                
                if char == '[':
                    in_bracket += 1
                elif char == ']':
                    in_bracket -= 1
                elif char == ',' and in_bracket == 0:
                    # Đây là dấu phẩy kết thúc value
                    # Thêm dấu ngoặc kép trước dấu phẩy
                    fixed = content[:pos] + '"' + content[pos:]
                    return prefix + fixed
                
                pos += 1
            
            # Nếu không tìm thấy dấu phẩy, thêm dấu ngoặc kép ở cuối
            return prefix + content + '"'
        
        return match.group(0)
    
    # Áp dụng fix
    fixed_json = re.sub(pattern, fix_ten_string, json_str)
    
    # Thêm một fix đơn giản hơn: tìm các pattern "TEN":"... và thêm " nếu thiếu
    # Tìm tất cả các vị trí bắt đầu của "TEN":
    ten_positions = []
    pos = 0
    while True:
        pos = fixed_json.find('"TEN":', pos)
        if pos == -1:
            break
        ten_positions.append(pos)
        pos += 6
    
    # Duyệt ngược để không ảnh hưởng đến vị trí
    for pos in reversed(ten_positions):
        # Tìm dấu ngoặc kép mở
        quote_pos = fixed_json.find('"', pos + 6)
        if quote_pos == -1:
            continue
        
        # Tìm dấu ngoặc kép đóng
        next_quote = fixed_json.find('"', quote_pos + 1)
        
        # Nếu không tìm thấy dấu ngoặc kép đóng, tìm dấu phẩy hoặc dấu ngoặc nhọn đóng
        if next_quote == -1:
            comma_pos = fixed_json.find(',', quote_pos + 1)
            brace_pos = fixed_json.find('}', quote_pos + 1)
            
            end_pos = min(comma_pos, brace_pos) if comma_pos != -1 and brace_pos != -1 else \
                     comma_pos if comma_pos != -1 else brace_pos
            
            if end_pos != -1:
                # Chèn dấu ngoặc kép trước dấu phẩy/dấu ngoặc nhọn
                fixed_json = fixed_json[:end_pos] + '"' + fixed_json[end_pos:]
    
    return fixed_json

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
    print(f"JSON string length trước khi fix: {len(json_str):,} chars")
    
    # Fix JSON
    fixed_json = fix_json_string(json_str)
    print(f"JSON string length sau khi fix: {len(fixed_json):,} chars")
    
    # Kiểm tra xem có khác biệt không
    if json_str != fixed_json:
        print("Đã sửa JSON string")
        
        # Tìm vị trí đầu tiên khác biệt
        for i in range(min(len(json_str), len(fixed_json))):
            if json_str[i] != fixed_json[i]:
                print(f"Khác biệt đầu tiên tại vị trí {i}:")
                print(f"  Original: {repr(json_str[i-20:i+20])}")
                print(f"  Fixed:    {repr(fixed_json[i-20:i+20])}")
                break
        
        # Lưu JSON đã fix
        output_file = base_dir / "json" / "jsonData_fixed.js"
        
        # Tạo file mới với JSON đã fix
        new_content = content.replace(json_str, fixed_json)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"\nĐã lưu file đã fix: {output_file}")
        
        # Test parse
        import json
        try:
            data = json.loads(fixed_json)
            print(f"\n✓ Đã parse thành công! Tổng số entries: {len(data)}")
        except json.JSONDecodeError as e:
            print(f"\n✗ Vẫn có lỗi parse: {e}")
            print(f"  Error position: {e.pos}")
            
            # Hiển thị context
            start = max(0, e.pos - 100)
            end = min(len(fixed_json), e.pos + 100)
            print(f"  Context: {fixed_json[start:end]}")
    else:
        print("Không cần fix")

if __name__ == "__main__":
    main()
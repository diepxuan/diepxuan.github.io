#!/usr/bin/env python3
"""
Fix tất cả lỗi JSON trong file
"""

import re
import json
from pathlib import Path

def fix_json_string(json_str):
    """Fix tất cả lỗi JSON phổ biến"""
    
    print(f"Đang fix JSON string (độ dài: {len(json_str):,} chars)...")
    
    # Tạo bản copy để sửa
    fixed = json_str
    
    # Fix 1: Thêm dấu ngoặc kép đóng cho các trường TEN bị thiếu
    # Pattern: "TEN":"... [không có dấu ngoặc kép đóng] theo sau bởi , hoặc }
    ten_pattern = r'("TEN"\s*:\s*")([^"]+?)(?=\s*[,}])'
    
    def fix_ten_match(match):
        prefix = match.group(1)
        content = match.group(2)
        
        # Nếu content không kết thúc với dấu ngoặc kép
        if not content.endswith('"'):
            # Loại bỏ khoảng trắng ở cuối
            content = content.rstrip()
            return prefix + content + '"'
        
        return match.group(0)
    
    # Áp dụng fix
    fixed = re.sub(ten_pattern, fix_ten_match, fixed, flags=re.DOTALL)
    
    # Fix 2: Escape các ký tự đặc biệt trong chuỗi
    # Tìm tất cả các chuỗi và escape brackets
    def escape_string(match):
        content = match.group(1)
        # Escape backslashes trước
        content = content.replace('\\', '\\\\')
        # Escape quotes
        content = content.replace('"', '\\"')
        return '"' + content + '"'
    
    # Pattern cho chuỗi đã được bao bởi dấu ngoặc kép
    string_pattern = r'"([^"\\]*(?:\\.[^"\\]*)*)"'
    fixed = re.sub(string_pattern, escape_string, fixed)
    
    # Fix 3: Đảm bảo mỗi object có đủ 6 trường
    # Đếm số lượng objects và kiểm tra
    print("  Đang kiểm tra cấu trúc objects...")
    
    # Tìm tất cả các objects
    objects = []
    pos = 0
    
    while pos < len(fixed):
        if fixed[pos] == '{':
            obj_start = pos
            brace_count = 0
            in_string = False
            escape = False
            
            for i in range(pos, len(fixed)):
                char = fixed[i]
                
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
                            objects.append(fixed[obj_start:i+1])
                            pos = i + 1
                            break
            
            if brace_count != 0:
                print(f"  Object không đóng tại vị trí {pos}")
                break
        else:
            pos += 1
    
    print(f"  Tìm thấy {len(objects)} objects")
    
    # Kiểm tra object đầu tiên và object cuối cùng
    if objects:
        print(f"\n  Object đầu tiên (100 chars đầu):")
        print(f"    {objects[0][:100]}...")
        
        print(f"\n  Object cuối cùng (100 chars cuối):")
        print(f"    ...{objects[-1][-100:]}")
    
    return fixed

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    print(f"Đọc file: {json_file}")
    
    # Đọc file với BOM handling
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    print(f"File size: {len(content):,} bytes")
    
    # Tìm jdAllTree
    print("\nTìm jdAllTree...")
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    print(f"Đã tìm thấy jdAllTree, độ dài: {len(json_str):,} chars")
    
    # Fix JSON
    fixed_json = fix_json_string(json_str)
    
    # Kiểm tra xem có thay đổi không
    if json_str != fixed_json:
        print(f"\nĐã sửa JSON string")
        print(f"Độ dài trước: {len(json_str):,} chars")
        print(f"Độ dài sau:  {len(fixed_json):,} chars")
        
        # Tìm vị trí đầu tiên khác biệt
        for i in range(min(len(json_str), len(fixed_json))):
            if json_str[i] != fixed_json[i]:
                print(f"\nKhác biệt đầu tiên tại vị trí {i}:")
                print(f"  Original: ...{json_str[max(0,i-50):i+50]}...")
                print(f"  Fixed:    ...{fixed_json[max(0,i-50):i+50]}...")
                break
        
        # Test parse
        print(f"\nThử parse JSON đã fix...")
        try:
            data = json.loads(fixed_json)
            print(f"✓ Parse thành công!")
            print(f"  Tổng số entries: {len(data)}")
            
            # Kiểm tra entry đầu tiên và entry cuối cùng
            print(f"\n  Entry đầu tiên:")
            first = data[0]
            print(f"    ID: {first.get('ID')}")
            print(f"    TEN: {first.get('TEN')[:50]}..." if first.get('TEN') and len(first.get('TEN')) > 50 else f"    TEN: {first.get('TEN')}")
            
            print(f"\n  Entry cuối cùng:")
            last = data[-1]
            print(f"    ID: {last.get('ID')}")
            print(f"    TEN: {last.get('TEN')[:50]}..." if last.get('TEN') and len(last.get('TEN')) > 50 else f"    TEN: {last.get('TEN')}")
            
            # Lưu file đã fix
            output_file = base_dir / "json" / "jsonData_fixed_complete.js"
            
            # Tạo file mới với JSON đã fix
            new_content = content.replace(json_str, fixed_json)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"\n✓ Đã lưu file đã fix: {output_file}")
            
            # Cũng lưu riêng JSON array để test
            json_output = base_dir / "json" / "jdAllTree_fixed.json"
            with open(json_output, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"✓ Đã lưu JSON array: {json_output}")
            
        except json.JSONDecodeError as e:
            print(f"✗ Parse thất bại: {e}")
            print(f"  Error position: {e.pos}")
            
            # Hiển thị context xung quanh lỗi
            start = max(0, e.pos - 100)
            end = min(len(fixed_json), e.pos + 100)
            print(f"  Context: {fixed_json[start:end]}")
    else:
        print(f"\nKhông cần fix")

if __name__ == "__main__":
    main()
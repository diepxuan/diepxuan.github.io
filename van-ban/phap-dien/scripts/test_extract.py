#!/usr/bin/env python3
"""
Test extract JSON từ file JavaScript
"""

import json
import re
import os
from pathlib import Path

def extract_json_section(file_path, section_name):
    """Trích xuất một section JSON từ file JS"""
    print(f"Trích xuất {section_name}...")
    
    # Đọc toàn bộ file
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f"File size: {len(content):,} bytes")
    
    # Tìm section
    pattern = rf'var {section_name} = (\[.*?\]);'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print(f"  ✗ Không tìm thấy {section_name}")
        return None
    
    print(f"  ✓ Tìm thấy {section_name}")
    json_str = match.group(1)
    
    # Kiểm tra độ dài
    print(f"  JSON string length: {len(json_str):,} chars")
    
    # Lấy 500 ký tự đầu và cuối để kiểm tra
    print(f"  First 500 chars: {json_str[:500]}")
    print(f"  Last 500 chars: {json_str[-500:]}")
    
    return json_str

def fix_json(json_str):
    """Sửa lỗi JSON"""
    # Xóa các ký tự control
    json_str = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_str)
    # Đảm bảo dấu ngoặc kép
    json_str = re.sub(r"'(.*?)'", r'"\1"', json_str)
    return json_str

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    if not json_file.exists():
        print(f"File không tồn tại: {json_file}")
        return
    
    # Test extract jdChuDe
    json_str = extract_json_section(json_file, 'jdChuDe')
    
    if json_str:
        # Sửa JSON
        json_str = fix_json(json_str)
        
        try:
            data = json.loads(json_str)
            print(f"  ✓ Đã load {len(data)} entries")
            print(f"  Sample entry: {data[0]}")
        except json.JSONDecodeError as e:
            print(f"  ✗ Lỗi decode: {e}")
            print(f"  Error position: {e.pos}")
            print(f"  Context: {json_str[e.pos-50:e.pos+50]}")
    
    print("\n" + "="*60 + "\n")
    
    # Test extract jdDeMuc
    json_str = extract_json_section(json_file, 'jdDeMuc')
    
    if json_str:
        json_str = fix_json(json_str)
        
        try:
            data = json.loads(json_str)
            print(f"  ✓ Đã load {len(data)} entries")
            print(f"  Sample entry: {data[0]}")
        except json.JSONDecodeError as e:
            print(f"  ✗ Lỗi decode: {e}")
            print(f"  Error position: {e.pos}")
    
    print("\n" + "="*60 + "\n")
    
    # Test extract jdAllTree (chỉ lấy phần đầu)
    print("Trích xuất jdAllTree (chỉ lấy phần đầu)...")
    with open(json_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Tìm vị trí bắt đầu của jdAllTree
    start_pattern = r'var jdAllTree = \['
    start_match = re.search(start_pattern, content)
    
    if start_match:
        start_pos = start_match.start()
        print(f"  Tìm thấy jdAllTree tại vị trí: {start_pos}")
        
        # Tìm vị trí kết thúc (];)
        # Chỉ lấy 10000 ký tự đầu để test
        test_content = content[start_pos:start_pos + 10000]
        print(f"  Test content (first 10000 chars):")
        print(test_content[:500] + "...")
        
        # Tìm closing bracket
        bracket_count = 0
        in_string = False
        escape = False
        
        for i, char in enumerate(test_content):
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
                if char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        print(f"  Tìm thấy closing bracket tại vị trí: {i}")
                        json_str = test_content[:i+1]
                        # Loại bỏ "var jdAllTree = "
                        json_str = json_str.replace('var jdAllTree = ', '', 1)
                        print(f"  JSON string length: {len(json_str):,} chars")
                        
                        # Parse thử
                        try:
                            json_str = fix_json(json_str)
                            data = json.loads(json_str)
                            print(f"  ✓ Đã load {len(data)} entries (test)")
                            print(f"  Sample entry: {data[0]}")
                        except json.JSONDecodeError as e:
                            print(f"  ✗ Lỗi decode: {e}")
                        
                        break

if __name__ == "__main__":
    main()
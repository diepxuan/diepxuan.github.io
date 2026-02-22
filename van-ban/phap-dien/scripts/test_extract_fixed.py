#!/usr/bin/env python3
"""
Test extract JSON từ file JavaScript với BOM handling
"""

import json
import re
import os
from pathlib import Path

def extract_json_section(file_path, section_name):
    """Trích xuất một section JSON từ file JS"""
    print(f"Trích xuất {section_name}...")
    
    # Đọc toàn bộ file với BOM handling
    with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    print(f"File size (after BOM removal): {len(content):,} bytes")
    
    # Tìm section
    pattern = rf'var {section_name}\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # Thử tìm không có dấu chấm phẩy
        pattern = rf'var {section_name}\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print(f"  ✗ Không tìm thấy {section_name}")
        return None
    
    print(f"  ✓ Tìm thấy {section_name}")
    json_str = match.group(1)
    
    # Kiểm tra độ dài
    print(f"  JSON string length: {len(json_str):,} chars")
    
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
            if e.pos > 100:
                print(f"  Context: {json_str[e.pos-100:e.pos+100]}")
    
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
    
    # Test extract jdAllTree (chỉ lấy 5 entries đầu để test)
    print("Trích xuất jdAllTree (chỉ test 5 entries đầu)...")
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    # Tìm vị trí bắt đầu của jdAllTree
    start_pattern = r'var jdAllTree\s*=\s*\['
    start_match = re.search(start_pattern, content)
    
    if start_match:
        start_pos = start_match.start()
        print(f"  Tìm thấy jdAllTree tại vị trí: {start_pos}")
        
        # Tìm vị trí kết thúc của 5 entries đầu
        # Đếm số lượng dấu ngoặc nhọn đóng
        test_content = content[start_pos:start_pos + 5000]  # Lấy 5000 ký tự đầu
        print(f"  Test content (first 200 chars):")
        print(test_content[:200] + "...")
        
        # Tìm 5 entries đầu
        entries = []
        pos = test_content.find('{')
        count = 0
        
        while pos != -1 and count < 5:
            # Tìm closing brace tương ứng
            brace_count = 0
            in_string = False
            escape = False
            
            for i in range(pos, len(test_content)):
                char = test_content[i]
                
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
                            entry_str = test_content[pos:i+1]
                            entries.append(entry_str)
                            count += 1
                            pos = test_content.find('{', i+1)
                            break
            
            if brace_count != 0:
                break
        
        if entries:
            test_json_str = '[' + ','.join(entries) + ']'
            print(f"  Created test JSON with {len(entries)} entries")
            
            try:
                json_str = fix_json(test_json_str)
                data = json.loads(json_str)
                print(f"  ✓ Đã load {len(data)} entries (test)")
                print(f"  Sample entry: {data[0]}")
            except json.JSONDecodeError as e:
                print(f"  ✗ Lỗi decode: {e}")

if __name__ == "__main__":
    main()
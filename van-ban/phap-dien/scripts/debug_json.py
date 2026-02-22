#!/usr/bin/env python3
"""
Debug JSON parsing issue
"""

import json
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
    print(f"JSON string length: {len(json_str):,} chars")
    
    # Tìm vị trí lỗi (5568466)
    error_pos = 5568466
    print(f"\nKiểm tra vị trí lỗi: {error_pos}")
    
    if error_pos < len(json_str):
        # Lấy context xung quanh vị trí lỗi
        start = max(0, error_pos - 200)
        end = min(len(json_str), error_pos + 200)
        context = json_str[start:end]
        
        print(f"\nContext around error position:")
        print("-" * 80)
        print(context)
        print("-" * 80)
        
        # Hiển thị các ký tự xung quanh
        print(f"\nCharacters at position {error_pos-10} to {error_pos+10}:")
        print(repr(json_str[error_pos-10:error_pos+10]))
        
        # Kiểm tra xem có ký tự đặc biệt nào không
        print(f"\nKiểm tra ký tự đặc biệt:")
        for i in range(error_pos-5, error_pos+6):
            if i < len(json_str):
                char = json_str[i]
                if ord(char) < 32 or ord(char) > 126:
                    print(f"  Position {i}: {repr(char)} (ord={ord(char)})")
    
    # Thử parse với json.JSONDecoder để bắt lỗi chi tiết
    print(f"\nThử parse với json.JSONDecoder...")
    
    decoder = json.JSONDecoder()
    pos = 0
    
    try:
        # Parse mảng
        if json_str[pos] == '[':
            pos += 1
            
            # Parse từng entry
            entry_count = 0
            while pos < len(json_str) and json_str[pos] != ']':
                # Bỏ qua whitespace
                while pos < len(json_str) and json_str[pos].isspace():
                    pos += 1
                
                if json_str[pos] == ']':
                    break
                
                # Parse một object
                try:
                    obj, new_pos = decoder.raw_decode(json_str, idx=pos)
                    pos = new_pos
                    entry_count += 1
                    
                    if entry_count % 10000 == 0:
                        print(f"  Đã parse {entry_count} entries, position: {pos}")
                    
                    # Bỏ qua dấu phẩy
                    while pos < len(json_str) and json_str[pos].isspace():
                        pos += 1
                    if pos < len(json_str) and json_str[pos] == ',':
                        pos += 1
                        
                except json.JSONDecodeError as e:
                    print(f"\nLỗi tại entry {entry_count + 1}, position {pos}:")
                    print(f"  Error: {e}")
                    
                    # Hiển thị context
                    start = max(0, pos - 100)
                    end = min(len(json_str), pos + 100)
                    print(f"  Context: {json_str[start:end]}")
                    break
                    
        print(f"\nTổng số entries đã parse: {entry_count}")
        
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Parse large JavaScript file chứa JSON data
"""

import json
import re
import sys

def parse_large_js(file_path):
    """Parse file JavaScript lớn bằng cách đọc từng phần"""
    print(f"Đang parse file: {file_path}")
    
    data = {}
    
    # Đọc file theo từng phần
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read(1000000)  # Đọc 1MB đầu tiên để tìm biến
        
        # Tìm vị trí bắt đầu của các biến
        jdChuDe_start = content.find('var jdChuDe = [')
        jdDeMuc_start = content.find('var jdDeMuc = [')
        jdAllTree_start = content.find('var jdAllTree = [')
        
        print(f"  jdChuDe bắt đầu tại: {jdChuDe_start}")
        print(f"  jdDeMuc bắt đầu tại: {jdDeMuc_start}")
        print(f"  jdAllTree bắt đầu tại: {jdAllTree_start}")
    
    # Parse jdChuDe
    if jdChuDe_start != -1:
        print("  Đang parse jdChuDe...")
        data['jdChuDe'] = parse_json_array(file_path, jdChuDe_start)
        print(f"  ✓ jdChuDe: {len(data['jdChuDe'])} records")
    
    # Parse jdDeMuc
    if jdDeMuc_start != -1:
        print("  Đang parse jdDeMuc...")
        data['jdDeMuc'] = parse_json_array(file_path, jdDeMuc_start)
        print(f"  ✓ jdDeMuc: {len(data['jdDeMuc'])} records")
    
    # Parse jdAllTree
    if jdAllTree_start != -1:
        print("  Đang parse jdAllTree...")
        data['jdAllTree'] = parse_json_array(file_path, jdAllTree_start)
        print(f"  ✓ jdAllTree: {len(data['jdAllTree'])} records")
    
    return data

def parse_json_array(file_path, start_pos):
    """Parse một JSON array từ vị trí bắt đầu"""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        f.seek(start_pos)
        
        # Tìm vị trí bắt đầu của array '['
        while True:
            char = f.read(1)
            if char == '[':
                break
            elif not char:
                return []
        
        # Đọc cho đến khi tìm thấy ']' tương ứng
        json_str = '['
        bracket_count = 1
        buffer_size = 100000  # 100KB buffer
        
        while bracket_count > 0:
            chunk = f.read(buffer_size)
            if not chunk:
                break
            
            for char in chunk:
                json_str += char
                if char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        break
            
            if bracket_count == 0:
                break
        
        # Parse JSON
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"  ✗ Lỗi parse JSON: {e}")
            # Thử fix trailing comma
            json_str = json_str.rstrip()
            if json_str.endswith(','):
                json_str = json_str[:-1] + ']'
            try:
                return json.loads(json_str)
            except:
                print(f"  ✗ Không thể parse JSON array")
                return []

if __name__ == "__main__":
    file_path = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'
    data = parse_large_js(file_path)
    
    print(f"\n=== KẾT QUẢ ===")
    print(f"jdChuDe: {len(data.get('jdChuDe', []))} records")
    print(f"jdDeMuc: {len(data.get('jdDeMuc', []))} records")
    print(f"jdAllTree: {len(data.get('jdAllTree', []))} records")
    
    # Sample data
    if data.get('jdChuDe'):
        print(f"\nSample jdChuDe: {data['jdChuDe'][0]}")
    if data.get('jdDeMuc'):
        print(f"Sample jdDeMuc: {data['jdDeMuc'][0]}")
    if data.get('jdAllTree'):
        print(f"Sample jdAllTree: {data['jdAllTree'][0]}")
#!/usr/bin/env python3
import json
import re

file_path = '/root/.openclaw/workspace/projects/github-io/van-ban/crawled/BoPhapDienDienTu/jsonData.js'
print(f'Đang đọc file: {file_path}')

with open(file_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Tìm jdAllTree bằng regex
pattern = r'var jdAllTree\s*=\s*(\[.*?\]);'
match = re.search(pattern, content, re.DOTALL)

if match:
    print('✓ Đã tìm thấy jdAllTree')
    json_str = match.group(1)
    
    # Clean JSON string - remove trailing commas
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    
    # Parse thử
    try:
        data = json.loads(json_str)
        print(f'✓ Đã parse thành công: {len(data)} records')
        
        # Kiểm tra 5 records đầu
        print('\n=== 5 RECORDS ĐẦU TIÊN ===')
        for i in range(min(5, len(data))):
            item = data[i]
            print(f'\nRecord {i}:')
            print(f'  ID: {item.get("ID")}')
            print(f'  MAPC: {item.get("MAPC")} (len={len(item.get("MAPC", ""))})')
            print(f'  TEN: {item.get("TEN", "")[:50]}...')
            print(f'  ChuDeID: {item.get("ChuDeID")}')
            print(f'  DeMucID: {item.get("DeMucID")}')
        
        # Tìm MAPC dài nhất trong 1000 records đầu
        max_len = 0
        max_mapc = ''
        for i in range(min(1000, len(data))):
            mapc = data[i].get('MAPC', '')
            if len(mapc) > max_len:
                max_len = len(mapc)
                max_mapc = mapc
        
        print(f'\n=== THỐNG KÊ ===')
        print(f'MAPC dài nhất (trong 1000 records đầu): {max_len} chars')
        print(f'MAPC đó: {max_mapc}')
        
    except json.JSONDecodeError as e:
        print(f'✗ Lỗi parse JSON: {e}')
        print(f'Vị trí lỗi: {e.pos}')
        print(f'Dòng lỗi: {e.lineno}, cột: {e.colno}')
        
        # Hiển thị context xung quanh lỗi
        start = max(0, e.pos - 100)
        end = min(len(json_str), e.pos + 100)
        print(f'Context: ...{json_str[start:end]}...')
else:
    print('✗ Không tìm thấy jdAllTree')
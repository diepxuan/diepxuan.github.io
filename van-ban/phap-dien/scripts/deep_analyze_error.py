#!/usr/bin/env python3
"""
Phân tích sâu lỗi JSON
"""

import re
import json
from pathlib import Path

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    print(f"Đang phân tích: {json_file}")
    
    # Đọc file
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    # Tìm jdAllTree
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("✗ Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    print(f"Độ dài jdAllTree: {len(json_str):,} chars")
    
    # Thử parse từng phần
    print("\nThử parse từng phần để tìm lỗi...")
    
    # Phương pháp: chia nhỏ và parse
    chunk_size = 1000000  # 1MB chunks
    chunks = []
    
    for i in range(0, len(json_str), chunk_size):
        chunk = json_str[i:i+chunk_size]
        chunks.append((i, chunk))
    
    print(f"Chia thành {len(chunks)} chunks")
    
    # Tìm chunk có lỗi
    error_chunk_idx = -1
    for idx, (start_pos, chunk) in enumerate(chunks):
        # Thử parse chunk này (thêm [ và ] để thành JSON array)
        test_str = '[' + chunk + ']'
        try:
            json.loads(test_str)
            # print(f"  Chunk {idx} (pos {start_pos:,}): OK")
        except json.JSONDecodeError as e:
            print(f"  ⚠ Chunk {idx} (pos {start_pos:,}): LỖI - {e}")
            error_chunk_idx = idx
            break
    
    if error_chunk_idx == -1:
        print("Không tìm thấy chunk có lỗi, thử parse toàn bộ...")
        try:
            data = json.loads(json_str)
            print(f"✓ Parse toàn bộ thành công! {len(data):,} entries")
            return
        except json.JSONDecodeError as e:
            print(f"✗ Parse toàn bộ thất bại: {e}")
            error_pos = e.pos
            print(f"  Error position: {error_pos:,}")
            error_chunk_idx = error_pos // chunk_size
    
    if error_chunk_idx >= 0:
        print(f"\nPhân tích chunk {error_chunk_idx} có lỗi...")
        start_pos, chunk = chunks[error_chunk_idx]
        
        # Tìm vị trí lỗi cụ thể trong chunk
        # Thử parse từng dòng
        lines = chunk.split('\n')
        print(f"Chunk có {len(lines)} lines")
        
        # Tìm line có vấn đề
        for line_idx, line in enumerate(lines[:100]):  # Check first 100 lines
            if not line.strip():
                continue
            
            # Thử parse line như JSON object
            if line.strip().startswith('{'):
                try:
                    json.loads(line.strip().rstrip(','))
                except json.JSONDecodeError as e:
                    print(f"\n⚠ Line {line_idx} có lỗi:")
                    print(f"  Line: {line[:200]}...")
                    print(f"  Error: {e}")
                    
                    # Phân tích cụ thể
                    if 'Unterminated string' in str(e):
                        print("  → Lỗi: String không đóng")
                        # Tìm vị trí của "
                        quote_pos = line.find('"TEN":"')
                        if quote_pos != -1:
                            ten_start = quote_pos + 7
                            # Tìm dấu " đóng
                            closing_quote = line.find('"', ten_start)
                            if closing_quote == -1:
                                print(f"  → TEN không có dấu đóng: {line[ten_start:ten_start+100]}...")
                    
                    break
        
        # Hiển thị context xung quanh error position
        if error_chunk_idx < len(chunks) - 1:
            # Lấy thêm chunk tiếp theo để xem context
            next_start, next_chunk = chunks[error_chunk_idx + 1]
            combined_chunk = chunk + next_chunk[:5000]  # Thêm 5k chars từ chunk tiếp theo
            
            # Tìm các entry trong combined chunk
            entries = re.findall(r'\{[^}]*\}', combined_chunk[:10000])
            print(f"\nTìm thấy {len(entries)} entries trong 10k chars đầu")
            
            for i, entry in enumerate(entries[:5]):
                print(f"\nEntry {i}:")
                print(f"  Length: {len(entry)} chars")
                print(f"  Preview: {entry[:200]}...")
                
                try:
                    parsed = json.loads(entry)
                    print(f"  ✓ Parse OK")
                except json.JSONDecodeError as e:
                    print(f"  ✗ Parse error: {e}")
                    
                    # Hiển thị chi tiết
                    lines = entry.split('\n')
                    for line in lines:
                        if 'TEN' in line:
                            print(f"    TEN line: {line}")
    
    # Phương pháp brute force: tìm tất cả các entry và thử parse
    print("\n\nPhương pháp brute force: tìm và parse từng entry...")
    
    # Tìm tất cả các objects
    objects = []
    pos = 0
    
    while pos < len(json_str):
        if json_str[pos] == '{':
            # Tìm } tương ứng
            brace_count = 0
            in_string = False
            escape = False
            end_pos = -1
            
            for i in range(pos, min(pos + 5000, len(json_str))):  # Giới hạn 5000 chars mỗi object
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
                            end_pos = i
                            break
            
            if end_pos != -1:
                obj_str = json_str[pos:end_pos+1]
                objects.append((pos, obj_str))
                pos = end_pos + 1
            else:
                pos += 1
        else:
            pos += 1
        
        if len(objects) >= 20000:  # Giới hạn để không quá lâu
            break
    
    print(f"Tìm thấy {len(objects)} objects")
    
    # Parse từng object
    error_objects = []
    for obj_idx, (obj_pos, obj_str) in enumerate(objects[:500]):  # Check first 500
        try:
            json.loads(obj_str)
        except json.JSONDecodeError as e:
            error_objects.append((obj_idx, obj_pos, obj_str, str(e)))
    
    print(f"\nTìm thấy {len(error_objects)} objects bị lỗi")
    
    for obj_idx, obj_pos, obj_str, error_msg in error_objects[:5]:  # Hiển thị 5 lỗi đầu
        print(f"\n⚠ Object {obj_idx} tại vị trí {obj_pos:,}:")
        print(f"  Error: {error_msg}")
        print(f"  Preview: {obj_str[:300]}...")
        
        # Tìm TEN field
        ten_match = re.search(r'"TEN":"([^"]*)', obj_str)
        if ten_match:
            print(f"  TEN (partial): {ten_match.group(1)[:100]}...")

if __name__ == "__main__":
    main()
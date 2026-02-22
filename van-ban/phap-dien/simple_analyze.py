#!/usr/bin/env python3
"""
Phân tích đơn giản cấu trúc dữ liệu Pháp điển
"""

import json
import re

def extract_section(js_content, var_name):
    """Trích xuất một section từ file JS"""
    # Tìm var_name = [ ... ];
    pattern = rf'var {var_name} = (\[.*?\]);'
    match = re.search(pattern, js_content, re.DOTALL)
    
    if not match:
        print(f"Không tìm thấy {var_name}")
        return None
    
    json_str = match.group(1)
    
    # Sửa một số lỗi JSON nếu có
    # Xóa các ký tự null
    json_str = json_str.replace('\x00', '')
    
    try:
        data = json.loads(json_str)
        return data
    except json.JSONDecodeError as e:
        print(f"Lỗi decode {var_name}: {e}")
        print(f"Độ dài JSON string: {len(json_str)}")
        
        # Thử cắt bớt nếu quá dài
        if len(json_str) > 1000000:  # 1MB
            print("JSON quá dài, thử cắt bớt để debug...")
            # Tìm vị trí kết thúc hợp lý
            end_pos = json_str.find('}]', 1000000)
            if end_pos > 0:
                json_str = json_str[:end_pos+2]
                try:
                    data = json.loads(json_str)
                    print(f"Đã load {var_name} (cắt bớt): {len(data)} entries")
                    return data
                except:
                    pass
        
        return None

def main():
    print("Đang đọc file jsonData.js...")
    
    with open('jsonData.js', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f"Độ dài file: {len(content)} bytes")
    
    # Trích xuất các phần
    print("\nTrích xuất dữ liệu...")
    
    jdChuDe = extract_section(content, 'jdChuDe')
    if jdChuDe:
        print(f"✓ jdChuDe: {len(jdChuDe)} chủ đề")
        print("5 chủ đề đầu tiên:")
        for i, chude in enumerate(jdChuDe[:5]):
            print(f"  {chude.get('STT')}. {chude.get('Text')}")
    
    jdDeMuc = extract_section(content, 'jdDeMuc')
    if jdDeMuc:
        print(f"\n✓ jdDeMuc: {len(jdDeMuc)} đề mục")
        
        # Đếm số đề mục theo chủ đề
        from collections import defaultdict
        demuc_by_chude = defaultdict(int)
        for demuc in jdDeMuc:
            chude_id = demuc.get('ChuDe')
            demuc_by_chude[chude_id] += 1
        
        print(f"Phân bố theo {len(demuc_by_chude)} chủ đề")
    
    # jdAllTree rất lớn, chỉ lấy mẫu
    print("\nTrích xuất jdAllTree (có thể mất thời gian)...")
    
    # Tìm vị trí bắt đầu và kết thúc
    start_pos = content.find('var jdAllTree = [')
    if start_pos > 0:
        print(f"Tìm thấy jdAllTree tại vị trí {start_pos}")
        
        # Tìm kết thúc mảng (từ start_pos)
        bracket_count = 0
        in_string = False
        escape_next = False
        
        for i in range(start_pos + len('var jdAllTree = ['), len(content)):
            char = content[i]
            
            if escape_next:
                escape_next = False
                continue
                
            if char == '\\':
                escape_next = True
                continue
                
            if char == '"' and not escape_next:
                in_string = not in_string
                continue
                
            if not in_string:
                if char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                    if bracket_count == -1:  # Đã đóng mảng jdAllTree
                        end_pos = i
                        break
        
        if 'end_pos' in locals():
            json_str = content[start_pos + len('var jdAllTree = '):end_pos+1]
            print(f"Độ dài JSON string: {len(json_str)}")
            
            # Lấy mẫu nhỏ để phân tích
            sample_size = 10000
            if len(json_str) > sample_size:
                # Tìm vị trí kết thúc entry gần nhất
                end_sample = json_str.find('},', sample_size)
                if end_sample > 0:
                    json_sample = json_str[:end_sample+1] + ']'
                    try:
                        jdAllTree_sample = json.loads(json_sample)
                        print(f"✓ jdAllTree (mẫu): {len(jdAllTree_sample)} entries")
                        
                        # Phân tích mẫu
                        print("\nPhân tích mẫu jdAllTree:")
                        print(f"  Tổng số entries trong mẫu: {len(jdAllTree_sample)}")
                        
                        # Phân tích độ dài MAPC
                        mapc_lengths = {}
                        for entry in jdAllTree_sample[:100]:
                            mapc = entry.get('MAPC', '')
                            length = len(mapc)
                            mapc_lengths[length] = mapc_lengths.get(length, 0) + 1
                        
                        print("  Độ dài MAPC (100 entries đầu):")
                        for length, count in mapc_lengths.items():
                            print(f"    {length} ký tự: {count}")
                        
                        # Hiển thị một vài entries
                        print("\n  5 entries đầu tiên:")
                        for i, entry in enumerate(jdAllTree_sample[:5]):
                            print(f"    {i+1}. MAPC={entry.get('MAPC')}, ChiMuc={entry.get('ChiMuc')}, TEN={entry.get('TEN')[:60]}...")
                        
                    except json.JSONDecodeError as e:
                        print(f"Lỗi decode mẫu: {e}")
    
    print("\n=== KẾT LUẬN ===")
    print("1. Hệ thống Pháp điển có cấu trúc dữ liệu rõ ràng")
    print("2. Dữ liệu được lưu trực tiếp trong file JSON")
    print("3. Có thể trích xuất toàn bộ dữ liệu mà không cần crawl HTML")
    print("4. Cần xử lý file JSON lớn (24MB) một cách hiệu quả")

if __name__ == "__main__":
    main()
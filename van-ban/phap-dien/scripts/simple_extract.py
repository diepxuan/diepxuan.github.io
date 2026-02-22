#!/usr/bin/env python3
"""
Trích xuất đơn giản dữ liệu Pháp điển
"""

import json
import re
import os

def main():
    print("=== TRÍCH XUẤT DỮ LIỆU PHÁP ĐIỂN ===\n")
    
    # Đọc file
    js_file = "jsonData.js"
    print(f"Đang đọc file {js_file}...")
    
    with open(js_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f"Độ dài file: {len(content):,} bytes\n")
    
    # Tìm các section
    print("Tìm các section dữ liệu...")
    
    # Tìm jdChuDe
    chu_de_match = re.search(r'var jdChuDe = (\[.*?\]);', content, re.DOTALL)
    if chu_de_match:
        print("✓ Tìm thấy jdChuDe")
        json_str = chu_de_match.group(1)
        # Cắt bớt nếu quá dài
        if len(json_str) > 10000:
            json_str = json_str[:10000] + ']'
        
        try:
            chude_data = json.loads(json_str)
            print(f"  Số chủ đề: {len(chude_data)}")
            print("  5 chủ đề đầu tiên:")
            for i, chude in enumerate(chude_data[:5]):
                print(f"    {chude.get('STT')}. {chude.get('Text')}")
        except:
            print("  Không thể parse JSON")
    else:
        print("✗ Không tìm thấy jdChuDe")
    
    print()
    
    # Tìm jdDeMuc
    de_muc_match = re.search(r'var jdDeMuc = (\[.*?\]);', content, re.DOTALL)
    if de_muc_match:
        print("✓ Tìm thấy jdDeMuc")
        json_str = de_muc_match.group(1)
        # Cắt bớt
        if len(json_str) > 20000:
            json_str = json_str[:20000] + ']'
        
        try:
            demuc_data = json.loads(json_str)
            print(f"  Số đề mục (mẫu): {len(demuc_data)}")
        except:
            print("  Không thể parse JSON")
    else:
        print("✗ Không tìm thấy jdDeMuc")
    
    print()
    
    # Tìm jdAllTree - rất lớn, chỉ lấy mẫu
    print("Tìm jdAllTree (rất lớn, chỉ lấy mẫu nhỏ)...")
    
    # Tìm vị trí bắt đầu
    start_pos = content.find('var jdAllTree = [')
    if start_pos > 0:
        print(f"✓ Tìm thấy jdAllTree tại vị trí {start_pos}")
        
        # Lấy 50000 ký tự đầu tiên của mảng
        sample_size = 50000
        sample_content = content[start_pos:start_pos + sample_size]
        
        # Tìm vị trí kết thúc trong mẫu
        end_pos = sample_content.rfind('}]')
        if end_pos > 0:
            json_str = sample_content[sample_content.find('['):end_pos+2]
            
            try:
                alltree_sample = json.loads(json_str)
                print(f"  Số entries (mẫu): {len(alltree_sample)}")
                
                print("\n  10 entries đầu tiên:")
                for i, entry in enumerate(alltree_sample[:10]):
                    mapc = entry.get('MAPC', '')
                    chimuc = entry.get('ChiMuc', '')
                    ten = entry.get('TEN', '')[:60]
                    print(f"    {i+1:2d}. MAPC={mapc[:20]}..., ChiMuc={chimuc}, TEN={ten}...")
                
                # Phân tích MAPC
                print("\n  Phân tích độ dài MAPC:")
                mapc_lengths = {}
                for entry in alltree_sample[:100]:
                    mapc = entry.get('MAPC', '')
                    length = len(mapc)
                    mapc_lengths[length] = mapc_lengths.get(length, 0) + 1
                
                for length, count in sorted(mapc_lengths.items()):
                    print(f"    {length} ký tự: {count}")
                    
            except json.JSONDecodeError as e:
                print(f"  Lỗi parse JSON: {e}")
    else:
        print("✗ Không tìm thấy jdAllTree")
    
    print("\n=== KẾT LUẬN ===")
    print("1. Dữ liệu Pháp điển có cấu trúc JSON rõ ràng")
    print("2. File rất lớn (23MB) cần xử lý đặc biệt")
    print("3. Có thể trích xuất toàn bộ dữ liệu với phương pháp phù hợp")
    print("4. Cần viết crawler chuyên dụng xử lý file lớn")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Phân tích cấu trúc dữ liệu Pháp điển Điện tử
"""

import json
import re
import os
from collections import defaultdict

def extract_json_from_js(js_file_path):
    """Trích xuất JSON từ file .js"""
    print(f"Đang đọc file: {js_file_path}")
    
    with open(js_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm và trích xuất các mảng JSON
    patterns = [
        (r'var jdChuDe = (\[.*?\]);', 'jdChuDe'),
        (r'var jdDeMuc = (\[.*?\]);', 'jdDeMuc'),
        (r'var jdAllTree = (\[.*?\]);', 'jdAllTree')
    ]
    
    data = {}
    
    for pattern, key in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                data[key] = json.loads(json_str)
                print(f"  ✓ Đã load {key}: {len(data[key])} entries")
            except json.JSONDecodeError as e:
                print(f"  ✗ Lỗi decode {key}: {e}")
                # Thử sửa lỗi JSON nếu có
                json_str = fix_json(json_str)
                try:
                    data[key] = json.loads(json_str)
                    print(f"  ✓ Đã load {key} (sau khi sửa): {len(data[key])} entries")
                except:
                    print(f"  ✗ Không thể load {key}")
        else:
            print(f"  ✗ Không tìm thấy {key}")
    
    return data

def fix_json(json_str):
    """Sửa một số lỗi JSON phổ biến"""
    # Xóa các ký tự không hợp lệ
    json_str = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_str)
    # Đảm bảo dấu ngoặc kép đúng
    json_str = re.sub(r"'(.*?)'", r'"\1"', json_str)
    return json_str

def analyze_mapc_structure(entries):
    """Phân tích cấu trúc mã MAPC"""
    print("\n=== PHÂN TÍCH CẤU TRÚC MAPC ===")
    
    # Phân nhóm theo độ dài MAPC
    length_groups = defaultdict(int)
    for entry in entries[:1000]:  # Chỉ phân tích 1000 entries đầu
        mapc = entry.get('MAPC', '')
        length_groups[len(mapc)] += 1
    
    print("Phân bố độ dài MAPC (1000 entries đầu):")
    for length, count in sorted(length_groups.items()):
        print(f"  Độ dài {length}: {count} entries")
    
    # Phân tích mẫu MAPC
    print("\nMẫu MAPC (10 entries đầu):")
    for i, entry in enumerate(entries[:10]):
        mapc = entry.get('MAPC', '')
        chimuc = entry.get('ChiMuc', '')
        ten = entry.get('TEN', '')[:50]
        print(f"  {i+1}. MAPC={mapc}, ChiMuc={chimuc}, TEN={ten}...")
    
    # Phân tích cấu trúc phân cấp
    print("\nPhân tích phân cấp từ ChiMuc:")
    chimuc_types = defaultdict(int)
    for entry in entries[:500]:
        chimuc = entry.get('ChiMuc', '')
        if chimuc:
            # Phân loại ChiMuc
            if chimuc.isdigit():
                chimuc_types['số'] += 1
            elif len(chimuc) == 1 and chimuc.isalpha():
                chimuc_types['chữ cái'] += 1
            elif chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']:
                chimuc_types['số la mã'] += 1
            else:
                chimuc_types['khác'] += 1
    
    print("Phân loại ChiMuc (500 entries đầu):")
    for chimuc_type, count in chimuc_types.items():
        print(f"  {chimuc_type}: {count}")

def build_hierarchy(entries):
    """Xây dựng cấu trúc phân cấp từ MAPC"""
    print("\n=== XÂY DỰNG CẤU TRÚC PHÂN CẤP ===")
    
    # Sắp xếp theo MAPC
    sorted_entries = sorted(entries, key=lambda x: x.get('MAPC', ''))
    
    # Phân tích cấp độ dựa trên MAPC
    # Giả định: MAPC có độ dài 20 ký tự, có thể phân cấp theo từng đoạn
    hierarchy = defaultdict(list)
    
    for entry in sorted_entries[:100]:  # Chỉ phân tích 100 entries đầu
        mapc = entry.get('MAPC', '')
        if len(mapc) == 20:
            # Phân tích theo từng đoạn 4 ký tự
            level1 = mapc[0:4]  # 4 ký tự đầu
            level2 = mapc[4:8]  # 4 ký tự tiếp
            level3 = mapc[8:12] # 4 ký char tiếp
            level4 = mapc[12:16] # 4 ký tự tiếp
            level5 = mapc[16:20] # 4 ký tự cuối
            
            hierarchy[level1].append({
                'entry': entry,
                'level2': level2,
                'level3': level3,
                'level4': level4,
                'level5': level5
            })
    
    print(f"Phân cấp level1: {len(hierarchy)} nhóm")
    for level1, entries in list(hierarchy.items())[:5]:
        print(f"  Level1={level1}: {len(entries)} entries")
        # Hiển thị một vài entries
        for i, item in enumerate(entries[:3]):
            entry = item['entry']
            print(f"    - {entry.get('ChiMuc')}. {entry.get('TEN')[:40]}...")

def analyze_topics(data):
    """Phân tích chủ đề và đề mục"""
    print("\n=== PHÂN TÍCH CHỦ ĐỀ VÀ ĐỀ MỤC ===")
    
    if 'jdChuDe' in data:
        print(f"Tổng số chủ đề: {len(data['jdChuDe'])}")
        print("10 chủ đề đầu tiên:")
        for i, chude in enumerate(data['jdChuDe'][:10]):
            print(f"  {chude.get('STT')}. {chude.get('Text')}")
    
    if 'jdDeMuc' in data:
        print(f"\nTổng số đề mục: {len(data['jdDeMuc'])}")
        
        # Nhóm đề mục theo chủ đề
        demuc_by_chude = defaultdict(list)
        for demuc in data['jdDeMuc']:
            chude_id = demuc.get('ChuDe')
            demuc_by_chude[chude_id].append(demuc)
        
        print(f"Số đề mục phân bố theo {len(demuc_by_chude)} chủ đề:")
        for chude_id, demucs in list(demuc_by_chude.items())[:5]:
            # Tìm tên chủ đề
            chude_name = "Unknown"
            for chude in data.get('jdChuDe', []):
                if chude.get('Value') == chude_id:
                    chude_name = chude.get('Text')
                    break
            
            print(f"  {chude_name}: {len(demucs)} đề mục")
            # Hiển thị 3 đề mục đầu
            for demuc in demucs[:3]:
                print(f"    - {demuc.get('STT')}. {demuc.get('Text')}")

def main():
    """Hàm chính"""
    js_file = "jsonData.js"
    
    if not os.path.exists(js_file):
        print(f"Không tìm thấy file: {js_file}")
        return
    
    # Trích xuất dữ liệu JSON
    data = extract_json_from_js(js_file)
    
    if 'jdAllTree' in data:
        # Phân tích cấu trúc
        analyze_mapc_structure(data['jdAllTree'])
        build_hierarchy(data['jdAllTree'])
    
    # Phân tích chủ đề và đề mục
    analyze_topics(data)
    
    # Thống kê tổng quan
    print("\n=== THỐNG KÊ TỔNG QUAN ===")
    for key, value in data.items():
        if isinstance(value, list):
            print(f"{key}: {len(value)} entries")
    
    # Ghi dữ liệu mẫu ra file
    print("\n=== XUẤT DỮ LIỆU MẪU ===")
    if 'jdAllTree' in data:
        sample_data = data['jdAllTree'][:20]
        with open('sample_data.json', 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
        print("Đã xuất 20 entries mẫu ra file sample_data.json")
    
    if 'jdChuDe' in data:
        with open('chude_data.json', 'w', encoding='utf-8') as f:
            json.dump(data['jdChuDe'], f, ensure_ascii=False, indent=2)
        print("Đã xuất dữ liệu chủ đề ra file chude_data.json")
    
    if 'jdDeMuc' in data:
        with open('demuc_data.json', 'w', encoding='utf-8') as f:
            json.dump(data['jdDeMuc'][:50], f, ensure_ascii=False, indent=2)
        print("Đã xuất 50 đề mục mẫu ra file demuc_data.json")

if __name__ == "__main__":
    main()
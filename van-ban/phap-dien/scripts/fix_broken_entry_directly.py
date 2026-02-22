#!/usr/bin/env python3
"""
Fix entry bị lỗi trực tiếp trong file JSON
Entry bị lỗi: "TEN":"Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]
Thiếu dấu ngoặc kép đóng
"""

import re
from pathlib import Path

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    if not json_file.exists():
        print(f"File không tồn tại: {json_file}")
        return
    
    print(f"Đang đọc file: {json_file}")
    
    # Đọc file với BOM handling
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    print(f"Đã đọc {len(content):,} chars")
    
    # Tìm jdAllTree
    print("\nTìm jdAllTree...")
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("✗ Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    print(f"✓ Tìm thấy jdAllTree, độ dài: {len(json_str):,} chars")
    
    # Vị trí lỗi: 5,568,331
    error_pos = 5568331
    print(f"\nVị trí lỗi: {error_pos:,}")
    
    # Tìm entry bị lỗi
    print("Tìm entry bị lỗi...")
    
    # Tìm từ error_pos trở về trước để tìm bắt đầu entry
    start_pos = json_str.rfind('{', 0, error_pos)
    if start_pos == -1:
        print("✗ Không tìm thấy bắt đầu entry")
        return
    
    print(f"  Bắt đầu entry tại: {start_pos:,}")
    
    # Tìm từ error_pos trở đi để tìm kết thúc entry
    # Entry bị lỗi có TEN không đóng, cần tìm pattern tiếp theo
    # Tìm "}, {" hoặc "}]"
    
    # Tìm pattern cho entry tiếp theo
    search_text = json_str[error_pos:error_pos + 500]
    print(f"\nContext tại vị trí lỗi (500 chars):")
    print("-" * 80)
    print(search_text)
    print("-" * 80)
    
    # Phân tích lỗi
    # Dòng bị lỗi: "TEN":"Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]
    # Thiếu dấu " sau [6]
    
    # Tìm vị trí của [6] trong context
    bracket_pos = search_text.find('[6]')
    if bracket_pos != -1:
        print(f"\nTìm thấy '[6]' tại vị trí: {bracket_pos}")
        print(f"Text xung quanh: {search_text[bracket_pos-50:bracket_pos+50]}")
        
        # Check xem có dấu " sau [6] không
        after_bracket = search_text[bracket_pos+3:bracket_pos+10]
        print(f"Sau '[6]': '{after_bracket}'")
        
        if '"' not in after_bracket:
            print("⚠ Xác nhận: Thiếu dấu \" sau [6]")
            
            # Tìm vị trí thực tế trong json_str
            actual_bracket_pos = error_pos + bracket_pos
            print(f"Vị trí thực tế của '[6]' trong json_str: {actual_bracket_pos:,}")
            
            # Fix: Thêm dấu " sau [6]
            # Nhưng cần đảm bảo không phá vỡ cấu trúc
            # Cần tìm đúng vị trí để insert
            
            # Tìm từ actual_bracket_pos+3 trở đi, tìm dấu , hoặc }
            for i in range(actual_bracket_pos + 3, min(actual_bracket_pos + 100, len(json_str))):
                if json_str[i] in ',}':
                    insert_pos = i
                    print(f"\nTìm thấy '{json_str[i]}' tại vị trí {i:,}")
                    print(f"Context: {json_str[i-20:i+20]}")
                    
                    # Check xem trước đó có dấu " không
                    if json_str[i-1] != '"':
                        print("✓ Có thể insert dấu \" tại đây")
                        
                        # Tạo JSON string đã fix
                        fixed_json = json_str[:insert_pos] + '"' + json_str[insert_pos:]
                        
                        # Test parse
                        import json
                        try:
                            # Test parse từ start_pos đến insert_pos+1
                            test_str = fixed_json[start_pos:insert_pos+100]
                            if test_str.startswith('{'):
                                # Tìm } đóng
                                end_pos = test_str.find('}', 100)
                                if end_pos != -1:
                                    test_entry = test_str[:end_pos+1]
                                    parsed = json.loads(test_entry)
                                    print(f"\n✓ Test parse thành công!")
                                    print(f"  ID: {parsed.get('ID')}")
                                    print(f"  TEN: {parsed.get('TEN')}")
                                    
                                    # Lưu file đã fix
                                    fixed_file = base_dir / "json" / "jsonData_fixed_all.js"
                                    
                                    # Thay thế json_str trong content
                                    fixed_content = content.replace(json_str, fixed_json)
                                    
                                    with open(fixed_file, 'w', encoding='utf-8') as f:
                                        f.write(fixed_content)
                                    
                                    print(f"\n✓ Đã lưu file đã fix: {fixed_file}")
                                    print(f"  Kích thước: {fixed_file.stat().st_size:,} bytes")
                                    
                                    return
                        except json.JSONDecodeError as e:
                            print(f"✗ Test parse thất bại: {e}")
    
    print("\nKhông thể tự động fix. Cần manual fix.")
    
    # Hiển thị thêm context để manual fix
    print("\n" + "="*80)
    print("CONTEXT CHI TIẾT ĐỂ MANUAL FIX")
    print("="*80)
    
    show_start = max(0, error_pos - 200)
    show_end = min(len(json_str), error_pos + 300)
    print(f"\nVị trí {show_start:,} đến {show_end:,}:")
    print("-" * 80)
    context = json_str[show_start:show_end]
    
    # Highlight phần bị lỗi
    lines = context.split('\n')
    for i, line in enumerate(lines):
        if '[6]' in line and '"' not in line[line.find('[6]')+3:line.find('[6]')+10]:
            print(f"⚠ LỖI → {line}")
        else:
            print(f"       {line}")
    
    print("-" * 80)
    
    # Ghi file để manual edit
    manual_fix_file = base_dir / "json" / "manual_fix_instructions.txt"
    with open(manual_fix_file, 'w', encoding='utf-8') as f:
        f.write("INSTRUCTIONS FOR MANUAL FIX\n")
        f.write("="*50 + "\n\n")
        f.write("FILE: jsonData.js\n")
        f.write("ERROR: Missing closing quote after [6]\n")
        f.write("POSITION: ~5,568,331\n\n")
        f.write("CONTEXT:\n")
        f.write(context + "\n\n")
        f.write("FIX:\n")
        f.write('Find: hàng hải[6],\n')
        f.write('Replace with: hàng hải[6]",\n')
    
    print(f"\n✓ Đã tạo hướng dẫn manual fix: {manual_fix_file}")

if __name__ == "__main__":
    main()
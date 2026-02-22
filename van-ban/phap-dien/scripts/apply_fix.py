#!/usr/bin/env python3
"""
Apply fix cho entry bị lỗi
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
    
    # Tìm và fix lỗi
    # Lỗi: "TEN":"Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]
    # Thiếu dấu " sau [6]
    
    error_pattern = r'hàng hải\[6\]\s*,'
    fixed_pattern = r'hàng hải[6]",'
    
    # Count occurrences
    occurrences = len(re.findall(error_pattern, content))
    print(f"\nTìm thấy {occurrences} occurrences của pattern lỗi")
    
    if occurrences == 0:
        # Thử pattern khác
        error_pattern = r'hàng hải\[6\]\s*}'
        fixed_pattern = r'hàng hải[6]"}'
        occurrences = len(re.findall(error_pattern, content))
        print(f"Thử pattern 2: {occurrences} occurrences")
    
    if occurrences == 0:
        # Tìm cụ thể hơn
        error_text = 'Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]'
        if error_text in content:
            print(f"Tìm thấy error text trong content")
            # Tìm vị trí
            pos = content.find(error_text)
            if pos != -1:
                print(f"Vị trí: {pos:,}")
                # Hiển thị context
                print(f"Context: {content[pos-50:pos+len(error_text)+50]}")
                
                # Fix: thêm dấu " sau [6]
                # Tìm từ pos + len(error_text) trở đi
                after_pos = pos + len(error_text)
                next_char = content[after_pos] if after_pos < len(content) else ''
                print(f"Ký tự sau '[6]': '{next_char}'")
                
                if next_char in ',}':
                    # Insert dấu " trước ký tự này
                    fixed_content = content[:after_pos] + '"' + content[after_pos:]
                    
                    # Lưu file đã fix
                    fixed_file = base_dir / "json" / "jsonData_fixed.js"
                    with open(fixed_file, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    
                    print(f"\n✓ Đã fix và lưu: {fixed_file}")
                    
                    # Test parse
                    import json
                    try:
                        # Extract jdAllTree để test
                        pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
                        match = re.search(pattern, fixed_content, re.DOTALL)
                        
                        if not match:
                            pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
                            match = re.search(pattern, fixed_content, re.DOTALL)
                        
                        if match:
                            json_str = match.group(1)
                            data = json.loads(json_str)
                            print(f"✓ Test parse thành công! Tổng entries: {len(data):,}")
                            
                            # Lưu thêm file test
                            test_file = base_dir / "output" / "test_parsed_fixed.json"
                            with open(test_file, 'w', encoding='utf-8') as f:
                                json.dump(data[:100], f, ensure_ascii=False, indent=2)
                            print(f"✓ Đã lưu 100 entries test: {test_file}")
                    except json.JSONDecodeError as e:
                        print(f"✗ Test parse thất bại: {e}")
                    
                    return
    
    # Try regex replace
    if occurrences > 0:
        print(f"\nĐang fix {occurrences} occurrences...")
        fixed_content = re.sub(error_pattern, fixed_pattern, content)
        
        # Lưu file đã fix
        fixed_file = base_dir / "json" / "jsonData_fixed.js"
        with open(fixed_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✓ Đã fix và lưu: {fixed_file}")
        
        # Verify fix
        occurrences_after = len(re.findall(error_pattern, fixed_content))
        print(f"Occurrences sau fix: {occurrences_after}")
        
        if occurrences_after == 0:
            print("✓ Fix thành công!")
        else:
            print("⚠ Vẫn còn occurrences, cần check lại")
    else:
        print("\n✗ Không tìm thấy pattern lỗi")
        print("Cần manual fix")

if __name__ == "__main__":
    main()
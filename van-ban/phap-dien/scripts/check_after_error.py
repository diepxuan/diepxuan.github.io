#!/usr/bin/env python3
"""
Kiểm tra xem có entries nào sau entry bị lỗi không
"""

import re
from pathlib import Path

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    print(f"Đang đọc: {json_file}")
    
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
    print(f"jdAllTree length: {len(json_str):,} chars")
    
    # Tìm entry bị lỗi
    error_text = 'Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]'
    error_pos = json_str.find(error_text)
    
    if error_pos == -1:
        print("✗ Không tìm thấy entry bị lỗi")
        return
    
    print(f"\nEntry bị lỗi tại: {error_pos:,}")
    
    # Phần sau entry bị lỗi
    after_error = json_str[error_pos + len(error_text):]
    print(f"\nPhần sau entry bị lỗi: {len(after_error):,} chars")
    
    if len(after_error) == 0:
        print("✓ KHÔNG CÓ entries nào sau entry bị lỗi")
        print("  File kết thúc ngay sau entry bị lỗi")
        return
    
    print(f"\nPreview (500 chars):")
    print("-" * 80)
    print(after_error[:500])
    print("-" * 80)
    
    # Tìm pattern của entry mới
    entry_patterns = [
        r'\{"ID":"[^"]+"',  # Bắt đầu entry mới
        r'"TEN":"[^"]+"',   # TEN field
        r'"MAPC":"[^"]+"',  # MAPC field
    ]
    
    print(f"\nTìm kiếm patterns của entries...")
    
    for pattern in entry_patterns:
        matches = re.findall(pattern, after_error[:10000])  # Check 10k chars đầu
        if matches:
            print(f"\nPattern: {pattern[:30]}...")
            print(f"  Tìm thấy {len(matches)} matches")
            
            for i, match in enumerate(matches[:3]):
                print(f"  {i+1}. {match[:100]}...")
    
    # Tìm ] cuối cùng (kết thúc array)
    last_bracket = after_error.rfind(']')
    if last_bracket != -1:
        print(f"\nTìm thấy ] cuối cùng tại vị trí: {last_bracket:,}")
        
        # Phần trước ] cuối cùng
        before_last_bracket = after_error[:last_bracket]
        
        # Tìm các entries trong phần này
        entry_starts = [m.start() for m in re.finditer(r'\{"ID":"', before_last_bracket)]
        
        if entry_starts:
            print(f"✓ Tìm thấy {len(entry_starts)} entries sau entry bị lỗi!")
            
            # Hiển thị entry đầu tiên sau lỗi
            first_after_error = before_last_bracket[entry_starts[0]:entry_starts[0]+500]
            print(f"\nEntry đầu tiên sau lỗi (500 chars):")
            print("-" * 80)
            print(first_after_error)
            print("-" * 80)
            
            # Ước tính tổng số entries
            print(f"\n📊 ƯỚC TÍNH:")
            print(f"  - Entries trước lỗi: 18,649")
            print(f"  - Entries sau lỗi: ~{len(entry_starts)}")
            print(f"  - Tổng ước tính: ~{18649 + len(entry_starts):,}")
        else:
            print("✗ Không tìm thấy entries sau ] cuối cùng")
    
    # Check xem có phải chỉ là whitespace không
    stripped = after_error.strip()
    if len(stripped) == 0 or stripped == ']':
        print(f"\n✓ Phần sau entry bị lỗi chỉ là whitespace/]")
        print(f"  Không có entries nào sau entry bị lỗi")
    else:
        print(f"\n⚠ CÓ DỮ LIỆU SAU ENTRY BỊ LỖI")
        print(f"  Cần phân tích thêm")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Parse từ cuối file lên để tìm entries sau lỗi
"""

import re
import json
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
    
    # Tìm từ cuối lên
    print("\nTìm entries từ cuối file lên...")
    
    # Tìm vị trí của entry cuối cùng đã parse được
    # Entry cuối cùng: "TEN":"Điều 14.4.NĐ.3.9. Thông báo hàng hải"
    last_known_entry = 'Điều 14.4.NĐ.3.9. Thông báo hàng hải'
    last_pos = json_str.find(last_known_entry)
    
    if last_pos == -1:
        print("✗ Không tìm thấy entry cuối cùng đã biết")
        return
    
    print(f"Vị trí entry cuối cùng đã biết: {last_pos:,}")
    
    # Tìm từ vị trí này trở đi
    search_pos = last_pos + len(last_known_entry) + 100  # Thêm buffer
    
    # Tìm entry tiếp theo
    next_entry_start = json_str.find('{"ID":"', search_pos)
    
    if next_entry_start == -1:
        print("✗ Không tìm thấy entry tiếp theo")
        
        # Có thể đã hết file, hoặc lỗi nghiêm trọng
        # Kiểm tra phần còn lại của file
        remaining = json_str[search_pos:]
        print(f"\nPhần còn lại của file ({len(remaining):,} chars):")
        print("-" * 80)
        print(remaining[:500])
        print("-" * 80)
        
        # Tìm bất kỳ pattern nào giống entry
        entry_patterns = [
            r'\{"ID":"[^"]+"',
            r'"TEN":"[^"]+',
            r'"MAPC":"[^"]+'
        ]
        
        for pattern in entry_patterns:
            matches = re.findall(pattern, remaining[:10000])
            if matches:
                print(f"\nTìm thấy {len(matches)} matches cho pattern: {pattern[:20]}...")
                for i, match in enumerate(matches[:3]):
                    print(f"  {i+1}. {match[:100]}...")
        
        return
    
    print(f"✓ Tìm thấy entry tiếp theo tại: {next_entry_start:,}")
    
    # Extract từ vị trí này đến hết
    remaining_json = json_str[next_entry_start:]
    
    # Đảm bảo bắt đầu bằng [
    if not remaining_json.startswith('['):
        remaining_json = '[' + remaining_json
    
    # Đảm bảo kết thúc bằng ]
    if not remaining_json.endswith(']'):
        remaining_json = remaining_json + ']'
    
    print(f"\nPhần JSON còn lại: {len(remaining_json):,} chars")
    print(f"Preview đầu: {remaining_json[:200]}...")
    print(f"Preview cuối: ...{remaining_json[-200:]}")
    
    # Thử parse
    try:
        data = json.loads(remaining_json)
        print(f"\n🎉 PARSE THÀNH CÔNG PHẦN CÒN LẠI!")
        print(f"  Số entries: {len(data):,}")
        
        # Lưu kết quả
        output_file = base_dir / "output" / "remaining_entries.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Đã lưu: {output_file}")
        
        # Sample
        if data:
            print(f"\n📝 SAMPLE TỪ PHẦN CÒN LẠI:")
            print(f"  Entry #1: {data[0].get('TEN', '')[:100]}...")
            if len(data) > 1:
                print(f"  Entry #{len(data)//2:,}: {data[len(data)//2].get('TEN', '')[:100]}...")
            print(f"  Entry #{len(data):,}: {data[-1].get('TEN', '')[:100]}...")
            
            # Tổng hợp với entries trước đó
            total_entries = 18649 + len(data)
            print(f"\n📊 TỔNG HỢP:")
            print(f"  - Entries trước lỗi: 18,649")
            print(f"  - Entries sau lỗi: {len(data):,}")
            print(f"  - Tổng cộng: {total_entries:,}")
            print(f"  - Tỷ lệ: {total_entries/76303*100:.1f}% of 76,303")
    
    except json.JSONDecodeError as e:
        print(f"\n✗ Parse phần còn lại thất bại: {e}")
        print(f"  Error position: {e.pos}")
        
        # Hiển thị context lỗi
        start = max(0, e.pos - 100)
        end = min(len(remaining_json), e.pos + 100)
        print(f"  Context: {remaining_json[start:end]}")
        
        # Thử manual fix
        print("\nThử manual fix...")
        
        # Tìm entry bị lỗi trong phần còn lại
        error_in_remaining = e.pos
        
        # Hiển thị chi tiết hơn
        print(f"\nChi tiết lỗi trong phần còn lại:")
        error_start = max(0, error_in_remaining - 200)
        error_end = min(len(remaining_json), error_in_remaining + 300)
        error_context = remaining_json[error_start:error_end]
        
        lines = error_context.split('\n')
        for i, line in enumerate(lines):
            if i == len(lines) // 2:
                print(f"⚠ LỖI → {line}")
            else:
                print(f"       {line}")

if __name__ == "__main__":
    main()
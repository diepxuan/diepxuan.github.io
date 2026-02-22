#!/usr/bin/env python3
"""
Recover từ vị trí lỗi và tiếp tục parse
"""

import re
import json
from pathlib import Path

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    # Đọc file với BOM handling
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    # Tìm jdAllTree
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    
    # Vị trí lỗi: 5568331 (bắt đầu của entry bị lỗi)
    error_pos = 5568331
    
    print(f"Vị trí lỗi: {error_pos}")
    print(f"Độ dài JSON: {len(json_str)}")
    
    # Tìm từ vị trí lỗi trở đi
    # Tìm entry tiếp theo sau entry bị lỗi
    # Entry bị lỗi có TEN: "Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]"
    # Không có dấu ngoặc kép đóng, nên chúng ta cần tìm nơi kết thúc
    
    # Tìm từ error_pos, tìm pattern của entry tiếp theo: },{
    search_pos = error_pos
    next_entry_pattern = r'\},\s*\{'
    
    match = re.search(next_entry_pattern, json_str[search_pos:search_pos+1000])
    
    if match:
        recovery_pos = search_pos + match.start() + 1  # Vị trí của { sau dấu phẩy
        print(f"\nTìm thấy entry tiếp theo tại vị trí: {recovery_pos}")
        
        # Lấy context xung quanh
        print(f"\nContext tại recovery position:")
        print("-" * 80)
        print(json_str[recovery_pos-50:recovery_pos+100])
        print("-" * 80)
        
        # Bây giờ parse từ recovery_pos trở đi
        print(f"\nParse từ vị trí {recovery_pos} trở đi...")
        
        # Tạo JSON string mới: [ + phần từ recovery_pos đến hết
        # Nhưng trước tiên cần tìm ] cuối cùng
        array_end = json_str.rfind(']')
        if array_end == -1:
            print("Không tìm thấy ] cuối cùng")
            return
        
        # Phần JSON còn lại
        remaining_json = json_str[recovery_pos-1:array_end+1]  # -1 để lấy cả dấu [
        print(f"Độ dài phần còn lại: {len(remaining_json):,} chars")
        
        # Đảm bảo bắt đầu bằng [
        if not remaining_json.startswith('['):
            remaining_json = '[' + remaining_json
        
        print(f"\nThử parse phần còn lại...")
        
        try:
            data = json.loads(remaining_json)
            print(f"✓ Parse phần còn lại thành công!")
            print(f"  Số entries: {len(data)}")
            
            # Lưu kết quả
            output_file = base_dir / "json" / "recovered_entries.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"\n✓ Đã lưu {len(data)} entries vào {output_file}")
            
            # Hiển thị sample
            if data:
                print(f"\nEntry đầu tiên trong phần recovered:")
                first = data[0]
                print(f"  ID: {first.get('ID')}")
                print(f"  TEN: {first.get('TEN')[:50]}..." if first.get('TEN') and len(first.get('TEN')) > 50 else f"  TEN: {first.get('TEN')}")
                
                print(f"\nEntry cuối cùng trong phần recovered:")
                last = data[-1]
                print(f"  ID: {last.get('ID')}")
                print(f"  TEN: {last.get('TEN')[:50]}..." if last.get('TEN') and len(last.get('TEN')) > 50 else f"  TEN: {last.get('TEN')}")
        
        except json.JSONDecodeError as e:
            print(f"✗ Parse phần còn lại thất bại: {e}")
            print(f"  Error position: {e.pos}")
            
            # Hiển thị context
            start = max(0, e.pos - 100)
            end = min(len(remaining_json), e.pos + 100)
            print(f"  Context: {remaining_json[start:end]}")
    
    else:
        print("\nKhông tìm thấy entry tiếp theo trong 1000 ký tự đầu")
        
        # Thử tìm cách khác: tìm pattern "ID":"...
        id_pattern = r'"ID"\s*:\s*"[^"]+"'
        match = re.search(id_pattern, json_str[error_pos+100:error_pos+500])
        
        if match:
            recovery_pos = error_pos + 100 + match.start()
            print(f"\nTìm thấy trường ID tại vị trí: {recovery_pos}")
            
            # Tìm dấu { trước đó
            brace_pos = json_str.rfind('{', 0, recovery_pos)
            if brace_pos > error_pos:
                recovery_pos = brace_pos
                print(f"  Tìm thấy dấu {{ tại vị trí: {recovery_pos}")
                
                # Hiển thị context
                print(f"\nContext tại recovery position:")
                print("-" * 80)
                print(json_str[recovery_pos-50:recovery_pos+200])
                print("-" * 80)

if __name__ == "__main__":
    main()
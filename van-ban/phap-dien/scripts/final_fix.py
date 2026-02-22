#!/usr/bin/env python3
"""
Final fix cho entry bị lỗi
Entry bị cắt ngang, cần thêm phần đóng
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
    
    print(f"\nTìm thấy entry bị lỗi tại: {error_pos:,}")
    
    # Tìm từ error_pos trở về trước để tìm bắt đầu entry
    start_pos = json_str.rfind('{', 0, error_pos)
    if start_pos == -1:
        print("✗ Không tìm thấy bắt đầu entry")
        return
    
    print(f"Bắt đầu entry: {start_pos:,}")
    
    # Extract entry bị lỗi
    broken_entry = json_str[start_pos:]
    
    # Tìm vị trí của [6] trong entry
    bracket_pos = broken_entry.find('[6]')
    if bracket_pos == -1:
        print("✗ Không tìm thấy [6]")
        return
    
    # Vị trí sau [6]
    after_bracket = bracket_pos + 3
    
    # Hiển thị entry bị lỗi
    print(f"\nENTRY BỊ LỖI (first 500 chars):")
    print("-" * 80)
    print(broken_entry[:500])
    print("-" * 80)
    
    # Phân tích: entry này thiếu gì?
    # 1. Thiếu dấu " sau [6] ✓
    # 2. Thiếu ,"ChuDeID":"..." ✓
    # 3. Thiếu ,"DeMucID":"..." ✓
    # 4. Thiếu } đóng ✓
    
    # Dựa trên các entries trước đó, tạo phần đóng
    # Entry trước đó có format:
    # ...","ChuDeID":"b82ee309-2527-4a7d-8d4d-fccdfabbc86c","DeMucID":"c9269682-f64e-4a54-a352-98e10cadaf26"}
    
    # Tìm ChuDeID và DeMucID từ entry trước
    prev_entry_start = json_str.rfind('{', 0, start_pos - 1)
    if prev_entry_start != -1:
        prev_entry_end = json_str.find('}', prev_entry_start)
        if prev_entry_end != -1:
            prev_entry = json_str[prev_entry_start:prev_entry_end+1]
            
            # Extract ChuDeID và DeMucID
            chude_match = re.search(r'"ChuDeID":"([^"]+)"', prev_entry)
            demuc_match = re.search(r'"DeMucID":"([^"]+)"', prev_entry)
            
            if chude_match and demuc_match:
                chude_id = chude_match.group(1)
                demuc_id = demuc_match.group(1)
                
                print(f"\nTìm thấy từ entry trước:")
                print(f"  ChuDeID: {chude_id}")
                print(f"  DeMucID: {demuc_id}")
                
                # Tạo phần đóng cho entry bị lỗi
                closing_part = f',"ChuDeID":"{chude_id}","DeMucID":"{demuc_id}"}}'
                
                # Fix entry
                # 1. Thêm dấu " sau [6]
                # 2. Thêm closing_part
                
                # Tìm vị trí để insert
                # Sau [6] có thể là kết thúc string hoặc có ký tự khác
                insert_pos = start_pos + after_bracket
                
                # Check ký tự tại insert_pos
                if insert_pos < len(json_str):
                    char_at_pos = json_str[insert_pos]
                    print(f"\nKý tự tại vị trí {insert_pos:,}: '{char_at_pos}'")
                    
                    # Tạo fixed JSON
                    if char_at_pos in ',}':
                        # Insert dấu " trước ký tự này
                        fixed_json = json_str[:insert_pos] + '"' + json_str[insert_pos:]
                        # Thêm closing_part sau dấu "
                        fixed_json = fixed_json[:insert_pos+1] + closing_part + fixed_json[insert_pos+1:]
                    else:
                        # Không có ký tự đóng, thêm cả
                        fixed_json = json_str[:insert_pos] + '"' + closing_part + json_str[insert_pos:]
                    
                    # Lưu file đã fix
                    fixed_file = base_dir / "json" / "jsonData_completely_fixed.js"
                    
                    # Thay thế trong content
                    fixed_content = content.replace(json_str, fixed_json)
                    
                    with open(fixed_file, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    
                    print(f"\n✓ Đã tạo file đã fix: {fixed_file}")
                    
                    # Test parse
                    import json
                    try:
                        # Extract jdAllTree từ file đã fix
                        fixed_match = re.search(pattern, fixed_content, re.DOTALL)
                        if not fixed_match:
                            fixed_match = re.search(r'var jdAllTree\s*=\s*(\[.*?\])', fixed_content, re.DOTALL)
                        
                        if fixed_match:
                            fixed_json_str = fixed_match.group(1)
                            data = json.loads(fixed_json_str)
                            print(f"🎉 PARSE TOÀN BỘ THÀNH CÔNG!")
                            print(f"  Tổng entries: {len(data):,}")
                            
                            # Lưu parsed data
                            parsed_file = base_dir / "output" / "completely_parsed.json"
                            with open(parsed_file, 'w', encoding='utf-8') as f:
                                json.dump(data, f, ensure_ascii=False, indent=2)
                            
                            print(f"✓ Đã lưu parsed data: {parsed_file}")
                            
                            # Tìm entry đã fix
                            for i, entry in enumerate(data):
                                if error_text in entry.get('TEN', ''):
                                    print(f"\n✓ Entry đã fix (index {i}):")
                                    print(f"  ID: {entry.get('ID')}")
                                    print(f"  TEN: {entry.get('TEN')}")
                                    print(f"  ChuDeID: {entry.get('ChuDeID')}")
                                    print(f"  DeMucID: {entry.get('DeMucID')}")
                                    break
                    
                    except json.JSONDecodeError as e:
                        print(f"✗ Parse thất bại: {e}")
                        print(f"  Error position: {e.pos}")
                        
                        # Hiển thị context
                        if hasattr(e, 'pos'):
                            start = max(0, e.pos - 100)
                            end = min(len(fixed_json_str), e.pos + 100)
                            print(f"  Context: {fixed_json_str[start:end]}")
    
    # Alternative: đơn giản bỏ entry bị lỗi
    print("\n\n--- ALTERNATIVE: BỎ ENTRY BỊ LỖI ---")
    
    # Tìm } đóng của entry trước entry bị lỗi
    prev_entry_end = json_str.rfind('}', 0, start_pos)
    if prev_entry_end != -1:
        # Tìm , sau } đó
        comma_after_prev = json_str.find(',', prev_entry_end)
        
        if comma_after_prev != -1:
            # Tìm } đóng của array
            array_end = json_str.rfind(']')
            
            if array_end != -1:
                # Tạo JSON mới bỏ entry bị lỗi
                # Từ đầu đến sau dấu , của entry trước
                # Đến trước ] cuối cùng
                new_json = json_str[:comma_after_prev] + json_str[array_end:]
                
                # Test parse
                import json
                try:
                    data = json.loads(new_json)
                    print(f"✓ Parse thành công sau khi bỏ entry bị lỗi")
                    print(f"  Tổng entries: {len(data):,}")
                    print(f"  Đã bỏ: 1 entry bị lỗi")
                    
                    # Lưu
                    skipped_file = base_dir / "output" / "skipped_broken_entry.json"
                    with open(skipped_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    
                    print(f"✓ Đã lưu: {skipped_file}")
                
                except json.JSONDecodeError as e:
                    print(f"✗ Parse thất bại: {e}")

if __name__ == "__main__":
    main()
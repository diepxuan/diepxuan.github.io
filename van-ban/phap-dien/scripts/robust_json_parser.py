#!/usr/bin/env python3
"""
Robust JSON parser cho dữ liệu Pháp điển
Xử lý các lỗi JSON phổ biến
"""

import re
import json
from pathlib import Path

class RobustJSONParser:
    def __init__(self):
        self.entries = []
        self.errors = []
    
    def parse_file(self, file_path):
        """Parse file JSON với xử lý lỗi"""
        print(f"Đang parse file: {file_path}")
        
        # Đọc file với BOM handling
        with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
            content = f.read()
        
        print(f"File size: {len(content):,} bytes")
        
        # Tìm jdAllTree
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
            match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print("Không tìm thấy jdAllTree")
            return False
        
        json_str = match.group(1)
        print(f"Đã tìm thấy jdAllTree, độ dài: {len(json_str):,} chars")
        
        # Parse với xử lý lỗi
        return self.parse_json_string(json_str)
    
    def parse_json_string(self, json_str):
        """Parse JSON string với xử lý lỗi"""
        print(f"Đang parse JSON string...")
        
        # Thử parse bình thường trước
        try:
            data = json.loads(json_str)
            self.entries = data
            print(f"✓ Parse thành công bình thường!")
            print(f"  Tổng số entries: {len(self.entries)}")
            return True
        except json.JSONDecodeError as e:
            print(f"Parse thất bại: {e}")
            print(f"  Sử dụng robust parser...")
        
        # Sử dụng robust parser
        return self._robust_parse(json_str)
    
    def _robust_parse(self, json_str):
        """Robust parsing - xử lý từng entry riêng biệt"""
        print(f"Robust parsing...")
        
        pos = 0
        entry_count = 0
        success_count = 0
        error_count = 0
        
        while pos < len(json_str):
            # Skip whitespace và dấu phẩy
            while pos < len(json_str) and json_str[pos] in ' \t\n\r,':
                pos += 1
            
            if pos >= len(json_str):
                break
            
            # Check for array start/end
            if json_str[pos] == '[':
                pos += 1
                continue
            elif json_str[pos] == ']':
                pos += 1
                continue
            
            # Parse object
            if json_str[pos] == '{':
                entry_start = pos
                entry_str, new_pos = self._extract_object(json_str, pos)
                
                if entry_str:
                    # Try to parse this entry
                    try:
                        entry = json.loads(entry_str)
                        self.entries.append(entry)
                        success_count += 1
                        
                        if success_count % 10000 == 0:
                            print(f"  Đã parse {success_count} entries thành công")
                    
                    except json.JSONDecodeError as e:
                        error_count += 1
                        
                        # Try to fix and parse
                        fixed_entry = self._fix_entry(entry_str)
                        if fixed_entry:
                            try:
                                entry = json.loads(fixed_entry)
                                self.entries.append(entry)
                                success_count += 1
                                print(f"  Đã fix và parse entry {success_count}")
                            except:
                                self.errors.append({
                                    'position': pos,
                                    'error': str(e),
                                    'entry_str': entry_str[:200] + '...' if len(entry_str) > 200 else entry_str
                                })
                        else:
                            self.errors.append({
                                'position': pos,
                                'error': str(e),
                                'entry_str': entry_str[:200] + '...' if len(entry_str) > 200 else entry_str
                            })
                    
                    pos = new_pos
                    entry_count += 1
                else:
                    # Cannot extract object, skip
                    print(f"  Không thể extract object tại vị trí {pos}")
                    break
            else:
                # Unexpected character, skip
                print(f"  Ký tự không mong muốn tại {pos}: {repr(json_str[pos])}")
                pos += 1
        
        print(f"\nKết quả parse:")
        print(f"  Tổng số entries xử lý: {entry_count}")
        print(f"  Parse thành công: {success_count}")
        print(f"  Lỗi: {error_count}")
        print(f"  Tổng entries trong danh sách: {len(self.entries)}")
        
        return success_count > 0
    
    def _extract_object(self, json_str, start_pos):
        """Trích xuất object từ JSON string"""
        if json_str[start_pos] != '{':
            return None, start_pos
        
        brace_count = 0
        in_string = False
        escape = False
        
        for i in range(start_pos, len(json_str)):
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
                        # Found complete object
                        return json_str[start_pos:i+1], i+1
        
        # Object không đóng
        return None, start_pos
    
    def _fix_entry(self, entry_str):
        """Fix common errors in an entry"""
        # Fix 1: Đảm bảo TEN có dấu ngoặc kép đóng
        # Tìm "TEN":"... và đảm bảo có dấu ngoặc kép đóng
        
        # Pattern tìm "TEN":"... [không kết thúc bằng "]
        ten_pattern = r'("TEN"\s*:\s*")([^"]+(?=\s*",))'
        
        def fix_ten(match):
            prefix = match.group(1)
            content = match.group(2)
            return prefix + content + '"'
        
        fixed = re.sub(ten_pattern, fix_ten, entry_str)
        
        # Fix 2: Escape các ký tự đặc biệt
        # Tìm các chuỗi và escape brackets
        if fixed != entry_str:
            return fixed
        
        return None
    
    def save_results(self, output_dir):
        """Lưu kết quả parse"""
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        # Lưu entries
        if self.entries:
            entries_file = output_dir / "parsed_entries.json"
            with open(entries_file, 'w', encoding='utf-8') as f:
                json.dump(self.entries, f, ensure_ascii=False, indent=2)
            
            print(f"\n✓ Đã lưu {len(self.entries)} entries vào {entries_file}")
        
        # Lưu errors
        if self.errors:
            errors_file = output_dir / "parse_errors.json"
            with open(errors_file, 'w', encoding='utf-8') as f:
                json.dump(self.errors, f, ensure_ascii=False, indent=2)
            
            print(f"✓ Đã lưu {len(self.errors)} errors vào {errors_file}")
        
        # Tạo summary
        summary_file = output_dir / "parse_summary.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# KẾT QUẢ PARSE PHÁP ĐIỂN\n\n")
            f.write(f"**Tổng số entries parse thành công:** {len(self.entries)}\n")
            f.write(f"**Tổng số lỗi:** {len(self.errors)}\n\n")
            
            f.write("## Thống kê\n\n")
            f.write(f"- Entries: {len(self.entries)}\n")
            f.write(f"- Lỗi: {len(self.errors)}\n\n")
            
            if self.errors:
                f.write("## Lỗi đầu tiên (5 lỗi)\n\n")
                for i, error in enumerate(self.errors[:5]):
                    f.write(f"### Lỗi {i+1}\n")
                    f.write(f"- Vị trí: {error['position']}\n")
                    f.write(f"- Lỗi: {error['error']}\n")
                    f.write(f"- Entry: `{error['entry_str']}`\n\n")
        
        print(f"✓ Đã lưu summary vào {summary_file}")
        
        return entries_file

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    output_dir = base_dir / "output"
    
    # Tạo parser
    parser = RobustJSONParser()
    
    # Parse file
    success = parser.parse_file(json_file)
    
    if success:
        # Lưu kết quả
        entries_file = parser.save_results(output_dir)
        
        # Hiển thị sample
        if parser.entries:
            print(f"\nSample entry đầu tiên:")
            first = parser.entries[0]
            print(f"  ID: {first.get('ID')}")
            print(f"  TEN: {first.get('TEN')}")
            
            print(f"\nSample entry cuối cùng:")
            last = parser.entries[-1]
            print(f"  ID: {last.get('ID')}")
            print(f"  TEN: {last.get('TEN')}")
    else:
        print("\n✗ Parse thất bại!")

if __name__ == "__main__":
    main()
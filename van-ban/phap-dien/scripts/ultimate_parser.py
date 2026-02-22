#!/usr/bin/env python3
"""
Ultimate parser - Parse toàn bộ 76,303 entries bằng mọi cách
"""

import re
import json
import sys
from pathlib import Path

class UltimateParser:
    def __init__(self, json_str):
        self.json_str = json_str
        self.length = len(json_str)
        self.entries = []
        self.stats = {
            'total_parsed': 0,
            'errors_skipped': 0,
            'malformed_entries': 0
        }
    
    def parse_all(self):
        """Parse toàn bộ entries bằng nhiều phương pháp"""
        print(f"Bắt đầu parse {self.length:,} chars...")
        
        # Phương pháp 1: Thử parse bình thường
        try:
            data = json.loads(self.json_str)
            self.entries = data
            self.stats['total_parsed'] = len(data)
            print(f"✓ Parse bình thường thành công: {len(data):,} entries")
            return self.entries
        except json.JSONDecodeError as e:
            print(f"✗ Parse bình thường thất bại: {e}")
        
        # Phương pháp 2: Robust parsing với state machine
        print("\nChuyển sang robust parsing...")
        return self._robust_parse()
    
    def _robust_parse(self):
        """Robust parsing với state machine"""
        entries = []
        pos = 0
        current_entry = []
        brace_depth = 0
        in_string = False
        escape = False
        last_valid_pos = 0
        
        # Progress tracking
        last_report = 0
        
        while pos < self.length:
            char = self.json_str[pos]
            
            # Escape handling
            if escape:
                escape = False
                current_entry.append(char)
                pos += 1
                continue
            
            if char == '\\':
                escape = True
                current_entry.append(char)
                pos += 1
                continue
            
            # String handling
            if char == '"' and not escape:
                in_string = not in_string
                current_entry.append(char)
                pos += 1
                continue
            
            # Brace handling (chỉ khi không trong string)
            if not in_string:
                if char == '{':
                    brace_depth += 1
                    if brace_depth == 1:
                        # Bắt đầu entry mới
                        current_entry = ['{']
                    else:
                        current_entry.append(char)
                
                elif char == '}':
                    brace_depth -= 1
                    current_entry.append(char)
                    
                    if brace_depth == 0:
                        # Kết thúc entry
                        entry_str = ''.join(current_entry)
                        
                        # Thử parse entry này
                        try:
                            entry = json.loads(entry_str)
                            entries.append(entry)
                            self.stats['total_parsed'] += 1
                            
                            # Progress report
                            if len(entries) % 5000 == 0:
                                print(f"  Đã parse {len(entries):,} entries")
                            
                            # Reset
                            current_entry = []
                            last_valid_pos = pos
                        
                        except json.JSONDecodeError:
                            # Entry bị lỗi, thử fix
                            fixed_entry = self._try_fix_entry(entry_str)
                            if fixed_entry:
                                try:
                                    entry = json.loads(fixed_entry)
                                    entries.append(entry)
                                    self.stats['total_parsed'] += 1
                                    self.stats['malformed_entries'] += 1
                                except:
                                    self.stats['errors_skipped'] += 1
                            else:
                                self.stats['errors_skipped'] += 1
                        
                        # Skip whitespace và dấu phẩy
                        pos += 1
                        while pos < self.length and self.json_str[pos] in ' \t\n\r,':
                            pos += 1
                        continue
                
                elif char == '[' or char == ']':
                    # Bỏ qua array brackets
                    pass
                else:
                    # Các ký tự khác
                    current_entry.append(char)
            else:
                # Trong string
                current_entry.append(char)
            
            pos += 1
        
        self.entries = entries
        print(f"\n✓ Robust parsing hoàn tất:")
        print(f"  - Entries parsed: {len(entries):,}")
        print(f"  - Malformed fixed: {self.stats['malformed_entries']}")
        print(f"  - Errors skipped: {self.stats['errors_skipped']}")
        
        return entries
    
    def _try_fix_entry(self, entry_str):
        """Thử fix entry bị lỗi"""
        # Phổ biến: thiếu dấu " đóng trong TEN
        if '"TEN":"' in entry_str:
            # Tìm vị trí bắt đầu TEN
            ten_start = entry_str.find('"TEN":"') + 7
            
            # Tìm dấu " đóng
            quote_pos = entry_str.find('"', ten_start)
            comma_pos = entry_str.find(',', ten_start)
            brace_pos = entry_str.find('}', ten_start)
            
            # Nếu không tìm thấy dấu " đóng
            if quote_pos == -1 or (comma_pos != -1 and comma_pos < quote_pos) or (brace_pos != -1 and brace_pos < quote_pos):
                # Tìm vị trí để insert dấu "
                insert_pos = min(
                    comma_pos if comma_pos != -1 else len(entry_str),
                    brace_pos if brace_pos != -1 else len(entry_str)
                )
                
                if insert_pos < len(entry_str):
                    # Insert dấu "
                    fixed = entry_str[:insert_pos] + '"' + entry_str[insert_pos:]
                    return fixed
        
        return None
    
    def save_results(self, output_file):
        """Lưu kết quả"""
        output_file.parent.mkdir(exist_ok=True)
        
        print(f"\nĐang lưu {len(self.entries):,} entries...")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Đã lưu: {output_file}")
        print(f"  Kích thước: {output_file.stat().st_size:,} bytes")
        
        # Tạo summary
        summary_file = output_file.parent / f"{output_file.stem}_summary.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# ULTIMATE PARSER - SUMMARY\n\n")
            f.write(f"**Total Entries**: {len(self.entries):,}\n")
            f.write(f"**Malformed Fixed**: {self.stats['malformed_entries']}\n")
            f.write(f"**Errors Skipped**: {self.stats['errors_skipped']}\n\n")
            
            if self.entries:
                f.write("## First Entry\n```json\n")
                f.write(json.dumps(self.entries[0], ensure_ascii=False, indent=2))
                f.write("\n```\n\n")
                
                f.write("## Last Entry\n```json\n")
                f.write(json.dumps(self.entries[-1], ensure_ascii=False, indent=2))
                f.write("\n```\n")
        
        print(f"✓ Đã tạo summary: {summary_file}")

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    print(f"Đang đọc: {json_file}")
    
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    print(f"Đã đọc {len(content):,} chars")
    
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
    print(f"✓ Tìm thấy jdAllTree: {len(json_str):,} chars")
    
    # Parse
    parser = UltimateParser(json_str)
    entries = parser.parse_all()
    
    # Lưu kết quả
    output_file = base_dir / "output" / "ultimate_parsed.json"
    parser.save_results(output_file)
    
    # Thống kê
    print(f"\n📊 FINAL STATS:")
    print(f"  - Total entries: {len(entries):,}")
    
    if entries:
        # Phân tích MAPC để ước tính tổng số entries
        mapc_values = [e.get('MAPC', '') for e in entries]
        unique_mapc = len(set(mapc_values))
        print(f"  - Unique MAPC values: {unique_mapc:,}")
        
        # Sample
        print(f"\n📝 SAMPLE ENTRIES:")
        print(f"  #1: {entries[0].get('TEN', '')[:80]}...")
        print(f"  #{len(entries)//2:,}: {entries[len(entries)//2].get('TEN', '')[:80]}...")
        print(f"  #{len(entries):,}: {entries[-1].get('TEN', '')[:80]}...")
        
        # Check nếu đã parse được nhiều hơn 18,649
        if len(entries) > 18649:
            print(f"\n🎉 ĐÃ PARSE ĐƯỢC NHIỀU HƠN 18,649 ENTRIES!")
            print(f"   Tăng: +{len(entries) - 18649:,} entries")
            print(f"   Tỷ lệ: {len(entries)/76303*100:.1f}% of 76,303")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Trích xuất dữ liệu từ Bộ Pháp điển Điện tử
"""

import json
import re
import os
from collections import defaultdict

class PhapDienExtractor:
    def __init__(self, js_file_path):
        self.js_file_path = js_file_path
        self.content = None
        self.data = {
            'jdChuDe': [],
            'jdDeMuc': [],
            'jdAllTree': []
        }
        
    def load_file(self):
        """Đọc file JS"""
        print(f"Đang đọc file: {self.js_file_path}")
        try:
            with open(self.js_file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            print(f"  ✓ Đã đọc {len(self.content)} bytes")
            return True
        except Exception as e:
            print(f"  ✗ Lỗi đọc file: {e}")
            return False
    
    def extract_by_line(self):
        """Trích xuất dữ liệu bằng cách đọc từng dòng (cho file lớn)"""
        if not self.content:
            return False
        
        print("\nĐang trích xuất dữ liệu...")
        
        # Tìm vị trí bắt đầu của các biến
        lines = self.content.split('\n')
        
        current_var = None
        json_buffer = ""
        brace_count = 0
        in_string = False
        escape_next = False
        
        for line_num, line in enumerate(lines):
            # Tìm khai báo biến
            if 'var jdChuDe = ' in line:
                current_var = 'jdChuDe'
                start_idx = line.find('[')
                if start_idx > 0:
                    json_buffer = line[start_idx:]
                    brace_count = 1
                continue
            elif 'var jdDeMuc = ' in line:
                current_var = 'jdDeMuc'
                start_idx = line.find('[')
                if start_idx > 0:
                    json_buffer = line[start_idx:]
                    brace_count = 1
                continue
            elif 'var jdAllTree = ' in line:
                current_var = 'jdAllTree'
                start_idx = line.find('[')
                if start_idx > 0:
                    json_buffer = line[start_idx:]
                    brace_count = 1
                continue
            
            # Nếu đang thu thập JSON
            if current_var and json_buffer:
                # Đếm dấu ngoặc
                for char in line:
                    if escape_next:
                        escape_next = False
                        json_buffer += char
                        continue
                    
                    if char == '\\':
                        escape_next = True
                        json_buffer += char
                        continue
                    
                    if char == '"' and not escape_next:
                        in_string = not in_string
                    
                    if not in_string:
                        if char == '[':
                            brace_count += 1
                        elif char == ']':
                            brace_count -= 1
                    
                    json_buffer += char
                
                # Kiểm tra nếu đã đóng mảng
                if brace_count == 0:
                    try:
                        self.data[current_var] = json.loads(json_buffer)
                        print(f"  ✓ Đã load {current_var}: {len(self.data[current_var])} entries")
                    except json.JSONDecodeError as e:
                        print(f"  ✗ Lỗi decode {current_var}: {e}")
                        # Thử sửa lỗi
                        try:
                            # Xóa các ký tự không hợp lệ
                            json_buffer_clean = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_buffer)
                            self.data[current_var] = json.loads(json_buffer_clean)
                            print(f"  ✓ Đã load {current_var} (sau khi sửa): {len(self.data[current_var])} entries")
                        except:
                            print(f"  ✗ Không thể load {current_var}")
                    
                    # Reset
                    current_var = None
                    json_buffer = ""
                    brace_count = 0
        
        return True
    
    def analyze_structure(self):
        """Phân tích cấu trúc dữ liệu"""
        print("\n=== PHÂN TÍCH CẤU TRÚC ===")
        
        if self.data['jdChuDe']:
            print(f"Chủ đề (jdChuDe): {len(self.data['jdChuDe'])}")
            print("10 chủ đề đầu tiên:")
            for i, chude in enumerate(self.data['jdChuDe'][:10]):
                print(f"  {chude.get('STT')}. {chude.get('Text')}")
        
        if self.data['jdDeMuc']:
            print(f"\nĐề mục (jdDeMuc): {len(self.data['jdDeMuc'])}")
            
            # Tạo map từ ChuDeID sang tên chủ đề
            chude_map = {}
            for chude in self.data['jdChuDe']:
                chude_map[chude['Value']] = chude['Text']
            
            # Đếm đề mục theo chủ đề
            demuc_by_chude = defaultdict(list)
            for demuc in self.data['jdDeMuc']:
                chude_id = demuc.get('ChuDe')
                demuc_by_chude[chude_id].append(demuc)
            
            print(f"Phân bố theo {len(demuc_by_chude)} chủ đề:")
            for chude_id, demucs in list(demuc_by_chude.items())[:5]:
                chude_name = chude_map.get(chude_id, f"Unknown ({chude_id[:8]}...)")
                print(f"  {chude_name}: {len(demucs)} đề mục")
        
        if self.data['jdAllTree']:
            print(f"\nĐiều khoản (jdAllTree): {len(self.data['jdAllTree'])}")
            
            # Phân tích độ dài MAPC
            mapc_lengths = defaultdict(int)
            for entry in self.data['jdAllTree'][:1000]:  # Chỉ phân tích 1000 entries đầu
                mapc = entry.get('MAPC', '')
                mapc_lengths[len(mapc)] += 1
            
            print("Độ dài MAPC (1000 entries đầu):")
            for length, count in sorted(mapc_lengths.items()):
                print(f"  {length} ký tự: {count}")
            
            # Phân tích ChiMuc
            chimuc_types = defaultdict(int)
            for entry in self.data['jdAllTree'][:500]:
                chimuc = entry.get('ChiMuc', '')
                if chimuc:
                    if chimuc.isdigit():
                        chimuc_types['số'] += 1
                    elif len(chimuc) == 1 and chimuc.isalpha():
                        chimuc_types['chữ cái'] += 1
                    elif chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']:
                        chimuc_types['số la mã'] += 1
                    else:
                        chimuc_types['khác'] += 1
            
            print("\nPhân loại ChiMuc (500 entries đầu):")
            for chimuc_type, count in chimuc_types.items():
                print(f"  {chimuc_type}: {count}")
            
            # Hiển thị mẫu
            print("\n10 entries mẫu:")
            for i, entry in enumerate(self.data['jdAllTree'][:10]):
                mapc = entry.get('MAPC', '')
                chimuc = entry.get('ChiMuc', '')
                ten = entry.get('TEN', '')[:80]
                print(f"  {i+1:2d}. MAPC={mapc[:20]}..., ChiMuc={chimuc}, TEN={ten}...")
    
    def export_sample(self, output_dir='output'):
        """Xuất dữ liệu mẫu"""
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\n=== XUẤT DỮ LIỆU MẪU ĐẾN {output_dir} ===")
        
        if self.data['jdChuDe']:
            with open(f'{output_dir}/chude.json', 'w', encoding='utf-8') as f:
                json.dump(self.data['jdChuDe'], f, ensure_ascii=False, indent=2)
            print(f"✓ Đã xuất {len(self.data['jdChuDe'])} chủ đề")
        
        if self.data['jdDeMuc']:
            with open(f'{output_dir}/demuc_sample.json', 'w', encoding='utf-8') as f:
                json.dump(self.data['jdDeMuc'][:100], f, ensure_ascii=False, indent=2)
            print(f"✓ Đã xuất 100 đề mục mẫu")
        
        if self.data['jdAllTree']:
            # Xuất mẫu nhỏ
            with open(f'{output_dir}/alltree_sample.json', 'w', encoding='utf-8') as f:
                json.dump(self.data['jdAllTree'][:200], f, ensure_ascii=False, indent=2)
            print(f"✓ Đã xuất 200 điều khoản mẫu")
            
            # Xuất thống kê
            stats = {
                'total_entries': len(self.data['jdAllTree']),
                'mapc_lengths': defaultdict(int),
                'chimuc_types': defaultdict(int)
            }
            
            for entry in self.data['jdAllTree'][:10000]:  # Chỉ thống kê 10000 entries đầu
                mapc = entry.get('MAPC', '')
                stats['mapc_lengths'][len(mapc)] += 1
                
                chimuc = entry.get('ChiMuc', '')
                if chimuc:
                    if chimuc.isdigit():
                        stats['chimuc_types']['số'] += 1
                    elif len(chimuc) == 1 and chimuc.isalpha():
                        stats['chimuc_types']['chữ cái'] += 1
                    elif chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']:
                        stats['chimuc_types']['số la mã'] += 1
                    else:
                        stats['chimuc_types']['khác'] += 1
            
            with open(f'{output_dir}/stats.json', 'w', encoding='utf-8') as f:
                # Convert defaultdict to dict
                stats['mapc_lengths'] = dict(stats['mapc_lengths'])
                stats['chimuc_types'] = dict(stats['chimuc_types'])
                json.dump(stats, f, ensure_ascii=False, indent=2)
            print(f"✓ Đã xuất thống kê")
    
    def create_markdown_sample(self, output_dir='output'):
        """Tạo file Markdown mẫu từ dữ liệu"""
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\n=== TẠO MARKDOWN MẪU ===")
        
        if not self.data['jdAllTree']:
            print("Không có dữ liệu jdAllTree")
            return
        
        # Lấy 50 entries đầu tiên
        sample_entries = self.data['jdAllTree'][:50]
        
        # Nhóm theo DeMucID
        entries_by_demuc = defaultdict(list)
        for entry in sample_entries:
            demuc_id = entry.get('DeMucID')
            if demuc_id:
                entries_by_demuc[demuc_id].append(entry)
        
        # Tạo map từ DeMucID sang tên đề mục
        demuc_map = {}
        for demuc in self.data['jdDeMuc']:
            demuc_map[demuc['Value']] = demuc['Text']
        
        # Tạo map từ ChuDeID sang tên chủ đề
        chude_map = {}
        for chude in self.data['jdChuDe']:
            chude_map[chude['Value']] = chude['Text']
        
        # Tạo file Markdown cho mỗi đề mục có dữ liệu
        for demuc_id, entries in list(entries_by_demuc.items())[:3]:  # Chỉ tạo 3 file mẫu
            demuc_name = demuc_map.get(demuc_id, f"Đề mục {demuc_id[:8]}")
            
            # Tìm chủ đề của đề mục này
            chude_id = None
            chude_name = "Unknown"
            for demuc in self.data['jdDeMuc']:
                if demuc['Value'] == demuc_id:
                    chude_id = demuc.get('ChuDe')
                    chude_name = chude_map.get(chude_id, "Unknown")
                    break
            
            filename = f"{output_dir}/sample_{demuc_id[:8]}.md"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# {demuc_name}\n\n")
                f.write(f"**Chủ đề:** {chude_name}\n\n")
                f.write(f"**Đề mục ID:** {demuc_id}\n\n")
                f.write("---\n\n")
                
                # Sắp xếp entries theo MAPC
                sorted_entries = sorted(entries, key=lambda x: x.get('MAPC', ''))
                
                for entry in sorted_entries:
                    chimuc = entry.get('ChiMuc', '')
                    ten = entry.get('TEN', '')
                    mapc = entry.get('MAPC', '')
                    
                    # Xác định cấp độ dựa trên ChiMuc
                    if chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']:
                        f.write(f"\n## Chương {chimuc}: {ten}\n")
                    elif chimuc.isdigit() and len(chimuc) == 1:
                        f.write(f"\n### Điều {chimuc}: {ten}\n")
                    elif '.' in chimuc or (chimuc.isdigit() and len(chimuc) > 1):
                        f.write(f"#### {chimuc}. {ten}\n")
                    else:
                        f.write(f"\n**{chimuc}.** {ten}\n")
                    
                    f.write(f"\n*Mã phân cấp: `{mapc}`*\n")
            
            print(f"✓ Đã tạo {filename} với {len(entries)} entries")

def main():
    extractor = PhapDienExtractor('jsonData.js')
    
    if not extractor.load_file():
        return
    
    if not extractor.extract_by_line():
        print("Lỗi trích xuất dữ liệu")
        return
    
    extractor.analyze_structure()
    extractor.export_sample()
    extractor.create_markdown_sample()
    
    print("\n=== HOÀN THÀNH ===")
    print("Đã phân tích thành công cấu trúc dữ liệu Pháp điển Điện tử")
    print("Dữ liệu mẫu đã được xuất ra thư mục 'output/'")

if __name__ == "__main__":
    main()
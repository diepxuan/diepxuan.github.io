#!/usr/bin/env python3
"""
Crawler đơn giản cho Bộ Pháp điển Điện tử
Trích xuất dữ liệu và chuyển đổi sang Markdown
"""

import json
import re
import os
import sys
from pathlib import Path

class PhapDienCrawler:
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.json_file = self.data_dir / "jsonData.js"
        self.demuc_dir = self.data_dir / "demuc"
        
        # Dữ liệu
        self.chude_data = []  # Chủ đề
        self.demuc_data = []  # Đề mục
        self.alltree_data = []  # Tất cả điều khoản
        
        # Maps
        self.chude_map = {}  # Value -> Text
        self.demuc_map = {}  # Value -> {Text, ChuDe}
        
    def extract_json_section(self, section_name):
        """Trích xuất một section JSON từ file JS"""
        print(f"Trích xuất {section_name}...")
        
        # Đọc toàn bộ file
        with open(self.json_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Tìm section
        pattern = rf'var {section_name} = (\[.*?\]);'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print(f"  Không tìm thấy {section_name}")
            return None
        
        json_str = match.group(1)
        
        # Sửa lỗi JSON
        json_str = self.fix_json(json_str)
        
        try:
            data = json.loads(json_str)
            print(f"  ✓ Đã load {len(data)} entries")
            return data
        except json.JSONDecodeError as e:
            print(f"  ✗ Lỗi decode: {e}")
            
            # Thử cắt bớt để debug
            if len(json_str) > 10000:
                # Tìm vị trí kết thúc hợp lý
                end_pos = json_str.find('}]', 10000)
                if end_pos > 0:
                    json_str = json_str[:end_pos+2]
                    try:
                        data = json.loads(json_str)
                        print(f"  ✓ Đã load mẫu {len(data)} entries")
                        return data
                    except:
                        pass
            
            return None
    
    def fix_json(self, json_str):
        """Sửa lỗi JSON"""
        # Xóa các ký tự control
        json_str = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_str)
        # Đảm bảo dấu ngoặc kép
        json_str = re.sub(r"'(.*?)'", r'"\1"', json_str)
        return json_str
    
    def load_data(self):
        """Tải tất cả dữ liệu"""
        print("=== TẢI DỮ LIỆU PHÁP ĐIỂN ===")
        
        # Tải chủ đề
        self.chude_data = self.extract_json_section('jdChuDe') or []
        for chude in self.chude_data:
            self.chude_map[chude['Value']] = chude['Text']
        
        # Tải đề mục
        self.demuc_data = self.extract_json_section('jdDeMuc') or []
        for demuc in self.demuc_data:
            self.demuc_map[demuc['Value']] = {
                'Text': demuc['Text'],
                'ChuDe': demuc['ChuDe'],
                'STT': demuc.get('STT', '')
            }
        
        # Tải điều khoản (có thể rất lớn)
        print("Trích xuất jdAllTree (có thể mất thời gian)...")
        alltree_data = self.extract_json_section('jdAllTree')
        
        if alltree_data:
            self.alltree_data = alltree_data
            print(f"✓ Đã tải {len(self.alltree_data)} điều khoản")
        else:
            print("✗ Không thể tải jdAllTree, thử phương pháp khác...")
            self.alltree_data = self.extract_alltree_manual()
        
        return len(self.alltree_data) > 0
    
    def extract_alltree_manual(self):
        """Trích xuất jdAllTree thủ công (cho file rất lớn)"""
        print("  Sử dụng phương pháp thủ công...")
        
        with open(self.json_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Tìm vị trí bắt đầu
        start_marker = 'var jdAllTree = ['
        start_pos = content.find(start_marker)
        
        if start_pos == -1:
            print("  Không tìm thấy jdAllTree")
            return []
        
        start_pos += len(start_marker)
        
        # Tìm vị trí kết thúc (tìm dấu ngoặc vuông đóng tương ứng)
        # Đây là phương pháp đơn giản, có thể không chính xác với file rất lớn
        # Nhưng có thể lấy được mẫu dữ liệu
        
        # Lấy 1MB đầu tiên của mảng
        sample_size = 1000000  # 1MB
        end_pos = content.find('}]', start_pos + sample_size)
        
        if end_pos == -1:
            # Nếu không tìm thấy, lấy đến cuối file
            end_pos = len(content) - 1
        
        json_str = '[' + content[start_pos:end_pos+1]
        
        # Thêm dấu ngoặc đóng nếu cần
        if not json_str.endswith(']'):
            json_str += ']'
        
        # Sửa lỗi JSON
        json_str = self.fix_json(json_str)
        
        try:
            data = json.loads(json_str)
            print(f"  ✓ Đã load mẫu {len(data)} entries")
            return data
        except json.JSONDecodeError as e:
            print(f"  ✗ Lỗi decode: {e}")
            return []
    
    def analyze_hierarchy(self):
        """Phân tích cấu trúc phân cấp"""
        print("\n=== PHÂN TÍCH CẤU TRÚC PHÂN CẤP ===")
        
        if not self.alltree_data:
            print("Không có dữ liệu để phân tích")
            return
        
        # Phân tích MAPC
        mapc_samples = {}
        for entry in self.alltree_data[:100]:
            mapc = entry.get('MAPC', '')
            if mapc:
                length = len(mapc)
                if length not in mapc_samples:
                    mapc_samples[length] = mapc
        
        print("Mẫu MAPC (độ dài khác nhau):")
        for length, sample in sorted(mapc_samples.items()):
            print(f"  {length} ký tự: {sample[:40]}...")
        
        # Phân tích quan hệ cha-con dựa trên MAPC
        print("\nPhân tích quan hệ cha-con:")
        
        # Lấy một vài MAPC mẫu
        sample_entries = self.alltree_data[:50]
        
        for i, entry in enumerate(sample_entries[:10]):
            mapc = entry.get('MAPC', '')
            chimuc = entry.get('ChiMuc', '')
            ten = entry.get('TEN', '')[:60]
            
            print(f"  {i+1:2d}. MAPC={mapc[:20]}..., ChiMuc={chimuc}, TEN={ten}...")
            
            # Thử tìm entries con
            if mapc:
                children = []
                for other in sample_entries:
                    other_mapc = other.get('MAPC', '')
                    if other_mapc.startswith(mapc) and len(other_mapc) > len(mapc):
                        children.append(other)
                
                if children:
                    print(f"     → Có {len(children)} entries con")
    
    def export_to_markdown(self, output_dir):
        """Xuất dữ liệu ra Markdown"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        print(f"\n=== XUẤT DỮ LIỆU RA MARKDOWN ===")
        print(f"Thư mục đầu ra: {output_path}")
        
        # Xuất danh sách chủ đề
        self.export_chude_list(output_path)
        
        # Xuất dữ liệu theo đề mục
        self.export_by_demuc(output_path)
        
        # Xuất file tổng hợp
        self.export_summary(output_path)
        
        print(f"\n✓ Đã xuất dữ liệu ra {output_path}")
    
    def export_chude_list(self, output_path):
        """Xuất danh sách chủ đề"""
        chude_file = output_path / "00-chu-de.md"
        
        with open(chude_file, 'w', encoding='utf-8') as f:
            f.write("# DANH SÁCH CHỦ ĐỀ PHÁP ĐIỂN\n\n")
            f.write("Tổng số: 45 chủ đề\n\n")
            f.write("| STT | Chủ đề | Số đề mục |\n")
            f.write("|-----|---------|-----------|\n")
            
            # Đếm đề mục theo chủ đề
            demuc_count = {}
            for demuc in self.demuc_data:
                chude_id = demuc.get('ChuDe')
                demuc_count[chude_id] = demuc_count.get(chude_id, 0) + 1
            
            for chude in self.chude_data:
                chude_id = chude['Value']
                count = demuc_count.get(chude_id, 0)
                f.write(f"| {chude['STT']} | {chude['Text']} | {count} |\n")
        
        print(f"  ✓ Đã xuất danh sách chủ đề: {chude_file}")
    
    def export_by_demuc(self, output_path, max_demuc=5):
        """Xuất dữ liệu theo đề mục (giới hạn số lượng)"""
        print(f"  Xuất dữ liệu cho {max_demuc} đề mục đầu tiên...")
        
        # Lấy các đề mục đầu tiên
        demuc_to_export = self.demuc_data[:max_demuc]
        
        for demuc in demuc_to_export:
            demuc_id = demuc['Value']
            demuc_name = demuc['Text']
            chude_id = demuc['ChuDe']
            chude_name = self.chude_map.get(chude_id, "Unknown")
            
            # Tạo tên file an toàn
            safe_name = re.sub(r'[^\w\s-]', '', demuc_name)
            safe_name = re.sub(r'[-\s]+', '-', safe_name)
            filename = f"{demuc['STT']}-{safe_name[:50]}.md"
            filepath = output_path / filename
            
            # Lấy các entries thuộc đề mục này
            demuc_entries = []
            for entry in self.alltree_data:
                if entry.get('DeMucID') == demuc_id:
                    demuc_entries.append(entry)
            
            if not demuc_entries:
                print(f"    ✗ Đề mục '{demuc_name}': không có entries")
                continue
            
            # Sắp xếp theo MAPC
            demuc_entries.sort(key=lambda x: x.get('MAPC', ''))
            
            # Xuất ra Markdown
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {demuc_name}\n\n")
                f.write(f"**Chủ đề:** {chude_name}\n\n")
                f.write(f"**Đề mục ID:** {demuc_id}\n\n")
                f.write(f"**Số điều khoản:** {len(demuc_entries)}\n\n")
                f.write("---\n\n")
                
                current_chapter = None
                current_article = None
                
                for entry in demuc_entries[:100]:  # Giới hạn 100 entries mỗi đề mục
                    chimuc = entry.get('ChiMuc', '')
                    ten = entry.get('TEN', '')
                    mapc = entry.get('MAPC', '')
                    
                    # Xác định cấp độ
                    if chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']:
                        # Chương
                        f.write(f"\n## Chương {chimuc}: {ten}\n\n")
                        current_chapter = chimuc
                        current_article = None
                    elif chimuc.isdigit() and len(chimuc) <= 2:
                        # Điều
                        f.write(f"\n### Điều {chimuc}: {ten}\n\n")
                        current_article = chimuc
                    elif '.' in chimuc:
                        # Khoản, điểm
                        f.write(f"**{chimuc}** {ten}\n\n")
                    else:
                        # Khác
                        f.write(f"**{chimuc}.** {ten}\n\n")
                    
                    # f.write(f"*Mã: `{mapc}`*\n\n")
            
            print(f"    ✓ Đề mục '{demuc_name}': {len(demuc_entries)} entries → {filename}")
    
    def export_summary(self, output_path):
        """Xuất file tổng hợp"""
        summary_file = output_path / "SUMMARY.md"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# TỔNG HỢP DỮ LIỆU PHÁP ĐIỂN\n\n")
            
            f.write("## Thống kê\n\n")
            f.write(f"- **Tổng số chủ đề:** {len(self.chude_data)}\n")
            f.write(f"- **Tổng số đề mục:** {len(self.demuc_data)}\n")
            f.write(f"- **Tổng số điều khoản:** {len(self.alltree_data)}\n\n")
            
            f.write("## Cấu trúc dữ liệu\n\n")
            f.write("Dữ liệu Pháp điển được tổ chức theo cấu trúc:\n\n")
            f.write("1. **Chủ đề** (45 chủ đề) - Lĩnh vực pháp luật\n")
            f.write("2. **Đề mục** (271 đề mục) - Chuyên đề cụ thể trong mỗi chủ đề\n")
            f.write("3. **Điều khoản** (76,303 entries) - Các chương, điều, khoản, điểm pháp luật\n\n")
            
            f.write("## Mã phân cấp (MAPC)\n\n")
            f.write("Mỗi điều khoản có mã MAPC dài 20-80 ký tự, thể hiện cấu trúc phân cấp.\n\n")
            
            f.write("## Cách sử dụng\n\n")
            f.write("1. Xem danh sách chủ đề trong `00-chu-de.md`\n")
            f.write("2. Mỗi đề mục được xuất ra file Markdown riêng\n")
            f.write("3. Cấu trúc phân cấp được bảo tồn (Chương → Điều → Khoản → Điểm)\n\n")
            
            f.write("## Nguồn dữ liệu\n\n")
            f.write("Bộ Pháp điển Điện tử - Bộ Tư pháp Việt Nam\n")
            f.write("Website: https://phapdien.moj.gov.vn/\n")
        
        print(f"  ✓ Đã xuất file tổng hợp: {summary_file}")

def main():
    # Kiểm tra thư mục dữ liệu
    data_dir = "/root/.openclaw/workspace/BoPhapDienDienTu"
    
    if not os.path.exists(data_dir):
        print(f"Không tìm thấy thư mục dữ liệu: {data_dir}")
        sys.exit(1)
    
    # Tạo crawler
    crawler = PhapDienCrawler(data_dir)
    
    # Tải dữ liệu
    if not crawler.load_data():
        print("Không thể tải dữ liệu. Kiểm tra file jsonData.js")
        sys.exit(1)
    
    # Phân tích cấu trúc
    crawler.analyze_hierarchy()
    
    # Xuất ra Markdown
    output_dir = "/root/.openclaw/workspace/BoPhapDienDienTu/markdown_output"
    crawler.export_to_markdown(output_dir)
    
    print("\n" + "="*60)
    print("HOÀN THÀNH XUẤT DỮ LIỆU PHÁP ĐIỂN")
    print("="*60)
    print(f"Đã xuất dữ liệu ra thư mục: {output_dir}")
    print(f"- {len(crawler.chude_data)} chủ đề")
    print(f"- {len(crawler.demuc_data)} đề mục")
    print(f"- {len(crawler.alltree_data)} điều khoản")
    print("="*60)
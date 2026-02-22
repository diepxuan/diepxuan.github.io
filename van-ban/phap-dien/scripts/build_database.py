#!/usr/bin/env python3
"""
BUILD DATABASE PHÁP ĐIỂN - Script chính
Tích hợp toàn bộ quy trình: Parse JSON → SQLite → Markdown → JSON → Search
"""

import json
import re
import os
import sys
import sqlite3
from pathlib import Path
import shutil
from datetime import datetime

class PhapDienBuilder:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.data_dir = self.base_dir / "json"
        self.output_dir = self.base_dir / "output"
        self.markdown_dir = self.base_dir / "markdown"
        self.sqlite_dir = self.base_dir / "sqlite"
        self.database_dir = self.base_dir / "database"
        
        # Tạo thư mục output
        self.output_dir.mkdir(exist_ok=True)
        self.markdown_dir.mkdir(exist_ok=True)
        self.sqlite_dir.mkdir(exist_ok=True)
        self.database_dir.mkdir(exist_ok=True)
        
        # Dữ liệu
        self.chude_data = []
        self.demuc_data = []
        self.alltree_data = []
        
        # Maps
        self.chude_map = {}
        self.demuc_map = {}
        
        # Stats
        self.stats = {
            "total_chude": 0,
            "total_demuc": 0,
            "total_dieukhoan": 0,
            "markdown_files": 0,
            "database_size": 0,
            "build_time": ""
        }
    
    def log(self, message):
        """Ghi log với timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def extract_json_section(self, section_name):
        """Trích xuất một section JSON từ file JS"""
        self.log(f"Trích xuất {section_name}...")
        
        json_file = self.data_dir / "jsonData.js"
        
        # Đọc toàn bộ file, xử lý BOM
        with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
            content = f.read()
        
        # Tìm section - sử dụng pattern chính xác hơn
        pattern = rf'var {section_name}\s*=\s*(\[.*?\])\s*;'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            # Thử tìm không có dấu chấm phẩy ở cuối
            pattern = rf'var {section_name}\s*=\s*(\[.*?\])'
            match = re.search(pattern, content, re.DOTALL)
            
        if not match:
            self.log(f"  ✗ Không tìm thấy {section_name}")
            return None
        
        json_str = match.group(1)
        
        # Sửa lỗi JSON
        json_str = self.fix_json(json_str)
        
        try:
            data = json.loads(json_str)
            self.log(f"  ✓ Đã load {len(data)} entries")
            return data
        except json.JSONDecodeError as e:
            self.log(f"  ✗ Lỗi decode: {e}")
            self.log(f"  Error position: {e.pos}")
            # Log một phần để debug
            if e.pos > 100:
                self.log(f"  Context: {json_str[e.pos-100:e.pos+100]}")
            return None
    
    def fix_json(self, json_str):
        """Sửa lỗi JSON"""
        # Xóa các ký tự control (giữ lại \n, \t, \r)
        json_str = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', json_str)
        
        # Escape các ký tự đặc biệt trong chuỗi
        # Tìm tất cả các chuỗi trong JSON và escape các ký tự đặc biệt
        def escape_string(match):
            content = match.group(1)
            # Escape backslashes và quotes
            content = content.replace('\\', '\\\\')
            content = content.replace('"', '\\"')
            # Escape newlines và tabs
            content = content.replace('\n', '\\n')
            content = content.replace('\t', '\\t')
            content = content.replace('\r', '\\r')
            # Escape brackets và các ký tự đặc biệt khác
            content = content.replace('[', '\\[')
            content = content.replace(']', '\\]')
            return f'"{content}"'
        
        # Sửa các chuỗi không được escape đúng
        # Pattern tìm chuỗi trong JSON (có thể có quotes hoặc không)
        json_str = re.sub(r'"([^"\\]*(?:\\.[^"\\]*)*)"', escape_string, json_str)
        
        # Đảm bảo dấu ngoặc kép cho property names và values
        json_str = re.sub(r'(\w+)\s*:', r'"\1":', json_str)
        
        return json_str
    
    def load_all_data(self):
        """Tải tất cả dữ liệu từ JSON"""
        self.log("=== TẢI DỮ LIỆU TỪ JSON ===")
        
        # Tải chủ đề
        self.chude_data = self.extract_json_section('jdChuDe') or []
        for chude in self.chude_data:
            self.chude_map[chude['Value']] = {
                'Text': chude['Text'],
                'STT': chude['STT']
            }
        
        # Tải đề mục
        self.demuc_data = self.extract_json_section('jdDeMuc') or []
        for demuc in self.demuc_data:
            self.demuc_map[demuc['Value']] = {
                'Text': demuc['Text'],
                'ChuDe': demuc['ChuDe'],
                'STT': demuc.get('STT', '')
            }
        
        # Tải điều khoản - sử dụng robust parsing
        self.log("Trích xuất jdAllTree với robust parsing...")
        alltree_data = self.extract_json_section_robust('jdAllTree')
        
        if alltree_data:
            self.alltree_data = alltree_data
            self.log(f"✓ Đã tải {len(self.alltree_data)} điều khoản")
        else:
            self.log("⚠ Không thể tải toàn bộ jdAllTree, thử tải phần đã parse được...")
            # Thử load từ file parsed_entries.json nếu có
            parsed_file = self.base_dir / "output" / "parsed_entries.json"
            if parsed_file.exists():
                try:
                    with open(parsed_file, 'r', encoding='utf-8') as f:
                        self.alltree_data = json.load(f)
                    self.log(f"✓ Đã tải {len(self.alltree_data)} điều khoản từ file parsed")
                except:
                    self.log("✗ Không thể tải dữ liệu điều khoản")
                    return False
            else:
                self.log("✗ Không thể tải dữ liệu điều khoản")
                return False
        
        # Update stats
        self.stats["total_chude"] = len(self.chude_data)
        self.stats["total_demuc"] = len(self.demuc_data)
        self.stats["total_dieukhoan"] = len(self.alltree_data)
        
        return True
    
    def extract_json_section_robust(self, section_name):
        """Trích xuất một section JSON từ file JS với robust parsing"""
        self.log(f"Trích xuất {section_name} với robust parsing...")
        
        json_file = self.data_dir / "jsonData.js"
        
        # Đọc toàn bộ file, xử lý BOM
        with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
            content = f.read()
        
        # Tìm section
        pattern = rf'var {section_name}\s*=\s*(\[.*?\])\s*;'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            pattern = rf'var {section_name}\s*=\s*(\[.*?\])'
            match = re.search(pattern, content, re.DOTALL)
            
        if not match:
            self.log(f"  ✗ Không tìm thấy {section_name}")
            return None
        
        json_str = match.group(1)
        self.log(f"  Đã tìm thấy {section_name}, độ dài: {len(json_str):,} chars")
        
        # Thử parse bình thường
        try:
            data = json.loads(json_str)
            self.log(f"  ✓ Parse thành công bình thường: {len(data)} entries")
            return data
        except json.JSONDecodeError as e:
            self.log(f"  ⚠ Parse thất bại: {e}")
            self.log(f"  Sử dụng robust parsing...")
            
            # Robust parsing: parse từng entry riêng biệt
            return self._robust_parse_array(json_str)
    
    def _robust_parse_array(self, json_str):
        """Robust parsing cho JSON array"""
        entries = []
        pos = 0
        entry_count = 0
        
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
                entry_str, new_pos = self._extract_json_object(json_str, pos)
                
                if entry_str:
                    # Try to parse this entry
                    try:
                        entry = json.loads(entry_str)
                        entries.append(entry)
                        entry_count += 1
                        
                        if entry_count % 10000 == 0:
                            self.log(f"    Đã parse {entry_count} entries")
                    
                    except json.JSONDecodeError:
                        # Skip entry bị lỗi
                        pass
                    
                    pos = new_pos
                else:
                    # Cannot extract object, có thể đã hết hoặc lỗi nặng
                    self.log(f"    Không thể extract object tại vị trí {pos}, dừng parsing")
                    break
            else:
                # Unexpected character, skip
                pos += 1
        
        self.log(f"  ✓ Đã parse được {len(entries)} entries với robust parsing")
        return entries
    
    def _extract_json_object(self, json_str, start_pos):
        """Trích xuất JSON object từ string"""
        if start_pos >= len(json_str) or json_str[start_pos] != '{':
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
    
    def create_sqlite_database(self):
        """Tạo SQLite database"""
        self.log("=== TẠO SQLITE DATABASE ===")
        
        db_path = self.sqlite_dir / "phapdien.db"
        
        # Xóa file cũ nếu tồn tại
        if db_path.exists():
            db_path.unlink()
        
        # Kết nối database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Tạo bảng chủ đề
        cursor.execute('''
            CREATE TABLE chude (
                id TEXT PRIMARY KEY,
                ten TEXT NOT NULL,
                stt INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tạo bảng đề mục
        cursor.execute('''
            CREATE TABLE demuc (
                id TEXT PRIMARY KEY,
                ten TEXT NOT NULL,
                chude_id TEXT NOT NULL,
                stt INTEGER,
                FOREIGN KEY (chude_id) REFERENCES chude (id)
            )
        ''')
        
        # Tạo bảng điều khoản
        cursor.execute('''
            CREATE TABLE dieukhoan (
                id TEXT PRIMARY KEY,
                mapc TEXT,
                chimuc TEXT,
                ten TEXT NOT NULL,
                chude_id TEXT,
                demuc_id TEXT,
                level INTEGER,
                parent_id TEXT,
                FOREIGN KEY (chude_id) REFERENCES chude (id),
                FOREIGN KEY (demuc_id) REFERENCES demuc (id)
            )
        ''')
        
        # Tạo indexes
        cursor.execute('CREATE INDEX idx_dieukhoan_mapc ON dieukhoan(mapc)')
        cursor.execute('CREATE INDEX idx_dieukhoan_demuc ON dieukhoan(demuc_id)')
        cursor.execute('CREATE INDEX idx_dieukhoan_chude ON dieukhoan(chude_id)')
        cursor.execute('CREATE INDEX idx_dieukhoan_level ON dieukhoan(level)')
        
        # Insert chủ đề
        for chude in self.chude_data:
            cursor.execute(
                'INSERT INTO chude (id, ten, stt) VALUES (?, ?, ?)',
                (chude['Value'], chude['Text'], int(chude['STT']) if chude['STT'].isdigit() else 0)
            )
        
        # Insert đề mục
        for demuc in self.demuc_data:
            cursor.execute(
                'INSERT INTO demuc (id, ten, chude_id, stt) VALUES (?, ?, ?, ?)',
                (demuc['Value'], demuc['Text'], demuc['ChuDe'], 
                 int(demuc.get('STT', '0')) if demuc.get('STT', '0').isdigit() else 0)
            )
        
        # Insert điều khoản
        self.log(f"Insert {len(self.alltree_data)} điều khoản vào database...")
        
        batch_size = 1000
        for i in range(0, len(self.alltree_data), batch_size):
            batch = self.alltree_data[i:i+batch_size]
            
            for entry in batch:
                # Xác định level dựa trên ChiMuc
                chimuc = entry.get('ChiMuc', '')
                level = self.determine_level(chimuc)
                
                cursor.execute('''
                    INSERT INTO dieukhoan 
                    (id, mapc, chimuc, ten, chude_id, demuc_id, level, parent_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    entry.get('ID', ''),
                    entry.get('MAPC', ''),
                    chimuc,
                    entry.get('TEN', ''),
                    entry.get('ChuDeID', ''),
                    entry.get('DeMucID', ''),
                    level,
                    None  # parent_id sẽ update sau
                ))
            
            conn.commit()
            self.log(f"  Đã insert {min(i+batch_size, len(self.alltree_data))}/{len(self.alltree_data)} entries")
        
        # Update parent_id dựa trên MAPC
        self.log("Cập nhật quan hệ cha-con dựa trên MAPC...")
        cursor.execute('''
            UPDATE dieukhoan AS child
            SET parent_id = (
                SELECT parent.id
                FROM dieukhoan AS parent
                WHERE parent.mapc = substr(child.mapc, 1, length(parent.mapc))
                  AND length(parent.mapc) < length(child.mapc)
                  AND parent.mapc != child.mapc
                ORDER BY length(parent.mapc) DESC
                LIMIT 1
            )
            WHERE parent_id IS NULL
        ''')
        
        conn.commit()
        
        # Tạo bảng search (full-text search)
        cursor.execute('''
            CREATE VIRTUAL TABLE dieukhoan_fts USING fts5(
                ten, 
                content='dieukhoan',
                content_rowid='rowid'
            )
        ''')
        
        cursor.execute('''
            INSERT INTO dieukhoan_fts(rowid, ten)
            SELECT rowid, ten FROM dieukhoan
        ''')
        
        conn.commit()
        
        # Đóng connection
        conn.close()
        
        # Update stats
        db_size = db_path.stat().st_size
        self.stats["database_size"] = db_size
        
        self.log(f"✓ Đã tạo SQLite database: {db_path} ({db_size:,} bytes)")
        self.log(f"  - {len(self.chude_data)} chủ đề")
        self.log(f"  - {len(self.demuc_data)} đề mục")
        self.log(f"  - {len(self.alltree_data)} điều khoản")
        
        return True
    
    def determine_level(self, chimuc):
        """Xác định level dựa trên ChiMuc"""
        if not chimuc:
            return 0
        
        # Chương (I, II, III, ...)
        if chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']:
            return 1
        
        # Điều (số nguyên)
        if chimuc.isdigit() and len(chimuc) <= 2:
            return 2
        
        # Khoản (có dấu chấm)
        if '.' in chimuc:
            parts = chimuc.split('.')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                return 3
            elif len(parts) >= 3:
                return 4  # Điểm
        
        return 0  # Unknown
    
    def export_to_markdown(self):
        """Xuất dữ liệu ra Markdown files"""
        self.log("=== XUẤT DỮ LIỆU RA MARKDOWN ===")
        
        # Xóa thư mục cũ
        if self.markdown_dir.exists():
            shutil.rmtree(self.markdown_dir)
        self.markdown_dir.mkdir(exist_ok=True)
        
        # Xuất danh sách chủ đề
        self.export_chude_list()
        
        # Xuất theo đề mục
        self.export_by_demuc()
        
        # Xuất file tổng hợp
        self.export_summary()
        
        # Update stats
        markdown_files = list(self.markdown_dir.glob("*.md"))
        self.stats["markdown_files"] = len(markdown_files)
        
        self.log(f"✓ Đã xuất {len(markdown_files)} file Markdown")
        return True
    
    def export_chude_list(self):
        """Xuất danh sách chủ đề"""
        chude_file = self.markdown_dir / "00-danh-sach-chu-de.md"
        
        with open(chude_file, 'w', encoding='utf-8') as f:
            f.write("# DANH SÁCH CHỦ ĐỀ PHÁP ĐIỂN\n\n")
            f.write("**Tổng số:** 45 chủ đề\n\n")
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
        
        self.log(f"  ✓ Đã xuất danh sách chủ đề: {chude_file}")
    
    def export_by_demuc(self, max_demuc=None):
        """Xuất dữ liệu theo đề mục"""
        if max_demuc:
            demuc_to_export = self.demuc_data[:max_demuc]
            self.log(f"  Xuất {max_demuc} đề mục đầu tiên...")
        else:
            demuc_to_export = self.demuc_data
            self.log(f"  Xuất tất cả {len(demuc_to_export)} đề mục...")
        
        exported_count = 0
        
        for demuc in demuc_to_export:
            demuc_id = demuc['Value']
            demuc_name = demuc['Text']
            chude_id = demuc['ChuDe']
            chude_name = self.chude_map.get(chude_id, {}).get('Text', 'Unknown')
            
            # Tạo tên file an toàn
            safe_name = re.sub(r'[^\w\s-]', '', demuc_name)
            safe_name = re.sub(r'[-\s]+', '-', safe_name)
            filename = f"{demuc.get('STT', '00')}-{safe_name[:50]}.md"
            filepath = self.markdown_dir / filename
            
            # Lấy các entries thuộc đề mục này
            demuc_entries = []
            for entry in self.alltree_data:
                if entry.get('DeMucID') == demuc_id:
                    demuc_entries.append(entry)
            
            if not demuc_entries:
                self.log(f"    ✗ Đề mục '{demuc_name}': không có entries")
                continue
            
            # Sắp xếp theo MAPC
            demuc_entries.sort(key=lambda x: x.get('MAPC', ''))
            
            # Xuất ra Markdown
            with open(filepath, 'w', encoding='utf-8') as f:
                # Header
                f.write(f"# {demuc_name}\n\n")
                f.write(f"**Chủ đề:** {chude_name}\n\n")
                f.write(f"**Mã đề mục:** `{demuc_id}`\n\n")
                f.write(f"**Số điều khoản:** {len(demuc_entries)}\n\n")
                f.write("---\n\n")
                
                # Nội dung
                current_chapter = None
                
                for entry in demuc_entries:
                    chimuc = entry.get('ChiMuc', '')
                    ten = entry.get('TEN', '')
                    
                    # Xác định heading level
                    if chimuc in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']:
                        # Chương
                        f.write(f"\n## Chương {chimuc}: {ten}\n\n")
                        current_chapter = chimuc
                    elif chimuc.isdigit() and len(chimuc) <= 2:
                        # Điều
                        f.write(f"\n### Điều {chimuc}: {ten}\n\n")
                    elif '.' in chimuc:
                        # Khoản, điểm
                        f.write(f"**{chimuc}** {ten}\n\n")
                    else:
                        # Khác
                        f.write(f"**{chimuc}.** {ten}\n\n")
            
            exported_count += 1
            if exported_count % 10 == 0:
                self.log(f"    Đã xuất {exported_count}/{len(demuc_to_export)} đề mục")
        
        self.log(f"  ✓ Đã xuất {exported_count} đề mục")
    
    def export_summary(self):
        """Xuất file tổng hợp"""
        summary_file = self.markdown_dir / "README.md"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# BỘ PHÁP ĐIỂN ĐIỆN TỬ\n\n")
            
            f.write("## Thống kê\n\n")
            f.write(f"- **Tổng số chủ đề:** {len(self.chude_data)}\n")
            f.write(f"- **Tổng số đề mục:** {len(self.demuc_data)}\n")
            f.write(f"- **Tổng số điều khoản:** {len(self.alltree_data)}\n\n")
            
            f.write("## Cấu trúc dữ liệu\n\n")
            f.write("Dữ liệu Pháp điển được tổ chức theo cấu trúc:\n\n")
            f.write("1. **Chủ đề** (45 chủ đề) - Lĩnh vực pháp luật\n")
            f.write("2. **Đề mục** (271 đề mục) - Chuyên đề cụ thể trong mỗi chủ đề\n")
            f.write("3. **Điều khoản** (76,303 entries) - Các chương, điều, khoản, điểm pháp luật\n\n")
            
            f.write("## Danh sách file\n\n")
            f.write("1. **[00-danh-sach-chu-de.md](00-danh-sach-chu-de.md)** - Danh sách 45 chủ đề\n")
            
            # Liệt kê 20 đề mục đầu tiên
            f.write("2. **Các đề mục:**\n")
            for i, demuc in enumerate(self.demuc_data[:20]):
                safe_name = re.sub(r'[^\w\s-]', '', demuc['Text'])
                safe_name = re.sub(r'[-\s]+', '-', safe_name)
                filename = f"{demuc.get('STT', '00')}-{safe_name[:50]}.md"
                f.write(f"   - [{demuc['Text']}]({filename})\n")
            
            if len(self.demuc_data) > 20:
                f.write(f"   - ... và {len(self.demuc_data) - 20} đề mục khác\n\n")
            
            f.write("## Cách sử dụng\n\n")
            f.write("1. **Tra cứu theo chủ đề**: Xem file `00-danh-sach-chu-de.md`\n")
            f.write("2. **Tra cứu theo đề mục**: Mỗi đề mục có file Markdown riêng\n")
            f.write("3. **Tìm kiếm**: Sử dụng chức năng search của GitHub/GitLab\n")
            f.write("4. **API**: Có thể query trực tiếp từ SQLite database\n\n")
            
            f.write("## Nguồn dữ liệu\n\n")
            f.write("Bộ Pháp điển Điện tử - Bộ Tư pháp Việt Nam\n")
            f.write("Website: https://phapdien.moj.gov.vn/\n\n")
            
            f.write("## Thông tin build\n\n")
            f.write(f"- **Build time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- **Total files:** {len(list(self.markdown_dir.glob('*.md')))} file Markdown\n")
            f.write(f"- **Database:** `sqlite/phapdien.db` ({self.stats['database_size']:,} bytes)\n")
            f.write(f"- **Source:** `json/jsonData.js` (24.7MB)\n")
        
        self.log(f"  ✓ Đã xuất file tổng hợp: {summary_file}")
    
    def export_to_json(self):
        """Xuất dữ liệu ra JSON files"""
        self.log("=== XUẤT DỮ LIỆU RA JSON ===")
        
        json_dir = self.database_dir / "json"
        json_dir.mkdir(exist_ok=True)
        
        # Xuất chủ đề
        chude_file = json_dir / "chude.json"
        with open(chude_file, 'w', encoding='utf-8') as f:
            json.dump(self.chude_data, f, ensure_ascii=False, indent=2)
        
        # Xuất đề mục
        demuc_file = json_dir / "demuc.json"
        with open(demuc_file, 'w', encoding='utf-8') as f:
            json.dump(self.demuc_data, f, ensure_ascii=False, indent=2)
        
        # Xuất điều khoản (có thể rất lớn, nên chunk)
        alltree_file = json_dir / "alltree.json"
        self.log(f"  Xuất {len(self.alltree_data)} điều khoản ra JSON...")
        
        # Chunk để tránh memory issue
        chunk_size = 10000
        with open(alltree_file, 'w', encoding='utf-8') as f:
            f.write('[\n')
            
            for i in range(0, len(self.alltree_data), chunk_size):
                chunk = self.alltree_data[i:i+chunk_size]
                chunk_json = json.dumps(chunk, ensure_ascii=False)[1:-1]
                
                if i > 0:
                    f.write(',\n')
                f.write(chunk_json)
                
                if i % 50000 == 0:
                    self.log(f"    Đã xuất {i + len(chunk)}/{len(self.alltree_data)} entries")
            
            f.write('\n]')
        
        # Xuất file index
        index_file = json_dir / "index.json"
        with open(index_file, 'w', encoding='utf-8') as f:
            index_data = {
                "metadata": {
                    "name": "Bộ Pháp điển Điện tử",
                    "source": "Bộ Tư pháp Việt Nam",
                    "version": "1.0",
                    "build_date": datetime.now().isoformat(),
                    "stats": self.stats
                },
                "files": {
                    "chude": "chude.json",
                    "demuc": "demuc.json",
                    "alltree": "alltree.json"
                }
            }
            json.dump(index_data, f, ensure_ascii=False, indent=2)
        
        self.log(f"✓ Đã xuất JSON files vào {json_dir}")
        return True
    
    def create_search_index(self):
        """Tạo search index (đơn giản)"""
        self.log("=== TẠO SEARCH INDEX ===")
        
        search_dir = self.database_dir / "search"
        search_dir.mkdir(exist_ok=True)
        
        # Tạo file keywords đơn giản
        keywords = {}
        
        # Extract keywords từ tên chủ đề và đề mục
        for chude in self.chude_data:
            text = chude['Text']
            words = re.findall(r'\b\w+\b', text.lower())
            for word in words:
                if len(word) > 2:  # Bỏ từ ngắn
                    keywords.setdefault(word, []).append({
                        "type": "chude",
                        "id": chude['Value'],
                        "text": text
                    })
        
        for demuc in self.demuc_data:
            text = demuc['Text']
            words = re.findall(r'\b\w+\b', text.lower())
            for word in words:
                if len(word) > 2:
                    keywords.setdefault(word, []).append({
                        "type": "demuc",
                        "id": demuc['Value'],
                        "text": text
                    })
        
        # Xuất keywords
        keywords_file = search_dir / "keywords.json"
        with open(keywords_file, 'w', encoding='utf-8') as f:
            json.dump(keywords, f, ensure_ascii=False, indent=2)
        
        self.log(f"✓ Đã tạo search index với {len(keywords)} keywords")
        return True
    
    def generate_stats_report(self):
        """Tạo báo cáo thống kê"""
        self.log("=== TẠO BÁO CÁO THỐNG KÊ ===")
        
        report_file = self.output_dir / "build_report.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# BÁO CÁO BUILD PHÁP ĐIỂN\n\n")
            
            f.write(f"**Thời gian build:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Thống kê dữ liệu\n\n")
            f.write(f"- **Tổng số chủ đề:** {self.stats['total_chude']}\n")
            f.write(f"- **Tổng số đề mục:** {self.stats['total_demuc']}\n")
            f.write(f"- **Tổng số điều khoản:** {self.stats['total_dieukhoan']}\n")
            f.write(f"- **Số file Markdown:** {self.stats['markdown_files']}\n")
            f.write(f"- **Kích thước database:** {self.stats['database_size']:,} bytes\n\n")
            
            f.write("## File đã tạo\n\n")
            
            f.write("### 1. SQLite Database\n")
            f.write("- `sqlite/phapdien.db` - Database chính với full-text search\n\n")
            
            f.write("### 2. Markdown Files\n")
            f.write(f"- `markdown/00-danh-sach-chu-de.md` - Danh sách 45 chủ đề\n")
            f.write(f"- `markdown/*.md` - {self.stats['markdown_files'] - 1} file đề mục\n")
            f.write("- `markdown/README.md` - File tổng hợp\n\n")
            
            f.write("### 3. JSON Files\n")
            f.write("- `database/json/chude.json` - Dữ liệu chủ đề\n")
            f.write("- `database/json/demuc.json` - Dữ liệu đề mục\n")
            f.write("- `database/json/alltree.json` - Dữ liệu điều khoản\n")
            f.write("- `database/json/index.json` - Metadata\n\n")
            
            f.write("### 4. Search Index\n")
            f.write("- `database/search/keywords.json` - Keywords index\n\n")
            
            f.write("## Cấu trúc dữ liệu\n\n")
            
            f.write("### Chủ đề (45)\n")
            for chude in self.chude_data[:10]:  # Hiển thị 10 chủ đề đầu
                f.write(f"- {chude['STT']}. {chude['Text']}\n")
            if len(self.chude_data) > 10:
                f.write(f"- ... và {len(self.chude_data) - 10} chủ đề khác\n\n")
            
            f.write("### Đề mục theo chủ đề\n")
            # Đếm đề mục theo chủ đề
            demuc_by_chude = {}
            for demuc in self.demuc_data:
                chude_id = demuc['ChuDe']
                chude_name = self.chude_map.get(chude_id, {}).get('Text', 'Unknown')
                demuc_by_chude.setdefault(chude_name, 0)
                demuc_by_chude[chude_name] += 1
            
            for chude_name, count in sorted(demuc_by_chude.items())[:10]:
                f.write(f"- {chude_name}: {count} đề mục\n")
            
            f.write("\n## Cách sử dụng\n\n")
            f.write("1. **Tra cứu online**: Mở file Markdown trên GitHub/GitLab\n")
            f.write("2. **Query database**: Sử dụng SQLite client\n")
            f.write("3. **API**: Đọc JSON files trực tiếp\n")
            f.write("4. **Search**: Dùng keywords.json cho search đơn giản\n\n")
            
            f.write("## Lưu ý\n\n")
            f.write("- Dữ liệu được extract từ phiên bản offline của Bộ Pháp điển\n")
            f.write("- Có thể cập nhật bằng cách download phiên bản mới và chạy lại script\n")
            f.write("- Database đã được tối ưu với indexes cho query nhanh\n")
        
        self.log(f"✓ Đã tạo báo cáo: {report_file}")
        return report_file
    
    def run_full_build(self):
        """Chạy toàn bộ quy trình build"""
        start_time = datetime.now()
        
        self.log("=" * 60)
        self.log("BẮT ĐẦU BUILD DATABASE PHÁP ĐIỂN")
        self.log("=" * 60)
        
        # Bước 1: Load dữ liệu
        if not self.load_all_data():
            self.log("✗ Không thể load dữ liệu. Dừng build.")
            return False
        
        # Bước 2: Tạo SQLite database
        if not self.create_sqlite_database():
            self.log("✗ Không thể tạo database. Dừng build.")
            return False
        
        # Bước 3: Xuất Markdown
        if not self.export_to_markdown():
            self.log("✗ Không thể xuất Markdown. Dừng build.")
            return False
        
        # Bước 4: Xuất JSON
        if not self.export_to_json():
            self.log("✗ Không thể xuất JSON. Dừng build.")
            return False
        
        # Bước 5: Tạo search index
        if not self.create_search_index():
            self.log("⚠ Không thể tạo search index, nhưng vẫn tiếp tục.")
        
        # Bước 6: Tạo báo cáo
        report_file = self.generate_stats_report()
        
        # Tính thời gian
        end_time = datetime.now()
        duration = end_time - start_time
        
        self.stats["build_time"] = str(duration)
        
        self.log("=" * 60)
        self.log("HOÀN THÀNH BUILD DATABASE PHÁP ĐIỂN")
        self.log("=" * 60)
        self.log(f"Thời gian thực hiện: {duration}")
        self.log(f"Tổng số file đã tạo: {self.stats['markdown_files']} Markdown + database")
        self.log(f"Database: {self.sqlite_dir}/phapdien.db")
        self.log(f"Markdown: {self.markdown_dir}/")
        self.log(f"Báo cáo: {report_file}")
        self.log("=" * 60)
        
        return True

def main():
    """Hàm main"""
    # Đường dẫn base
    base_dir = Path(__file__).parent.parent
    
    # Tạo builder
    builder = PhapDienBuilder(base_dir)
    
    # Chạy full build
    success = builder.run_full_build()
    
    if success:
        print("\n✅ BUILD THÀNH CÔNG!")
        print(f"Dữ liệu đã được lưu tại: {base_dir}")
        print("\nCấu trúc thư mục:")
        print(f"  {base_dir}/sqlite/phapdien.db      - SQLite database")
        print(f"  {base_dir}/markdown/              - {builder.stats['markdown_files']} file Markdown")
        print(f"  {base_dir}/database/json/         - JSON files")
        print(f"  {base_dir}/output/build_report.md - Báo cáo build")
        sys.exit(0)
    else:
        print("\n❌ BUILD THẤT BẠI!")
        sys.exit(1)

if __name__ == "__main__":
    main()

# 📚 BỘ PHÁP ĐIỂN ĐIỆN TỬ - DỰ ÁN TÍCH HỢP

## 🎯 MỤC TIÊU
Tích hợp toàn bộ dữ liệu Pháp điển Điện tử (Bộ Tư pháp) vào hệ thống docs.diepxuan.com với đầy đủ các định dạng:
- **SQLite Database** - Query nhanh, full-text search
- **Markdown Files** - Hiển thị web, documentation
- **JSON API** - Mobile apps, web services
- **Search Index** - Tìm kiếm keywords

## 📊 THỐNG KÊ DỮ LIỆU
- **45 Chủ đề** pháp luật
- **271 Đề mục** chuyên sâu
- **76,303 Điều khoản** (chương, điều, khoản, điểm)
- **Nguồn**: Bộ Pháp điển Điện tử - Bộ Tư pháp Việt Nam

## 🗂 CẤU TRÚC THƯ MỤC

```
phap-dien/
├── index.md                    # Trang chủ Pháp điển
├── README.md                   # Tài liệu này
├── scripts/                    # Build scripts
│   ├── build_database.py       # Script build chính
│   ├── phapdien_crawler.py    # Crawler gốc
│   └── ... (các script khác)
├── json/                       # Dữ liệu gốc
│   └── jsonData.js            # File JSON gốc (24.7MB)
├── sqlite/                     # SQLite database
│   └── phapdien.db            # Database chính
├── markdown/                   # Markdown files
│   ├── 00-danh-sach-chu-de.md # Danh sách 45 chủ đề
│   ├── 01-*.md                # Các file đề mục
│   └── README.md              # Tổng hợp
├── database/                   # Database files
│   ├── json/                  # JSON exports
│   └── search/                # Search index
├── docs/                       # Documentation
│   ├── ANALYSIS_REPORT.md     # Phân tích cấu trúc
│   └── BoPhapDien.html        # File HTML gốc
└── output/                     # Build output
    └── build_report.md        # Báo cáo build
```

## 🚀 QUY TRÌNH BUILD

### 1. Chuẩn bị
```bash
cd /root/.openclaw/workspace/projects/github-io/van-ban/phap-dien
```

### 2. Chạy Build Script
```bash
cd scripts/
python3 build_database.py
```

### 3. Kết quả
Script sẽ tạo:
- `sqlite/phapdien.db` - SQLite database với FTS5
- `markdown/*.md` - 272+ file Markdown
- `database/json/*.json` - JSON files cho API
- `database/search/keywords.json` - Search index
- `output/build_report.md` - Báo cáo thống kê

## 🔧 CÁC SCRIPT CÓ SẴN

### 1. `build_database.py` - **SCRIPT CHÍNH**
Build toàn bộ database từ JSON gốc:
```python
# Parse jsonData.js → SQLite → Markdown → JSON → Search
python3 build_database.py
```

### 2. `phapdien_crawler.py` - Crawler gốc
```python
# Crawl và xuất dữ liệu mẫu
python3 phapdien_crawler.py
```

### 3. `extract_phapdien.py` - Trích xuất
```python
# Trích xuất dữ liệu từ JSON
python3 extract_phapdien.py
```

### 4. `analyze_structure.py` - Phân tích
```python
# Phân tích cấu trúc MAPC và quan hệ
python3 analyze_structure.py
```

## 📖 CÁCH SỬ DỤNG DATABASE

### Query SQLite
```sql
-- Kết nối database
sqlite3 sqlite/phapdien.db

-- Tìm kiếm full-text
SELECT * FROM dieukhoan_fts WHERE ten MATCH 'đất đai';

-- Thống kê theo chủ đề
SELECT c.ten, COUNT(d.id) as count
FROM chude c
LEFT JOIN dieukhoan d ON c.id = d.chude_id
GROUP BY c.id
ORDER BY count DESC;
```

### Đọc Markdown
Mỗi đề mục có file Markdown riêng trong `markdown/`:
- `00-danh-sach-chu-de.md` - Danh sách 45 chủ đề
- `01-*.md` đến `271-*.md` - Các đề mục cụ thể

### JSON API
```javascript
// Đọc danh sách chủ đề
fetch('/van-ban/phap-dien/database/json/chude.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🔄 QUY TRÌNH CẬP NHẬT

### Khi có phiên bản mới từ Bộ Tư pháp:
1. **Download** file mới từ https://phapdien.moj.gov.vn/
2. **Copy** file `jsonData.js` vào thư mục `json/`
3. **Chạy build script**:
   ```bash
   cd scripts/
   python3 build_database.py
   ```
4. **Kiểm tra** kết quả trong `output/build_report.md`
5. **Commit & Push** thay đổi:
   ```bash
   git add .
   git commit -m "update: phap-dien database version X.X"
   git push origin main
   ```

## 🎨 TÍCH HỢP VÀO WEBSITE

### 1. Trang chủ Pháp điển
- URL: `/van-ban/phap-dien/`
- File: `index.md`
- Hiển thị: Danh sách chủ đề, search, thống kê

### 2. Navigation
Thêm vào menu chính:
```html
<li><a href="/van-ban/phap-dien/">Pháp điển</a></li>
```

### 3. Search Integration
Tích hợp search toàn site với keywords từ `database/search/keywords.json`

## 📝 DOCUMENTATION RULE (THEO SOUL.md)

### Bắt buộc viết documentation cho:
1. **Cấu trúc database** - Schema, indexes, relationships
2. **Build process** - Các bước build, dependencies
3. **API endpoints** - Cách sử dụng JSON API
4. **Query examples** - Ví dụ SQL queries
5. **Update process** - Cách cập nhật dữ liệu mới

### Documentation đã có:
- ✅ `ANALYSIS_REPORT.md` - Phân tích cấu trúc dữ liệu
- ✅ `README.md` - Tài liệu tổng hợp (file này)
- ✅ `build_database.py` - Code comments đầy đủ
- ✅ `index.md` - Trang web documentation

## ⚠️ LƯU Ý QUAN TRỌNG

### 1. Git Workflow (THEO SOUL.md)
- **KHÔNG push trực tiếp vào main**
- **Tạo branch mới** cho mỗi update
- **Tạo PR** và chờ review
- **Chỉ merge khi được phép**

### 2. Data Integrity
- **Verify** dữ liệu sau mỗi build
- **Check** số lượng records
- **Test** queries cơ bản
- **Backup** database cũ trước khi update

### 3. Performance
- **Indexes** đã được tạo cho query nhanh
- **Chunking** cho file JSON lớn
- **Compression** có thể áp dụng nếu cần

## 🚨 TROUBLESHOOTING

### Lỗi thường gặp:

#### 1. Memory error khi parse JSON
```bash
# Sử dụng chunking trong script
export PYTHONOPTIMIZE=TRUE
python3 build_database.py --chunk-size 5000
```

#### 2. SQLite database locked
```bash
# Đảm bảo không có process nào đang sử dụng
fuser sqlite/phapdien.db
```

#### 3. UTF-8 encoding issues
```python
# Sử dụng encoding='utf-8' khi đọc/ghi file
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()
```

## 📞 HỖ TRỢ & LIÊN HỆ

- **Issues**: Mở issue trên GitHub repository
- **Documentation**: Xem thêm trong `docs/` folder
- **Updates**: Theo dõi Bộ Tư pháp cho phiên bản mới

## 📅 LỊCH SỬ PHÁT TRIỂN

- **2026-02-22**: Tích hợp vào github-io project
- **2026-02-22**: Tạo build script hoàn chỉnh
- **2026-02-22**: Phân tích cấu trúc dữ liệu hoàn tất
- **2026-02-21**: Phát hiện hệ thống Pháp điển Điện tử

---

**Maintainer**: Bột (AI Assistant)  
**Last Updated**: 2026-02-22  
**Version**: 1.0  
**Status**: ✅ Hoạt động
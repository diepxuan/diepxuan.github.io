# SCRIPTS - Van-Ban Project

## 📋 Tổng quan

Thư mục này chứa các scripts để xử lý dữ liệu văn bản pháp luật từ database MySQL.

## 🎯 Script chính (DUY NHẤT CẦN DÙNG)

### `vanban_generator.py`
**Script hợp nhất duy nhất** - Tạo markdown files từ database với cấu trúc URL đúng.

```bash
python3 vanban_generator.py
```

**Chức năng:**
1. Xoá tất cả markdown files cũ
2. Kết nối database `vbpl` và lấy dữ liệu
3. Tạo markdown files với cấu trúc:
   - Home: `/van-ban/`
   - Topic: `/van-ban/<topic-slug>/`
   - Subject: `/van-ban/<topic-slug>/<subject-slug>/`
4. Tạo backward compatibility files (files với dấu gạch dưới)

**Database connection:**
- Host: `mysql.diepxuan.corp`
- Database: `vbpl`
- User: `vbpl`
- Password: `G]9E9S_TahIFVbq-`

## 🗑️ Scripts dư thừa (CÓ THỂ XOÁ)

### Scripts import (đã hoàn thành)
- `parse_large_js.py` - Parse JSON data (đã xong)
- `ultimate_import.py` - Import data vào database (đã xong)
- `import_phapdien_data.py` - Import data (đã xong)
- `simple_import.py` - Import đơn giản (đã xong)
- `test_import.py` - Test import (đã xong)
- `final_import.py` - Import cuối cùng (đã xong)

### Scripts HTML/Markdown conversion (đã hoàn thành)
- `import_demuc_content.py` - Import HTML content (đã xong)
- `import_demuc_markdown.py` - Import markdown (đã xong)
- `import_demuc_simple.py` - Import đơn giản (đã xong)
- `import_demuc_simple_markdown.py` - Import markdown đơn giản (đã xong)
- `import_all_demuc_markdown.py` - Import tất cả markdown (đã xong)
- `import_demuc_batch.py` - Import theo batch (đã xong)
- `import_3_large_files.py` - Import files lớn (đã xong)
- `import_final_11_files.py` - Import 11 files cuối (đã xong)
- `import_missing_demuc.py` - Import thiếu (đã xong)

### Scripts markdown generation (cũ)
- `generate_vanban.py` - Script cũ (SQLite, tạo files UUID)
- `generate_vanban_mysql.py` - Script MySQL cũ
- `generate_vanban_simple.py` - Script đơn giản cũ
- `generate_vanban_optimized.py` - Script tối ưu cũ
- `generate_vanban_full.py` - Script đầy đủ cũ
- `generate_vanban_with_full_content.py` - Script với nội dung đầy đủ (đã thay thế)

### Scripts conversion (đã hoàn thành)
- `complete_markdown_conversion.py` - Chuyển đổi markdown (đã xong)
- `convert_final_batch.py` - Chuyển đổi batch cuối (đã xong)
- `convert_remaining_simple.py` - Chuyển đổi còn lại (đã xong)
- `convert_skip_large_files.py` - Bỏ qua files lớn (đã xong)
- `convert_with_retry.py` - Chuyển đổi với retry (đã xong)
- `test_markdown_conversion.py` - Test chuyển đổi (đã xong)

### Scripts update (đã hoàn thành)
- `update_dieu_khoan_full_content.py` - Update nội dung điều khoản (đã xong)
- `batch_update_dieu_khoan.py` - Update batch điều khoản (đã xong)

### Scripts cleanup (đã hoàn thành)
- `cleanup_uuid_files.py` - Xoá files UUID (đã xong)
- `cleanup_uuid_files_auto.py` - Xoá files UUID tự động (đã xong)

### Scripts khác
- `crawl-legal-documents.py` - Crawl dữ liệu (không dùng)
- `debug_parse.py` - Debug parse (không dùng)
- `test_mysql_connection.py` - Test connection (không dùng)

## 🗄️ Database Structure

### Tables chính:
1. `chu_de` (45 records) - Chủ đề
2. `de_muc` (306 records) - Đề mục (chứa cả metadata và content)
3. `dieu_khoan` (76,303 records) - Điều khoản (chứa nội dung đầy đủ)
4. `system_metadata` (1 record) - Metadata hệ thống

### Views:
1. `vw_dieu_khoan_full` - View điều khoản đầy đủ
2. `vw_mapc_hierarchy` - View hierarchy MAPC

## 🔄 Workflow

1. **Data import** (đã hoàn thành):
   - Parse JSON từ `jsonData.js`
   - Import vào database MySQL
   - Import HTML content từ files
   - Convert HTML to Markdown

2. **Markdown generation** (sử dụng `vanban_generator.py`):
   - Kết nối database
   - Lấy dữ liệu topics, subjects, provisions
   - Tạo markdown files với cấu trúc URL đúng
   - Tạo backward compatibility files

3. **Cleanup** (tự động):
   - Xoá files cũ trước khi tạo mới
   - Xoá folders trống

## 📁 File Structure

```
van-ban/
├── index.md                    # Home page
├── DATABASE_CONTENT_STANDARD.md # Database documentation
├── an-ninh-quoc-gia.md         # Topic page
├── an-ninh-quoc-gia/           # Topic folder
│   ├── an-ninh-mang.md         # Subject page
│   └── ...
├── an-ninh-quoc-gia_an-ninh-mang.md # Backward compatibility
└── ...
```

## 🚀 Quick Start

```bash
# Kích hoạt virtual environment
source venv/bin/activate

# Chạy script chính
python3 vanban_generator.py

# Kiểm tra kết quả
find van-ban -name "*.md" | wc -l
```

## 📊 Statistics

- **Topics**: 45
- **Subjects**: 306
- **Legal provisions**: 76,303
- **Markdown files**: ~645 (352 + 293 compatibility)

## 🔧 Troubleshooting

### Lỗi kết nối database:
```bash
# Test connection
mysql -h mysql.diepxuan.corp -u vbpl -p'G]9E9S_TahIFVbq-' vbpl -e "SELECT 'Connected'"
```

### Lỗi Python packages:
```bash
# Cài đặt dependencies
pip install mysql-connector-python
```

### Lỗi file permissions:
```bash
# Cấp quyền execute
chmod +x vanban_generator.py
```

## 📞 Support

- **Database issues**: Kiểm tra `MYSQL_CONNECTION.md`
- **Script issues**: Kiểm tra logs và error messages
- **Content issues**: Kiểm tra database content
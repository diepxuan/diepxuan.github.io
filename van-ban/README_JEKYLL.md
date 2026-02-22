# CẤU TRÚC JEKYLL CHO VAN-BAN

## CẤU TRÚC MỚI
```
van-ban/
├── _config.yml           # Jekyll configuration
├── _layouts/             # Layout templates
│   └── default.html      # Main layout
├── _pages/               # Tất cả pages (Jekyll collection)
│   ├── index.md          # Trang chính
│   ├── chu-de/           # Chủ đề pages
│   │   ├── an-ninh-quoc-gia.md
│   │   ├── bao-hiem.md
│   │   └── ... (45 files)
│   └── de-muc/           # Đề mục pages
│       ├── an-ninh-quoc-gia.md
│       ├── bao-hiem-y-te.md
│       └── ... (306 files)
├── chu-de/               # Files cũ (backup)
├── de-muc/               # Files cũ (backup)
└── phap-dien/            # Database và scripts
```

## URLs ĐÚNG
Với cấu trúc Jekyll mới:

### 1. TRANG CHÍNH
```
https://docs.diepxuan.com/van-ban/
```

### 2. TRANG CHỦ ĐỀ
```
https://docs.diepxuan.com/van-ban/chu-de/[tên-chủ-đề]/
```

Ví dụ:
- https://docs.diepxuan.com/van-ban/chu-de/bao-hiem/
- https://docs.diepxuan.com/van-ban/chu-de/an-ninh-quoc-gia/

### 3. TRANG ĐỀ MỤC
```
https://docs.diepxuan.com/van-ban/de-muc/[tên-đề-mục]/
```

Ví dụ:
- https://docs.diepxuan.com/van-ban/de-muc/bao-hiem-y-te/
- https://docs.diepxuan.com/van-ban/de-muc/an-ninh-quoc-gia/

## CÁCH HOẠT ĐỘNG
1. Jekyll đọc `_config.yml` để biết cấu hình
2. Tất cả files trong `_pages/` được xử lý như collection
3. Mỗi file có `layout: page` trong front matter
4. Layout `default.html` được áp dụng cho tất cả pages
5. GitHub Pages tự động build và deploy

## FIX URLs SAI
URL sai: `https://docs.diepxuan.com/van-ban/chu-de/de-muc/bao-hiem-y-te/`

**Nguyên nhân**: Thừa `chu-de/` trong URL

**Giải pháp**: 
1. Truy cập URL đúng: `https://docs.diepxuan.com/van-ban/de-muc/bao-hiem-y-te/`
2. Hoặc từ trang chính: https://docs.diepxuan.com/van-ban/ → Bảo hiểm → Bảo hiểm y tế

## KIỂM TRA
1. Local test: `bundle exec jekyll serve`
2. GitHub Pages: Tự động build khi push
3. Check URLs: Tất cả phải kết thúc bằng `/`

## BACKUP
Files cũ được giữ trong:
- `chu-de/` (backup)
- `de-muc/` (backup)

Có thể xóa sau khi xác nhận hoạt động.

---
*Cập nhật: 2026-02-22*

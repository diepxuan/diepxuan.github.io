# Vietnamese Legal Documents Crawler

## 📋 Tổng quan

Công cụ tự động thu thập văn bản pháp luật Việt Nam từ các nguồn chính thống, tích hợp với GitHub Actions để cập nhật định kỳ.

## 🎯 Mục tiêu

- Tự động thu thập văn bản pháp luật mới nhất
- Lưu trữ có cấu trúc trong repository
- Cập nhật định kỳ hàng tuần
- Tích hợp với website công ty

## 🏗️ Kiến trúc

### 1. **GitHub Actions Workflow**
- File: `.github/workflows/crawl-legal-documents.yml`
- Lịch trình: Hàng tuần (thứ 2, 9:00 AM GMT+7)
- Trigger: Manual (workflow_dispatch) hoặc schedule

### 2. **Python Crawler Script**
- File: `scripts/crawl-legal-documents.py`
- Ngôn ngữ: Python 3.11+
- Thư viện: requests, BeautifulSoup4, pandas, markdownify

### 3. **Output Structure**
```
documents/van-ban-phap-luat/crawled/
├── legal_documents.json      # Dữ liệu JSON đầy đủ
├── legal_documents.csv       # Dữ liệu CSV
└── README.md                 # Tóm tắt markdown
```

## 🔧 Cấu hình

### Nguồn dữ liệu
1. **vanban.chinhphu.vn** - Văn bản Chính phủ
2. **thuvienphapluat.vn** - Thư viện Pháp luật
3. **moj.gov.vn** - Bộ Tư pháp (chưa triển khai)

### Cài đặt môi trường
```bash
# Cài đặt dependencies
pip install requests beautifulsoup4 lxml pandas markdownify python-dateutil

# Chạy crawler
python scripts/crawl-legal-documents.py
```

## 🚀 Sử dụng

### 1. Chạy thủ công
```bash
cd /root/.openclaw/workspace/projects/github-io
python scripts/crawl-legal-documents.py
```

### 2. Chạy qua GitHub Actions
1. Truy cập **Actions** tab trên GitHub
2. Chọn **"Crawl Vietnamese Legal Documents"**
3. Click **"Run workflow"**
4. Chọn branch và click **"Run workflow"**

### 3. Lịch trình tự động
- Tự động chạy mỗi thứ 2 lúc 9:00 AM GMT+7
- Tạo PR tự động nếu có thay đổi
- Commit changes vào branch `feat/legal-documents-crawler`

## 📊 Output Format

### JSON Format
```json
[
  {
    "source": "vanban_chinhphu",
    "title": "Nghị định 123/2024/NĐ-CP về...",
    "url": "https://vanban.chinhphu.vn/...",
    "document_number": "123/2024/NĐ-CP",
    "issue_date": "2024-12-31T00:00:00",
    "crawled_at": "2026-02-21T23:48:00"
  }
]
```

### CSV Columns
- source: Nguồn dữ liệu
- title: Tiêu đề văn bản
- url: Link đến văn bản gốc
- document_number: Số hiệu văn bản
- issue_date: Ngày ban hành
- crawled_at: Thời gian thu thập

## 🔍 Xử lý Dữ liệu

### 1. Trích xuất thông tin
- **Số hiệu văn bản**: Regex pattern `Số\s+(\d+/\d+/\S+)`
- **Ngày ban hành**: Phân tích cú pháp ngày tháng
- **Tiêu đề**: Làm sạch và chuẩn hóa

### 2. Loại bỏ trùng lặp
- Dựa trên URL để loại bỏ bản ghi trùng
- Giữ lại bản ghi mới nhất

### 3. Lưu trữ
- JSON: Cho ứng dụng đọc
- CSV: Cho phân tích dữ liệu
- Markdown: Cho documentation

## 🛡️ Bảo mật và Đạo đức

### 1. Rate Limiting
- Delay 2 giây giữa các request
- User-Agent hợp lệ
- Tôn trọng robots.txt

### 2. Dữ liệu
- Chỉ thu thập thông tin công khai
- Không lưu trữ nội dung đầy đủ
- Chỉ lưu metadata và links

### 3. Tuân thủ
- Tuân thủ điều khoản sử dụng website
- Không gây quá tải server
- Chỉ sử dụng cho mục đích hợp pháp

## 🚀 Tích hợp với Website

### 1. Hiển thị trên Website
```html
<!-- Có thể tích hợp vào pages/documents.html -->
<section id="legal-documents">
  <h2>Văn bản Pháp luật Mới nhất</h2>
  <div id="legal-documents-list">
    <!-- Load từ legal_documents.json -->
  </div>
</section>
```

### 2. API Endpoint (tương lai)
```javascript
// GET /api/legal-documents
fetch('/documents/van-ban-phap-luat/crawled/legal_documents.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🔧 Troubleshooting

### Lỗi thường gặp
1. **Connection timeout**: Kiểm tra network, tăng timeout
2. **HTML structure changed**: Cập nhật CSS selectors
3. **Rate limiting**: Tăng delay giữa các request
4. **Authentication required**: Cập nhật headers hoặc session

### Debug
```bash
# Chạy với debug output
python -c "import scripts.crawl_legal_documents; crawler = scripts.crawl_legal_documents.VietnameseLegalCrawler(); print(crawler.crawl_vanban_chinhphu())"

# Kiểm tra output
ls -la documents/van-ban-phap-luat/crawled/
cat documents/van-ban-phap-luat/crawled/legal_documents.json | jq '. | length'
```

## 📈 Phát triển Tương lai

### 1. Tính năng mong muốn
- [ ] Thu thập nội dung đầy đủ văn bản
- [ ] Phân loại theo loại văn bản (Nghị định, Thông tư, etc.)
- [ ] Tìm kiếm full-text
- [ ] Thông báo khi có văn bản mới
- [ ] Dashboard thống kê

### 2. Mở rộng nguồn dữ liệu
- [ ] Cổng thông tin điện tử các Bộ
- [ ] Cơ sở dữ liệu quốc gia về pháp luật
- [ ] Văn bản địa phương

### 3. Cải thiện hiệu suất
- [ ] Parallel crawling
- [ ] Caching
- [ ] Incremental updates
- [ ] Error recovery

## 📞 Hỗ trợ

### Liên hệ
- **GitHub Issues**: Báo cáo bug hoặc đề xuất tính năng
- **Email**: support@diepxuan.com
- **Documentation**: Xem thêm tại docs.diepxuan.com

### Tài liệu tham khảo
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Vietnamese Legal System](https://moj.gov.vn)

---

*Cập nhật lần cuối: 2026-02-21*  
*Phiên bản: 1.0.0*  
*Dự án: Điệp Xuân Legal Documents Crawler*
# PHÂN TÍCH HỆ THỐNG PHÁP ĐIỂN ĐIỆN TỬ

## TỔNG QUAN
- **Nguồn**: Bộ Pháp điển Điện tử của Bộ Tư pháp (phapdien.moj.gov.vn)
- **Định dạng**: Offline HTML/JavaScript application
- **Kích thước**: 28MB ZIP file, giải nén thành 370 files
- **Cấu trúc**: Web application tĩnh với dữ liệu JSON embedded

## CẤU TRÚC DỮ LIỆU

### 1. File chính
- `BoPhapDien.html`: Giao diện chính, tải dữ liệu từ `jsonData.js`
- `jsonData.js`: Dữ liệu chính (24MB) chứa 3 biến:
  - `jdChuDe`: 45 chủ đề (topics)
  - `jdDeMuc`: 271 đề mục (subjects)
  - `jdAllTree`: 76,303 điều khoản pháp luật (legal provisions)

### 2. Folder `demuc/`
- 271 file HTML (mỗi file tương ứng một đề mục)
- Chỉ chứa cấu trúc khung, nội dung được tải động từ JSON
- Tên file là UUID (giống `Value` trong `jdDeMuc`)

### 3. Folder `lib/`
- CSS, JavaScript, hình ảnh cho giao diện

## CẤU TRÚC DỮ LIỆU CHI TIẾT

### A. Chủ đề (jdChuDe)
```javascript
{
  "Value": "c3b69131-2931-4f67-926e-b244e18e8081",
  "Text": "An ninh quốc gia",
  "STT": "1"
}
```
- **45 chủ đề** (An ninh quốc gia, Bảo hiểm, Bưu chính viễn thông, ...)
- Mỗi chủ đề có UUID (`Value`), tên (`Text`), số thứ tự (`STT`)

### B. Đề mục (jdDeMuc)
```javascript
{
  "Value": "049522e0-fec2-4d52-916d-dd103ba69627",
  "Text": "Công tác dân tộc",
  "ChuDe": "a6ee2d1a-2edc-4c30-bff5-81efbd765464",
  "STT": "1"
}
```
- **271 đề mục** thuộc 45 chủ đề
- Mỗi đề mục thuộc một chủ đề (`ChuDe` = UUID của chủ đề)

### C. Điều khoản pháp luật (jdAllTree)
```javascript
{
  "ID": "91DDF634-BD49-4BAB-ABEE-F1EF054BF18D",
  "ChiMuc": "I",
  "MAPC": "01001000000000001000",
  "TEN": "Chương I Những quy định chung",
  "ChuDeID": "c3b69131-2931-4f67-926e-b244e18e8081",
  "DeMucID": "55323c64-e78f-4537-afcd-6a3c2af3c71d"
}
```
- **76,303 điều khoản** (chương, điều, khoản, điểm)
- `MAPC`: Mã phân cấp (20 ký tự) thể hiện cấu trúc phân cấp
- `TEN`: Tiêu đề điều khoản (ví dụ: "Điều 1.1.LQ.1. Phạm vi điều chỉnh")
- `ChuDeID`, `DeMucID`: Liên kết với chủ đề và đề mục

## PHÂN TÍCH MÃ PHÂN CẤP (MAPC)

Mã `MAPC` dài 20 ký tự, có thể phân tích như sau:
- **12 ký tự đầu**: Mã đề mục (DeMuc)
- **8 ký tự cuối**: Mã phân cấp trong đề mục

Ví dụ: `01001000000000001000` có thể phân tích thành:
- `01`: Cấp 1 (chủ đề?)
- `001`: Cấp 2
- `00000000001000`: Cấp 3...

## CÁCH THỨC HOẠT ĐỘNG CỦA ỨNG DỤNG

1. Ứng dụng tải `jsonData.js` chứa toàn bộ dữ liệu
2. Xây dựng cây phân cấp từ `jdAllTree` dựa trên `MAPC`
3. Khi click vào đề mục, tải file HTML tương ứng từ folder `demuc/`
4. Hiển thị nội dung chi tiết từ dữ liệu JSON

## ĐỀ XUẤT CRAWLER CHO HỆ THỐNG PHÁP ĐIỂN

### Phương án 1: Trích xuất trực tiếp từ JSON (ƯU TIÊN)
- **Ưu điểm**: Đơn giản, không cần parse HTML, có đầy đủ cấu trúc phân cấp
- **Cách làm**: 
  1. Parse `jsonData.js` để lấy dữ liệu JSON
  2. Xây dựng cấu trúc phân cấp từ `jdAllTree` dựa trên `MAPC`
  3. Xuất ra Markdown với cấu trúc phân cấp rõ ràng

### Phương án 2: Mô phỏng trình duyệt
- **Ưu điểm**: Có thể lấy được định dạng HTML gốc
- **Nhược điểm**: Phức tạp, cần render JavaScript

### Phương án 3: Kết hợp cả hai
- Lấy cấu trúc và metadata từ JSON
- Lấy nội dung HTML từ các file trong `demuc/` (nếu cần định dạng)

## KẾ HOẠCH TRIỂN KHAI CRAWLER

### Bước 1: Phân tích cấu trúc MAPC
- Hiểu rõ cách mã hóa phân cấp trong `MAPC`
- Xác định cách xây dựng cây phân cấp từ 76,303 entries

### Bước 2: Trích xuất dữ liệu từ JSON
- Viết script parse `jsonData.js` (cần xử lý file 24MB)
- Xây dựng cấu trúc cây từ quan hệ cha-con dựa trên `MAPC`

### Bước 3: Xuất ra Markdown
- Tạo cấu trúc thư mục theo chủ đề → đề mục
- Xuất mỗi điều khoản thành Markdown với heading phù hợp
- Bảo tồn cấu trúc phân cấp (chương, điều, khoản, điểm)

### Bước 4: Tích hợp vào website
- Tạo cấu trúc thư mục `van-ban/phap-dien/`
- Xuất ra định dạng phù hợp với Jekyll/GitHub Pages
- Cập nhật navigation và index

## LỢI ÍCH CỦA HỆ THỐNG PHÁP ĐIỂN
1. **Chính thống**: Dữ liệu từ Bộ Tư pháp
2. **Cấu trúc rõ ràng**: 45 chủ đề, 271 đề mục, phân cấp chi tiết
3. **Đầy đủ**: 76,303 điều khoản pháp luật
4. **Cập nhật**: Phiên bản mới nhất (có thể cập nhật định kỳ)

## SO SÁNH VỚI vanban.chinhphu.vn
- **Pháp điển**: Cấu trúc phân cấp, tập trung vào điều khoản pháp luật
- **Văn bản Chính phủ**: Danh sách văn bản, ít phân cấp chi tiết
- **Bổ sung**: Có thể crawl cả hai nguồn để có dữ liệu toàn diện

## KẾT LUẬN
Hệ thống Pháp điển Điện tử là nguồn dữ liệu **lý tưởng** cho việc xây dựng kho dữ liệu pháp luật Việt Nam. Với cấu trúc phân cấp rõ ràng và dữ liệu đầy đủ, có thể xây dựng crawler hiệu quả bằng cách trích xuất trực tiếp từ file JSON.
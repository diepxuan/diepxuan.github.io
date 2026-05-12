# HƯỚNG DẪN GỌI ĐỆ REFACTOR TỪNG FILE

## Mục đích

Hướng dẫn đệ làm từng file trong `van-ban/*` để bổ sung nội dung, cập nhật front matter `lastedit`, và tạo PR cho Sếp review.

## Quy trình

### Bước 1: Đọc danh sách file

Đệ đọc toàn bộ file `.md` trong `van-ban/` để xác định:

- File nào đã có nội dung đầy đủ
- File nào cần bổ sung nội dung
- File nào cần cập nhật front matter `lastedit`

### Bước 2: Xác định ưu tiên

Ưu tiên theo thứ tự:

1. **File chưa có front matter `lastedit`** (chưa từng được edit)
2. **File có `lastedit` cũ nhất** (lâu chưa được check)
3. **File có nội dung ngắn, thiếu thông tin**
4. **File có cấu trúc chưa rõ ràng**

### Bước 3: Bổ sung nội dung

Với mỗi file cần bổ sung:

1. Đọc nội dung hiện tại
2. Xác định phần còn thiếu (nếu có)
3. Tìm nội dung từ nguồn chính thức:
   - `vbpl.vn`
   - `thuvienphapluat.vn`
   - `luatviệtonline.vn`
4. Bổ sung nội dung vào file
5. Cập nhật front matter `lastedit: YYYY-MM-DD HH:mm` (UTC)

### Bước 4: Tạo PR

1. Tạo branch mới: `refactor-vanban/[ten-file]`
2. Commit thay đổi
3. Push branch
4. Tạo PR với tiêu đề: `[refactor-vanban] [ten-file] - bổ sung nội dung`
5. Mô tả chi tiết trong PR:
   - Nội dung đã bổ sung
   - Nguồn tham khảo
   - Lý do cần bổ sung

### Bước 5: Ghi nhận

Sau khi PR được merge:

1. Cập nhật `memory/YYYY-MM-DD.md` với:
   - Tên file
   - Nội dung đã bổ sung
   - Ngày `lastedit` mới
   - Link PR

## Ví dụ

### File: `van-ban/an-ninh-quoc-gia/du-lieu.md`

- **Trước**: Dừng ở "Điều 15. Cung cấp"
- **Sau**: Đầy đủ từ Điều 1 đến Điều 24 (Chương V)
- **lastedit**: `2026-05-12 14:56`
- **PR**: #62 (ví dụ)

## Lưu ý

- **Không tự ý push**. Chỉ push khi Sếp nói rõ: "Em tạo PR đi".
- **Mỗi file = 1 branch = 1 PR**.
- **Ghi nhận vào memory** trước khi tạo PR nếu chưa được phép.
- **Tìm nội dung từ nguồn chính thức** (vbpl.vn, thuvienphapluat.vn).

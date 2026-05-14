# Báo Cáo Review Văn Bản Pháp Luật

> Review toàn bộ 634 file .md trong thư mục van-ban/
> Ngày: 2026-05-13

---

## 6. Nhận Xét Chính

### Vấn đề 1: Lặp nội dung (duplicate root/subfolder)
Đa số văn bản tồn tại ở **2 bản**:
- Bản trong subfolder: `chủ-đề/ten-van-ban.md`
- Bản ở root: `chủ-de_ten-van-ban.md` (dùng underscore thay dấu /)

Ví dụ: `quoc-phong_quoc-phong.md` vs `quoc-phong/quoc-phong.md` — cả 2 có nội dung **giống hệt nhau**.

=> **Khuyến nghị:** Chỉ giữ lại 1 bản (ưu tiên subfolder) và xoá bản root duplicate.

### Vấn đề 2: Số lượng Điều bất thường
Nhiều file có **> 1000 Điều**, vượt xa văn bản luật thực tế. Ví dụ:
- `xử lý vi phạm hành chính`: 29,117 Điều (thực tế khoảng 65 Điều)
- `hải quan`: 7,003 Điều (thực tế khoảng 100 Điều)

Điều này cho thấy **nội dung bị crawl nhiều lần**, gộp cả văn bản gốc, sửa đổi, bổ sung, thông tư hướng dẫn.

### Vấn đề 3: Thiếu "Thông tin văn bản"
Tất cả 634 file, không có file nào có phần **Thông tin văn bản** (số hiệu, ngày ban hành, cơ quan ban hành, hiệu lực...). Đây là phần bắt buộc để người đọc biết văn bản còn hiệu lực hay không.

### Vấn đề 4: 126 file placeholder/subfolder rỗng
126 file chỉ có tiêu đề và body trống (7-100 chars). Đây là các subfolder placeholder chưa được điền nội dung. Cần xoá hoặc bổ sung.

### Vấn đề 5: File "-loại-bo"
14 file có suffix "-loại-bo" trong tên — đã đánh dấu để xoá nhưng chưa xoá.

---

## 1. Bảng Tổng Kết

| Nhóm | Số file | Tỷ lệ |
|------|---------|-------|
| CẦN XOÁ | 120 | 18.9% |
| CẦN CẬP NHẬT | 401 | 63.2% |
| CẦN BỔ SUNG | 109 | 17.2% |
| ỔN | 4 | 0.6% |
| **Tổng** | **634** | **100%** |

## 2. CẦN XOÁ

**Mô tả:** File placeholder, loại-bo, body trống, index page không có nội dung văn bản
**Số file:** 120

| # | File | Lý do | Gợi ý |
|---|------|-------|-------|
| 1 | `bao-hiem/bao-hiem-xa-hoi.md` | Body gần như trống: 17 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 2 | `bao-hiem_bao-hiem-xa-hoi.md` | Body gần như trống: 17 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 3 | `bo-tro-tu-phap/cong-chung.md` | Body gần như trống: 12 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 4 | `bo-tro-tu-phap_cong-chung.md` | Body gần như trống: 12 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 5 | `buu-chinh-vien-thong/giao-dich-dien-tu.md` | Body gần như trống: 19 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 6 | `buu-chinh-vien-thong_giao-dich-dien-tu.md` | Body gần như trống: 19 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 7 | `can-bo-cong-chuc-vien-chuc/can-bo-cong-chuc.md` | Body gần như trống: 19 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 8 | `can-bo-cong-chuc-vien-chuc/kiem-sat-vien-vien-kiem-sat-nhan-dan.md` | Body gần như trống: 38 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 9 | `can-bo-cong-chuc-vien-chuc_can-bo-cong-chuc.md` | Body gần như trống: 19 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 10 | `can-bo-cong-chuc-vien-chuc_kiem-sat-vien-vien-kiem-sat-nhan-dan.md` | Body gần như trống: 38 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 11 | `cong-nghiep/dien-luc.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 12 | `cong-nghiep_dien-luc.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 13 | `dan-so-gia-dinh-tre-em-binh-dang-gioi/phong-chong-bao-luc-gia-dinh.md` | Body gần như trống: 31 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 14 | `dan-so-gia-dinh-tre-em-binh-dang-gioi_phong-chong-bao-luc-gia-dinh.md` | Body gần như trống: 31 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 15 | `dan-toc.md` | Body gần như trống: 79 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 16 | `dan-toc/cong-tac-dan-toc.md` | Body gần như trống: 18 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 17 | `dan-toc_cong-tac-dan-toc.md` | Body gần như trống: 18 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 18 | `dat-dai.md` | Body gần như trống: 61 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 19 | `dat-dai/dat-dai.md` | Body gần như trống: 9 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 20 | `doanh-nghiep-hop-tac-xa/ho-tro-phap-ly-cho-doanh-nghiep.md` | Body gần như trống: 33 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 21 | `doanh-nghiep-hop-tac-xa/to-hop-tac.md` | Body gần như trống: 12 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 22 | `doanh-nghiep-hop-tac-xa_ho-tro-phap-ly-cho-doanh-nghiep.md` | Body gần như trống: 33 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 23 | `doanh-nghiep-hop-tac-xa_to-hop-tac.md` | Body gần như trống: 12 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 24 | `giao-thong-van-tai/giao-thong-duong-bo.md` | Body gần như trống: 21 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 25 | `giao-thong-van-tai_giao-thong-duong-bo.md` | Body gần như trống: 21 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 26 | `hanh-chinh-tu-phap/chung-thuc-loai-bo.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 27 | `hanh-chinh-tu-phap_chung-thuc-loai-bo.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 28 | `ke-toan-kiem-toan/kiem-toan-nha-nuoc.md` | Body gần như trống: 20 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 29 | `ke-toan-kiem-toan_kiem-toan-nha-nuoc.md` | Body gần như trống: 20 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 30 | `ngan-hang-tien-te/cac-to-chuc-tin-dung.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 31 | `ngan-hang-tien-te/phong-chong-rua-tien.md` | Body gần như trống: 23 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 32 | `ngan-hang-tien-te_cac-to-chuc-tin-dung.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 33 | `ngan-hang-tien-te_phong-chong-rua-tien.md` | Body gần như trống: 23 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 34 | `ngoai-giao-dieu-uoc-quoc-te/cong-tac-lanh-su.md` | Body gần như trống: 18 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 35 | `ngoai-giao-dieu-uoc-quoc-te/quy-che-cac-doan-cua-ta-ra-nuoc-ngoai-va-cac-doan-nuoc-ngoai-vao-nuoc-ta.md` | Body gần như trống: 74 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 36 | `ngoai-giao-dieu-uoc-quoc-te_cong-tac-lanh-su.md` | Body gần như trống: 18 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 37 | `ngoai-giao-dieu-uoc-quoc-te_quy-che-cac-doan-cua-ta-ra-nuoc-ngoai-va-cac-doan-nuoc-ngoai-vao-nuoc-ta.md` | Body gần như trống: 74 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 38 | `nong-nghiep-nong-thon/khuyen-nong-loai-bo.md` | Body gần như trống: 23 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 39 | `nong-nghiep-nong-thon/quan-ly-thuc-an-chan-nuoi-loai-bo.md` | Body gần như trống: 37 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 40 | `nong-nghiep-nong-thon_khuyen-nong-loai-bo.md` | Body gần như trống: 23 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 41 | `nong-nghiep-nong-thon_quan-ly-thuc-an-chan-nuoi-loai-bo.md` | Body gần như trống: 37 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 42 | `quoc-phong/cong-nghiep-quoc-phong-an-ninh-va-dong-vien-cong-nghiep.md` | Body gần như trống: 58 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 43 | `quoc-phong/luat-phong-thu-dan-su.md` | Body gần như trống: 23 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 44 | `quoc-phong/phong-khong-nhan-dan.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 45 | `quoc-phong/phong-thu-dan-su.md` | Body gần như trống: 18 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 46 | `quoc-phong/quan-ly-bao-ve-cong-trinh-quoc-phong-va-khu-quan-su.md` | Body gần như trống: 54 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 47 | `quoc-phong/quan-ly-bao-ve-khu-di-tich-lang-chu-tich-ho-chi-minh.md` | Body gần như trống: 55 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 48 | `quoc-phong/tieu-chuan-vat-chat-hau-can-doi-voi-quan-nhan-tai-ngu-loai-bo.md` | Body gần như trống: 65 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 49 | `quoc-phong_cong-nghiep-quoc-phong-an-ninh-va-dong-vien-cong-nghiep.md` | Body gần như trống: 58 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 50 | `quoc-phong_luat-phong-thu-dan-su.md` | Body gần như trống: 23 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 51 | `quoc-phong_phong-khong-nhan-dan.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 52 | `quoc-phong_phong-thu-dan-su.md` | Body gần như trống: 18 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 53 | `quoc-phong_quan-ly-bao-ve-cong-trinh-quoc-phong-va-khu-quan-su.md` | Body gần như trống: 54 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 54 | `quoc-phong_quan-ly-bao-ve-khu-di-tich-lang-chu-tich-ho-chi-minh.md` | Body gần như trống: 55 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 55 | `quoc-phong_tieu-chuan-vat-chat-hau-can-doi-voi-quan-nhan-tai-ngu-loai-bo.md` | Body gần như trống: 65 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 56 | `tai-nguyen/dia-chat-va-khoang-san.md` | Body gần như trống: 24 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 57 | `tai-nguyen/tai-nguyen-nuoc.md` | Body gần như trống: 17 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 58 | `tai-nguyen_dia-chat-va-khoang-san.md` | Body gần như trống: 24 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 59 | `tai-nguyen_tai-nguyen-nuoc.md` | Body gần như trống: 17 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 60 | `thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc.md` | Trang index chỉ có danh sách đề mục, không có nội dung văn bản | Xoá hoặc chuyển thành trang redirect |
| 61 | `thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/thi-dua-khen-thuong.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 62 | `thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc_thi-dua-khen-thuong.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 63 | `thi-hanh-an/thi-hanh-tam-giu-tam-giam.md` | Body gần như trống: 28 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 64 | `thi-hanh-an_thi-hanh-tam-giu-tam-giam.md` | Body gần như trống: 28 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 65 | `thong-tin-bao-chi-xuat-ban/hoat-dong-in.md` | Body gần như trống: 14 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 66 | `thong-tin-bao-chi-xuat-ban_hoat-dong-in.md` | Body gần như trống: 14 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 67 | `thuong-mai-dau-tu-chung-khoan/dau-thau.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 68 | `thuong-mai-dau-tu-chung-khoan/dau-tu-theo-phuong-thuc-doi-tac-cong-tu.md` | Body gần như trống: 41 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 69 | `thuong-mai-dau-tu-chung-khoan/khu-cong-nghiep-khu-che-xuat-va-khu-kinh-te.md` | Body gần như trống: 46 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 70 | `thuong-mai-dau-tu-chung-khoan/lap-phe-duyet-va-quan-ly-quy-hoach-tong-the-phat-trien-kinh-te-xa-hoi.md` | Body gần như trống: 74 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 71 | `thuong-mai-dau-tu-chung-khoan/mot-so-hoat-dong-kinh-doanh-dac-thu.md` | Body gần như trống: 37 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 72 | `thuong-mai-dau-tu-chung-khoan/quy-hoach.md` | Body gần như trống: 11 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 73 | `thuong-mai-dau-tu-chung-khoan_dau-thau.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 74 | `thuong-mai-dau-tu-chung-khoan_dau-tu-theo-phuong-thuc-doi-tac-cong-tu.md` | Body gần như trống: 41 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 75 | `thuong-mai-dau-tu-chung-khoan_khu-cong-nghiep-khu-che-xuat-va-khu-kinh-te.md` | Body gần như trống: 46 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 76 | `thuong-mai-dau-tu-chung-khoan_lap-phe-duyet-va-quan-ly-quy-hoach-tong-the-phat-trien-kinh-te-xa-hoi.md` | Body gần như trống: 74 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 77 | `thuong-mai-dau-tu-chung-khoan_mot-so-hoat-dong-kinh-doanh-dac-thu.md` | Body gần như trống: 37 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 78 | `thuong-mai-dau-tu-chung-khoan_quy-hoach.md` | Body gần như trống: 11 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 79 | `to-chuc-bo-may-nha-nuoc/bau-cu-dai-bieu-quoc-hoi-loai-bo.md` | Body gần như trống: 36 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 80 | `to-chuc-bo-may-nha-nuoc/thu-do.md` | Body gần như trống: 8 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 81 | `to-chuc-bo-may-nha-nuoc/to-chuc-chinh-phu.md` | Body gần như trống: 19 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 82 | `to-chuc-bo-may-nha-nuoc/to-chuc-chinh-quyen-dia-phuong.md` | Body gần như trống: 32 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 83 | `to-chuc-bo-may-nha-nuoc/to-chuc-toa-an-nhan-dan.md` | Body gần như trống: 25 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 84 | `to-chuc-bo-may-nha-nuoc_bau-cu-dai-bieu-quoc-hoi-loai-bo.md` | Body gần như trống: 36 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 85 | `to-chuc-bo-may-nha-nuoc_thu-do.md` | Body gần như trống: 8 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 86 | `to-chuc-bo-may-nha-nuoc_to-chuc-chinh-phu.md` | Body gần như trống: 19 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 87 | `to-chuc-bo-may-nha-nuoc_to-chuc-chinh-quyen-dia-phuong.md` | Body gần như trống: 32 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 88 | `to-chuc-bo-may-nha-nuoc_to-chuc-toa-an-nhan-dan.md` | Body gần như trống: 25 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 89 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/tu-phap-nguoi-chua-thanh-nien.md` | Body gần như trống: 31 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 90 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_tu-phap-nguoi-chua-thanh-nien.md` | Body gần như trống: 31 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 91 | `trat-tu-an-toan-xa-hoi/can-cuoc.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 92 | `trat-tu-an-toan-xa-hoi/luc-luong-tham-gia-bao-ve-an-ninh-trat-tu-o-co-so.md` | Body gần như trống: 52 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 93 | `trat-tu-an-toan-xa-hoi/phong-chay-chua-chay-va-cuu-nan-cuu-ho.md` | Body gần như trống: 42 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 94 | `trat-tu-an-toan-xa-hoi/phong-chong-mua-ban-nguoi.md` | Body gần như trống: 28 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 95 | `trat-tu-an-toan-xa-hoi/trat-tu-an-toan-giao-thong-duong-bo.md` | Body gần như trống: 38 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 96 | `trat-tu-an-toan-xa-hoi_can-cuoc.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 97 | `trat-tu-an-toan-xa-hoi_luc-luong-tham-gia-bao-ve-an-ninh-trat-tu-o-co-so.md` | Body gần như trống: 52 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 98 | `trat-tu-an-toan-xa-hoi_phong-chay-chua-chay-va-cuu-nan-cuu-ho.md` | Body gần như trống: 42 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 99 | `trat-tu-an-toan-xa-hoi_phong-chong-mua-ban-nguoi.md` | Body gần như trống: 28 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 100 | `trat-tu-an-toan-xa-hoi_trat-tu-an-toan-giao-thong-duong-bo.md` | Body gần như trống: 38 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 101 | `van-hoa-the-thao-du-lich/di-san-van-hoa.md` | Body gần như trống: 16 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 102 | `van-hoa-the-thao-du-lich_di-san-van-hoa.md` | Body gần như trống: 16 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 103 | `van-thu-luu-tru/luu-tru.md` | Body gần như trống: 9 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 104 | `van-thu-luu-tru_luu-tru.md` | Body gần như trống: 9 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 105 | `xay-dung-nha-o-do-thi/kinh-doanh-bat-dong-san.md` | Body gần như trống: 25 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 106 | `xay-dung-nha-o-do-thi/nha-o.md` | Body gần như trống: 7 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 107 | `xay-dung-nha-o-do-thi/xay-dung.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 108 | `xay-dung-nha-o-do-thi_kinh-doanh-bat-dong-san.md` | Body gần như trống: 25 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 109 | `xay-dung-nha-o-do-thi_nha-o.md` | Body gần như trống: 7 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 110 | `xay-dung-nha-o-do-thi_xay-dung.md` | Body gần như trống: 10 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 111 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/ban-hanh-van-ban-quy-pham-phap-luat.md` | Body gần như trống: 37 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 112 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat-loai-bo.md` | Body gần như trống: 56 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 113 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/quan-ly-hop-tac-quoc-te-ve-phap-luat-va-cai-cach-tu-phap.md` | Body gần như trống: 58 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 114 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/ra-soat-he-thong-hoa-van-ban-quy-pham-phap-luat-loai-bo.md` | Body gần như trống: 60 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 115 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_ban-hanh-van-ban-quy-pham-phap-luat.md` | Body gần như trống: 37 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 116 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat-loai-bo.md` | Body gần như trống: 56 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 117 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_quan-ly-hop-tac-quoc-te-ve-phap-luat-va-cai-cach-tu-phap.md` | Body gần như trống: 58 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 118 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_ra-soat-he-thong-hoa-van-ban-quy-pham-phap-luat-loai-bo.md` | Body gần như trống: 60 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 119 | `y-te-duoc/kham-benh-chua-benh.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |
| 120 | `y-te-duoc_kham-benh-chua-benh.md` | Body gần như trống: 22 chars, chỉ có tiêu đề và có thể là link index | Xoá file |

### Ghi chú bổ sung:

- File loại-bo: 14 file
- File gần như trống (body < 50 chars): 97 file
- Trang index chỉ có mục lục: 0 file

## 3. CẦN CẬP NHẬT

**Mô tả:** File có nội dung nhưng vấn đề về hiệu lực, trùng lặp, sai cấu trúc
**Số file:** 401

| # | File | Lý do | Gợi ý |
|---|------|-------|-------|
| 1 | `an-ninh-quoc-gia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2046 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 2 | `an-ninh-quoc-gia/an-ninh-quoc-gia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 3 | `an-ninh-quoc-gia/bao-ve-bi-mat-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 4 | `an-ninh-quoc-gia/bien-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 5 | `an-ninh-quoc-gia/canh-ve.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 6 | `an-ninh-quoc-gia/co-yeu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 7 | `an-ninh-quoc-gia/cong-an-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1150 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 8 | `an-ninh-quoc-gia/du-lieu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 9 | `an-ninh-quoc-gia/nhap-canh-xuat-canh-qua-canh-cu-tru-cua-nguoi-nuoc-ngoai-tai-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 10 | `an-ninh-quoc-gia/xuat-canh-nhap-canh-cua-cong-dan-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 11 | `an-ninh-quoc-gia_bao-ve-bi-mat-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 12 | `an-ninh-quoc-gia_bien-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 13 | `an-ninh-quoc-gia_canh-ve.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 14 | `an-ninh-quoc-gia_co-yeu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 15 | `an-ninh-quoc-gia_cong-an-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1150 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 16 | `an-ninh-quoc-gia_du-lieu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 17 | `an-ninh-quoc-gia_nhap-canh-xuat-canh-qua-canh-cu-tru-cua-nguoi-nuoc-ngoai-tai-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 18 | `an-ninh-quoc-gia_xuat-canh-nhap-canh-cua-cong-dan-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 19 | `bao-hiem.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1183 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 20 | `bao-hiem/bao-hiem-y-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2383 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 21 | `bao-hiem/kinh-doanh-bao-hiem.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3195 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 22 | `bao-hiem_bao-hiem-y-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2383 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 23 | `bao-hiem_kinh-doanh-bao-hiem.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3195 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 24 | `bo-tro-tu-phap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1243 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 25 | `bo-tro-tu-phap/dau-gia-tai-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1174 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 26 | `bo-tro-tu-phap/giam-dinh-tu-phap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1318 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 27 | `bo-tro-tu-phap/luat-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1406 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 28 | `bo-tro-tu-phap/tro-giup-phap-ly.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1105 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 29 | `bo-tro-tu-phap/tu-van-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 30 | `bo-tro-tu-phap_dau-gia-tai-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1174 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 31 | `bo-tro-tu-phap_giam-dinh-tu-phap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1318 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 32 | `bo-tro-tu-phap_luat-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1406 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 33 | `bo-tro-tu-phap_tro-giup-phap-ly.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1105 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 34 | `bo-tro-tu-phap_tu-van-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 35 | `buu-chinh-vien-thong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2069 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 36 | `buu-chinh-vien-thong/an-toan-thong-tin-mang.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1102 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 37 | `buu-chinh-vien-thong/buu-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1465 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 38 | `buu-chinh-vien-thong/cong-nghe-thong-tin.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5128 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 39 | `buu-chinh-vien-thong/tan-so-vo-tuyen-dien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 40 | `buu-chinh-vien-thong_an-toan-thong-tin-mang.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1102 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 41 | `buu-chinh-vien-thong_buu-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1465 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 42 | `buu-chinh-vien-thong_cong-nghe-thong-tin.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5128 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 43 | `buu-chinh-vien-thong_tan-so-vo-tuyen-dien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 44 | `can-bo-cong-chuc-vien-chuc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1715 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 45 | `can-bo-cong-chuc-vien-chuc/vien-chuc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5734 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 46 | `can-bo-cong-chuc-vien-chuc_vien-chuc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5734 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 47 | `chinh-sach-xa-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 48 | `chinh-sach-xa-hoi/chinh-sach-tro-giup-xa-hoi-doi-voi-doi-tuong-bao-tro-xa-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 49 | `chinh-sach-xa-hoi/nguoi-cao-tuoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 50 | `chinh-sach-xa-hoi/nguoi-khuyet-tat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 51 | `chinh-sach-xa-hoi/phong-chong-mai-dam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 52 | `chinh-sach-xa-hoi/uu-dai-nguoi-co-cong-voi-cach-mang.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1714 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 53 | `chinh-sach-xa-hoi_chinh-sach-tro-giup-xa-hoi-doi-voi-doi-tuong-bao-tro-xa-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 54 | `chinh-sach-xa-hoi_nguoi-cao-tuoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 55 | `chinh-sach-xa-hoi_nguoi-khuyet-tat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 56 | `chinh-sach-xa-hoi_phong-chong-mai-dam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 57 | `chinh-sach-xa-hoi_uu-dai-nguoi-co-cong-voi-cach-mang.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1714 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 58 | `cong-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 59 | `cong-nghiep/dau-khi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1033 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 60 | `cong-nghiep/hoa-chat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1102 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 61 | `cong-nghiep/su-dung-nang-luong-tiet-kiem-va-hieu-qua.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 62 | `cong-nghiep_dau-khi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1033 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 63 | `cong-nghiep_hoa-chat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1102 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 64 | `cong-nghiep_su-dung-nang-luong-tiet-kiem-va-hieu-qua.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 65 | `dan-so-gia-dinh-tre-em-binh-dang-gioi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 66 | `dan-so-gia-dinh-tre-em-binh-dang-gioi/binh-dang-gioi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 67 | `dan-so-gia-dinh-tre-em-binh-dang-gioi/dan-so.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 68 | `dan-so-gia-dinh-tre-em-binh-dang-gioi/hon-nhan-va-gia-dinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1350 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 69 | `dan-so-gia-dinh-tre-em-binh-dang-gioi/tre-em.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1209 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 70 | `dan-so-gia-dinh-tre-em-binh-dang-gioi_binh-dang-gioi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 71 | `dan-so-gia-dinh-tre-em-binh-dang-gioi_dan-so.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 72 | `dan-so-gia-dinh-tre-em-binh-dang-gioi_hon-nhan-va-gia-dinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1350 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 73 | `dan-so-gia-dinh-tre-em-binh-dang-gioi_tre-em.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1209 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 74 | `dan-su/dan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3090 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 75 | `dan-su/quy-dinh-thi-hanh-bo-luat-dan-su-ve-bao-dam-thuc-hien-nghia-vu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 76 | `dan-su_quy-dinh-thi-hanh-bo-luat-dan-su-ve-bao-dam-thuc-hien-nghia-vu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 77 | `doanh-nghiep-hop-tac-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1854 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 78 | `doanh-nghiep-hop-tac-xa/doanh-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1853 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 79 | `doanh-nghiep-hop-tac-xa/ho-tro-doanh-nghiep-nho-va-vua.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2088 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 80 | `doanh-nghiep-hop-tac-xa/hop-tac-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1762 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 81 | `doanh-nghiep-hop-tac-xa_doanh-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1853 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 82 | `doanh-nghiep-hop-tac-xa_ho-tro-doanh-nghiep-nho-va-vua.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2088 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 83 | `doanh-nghiep-hop-tac-xa_hop-tac-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1762 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 84 | `giao-duc-dao-tao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2152 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 85 | `giao-duc-dao-tao/giao-duc-dai-hoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2099 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 86 | `giao-duc-dao-tao/giao-duc.md` | Có 1635 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 87 | `giao-duc-dao-tao_giao-duc-dai-hoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2099 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 88 | `giao-duc-dao-tao_giao-duc.md` | Có 1635 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 89 | `giao-thong-van-tai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5169 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 90 | `giao-thong-van-tai/duong-sat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3417 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 91 | `giao-thong-van-tai/giao-thong-duong-thuy-noi-dia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2183 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 92 | `giao-thong-van-tai/hang-hai-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3521 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 93 | `giao-thong-van-tai/hang-khong-dan-dung-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4354 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 94 | `giao-thong-van-tai_duong-sat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3417 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 95 | `giao-thong-van-tai_giao-thong-duong-thuy-noi-dia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2183 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 96 | `giao-thong-van-tai_hang-hai-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3521 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 97 | `giao-thong-van-tai_hang-khong-dan-dung-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4354 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 98 | `hanh-chinh-tu-phap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 99 | `hanh-chinh-tu-phap/ho-tich.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 100 | `hanh-chinh-tu-phap/nuoi-con-nuoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 101 | `hanh-chinh-tu-phap/quoc-tich-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 102 | `hanh-chinh-tu-phap_ho-tich.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 103 | `hanh-chinh-tu-phap_nuoi-con-nuoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 104 | `hanh-chinh-tu-phap_quoc-tich-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 105 | `hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 106 | `hinh-su/hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4235 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 107 | `ke-toan-kiem-toan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1722 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 108 | `ke-toan-kiem-toan/ke-toan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1464 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 109 | `ke-toan-kiem-toan/kiem-toan-doc-lap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1052 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 110 | `ke-toan-kiem-toan_ke-toan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1464 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 111 | `ke-toan-kiem-toan_kiem-toan-doc-lap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1052 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 112 | `khieu-nai-to-cao.md` | Có 1019 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 113 | `khieu-nai-to-cao/khieu-nai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1491 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 114 | `khieu-nai-to-cao/phong-chong-tham-nhung.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1286 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 115 | `khieu-nai-to-cao/tiep-cong-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 116 | `khieu-nai-to-cao/to-cao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1327 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 117 | `khieu-nai-to-cao_khieu-nai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1491 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 118 | `khieu-nai-to-cao_phong-chong-tham-nhung.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1286 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 119 | `khieu-nai-to-cao_tiep-cong-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 120 | `khieu-nai-to-cao_to-cao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1327 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 121 | `khoa-hoc-cong-nghe.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3940 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 122 | `khoa-hoc-cong-nghe/chat-luong-san-pham-hang-hoa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1128 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 123 | `khoa-hoc-cong-nghe/chuyen-giao-cong-nghe.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1643 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 124 | `khoa-hoc-cong-nghe/cong-nghe-cao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1719 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 125 | `khoa-hoc-cong-nghe/do-luong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2192 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 126 | `khoa-hoc-cong-nghe/khoa-hoc-va-cong-nghe.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 6411 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 127 | `khoa-hoc-cong-nghe/nang-luong-nguyen-tu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3520 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 128 | `khoa-hoc-cong-nghe/tieu-chuan-va-quy-chuan-ky-thuat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2374 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 129 | `khoa-hoc-cong-nghe_chat-luong-san-pham-hang-hoa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1128 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 130 | `khoa-hoc-cong-nghe_chuyen-giao-cong-nghe.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1643 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 131 | `khoa-hoc-cong-nghe_cong-nghe-cao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1719 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 132 | `khoa-hoc-cong-nghe_do-luong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2192 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 133 | `khoa-hoc-cong-nghe_khoa-hoc-va-cong-nghe.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 6411 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 134 | `khoa-hoc-cong-nghe_nang-luong-nguyen-tu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3520 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 135 | `khoa-hoc-cong-nghe_tieu-chuan-va-quy-chuan-ky-thuat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2374 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 136 | `lao-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2768 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 137 | `lao-dong/an-toan-ve-sinh-lao-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1400 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 138 | `lao-dong/giao-duc-nghe-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3226 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 139 | `lao-dong/lao-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2517 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 140 | `lao-dong/nguoi-lao-dong-viet-nam-di-lam-viec-o-nuoc-ngoai-theo-hop-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 141 | `lao-dong/viec-lam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1822 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 142 | `lao-dong_an-toan-ve-sinh-lao-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1400 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 143 | `lao-dong_giao-duc-nghe-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3226 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 144 | `lao-dong_nguoi-lao-dong-viet-nam-di-lam-viec-o-nuoc-ngoai-theo-hop-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 145 | `lao-dong_viec-lam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1822 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 146 | `ngan-hang-tien-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2863 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 147 | `ngan-hang-tien-te/bao-hiem-tien-gui.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 148 | `ngan-hang-tien-te/cac-cong-cu-chuyen-nhuong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 149 | `ngan-hang-tien-te/ngan-hang-nha-nuoc-viet-nam.md` | Có 1785 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 150 | `ngan-hang-tien-te/ngoai-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3714 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 151 | `ngan-hang-tien-te_bao-hiem-tien-gui.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 152 | `ngan-hang-tien-te_cac-cong-cu-chuyen-nhuong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 153 | `ngan-hang-tien-te_ngan-hang-nha-nuoc-viet-nam.md` | Có 1785 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 154 | `ngan-hang-tien-te_ngoai-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3714 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 155 | `ngoai-giao-dieu-uoc-quoc-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 156 | `ngoai-giao-dieu-uoc-quoc-te/co-quan-dai-dien-nuoc-cong-hoa-xa-hoi-chu-nghia-viet-nam-o-nuoc-ngoai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 157 | `ngoai-giao-dieu-uoc-quoc-te/dieu-uoc-quoc-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 158 | `ngoai-giao-dieu-uoc-quoc-te/ham-cap-ngoai-giao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 159 | `ngoai-giao-dieu-uoc-quoc-te/mot-so-chinh-sach-doi-voi-nguoi-viet-nam-o-nuoc-ngoai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 160 | `ngoai-giao-dieu-uoc-quoc-te/quyen-uu-dai-mien-tru-danh-cho-co-quan-dai-dien-ngoai-giao-co-quan-lanh-su-va-co-quan-dai-dien-cua-to-chuc-quoc-te-tai-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 161 | `ngoai-giao-dieu-uoc-quoc-te/thoa-thuan-quoc-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 162 | `ngoai-giao-dieu-uoc-quoc-te_co-quan-dai-dien-nuoc-cong-hoa-xa-hoi-chu-nghia-viet-nam-o-nuoc-ngoai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 163 | `ngoai-giao-dieu-uoc-quoc-te_dieu-uoc-quoc-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 164 | `ngoai-giao-dieu-uoc-quoc-te_ham-cap-ngoai-giao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 165 | `ngoai-giao-dieu-uoc-quoc-te_mot-so-chinh-sach-doi-voi-nguoi-viet-nam-o-nuoc-ngoai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 166 | `ngoai-giao-dieu-uoc-quoc-te_quyen-uu-dai-mien-tru-danh-cho-co-quan-dai-dien-ngoai-giao-co-quan-lanh-su-va-co-quan-dai-dien-cua-to-chuc-quoc-te-tai-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 167 | `ngoai-giao-dieu-uoc-quoc-te_thoa-thuan-quoc-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 168 | `nong-nghiep-nong-thon.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3860 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 169 | `nong-nghiep-nong-thon/bao-ve-va-kiem-dich-thuc-vat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1172 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 170 | `nong-nghiep-nong-thon/chan-nuoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1072 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 171 | `nong-nghiep-nong-thon/de-dieu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 172 | `nong-nghiep-nong-thon/phat-trien-nganh-nghe-nong-thon.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 173 | `nong-nghiep-nong-thon/phong-chong-thien-tai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1960 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 174 | `nong-nghiep-nong-thon/quan-ly-san-xuat-kinh-doanh-muoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 175 | `nong-nghiep-nong-thon/thu-y.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2233 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 176 | `nong-nghiep-nong-thon/thuy-loi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1167 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 177 | `nong-nghiep-nong-thon/thuy-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2415 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 178 | `nong-nghiep-nong-thon/trong-trot.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1219 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 179 | `nong-nghiep-nong-thon_bao-ve-va-kiem-dich-thuc-vat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1172 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 180 | `nong-nghiep-nong-thon_chan-nuoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1072 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 181 | `nong-nghiep-nong-thon_de-dieu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 182 | `nong-nghiep-nong-thon_phat-trien-nganh-nghe-nong-thon.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 183 | `nong-nghiep-nong-thon_phong-chong-thien-tai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1960 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 184 | `nong-nghiep-nong-thon_quan-ly-san-xuat-kinh-doanh-muoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 185 | `nong-nghiep-nong-thon_thu-y.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2233 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 186 | `nong-nghiep-nong-thon_thuy-loi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1167 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 187 | `nong-nghiep-nong-thon_thuy-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2415 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 188 | `nong-nghiep-nong-thon_trong-trot.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1219 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 189 | `quoc-phong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1852 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 190 | `quoc-phong/bien-phong-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 191 | `quoc-phong/canh-sat-bien-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 192 | `quoc-phong/dan-quan-tu-ve.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 193 | `quoc-phong/giao-duc-quoc-phong-va-an-ninh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 194 | `quoc-phong/luc-luong-du-bi-dong-vien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 195 | `quoc-phong/nghia-vu-quan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 196 | `quoc-phong/quan-nhan-chuyen-nghiep-cong-nhan-va-vien-chuc-quoc-phong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 197 | `quoc-phong/quoc-phong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1009 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 198 | `quoc-phong/si-quan-quan-doi-nhan-dan-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 199 | `quoc-phong_bien-phong-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 200 | `quoc-phong_canh-sat-bien-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 201 | `quoc-phong_dan-quan-tu-ve.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 202 | `quoc-phong_giao-duc-quoc-phong-va-an-ninh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 203 | `quoc-phong_luc-luong-du-bi-dong-vien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 204 | `quoc-phong_nghia-vu-quan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 205 | `quoc-phong_quan-nhan-chuyen-nghiep-cong-nhan-va-vien-chuc-quoc-phong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 206 | `quoc-phong_si-quan-quan-doi-nhan-dan-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 207 | `tai-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2244 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 208 | `tai-chinh/hai-quan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 7003 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 209 | `tai-chinh/ngan-sach-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2958 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 210 | `tai-chinh/thuc-hanh-tiet-kiem-chong-lang-phi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 211 | `tai-chinh_hai-quan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 7003 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 212 | `tai-chinh_ngan-sach-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2958 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 213 | `tai-chinh_thuc-hanh-tiet-kiem-chong-lang-phi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 214 | `tai-nguyen.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2119 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 215 | `tai-nguyen/do-dac-va-ban-do.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1106 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 216 | `tai-nguyen/hoat-dong-vien-tham.md` | Có 2155 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 217 | `tai-nguyen/khi-tuong-thuy-van.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1990 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 218 | `tai-nguyen/tai-nguyen-moi-truong-bien-va-hai-dao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2021 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 219 | `tai-nguyen_do-dac-va-ban-do.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1106 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 220 | `tai-nguyen_hoat-dong-vien-tham.md` | Có 2155 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 221 | `tai-nguyen_khi-tuong-thuy-van.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1990 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 222 | `tai-nguyen_tai-nguyen-moi-truong-bien-va-hai-dao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2021 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 223 | `tai-san-cong-no-cong-du-tru-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2141 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 224 | `tai-san-cong-no-cong-du-tru-nha-nuoc/du-tru-quoc-gia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 225 | `tai-san-cong-no-cong-du-tru-nha-nuoc/quan-ly-su-dung-tai-san-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5959 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 226 | `tai-san-cong-no-cong-du-tru-nha-nuoc/quan-ly-va-su-dung-vien-tro-khong-hoan-lai-khong-thuoc-ho-tro-phat-trien-chinh-thuc-cua-cac-co-quan-to-chuc-ca-nhan-nuoc-ngoai-danh-cho-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 227 | `tai-san-cong-no-cong-du-tru-nha-nuoc/trung-mua-trung-dung-tai-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 228 | `tai-san-cong-no-cong-du-tru-nha-nuoc_du-tru-quoc-gia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 229 | `tai-san-cong-no-cong-du-tru-nha-nuoc_quan-ly-su-dung-tai-san-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5959 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 230 | `tai-san-cong-no-cong-du-tru-nha-nuoc_quan-ly-va-su-dung-vien-tro-khong-hoan-lai-khong-thuoc-ho-tro-phat-trien-chinh-thuc-cua-cac-co-quan-to-chuc-ca-nhan-nuoc-ngoai-danh-cho-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 231 | `tai-san-cong-no-cong-du-tru-nha-nuoc_trung-mua-trung-dung-tai-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 232 | `thi-hanh-an.md` | Có 1658 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 233 | `thi-hanh-an/dac-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 234 | `thi-hanh-an/thi-hanh-an-dan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2823 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 235 | `thi-hanh-an/thi-hanh-an-hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3094 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 236 | `thi-hanh-an/to-chuc-va-hoat-dong-cua-thua-phat-lai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 237 | `thi-hanh-an_dac-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 238 | `thi-hanh-an_thi-hanh-an-dan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2823 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 239 | `thi-hanh-an_thi-hanh-an-hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3094 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 240 | `thi-hanh-an_to-chuc-va-hoat-dong-cua-thua-phat-lai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 241 | `thong-ke.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 242 | `thong-ke/thong-ke.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 243 | `thong-tin-bao-chi-xuat-ban.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 244 | `thong-tin-bao-chi-xuat-ban/bao-chi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1335 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 245 | `thong-tin-bao-chi-xuat-ban_bao-chi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1335 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 246 | `thue-phi-le-phi-cac-khoan-thu-khac.md` | Có 2643 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 247 | `thue-phi-le-phi-cac-khoan-thu-khac/phi-va-le-phi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4502 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 248 | `thue-phi-le-phi-cac-khoan-thu-khac/quan-ly-thue.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5960 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 249 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-bao-ve-moi-truong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 250 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-su-dung-dat-nong-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 251 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-thu-nhap-ca-nhan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 252 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-thu-nhap-doanh-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 253 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-tieu-thu-dac-biet.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 254 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-xuat-khau-thue-nhap-khau.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1599 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 255 | `thue-phi-le-phi-cac-khoan-thu-khac_phi-va-le-phi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4502 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 256 | `thue-phi-le-phi-cac-khoan-thu-khac_quan-ly-thue.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5960 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 257 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-bao-ve-moi-truong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 258 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-su-dung-dat-nong-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 259 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-thu-nhap-ca-nhan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 260 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-thu-nhap-doanh-nghiep.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 261 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-tieu-thu-dac-biet.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 262 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-xuat-khau-thue-nhap-khau.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1599 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 263 | `thuong-mai-dau-tu-chung-khoan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4658 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 264 | `thuong-mai-dau-tu-chung-khoan/bao-ve-quyen-loi-nguoi-tieu-dung.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 265 | `thuong-mai-dau-tu-chung-khoan/canh-tranh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 266 | `thuong-mai-dau-tu-chung-khoan/chung-khoan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 6263 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 267 | `thuong-mai-dau-tu-chung-khoan/dau-tu-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 268 | `thuong-mai-dau-tu-chung-khoan/quan-ly-ngoai-thuong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1598 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 269 | `thuong-mai-dau-tu-chung-khoan/quan-ly-thi-truong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 270 | `thuong-mai-dau-tu-chung-khoan/thuong-mai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2786 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 271 | `thuong-mai-dau-tu-chung-khoan_bao-ve-quyen-loi-nguoi-tieu-dung.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 272 | `thuong-mai-dau-tu-chung-khoan_canh-tranh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 273 | `thuong-mai-dau-tu-chung-khoan_chung-khoan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 6263 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 274 | `thuong-mai-dau-tu-chung-khoan_dau-tu-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 275 | `thuong-mai-dau-tu-chung-khoan_quan-ly-ngoai-thuong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1598 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 276 | `thuong-mai-dau-tu-chung-khoan_quan-ly-thi-truong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 277 | `thuong-mai-dau-tu-chung-khoan_thuong-mai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 2786 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 278 | `to-chuc-bo-may-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 279 | `to-chuc-bo-may-nha-nuoc/bau-cu-dai-bieu-quoc-hoi-va-dai-bieu-hoi-dong-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 280 | `to-chuc-bo-may-nha-nuoc/hoat-dong-giam-sat-cua-quoc-hoi-va-hoi-dong-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 281 | `to-chuc-bo-may-nha-nuoc/mat-tran-to-quoc-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 282 | `to-chuc-bo-may-nha-nuoc/to-chuc-quoc-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 283 | `to-chuc-bo-may-nha-nuoc/to-chuc-vien-kiem-sat-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1076 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 284 | `to-chuc-bo-may-nha-nuoc_bau-cu-dai-bieu-quoc-hoi-va-dai-bieu-hoi-dong-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 285 | `to-chuc-bo-may-nha-nuoc_hoat-dong-giam-sat-cua-quoc-hoi-va-hoi-dong-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 286 | `to-chuc-bo-may-nha-nuoc_mat-tran-to-quoc-viet-nam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 287 | `to-chuc-bo-may-nha-nuoc_to-chuc-quoc-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 288 | `to-chuc-bo-may-nha-nuoc_to-chuc-vien-kiem-sat-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1076 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 289 | `to-chuc-chinh-tri-xa-hoi-hoi/cong-doan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 290 | `to-chuc-chinh-tri-xa-hoi-hoi/cuu-chien-binh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 291 | `to-chuc-chinh-tri-xa-hoi-hoi/quyen-lap-hoi-va-to-chuc-hoat-dong-quan-ly-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 292 | `to-chuc-chinh-tri-xa-hoi-hoi/thanh-nien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 293 | `to-chuc-chinh-tri-xa-hoi-hoi/to-chuc-hoat-dong-cua-quy-xa-hoi-quy-tu-thien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 294 | `to-chuc-chinh-tri-xa-hoi-hoi_cong-doan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 295 | `to-chuc-chinh-tri-xa-hoi-hoi_cuu-chien-binh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 296 | `to-chuc-chinh-tri-xa-hoi-hoi_quyen-lap-hoi-va-to-chuc-hoat-dong-quan-ly-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 297 | `to-chuc-chinh-tri-xa-hoi-hoi_thanh-nien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 298 | `to-chuc-chinh-tri-xa-hoi-hoi_to-chuc-hoat-dong-cua-quy-xa-hoi-quy-tu-thien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 299 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3342 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 300 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/hoa-giai-doi-thoai-tai-toa-an.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 301 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/hoa-giai-o-co-so.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 302 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/pha-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1156 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 303 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/thi-hanh-tam-giu-tam-giam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 304 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/thu-tuc-bat-giu-tau-bay.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 305 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/to-chuc-co-quan-dieu-tra-hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 306 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/to-tung-dan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3954 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 307 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/to-tung-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1997 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 308 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/to-tung-hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4311 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 309 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/trach-nhiem-boi-thuong-cua-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1281 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 310 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_hoa-giai-doi-thoai-tai-toa-an.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 311 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_hoa-giai-o-co-so.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 312 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_pha-san.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1156 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 313 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_thi-hanh-tam-giu-tam-giam.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 314 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_thu-tuc-bat-giu-tau-bay.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 315 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_to-chuc-co-quan-dieu-tra-hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 316 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_to-tung-dan-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3954 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 317 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_to-tung-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1997 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 318 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_to-tung-hinh-su.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 4311 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 319 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_trach-nhiem-boi-thuong-cua-nha-nuoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1281 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 320 | `ton-giao-tin-nguong/tin-nguong-ton-giao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 321 | `ton-giao-tin-nguong_tin-nguong-ton-giao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 322 | `trat-tu-an-toan-xa-hoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5257 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 323 | `trat-tu-an-toan-xa-hoi/canh-sat-co-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 324 | `trat-tu-an-toan-xa-hoi/canh-sat-moi-truong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 325 | `trat-tu-an-toan-xa-hoi/chung-minh-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 326 | `trat-tu-an-toan-xa-hoi/cong-an-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 327 | `trat-tu-an-toan-xa-hoi/cu-tru.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 328 | `trat-tu-an-toan-xa-hoi/dieu-kien-ve-an-ninh-trat-tu-doi-voi-mot-so-nganh-nghe-kinh-doanh-co-dieu-kien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 329 | `trat-tu-an-toan-xa-hoi/mot-so-bien-phap-bao-dam-trat-tu-cong-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 330 | `trat-tu-an-toan-xa-hoi/phong-chong-ma-tuy.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1170 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 331 | `trat-tu-an-toan-xa-hoi/xu-ly-vi-pham-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 29117 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 332 | `trat-tu-an-toan-xa-hoi_canh-sat-co-dong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 333 | `trat-tu-an-toan-xa-hoi_canh-sat-moi-truong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 334 | `trat-tu-an-toan-xa-hoi_chung-minh-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 335 | `trat-tu-an-toan-xa-hoi_cong-an-xa.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 336 | `trat-tu-an-toan-xa-hoi_cu-tru.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 337 | `trat-tu-an-toan-xa-hoi_dieu-kien-ve-an-ninh-trat-tu-doi-voi-mot-so-nganh-nghe-kinh-doanh-co-dieu-kien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 338 | `trat-tu-an-toan-xa-hoi_mot-so-bien-phap-bao-dam-trat-tu-cong-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 339 | `trat-tu-an-toan-xa-hoi_phong-chong-ma-tuy.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1170 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 340 | `trat-tu-an-toan-xa-hoi_xu-ly-vi-pham-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 29117 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 341 | `van-hoa-the-thao-du-lich.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1762 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 342 | `van-hoa-the-thao-du-lich/cong-bo-pho-bien-tac-pham-ra-nuoc-ngoai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 343 | `van-hoa-the-thao-du-lich/dien-anh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 344 | `van-hoa-the-thao-du-lich/du-lich.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1170 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 345 | `van-hoa-the-thao-du-lich/hoat-dong-my-thuat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 346 | `van-hoa-the-thao-du-lich/hoat-dong-nghe-thuat-bieu-dien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 347 | `van-hoa-the-thao-du-lich/hoat-dong-van-hoa-va-kinh-doanh-dich-vu-van-hoa-cong-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 348 | `van-hoa-the-thao-du-lich/nhuan-but-thu-lao-doi-voi-tac-pham-dien-anh-my-thuat-nhiep-anh-san-khau-va-cac-loai-hinh-nghe-thuat-bieu-dien-khac.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 349 | `van-hoa-the-thao-du-lich/quang-cao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 350 | `van-hoa-the-thao-du-lich/quy-che-dat-ten-doi-ten-duong-pho-va-cong-trinh-cong-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 351 | `van-hoa-the-thao-du-lich/thu-vien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 352 | `van-hoa-the-thao-du-lich/thuc-hien-nep-song-van-minh-trong-viec-cuoi-viec-tang.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 353 | `van-hoa-the-thao-du-lich_cong-bo-pho-bien-tac-pham-ra-nuoc-ngoai.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 354 | `van-hoa-the-thao-du-lich_dien-anh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 355 | `van-hoa-the-thao-du-lich_du-lich.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1170 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 356 | `van-hoa-the-thao-du-lich_hoat-dong-my-thuat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 357 | `van-hoa-the-thao-du-lich_hoat-dong-nghe-thuat-bieu-dien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 358 | `van-hoa-the-thao-du-lich_hoat-dong-van-hoa-va-kinh-doanh-dich-vu-van-hoa-cong-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 359 | `van-hoa-the-thao-du-lich_nhuan-but-thu-lao-doi-voi-tac-pham-dien-anh-my-thuat-nhiep-anh-san-khau-va-cac-loai-hinh-nghe-thuat-bieu-dien-khac.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 360 | `van-hoa-the-thao-du-lich_quang-cao.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 361 | `van-hoa-the-thao-du-lich_quy-che-dat-ten-doi-ten-duong-pho-va-cong-trinh-cong-cong.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 362 | `van-hoa-the-thao-du-lich_thu-vien.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 363 | `van-hoa-the-thao-du-lich_thuc-hien-nep-song-van-minh-trong-viec-cuoi-viec-tang.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 364 | `van-thu-luu-tru/cong-tac-van-thu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 365 | `van-thu-luu-tru_cong-tac-van-thu.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 366 | `xay-dung-phap-luat-va-thi-hanh-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 367 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/chuc-nang-nhiem-vu-quyen-han-va-to-chuc-bo-may-cua-to-chuc-phap-che.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 368 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/hop-nhat-van-ban-quy-pham-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 369 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-soat-thu-tuc-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 370 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/phap-dien-he-thong-quy-pham-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 371 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/pho-bien-giao-duc-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 372 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-o-co-so.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1225 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 373 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/tiep-nhan-xu-ly-phan-anh-kien-nghi-cua-ca-nhan-to-chuc-ve-quy-dinh-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 374 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/trung-cau-y-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 375 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_chuc-nang-nhiem-vu-quyen-han-va-to-chuc-bo-may-cua-to-chuc-phap-che.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 376 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_hop-nhat-van-ban-quy-pham-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 377 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_kiem-soat-thu-tuc-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 378 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_phap-dien-he-thong-quy-pham-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 379 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_pho-bien-giao-duc-phap-luat.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 380 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_thuc-hien-dan-chu-o-co-so.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1225 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 381 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_tiep-nhan-xu-ly-phan-anh-kien-nghi-cua-ca-nhan-to-chuc-ve-quy-dinh-hanh-chinh.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 382 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_trung-cau-y-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 383 | `y-te-duoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 3878 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 384 | `y-te-duoc/an-toan-thuc-pham.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1264 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 385 | `y-te-duoc/bao-ve-suc-khoe-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 386 | `y-te-duoc/dieu-kien-san-xuat-my-pham.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 387 | `y-te-duoc/duoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5676 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 388 | `y-te-duoc/phong-chong-benh-truyen-nhiem.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1797 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 389 | `y-te-duoc/phong-chong-nhiem-vi-rut-gay-ra-hoi-chung-suy-giam-mien-dich-mac-phai-o-nguoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1004 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 390 | `y-te-duoc/phong-chong-tac-hai-cua-ruou-bia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 391 | `y-te-duoc/phong-chong-tac-hai-cua-thuoc-la.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 392 | `y-te-duoc/quan-ly-trang-thiet-bi-y-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 393 | `y-te-duoc_an-toan-thuc-pham.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1264 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 394 | `y-te-duoc_bao-ve-suc-khoe-nhan-dan.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 395 | `y-te-duoc_dieu-kien-san-xuat-my-pham.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 396 | `y-te-duoc_duoc.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 5676 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 397 | `y-te-duoc_phong-chong-benh-truyen-nhiem.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1797 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 398 | `y-te-duoc_phong-chong-nhiem-vi-rut-gay-ra-hoi-chung-suy-giam-mien-dich-mac-phai-o-nguoi.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái; Có 1004 Điều - khả năng trùng lặp văn bản cũ/mới, cần kiểm tra | Kiểm tra và cập nhật |
| 399 | `y-te-duoc_phong-chong-tac-hai-cua-ruou-bia.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 400 | `y-te-duoc_phong-chong-tac-hai-cua-thuoc-la.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |
| 401 | `y-te-duoc_quan-ly-trang-thiet-bi-y-te.md` | Nội dung nhắc đến hết hiệu lực/bị thay thế/bãi bỏ - cần ghi rõ trạng thái | Kiểm tra và cập nhật |

### Ghi chú bổ sung:

- File có > 1000 Điều (nghi vấn trùng lặp): 187 file
- File nhắc đến hết hiệu lực/thay thế: 392 file

## 4. CẦN BỔ SUNG

**Mô tả:** File có front matter nhưng body quá ngắn, thiếu Điều/Chương, thiếu Thông tin văn bản
**Số file:** 109

| # | File | Lý do | Gợi ý |
|---|------|-------|-------|
| 1 | `DATABASE_CONTENT_STANDARD.md` | Thiếu phần 'Thông tin văn bản' (5201 chars, 4 Điều, 1 Chương) | Bổ sung nội dung |
| 2 | `an-ninh-quoc-gia/an-ninh-mang.md` | Thiếu phần 'Thông tin văn bản' (151584 chars, 339 Điều, 14 Chương) | Bổ sung nội dung |
| 3 | `an-ninh-quoc-gia/bao-ve-cong-trinh-quan-trong-lien-quan-den-an-ninh-quoc-gia.md` | Thiếu phần 'Thông tin văn bản' (96332 chars, 288 Điều, 10 Chương) | Bổ sung nội dung |
| 4 | `an-ninh-quoc-gia/bien-gioi-quoc-gia.md` | Thiếu phần 'Thông tin văn bản' (368540 chars, 919 Điều, 8 Chương) | Bổ sung nội dung |
| 5 | `an-ninh-quoc-gia/phong-chong-khung-bo.md` | Thiếu phần 'Thông tin văn bản' (106693 chars, 368 Điều, 23 Chương) | Bổ sung nội dung |
| 6 | `an-ninh-quoc-gia_an-ninh-mang.md` | Thiếu phần 'Thông tin văn bản' (151584 chars, 339 Điều, 14 Chương) | Bổ sung nội dung |
| 7 | `an-ninh-quoc-gia_bao-ve-cong-trinh-quan-trong-lien-quan-den-an-ninh-quoc-gia.md` | Thiếu phần 'Thông tin văn bản' (96332 chars, 288 Điều, 10 Chương) | Bổ sung nội dung |
| 8 | `an-ninh-quoc-gia_bien-gioi-quoc-gia.md` | Thiếu phần 'Thông tin văn bản' (368540 chars, 919 Điều, 8 Chương) | Bổ sung nội dung |
| 9 | `an-ninh-quoc-gia_phong-chong-khung-bo.md` | Thiếu phần 'Thông tin văn bản' (106693 chars, 368 Điều, 23 Chương) | Bổ sung nội dung |
| 10 | `buu-chinh-vien-thong/vien-thong.md` | Thiếu phần 'Thông tin văn bản' (31670 chars, 28 Điều, 2 Chương) | Bổ sung nội dung |
| 11 | `buu-chinh-vien-thong_vien-thong.md` | Thiếu phần 'Thông tin văn bản' (31670 chars, 28 Điều, 2 Chương) | Bổ sung nội dung |
| 12 | `can-bo-cong-chuc-vien-chuc/tham-phan-va-hoi-tham-toa-an-nhan-dan.md` | Thiếu phần 'Thông tin văn bản' (6768 chars, 16 Điều, 5 Chương) | Bổ sung nội dung |
| 13 | `can-bo-cong-chuc-vien-chuc_tham-phan-va-hoi-tham-toa-an-nhan-dan.md` | Thiếu phần 'Thông tin văn bản' (6768 chars, 16 Điều, 5 Chương) | Bổ sung nội dung |
| 14 | `cong-nghiep/khuyen-cong.md` | Thiếu phần 'Thông tin văn bản' (165083 chars, 496 Điều, 12 Chương) | Bổ sung nội dung |
| 15 | `cong-nghiep/quan-ly-phan-bon.md` | Thiếu phần 'Thông tin văn bản' (6616 chars, 35 Điều, 6 Chương) | Bổ sung nội dung |
| 16 | `cong-nghiep_khuyen-cong.md` | Thiếu phần 'Thông tin văn bản' (165083 chars, 496 Điều, 12 Chương) | Bổ sung nội dung |
| 17 | `cong-nghiep_quan-ly-phan-bon.md` | Thiếu phần 'Thông tin văn bản' (6616 chars, 35 Điều, 6 Chương) | Bổ sung nội dung |
| 18 | `crawled/README.md` | Body 2079 chars nhưng ít Điều/Chương (0 Điều, 0 Chương) | Bổ sung nội dung |
| 19 | `dan-su.md` | Thiếu phần 'Thông tin văn bản' (221135 chars, 891 Điều, 37 Chương) | Bổ sung nội dung |
| 20 | `dan-su/dang-ky-bien-phap-bao-dam.md` | Thiếu phần 'Thông tin văn bản' (222361 chars, 920 Điều, 12 Chương) | Bổ sung nội dung |
| 21 | `dan-su_dang-ky-bien-phap-bao-dam.md` | Thiếu phần 'Thông tin văn bản' (222361 chars, 920 Điều, 12 Chương) | Bổ sung nội dung |
| 22 | `hanh-chinh-tu-phap/cap-ban-sao-tu-so-goc-chung-thuc-ban-sao-tu-ban-chinh-chung-thuc-chu-ky.md` | Thiếu phần 'Thông tin văn bản' (111324 chars, 387 Điều, 10 Chương) | Bổ sung nội dung |
| 23 | `hanh-chinh-tu-phap/ly-lich-tu-phap.md` | Thiếu phần 'Thông tin văn bản' (30352 chars, 187 Điều, 7 Chương) | Bổ sung nội dung |
| 24 | `hanh-chinh-tu-phap_cap-ban-sao-tu-so-goc-chung-thuc-ban-sao-tu-ban-chinh-chung-thuc-chu-ky.md` | Thiếu phần 'Thông tin văn bản' (111324 chars, 387 Điều, 10 Chương) | Bổ sung nội dung |
| 25 | `hanh-chinh-tu-phap_ly-lich-tu-phap.md` | Thiếu phần 'Thông tin văn bản' (30352 chars, 187 Điều, 7 Chương) | Bổ sung nội dung |
| 26 | `index.md` | Body 2197 chars nhưng ít Điều/Chương (0 Điều, 0 Chương) | Bổ sung nội dung |
| 27 | `khieu-nai-to-cao/thanh-tra.md` | Thiếu phần 'Thông tin văn bản' (5996 chars, 10 Điều, 6 Chương) | Bổ sung nội dung |
| 28 | `khieu-nai-to-cao_thanh-tra.md` | Thiếu phần 'Thông tin văn bản' (5996 chars, 10 Điều, 6 Chương) | Bổ sung nội dung |
| 29 | `khoa-hoc-cong-nghe/so-huu-tri-tue.md` | Thiếu phần 'Thông tin văn bản' (205324 chars, 366 Điều, 22 Chương) | Bổ sung nội dung |
| 30 | `khoa-hoc-cong-nghe_so-huu-tri-tue.md` | Thiếu phần 'Thông tin văn bản' (205324 chars, 366 Điều, 22 Chương) | Bổ sung nội dung |
| 31 | `moi-truong.md` | Thiếu phần 'Thông tin văn bản' (57717 chars, 358 Điều, 8 Chương) | Bổ sung nội dung |
| 32 | `moi-truong/bao-ve-moi-truong.md` | Thiếu phần 'Thông tin văn bản' (20506 chars, 56 Điều, 22 Chương) | Bổ sung nội dung |
| 33 | `moi-truong/da-dang-sinh-hoc.md` | Thiếu phần 'Thông tin văn bản' (64122 chars, 391 Điều, 10 Chương) | Bổ sung nội dung |
| 34 | `moi-truong_bao-ve-moi-truong.md` | Thiếu phần 'Thông tin văn bản' (20485 chars, 56 Điều, 22 Chương) | Bổ sung nội dung |
| 35 | `moi-truong_da-dang-sinh-hoc.md` | Thiếu phần 'Thông tin văn bản' (64122 chars, 391 Điều, 10 Chương) | Bổ sung nội dung |
| 36 | `ngoai-giao-dieu-uoc-quoc-te/dang-ky-va-quan-ly-hoat-dong-cua-cac-to-chuc-phi-chinh-phu-nuoc-ngoai-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (74024 chars, 141 Điều, 57 Chương) | Bổ sung nội dung |
| 37 | `ngoai-giao-dieu-uoc-quoc-te/lap-va-hoat-dong-cua-van-phong-dai-dien-cua-cac-to-chuc-hop-tac-nghien-cuu-cua-nuoc-ngoai-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (34116 chars, 99 Điều, 10 Chương) | Bổ sung nội dung |
| 38 | `ngoai-giao-dieu-uoc-quoc-te/le-tan-ngoai-giao.md` | Thiếu phần 'Thông tin văn bản' (7022 chars, 19 Điều, 5 Chương) | Bổ sung nội dung |
| 39 | `ngoai-giao-dieu-uoc-quoc-te/to-chuc-quan-ly-hoi-nghi-hoi-thao-quoc-te-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (17787 chars, 79 Điều, 6 Chương) | Bổ sung nội dung |
| 40 | `ngoai-giao-dieu-uoc-quoc-te_dang-ky-va-quan-ly-hoat-dong-cua-cac-to-chuc-phi-chinh-phu-nuoc-ngoai-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (74024 chars, 141 Điều, 57 Chương) | Bổ sung nội dung |
| 41 | `ngoai-giao-dieu-uoc-quoc-te_lap-va-hoat-dong-cua-van-phong-dai-dien-cua-cac-to-chuc-hop-tac-nghien-cuu-cua-nuoc-ngoai-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (34116 chars, 99 Điều, 10 Chương) | Bổ sung nội dung |
| 42 | `ngoai-giao-dieu-uoc-quoc-te_le-tan-ngoai-giao.md` | Thiếu phần 'Thông tin văn bản' (7022 chars, 19 Điều, 5 Chương) | Bổ sung nội dung |
| 43 | `ngoai-giao-dieu-uoc-quoc-te_to-chuc-quan-ly-hoi-nghi-hoi-thao-quoc-te-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (17787 chars, 79 Điều, 6 Chương) | Bổ sung nội dung |
| 44 | `nong-nghiep-nong-thon/lam-nghiep.md` | Thiếu phần 'Thông tin văn bản' (137383 chars, 933 Điều, 13 Chương) | Bổ sung nội dung |
| 45 | `nong-nghiep-nong-thon/quan-ly-thuc-an-chan-nuoi.md` | Thiếu phần 'Thông tin văn bản' (21430 chars, 28 Điều, 7 Chương) | Bổ sung nội dung |
| 46 | `nong-nghiep-nong-thon_lam-nghiep.md` | Thiếu phần 'Thông tin văn bản' (137383 chars, 933 Điều, 13 Chương) | Bổ sung nội dung |
| 47 | `nong-nghiep-nong-thon_quan-ly-thuc-an-chan-nuoi.md` | Thiếu phần 'Thông tin văn bản' (21430 chars, 28 Điều, 7 Chương) | Bổ sung nội dung |
| 48 | `quoc-phong/mot-so-che-do-doi-voi-doi-tuong-tham-gia-chien-tranh-bao-ve-to-quoc-lam-nhiem-vu-quoc-te-o-cam-pu-chia-giup-ban-lao-sau-ngay-30-thang-4-nam-1975-co-tu-du-20-nam-tro-len-phuc-vu-trong-quan-doi-cong-an-da-phuc-vien-xuat-ngu-thoi-viec.md` | Thiếu phần 'Thông tin văn bản' (70498 chars, 171 Điều, 0 Chương) | Bổ sung nội dung |
| 49 | `quoc-phong/thuc-hien-che-do-huu-tri-doi-voi-quan-nhan-truc-tiep-tham-gia-khang-chien-chong-my-cuu-nuoc-tu-ngay-30-thang-4-nam-1975-tro-ve-truoc-co-20-nam-tro-len-phuc-vu-quan-doi-da-phuc-vien-xuat-ngu.md` | Thiếu phần 'Thông tin văn bản' (124238 chars, 221 Điều, 0 Chương) | Bổ sung nội dung |
| 50 | `quoc-phong_mot-so-che-do-doi-voi-doi-tuong-tham-gia-chien-tranh-bao-ve-to-quoc-lam-nhiem-vu-quoc-te-o-cam-pu-chia-giup-ban-lao-sau-ngay-30-thang-4-nam-1975-co-tu-du-20-nam-tro-len-phuc-vu-trong-quan-doi-cong-an-da-phuc-vien-xuat-ngu-thoi-viec.md` | Thiếu phần 'Thông tin văn bản' (70498 chars, 171 Điều, 0 Chương) | Bổ sung nội dung |
| 51 | `quoc-phong_thuc-hien-che-do-huu-tri-doi-voi-quan-nhan-truc-tiep-tham-gia-khang-chien-chong-my-cuu-nuoc-tu-ngay-30-thang-4-nam-1975-tro-ve-truoc-co-20-nam-tro-len-phuc-vu-quan-doi-da-phuc-vien-xuat-ngu.md` | Thiếu phần 'Thông tin văn bản' (124238 chars, 221 Điều, 0 Chương) | Bổ sung nội dung |
| 52 | `tai-chinh/gia.md` | Thiếu phần 'Thông tin văn bản' (6223 chars, 12 Điều, 1 Chương) | Bổ sung nội dung |
| 53 | `tai-chinh_gia.md` | Thiếu phần 'Thông tin văn bản' (6216 chars, 12 Điều, 1 Chương) | Bổ sung nội dung |
| 54 | `tai-san-cong-no-cong-du-tru-nha-nuoc/quan-ly-no-cong.md` | Thiếu phần 'Thông tin văn bản' (75982 chars, 572 Điều, 11 Chương) | Bổ sung nội dung |
| 55 | `tai-san-cong-no-cong-du-tru-nha-nuoc/quan-ly-su-dung-von-nha-nuoc-dau-tu-vao-san-xuat-kinh-doanh-tai-doanh-nghiep.md` | Thiếu phần 'Thông tin văn bản' (7255 chars, 23 Điều, 8 Chương) | Bổ sung nội dung |
| 56 | `tai-san-cong-no-cong-du-tru-nha-nuoc/quan-ly-va-su-dung-nguon-ho-tro-phat-trien-chinh-thuc-oda-va-nguon-von-vay-uu-dai-cua-cac-nha-tai-tro.md` | Body quá ngắn (105 chars), chưa có Điều/Chương | Bổ sung nội dung |
| 57 | `tai-san-cong-no-cong-du-tru-nha-nuoc_quan-ly-no-cong.md` | Thiếu phần 'Thông tin văn bản' (75982 chars, 572 Điều, 11 Chương) | Bổ sung nội dung |
| 58 | `tai-san-cong-no-cong-du-tru-nha-nuoc_quan-ly-su-dung-von-nha-nuoc-dau-tu-vao-san-xuat-kinh-doanh-tai-doanh-nghiep.md` | Thiếu phần 'Thông tin văn bản' (7173 chars, 23 Điều, 8 Chương) | Bổ sung nội dung |
| 59 | `tai-san-cong-no-cong-du-tru-nha-nuoc_quan-ly-va-su-dung-nguon-ho-tro-phat-trien-chinh-thuc-oda-va-nguon-von-vay-uu-dai-cua-cac-nha-tai-tro.md` | Body quá ngắn (105 chars), chưa có Điều/Chương | Bổ sung nội dung |
| 60 | `thong-tin-bao-chi-xuat-ban/hoat-dong-thong-tin-bao-chi-cua-bao-chi-nuoc-ngoai-co-quan-dai-dien-nuoc-ngoai-to-chuc-nuoc-ngoai-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (8766 chars, 22 Điều, 7 Chương) | Bổ sung nội dung |
| 61 | `thong-tin-bao-chi-xuat-ban/tiep-can-thong-tin.md` | Thiếu phần 'Thông tin văn bản' (100291 chars, 420 Điều, 14 Chương) | Bổ sung nội dung |
| 62 | `thong-tin-bao-chi-xuat-ban/xuat-ban.md` | Thiếu phần 'Thông tin văn bản' (57535 chars, 276 Điều, 8 Chương) | Bổ sung nội dung |
| 63 | `thong-tin-bao-chi-xuat-ban_hoat-dong-thong-tin-bao-chi-cua-bao-chi-nuoc-ngoai-co-quan-dai-dien-nuoc-ngoai-to-chuc-nuoc-ngoai-tai-viet-nam.md` | Thiếu phần 'Thông tin văn bản' (8766 chars, 22 Điều, 7 Chương) | Bổ sung nội dung |
| 64 | `thong-tin-bao-chi-xuat-ban_tiep-can-thong-tin.md` | Thiếu phần 'Thông tin văn bản' (100291 chars, 420 Điều, 14 Chương) | Bổ sung nội dung |
| 65 | `thong-tin-bao-chi-xuat-ban_xuat-ban.md` | Thiếu phần 'Thông tin văn bản' (57535 chars, 276 Điều, 8 Chương) | Bổ sung nội dung |
| 66 | `thue-phi-le-phi-cac-khoan-thu-khac/chi-phi-to-tung.md` | Thiếu phần 'Thông tin văn bản' (118681 chars, 503 Điều, 14 Chương) | Bổ sung nội dung |
| 67 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-gia-tri-gia-tang.md` | Thiếu phần 'Thông tin văn bản' (12611 chars, 22 Điều, 10 Chương) | Bổ sung nội dung |
| 68 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-su-dung-dat-phi-nong-nghiep.md` | Thiếu phần 'Thông tin văn bản' (39679 chars, 106 Điều, 7 Chương) | Bổ sung nội dung |
| 69 | `thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md` | Thiếu phần 'Thông tin văn bản' (5772 chars, 57 Điều, 5 Chương) | Bổ sung nội dung |
| 70 | `thue-phi-le-phi-cac-khoan-thu-khac_chi-phi-to-tung.md` | Thiếu phần 'Thông tin văn bản' (118681 chars, 503 Điều, 14 Chương) | Bổ sung nội dung |
| 71 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-gia-tri-gia-tang.md` | Thiếu phần 'Thông tin văn bản' (12586 chars, 22 Điều, 10 Chương) | Bổ sung nội dung |
| 72 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-su-dung-dat-phi-nong-nghiep.md` | Thiếu phần 'Thông tin văn bản' (39679 chars, 106 Điều, 7 Chương) | Bổ sung nội dung |
| 73 | `thue-phi-le-phi-cac-khoan-thu-khac_thue-tai-nguyen.md` | Thiếu phần 'Thông tin văn bản' (5772 chars, 57 Điều, 5 Chương) | Bổ sung nội dung |
| 74 | `thuong-mai-dau-tu-chung-khoan/dau-tu.md` | Thiếu phần 'Thông tin văn bản' (6789 chars, 21 Điều, 6 Chương) | Bổ sung nội dung |
| 75 | `thuong-mai-dau-tu-chung-khoan_dau-tu.md` | Thiếu phần 'Thông tin văn bản' (6789 chars, 21 Điều, 6 Chương) | Bổ sung nội dung |
| 76 | `to-chuc-chinh-tri-xa-hoi-hoi.md` | Thiếu phần 'Thông tin văn bản' (63353 chars, 445 Điều, 31 Chương) | Bổ sung nội dung |
| 77 | `to-chuc-chinh-tri-xa-hoi-hoi/hoat-dong-chu-thap-do.md` | Thiếu phần 'Thông tin văn bản' (117492 chars, 467 Điều, 17 Chương) | Bổ sung nội dung |
| 78 | `to-chuc-chinh-tri-xa-hoi-hoi_hoat-dong-chu-thap-do.md` | Thiếu phần 'Thông tin văn bản' (117492 chars, 467 Điều, 17 Chương) | Bổ sung nội dung |
| 79 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/thu-tuc-bat-giu-tau-bien.md` | Thiếu phần 'Thông tin văn bản' (134668 chars, 456 Điều, 15 Chương) | Bổ sung nội dung |
| 80 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/trong-tai-thuong-mai.md` | Thiếu phần 'Thông tin văn bản' (20955 chars, 166 Điều, 14 Chương) | Bổ sung nội dung |
| 81 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_thu-tuc-bat-giu-tau-bien.md` | Thiếu phần 'Thông tin văn bản' (134668 chars, 456 Điều, 15 Chương) | Bổ sung nội dung |
| 82 | `to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap_trong-tai-thuong-mai.md` | Thiếu phần 'Thông tin văn bản' (20955 chars, 166 Điều, 14 Chương) | Bổ sung nội dung |
| 83 | `ton-giao-tin-nguong.md` | Thiếu phần 'Thông tin văn bản' (16737 chars, 110 Điều, 9 Chương) | Bổ sung nội dung |
| 84 | `trat-tu-an-toan-xa-hoi/quan-ly-su-dung-phao.md` | Thiếu phần 'Thông tin văn bản' (49095 chars, 123 Điều, 10 Chương) | Bổ sung nội dung |
| 85 | `trat-tu-an-toan-xa-hoi/quan-ly-su-dung-vu-khi-vat-lieu-no-va-cong-cu-ho-tro.md` | Thiếu phần 'Thông tin văn bản' (9295 chars, 22 Điều, 8 Chương) | Bổ sung nội dung |
| 86 | `trat-tu-an-toan-xa-hoi/quan-ly-va-su-dung-con-dau.md` | Thiếu phần 'Thông tin văn bản' (57138 chars, 150 Điều, 8 Chương) | Bổ sung nội dung |
| 87 | `trat-tu-an-toan-xa-hoi_quan-ly-su-dung-phao.md` | Thiếu phần 'Thông tin văn bản' (49095 chars, 123 Điều, 10 Chương) | Bổ sung nội dung |
| 88 | `trat-tu-an-toan-xa-hoi_quan-ly-su-dung-vu-khi-vat-lieu-no-va-cong-cu-ho-tro.md` | Thiếu phần 'Thông tin văn bản' (9295 chars, 22 Điều, 8 Chương) | Bổ sung nội dung |
| 89 | `trat-tu-an-toan-xa-hoi_quan-ly-va-su-dung-con-dau.md` | Thiếu phần 'Thông tin văn bản' (57138 chars, 150 Điều, 8 Chương) | Bổ sung nội dung |
| 90 | `tuong-tro-tu-phap.md` | Thiếu phần 'Thông tin văn bản' (20259 chars, 158 Điều, 7 Chương) | Bổ sung nội dung |
| 91 | `tuong-tro-tu-phap/tuong-tro-tu-phap.md` | Thiếu phần 'Thông tin văn bản' (222646 chars, 795 Điều, 24 Chương) | Bổ sung nội dung |
| 92 | `van-hoa-the-thao-du-lich/the-duc-the-thao.md` | Thiếu phần 'Thông tin văn bản' (87871 chars, 683 Điều, 10 Chương) | Bổ sung nội dung |
| 93 | `van-hoa-the-thao-du-lich/to-chuc-le-tang-can-bo-cong-chuc-vien-chuc.md` | Thiếu phần 'Thông tin văn bản' (159108 chars, 657 Điều, 23 Chương) | Bổ sung nội dung |
| 94 | `van-hoa-the-thao-du-lich_the-duc-the-thao.md` | Thiếu phần 'Thông tin văn bản' (87871 chars, 683 Điều, 10 Chương) | Bổ sung nội dung |
| 95 | `van-hoa-the-thao-du-lich_to-chuc-le-tang-can-bo-cong-chuc-vien-chuc.md` | Thiếu phần 'Thông tin văn bản' (159108 chars, 657 Điều, 23 Chương) | Bổ sung nội dung |
| 96 | `van-thu-luu-tru.md` | Thiếu phần 'Thông tin văn bản' (10541 chars, 44 Điều, 7 Chương) | Bổ sung nội dung |
| 97 | `xay-dung-nha-o-do-thi.md` | Thiếu phần 'Thông tin văn bản' (12370 chars, 92 Điều, 5 Chương) | Bổ sung nội dung |
| 98 | `xay-dung-nha-o-do-thi/kien-truc.md` | Thiếu phần 'Thông tin văn bản' (62298 chars, 238 Điều, 11 Chương) | Bổ sung nội dung |
| 99 | `xay-dung-nha-o-do-thi/quy-hoach-do-thi.md` | Thiếu phần 'Thông tin văn bản' (58029 chars, 75 Điều, 6 Chương) | Bổ sung nội dung |
| 100 | `xay-dung-nha-o-do-thi_kien-truc.md` | Thiếu phần 'Thông tin văn bản' (62298 chars, 238 Điều, 11 Chương) | Bổ sung nội dung |
| 101 | `xay-dung-nha-o-do-thi_quy-hoach-do-thi.md` | Thiếu phần 'Thông tin văn bản' (58029 chars, 75 Điều, 6 Chương) | Bổ sung nội dung |
| 102 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/theo-doi-tinh-hinh-thi-hanh-phap-luat.md` | Thiếu phần 'Thông tin văn bản' (5394 chars, 13 Điều, 0 Chương) | Bổ sung nội dung |
| 103 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md` | Body quá ngắn (96 chars), chưa có Điều/Chương | Bổ sung nội dung |
| 104 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_theo-doi-tinh-hinh-thi-hanh-phap-luat.md` | Thiếu phần 'Thông tin văn bản' (5394 chars, 13 Điều, 0 Chương) | Bổ sung nội dung |
| 105 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md` | Body quá ngắn (96 chars), chưa có Điều/Chương | Bổ sung nội dung |
| 106 | `y-te-duoc/co-che-hoat-dong-co-che-tai-chinh-doi-voi-cac-don-vi-su-nghiep-y-te-cong-lap-va-gia-dich-vu-kham-benh-chua-benh-cua-cac-co-so-kham-benh-chua-benh-cong-lap.md` | Body quá ngắn (159 chars), chưa có Điều/Chương | Bổ sung nội dung |
| 107 | `y-te-duoc/hien-lay-ghep-mo-bo-phan-co-the-nguoi-va-hien-lay-xac.md` | Thiếu phần 'Thông tin văn bản' (80366 chars, 384 Điều, 12 Chương) | Bổ sung nội dung |
| 108 | `y-te-duoc_co-che-hoat-dong-co-che-tai-chinh-doi-voi-cac-don-vi-su-nghiep-y-te-cong-lap-va-gia-dich-vu-kham-benh-chua-benh-cua-cac-co-so-kham-benh-chua-benh-cong-lap.md` | Body quá ngắn (159 chars), chưa có Điều/Chương | Bổ sung nội dung |
| 109 | `y-te-duoc_hien-lay-ghep-mo-bo-phan-co-the-nguoi-va-hien-lay-xac.md` | Thiếu phần 'Thông tin văn bản' (80366 chars, 384 Điều, 12 Chương) | Bổ sung nội dung |

## 5. ỔN

**Mô tả:** File có nội dung đầy đủ, đúng cấu trúc
**Số file:** 4

| # | File | Lý do | Gợi ý |
|---|------|-------|-------|
| 1 | `ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md` |  |  |
| 2 | `ngoai-giao-dieu-uoc-quoc-te_dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md` |  |  |
| 3 | `xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md` |  |  |
| 4 | `xay-dung-phap-luat-va-thi-hanh-phap-luat_kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md` |  |  |

### Ghi chú:

- `ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md`: 3133 chars, 14 Điều, 0 Chương - Không có Thông tin VB
- `ngoai-giao-dieu-uoc-quoc-te_dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md`: 3133 chars, 14 Điều, 0 Chương - Không có Thông tin VB
- `xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md`: 4893 chars, 13 Điều, 3 Chương - Không có Thông tin VB
- `xay-dung-phap-luat-va-thi-hanh-phap-luat_kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md`: 4893 chars, 13 Điều, 3 Chương - Không có Thông tin VB

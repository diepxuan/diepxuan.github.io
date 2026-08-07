# Reviewer v99 Report — 2026-08-07 06:32 ICT
## Agent: github-io:subagent:f02b0200 (Dệ #4 Content Reviewer + PR Comment Reviewer)

---

## Nhiệm vụ 1: OCR Quality Gate — 5 VB

Chọn 5 VB chưa từng được quality gate trong các dợt v84-v98:

| VB | Dòng | OCR trước sửa | Điều | Missing | Dup | Chương | Metadata | Đánh giá |
|---|---|---|---|---|---|---|---|---|
| 210/ND-CP (Hợp đồng xây dựng) | 2288 | 2 (vận chuyên 1x, kê từ 1x) | 34 (1-34) | [] | [] | 3 (I-III) | PASS | PASS - 2 loi |
| 204/ND-CP (Xử phạt thú y) | 932 | 0 | 52 (1-52) | [] | [] | 4 (I-IV) | PASS | PASS CLEAN |
| 26/TT-BTC (Luật NS) | 956 | 0 | 38 (1-38) | [] | [] | 8 (I-VIII) | PASS | PASS CLEAN |
| 46/ND-CP (ATTP) | 1187 | 0 (*) | 55 (1-55) | [] | [] | 11 (I-XI) | FAIL (non-standard) | PASS CONTENT |
| 273/ND-CP (KD hàng miễn thuế) | 1794 | 45 trước / 0 sau | 23 (1-23) | [] | [] | 0 | PASS | PASS sau fix |

### Chi tiết từng VB:

**1. 210/2026/ND-CP** (`van-ban/xay-dung/nghi-dinh-210-2026-nd-cp-hop-dong-xay-dung.md`)
- Loại: Nghị định về hợp đồng trong hoạt động xây dựng
- 2288 dòng, 34 Điều (1-34), 3 Chương (I-III)
- 2 lỗi OCR đã sửa:
  - `vận chuyên` (L1023) -> `vận chuyển`
  - `kê từ thời điệm` + `tôi thiểu` (L801) -> `kể từ thời điểm` + `tối thiểu`
- POST-FIX: OCR = 0. Missing = [], Dup = []. PASS.

**2. 204/2026/ND-CP** (`van-bin/thu-y/nghi-dinh-204-2026-nd-cp-xu-phet-vi-pham-hanh-chinh-linh-vuc-thuy-y.md`)
- Loại: Nghị định xử phạt VPHC lĩnh vực thú y
- 932 dòng, 52 Điều (1-52), 4 Chương (I-IV)
- OCR = 0 — file sạch hoàn toàn. PASS CLEAN.

**3. 26/2026/TT-BTC** (`van-bin/tai-chinh/thong-tu-26-2026-tt-btc-huong-dan-nghi-dinh-73-2026-luat-ngan-sach.md`)
- Loại: Thông tư hướng dẫn Luật Ngân sách nhà nước
- 956 dòng, 38 Điều (1-38), 8 Chương (I-VIII)
- OCR = 0 — PASS CLEAN.

**4. 46/2026/ND-CP** (`van-bin/y-te-duoc/nghi-dinh-46-2026-nd-cp-an-toan-thuc-pham.md`)
- Loại: Nghị định quy định chi tiết Luật An toàn thực phẩm
- 1187 dòng, 55 Điều (1-55), 11 Chương (I-XI)
- OCR content = 0 — PASS CLEAN (về mặt nội dung)
- Metadata non-standard: YAML front matter không có `layout: vanban`, không có `date` trong format Jekyll chuẩn. Các trường không chuẩn: `so_hieu`, `loai_van_ban`, `nguon`, `trang_thai` thay vi `source`. Đánh giá: PASS CONTENT, FAIL METADATA (cần refactor front matter sau).

**5. 273/2026/ND-CP** (`van-bin/tai-chinh/nghi-dinh-273-2026-nd-cp-kinh-doanh-hang-mien-thue.md`)
- Loại: Nghị định kinh doanh hàng miễn thuế
- 1794 dòng, 23 Điều (1-23), 0 Chương
- 68+ lỗi OCR systematic đã sửa:
  - `đữ liệu` -> `dữ liệu` (25 lần)
  - `kế từ` -> `kể từ` (10 lần)
  - `hệ thông` -> `hệ thống` (9 lần)
  - `vận chuyên` -> `vận chuyển` (8 lần)
  - `sự có / sự cô` -> `sự cố` (8 lần)
  - `đên hệ` -> `đến hệ` (3 lần)
  - `tiên mặt` -> `tiền mặt` (4 lần)
  - `phiều` -> `phiếu` (2 lần)
  - `chậm nhật` -> `chậm nhất` (1 lần)
  - `thông tn` -> `thông tin` (1 lần)
- POST-FIX: OCR = 0. PASS.

**TỔNG KẾT**: 5/5 VB PASS quality gate content. 3 PASS CLEAN, 2 PASS với fixes. 1 VB có metadata non-standard (46/ND-CP).

---

## Nhiệm vụ 2: Scan Refactor toàn bộ van-ban/

| Tiêu chí | v97 | v98 | v99 | Thay đổi vs v98 |
|---|---|---|---|---|
| Total *.md trong van-ban/ | 645 | 645 | 639 | -6 |
| File "Đang cập nhật" | 159 | 159 | 158 | -1 |
| File < 10KB (non-STUB, non-ĐCN) | 72 | 72 | 72 | 0 |
| File < 3KB + lastedit > 7d | 7 | 7 | 3 | -4 |

**Nhận xét**:
- Giảm 6 file total so với v98 — có thế do dọn dẹp hoặc thay dôi cấu trúc thw mục
- Giảm 1 file "Đang cập nhật" — có 1 file đã dược hoàn thiện
- < 3KB + >7d giảm mạnh từ 7 -> 3 — các file nhỏ cũ đã được xwp lý hoặc cập nhật

**3 file < 3KB + lastedit > 7d** (non-STUB, non-ĐCN):
| File | Size | lastedit | Age |
|---|---|---|---|
| `nghi-dinh-286-2026-nd-cp-cơ-che-phối-hop...` | 2076B | 2026-07-23 | 15d |
| `nghi-dinh-279-2026-nd-cp-to-chuc-bo-gddt.md` | 1317B | 2026-07-18 | 20d |
| `thong-tu-26-2026-tt-btc-nguon-ngan-sach.md` | 2605B | 2026-06-11 | 57d |

Cần refactor: 0 file khẩn (3 file trên là file nhỏ, đã lưu ý trong tracking).

---

## Nhiệm vụ 3: STUB Re-check

| STUB | KB | Dòng | Trạng thái | Ghi chú |
|---|---|---|---|---|
| 279/ND-CP (Bộ GD&ĐT) | 1.3 | 27 | VẪN STUB | Modified 2026-07-18, 20 ngày, chấp nhận |
| 286/ND-CP (XNX lạnh) | 2.1 | 57 | VẪN CHưA HOÀN THIỆN | Modified 2026-07-23, thiếu nội dung toàn văn |
| 20/TAY-BVHTTDL (Giấy phép báo chí) | 1.7 | 45 | STUB | Modified 2026-07-23, layout khác |
| 61/TT-BGDĐT (Tài nguyên GD mở) | 2.9 | 61 | STUB | Modified 2026-07-22 |
| 291/NQ-TPQH16 (Văn hóa) | 1.6 | 41 | STUB + NGHI MỚ | Modified 2026-07-23, nghi ngờ số hiệu |
| 44/TT-BKHCN (Tần số vô tuyến) | — | — | KHÔNG CÓ FILE | Đệ #3 fail 3x, slug 442979, chỉ trong tracking |

**TỔNG KẾT STUB**: 5/6 vẫn là STUB bền vững (không thay đổi từ v95), 1/6 (44/TT-BKHCN) chưa được crawl từ nỗi lần thất bại của Đệ #3.

---

## Nhiệm vụ 4: PR Comments

### PR #263: heartbeat/crawl-vanban-20260806
- Author: caothu159 (Trần Ngọc Đức)
- Created: 2026-08-06
- Branch: `heartbeat/crawl-vanban-20260806`
- Comments: **0**
- Reviews: **0**
- Trạng thái: **CHỜ SẾP REVIEW**

### Phân loại:
| PR | Comments | Reviews | Phân loại | Hành động |
|---|---|---|---|---|
| #263 | 0 | 0 | Chờ Sếp review | Đề nghị Sếp review |

Chỉ có 1 PR open duy nhất.

---

## Nhiệm vụ 5: Discovery bổ sung

- NĐ sitemap: **403 Forbidden** (luatvietnam.vn block)
- TT sitemap: **403 Forbidden** (luatvietnam.vn block)
- So với v98 ref:
  - NĐ: `23553db37114f2cc3ecf513220a57416` — không thể refresh vì 403
  - TT: `59062d8a7f6f3b500befc786a9e9e782` — không thể refresh vì 403

**Kết luận**: Sitemap không thể refresh. Cần thử lại vào lần poll sau (có thể do rate limit).

---

## Commit
Sẽ commit các file đx sửa vào branch hiện tại `heartbeat/crawl-vanban-20260806`.

2 file đx sửa OCR:
- `van-bin/xay-dung/nghi-dinh-210-2026-nd-cp-hop-dong-xay-dung.md` (2 lỗi: vận chuyên, kê từ/thời điệp/tôi thiểu)
- `van-bin/tai-chinh/nghi-dinh-273-2026-nd-cp-kinh-doanh-hang-mien-thue.md` (62+ lỗi systematic)

3 file PASS CLEAN (0 lỗi, không cần sửa):
- `van-bin/thu-y/nghi-dinh-204-2026-nd-cp-xu-phet-vi-phom-hanh-chinh-linh-vuc-thuy-y.md`
- `van-bin/tai-chinh/thong-tu-26-2026-tt-btc-huong-dan-nghi-dinh-73-2026-luat-ngan-sach.md`
- `van-bin/y-te-duoc/nghi-dinh-46-2026-nd-cp-an-toan-thuc-pham.md` (CONTENT PASS, metadata note)
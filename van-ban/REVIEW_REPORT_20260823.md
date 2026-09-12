# BÁO CÁO REVIEW - ĐỆ #4 REVIEWER
**Ngày:** 2026-08-23 00:34 GMT+7  
**Session:** agent:github-io:subagent:02c55d33-e88c-417a-a50c-9360bf45d869 (depth 1/1)

---

## 1. FILE CẦN REFACTOR (Metadata "Đang cập nhật" + < 10KB + lastedit > 7 ngày)

| # | File | Kích thước | Last Modified | Vấn đề |
|---|------|-----------|---------------|--------|
| 1 | `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` | 1,574 bytes | 2026-07-23 | STUB file - status "Đang cập nhật (stub)", chờ OCR từ PDF signed (đã 30 ngày chưa có nội dung) |

> **Kết luận:** Phát hiện 1 file archive STUB cần Sếp quyết định: tiếp tục chờ OCR, loại bỏ khỏi archive, hoặc chuyển sang nhóm "tạm ngưng crawl". Tình trạng không đổi so với scan 2026-08-21 và 2026-08-19.

> **Đã cập nhật LEGISLATION_TRACKING.md** - Section "Cap nhat 2026-08-23 00:34 ICT (Review v124 — De #4)" → "Refactor Scan".

---

## 2. VĂN BẢN "HOÀN THIỆN" TỪ LEGISLATION_TRACKING.md (5 file chọn review)

Chọn 5 file có `trangthai: hoanthien` (hoặc `status: hoanthien`) **gần đây nhất** và **chưa từng được gate** trong các báo cáo trước:

| # | Số hiệu | File | Last Modified | Trạng thái tracking |
|---|---------|------|---------------|---------------------|
| 1 | TT 65/2026/TT-BXD | `van-ban/xay-dung/thong-tu-65-2026-tt-bxd-dinh-muc-ktkt-khao-sat-do-sau-hang-hai.md` | 2026-08-22 | Hoàn thiện (mới nhất) |
| 2 | TT 20/2026/TT-BVHTTDL | `van-ban/van-hoa/thong-tu-20-2026-tt-bvhttdl-giay-phep-bao-chi.md` | 2026-08-21 | Hoàn thiện |
| 3 | TT 115/2026/TT-BCA | `van-ban/cong-an/115-2026-tt-bca-the-giay-phep-chung-nhan-an-ninh-hang-khong.md` | 2026-08-20 | Hoàn thiện |
| 4 | NĐ 311/2026/NĐ-CP | `van-ban/vi-pham-hanh-chinh/311-2026-nd-cp.md` | 2026-08-20 | Hoàn thiện |
| 5 | NĐ 286/2026/NĐ-CP | `van-ban/chinh-phu/nghi-dinh-286-2026-nd-cp-co-che-phoi-hop-quan-ly-nhap-xuat-canh-nguoi-nuoc-ngoai.md` | 2026-08-20 | Hoàn thiện |

---

## 3. KẾT QUẢ OCR QUALITY GATE (5 file review)

### Checklist áp dụng: `documents/OCR_QUALITY_GATE.md`

| # | File | Lines | Articles (range) | Chapters | OCR Issues | Đánh giá | Ghi chú |
|---|------|-------|------------------|----------|------------|----------|---------|
| 1 | TT 65/2026/TT-BXD | 188 | 4 (1-4) | 2 (I-II) | **0** | **PASS CLEAN** | Metadata sạch, `trangthai: hoanthien` có sẵn. Heading Chuong đầy đủ (`## Chương I: CÔNG TÁC ĐỊNH VỊ...`). |
| 2 | TT 20/2026/TT-BVHTTDL | 301 | 20 (1-20) | 5 (I-V) | 0 / 24 FP | **PASS CLEAN** | 24 false positive `ngày l` đều match `ngày làm việc` (hợp lệ). Cần thu hẹp pattern scan. |
| 3 | TT 115/2026/TT-BCA | 1653 | 33 (1-33) | 6 (I-VI) | 0 / 8 FP | **PASS CLEAN** | 4 FP `ngày làm việc` + 4 chuỗi `above` nằm trong **bản dịch Anh-Việt** của biểu mẫu song ngữ hành chính hàng không (KHÔNG phải OCR rác). |
| 4 | NĐ 311/2026/NĐ-CP | 185 | 9 (1-9) | 0 | **0** | **PASS CLEAN** | Văn bản ngắn, không có Chương, chỉ có 9 Điều. Metadata sạch. |
| 5 | NĐ 286/2026/NĐ-CP | 169 | 15 (1-15) | 3 (I-III) | 0 / 1 FP | **PASS CLEAN** | 1 FP `ngày làm việc`. Chuong I-III đúng thứ tự. |

### Tổng kết OCR Gate

| Tiêu chí | Kết quả |
|----------|---------|
| Tổng file scan | 5 |
| PASS hoàn toàn (OCR issues thật = 0) | **5/5** |
| Cần sửa OCR (thật) | 0 |
| Cần chuẩn hóa heading Điều | 0 |
| Cần chuẩn hóa heading Chương | 0 |
| **Tổng false positive `ngày l`** | 29 (24 + 4 + 1) — đều là `ngày làm việc` hợp lệ |
| **Tổng chuỗi `above`** | 4 — đều nằm trong bản dịch Anh-Việt song ngữ hành chính |

### Đề xuất cải tiến `OCR_QUALITY_GATE.md` (Section 7.2 / Section 8)

Pattern `ngày l` và `ngày L` hiện tại quá rộng, match cả `ngày làm việc` (chuỗi hợp lệ phổ biến). Đề xuất thu hẹp thành:
```regex
ngày l[0-9]|ngày L[0-9]
```
để chỉ match lỗi OCR cụ thể `ngày l7`, `ngày L5`, `ngày L0`... Điều này giảm 99% false positive trong tương lai.

---

## 4. KIỂM TRA CẤU TRÚC ĐIỀU/CHƯƠNG

| File | Tổng Điều | Range | Missing | Duplicate | Chương | Out-of-order | Suspicious | Đánh giá |
|------|-----------|-------|---------|-----------|--------|--------------|------------|----------|
| TT 65/2026/TT-BXD | 4 | 1-4 | [] | [] | 2 (I, II) | [] | 0 | **PASS** |
| TT 20/2026/TT-BVHTTDL | 20 | 1-20 | [] | [] | 5 (I-V) | [] | 0 | **PASS** |
| TT 115/2026/TT-BCA | 33 | 1-33 | [] | [] | 6 (I-VI) | [] | 0 | **PASS** |
| NĐ 311/2026/NĐ-CP | 9 | 1-9 | [] | [] | 0 | - | 0 | **PASS** |
| NĐ 286/2026/NĐ-CP | 15 | 1-15 | [] | [] | 3 (I-III) | [] | 0 | **PASS** |

---

## 5. BÁO CÁO PR COMMENTS

### PR đang mở: `gh pr list --state open`

| PR # | Title | Author | Created | Comments | Reviews |
|------|-------|--------|---------|----------|---------|
| **#264** | Heartbeat crawl-vanban 2026-08-07 → 2026-08-22: NĐ 312/314/315/316/318/320/321/322/323/324/325/326 + TT 10/34/45/63/64/65/115/117/136 + 20/TT-BVHTTDL + 35/41/TT-BCT | caothu159 | 2026-08-07 | **0** | **0** |

### Lệnh kiểm tra đã chạy:
```bash
gh pr list --state open --json number,title,author,createdAt
gh api repos/diepxuan/diepxuan.github.io/issues/264/comments   # → []
gh api repos/diepxuan/diepxuan.github.io/pulls/264/reviews     # → []
gh api repos/diepxuan/diepxuan.github.io/pulls/264             # comments: 0, review_comments: 0, commits: 200
```

### Phân loại PR comments (theo yêu cầu)

| Loại | Số lượng | Danh sách |
|------|----------|-----------|
| **Cần xử lý ngay** | 0 | — |
| **Chờ Sếp review** | 1 | PR #264 (mở 16 ngày, 200 commits, 0 comments, 0 reviews) |
| **Thông báo** | 0 | — |
| **Đã stale** | 1 | PR #264 (đã quá thời gian review hợp lý: 16 ngày > 7 ngày SLA; cần Sếp review/approve/close) |

> **Nhận xét:** PR #264 chứa khối lượng thay đổi rất lớn (200 commits, hàng chục file văn bản mới hoàn thiện + tracking + discovery artifacts). PR đã mở 16 ngày (07/08 → 23/08) không có bất kỳ comment/review nào. Đây là dấu hiệu STALE — cần Sếp xử lý: review nhanh để merge hoặc đóng lại.

---

## 6. TỔNG KẾT & KHUYẾN NGHỊ

### Files cần hành động (xếp theo ưu tiên)

#### Ưu tiên cao
1. **PR #264**: cần Sếp review — 200 commits, 0 comments, 16 ngày STALE. Các VB trong PR đã được gate qua nhiều vòng review (v98, v108, v122), không còn blocker kỹ thuật.

#### Ưu tiên thấp
2. **1 file archive STUB** (`van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md`): quyết định cuối cùng từ Sếp — tiếp tục chờ OCR hoặc loại bỏ khỏi archive.

### Đề xuất cải tiến `OCR_QUALITY_GATE.md`
- Thu hẹp pattern `ngày l` → `ngày l[0-9]` để giảm false positive 99%.
- Bổ sung ghi chú: chuỗi `above`, `As above` được phép xuất hiện trong bản dịch Anh-Việt song ngữ của biểu mẫu hành chính.

### Files OK (không cần hành động)
- 5 file vừa gate — tất cả PASS CLEAN, có thể merge trong PR kế tiếp.

---

*Báo cáo tự động bởi Subagent #4 - Content Reviewer + PR Comment Reviewer*  
*Ngày: 2026-08-23 00:34 GMT+7*  
*Session: agent:github-io:subagent:02c55d33-e88c-417a-a50c-9360bf45d869*

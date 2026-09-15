# Review Report - 2026-08-22 (Heartbeat Đệ #4)

**Subagent**: agent:github-io:subagent:377c20c9-1706-45ac-b60c-1a0bfd583bb1
**Ngày**: 2026-08-22 09:05 ICT Asia/Saigon
**Nhiệm vụ**: Content Reviewer + PR Comment Reviewer (Đệ #4)

---

## 1. PR Comments Review

### Phương pháp
- `gh pr list --state open` → 1 PR: #264
- `gh api repos/.../issues/264/comments` → []
- `gh api repos/.../pulls/264/comments` → []
- `gh api repos/.../pulls/264/reviews` → []

### Kết quả

| PR | Tiêu đề | Trạng thái | Issue Comments | Review Comments | Reviews | Updated |
|----|---------|-----------|----------------|-----------------|---------|---------|
| #264 | Heartbeat crawl-vanban 2026-08-07 → 2026-08-21: NĐ 318/319/320/321/322/323 + hoàn thiện TT 10/45/63/64/65/105/115/117 + 20/2026/TT-BVHTTDL | OPEN | 0 | 0 | 0 | 2026-08-22T01:40Z |

### Phân loại comment

| Phân loại | Mô tả | Số lượng |
|-----------|-------|---------|
| **Cần xử lý ngay** | Action item cụ thể | 0 |
| **Chờ Sếp review** | Review request, đang chờ Sếp phản hồi | 0 |
| **Thông báo** | Thông tin, status update | 0 |
| **Đã stale** | Comment cũ > 7 ngày, có thể đóng | 0 |

### Kết luận PR Comments
- **Trạng thái**: Trống hoàn toàn — không có issue comment, review comment, hay review nào.
- **Phân loại**: **Chờ Sếp review** — PR #264 (heartbeat/crawl-vanban-20260807) đã có 194 commits, mở từ 07/08/2026, đang chờ Sếp review/merge/close.
- **Khuyến nghị**: PR #264 đã được mở hơn 14 ngày (07/08/2026 → 22/08/2026) với 194 commits. Cần Sếp quyết định:
  - Merge nếu đã pass review
  - Hoặc yêu cầu xử lý tiếp
  - Hoặc close nếu cần rebase/reset

---

## 2. Refactor Scan van-ban/

### Tiêu chí chính (theo task)
- Metadata "Đang cập nhật"
- Kích thước < 10KB
- Lastedit > 7 ngày

### Kết quả quét chính xác (đúng cả 3 tiêu chí)

| File | Kích thước | Lastedit | Tuổi | Trạng thái |
|------|-----------|----------|------|-----------|
| `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` | 1574 B | 2026-07-23 | 30d | **STUB** — metadata `status: Đang cập nhật (stub)`, chờ OCR từ PDF signed |

### Kết quả mở rộng (status: stub/chưa hoàn thiện)

Quét mở rộng các file có `status:` metadata là stub/chưa hoàn thiện (bất kể kích thước):

| # | File | Size | Lastedit | Tuổi | Status | Ghi chú |
|---|------|------|----------|------|--------|---------|
| 1 | `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` | 1574 B | 2026-07-23 | 30d | "Đang cập nhật (stub)" | PDF 86-btc.signed.pdf tồn tại, chờ OCR |
| 2 | `van-ban/van-hoa/nghi-quyet-291-2026-nq-tpqh16-phat-trien-van-hoa.md` | 1575 B | 2026-08-04 | 18d | "STUB" | Có ghi chú xác minh số hiệu sai (slug 441168 thực ra là NĐ 291 về thuế) |
| 3 | `van-ban/ngan-hang/106-2026-tt-btc-dang-ky-hoat-dong-ngan-hang-chinh-sach-xa-hoi.md` | 18200 B | 2026-08-04 | 18d | "stub" | Đã OCR nhưng chất lượng thấp, cần re-OCR hoặc text sạch |
| 4 | `van-ban/xay-dung/thong-tu-65-2026-tt-bxd-dinh-muc-ktkt-khao-sat-do-sau-hang-hai.md` | 17895 B | 2026-08-20 | 1d | "STUB" | Mới thêm ngày 20/8, đã có nội dung dài, có thể refactor status |
| 5 | `van-ban/tai-chinh/thong-tu-40-2026-tt-nhnn.md` | 24863 B | 2026-08-20 | 2d | "chua-hoanthien" | Nội dung crawl từ luatvietnam.vn bị ngắt tại Điều 10 khoản 6 |

### Phân tích chi tiết

**File 1 — `86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md`** (tuổi: 30d, STUB chính thức):
- File archive, có status rõ ràng "Đang cập nhật (stub)".
- Đã có metadata đầy đủ + căn cứ pháp lý.
- Đang chờ OCR hoàn tất từ PDF signed `86-btc.signed.pdf`.
- **Cần refactor**: Ưu tiên thấp (đã 30 ngày, archive folder, có thể giữ nguyên hoặc xóa nếu không có nhu cầu).

**File 2 — `nghi-quyet-291-2026-nq-tpqh16-phat-trien-van-hoa.md`** (tuổi: 18d, STUB có ghi chú xác minh):
- Có ghi chú trong metadata: "Không tìm thấy nội dung trên vanban.chinhphu.vn hoặc luatvietnam.vn. Slug 441168 trên sitemap_nghidinh là Nghị định 291/NĐ-CP (thuế, hóa đơn), không phải Nghị quyết 291/NQ-TPQH16. Cần xác minh lại số hiệu/văn bản."
- **Cần refactor**: Cao — số hiệu có thể sai, cần Sếp xác minh.

**File 3 — `106-2026-tt-btc-dang-ky-hoat-dong-ngan-hang-chinh-sach-xa-hoi.md`** (tuổi: 18d, OCR kém):
- 18.2KB nhưng OCR chất lượng thấp (nhiều lỗi ký tự, dấu thanh sai, một số heading Điều không khớp).
- Có ghi chú kỹ thuật đầy đủ, đã chuẩn hóa một số lỗi chắc chắn.
- **Cần refactor**: Trung bình — cần re-OCR khi engine cải thiện hoặc tìm nguồn text sạch (vbpl.vn, hethongphapluat.com).

**File 4 — `thong-tu-65-2026-tt-bxd-dinh-muc-ktkt-khao-sat-do-sau-hang-hai.md`** (tuổi: 1d, STUB metadata nhưng có nội dung):
- 17.9KB, đã có nội dung từ Điều 1-4 + Phụ lục định mức.
- Status "STUB" có thể đã outdated vì nội dung đã được crawl đầy đủ.
- **Cần refactor**: Thấp — chỉ cần đổi status từ "STUB" sang "hoanthien" nếu nội dung đã đủ.

**File 5 — `thong-tu-40-2026-tt-nhnn.md`** (tuổi: 2d, "chua-hoanthien"):
- 24.8KB, nội dung crawl bị ngắt tại Điều 10 khoản 6.
- Cần nguồn text đầy đủ từ luatvietnam.vn hoặc PDF chính thức.
- **Cần refactor**: Trung bình — nội dung gần đủ, chỉ thiếu đoạn cuối.

---

## 3. OCR Quality Gate — Random 5 văn bản

### Phương pháp
- Random 5 file từ `van-ban/` với kích thước > 5KB.
- Chạy script OCR Quality Gate (theo `documents/OCR_QUALITY_GATE.md` mục 8-10).
- Đánh giá: OCR Issues, Articles, Chapters, Suspicious headings.

### Kết quả

| # | File | Size | Lines | Articles | Chapters | OCR Issues | Suspicious | Đánh giá |
|---|------|------|-------|----------|----------|------------|------------|----------|
| 1 | `van-ban/giao-duc/nghe-nghiep/65-2026-tt-bgddt.md` | 24.9KB | 142 | 1-8 (OK) | 0 | **0** | 0 | **OK** |
| 2 | `van-ban/doanh-nghiep-hop-tac-xa/295-2026-nd-cp.md` | 214.6KB | 1247 | 1-69 (OK) | 6 (I-VI, OK) | **0** | 0 | **OK** |
| 3 | `van-ban/an-ninh-quoc-gia/thong-tu-115-2026-tt-bqp-quy-dinh-bao-ve-bi-mat-nha-nuoc-trong-bo-quoc-phong.md` | 24.9KB | 170 | 1-6 (OK) | 0 | **0** | 0 | **OK** |
| 4 | `van-ban/ngoai-giao-dieu-uoc-quoc-te/thoa-thuan-quoc-te.md` | 288.7KB | 2951 | Format tổng hợp (Điều 23.6.LQ.X / 23.6.TT.X.Y) | — | **0** | 233 (format đặc biệt) | **OK** (trang tổng hợp) |
| 5 | `van-ban/tai-chinh/nghi-dinh-318-2026-nd-cp.md` | 10.5KB | 95 | 1-10 (OK) | 0 | **0** | 0 | **OK** |

### Chi tiết từng file

**1. `van-ban/giao-duc/nghe-nghiep/65-2026-tt-bgddt.md`** — TT 65/2026/TT-BGDĐT
- Loại: Thông tư
- Số Điều: 8 (range 1-8)
- Missing: [] | Duplicate: []
- Chương: 0 (TT thường không có Chương)
- **Verdict: OK để merge**

**2. `van-ban/doanh-nghiep-hop-tac-xa/295-2026-nd-cp.md`** — NĐ 295/2026/NĐ-CP
- Loại: Nghị định
- Số Điều: 69 (range 1-69)
- Missing: [] | Duplicate: []
- Chương: 6 (I, II, III, IV, V, VI — đúng thứ tự)
- **Verdict: OK để merge**

**3. `van-ban/an-ninh-quoc-gia/thong-tu-115-2026-tt-bqp-quy-dinh-bao-ve-bi-mat-nha-nuoc-trong-bo-quoc-phong.md`** — TT 115/2026/TT-BQP
- Loại: Thông tư
- Số Điều: 6 (range 1-6)
- Missing: [] | Duplicate: []
- Chương: 0
- **Verdict: OK để merge**

**4. `van-ban/ngoai-giao-dieu-uoc-quoc-te/thoa-thuan-quoc-te.md`** — Trang tổng hợp
- Loại: Trang tổng hợp (layout: page, không phải vanban)
- Format đặc biệt: `Điều 23.6.LQ.X` (Luật) / `Điều 23.6.TT.X.Y` (Thông tư) — chuẩn hóa theo format tổng hợp.
- 233 suspicious headings do format không phải `### Điều X.` mà là heading lồng trong đoạn văn (không phải heading markdown thật).
- **Verdict: OK** — file tổng hợp đã được crawl với format chuẩn hóa, không phải STUB.

**5. `van-ban/tai-chinh/nghi-dinh-318-2026-nd-cp.md`** — NĐ 318/2026/NĐ-CP
- Loại: Nghị định
- Số Điều: 10 (range 1-10)
- Missing: [] | Duplicate: []
- Chương: 0 (NĐ sửa đổi NĐ 86/2021, không có Chương)
- **Verdict: OK để merge**

---

## 4. Tổng kết

### Phân loại kết quả

| Hạng mục | Kết quả |
|----------|---------|
| **PR cần Sếp review** | 1 (PR #264, 194 commits, 0 comments) |
| **File cần refactor (đúng tiêu chí)** | 1 (`86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md`, 30d stub) |
| **File STUB mở rộng** | 5 (trong đó 1 file mới edit ngày 20/8 có thể đã đủ nội dung) |
| **Văn bản OK để merge** | 5/5 (100% sample OCR Quality Gate pass) |

### Khuyến nghị hành động

**Cao** (Sếp quyết định):
1. **PR #264**: 14 ngày chưa có feedback, 194 commits. Cần Sếp quyết định merge/close.
2. **`nghi-quyet-291-2026-nq-tpqh16`**: Số hiệu có thể sai (slug 441168 là NĐ 291, không phải NQ 291). Cần Sếp xác minh hoặc xóa file STUB này.
3. **`thong-tu-65-2026-tt-bxd-...`**: Status "STUB" nhưng nội dung 17.9KB đã đầy đủ. Cần refactor status sang "hoanthien".

**Trung bình** (tự động xử lý được khi có thời gian):
4. **`106-2026-tt-btc`**: Re-OCR hoặc tìm text sạch từ nguồn khác.
5. **`40-2026-tt-nhnn`**: Bổ sung nội dung bị thiếu từ Điều 10 khoản 6.

**Thấp** (theo dõi):
6. **`86-2026-TT-BTC`**: File archive, có thể giữ nguyên trạng thái STUB.

### So sánh với review trước (2026-08-20)

| Hạng mục | 2026-08-20 | 2026-08-22 | Thay đổi |
|----------|-----------|-----------|---------|
| PR open | 1 (#264, 0 comment) | 1 (#264, 0 comment) | Không đổi |
| File cần refactor (đúng tiêu chí) | 2 (86-TT-BTC, 62-TT-BXD) | 1 (chỉ 86-TT-BTC) | -1 (62-TT-BXD đã được include sau refactor lần trước) |
| File STUB mở rộng | — | 5 (mở rộng tiêu chí) | +5 |
| OCR Gate pass rate (sample 5) | 1/5 (20%) | 5/5 (100%) | +80% |

**Nhận xét tích cực**: Sample OCR Quality Gate đợt này 100% pass. Có thể do random chọn vào các file đã hoàn thiện tốt (65/TT-BGDDT, 295/NĐ-CP, 115/TT-BQP, 318/NĐ-CP đều có format chuẩn).

---

**Phiên thực hiện**
- agent: github-io:subagent:377c20c9-1706-45ac-b60c-1a0bfd583bb1 (Đệ #4 Content Reviewer + PR Comment Reviewer)
- Ngày: 2026-08-22 09:05 ICT Asia/Saigon
- Branch: `heartbeat/crawl-vanban-20260807` (PR #264 active)
- Output: Review report này + entry cập nhật LEGISLATION_TRACKING.md

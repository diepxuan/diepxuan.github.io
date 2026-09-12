# BÁO CÁO REVIEW - ĐỆ #4 REVIEWER
**Ngày:** 2026-08-18 08:34 GMT+7  
**Session:** agent:github-io:subagent:16932b95-6d51-4c10-a63c-a65d1b5216ba

---

## 1. FILE CẦN REFACTOR (Metadata "Đang cập nhật" + < 10KB + lastedit > 7 ngày)

| # | File | Kích thước | Last Modified | Vấn đề |
|---|------|-----------|---------------|--------|
| 1 | `van-ban/tai-chinh/thong-tu-105-2026-tt-btc.md` | 6,020 bytes | 2026-08-04 | Metadata có "Đang cập nhật" cho Ngày công báo & Số công báo |
| 2 | `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` | 1,574 bytes | 2026-07-23 | Stub file - status "Đang cập nhật (stub)", chờ OCR từ PDF |
| 3 | `van-ban/xay-dung/62-2026-tt-bxd-qcvn-32-duong-sat-do-thi-metro.md` | 1,557 bytes | 2026-08-04 | Stub file - "Đang cập nhật nội dung", QCVN 32:2026/BXD chưa có toàn văn |

> **Đã cập nhật LEGISLATION_TRACKING.md** - Đã đánh dấu 3 file này vào danh sách cần refactor.

---

## 2. VĂN BẢN "HOÀN THIỆN" TỪ LEGISLATION_TRACKING.md

| # | Số hiệu | File | Trạng thái tracking | Ngày hoàn thành |
|---|---------|------|---------------------|-----------------|
| 1 | 315/2026/NĐ-CP | `van-ban/315-2026-nd-cp.md` | Hoàn thiện | 2026-08-17 |
| 2 | 312/2026/NĐ-CP | `van-ban/hanh-chinh/nghi-dinh-312-2026-nd-cp.md` | Hoàn thiện | 2026-08-16 |
| 3 | 136/2026/TT-BCA | `van-ban/hanh-chinh/thong-tu-136-2026-tt-bca.md` | Hoàn thiện | 2026-08-15 |
| 3 | 314/2026/NĐ-CP | `van-ban/314-2026-nd-cp.md` | Hoàn thiện | 2026-08-16 |

---

## 3. KẾT QUẢ OCR QUALITY GATE (10 file review)

### 3.1 File PASS hoàn toàn (OCR issues = 0, Articles OK, Chapters OK)

| File | Lines | Articles | Chapters | Đánh giá |
|------|-------|----------|----------|----------|
| `van-ban/hanh-chinh/nghi-dinh-312-2026-nd-cp.md` | 155 | 17 (1-17) | 4 | **PASS** |
| `van-ban/314-2026-nd-cp.md` | 162 | 8 (1-8) | 2 | **PASS** |
| `van-ban/tai-chinh/nghi-dinh-316-2026-nd-cp.md` | 139 | 1 | 0 | **PASS** |
| `van-ban/tai-chinh/nghi-dinh-318-2026-nd-cp.md` | 95 | 10 (1-10) | 0 | **PASS** |

### 3.2 File CẦN SỬA (OCR issues > 0)

| File | Lines | Articles | OCR Issues | Chi tiết lỗi |
|------|-------|----------|------------|--------------|
| `van-ban/315-2026-nd-cp.md` | 200 | 17 (1-17) | **5** | `ngày l` (5 lần, dòng 113, 116, 125, 143, 153) → sửa thành `ngày 1` |
| `van-ban/cong-an/127-2026-tt-bca-qcvn-13-co-so-giam-giu.md` | 716 | 4 (1-4) | **1** | `ngày l` (dòng 434) → sửa thành `ngày 1` |
| `van-ban/ngoai-giao/nghi-dinh-293-2026-nd-cp-apostille-hieu-luc-ngay.md` | 590 | 37 (1-37) | **13** | `ngày l` (13 lần, dòng 201, 235, 269, 271, 273...) → sửa thành `ngày 1` |
| `van-ban/ngan-hang/thong-tu-04-2026-tt-nhnn-bao-hiem-tien-gui.md` | 241 | 15 (1-15) | **10** | `ngày l` (10 lần, dòng 67, 108, 116, 118, 126...) → sửa thành `ngày 1` |

### 3.3 File CẦN CHUẨN HÓA CẤU TRÚC (Suspicious article headings)

| File | Vấn đề | Chi tiết |
|------|--------|----------|
| `van-ban/hanh-chinh/thong-tu-136-2026-tt-bca.md` | 5 suspicious articles | Dùng `**Điều X.**` thay vì `### Điều X.` (dòng 36, 39, 43, 85, 89) |
| `van-ban/lao-dong/nghi-dinh-162-2026-nd-cp-dieu-chinh-luong-huu-tro-cap-bhxh-tro-cap-hang-thang.md` | 6 suspicious articles + 1 OCR | Dùng `**Điều X.**` (dòng 95, 119, 131, 139, 156) + ký tự `ø` (dòng 214) |

---

## 4. TỔNG KẾT OCR GATE

| Tiêu chí | Kết quả |
|----------|---------|
| Tổng file scan | 10 |
| PASS hoàn toàn | 4 |
| Cần sửa OCR (ngày l) | 5 |
| Cần chuẩn hóa heading Điều | 2 |
| **Tổng lỗi "ngày l" phát hiện** | **29 lỗi** |
| **Tổng lỗi ký tự rác khác** | **1 (ø)** |

> **Lưu ý:** File `van-ban/315-2026-nd-cp.md` được tracking ghi là "Pass Quality Gate" nhưng thực tế còn 5 lỗi `ngày l`. Cần fix trước khi merge.

---

## 5. BÁO CÁO PR COMMENTS

### PR #264 - "Heartbeat crawl-vanban 2026-08-07/08/09: review + discovery v100-v106 + 5 VB hoàn thiện"

| Thông tin | Giá trị |
|-----------|---------|
| **Author** | caothu159 (Trần Ngọc Đức) |
| **Created** | 2026-08-07T05:03:22Z |
| **State** | Open |
| **Comments** | **0 comments** |

### Phân loại PR comments

| Loại | Số lượng | Danh sách |
|------|----------|-----------|
| **Cần xử lý ngay** | 0 | - |
| **Chờ Sếp review** | 1 | PR #264 (chưa có comment review) |
| **Thông báo** | 0 | - |
| **Đã stale** | 0 | - |

> **Nhận xét:** PR #264 đã mở 11 ngày (từ 07/08) nhưng chưa có comment review nào. Cần Sếp review hoặc assign reviewer.

---

## 6. KHUYẾN NGHỊ HÀNH ĐỘNG

### 6.1 Ưu tiên cao (Fix ngay)
1. **Fix 29 lỗi "ngày l" → "ngày 1"** trong 5 file:
   - `van-ban/315-2026-nd-cp.md` (5 lỗi)
   - `van-ban/cong-an/127-2026-tt-bca-qcvn-13-co-so-giam-giu.md` (1 lỗi)
   - `van-ban/ngoai-giao/nghi-dinh-293-2026-nd-cp-apostille-hieu-luc-ngay.md` (13 lỗi)
   - `van-ban/ngan-hang/thong-tu-04-2026-tt-nhnn-bao-hiem-tien-gui.md` (10 lỗi)

2. **Fix ký tự `ø`** trong `van-ban/lao-dong/nghi-dinh-162-2026-nd-cp-dieu-chinh-luong-huu-tro-cap-bhxh-tro-cap-hang-thang.md` (dòng 214)

### 6.2 Ưu tiên trung bình (Chuẩn hóa cấu trúc)
3. **Chuẩn hóa heading Điều** từ `**Điều X.**` → `### Điều X.`:
   - `van-ban/hanh-chinh/thong-tu-136-2026-tt-bca.md` (5 Điều)
   - `van-ban/lao-dong/nghi-dinh-162-2026-nd-cp-dieu-chinh-luong-huu-tro-cap-bhxh-tro-cap-hang-thang.md` (6 Điều)

### 6.3 Ưu tiên thấp (Refactor stub)
4. **Bổ sung nội dung 3 file stub** (đã đánh dấu trong LEGISLATION_TRACKING.md):
   - `van-ban/tai-chinh/thong-tu-105-2026-tt-btc.md` - Cập nhật Ngày công báo, Số công báo
   - `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` - OCR từ PDF signed
   - `van-ban/xay-dung/62-2026-tt-bxd-qcvn-32-duong-sat-do-thi-metro.md` - Cập nhật QCVN 32:2026/BXD

### 6.4 Quản trị PR
5. **PR #264**: Cần Sếp review hoặc assign reviewer (đã 11 ngày không có comment)

---

## 7. SCRIPT AUTO-FIX GỢI Ý

```bash
# Fix "ngày l" -> "ngày 1" cho 5 file
sed -i 's/ngày l/ngày 1/g' \
  van-ban/315-2026-nd-cp.md \
  van-ban/cong-an/127-2026-tt-bca-qcvn-13-co-so-giam-giu.md \
  van-ban/ngoai-giao/nghi-dinh-293-2026-nd-cp-apostille-hieu-luc-ngay.md \
  van-ban/ngan-hang/thong-tu-04-2026-tt-nhnn-bao-hiem-tien-gui.md

# Fix "ngày L" -> "ngày 1" (nếu có)
sed -i 's/ngày L/ngày 1/g' \
  van-ban/315-2026-nd-cp.md \
  van-ban/cong-an/127-2026-tt-bca-qcvn-13-co-so-giam-giu.md \
  van-ban/ngoai-giao/nghi-dinh-293-2026-nd-cp-apostille-hieu-luc-ngay.md \
  van-ban/ngan-hang/thong-tu-04-2026-tt-nhnn-bao-hiem-tien-gui.md

# Fix ø -> g) trong file lao-dong
sed -i 's/ø)/g)/g' van-ban/lao-dong/nghi-dinh-162-2026-nd-cp-dieu-chinh-luong-huu-tro-cap-bhxh-tro-cap-hang-thang.md
```

---

*Báo cáo tạo tự động bởi Đệ #4 Reviewer session.*
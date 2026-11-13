# TASK_OCR_FREE_MODEL.md

**Trạng thái**: CHỜ SẾP DUYỆT
**Loại**: Task nghiên cứu / nâng cấp pipeline OCR
**Ngày tạo**: 2026-11-12
**Liên quan**: `documents/OCR_QUALITY_GATE.md`, `scripts/ocr_pdf.py`, `HEARTBEAT.md` mục 3

---

## 1. Vấn đề

Pipeline OCR hiện tại dùng `tesseract -l vie` trên ảnh `pdftoppm`. Chất lượng **không đủ**
cho văn bản pháp luật: sai dấu, sai từ, sai số hiệu → **sai nghĩa pháp lý**.

Bằng chứng từ đợt sửa 2026-11-12 (sau khi PR #266 merge):

| Lỗi | Số chỗ | File dính |
|---|---|---|
| `chỉ thường xuyên` (đúng: `chi thường xuyên`) | 48 | 10 |
| `thâm quyền` / `thấm quyền` (đúng: `thẩm quyền`) | 49 | 14 |
| `chuyên đổi số` (đúng: `chuyển đổi số`) | 9 | 9 |
| `hăng năm` (đúng: `hằng năm`) | 6 | 5 |
| Ký tự rác `¬ © § † ø ®` | 91 dòng | 21 |

Đây chỉ là phần **phát hiện được bằng pattern**. Lỗi sai nghĩa nhưng không khớp pattern
thì **không ai biết**. Đó là rủi ro pháp lý thật.

## 2. Thực nghiệm đã chạy (2026-11-12)

### Thiết lập
- PDF mẫu: `136-btc.signed.pdf` (392 KB, 2 trang) — Thông tư 136/2026/TT-BTC.
- Ảnh: `pdftoppm -r 200 -png`, trang 1 (466 KB).
- Model truy cập qua 9router `http://10.0.0.101:3000/v1`, ảnh gửi dạng base64 data URL.

### Kết quả

| Model | Kết quả | Thời gian |
|---|---|---|
| `tesseract 5.3` (baseline) | 7 lỗi/trang | ~1 s |
| `llmfree-tier` | **Chính xác** | 15 s |
| `llmfree` | Trả về rỗng | 23 s |
| `ocz/glm-5.3-flash-free` | 429 FreeUsageLimitError | 1 s |
| `openrouter/google/gemma-4-31b-it:free` | 429 provider error | 1 s |

### So sánh trực tiếp trên cùng trang, cùng ảnh

**Tesseract 5.3 (`-l vie`, 200 DPI):**
```
Số: 136/2026/TT-BTC Hà Nội, ngày 14 tháng 9 năm 2026

THÔNG TƯ

Sữa đổi, bồ sung khoăn 2 Điều 3 của Thông tư số 158/2025/TT-BTC ngày 31
tháng 12 năm 2025 của Bộ trưởng Bộ Tài chính quy định chỉ tiết một số
...
Căn cứ Luật Thuế tiêu thụ đặc biệt số 66/2025/QH15 được sửa đối, bỏ
sung bởi Luật sô 09/2026/QH16;
...
Căn cứ Nghị định số ) 29/2025/NĐ-CP của Chính phủ quy định chức năng,
nhiệm vụ, quyên hạn và cơ cầu tỖ chức của Bộ Tài chính ...
```

**`llmfree-tier` (cùng ảnh):**
```
Số: 136/2026/TT-BTC
Hà Nội, ngày 14 tháng 9 năm 2026

THÔNG TƯ

Sửa đổi, bổ sung khoản 2 Điều 3 của Thông tư số 158/2025/TT-BTC ngày 31 tháng 12 năm 2025 của Bộ trưởng Bộ Tài chính quy định chi tiết một số điều của Nghị định số 360/2025/NĐ-CP ...
...
Căn cứ Luật Thuế tiêu thụ đặc biệt số 66/2025/QH15 được sửa đổi, bổ sung bởi Luật số 09/2026/QH16;
...
Căn cứ Nghị định số 360/2025/NĐ-CP của Chính phủ quy định chi tiết thi hành một số điều ...
```

**Đối chiếu từng lỗi:**

| # | Tesseract | Đúng (model đọc ra) | Loại lỗi |
|---|---|---|---|
| 1 | `Sữa đổi` | `Sửa đổi` | sai dấu thanh |
| 2 | `bồ sung` | `bổ sung` | sai dấu thanh |
| 3 | `khoăn` | `khoản` | sai dấu |
| 4 | `chỉ tiết` | `chi tiết` | sai dấu thanh |
| 5 | `sửa đối` | `sửa đổi` | sai dấu thanh |
| 6 | `bỏ sung` | `bổ sung` | sai dấu thanh |
| 7 | `Luật sô 09` | `Luật số 09` | sai dấu |
| 8 | `Nghị định số ) 29` | `Nghị định số 360` | **mất chữ số** |
| 9 | `cơ cầu tỖ chức` | `cơ cấu tổ chức` | sai dấu |
| 10 | `Thôi gian ký: ... 16:80: 0` | `Thời gian ký: 14/09/2026 16:50:00 +07:00` | sai giờ |
| 11 | `quy định chỉ tiết thị hành` | `quy định chi tiết thi hành` | sai dấu |

**Kết luận**: 11 lỗi trên 1 trang, model sửa đúng cả 11. Đặc biệt lỗi #8 (`số ) 29` →
`số 360`) là loại **làm sai số hiệu văn bản** — nguy hiểm nhất về pháp lý, tesseract
không tự phát hiện được bằng pattern.

Ghi chú trung thực: đây là mẫu nhỏ (1 trang, 1 PDF). Chưa đủ để kết luận thống kê —
đó chính là lý do cần Bước 1 và 2 ở mục 6.

## 3. Rủi ro phải kiểm soát

| Rủi ro | Mức | Cách xử lý |
|---|---|---|
| **Model bịa nội dung** (hallucination) | NGHIÊM TRỌNG | Không dùng làm nguồn duy nhất. Chỉ dùng đối chiếu/soát lỗi |
| Rate limit free tier | Cao | Đã gặp 429 ở 2/5 model. Cần fallback + backoff |
| Không tất định (cùng ảnh, khác kết quả) | Cao | Chạy 2 lần, chỉ chấp nhận chỗ trùng khớp |
| Giới hạn context | Trung bình | 128K token ≈ 15-25 trang/lần. Văn bản dài phải chia |
| Chi phí ẩn khi hết free | Trung bình | Theo dõi, có ngưỡng dừng |
| Chậm hơn tesseract 15-30x | Thấp | Chấp nhận được nếu chạy nền |

**Nguyên tắc bất di bất dịch**: với văn bản pháp luật, **không bao giờ** để model tự do
sinh nội dung. Mọi ký tự đầu ra phải truy được về ảnh gốc.

## 4. Phương án

### Phương án A — Thay thế hoàn toàn tesseract (KHÔNG KHUYẾN NGHỊ)

Dùng model vision đọc thẳng ảnh, bỏ tesseract.

- Ưu: chất lượng cao nhất, một bước.
- Nhược: **vi phạm nguyên tắc không bịa**; không tất định; rate limit chặn giữa chừng;
  không kiểm chứng được khi model sai.
- Rủi ro: **RẤT CAO** cho văn bản pháp luật.

### Phương án B — Tesseract + LLM hậu kiểm (KHUYẾN NGHỊ)

Giữ tesseract làm nguồn chính, dùng model free để **soát lỗi**:

```
PDF → pdftoppm 200dpi → tesseract → text thô
                                      ↓
                         model free đọc cùng ảnh → text đối chứng
                                      ↓
                         so khớp 2 nguồn: chỗ nào khác → đánh dấu REVIEW
                                      ↓
                    người/agent quyết định, ghi lại quyết định
```

- Ưu: hai nguồn độc lập; chỗ khác nhau chính là chỗ **cần người xem**; vẫn giữ được
  khả năng truy vết về ảnh gốc; không phụ thuộc một model.
- Nhược: chậm gấp đôi; cần công cụ so khớp; vẫn phải review thủ công phần khác biệt.
- Rủi ro: **THẤP** — model chỉ đề xuất, không tự quyết.

### Phương án C — LLM làm nguồn chính, tesseract kiểm tra (TRUNG BÌNH)

Đảo vai trò: model đọc trước, tesseract xác nhận chỗ mơ hồ.

- Ưu: tận dụng chất lượng model; tesseract chỉ để chặn hallucination.
- Nhược: nếu model bịa cả một câu trôi chảy, tesseract khó phát hiện vì câu vẫn "hợp lệ".
- Rủi ro: **TRUNG BÌNH** — nguy hiểm hơn B vì model được quyền chủ động.

### Phương án D — OCR theo cấp độ, chỉ dùng LLM khi cần

Tesseract chạy trước, đo "độ nghi ngờ" (confidence, mật độ ký tự lạ, số từ ngoài từ điển).
Chỉ những trang/đoạn vượt ngưỡng mới đưa qua model free.

- Ưu: tiết kiệm nhất; chỉ dùng model ở chỗ thật sự cần; nhanh nhất.
- Nhược: phải xây bộ đo độ nghi ngờ; tesseract có thể sai mà vẫn tự tin.
- Rủi ro: **TRUNG BÌNH** — phụ thuộc chất lượng bộ đo.

## 5. So sánh

| Tiêu chí | A — thay thế | B — hậu kiểm | C — đảo vai trò | D — theo cấp độ |
|---|---|---|---|---|
| Chất lượng | Cao nhất | Cao | Cao | Trung bình-cao |
| An toàn pháp lý | Rất thấp | **Cao** | Trung bình | Trung bình |
| Truy vết về ảnh gốc | Khó | **Có** | Có | Có |
| Chi phí/thời gian | Cao | Trung bình | Trung bình | **Thấp** |
| Phụ thuộc model | Toàn bộ | Một phần | Lớn | Nhỏ |
| Công sức xây | Thấp | Trung bình | Trung bình | **Cao** |

**Khuyến nghị: Phương án B**, có thể tiến hoá lên D sau khi có số liệu tin cậy.

## 6. Kế hoạch triển khai đề xuất (Phương án B)

### Bước 1 — Đo baseline (chưa đổi gì)
- Chọn 10 văn bản đã có kết quả kiểm định thủ công (đã biết đúng).
- Chạy tesseract, đếm lỗi so với bản đúng → biết tỉ lệ lỗi hiện tại.
- Mục tiêu: có con số cụ thể, không phán đoán.

### Bước 2 — Thử nghiệm hậu kiểm trên 10 văn bản đó
- Chạy model free, so khớp với tesseract.
- Đo: bao nhiêu % chỗ khác biệt là **sửa đúng**, bao nhiêu % là **model bịa**.
- Đây là con số quyết định: nếu model bịa > 10% thì không dùng.

### Bước 3 — Nếu đạt ngưỡng, viết `scripts/ocr_crosscheck.py`
```
Input:  PDF
Output: - text chính (tesseract)
        - danh sách chỗ khác biệt, kèm ảnh crop để review
        - báo cáo: số chỗ khác, mức độ nghi ngờ
```

### Bước 4 — Tích hợp vào quy trình
- Cập nhật `HEARTBEAT.md` mục 3 và `OCR_QUALITY_GATE.md`.
- Quy tắc: file có chỗ khác biệt chưa review **không được** đánh dấu Hoàn thiện.
- Ngoại lệ vẫn cho stub khi không xác minh được.

### Bước 5 — Đo lại
- So tỉ lệ lỗi sau cải tiến với baseline bước 1.
- Nếu không cải thiện rõ, dừng và báo cáo trung thực.

## 7. Việc cần Sếp quyết

1. Chọn phương án **A / B / C / D** (đề xuất B).
2. Có đồng ý chạy bước 1-2 (đo baseline, không đổi code) trước không.
3. Ngưỡng chấp nhận: model được phép bịa tối đa bao nhiêu % để còn dùng.
4. Có cho phép dùng model free ngoài `llmfree-tier` không (ví dụ trả phí khi cần).

## 8. Ghi chú kỹ thuật

- Endpoint 9router đã kiểm: 114 model, nhiều model có `vision: true`, một số có `pdf: true`
  (`llmfree`, `glm`, `llmcoder`, `deepseek-flash`, `gpt-5.5`).
- `llmfree-tier`: context 1.000.000, vision, không PDF → phải convert ảnh trước.
- `ocz/glm-5.3-flash-free`: có cả vision + pdf, nhưng đã gặp rate limit khi test.
- Ảnh 200 DPI PNG ~466 KB/trang → base64 ~620 KB. Với context 128K, chỉ gửi được
  vài trang/lần. Nên dùng 150 DPI hoặc JPEG để giảm.
- Không tự thay đổi pipeline hiện tại cho tới khi Sếp duyệt.

## 9. Câu hỏi mở

- Có nguồn PDF nào **có sẵn text layer** (không phải scan) để so sánh không?
  Nếu có, đó là ground truth tốt nhất, tốt hơn cả hai phương án.
- Các văn bản đã sửa thủ công trong đợt 2026-11-12 có thể dùng làm bộ test chuẩn không?
- Có cần giữ khả năng OCR hoàn toàn offline (không gọi mạng) không?

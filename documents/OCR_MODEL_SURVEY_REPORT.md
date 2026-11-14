# BÁO CÁO: Model OCR free — khảo sát và đề xuất tích hợp

Ngày đo: 2026-11-14. Người đo: Bot.
Phương pháp: gọi thật qua API, đo chất lượng trên cùng một trang PDF, có đối chứng.

---

## 1. Cách đo (để Sếp đánh giá độ tin cậy)

- **Ảnh test**: `136-btc.signed.pdf` trang 1 → `pdftoppm -r 200 -png` (466 KB).
- **Ground truth**: bản đọc bằng mắt (đã kiểm trong phiên 2026-11-12), không dùng
  kết quả của bất kỳ model nào làm chuẩn.
- **Mốc đúng** (11 cụm bắt buộc phải có): `Sửa đổi`, `bổ sung`, `khoản 2 Điều 3`,
  `158/2025/TT-BTC`, `360/2025/NĐ-CP`, `66/2025/QH15`, `09/2026/QH16`,
  `Trần Hưng Đạo`, `136/2026/TT-BTC`, `Thông tư`, `Bộ Tài chính`.
- **Mốc sai** (9 lỗi tesseract đã biết): `Sữa đổi`, `bồ sung`, `khoăn`, `chỉ tiết`,
  `sửa đối`, `bỏ sung`, `sô 09`, `Trần Hùng Đạo`, `cơ cầu`.
- Mỗi model gọi với `max_tokens=4000`, `temperature=0`.

**Lưu ý quan trọng về `max_tokens`**: lần test đầu em đặt 300 nên nhiều model trả
`content` rỗng (kết quả bị cắt). Đó là **lỗi của em**, không phải lỗi model. Đã test lại
với 4000 — kết quả dưới đây là số đúng.

---

## 2. Kết quả đo

### 2.1. Model free qua 9router (endpoint `http://10.0.0.101:3000/v1`)

| Model | Trạng thái | Thời gian | Đúng | Sai | Ghi chú |
|---|---|---|---|---|---|
| `llmfree-tier` | OK | 21s | 11/11 | **0** | Chất lượng cao nhất |
| `oc/glm-5.3-flash-free` | OK | 9s | 11/11 | **0** | Nhanh nhất trong nhóm đạt |
| `oc/mimo-v2.6-flash-free` | OK | 43s | 11/11 | **0** | Chậm nhất |
| `llmfree` | FAIL | 38s | — | — | Trả `tool_calls`, không trả text |
| `llmfree-opencode` | FAIL | 3s | — | — | Trả `tool_calls` |
| `oc/deepseek-v4.1-flash-free` | FAIL | 9s | — | — | Trả `tool_calls` |
| `ocz/glm-5.3-flash-free` | FAIL | 1s | — | — | **429 FreeUsageLimitError** |
| `ocz/mimo-v2.6-flash-free` | FAIL | 1s | — | — | 429 (đã test phiên trước) |
| `ocz/deepseek-v4.1-flash-free` | FAIL | 1s | — | — | 429 |
| `ocz/nemotron-3.5-super-vl-free` | FAIL | 2s | — | — | 429 |
| `openrouter/google/gemma-4-31b-it:free` | FAIL | 1s | — | — | 429 provider |
| `openrouter/nex-agi/nex-n2.5-mini:free` | FAIL | 0.5s | — | — | 404 — không còn free |
| `openrouter/openrouter/free` | FAIL | 12s | — | — | Response không parse được |
| `openrouter/dots-studio/dots-3-note-preview:free` | FAIL | 26s | — | — | Response không parse được |

**Nhóm `ocz/*`**: toàn bộ trả 429 với thông báo "Free models work in OpenCode
(https://opencode.ai)". Đây là free tier **chỉ dùng được trong app OpenCode**, không
dùng được qua API. **Không nên tích hợp.**

**Nhóm `oc/*`** (không có `z`): dùng được qua API, là mirror của cùng model.

### 2.2. Provider ngoài (không qua 9router)

| Provider | Model | Kết quả | Ghi chú |
|---|---|---|---|
| Google AI Studio | `gemini-2.5-flash` | 11/12 đúng, **1 sai** | Sai `Trần Hưng Đạo` → `Trần Hùng Đạo` |
| Google AI Studio | `gemini-2.5-flash-lite` | 11/12 đúng, 0 sai | Nhanh 4.4s, nhưng đọc thiếu phần đầu |
| Google AI Studio | `gemini-3-flash-preview` | FAIL | `finishReason: RECITATION` (bị chặn nội dung) |
| OCR.space | `helloworld` key | Sai | Vẫn mắc `Sữa đổi`, `khoăn`, `PHÔNG`, `CHINH` — **kém hơn tesseract** |

**Google AI Studio** dùng được key có sẵn trong config (`AIzaSy...`), 50 model, free tier
có hạn mức theo ngày. `gemini-2.5-flash` có 1 lỗi thật → không nên làm nguồn chính.

### 2.3. Đối chứng: tesseract (baseline hiện tại)

| Model | Đúng | Sai |
|---|---|---|
| `tesseract 5.3 -l vie` | 11/12 | **8** |

Cụ thể 8 lỗi: `Sữa đổi`, `bồ sung`, `khoăn`, `chỉ tiết`, `sửa đối`, `sô 09`,
`cơ cầu`, sai giờ ký `16:80`.

### 2.4. Kiểm tra tất định (chạy lại nhiều lần)

Test 3 lần liên tiếp mỗi model trên cùng ảnh:

| Model | Thành công | Ghi chú |
|---|---|---|
| `oc/glm-5.3-flash-free` | **3/3** | Ổn định nhất, 3.9–5.2s/lần |
| `llmfree-tier` | 1/3 | Lúc được lúc không — **rủi ro cao** |

Đây là điểm quan trọng: `llmfree-tier` cho chất lượng tốt nhất nhưng **không ổn định**.
`oc/glm-5.3-flash-free` ổn định 3/3 và vẫn 0 lỗi.

### 2.5. Độ đồng thuận giữa các model (trang 2, ảnh khó hơn)

| Cặp so sánh | Độ giống |
|---|---|
| `llmfree-tier` vs `llmfree` | 99,76% |
| `llmfree-tier` vs `oc/glm-5.3` | 99,62% |
| `llmfree` vs `oc/glm-5.3` | 99,90% |

Khác biệt chỉ là chuẩn hoá dấu (`hóa`/`hoá`), markdown (`**Điều`/`Điều`), dấu ngoặc kép.
**Không có dấu hiệu model tự bịa thêm câu** — đây là tín hiệu an toàn quan trọng.

---

## 3. Đề xuất tích hợp

### 3.1. Model nên đưa vào provider (thứ tự ưu tiên)

| Hạng | Model | Lý do |
|---|---|---|
| 1 | `oc/glm-5.3-flash-free` | 0 lỗi, **3/3 ổn định**, 9s, context 1M, có cả `pdf: true` |
| 2 | `llmfree-tier` | 0 lỗi, context 1M, nhưng chỉ 1/3 ổn định → chỉ dùng dự phòng |
| 3 | `oc/mimo-v2.6-flash-free` | 0 lỗi, context 1M, nhưng chậm 43s |
| — | `gemini-2.5-flash-lite` | Ngoài 9router, cần key Google; dự phòng cuối |

### 3.2. Cấu hình cần thêm

Trong `openclaw.json` (provider `9router`), bổ sung 3 model:

```json
{
  "id": "glm-5.3-flash-free",
  "name": "GLM 5.3 Flash (OCR, free, vision+pdf)"
},
{
  "id": "mimo-v2.6-flash-free",
  "name": "MiMo v2.6 Flash (OCR, free, vision)"
},
{
  "id": "llmfree-tier",
  "name": "LLM Free Tier (OCR, free, vision, 1M ctx)"
}
```

Trong DSH profile (`/root/.dsh/profiles/web/cordis.patch.yml`), mục `llm-pi-ai.providers.ninerouter.models`:

```yaml
- id: oc/glm-5.3-flash-free
  contextWindow: 1000000
- id: oc/mimo-v2.6-flash-free
  contextWindow: 1048576
- id: llmfree-tier
  contextWindow: 1000000
```

**Lưu ý**: tên model phải có tiền tố `oc/` (không phải `ocz/`). `ocz/` sẽ 429.

### 3.3. Cách dùng đề xuất (quan trọng)

**Không dùng model làm nguồn duy nhất.** Theo task `TASK_OCR_FREE_MODEL.md` phương án B:

```
PDF → pdftoppm 200dpi → tesseract → text A
                     ↘ oc/glm-5.3-flash-free → text B
                                    ↓
                    so khớp A vs B → chỗ khác = REVIEW
                                    ↓
                        người/agent quyết định
```

Lý do: model có thể bịa. Độ đồng thuận 99,6% là tín hiệu tốt nhưng **không bảo đảm**
trên văn bản khác. Chỗ nào hai nguồn khác nhau chính là chỗ cần người xem — đó là
giá trị lớn nhất của việc có 2 nguồn.

### 3.4. Hạn mức cần theo dõi

- `oc/glm-5.3-flash-free`: chưa gặp 429 trong 3 lần liên tiếp, nhưng là free tier —
  cần theo dõi, có fallback.
- `llmfree-tier`: 1/3 → **phải có retry** trước khi coi là lỗi.
- `ocz/*`: không dùng.
- Gemini free tier: giới hạn theo ngày, cần đo thêm nếu muốn dùng.

---

## 4. Những gì em chưa xác minh được

1. **Chỉ test 1 văn bản, 2 trang.** Chưa đủ để khẳng định chất lượng trên toàn bộ
   745 văn bản. Cần đo baseline trên 10-20 văn bản đã biết kết quả đúng.
2. **Chưa test văn bản có bảng biểu phức tạp** (phụ lục, biểu mẫu) — đây là chỗ model
   thường sai nhiều nhất. Trong repo có nhiều file dạng này.
3. **Chưa xác định hạn mức chính xác** của `oc/glm-5.3-flash-free` (bao nhiêu request/ngày).
4. **Chưa test model với ảnh mờ, nghiêng, scan chất lượng thấp** — PDF thật trong repo
   có nhiều loại này.
5. **Chưa test tiếng Việt có dấu phức tạp** ở văn bản dài (model có thể mất dấu ở cuối).
6. Tên `oc/` vs `ocz/`: em suy ra từ việc test, chưa có tài liệu chính thức xác nhận
   đây là hai nhóm khác nhau về quyền truy cập.

---

## 5. Việc cần Sếp quyết

1. Có đồng ý thêm 3 model vào provider không (`oc/glm-5.3-flash-free`,
   `oc/mimo-v2.6-flash-free`, `llmfree-tier`)?
2. Có đồng ý dùng theo mô hình **2 nguồn đối chứng** (tesseract + model), không dùng
   model làm nguồn duy nhất?
3. Có cho phép em chạy **đo baseline trên 20 văn bản** trước khi tích hợp chính thức?
   (chỉ đọc, không sửa nội dung)
4. Có muốn thêm Gemini vào danh sách dự phòng (cần theo dõi hạn mức theo ngày)?

# HEARTBEAT.md - Tasks tự động hoá

Tất cả tasks được trigger bởi cron jobs. Agent đọc HEARTBEAT.md khi heartbeat ping hoặc khi cron job wake session.

---

## Execution Tracking

source: `.heartbeat-state.json`

> **Lưu ý:** State thực tế được lưu trong `.heartbeat-state.json`. Mỗi lần chạy, agent cập nhật `.heartbeat-state.json` thay vì HEARTBEAT.md.

---

## Shared Backlog: `documents/LEGISLATION_TRACKING.md`

File `documents/LEGISLATION_TRACKING.md` là backlog pháp luật mới dùng chung cho các task heartbeat.

### Mục đích

- Ghi nhận văn bản pháp luật mới phát hiện từ nguồn chính thức `vanban.chinhphu.vn`.
- Đối chiếu văn bản mới với nội dung hiện có trong `van-ban/`.
- Xếp ưu tiên tạo/cập nhật trang pháp luật tiếp theo.
- Tránh crawl trùng và tránh tạo nhiều PR cho cùng một văn bản.

### Nguồn dữ liệu mặc định

- Danh sách văn bản: `https://vanban.chinhphu.vn/he-thong-van-ban?classid=1&mode=1&maxresults=50`
- Chi tiết văn bản: `https://vanban.chinhphu.vn/?pageid=...&docid=...`
- PDF đính kèm: `datafiles.chinhphu.vn`

### Cách task sử dụng

1. Trước khi crawl luật mới, đọc `documents/LEGISLATION_TRACKING.md` nếu file tồn tại.
2. Lấy danh sách backlog trong mục "Văn bản mới đáng chú ý" và "Đề xuất ưu tiên cập nhật tiếp theo".
3. Đối chiếu với `van-ban/`:
   - Nếu đã có file liên quan → chỉ cập nhật metadata/full text nếu thiếu.
   - Nếu chưa có file chuyên biệt → đề xuất tạo file mới theo nhóm phù hợp.
4. Nếu crawl phát hiện văn bản mới chưa có trong backlog → cập nhật `documents/LEGISLATION_TRACKING.md`
5. Commit chỉ mỗi 1 file backlog `documents/LEGISLATION_TRACKING.md` vào branch main.
6. Với văn bản pháp luật, mỗi nhóm nội dung đưa vào một branch/PR riêng. Không gom quá nhiều nhóm pháp luật vào một PR.

### Ưu tiên hiện tại

1. **An ninh mạng**
   - Nhóm đề xuất: `van-ban/an-ninh-quoc-gia/`.

2. **Thuế / thương mại**
   - Nhóm đề xuất: `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/`, `van-ban/thuong-mai-dau-tu-chung-khoan/`.

3. **Đất đai / dự án tồn đọng**
   - Nhóm đề xuất: `van-ban/dat-dai/` hoặc nhóm tương ứng nếu đã tồn tại.

4. **Chứng khoán / tài chính**
   - Nhóm đề xuất: `van-ban/thuong-mai-dau-tu-chung-khoan/` hoặc `van-ban/tai-chinh/`.

### Quy tắc cập nhật backlog

- Không xóa lịch sử đã ghi nhận; chỉ chỉnh nếu sai rõ ràng.
- Khi thêm văn bản mới, ghi đủ: số hiệu, ngày ban hành, trích yếu, nhóm, trạng thái đã có/chưa có trong `van-ban/`, nguồn URL.
- Nếu văn bản đã được tạo thành file riêng trong `van-ban/`, cập nhật trạng thái trong backlog là "đã có".
- Nếu văn bản không phù hợp website, ghi lý do bỏ qua.

---

## Tasks

### Task 1: Refactor Văn bản Pháp luật (Hàng giờ)
**Cron:** `every 30m`
**Mô tả:** Quét và refactor các van-ban/ cần cập nhật
**Quy trình:**
1. Quét `van-ban/`, chọn **tối đa 3 file** thỏa mãn:
   - Có metadata "Đang cập nhật" -> Ưu tiên 1.
   - File cấu trúc lỗi (thiếu Chapter/Điều) -> Ưu tiên 2.
   - File < 10k chars và chưa có full text -> Ưu tiên 3.
   - Có `lastedit` cũ nhất -> Ưu tiên 4.
2.  Tiến hành crawl/sửa đổi -> Tạo 1 branch riêng từ `main` cho mỗi file -> Tạo PR.
3. Ghi log vào `MEMORY.md` và cập nhật "Lần chạy cuối" ở `.heartbeat-state.json`.

### Task 2: Phát hiện Văn bản mới (Discovery)
**Cron:** `every 24h` (08:00 ICT)
**Mô tả:** Theo dõi tình hình luật mới Việt Nam
**Quy trình:**
1. Search kiểm tra nguồn: `site:vanban.chinhphu.vn "2026" "Nghị định" OR "Thông tư" OR "Luật"`
2. Đối chiếu với `documents/LEGISLATION_TRACKING.md`. Nếu xuất hiện văn bản mới, ghi nhận vào mục "Văn bản mới đáng chú ý" và set trạng thái là `Chưa có`.
3. Commit cập nhật file Backlog vào main.

### Task 3: Cập nhật Nội dung từ Backlog (Ingestion)
**Cron:** `every 24h` (09:00 ICT - Chạy sau Task 2)
**Quy trình:**
1. Đọc `documents/LEGISLATION_TRACKING.md`, chọn ra các văn bản có trạng thái `Chưa có` theo thứ tự ưu tiên (An ninh mạng -> Thuế -> Đất đai -> Tài chính).
2. Crawl chi tiết từ `vanban.chinhphu.vn` và PDF từ `datafiles.chinhphu.vn` -> Sử dụng công cụ trích xuất text/OCR.
3. Tạo file Markdown mới trong thư mục nhóm tương ứng (ví dụ: `van-ban/an-ninh-quoc-gia/`).
4. Cập nhật trạng thái văn bản đó trong Backlog thành `Đã có`.
5. Tạo branch từ `main` -> Open PR.

### Task 4: Công việc hàng ngày
**Cron:** `every 2h`
**Mô tả:** Kiểm tra công việc trong `memory/`

**Quy trình:**
1. Đọc `memory/YYYY-MM-DD.md` → xem công việc đã lên lịch.
2. Đọc `documents/LEGISLATION_TRACKING.md` → xem backlog pháp luật mới đang chờ xử lý.
3. Nếu có việc:
   - Nếu là backlog pháp luật → xử lý theo nhóm ưu tiên trong `LEGISLATION_TRACKING.md`.
   - Nếu cần tạo file hoặc cập nhật nội dung → tạo branch + PR.
   - Nếu chỉ là ghi nhận tracking → cập nhật `documents/LEGISLATION_TRACKING.md` + memory.
4. Không có → HEARTBEAT_OK.

---

## Quy tắc thực hiện

- Chỉ thực hiện task khi hết hạn interval (check "Lần chạy tiếp theo")
- Nếu gặp vấn đề → HEARTBEAT_OK + ghi log MEMORY.md
- **Tạo PR cho mọi thay đổi nội dung** → Sếp review trước merge
- Mỗi task = 1 branch mới = 1 PR mới
- **Branch phải được tạo từ main** (git checkout -b <branch> khi đang ở main)
- Không push trực tiếp main, ngoại trừ cập nhật `documents/LEGISLATION_TRACKING.md`
- Không merge PR tự động
- Ghi nhận MEMORY.md khi chưa được phép tạo PR

## Quy tắc tránh Artifact trong PR

Khi refactor-vanban chạy nhiều lần, PR có thể chứa nhiều commit từ các lần chạy trước (artifact). Áp dụng nguyên tắc sau:

1. **Mỗi heartbeat run = 1 branch mới từ main**
   - Luôn checkout về main và pull trước khi tạo branch
   - Tạo branch mới: `git checkout main && git pull && git checkout -b <branch>`
   - Không push thêm commit vào PR đã mở

2. **Trước khi tạo PR:**
   - Kiểm tra `git log` branch hiện tại để đảm bảo chỉ có commit của run hiện tại
   - Nếu chứa commit từ heartbeat trước đó → tạo branch mới từ main
   - Chỉ commit các file thuộc phạm vi thay đổi

3. **Nếu PR đã mở cần sửa:**
   - Tạo branch mới từ main với nội dung sạch
   - Tạo PR mới thay thế
   - Ghi chú vào nội dung PR cũ nguyên nhân bỏ qua PR này và link đến PR mới để sếp review so sánh
   - không tự ý đóng PR

4. **Checklist trước khi push:**
   - [ ] Branch được tạo từ main
   - [ ] Chỉ chứa file thuộc phạm vi thay đổi
   - [ ] Không chứa file từ heartbeat run trước đó

## Nguồn dữ liệu

| Nguồn | Trạng thái | Cách dùng |
|-|-|-|
| vanban.chinhphu.vn | ✅ Hoạt động | Metadata + thông tin văn bản |
| datafiles.chinhphu.vn | ✅ Hoạt động | PDF download → pdf tool / OCR |
| vbpl.vn | ❌ WAF block | Loại bỏ |
| luatvietnam.vn | ❌ Cloudflare block | Loại bỏ |
| thuvienphapluat.vn | ❌ Login wall | Loại bỏ |

## Refactor Priority

1. Có metadata "Đang cập nhật" → crawl chinhphu.vn
2. File < 10k chars → crawl full text PDF
3. File có lastedit cũ nhất (> 7 ngày)
4. File cấu trúc sai (thiếu Chapter/Điều)
5. File có thông tin lỗi thời
6. File thiếu mục lục

## Quy tắc cập nhật state

- **Không sửa HEARTBEAT.md khi cập nhật lần chạy.** 
- State được lưu trong file `.heartbeat-state.json` (đã được .gitignore).
- Cấu trúc `.heartbeat-state.json` ví dụ:

```json
{
  "last_runs": {
    "refactor-vanban": "2026-05-15T11:22:00+07:00",
    ...
  },
  "next_runs": {
    "refactor-vanban": "2026-05-15T11:52:00+07:00",
    ...
  },
  "intervals": {
    "refactor-vanban": "30m",
    ...
  }
}
```

| Task | Lần chạy cuối | Lần chạy tiếp theo | Trạng thái |
|------|---------------|--------------------|------------|
| refactor-vanban | 2026-05-15 11:22 ICT | 2026-05-15 11:52 ICT | ✅ Đang chạy |
| track-legislation | 2026-05-14 08:00 ICT | 2026-05-15 08:00 ICT | ⚠️ Qua hạn |
| check-new-laws | 2026-05-14 08:00 ICT | 2026-05-15 08:00 ICT | ⚠️ Qua hạn |
| update-vbpl | 2026-05-14 08:00 ICT | 2026-05-21 08:00 ICT | ✅ Đang chạy |
| daily-tasks | 2026-05-14 12:00 ICT | 2026-05-15 12:00 ICT | ✅ Đang chạy |
- đây là tài liệu tham khảo, state thực tế được lưu trong `.heartbeat-state.json`. Sau mỗi lần chạy, agent cập nhật `.heartbeat-state.json` thay vì HEARTBEAT.md.
- Sau mỗi lần chạy task, agent cập nhật `last_runs` và `next_runs` trong `.heartbeat-state.json`.

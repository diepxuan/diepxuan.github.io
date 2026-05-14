# HEARTBEAT.md - Tasks tự động hoá

Tất cả tasks được trigger bởi cron jobs. Agent đọc HEARTBEAT.md khi heartbeat ping hoặc khi cron job wake session.

---

## Execution Tracking

| Task | Lần chạy cuối | Lần chạy tiếp theo | Trạng thái |
|------|---------------|--------------------|------------|
| refactor-vanban | 2026-05-14 12:52 ICT | 2026-05-14 13:22 ICT | ✅ Hoàn thành (metadata) |
| track-legislation | 2026-05-14 08:00 ICT | 2026-05-15 08:00 ICT | ✅ Đang chạy |
| check-new-laws | 2026-05-14 08:00 ICT | 2026-05-15 08:00 ICT | ✅ Đang chạy |
| update-vbpl | 2026-05-14 08:00 ICT | 2026-05-21 08:00 ICT | ✅ Đang chạy |
| daily-tasks | 2026-05-14 10:00 ICT | 2026-05-14 12:00 ICT | ✅ Đang chạy |

---

## Tasks

### Task 1: Refactor Văn bản Pháp luật

**Cron:** `every 30m`
**Trạng thái:** Đang chạy
**Mô tả:** Quét và refactor các van-ban/ cần cập nhật

**Quy trình:**
1. Quét `van-ban/` — kiểm tra:
   - File có `lastedit` cũ > 30m → ưu tiên
   - File có nội dung ngắn < 10k chars → ưu tiên
   - File có metadata "Đang cập nhật" → cần crawl chinhphu.vn
   - File có cấu trúc sai (thiếu Chapter/Điều) → cần fix
2. Với mỗi file cần refactor:
   - Nếu "Đang cập nhật" metadata → `web_search` → `vanban.chinhphu.vn` → `firecrawl_scrape` → update
   - Nếu nội dung thiếu → crawl PDF từ `datafiles.chinhphu.vn` → `pdf` tool hoặc OCR → update
   - Commit → branch mới → tạo PR
3. Ghi log vào `MEMORY.md` và cập nhật "Lần chạy cuối" ở bảng trên
4. Nếu xong → reply HEARTBEAT_OK

### Task 2: Theo dõi Luật mới

**Cron:** `every 24h` (08:00 ICT hàng ngày)
**Trạng thái:** Đang chạy
**Mô tả:** Theo dõi tình hình luật mới Việt Nam

**Quy trình:**
1. `web_search`:
   - `"du an luat" Viet Nam 2026`
   - `"thong tu moi" OR "quyet dinh moi" thang nay`
2. Kiểm tra: kinh tế, pháp lý, xã hội
3. Nếu có luật mới:
   - Ghi nhận `MEMORY.md`: tên, ngày, tiến độ, nguồn
   - Kiểm tra van-ban/ đã có chưa → nếu chưa → ghi nhận để crawl
4. Nếu không có gì mới → HEARTBEAT_OK

### Task 3: Pháp luật mới - Kiểm tra ban hành

**Cron:** `every 24h` (09:00 ICT hàng ngày)
**Trạng thái:** Đang chạy
**Mô tả:** Kiểm tra văn bản pháp luật mới ban hành

**Quy trình:**
1. `web_search`:
   - `"quyet dinh moi ban hanh phap luat Viet Nam 2026"`
   - `"nghi dinh moi 2026"`
2. Check van-ban/ → ghi nguồn nếu chưa có
3. Tạo PR nếu cần update
4. Nếu không có → HEARTBEAT_OK

### Task 4: Cập nhật VBPL

**Cron:** `every 168h` (Tuần, Thứ 5 10:00 ICT)
**Trạng thái:** Đang chạy
**Mô tả:** Kiểm tra cập nhật từ chinhphu.vn

**Quy trình:**
1. `web_search`: `site:vanban.chinhphu.vn "2026" moi nhat`
2. Kiểm tra: an ninh, phòng chống tham nhũng, bảo hiểm, đất đai
3. Nếu có update → check van-ban/ → tạo PR
4. Nếu không → HEARTBEAT_OK

### Task 5: Công việc hàng ngày

**Cron:** `every 2h` (Trong giờ làm việc: 08:00-18:00 ICT)
**Trạng thái:** Đang chạy
**Mô tả:** Kiểm tra công việc trong memory/YYYY-MM-DD.md

**Quy trình:**
1. Đọc `memory/YYYY-MM-DD.md` → xem công việc đã lên lịch
2. Nếu có việc → thực hiện (tạo file, update, PR)
3. Không có → HEARTBEAT_OK

---

## Quy tắc thực hiện

- Chỉ thực hiện task khi hết hạn interval (check "Lần chạy tiếp theo")
- Nếu gặp vấn đề → HEARTBEAT_OK + ghi log MEMORY.md
- **Tạo PR cho mọi thay đổi nội dung** → Sếp review trước merge
- Mỗi task = 1 branch mới = 1 PR mới
- Không push trực tiếp main
- Không merge PR tự động
- Chỉ ghi nhận MEMORY.md khi chưa được phép tạo PR

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

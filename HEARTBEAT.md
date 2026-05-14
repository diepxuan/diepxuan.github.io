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

## Shared Backlog: `documents/LEGISLATION_TRACKING.md`

File `documents/LEGISLATION_TRACKING.md` là backlog pháp luật mới dùng chung cho các task heartbeat.

### Mục đích

- Ghi nhận văn bản pháp luật mới phát hiện từ nguồn chính thức `vanban.chinhphu.vn`.
- Đối chiếu văn bản mới với nội dung hiện có trong `van-ban/`.
- Xếp ưu tiên tạo/cập nhật trang pháp luật tiếp theo.
- Tránh crawl trùng và tránh tạo nhiều PR cho cùng một văn bản.

### Nguồn dữ liệu mặc định

- Danh sách văn bản: `https://vanban.chinhphu.vn/he-thong-van-ban?classid=1&mode=1&maxresults=50`
- Chi tiết văn bản: `https://vanban.chinhphu.vn/?pageid=27160&docid=...`
- PDF đính kèm: `datafiles.chinhphu.vn`

### Cách task sử dụng

1. Trước khi crawl luật mới, đọc `documents/LEGISLATION_TRACKING.md` nếu file tồn tại.
2. Lấy danh sách backlog trong mục "Văn bản mới đáng chú ý" và "Đề xuất ưu tiên cập nhật tiếp theo".
3. Đối chiếu với `van-ban/`:
   - Nếu đã có file liên quan → chỉ cập nhật metadata/full text nếu thiếu.
   - Nếu chưa có file chuyên biệt → đề xuất tạo file mới theo nhóm phù hợp.
4. Nếu crawl phát hiện văn bản mới chưa có trong backlog → cập nhật `documents/LEGISLATION_TRACKING.md` và tạo PR.
5. Mỗi nhóm nội dung đi một branch/PR riêng. Không gom quá nhiều nhóm pháp luật vào một PR.

### Ưu tiên hiện tại

1. **An ninh mạng**
   - 48/2026/TT-BCA: Quy chuẩn kỹ thuật quốc gia về thiết bị camera giám sát sử dụng giao thức Internet - yêu cầu an ninh mạng cơ bản.
   - 47/2026/TT-BCA: Quy chuẩn kỹ thuật quốc gia về an ninh mạng cho hệ thống thông tin lưu trữ tài liệu điện tử trong cơ quan Đảng, Nhà nước.
   - Nhóm đề xuất: `van-ban/an-ninh-quoc-gia/`.

2. **Thuế / thương mại**
   - 143/2026/NĐ-CP: Biểu thuế nhập khẩu ưu đãi đặc biệt CEPA Việt Nam - UAE giai đoạn 2026-2027.
   - 144/2026/NĐ-CP: Sửa đổi Nghị định 181/2025/NĐ-CP hướng dẫn Luật Thuế giá trị gia tăng.
   - 141/2026/NĐ-CP: Chính sách thuế đối với hộ kinh doanh, cá nhân kinh doanh và hướng dẫn Luật Thuế TNDN.
   - Nhóm đề xuất: `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/`, `van-ban/thuong-mai-dau-tu-chung-khoan/`.

3. **Đất đai / dự án tồn đọng**
   - 29/2026/QH16: Cơ chế đặc thù xử lý vi phạm đất đai trước Luật Đất đai 2024 và tháo gỡ dự án tồn đọng.
   - 147/2026/NĐ-CP: Hướng dẫn cơ chế, chính sách đặc thù tháo gỡ dự án tồn đọng, kéo dài.
   - Nhóm đề xuất: `van-ban/dat-dai/` hoặc nhóm tương ứng nếu đã tồn tại.

4. **Chứng khoán / tài chính**
   - 145/2026/NĐ-CP: Cơ chế quản lý tài chính, đánh giá, xếp loại doanh nghiệp đối với Sở GDCK Việt Nam, VSDC.
   - Nhóm đề xuất: `van-ban/thuong-mai-dau-tu-chung-khoan/` hoặc `van-ban/tai-chinh/`.

### Quy tắc cập nhật backlog

- Không xóa lịch sử đã ghi nhận; chỉ chỉnh nếu sai rõ ràng.
- Khi thêm văn bản mới, ghi đủ: số hiệu, ngày ban hành, trích yếu, nhóm, trạng thái đã có/chưa có trong `van-ban/`, nguồn URL.
- Nếu văn bản đã được tạo thành file riêng trong `van-ban/`, cập nhật trạng thái trong backlog là "đã có".
- Nếu văn bản không phù hợp website, ghi lý do bỏ qua.

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
1. Đọc `documents/LEGISLATION_TRACKING.md` để lấy backlog và ưu tiên hiện tại.
2. `web_search` hoặc `firecrawl_search` nếu `web_search` lỗi:
   - `"du an luat" Viet Nam 2026`
   - `"thong tu moi" OR "quyet dinh moi" thang nay`
   - `site:vanban.chinhphu.vn 2026 luật nghị định thông tư mới`
3. Kiểm tra: kinh tế, pháp lý, xã hội.
4. Nếu có luật/văn bản mới:
   - Cập nhật `documents/LEGISLATION_TRACKING.md` với số hiệu, ngày, trích yếu, nhóm, nguồn.
   - Ghi nhận vào `memory/YYYY-MM-DD.md`.
   - Kiểm tra `van-ban/` đã có chưa → nếu chưa → đánh dấu backlog để crawl/tạo file.
   - Tạo branch + PR cho thay đổi backlog.
5. Nếu không có gì mới → HEARTBEAT_OK.

### Task 3: Pháp luật mới - Kiểm tra ban hành

**Cron:** `every 24h` (09:00 ICT hàng ngày)
**Trạng thái:** Đang chạy
**Mô tả:** Kiểm tra văn bản pháp luật mới ban hành

**Quy trình:**
1. Đọc `documents/LEGISLATION_TRACKING.md` trước để tránh trùng lặp.
2. Ưu tiên xử lý backlog theo thứ tự:
   - An ninh mạng: 48/2026/TT-BCA, 47/2026/TT-BCA.
   - Thuế/thương mại: 143/2026/NĐ-CP, 144/2026/NĐ-CP, 141/2026/NĐ-CP.
   - Đất đai/dự án tồn đọng: 29/2026/QH16, 147/2026/NĐ-CP.
3. Crawl chi tiết từ `vanban.chinhphu.vn` và PDF từ `datafiles.chinhphu.vn` nếu có.
4. Check `van-ban/`:
   - Nếu đã có trang → cập nhật metadata/full text.
   - Nếu chưa có trang → tạo file mới trong nhóm phù hợp.
5. Tạo branch + PR cho mỗi nhóm nội dung.
6. Cập nhật trạng thái trong `documents/LEGISLATION_TRACKING.md`.
7. Nếu không có gì cần update → HEARTBEAT_OK.

### Task 4: Cập nhật VBPL

**Cron:** `every 168h` (Tuần, Thứ 5 10:00 ICT)
**Trạng thái:** Đang chạy
**Mô tả:** Kiểm tra cập nhật từ chinhphu.vn

**Quy trình:**
1. Đọc `documents/LEGISLATION_TRACKING.md` để lấy danh sách văn bản cần cập nhật theo nhóm.
2. `web_search` hoặc `firecrawl_search`: `site:vanban.chinhphu.vn "2026" moi nhat`.
3. Kiểm tra các nhóm ưu tiên: an ninh mạng, thuế/thương mại, đất đai/dự án tồn đọng, chứng khoán/tài chính.
4. Nếu có cập nhật mới:
   - Cập nhật backlog trong `documents/LEGISLATION_TRACKING.md`.
   - Check `van-ban/` → tạo/cập nhật file phù hợp.
   - Tạo branch + PR.
5. Nếu không → HEARTBEAT_OK.

### Task 5: Công việc hàng ngày

**Cron:** `every 2h` (Trong giờ làm việc: 08:00-18:00 ICT)
**Trạng thái:** Đang chạy
**Mô tả:** Kiểm tra công việc trong memory/YYYY-MM-DD.md

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

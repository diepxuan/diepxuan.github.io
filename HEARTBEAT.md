# HEARTBEAT - github-io workspace

File này định nghĩa các task định kỳ mà Bột phải thực hiện.
Mỗi task có interval, mô tả, và quy trình rõ ràng.

---

## 1. Task tổng quan

| Task | Interval | Mục đích |
|------|----------|----------|
| `crawl-vanban` | 30m | Đánh thức Bột để gọi đệ thực hiện phương án crawl văn bản pháp luật |

**Quy tắc bắt buộc:**
- Chỉ có DUY NHẤT 1 task này, chạy mỗi 30 phút.
- Mục đích: đánh thức Bột, KHÔNG tự động thực hiện bất kỳ hành động nào.
- Khi task chạy, Bột sẽ đọc lại phương án ở mục 2 và quyết định có gọi đệ hay không.

---

## 2. Phương án crawl văn bản pháp luật

### 2.1. Nguyên tắc tổng quan

1. **Phân tách theo chức năng** - mỗi đệ thực hiện một chức năng riêng biệt
2. **Bột là người ra quyết định** - Bột quyết định gọi đệ nào, khi nào
3. **Chạy theo yêu cầu** - không tự động, chỉ chạy khi Bột yêu cầu
4. **Hết khi Bột quyết định** - Bột có thể dừng lại bất kỳ lúc nào
5. **Áp dụng OCR Pipeline** (mục 3) cho mỗi file PDF có chữ ký số

### 2.2. Các đệ theo chức năng

**Đệ #1: Discovery & Tracking**

- Mục đích: Tìm kiếm văn bản pháp luật trên vanban.chinhphu.vn và các nguồn chính thức
- Quy trình:
  1. Quét vanban.chinhphu.vn theo các nhóm chủ đề (Thuế, Đất đai, KHCN, Lâm nghiệp, Chứng khoán...)
  2. So sánh với danh sách đã có trong `documents/LEGISLATION_TRACKING.md` và `van-ban/`
  3. Phát hiện văn bản chưa có -> thêm vào `documents/LEGISLATION_TRACKING.md` với trạng thái "Chưa có"
  4. Phát hiện file trong `van-ban/` chưa hoàn thiện (metadata "Đang cập nhật", file <10k chars, lastedit cũ) -> đánh dấu trong tracking
- Giới hạn: 5 văn bản/lần
- Output: Báo cáo cho Bột, cập nhật `documents/LEGISLATION_TRACKING.md`
- Bột quyết định: tìm thêm văn bản mới hay dừng lại

**Đệ #2: Content Auditor**

- Mục đích: Duyệt các văn bản trong `documents/LEGISLATION_TRACKING.md` đã được đánh dấu là "Chưa hoàn thiện"
- Quy trình:
  1. Đọc `documents/LEGISLATION_TRACKING.md`
  2. Liệt kê các văn bản có trạng thái "Chưa có" hoặc "Chưa hoàn thiện"
  3. Báo cáo từng danh mục văn bản riêng biệt (theo từng nhóm chủ đề)
  4. Phân tích tình trạng: metadata thiếu, nội dung thiếu, OCR cần thiết
  5. Ưu tiên theo nhóm chủ đề và độ quan trọng
- Output: Báo cáo cho Bột các văn bản cần hoàn thiện, phân loại theo từng danh mục
- Bột quyết định: gọi Đệ #3 để hoàn thiện văn bản nào

**Đệ #3: Full Content Crawler**

- Mục đích: Kết hợp metadata + OCR để tạo file hoàn chỉnh
- Quy trình (cho mỗi văn bản được yêu cầu):
  1. Lấy metadata từ vanban.chinhphu.vn (số hiệu, ngày ban hành, người ký, ngày hiệu lực, trích yếu, căn cứ pháp luật)
  2. Nếu có PDF có chữ ký số -> áp dụng Signed PDF OCR Pipeline (mục 3)
  3. Merge metadata + nội dung OCR thành 1 file Markdown hoàn chỉnh
  4. Lưu file hoàn chỉnh vào `van-ban/` và tạo branch riêng để Bột review
- Output: 1 PR mới file, chờ Bột review và merge

**Đệ #4: Content Reviewer**

- Mục đích: Duyệt các văn bản đã có đầy đủ nội dung hoặc được đánh dấu "Hoàn thiện" trong tracking
- Quy trình:
  1. Quét `van-ban/` để tìm file có nội dung đầy đủ
  2. Đọc `documents/LEGISLATION_TRACKING.md` để lấy các văn bản "Hoàn thiện"
  3. Review liên tục 5 văn bản/lần, toàn bộ nội dung trong van-ban
  4. Phân tích chất lượng: metadata có chính xác không, nội dung có đầy đủ không, có cần cập nhật theo văn bản mới sửa đổi không, lỗi OCR cần chỉnh sửa
  5. Phát hiện file có metadata sai, nội dung lỗi, hoặc văn bản mới sửa đổi cần cập nhật
- Output: Báo cáo cho Bột các văn bản cần review
- Bột quyết định: File OK -> không cần xử lý; File cần bổ sung -> gọi Đệ #3; File cần cập nhật metadata -> sửa trực tiếp

### 2.3. Quy trình thực thi

```
Vòng lặp (Bột quyết định khi nào chạy):

1. Bột gọi Đệ #1 (Discovery) -> Nhận báo cáo (tối đa 5 văn bản/lần)
2. Bột quyết định:
   - Tìm thêm văn bản mới? -> Lặp lại từ 1
   - Dừng lại? -> Sang bước 3
3. Bột gọi Đệ #2 (Auditor) -> Nhận báo cáo các văn bản chưa hoàn thiện (phân loại theo danh mục)
4. Bột quyết định:
   - Văn bản nào cần hoàn thiện? -> Chọn và gọi Đệ #3
5. Bột gọi Đệ #3 (Full Crawler) -> Nhận 1 PR mới (file hoàn chỉnh)
6. Bột review nội dung và merge PR
7. Sau khi duyệt, Bột gọi Đệ #4 (Reviewer) -> Nhận báo cáo (5 văn bản/lần)
8. Bột quyết định:
   - File OK -> kết thúc
   - File cần sửa -> gọi Đệ #3 hoặc sửa trực tiếp
```

### 2.4. Tóm tắt các đệ

| Đệ | Chức năng | Giới hạn | Output |
|----|-----------|----------|--------|
| #1 | Discovery & Tracking | 5 văn bản/lần | Cập nhật tracking, báo cáo |
| #2 | Content Auditor | Báo cáo theo danh mục | Danh sách chưa hoàn thiện |
| #3 | Full Content Crawler | 1 văn bản / lần | 1 PR mới, chờ review |
| #4 | Content Reviewer | 5 văn bản/lần, toàn bộ van-ban | Danh sách cần review |

---

## 3. Signed PDF OCR Pipeline

### 3.1. Khi nào cần dùng

Khi crawl văn bản từ `vanban.chinhphu.vn` hoặc nguồn chính thức khác, mọi file PDF đính kèm đều phải được OCR để lấy nội dung, không được bỏ qua bước này.

Đặc biệt bắt buộc với PDF có chữ ký số CAdES-BES (`pdftotext` chỉ trích được metadata chữ ký, không lấy được nội dung văn bản).

### 3.2. Pipeline chuẩn

```bash
# Bước 1: Tải PDF từ datafiles.chinhphu.vn
curl -sL "https://datafiles.chinhphu.vn/.../<file>.pdf" -o /tmp/<file>.pdf

# Bước 2: Convert từng trang PDF thành ảnh PPM (200 DPI)
pdftoppm -r 200 /tmp/<file>.pdf /tmp/p

# Bước 3: OCR từng ảnh bằng tesseract với gói tiếng Việt
cd /tmp && for f in p-*.ppm; do tesseract "$f" "${f%.ppm}" -l vie; done

# Bước 4: Gộp kết quả thành một file toàn văn
cat /tmp/p-*.txt > /tmp/<file>-ocr.txt
```

### 3.3. Yêu cầu môi trường

- `pdftoppm` (gói `poppler-utils`)
- `tesseract-ocr` với gói ngôn ngữ `tesseract-ocr-vie`
- Đủ dung lượng `/tmp` (PDF trung bình 5-15MB, sau convert còn ~26MB/trang)

### 3.4. Lỗi OCR thường gặp và cách xử lý

| Lỗi | Ví dụ | Cách xử lý |
|------|-------|------------|
| Số bị đọc thành chữ | `Dieu 11` → `Dieu I1` | Đối chiếu lại bằng metadata gốc từ vanban.chinhphu.vn |
| Ký tự đặc biệt | `đ)` → `o`) | So sánh ngữ cảnh để sửa |
| Mất dấu ngoặc kép | `BM-09` → `BM-09` | Bổ sung thủ công khi viết nội dung |
| Ngắt dòng giữa từ | `khoa` newline `học` | Gộp lại khi viết lại nội dung |

### 3.5. Quy trình áp dụng trong các task

Khi thực hiện Đệ #3 (Full Content Crawler) hoặc các task khác có liên quan đến PDF:

1. Tải PDF về `/tmp/`
2. Chạy Signed PDF OCR Pipeline (mục 3.2)
3. Dùng output OCR làm nguồn nội dung chính để cập nhật file
4. Ghi chú phương pháp vào file Markdown

Không tạo task riêng cho OCR. OCR là công cụ bắt buộc của mọi task có liên quan đến PDF.

### 3.6. Lưu trữ output OCR

- Output OCR tạm thời lưu tại `/tmp/<file>-ocr.txt`
- Không commit file OCR output vào repo (file lớn, nhiễu, dễ lỗi chính tả)
- Nội dung đã sửa và bổ sung mới commit vào repo dưới dạng Markdown

---

## 4. Kích hoạt task

### 4.1. Cấu hình cron

Cron job gọi task `crawl-vanban` mỗi 30 phút:

```json
{
  "name": "crawl-vanban",
  "schedule": { "kind": "every", "everyMs": 1800000 },
  "sessionTarget": "current",
  "payload": {
    "kind": "agentTurn",
    "message": "HEARTBEAT: Đọc HEARTBEAT.md. Kiểm tra task 'crawl-vanban' (interval 30m). Nếu đến giờ chạy, thực hiện theo mô tả: đọc lại phương án ở mục 2, quyết định có gọi đệ nào hay không, báo cáo cho Sếp. Nếu không có gì cần làm, reply HEARTBEAT_OK."
  }
}
```

### 4.2. Hành vi khi task chạy

- Bột đọc HEARTBEAT.md, đặc biệt mục 2
- Bột kiểm tra PR đang mở
- Bột quyết định: gọi đệ nào (dựa trên tình trạng hiện tại)
- Bột báo cáo cho Sếp các hành động đã thực hiện
- Nếu không có gì cần làm: reply `HEARTBEAT_OK`

### 4.3. Nguyên tắc quan trọng

- Bột tự gọi đệ #1 và đệ #4 song song khi không còn task/ không biết làm gì
- Bột tự quyết định mọi hành động trong vòng lặp cron (không hỏi Sếp, không chờ phê duyệt giữa các bước)
- Báo cáo tổng hợp cho Sếp sau khi hoàn thành chuỗi công việc (hoặc khi có PR cần review)
- KHÔNG tự động tạo PR
- KHÔNG tự động merge
- Crawl liên tục, nếu có thắc mắc có nên crawl hay không thì gọi Đệ #4 review rồi Bột tự quyết định
- Gọi nhiều đệ thực hiện song song

### 4.4. Hành vi mặc định của Bột khi cron chạy (cập nhật 2026-06-07)

Khi cron `crawl-vanban` đánh thức Bột, Bột thực hiện tuần tự:

1. Đọc `HEARTBEAT.md` mục 2 và `documents/LEGISLATION_TRACKING.md`.
2. Kiểm tra PR đang mở.
3. **Tự quyết định** theo luật ưu tiên:
   - Có file chưa hoàn thiện + văn bản đó không có PR mở → gọi Đệ #3 để tạo PR mới (mỗi lần 1 văn bản). Văn bản đang có PR mở thì BỎ QUA, chuyển sang văn bản tiếp theo.
   - Không có file chưa hoàn thiện + tracking thiếu văn bản → gọi Đệ #1 (Discovery, 5 văn bản/lần) + Đệ #4 (Reviewer, 5 văn bản/lần) song song.
   - Có PR mở → vẫn tiếp tục vòng lặp với văn bản khác; PR đang mở chỉ loại trừ văn bản đó khỏi review/crawl tiếp theo. Trong báo cáo liệt kê danh sách PR đang chờ Sếp review.
   - Tracking đầy đủ + không có file cần refactor + không có PR → tự động gọi Đệ #1 (Discovery) để tìm văn bản mới.
4. Báo cáo 1 lần cuối cho Sếp trong main session (số PR tạo, số văn bản cập nhật, danh sách PR chờ review).
5. Nếu lỗi → ghi `memory/YYYY-MM-DD.md` rồi reply lỗi; nếu thành công → ghi log ngắn vào `memory/YYYY-MM-DD.md`.

**Không hỏi Sếp giữa chừng. Không dừng để chờ phản hồi.**

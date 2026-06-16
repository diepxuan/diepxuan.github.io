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
6. **Bắt buộc đọc và áp dụng OCR Quality Gate**: trước khi crawl/OCR/review/sửa văn bản pháp luật, Bột và mọi đệ phải đọc `documents/OCR_QUALITY_GATE.md` và chỉ commit file OCR khi đã chạy quality gate hoặc đánh dấu rõ là stub/chưa hoàn thiện.

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
  4. Đọc `documents/OCR_QUALITY_GATE.md`
  5. Chạy scan OCR + scan Điều/Chương trên file Markdown cuối cùng sẽ được commit
  6. Sửa lỗi OCR chắc chắn; lỗi không chắc phải đối chiếu nguồn hoặc đánh dấu stub/chưa hoàn thiện trong tracking
  7. Chạy lại quality gate sau khi sửa; chỉ lưu/commit khi artifact cuối đã pass hoặc đã được đánh dấu stub/chưa hoàn thiện
  8. Lưu file hoàn chỉnh vào `van-ban/` trên branch của PR heartbeat active
  9. Commit kết quả vào PR heartbeat active với message rõ văn bản/tác vụ
- Output: File hoàn chỉnh đã qua OCR quality gate + commit cập nhật vào PR heartbeat active, chờ Sếp review

**Đệ #4: Content Reviewer**

- Mục đích: Duyệt các văn bản đã có đầy đủ nội dung hoặc được đánh dấu "Hoàn thiện" trong tracking. **Đồng thời chịu trách nhiệm phát hiện file cần refactor trong `van-ban/`** (metadata "Đang cập nhật", file < 10KB, lastedit > 7 ngày).
- Quy trình:
  1. Quét `van-ban/` để tìm file có nội dung đầy đủ
  2. Quét `van-ban/` để phát hiện file cần refactor (metadata "Đang cập nhật", < 10KB, lastedit > 7 ngày) - đánh dấu trong `documents/LEGISLATION_TRACKING.md`
  3. Đọc `documents/LEGISLATION_TRACKING.md` để lấy các văn bản "Hoàn thiện"
  4. Review liên tục 5 văn bản/lần, toàn bộ nội dung trong van-ban
  5. Đọc `documents/OCR_QUALITY_GATE.md` và chạy lại OCR quality gate cho từng văn bản được review
  6. Phân tích chất lượng: metadata có chính xác không, nội dung có đầy đủ không, có cần cập nhật theo văn bản mới sửa đổi không, lỗi OCR cần chỉnh sửa
  7. Phát hiện file có metadata sai, nội dung lỗi, hoặc văn bản mới sửa đổi cần cập nhật
- Output: Báo cáo cho Bột các văn bản cần review + danh sách file cần refactor + kết quả OCR quality gate
- Bột quyết định: File OK -> không cần xử lý; File cần bổ sung/refactor -> gọi Đệ #3; File cần cập nhật metadata -> sửa trực tiếp
- Lưu ý: Đệ #4 KHÔNG cần kiểm tra PR đang mở. PR là output, không ảnh hưởng quyết định review.

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
5. Bột xác định/tạo PR heartbeat active, rồi gọi Đệ #3 (Full Crawler) -> Nhận file hoàn chỉnh + commit trong PR active
6. Bột push cập nhật vào cùng PR heartbeat active, cập nhật PR title/body/comment theo mục 2.6, rồi báo cáo Sếp chờ review
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
| #3 | Full Content Crawler | 1 văn bản / lần | Cập nhật PR heartbeat active, chờ review |
| #4 | Content Reviewer | 5 văn bản/lần, toàn bộ van-ban | Danh sách cần review |

### 2.5. Chính sách PR heartbeat active

Heartbeat `crawl-vanban` dùng mô hình **một PR làm việc active**, không tạo PR theo từng file/văn bản.

Quy tắc:

1. Nếu chưa có PR heartbeat active đang mở:
   - checkout từ `origin/main`;
   - tạo branch dạng `heartbeat/crawl-vanban-YYYYMMDD` (chưa mở PR);
   - đợi Đệ #3 tạo file và commit lên branch đó;
   - push branch lên origin;
   - mở 1 PR làm việc từ branch đã có commit để Sếp review.
2. Nếu đã có PR heartbeat active đang mở:
   - checkout branch của PR đó;
   - tiếp tục commit các văn bản/tác vụ mới vào cùng PR;
   - push thường, không force-push.
3. Mỗi văn bản/tác vụ phải là commit riêng hoặc nhóm commit nhỏ, message rõ scope.
4. Không tự merge/close PR heartbeat active khi chưa có lệnh rõ từ Sếp.
5. Nếu PR active gặp sự cố không thể tiếp tục an toàn, ví dụ branch hỏng, conflict nặng, PR bị đóng, mất trạng thái, không xác định được PR active, push thất bại hoặc worktree không an toàn:
   - không force-push để cứu PR cũ;
   - tạo PR heartbeat mới từ `origin/main`;
   - ghi rõ trong PR body/comment: `Tiếp tục heartbeat sau sự cố`, kèm PR cũ nếu xác định được;
   - từ đó tiếp tục làm việc trên PR mới.
6. Nếu có nhiều PR heartbeat đang mở, chọn PR mới nhất còn an toàn để tiếp tục; nếu không xác định chắc chắn, tạo PR mới từ `origin/main` và báo cáo Sếp.

PR heartbeat active là ngoại lệ được Sếp cho phép so với luật `mỗi file/mỗi task = 1 PR`. Ngoại lệ này chỉ áp dụng cho cron `crawl-vanban`.

### 2.6. Bắt buộc cập nhật nội dung PR sau mỗi lần push

Khi heartbeat có commit mới và push vào PR heartbeat active, Bột không được chỉ cập nhật branch. Bột phải cập nhật đồng thời nội dung PR để Sếp review được trạng thái mới nhất.

Quy trình bắt buộc sau mỗi lần push:

1. Re-query PR active bằng `gh pr view` để lấy:
   - số PR;
   - title hiện tại;
   - head/base branch;
   - changed files;
   - additions/deletions;
   - `mergeable` và `mergeStateStatus`.
2. Cập nhật PR body bằng trạng thái tổng hợp mới nhất:
   - mục tiêu PR;
   - phạm vi hiện tại;
   - danh sách văn bản/file đã thêm hoặc sửa;
   - commit mới nhất;
   - nguồn dữ liệu/PDF đã dùng;
   - kết quả OCR Quality Gate, scan Điều/Chương, placeholder/source check;
   - rủi ro còn lại và phần cần Sếp review.
3. Post thêm một PR comment cho lần heartbeat vừa chạy:
   - thời gian chạy theo Asia/Saigon;
   - commit vừa push;
   - file thay đổi;
   - validation đã chạy;
   - ghi chú review.
4. Nếu scope thực tế của PR đã thay đổi lớn so với title/body cũ, cập nhật title/body cho khớp diff hiện tại trước khi báo cáo Sếp.
5. Re-query PR lần cuối sau khi cập nhật body/comment và báo cáo Sếp kèm link PR/comment.

Nếu cập nhật PR body hoặc PR comment thất bại, Bột phải báo lỗi rõ trong báo cáo cuối. Không được báo `xong` khi branch đã push nhưng nội dung PR chưa được cập nhật.

Template PR body heartbeat:

```md
## Tổng quan

PR heartbeat active cho task `crawl-vanban`.

## Phạm vi hiện tại

- Branch: `<branch>`
- Base: `<base>`
- Số file thay đổi: `<n>`
- Additions/deletions: `+x / -y`

## Cập nhật mới nhất

- Thời gian: `<YYYY-MM-DD HH:mm Asia/Saigon>`
- Commit mới: `<sha>`
- Văn bản/tác vụ:
  - `<file/path.md>` — `<mô tả>`

## Validation

- `git diff --check`: pass/fail
- OCR Quality Gate: pass/fail/not applicable
- Scan Điều/Chương: pass/fail/not applicable
- Placeholder/source check: pass/fail/not applicable

## Cần Sếp review

- `<file>` — `<điểm cần chú ý>`

## Lịch sử heartbeat

- `<time>` — `<commit>` — `<summary>`
```

Template PR comment heartbeat:

```md
Heartbeat update `<YYYY-MM-DD HH:mm Asia/Saigon>`

Đã push commit `<sha>` vào PR active.

Thay đổi:
- `<file>`: `<mô tả>`

Validation:
- `git diff --check`: pass
- OCR Quality Gate: pass/not applicable
- Điều/Chương: pass/not applicable
- Placeholder/source check: pass

Ghi chú review:
- `<điểm cần Sếp xem>`
```

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
pdftoppm -r 150 /tmp/<file>.pdf /tmp/p

# Bước 3: OCR từng ảnh bằng tesseract với gói tiếng Việt
cd /tmp && for f in p-*.ppm; do tesseract "$f" "${f%.ppm}" -l vie; done

# Bước 4: Gộp kết quả thành một file toàn văn
cat /tmp/p-*.txt > /tmp/<file>-ocr.txt
```

### 3.3. Yêu cầu môi trường

- `pdftoppm` (gói `poppler-utils`)
- `tesseract-ocr` với gói ngôn ngữ `tesseract-ocr-vie`
- `scripts/ocr_pdf.py` - script tự động hóa pipeline (ưu tiên dùng)
- Dung lượng `/tmp`: PDF trung bình 5-15MB, sau convert còn ~15MB/trang (150 DPI)

### 3.4. Kiểm tra chất lượng PDF trước OCR

| Kiểm tra | Ngưỡng | Hành động |
|----------|--------|-----------|
| Kích thước file PDF | < 0.1 MB | Dừng, tìm nguồn PDF khác hoặc đánh dấu stub |
| Số trang | < 1 trang với văn bản dài | Cảnh báo, kiểm tra nguồn khác |
| Kích thước trang sau convert | < 5 KB | Skip trang (blank/missing), ghi log |

**Nếu PDF không đạt ngưỡng:**
- Không commit nội dung OCR từ PDF đó
- Tìm docid khác trên vanban.chinhphu.vn, hoặc nguồn khác (luatvietnam.vn, giaoduc.net.vn)
- Nếu không tìm được nguồn đáng tin cậy, đánh dấu file là "Chưa hoàn thiện" trong tracking

### 3.5. Lỗi OCR thường gặp và cách xử lý

| Lỗi | Ví dụ | Cách xử lý |
|------|-------|------------|
| Số bị đọc thành chữ | `Dieu 11` → `Dieu I1` | Đối chiếu lại bằng metadata gốc từ vanban.chinhphu.vn |
| Ký tự đặc biệt | `đ)` → `o`) | So sánh ngữ cảnh để sửa |
| Mất dấu ngoặc kép | `BM-09` → `BM-09` | Bổ sung thủ công khi viết nội dung |
| Ngắt dòng giữa từ | `khoa` newline `học` | Gộp lại khi viết lại nội dung |
| Trang blank/missing | PDF < 0.1 MB | Tìm nguồn khác, đánh dấu stub |

### 3.6. Quy trình áp dụng trong các task

Khi thực hiện Đệ #3 (Full Content Crawler) hoặc các task khác có liên quan đến PDF:

1. **Tải PDF về `/tmp/`**
2. **Kiểm tra chất lượng PDF trước OCR (mục 3.4)**
   - Nếu kích thước < 0.1 MB → dừng, tìm nguồn khác
3. Ưu tiên: `scripts/ocr_pdf.py` trước; nếu lỗi → fallback sang pipeline thủ công (mục 3.2)
4. Kiểm tra kích thước từng trang sau convert, skip trang < 5KB
5. Dùng output OCR làm nguồn nội dung chính để cập nhật file
6. Đọc `documents/OCR_QUALITY_GATE.md`
7. Chạy scan OCR, scan Điều, scan Chương/Mục
8. Sửa lỗi OCR chắc chắn; lỗi không chắc phải đối chiếu nguồn
9. **Chỉ commit Markdown khi:**
   - OCR issues nghiêm trọng = 0
   - Hoặc đánh dấu file là stub/chưa hoàn thiện trong tracking

Không tạo task riêng cho OCR. OCR và OCR Quality Gate là công cụ bắt buộc của mọi task có liên quan đến PDF.

Không ghi chú phương pháp, log OCR, timeout hoặc debug note vào file Markdown public. Các ghi chú kỹ thuật chỉ ghi trong báo cáo heartbeat/PR/memory.

### 3.7. Lưu trữ output OCR

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
- KHÔNG tự động tạo PR rời theo từng file/văn bản. Chỉ tạo PR heartbeat mới khi chưa có PR active hoặc khi PR active gặp sự cố theo mục 2.5
- KHÔNG tự động merge
- Crawl liên tục, nếu có thắc mắc có nên crawl hay không thì gọi Đệ #4 review rồi Bột tự quyết định
- Gọi nhiều đệ thực hiện song song

### 4.4. Hành vi mặc định của Bột khi cron chạy (cập nhật 2026-06-07)

Khi cron `crawl-vanban` đánh thức Bột, Bột thực hiện tuần tự:

1. Đọc `HEARTBEAT.md` mục 2 và `documents/LEGISLATION_TRACKING.md`.
2. Kiểm tra PR heartbeat active đang mở theo mục 2.5.
3. **Tự quyết định** theo luật ưu tiên:
   - Có file chưa hoàn thiện trong tracking → xác định/tạo PR heartbeat active theo mục 2.5, rồi gọi Đệ #3 xử lý 1 văn bản và commit/push vào PR active. Văn bản đã nằm trong PR active/open thì BỎ QUA, chuyển sang văn bản tiếp theo.
   - Không có file chưa hoàn thiện + tracking thiếu văn bản → gọi Đệ #1 (Discovery, 5 văn bản/lần) + Đệ #4 (Reviewer, 5 văn bản/lần) song song.
   - Tracking đầy đủ + không có file cần refactor → tự động gọi Đệ #1 (Discovery) để tìm văn bản mới.
4. **Quản lý vòng đời đệ theo mục 4.5** (chạy trước bước 5 để ghi kết quả kill/spawn vào báo cáo cuối).
5. Nếu có commit/push vào PR active, bắt buộc cập nhật PR title/body/comment theo mục 2.6 trước khi báo cáo Sếp.
6. Báo cáo 1 lần cuối cho Sếp trong main session (số PR tạo, số văn bản cập nhật, danh sách PR đang chờ review, link comment PR mới nhất nếu có, kết quả kill/spawn đệ stale).
7. Nếu lỗi → ghi `memory/YYYY-MM-DD.md` rồi reply lỗi; nếu thành công → ghi log ngắn vào `memory/YYYY-MM-DD.md`.

**Không hỏi Sếp giữa chừng. Không dừng để chờ phản hồi.**

### 4.5. Đánh giá tình trạng sub-agent khi task bắt đầu (cập nhật 2026-06-16)

Khi cron `crawl-vanban` đánh thức Bột ở đầu mỗi poll, **trước khi quyết định hành động tiếp theo**, Bột phải đánh giá tình trạng các đệ (sub-agent) đang hoạt động để quyết định kill hay giữ lại.

**Quy trình bắt buộc:**

1. Chạy `subagents` (không truyền tham số, hoặc `subagents action=list recentMinutes=30`) để liệt kê:
   - Sub-agent `active` (đang chạy)
   - Sub-agent `recent` trong 30 phút gần nhất

2. Với **mỗi** sub-agent đang active, đánh giá theo tiêu chí:

| Tiêu chí | Cách kiểm tra | Ngưỡng stale |
|----------|---------------|--------------|
| Thời gian chạy | `startedAt` → hiện tại | > 50% timeout đã set mà không có output mới |
| Có output mới trong 10 phút gần nhất | `endedAt` hoặc `lastMessage` | Không có output > 10 phút |
| Vượt quá timeout đã set | `runtimeMs` > `timeoutSeconds * 1000` | > 100% timeout |
| Sub-agent cũ từ poll trước | `startedAt` < `(poll_hiện_tại - 30 phút)` | Tồn tại > 1 chu kỳ poll |
| Sub-agent quá cũ từ poll cách đây > 2 | `startedAt` < `(poll_hiện_tại - 60 phút)` | Stale nghiêm trọng |

3. **Quyết định:**

| Tình trạng | Hành động |
|------------|-----------|
| Sub-agent active, < 50% timeout, có output mới < 10 phút | **GIỮ LẠI**, đợi completion. Báo cáo Sếp "đang chờ đệ X (đã chạy Y phút/Z timeout)". KHÔNG spawn thêm đệ mới cùng chức năng. |
| Sub-agent active, > 50% timeout hoặc không có output mới > 10 phút | **CÂN NHẮC KILL**: đánh giá xem work còn lại có thể hoàn thành trong thời gian còn lại không. Nếu nghi ngờ → KILL, báo cáo Sếp lý do. |
| Sub-agent active, > 100% timeout | **BẮT BUỘC KILL**. Sub-agent đã quá hạn. |
| Sub-agent recent (< 30 phút) đã completed | BỎ QUA (đã xử lý ở poll trước). |
| Sub-agent recent (< 30 phút) failed/cancelled | **GIỮ LẠI THÔNG TIN TRONG MEMORY** (không retry ngay). Báo cáo Sếp "đệ X fail, không retry". |
| Sub-agent cũ > 2 polls (> 60 phút), không nằm trong recent 30 phút | **STALE NGHIÊM TRỌNG**: Kill nếu vẫn còn active, ghi log memory. |

4. **Báo cáo cho Sếp** khi poll kết thúc phải liệt kê rõ:

```
- Sub-agent đang active: <id> <taskName> <runtime>/<timeout> <trạng thái: healthy/stale>
- Hành động: giữ/kill/lý do
- Sub-agent mới spawn: <id> <taskName> <runtime> <scope>
```

5. **Nguyên tắc:**

- Bột tự quyết định kill hay giữ dựa trên tiêu chí trên. KHÔNG cần hỏi Sếp giữa chừng.
- Kill sub-agent qua `sessions_send` với message yêu cầu dừng, hoặc dùng `process kill` nếu biết sessionId.
- Khi kill vì stale, BẮT BUỘC ghi log `memory/YYYY-MM-DD.md` kèm: sessionKey, taskName, runtime, lý do kill, work đã làm (nếu có), work còn lại cần làm lại.
- Khi kill, nếu work còn dang dổ → đánh dấu trong `documents/LEGISLATION_TRACKING.md` (ví dụ: "Stub - đệ crawl X timeout tại poll Y, cần retry") rồi mới xử lý văn bản khác ở poll kế tiếp.
- Ưu tiên GIỮ LẠI sub-agent nếu work gần xong (> 80% output, chỉ còn verify + commit). Ví dụ: sub-agent crawl 9m30s/10m timeout, đã có file output → giữ thêm 1-2 phút, kill nếu quá timeout.
- Nếu không xác định được tình trạng sub-agent (API lỗi, list rỗng), coi như sub-agent KHÔNG tồn tại và tiếp tục workflow bình thường. Ghi log warning trong memory.

**Ví dụ áp dụng:**

- Poll 09:26: Sub-agent `crawler-94-nd-cp` chạy 12 phút / 15 phút timeout, đã có file 76KB untracked → GIỮ LẠI, đợi commit + push.
- Poll 09:56: Sub-agent `crawler-94-nd-cp` vẫn chạy 17 phút / 15 phút timeout, không có output mới 7 phút → KILL, đánh dấu stub.
- Poll 10:26: Sub-agent `reviewer-20260616-0856` đã completed 30 phút trước → BỎ QUA (đã xử lý ở poll 09:05).

**Bắt buộc đọc mục 4.5 trước khi xử lý bất kỳ poll nào.**

---

## 5. Lịch sử cập nhật HEARTBEAT.md

| Ngày | Thay đổi |
|------|----------|
| 2026-06-07 | Thêm mục 4.4 - hành vi mặc định của Bột khi cron chạy |
| 2026-06-16 | Thêm mục 4.5 - đánh giá stale sub-agent + quyết định kill/giữ |

---

## 6. Quản lý vòng đời đệ (legacy - tích hợp vào 4.5)

> Phần này được tích hợp đầy đủ vào mục 4.5. Giữ lại ở đây chỉ để tham chiếu nhanh.

Khi cron `crawl-vanban` chạy, Bột kiểm tra trạng thái đệ đang chạy:

- Đệ đang chạy > 1 tiếng mà chưa có completion event → coi là stale.
- Hành động:
  1. Ghi `memory/YYYY-MM-DD.md` (stale: <taskName> at <time>).
  2. Kill session qua `sessions_send` với message `"STOP"` hoặc tool `subagents` kill.
  3. Spawn lại đệ mới.
- Mỗi cron chỉ kill/spawn tối đa 1 đệ stale (tránh thrash).
- Ghi log kết quả vào báo cáo cuối.

**Tracking trạng thái đệ trong `memory/YYYY-MM-DD.md`:**

- Trước khi spawn: ghi `running: <taskName> at <time>`.
- Khi có completion event: ghi `done: <taskName> at <time>`.
- Cron sau: nếu có `running` > 1 tiếng mà không có `done` tương ứng → stale.

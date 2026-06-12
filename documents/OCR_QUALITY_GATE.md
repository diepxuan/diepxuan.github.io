# OCR_QUALITY_GATE.md - Quy tắc kiểm soát chất lượng OCR văn bản pháp luật

Tài liệu này là quy tắc bắt buộc cho mọi agent/session khi crawl, OCR, review hoặc sửa văn bản pháp luật trong `van-ban/`.

Mục tiêu: lỗi OCR phải được phát hiện và sửa ngay trong lúc xử lý tài liệu, không chờ tới review PR cuối.

---

## 1. Nguyên tắc bắt buộc

1. OCR raw luôn là dữ liệu chưa sạch.
2. Không commit file OCR nếu chưa chạy quality gate.
3. Không đưa ghi chú nội bộ crawler vào nội dung public.
4. Không tự bịa nội dung pháp lý khi OCR thiếu hoặc lỗi.
5. Nếu OCR không đủ chất lượng thì phải re-OCR, lấy nguồn text khác, hoặc tạo stub metadata sạch và đánh dấu cần bổ sung trong tracking.
6. Văn bản pháp luật có lỗi OCR được coi là lỗi nghiêm trọng vì có thể làm sai nghĩa pháp lý.

---

## 2. Những nội dung cấm xuất hiện trong file public

Không được để các chuỗi sau trong file `van-ban/...`:

- `OCR không thực hiện được`
- `timeout`
- `LLM idle timeout`
- `NoSuchKey`
- `pipelineSigned`
- `above`
- `crawl failed`
- `nội dung lấy tạm`
- `cần bổ sung khi có PDF`
- `file này được lưu ở`
- ghi chú debug, ghi chú agent, log pipeline

Nếu cần ghi chú kỹ thuật thì ghi trong báo cáo heartbeat, memory log hoặc PR body, không ghi vào văn bản pháp luật public.

---

## 3. Checklist metadata

Front matter tối thiểu:

```yaml
---
layout: vanban
title: "..."
date: YYYY-MM-DD
modified: YYYY-MM-DD
group: ...
tags:
  - ...
docid: ...
source: vanban.chinhphu.vn; datafiles.chinhphu.vn
---
```

Bắt buộc kiểm tra:

- `title` có dấu tiếng Việt đầy đủ.
- `date` đúng ngày ban hành.
- `modified` là ngày cập nhật hiện tại.
- `group` đúng lĩnh vực.
- `tags` không lẫn tag sai lĩnh vực.
- `docid` đúng nếu có.
- `source` rõ ràng.
- Không có metadata không dấu kiểu `Thong tu`, `Quy dinh`, `Nghi dinh`.

---

## 4. Checklist cấu trúc văn bản

Heading khuyến nghị:

```md
# Tên văn bản

## THÔNG TIN VĂN BẢN

## VĂN BẢN

## Chương I

### Điều 1. ...
```

Không chấp nhận heading lỗi:

```md
- ## Chương III -
„ ## Chương VI
Chương VỊ
Chương VIH
Điều:72
Điền 80
„ Điều 86
```

Phải sửa thành:

```md
## Chương III
## Chương VI
## Chương VIII
### Điều 72.
### Điều 80.
### Điều 86.
```

---

## 5. Kiểm tra số Điều

Agent phải scan heading `### Điều X.`.

Bắt buộc báo cáo:

- Tổng số Điều.
- Range Điều đầu/cuối.
- Thiếu Điều nào.
- Trùng Điều nào.
- Heading Điều có bị OCR sai không.

Nếu văn bản có Điều nhưng script không detect được, phải kiểm tra format khác như:

```md
**Điều 1.**
Điều 1.
```

Sau đó chuẩn hóa về:

```md
### Điều 1.
```

File chỉ được đánh giá OK khi:

```text
Missing: []
Duplicate: []
```

---

## 6. Kiểm tra Chương/Mục

Agent phải scan:

```regex
^## Chương ([IVXLCDM]+)
^## Mục \d+
```

Bắt buộc kiểm tra:

- Số La Mã có hợp lý không.
- Có nhầm `VIH`, `VỊ`, `1H`, `IH`, `IIl` không.
- Thứ tự Chương có bị sai kiểu `I, II, II, V, IV` không.
- Heading có mất `##` không.

Lỗi thường gặp:

| OCR lỗi | Sửa |
|---|---|
| `Chương VỊ` | `Chương VI` |
| `Chương VIH` | `Chương VIII` |
| `Chương 1H` | `Chương III` |
| `Chương IIl` | `Chương III` |

---

## 7. Bảng lỗi OCR phổ biến

### 7.1. Lỗi ký tự điểm/bullet

| OCR lỗi | Thường là | Ghi chú |
|---|---|---|
| `©)` | `c)` | So chuỗi a), b), c), d) |
| `.©)` | `c)` | Dấu chấm thừa |
| `c©)` | `c)` | OCR lặp ký tự |
| `ø)` | `g)` | So chuỗi e), g), h) |
| `gø)` | `g)` | OCR lặp ký tự |
| `®)` | `d)` hoặc bỏ | Phải xem ngữ cảnh |
| `€©)` | `c)` | OCR lẫn ký hiệu euro |
| `__©` | `c)` | Lỗi Markdown/OCR |

Không sửa mù nếu không có ngữ cảnh. Phải xem điểm trước/sau.

### 7.2. Lỗi số

| OCR lỗi | Sửa |
|---|---|
| `ngày l7` | `ngày 17` |
| `ngày L5` | `ngày 15` |
| `khoản I` | `khoản 1` |
| `Điều 2§` | `Điều 25` |
| `Điều §` | thường là `Điều 5`, phải xem ngữ cảnh |
| `§.` | thường là `5.` |
| `§0` | `50` |
| `§2` | `52` |
| `§5` | `55` |
| `§9` | `59` |
| `®Z` | `2` |

Nguyên tắc: sửa số phải dựa vào ngữ cảnh hoặc nguồn gốc. Không đoán điều khoản pháp lý.

### 7.3. Lỗi từ tiếng Việt phổ biến

| OCR lỗi | Sửa |
|---|---|
| `tthủ tục` | `thủ tục` |
| `thâm quyền` | `thẩm quyền` |
| `thấm quyền` | `thẩm quyền` |
| `hỗ sơ` | `hồ sơ` |
| `Hồ SƠ` | `hồ sơ` |
| `giây tờ` | `giấy tờ` |
| `pháp ly` | `pháp lý` |
| `vến đầu tư` | `vốn đầu tư` |
| `tiễn độ` | `tiến độ` |
| `bạ tầng` | `hạ tầng` |
| `khủ công nghệ` | `khu công nghệ` |
| `công bế` | `công bố` |
| `kế từ ngày` | `kể từ ngày` |
| `kê từ ngày` | `kể từ ngày` |
| `bao gôm` | `bao gồm` |
| `xúc tiễn` | `xúc tiến` |
| `xúc tiên` | `xúc tiến` |
| `quôc gia` | `quốc gia` |
| `hăng năm` | `hằng năm` |
| `SỬA ĐỎI` | `SỬA ĐỔI` |
| `BỎ SUNG` | `BỔ SUNG` |
| `Một SÓ` | `Một SỐ` |
| `MỘT SÓ` | `MỘT SỐ` |
| `ĐIÊU KHOÁN` | `ĐIỀU KHOẢN` |
| `THỊ HÀNH` | `THI HÀNH` |

### 7.4. Ký tự rác bắt buộc scan

```text
ø © § † ® µ ¬ ¶ �
```

Nếu xuất hiện trong văn bản pháp luật thì gần như chắc chắn là lỗi OCR, trừ trường hợp đặc biệt có căn cứ rõ.

---

## 8. Script scan OCR bắt buộc

```python
from pathlib import Path
import re

path = Path("duong-dan-file.md")
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

patterns = [
    "ø", "©", "§", "†", "®", "µ", "�",
    "Điền", "Điều:", "„ Điều",
    "Chương VỊ", "Chương VIH", "Chương 1H",
    "ngày l", "ngày L",
    "tthủ tục",
    "thâm quyền", "thấm quyền",
    "giây tờ", "pháp ly",
    "vến đầu tư", "tiễn độ",
    "hỗ sơ", "Hồ SƠ",
    "hợp, lệ", "hợp. lệ",
    "bạ tầng", "ph��p",
    "khủ công nghệ", "công bế",
    "kế từ ngày", "kê từ ngày",
    "bao gôm", "xúc tiễn", "xúc tiên",
    "quôc gia", "hăng năm",
    "SỬA ĐỎI", "BỎ SUNG",
    "Một SÓ", "MỘT SÓ",
    "ĐIÊU KHOÁN", "THỊ HÀNH",
    "NoSuchKey", "timeout", "pipelineSigned", "above",
]

issues = []
for i, line in enumerate(lines, 1):
    for pattern in patterns:
        if pattern in line:
            issues.append((i, pattern, line[:160]))

print(f"File: {path}")
print(f"Lines: {len(lines)}")
print(f"OCR issues: {len(issues)}")
for line_no, pattern, context in issues[:100]:
    print(f"L{line_no}: {pattern} -> {context}")
```

Yêu cầu pass:

```text
OCR issues: 0
```

Nếu `OCR issues > 0`, không được báo file OK.

---

## 9. Script kiểm tra Điều

```python
from pathlib import Path
import re

path = Path("duong-dan-file.md")
lines = path.read_text(encoding="utf-8").splitlines()

articles = []
for i, line in enumerate(lines, 1):
    m = re.match(r"^### Điều\s+(\d+)\.", line)
    if m:
        articles.append((int(m.group(1)), i, line))

nums = [x[0] for x in articles]

if nums:
    missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    duplicate = sorted({n for n in nums if nums.count(n) > 1})
    print(f"Articles: {len(nums)}")
    print(f"Range: {min(nums)}-{max(nums)}")
    print(f"Missing: {missing}")
    print(f"Duplicate: {duplicate}")
else:
    print("No article heading found")
```

---

## 10. Script kiểm tra Chương

```python
from pathlib import Path
import re

path = Path("duong-dan-file.md")
lines = path.read_text(encoding="utf-8").splitlines()

chapters = []
for i, line in enumerate(lines, 1):
    m = re.match(r"^## Chương\s+([IVXLCDM]+)", line)
    if m:
        chapters.append((m.group(1), i, line))

print(f"Chapters: {len(chapters)}")
for roman, line_no, title in chapters:
    print(f"L{line_no}: {roman} - {title}")

bad_patterns = [
    "Chương VỊ",
    "Chương VIH",
    "Chương 1H",
    "Chương IH",
    "Chương IIl",
    "- ## Chương",
    "„ ## Chương",
]

for i, line in enumerate(lines, 1):
    for pattern in bad_patterns:
        if pattern in line:
            print(f"BAD L{i}: {pattern} -> {line}")
```

---

## 11. Quy trình bắt buộc cho crawler

Mỗi agent crawl văn bản phải làm theo thứ tự:

1. Xác minh nguồn: docid, trang vanban.chinhphu.vn, link PDF/datafiles nếu có.
2. Tải nguồn: ưu tiên text chính thức nếu có; nếu chỉ có PDF thì OCR.
3. Convert sang Markdown: front matter, thông tin văn bản, nội dung văn bản, heading chuẩn.
4. Chạy scan OCR.
5. Chạy scan cấu trúc Điều/Chương/Mục.
6. Sửa lỗi chắc chắn; lỗi không chắc thì kiểm tra nguồn.
7. Chạy scan lại.
8. Chỉ commit khi lỗi nghiêm trọng = 0, hoặc báo rõ file là stub/chưa hoàn thiện.
9. Báo cáo số dòng, số Điều, lỗi đã sửa, lỗi còn lại, đánh giá OK/Cần sửa/Không merge.

---

## 12. Tiêu chuẩn đánh giá

### OK để merge

- Metadata sạch.
- OCR issues = 0.
- Missing Điều = [].
- Duplicate Điều = [].
- Heading Chương không sai số La Mã.
- Không có ghi chú crawler/debug trong file public.
- Không có đoạn không dấu bất thường hoặc câu vô nghĩa.
- `git diff --check` pass.

### Cần sửa trước merge

- Còn ký tự OCR rác.
- Có `Điều:`, `Điền`, `„ Điều`.
- Có `Chương VỊ`, `Chương VIH`, sai số La Mã.
- Có lỗi phổ biến như `thâm quyền`, `hỗ sơ`, `tthủ tục`.
- Có ghi chú crawler/debug.
- Có đoạn mất dấu một phần.

### Không nên merge

- OCR rác nhiều.
- Nội dung không dấu toàn bộ.
- Câu vô nghĩa, sai ngữ cảnh pháp lý.
- Không xác định được số Điều.
- Văn bản chỉ là summary nhưng lại ghi như toàn văn.
- Agent tự viết nội dung thay vì lấy từ nguồn.
- Có khả năng sai số văn bản, sai ngày, sai cơ quan ban hành.

---

## 13. Mẫu báo cáo review

```text
Review PR #...

Tổng quan:
- Số file:
- Add/delete:
- File văn bản:
- File tracking:

Kết quả từng file:

1. path/to/file.md
- Loại: Nghị định/Thông tư/Nghị quyết
- Dòng:
- Điều: x, range y-z
- Chương:
- OCR issues trước sửa:
- OCR issues sau sửa:
- Lỗi đã sửa:
  - ...
- Đánh giá: OK / Cần sửa / Không merge

Kết luận:
- Có thể merge: Có/Không
- Điều kiện còn lại:
- Commit fix:
```

---

## 14. Bài học từ PR #202 và PR #204

Các lỗi thực tế đã gặp:

- `ngày l7` -> `ngày 17`
- `ø)` -> `g)`
- `©)` -> `c)`
- `§.` -> `5.`
- `Điều:72` -> `### Điều 72`
- `Điền 80` -> `### Điều 80`
- `„ Điều 86` -> `### Điều 86`
- `thâm quyền` -> `thẩm quyền`
- `hỗ sơ` -> `hồ sơ`
- `tthủ tục` -> `thủ tục`
- `Chương VỊ` -> `Chương VI`
- `Chương VIH` -> `Chương VIII`

Kết luận vận hành:

- OCR quality gate phải chạy ngay trong crawler session.
- Reviewer cuối PR chỉ là lớp phòng thủ thứ hai.
- Nếu để lỗi OCR tới PR review mới sửa thì tốn thời gian và dễ merge nhầm văn bản sai nghĩa pháp lý.

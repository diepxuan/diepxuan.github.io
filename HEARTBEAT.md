# HEARTBEAT.md - Quy trình heartbeat hiệu quả

HEARTBEAT.md định nghĩa cách agent tự động rà soát, chọn việc, tạo thay đổi sạch và chuẩn bị PR cho Sếp review.

Mục tiêu chính:

- Mỗi lần heartbeat phải tạo giá trị kiểm chứng được.
- Không chạy vòng lặp chỉ đọc memory rồi báo OK.
- Không gom nhiều việc không liên quan vào một PR.
- Không làm lại việc đã có PR, đã merge hoặc đã bị thay thế.
- Không push, tạo PR, merge hoặc đóng PR nếu chưa được Sếp cho phép rõ.

---

## 1. State Management

Heartbeat sử dụng 3 nguồn state để xác định phần nào đã làm, phần nào chưa làm.

### 1.1. PR đang mở (Primary Source of Truth)

PR đang mở là source of truth chính cho work in progress:

```bash
gh pr list --state open --limit 100 --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,url
```

- PR đang mở = item đang xử lý → không tạo PR trùng trên file đó.
- PR đã merge → item hoàn tất → cập nhật tracking.
- PR bị đóng/thay thế → item chưa hoàn tất hoặc có lỗi → xử lý lại.

### 1.2. Session State (OpenClaw Internal)

OpenClaw tự động track:

- `heartbeatTaskState`: last-run timestamp cho mỗi `tasks:` block.
- Session freshness, idle expiry.
- Không cần em quản lý thủ công.

### 1.3. Local State: .heartbeat-state.json

File local để track thông tin bổ sung không có trong PR hoặc session:

```json
{
  "last_runs": {
    "pr-hygiene": "2026-06-05T12:00:00+07:00",
    "legislation-crawl": "2026-06-05T08:00:00+07:00",
    "metadata-repair": "2026-06-04T20:00:00+07:00",
    "content-completion": "2026-06-01T10:00:00+07:00"
  },
  "next_runs": {
    "pr-hygiene": "2026-06-06T00:00:00+07:00",
    "legislation-crawl": "2026-06-06T08:00:00+07:00"
  },
  "last_result": {
    "pr-hygiene": "NO_ACTION",
    "legislation-crawl": "PR_CREATED"
  },
  "no_action_streak": {
    "metadata-repair": 2
  },
  "notes": {
    "legislation-crawl": "Nhóm Thuế/Thương mại: 2 item còn lại, cần retry khi có nguồn mới"
  }
}
```

**Quy tắc:**

- Không commit `.heartbeat-state.json`.
- Không dùng state để thay thế việc kiểm tra thực tế.
- State chỉ là cache để tránh quét lại toàn bộ.
- Luôn verify với PR đang mở và git diff trước khi hành động.

### 1.4. Luồng xác định state

```
1. Kiểm tra PR đang mở (gh pr list)
   ├── Có PR → Item đang xử lý, bỏ qua trùng
   └── Không có PR → Tiếp tục

2. Kiểm tra documents/LEGISLATION_TRACKING.md
   ├── Item có file → Đã có
   ├── Item có PR đang mở → Đang xử lý
   └── Item chưa xử lý → Chọn nhóm đầu tiên còn việc

3. Kiểm tra .heartbeat-state.json (optional)
   └── Track notes, no_action_streak, last run

4. Kiểm tra session state (OpenClaw auto)
   └── heartbeatTaskState cho tasks: blocks
```

---

## 2. Nguyên tắc vận hành

### 2.1. Heartbeat phải có đầu ra rõ ràng

Mỗi lượt chạy chỉ được kết thúc bằng một trong bốn kết quả:

1. **PR_CREATED**
   - Có branch sạch.
   - Có commit.
   - Diff đã kiểm tra.
   - Đã push branch và mở PR để Sếp review.
   - Đây là kết quả bắt buộc khi heartbeat đã tạo/cập nhật nội dung hoặc tài liệu.

2. **NEEDS_REVIEW**
   - Có phát hiện đáng chú ý nhưng chưa đủ chắc để sửa.
   - Cần Sếp quyết định phạm vi, nguồn dữ liệu hoặc hướng xử lý.

3. **BLOCKED**
   - Không thể tiếp tục vì lỗi công cụ, thiếu nguồn chính thức, conflict hoặc dữ liệu không đáng tin.
   - Phải ghi rõ blocker và bước xử lý đề xuất.

4. **NO_ACTION**
   - Không có việc đủ điều kiện xử lý.
   - Phải ghi rõ đã kiểm tra gì và vì sao không làm.

### 2.2. Không dùng memory làm task queue chính

- `memory/YYYY-MM-DD.md` chỉ dùng làm nhật ký local hoặc context phụ.
- Không quét memory mỗi 2 giờ để tìm việc mơ hồ.
- Task queue chính là:
  1. PR đang mở trên GitHub.
  2. `documents/LEGISLATION_TRACKING.md`.
  3. Các file `van-ban/` có metadata thiếu hoặc nguồn lỗi.

### 2.3. Task quá hạn phải tự nâng cấp mức xử lý

Nếu `Task B: Legislation Backlog Group Crawl` hoặc task backlog pháp luật quá hạn:

- Quá hạn dưới 24 giờ: chạy ngay trong lượt heartbeat kế tiếp.
- Quá hạn từ 24 giờ đến dưới 7 ngày: bỏ qua cooldown, ưu tiên trước task refactor thông thường.
- Quá hạn từ 7 ngày trở lên: coi là **OVERDUE_CRITICAL**.

Với `OVERDUE_CRITICAL`, heartbeat không được kết thúc `NO_ACTION` nếu backlog còn nhóm có item xử lý được. Phải tạo một trong hai đầu ra:

1. `PR_CREATED`: đã crawl nhóm backlog đầu tiên còn việc, tạo/cập nhật file, commit, push branch và mở PR cho Sếp review.
2. `BLOCKED`: nêu rõ nhóm, item, lỗi nguồn/công cụ và điều kiện retry.

---

## 3. Chu kỳ heartbeat chuẩn

Mỗi lượt heartbeat chạy theo đúng thứ tự dưới đây.

### Bước 1: Sync và kiểm tra môi trường

```bash
git checkout main
git fetch origin --prune
git pull --ff-only origin main
git status --short --branch
```

### Bước 2: Kiểm tra PR đang mở (Primary Source of Truth)

```bash
gh pr list --state open --limit 100 --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,changedFiles,updatedAt,url
```

Mục tiêu: tránh tạo thêm PR trùng, conflict hoặc lỗi thời.

Phân loại PR:
- **mergeable + đúng nội dung**: báo `NEEDS_REVIEW` để Sếp quyết merge.
- **conflict nhưng còn giá trị**: tạo branch thay thế từ `main`, cherry-pick/copy đúng phần cần giữ, push và mở PR thay thế.
- **trùng PR đã merge**: báo đề xuất đóng, không tự đóng nếu chưa được giao rõ.
- **sai metadata hoặc nguồn không đáng tin**: không merge; báo lỗi cụ thể.

### Bước 3: Chọn đúng một đơn vị công việc

Thứ tự ưu tiên:

1. Nếu có task backlog quá hạn `OVERDUE_CRITICAL`: xử lý ngay nhóm backlog đầu tiên còn việc.
2. Sửa hoặc thay thế PR đang mở bị conflict nhưng còn giá trị.
3. Hoàn tất nhóm backlog đầu tiên còn item `Chưa có`, `Cần cập nhật` hoặc `Blocked` có thể retry.
4. Sửa metadata sai rõ ràng trong một file `van-ban/`.
5. Bổ sung nội dung thiếu cho một file `van-ban/` có nguồn chính thức.
6. Nếu không có việc đủ dữ kiện: `NO_ACTION`.

Luật chọn nhóm backlog:

1. Đọc `documents/LEGISLATION_TRACKING.md` và lấy thứ tự nhóm theo thứ tự xuất hiện từ trên xuống dưới.
2. Chọn nhóm đầu tiên còn item chưa hoàn tất. Không nhảy sang nhóm dưới nếu nhóm trên còn item xử lý được.
3. Trong nhóm đã chọn, ưu tiên item theo thứ tự: `Chưa có` → `Cần cập nhật` → `Blocked` có thể retry.
4. Chỉ chuyển sang nhóm kế tiếp khi toàn bộ item trong nhóm hiện tại đã `Đã có`, `Bỏ qua` hoặc `Blocked` không thể retry.
5. Không được trả `NO_ACTION` nếu còn bất kỳ nhóm nào có item xử lý được.

Giới hạn phạm vi:

- Mỗi heartbeat xử lý tối đa **một nhóm backlog**.
- Trong nhóm đó, có thể xử lý nhiều item nếu cùng chủ đề, cùng nguồn/cơ quan hoặc diff vẫn nhỏ, dễ review.
- Mặc định không quá 3 file nội dung trong một heartbeat.
- Nếu nhóm có nhiều hơn 3 item hợp lệ, chia thành nhiều heartbeat/PR.

### Bước 4: Xác minh nguồn trước khi sửa

Nguồn ưu tiên:
1. `vanban.chinhphu.vn`
2. PDF/tệp đính kèm từ `datafiles.chinhphu.vn`
3. Nguồn cơ quan nhà nước chuyên ngành

### Bước 5: Tạo branch sạch và commit

```bash
git checkout main
git pull --ff-only origin main
git checkout -b <type>/<scope>-<yyyymmdd>
```

Sau khi sửa:
```bash
git diff --check
git add <files-trong-scope>
git commit -m "<type>: <mo-ta-ngan>"
```

### Bước 6: Báo cáo kết quả

Báo cáo phải gồm:
- Kết quả: `PR_CREATED`, `NEEDS_REVIEW`, `BLOCKED` hoặc `NO_ACTION`.
- File đã kiểm tra/sửa.
- Nguồn đã dùng.
- Branch, commit và PR URL nếu có.

---

## 4. Các task heartbeat

### Task A: PR Hygiene (12h)

Kiểm tra PR mở, phát hiện conflict/trùng/sai metadata.

### Task B: Legislation Backlog Group Crawl (24h)

Xử lý nhóm backlog đầu tiên còn item trong `documents/LEGISLATION_TRACKING.md`.

### Task C: Metadata Repair (24h)

Sửa metadata sai trong file `van-ban/`.

### Task D: Content Completion (168h)

Bổ sung nội dung thiếu cho văn bản quan trọng.

---

## 5. Quy tắc tạo PR

Heartbeat được phép push branch và mở PR khi:
- Task thuộc phạm vi đã được định nghĩa.
- Branch tạo mới từ `origin/main`.
- Có commit thực chất.
- `git diff --check` pass.
- Không có PR mở khác cùng phạm vi/file.

---

## 6. Nguồn dữ liệu

| Nguồn | Trạng thái | Cách dùng |
|-|-|-|
| `vanban.chinhphu.vn` | Ưu tiên | Metadata, trang chi tiết |
| `datafiles.chinhphu.vn` | Ưu tiên | PDF/tệp đính kèm |
| Website cơ quan nhà nước | Dự phòng | Đối chiếu |
| `luatvietnam.vn` | Không ổn định | Không làm nguồn chính |

---

## 7. Mẫu báo cáo

```
Kết quả: PR_CREATED
Task: Legislation Backlog Group Crawl
Nhóm backlog: Thuế / thương mại

Đã làm:
- Kiểm tra PR mở: <kết quả>
- Xác minh nguồn: <nguồn đã dùng>
- Xử lý item: <danh sách item>

Kiểm tra:
- git diff --check: pass
- git diff --stat: <summary>

Branch: <branch>
Commit: <sha> <message>
PR: <url>

Cần Sếp quyết:
- Review PR.
```

---

HEARTBEAT.md phải giữ vai trò là quy trình tạo giá trị, không phải nhật ký chạy cron.
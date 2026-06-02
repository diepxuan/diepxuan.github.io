# HEARTBEAT.md - Quy trình heartbeat hiệu quả

HEARTBEAT.md định nghĩa cách agent tự động rà soát, chọn việc, tạo thay đổi sạch và chuẩn bị PR cho Sếp review.

Mục tiêu chính:

- Mỗi lần heartbeat phải tạo giá trị kiểm chứng được.
- Không chạy vòng lặp chỉ đọc memory rồi báo OK.
- Không gom nhiều việc không liên quan vào một PR.
- Không làm lại việc đã có PR, đã merge hoặc đã bị thay thế.
- Không push, tạo PR, merge hoặc đóng PR nếu chưa được Sếp cho phép rõ.

---

## 1. Nguyên tắc vận hành

### 1.1. Heartbeat phải có đầu ra rõ ràng

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

Không dùng `HEARTBEAT_OK` chung chung nếu không có thông tin kiểm chứng.

### 1.2. Không dùng memory làm task queue chính

- `memory/YYYY-MM-DD.md` chỉ dùng làm nhật ký local hoặc context phụ.
- Không quét memory mỗi 2 giờ để tìm việc mơ hồ.
- Task queue chính là:
  1. PR đang mở trên GitHub.
  2. `documents/LEGISLATION_TRACKING.md`.
  3. Các file `van-ban/` có metadata thiếu hoặc nguồn lỗi.

### 1.3. Không cập nhật state vào HEARTBEAT.md

- `HEARTBEAT.md` là quy trình, không phải state runtime.
- State runtime lưu local-only trong `.heartbeat-state.json`.
- `.heartbeat-state.json` không commit.

### 1.4. Task quá hạn phải tự nâng cấp mức xử lý

Nếu `track-legislation`, `check-new-laws` hoặc task backlog pháp luật quá hạn:

- Quá hạn dưới 24 giờ: chạy ngay trong lượt heartbeat kế tiếp.
- Quá hạn từ 24 giờ đến dưới 7 ngày: bỏ qua cooldown, ưu tiên trước task refactor thông thường.
- Quá hạn từ 7 ngày trở lên: coi là **OVERDUE_CRITICAL**.

Với `OVERDUE_CRITICAL`, heartbeat không được kết thúc `NO_ACTION` nếu backlog còn nhóm có item xử lý được. Phải tạo một trong hai đầu ra:

1. `PR_CREATED`: đã crawl nhóm backlog đầu tiên còn việc, tạo/cập nhật file, commit, push branch và mở PR cho Sếp review.
2. `BLOCKED`: nêu rõ nhóm, item, lỗi nguồn/công cụ và điều kiện retry.

Trường hợp backlog pháp luật quá hạn từ 7 ngày trở lên, heartbeat phải xử lý nhóm backlog đầu tiên còn việc trong `documents/LEGISLATION_TRACKING.md` trước mọi refactor khác.

---

## 2. Chu kỳ heartbeat chuẩn

Mỗi lượt heartbeat chạy theo đúng thứ tự dưới đây.

### Bước 1: Sync và kiểm tra môi trường

```bash
git checkout main
git fetch origin --prune
git pull --ff-only origin main
git status --short --branch
gh pr list --state open --limit 100 --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,changedFiles,updatedAt,url
```

Điều kiện dừng:

- Working tree không sạch.
- Đang không ở `main` mà chưa có lý do rõ.
- `origin/main` không pull fast-forward được.

Kết quả: `BLOCKED`.

### Bước 2: Xử lý PR đang mở trước khi tạo việc mới

Mục tiêu: tránh tạo thêm PR trùng, conflict hoặc lỗi thời.

Với từng PR đang mở:

1. Đọc metadata và diff:

```bash
gh pr view <PR> --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,changedFiles,additions,deletions,url
gh pr diff <PR> --name-only
gh pr diff <PR> --patch --color=never
```

2. Phân loại:
   - **mergeable + đúng nội dung**: báo `NEEDS_REVIEW` để Sếp quyết merge, hoặc merge nếu Sếp đã giao rõ trong phiên hiện tại.
   - **conflict nhưng còn giá trị**: tạo branch thay thế từ `main`, cherry-pick/copy đúng phần cần giữ, push và mở PR thay thế để Sếp review.
   - **trùng PR đã merge**: báo đề xuất đóng, không tự đóng nếu chưa được giao rõ.
   - **sai metadata hoặc nguồn không đáng tin**: không merge; báo lỗi cụ thể.

3. Nếu còn PR mở có cùng file với task định làm, không tạo task mới trên file đó.

### Bước 3: Chọn đúng một đơn vị công việc

Mỗi heartbeat chỉ xử lý **một đơn vị công việc**.

Thứ tự ưu tiên:

1. Nếu có task backlog quá hạn `OVERDUE_CRITICAL`: xử lý ngay nhóm backlog đầu tiên còn việc trong `documents/LEGISLATION_TRACKING.md`.
2. Sửa hoặc thay thế PR đang mở bị conflict nhưng còn giá trị.
3. Hoàn tất nhóm backlog đầu tiên còn item `Chưa có`, `Cần cập nhật` hoặc `Blocked` có thể retry trong `documents/LEGISLATION_TRACKING.md`.
4. Sửa metadata sai rõ ràng trong một file `van-ban/`.
5. Bổ sung nội dung thiếu cho một file `van-ban/` có nguồn chính thức.
6. Nếu không có việc đủ dữ kiện: `NO_ACTION`.

Luật chọn nhóm backlog:

1. Đọc `documents/LEGISLATION_TRACKING.md` và lấy thứ tự nhóm theo thứ tự xuất hiện từ trên xuống dưới.
2. Chọn nhóm đầu tiên còn item chưa hoàn tất. Không nhảy sang nhóm dưới nếu nhóm trên còn item xử lý được.
3. Trong nhóm đã chọn, ưu tiên item theo thứ tự: `Chưa có` → `Cần cập nhật` → `Blocked` có thể retry.
4. Nếu một item bị `Blocked` không thể retry trong lượt hiện tại, ghi rõ URL đã thử, blocker và điều kiện retry; sau đó tiếp tục item kế tiếp trong cùng nhóm nếu còn.
5. Chỉ chuyển sang nhóm kế tiếp khi toàn bộ item trong nhóm hiện tại đã `Đã có`, `Bỏ qua` hoặc `Blocked` không thể retry.
6. Không được trả `NO_ACTION` nếu còn bất kỳ nhóm nào có item xử lý được.

Giới hạn phạm vi:

- Mỗi heartbeat xử lý tối đa **một nhóm backlog**.
- Trong nhóm đó, có thể xử lý nhiều item nếu cùng chủ đề, cùng nguồn/cơ quan hoặc diff vẫn nhỏ, dễ review.
- Mặc định không quá 3 file nội dung trong một heartbeat, chưa tính `documents/LEGISLATION_TRACKING.md`.
- Nếu nhóm có nhiều hơn 3 item hợp lệ, chia thành nhiều heartbeat/PR theo thứ tự từ trên xuống dưới.
- Không gom nhiều nhóm backlog vào một PR.
- Không refactor hàng loạt chỉ vì `lastedit` cũ.

### Bước 4: Xác minh nguồn trước khi sửa

Với văn bản pháp luật, trước khi sửa metadata hoặc nội dung phải xác minh tối thiểu:

- Số hiệu văn bản.
- Loại văn bản.
- Cơ quan ban hành.
- Ngày ban hành.
- Ngày hiệu lực nếu có.
- Nguồn chính thức.

Nguồn ưu tiên:

1. `vanban.chinhphu.vn`
2. PDF/tệp đính kèm từ `datafiles.chinhphu.vn`
3. Nguồn cơ quan nhà nước chuyên ngành
4. Nguồn phụ chỉ dùng để đối chiếu, không làm nguồn chính nếu có nguồn chính thức

Nếu không xác minh được số hiệu hoặc ngày hiệu lực: không sửa nội dung, báo `NEEDS_REVIEW` hoặc `BLOCKED`.

### Bước 5: Tạo branch sạch và commit

Chỉ sau khi chọn được một đơn vị công việc:

```bash
git checkout main
git pull --ff-only origin main
git checkout -b <type>/<scope>-<yyyymmdd>
```

Quy tắc branch:

- Tạo từ `main` mới nhất.
- Không dùng lại branch heartbeat cũ.
- Với heartbeat, sau khi commit hợp lệ phải push branch và mở PR để Sếp review.

Sau khi sửa:

```bash
git diff --check
git diff --stat
git diff --name-only
git status --short --branch
git add <files-trong-scope>
git commit -m "<type>: <mo-ta-ngan>"
```

Nếu không có thay đổi thực chất: không commit.

### Bước 6: Báo cáo kết quả

Báo cáo phải gồm:

- Kết quả: `PR_CREATED`, `NEEDS_REVIEW`, `BLOCKED` hoặc `NO_ACTION`.
- File đã kiểm tra/sửa.
- Nguồn đã dùng.
- Diff summary.
- Branch, commit và PR URL nếu có.
- Việc cần Sếp quyết định.

---

## 3. Quy tắc tạo PR

Heartbeat không được dừng ở branch local nếu đã tạo/cập nhật nội dung hoặc tài liệu. Kết quả hoàn tất phải là PR để Sếp review.

Heartbeat được phép push branch và mở PR khi tất cả điều kiện sau đúng:

- Task thuộc phạm vi đã được định nghĩa trong `HEARTBEAT.md` hoặc được Sếp giao rõ.
- Branch tạo mới từ `origin/main`.
- Có commit thực chất.
- `git diff --check` pass.
- Không có PR mở khác cùng phạm vi/file, trừ PR thay thế đã nêu rõ.
- PR chỉ để review, không merge/close tự động.

Trước khi tạo PR phải kiểm tra:

```bash
git log --oneline origin/main..HEAD
git diff --name-only origin/main...HEAD
git diff --check
gh pr list --state open --json number,title,headRefName,url
```

Checklist:

- [ ] Branch tạo từ `origin/main` mới nhất.
- [ ] Chỉ có commit của task hiện tại.
- [ ] Chỉ sửa file trong phạm vi.
- [ ] Không có file state local, memory local, credential.
- [ ] PR title mô tả đúng nội dung.
- [ ] PR body nêu nguồn, thay đổi, kiểm tra đã chạy.

---

## 4. Quy tắc chống hoạt động không hiệu quả

Cấm các hành vi sau trong heartbeat:

- Chạy định kỳ chỉ để đọc memory rồi báo OK.
- Tạo branch nhưng không commit thay đổi thực chất.
- Tạo nhiều PR cùng sửa một file mà không kiểm tra PR mở.
- Cập nhật `lastedit` nếu không có thay đổi nội dung/metadata thực chất.
- Dùng nguồn bị WAF/login-wall làm căn cứ chính.
- Tạo PR từ branch không đồng bộ `main`.
- Push thêm commit vào PR cũ nếu Sếp chưa yêu cầu.
- Tự đóng/merge PR nếu Sếp chưa giao rõ trong phiên hiện tại.

Nếu heartbeat chạy liên tiếp 2 lần `NO_ACTION` cho cùng nhóm việc, phải giảm tần suất hoặc tạm dừng nhóm đó thay vì tiếp tục chạy dày.

---

## 5. Các task heartbeat còn hiệu lực

### Task A: PR Hygiene

**Tần suất đề xuất:** mỗi 12 giờ hoặc trước khi tạo việc mới.

Mục tiêu:

- Kiểm tra PR mở.
- Phát hiện conflict, PR trùng, PR sai metadata.
- Không để backlog PR làm nhiễu heartbeat.

Đầu ra hợp lệ:

- `NEEDS_REVIEW`: danh sách PR nên merge/đóng/thay thế.
- `PR_CREATED`: PR thay thế đã được mở để Sếp review.
- `NO_ACTION`: không có PR mở.

### Task B: Legislation Backlog Group Crawl

**Tần suất bắt buộc:** mỗi ngày 1 lần.

Task này thay thế cách vận hành cũ của `track-legislation`, `check-new-laws` và `update-vbpl`.

Mục tiêu:

- Đọc `documents/LEGISLATION_TRACKING.md`.
- Xác định nhóm backlog đầu tiên còn item chưa hoàn tất theo thứ tự từ trên xuống dưới.
- Crawl trang chi tiết và PDF/tệp đính kèm cho item hợp lệ trong nhóm đó.
- Tạo hoặc cập nhật đúng file nội dung.
- Cập nhật trạng thái backlog và đường dẫn file tương ứng.
- Commit, push branch và mở PR để Sếp review khi có thay đổi thực chất.

Luật chọn nhóm và item:

1. Thứ tự nhóm là thứ tự xuất hiện trong bảng backlog, từ trên xuống dưới.
2. Chọn nhóm đầu tiên còn ít nhất một item `Chưa có`, `Cần cập nhật` hoặc `Blocked` có thể retry.
3. Trong nhóm được chọn, xử lý item theo thứ tự xuất hiện trong backlog.
4. Ưu tiên trạng thái theo thứ tự: `Chưa có` → `Cần cập nhật` → `Blocked` có thể retry.
5. Không nhảy sang nhóm dưới nếu nhóm trên còn item xử lý được.
6. Nếu một item bị `Blocked`, phải ghi rõ URL đã thử, nguyên nhân, điều kiện retry và tiếp tục item kế tiếp trong cùng nhóm nếu có.
7. Chỉ chuyển sang nhóm kế tiếp khi nhóm hiện tại đã hoàn tất theo quy tắc ở mục 6.
8. Có thể xử lý nhiều item cùng nhóm trong một PR nếu cùng chủ đề, cùng nguồn/cơ quan, tổng diff nhỏ và không vượt giới hạn phạm vi.

Quy trình bắt buộc:

```bash
# 1. Kiểm tra backlog và xác định nhóm đầu tiên còn việc
rg "\|.*\|.*\|.*\|.*(Chưa có|Cần cập nhật|Blocked)" documents/LEGISLATION_TRACKING.md

# 2. Crawl nguồn chính thức cho item trong nhóm đã chọn
# Ưu tiên trang chi tiết từ vanban.chinhphu.vn và PDF/tệp đính kèm datafiles.chinhphu.vn.

# 3. Tạo branch sạch theo nhóm backlog
git checkout main
git pull --ff-only origin main
git checkout -b refactor/<nhom-backlog>-<yyyymmdd>

# 4. Tạo/cập nhật nội dung trong đúng thư mục van-ban/<nhom-phu-hop>/

# 5. Cập nhật backlog, kiểm tra và commit
git diff --check
git add van-ban/<nhom-phu-hop>/*.md documents/LEGISLATION_TRACKING.md
git commit -m "refactor: cập nhật nhóm <nhom-backlog>"
git push -u origin refactor/<nhom-backlog>-<yyyymmdd>
gh pr create --base main --head refactor/<nhom-backlog>-<yyyymmdd> --title "refactor: cập nhật nhóm <nhom-backlog>" --body-file /tmp/pr-body.md
```

Đầu ra hợp lệ:

- `PR_CREATED`: đã mở PR xử lý nhóm backlog đầu tiên còn việc.
- `BLOCKED`: không crawl được nguồn chính thức hoặc không tìm được PDF/tệp đính kèm; phải nêu rõ nhóm, item, URL đã thử và điều kiện retry.
- `NEEDS_REVIEW`: nguồn có mâu thuẫn hoặc cần Sếp quyết định tách/gộp PR.
- `NO_ACTION`: chỉ được dùng khi toàn bộ backlog không còn nhóm nào có item xử lý được.

Không được trả `NO_ACTION` nếu còn bất kỳ item `Chưa có`, `Cần cập nhật` hoặc `Blocked` có thể retry trong `documents/LEGISLATION_TRACKING.md`.

### Task C: Metadata Repair

**Tần suất đề xuất:** mỗi ngày 1 lần hoặc chạy theo yêu cầu.

Mục tiêu:

- Tìm một file `van-ban/` có metadata sai hoặc `Đang cập nhật`.
- Xác minh với nguồn chính thức.
- Sửa metadata tối thiểu, không viết lại toàn bộ file nếu không cần.

Đầu ra hợp lệ:

- `PR_CREATED`: đã mở PR cho một metadata fix.
- `BLOCKED`: nguồn chính thức không xác minh được.

### Task D: Content Completion

**Tần suất đề xuất:** theo yêu cầu hoặc tối đa vài lần/tuần.

Mục tiêu:

- Bổ sung nội dung thiếu cho một văn bản quan trọng.
- Ưu tiên văn bản có backlog hoặc Sếp chỉ định.

Điều kiện chạy:

- Có nguồn chính thức đủ tin cậy.
- Có phạm vi rõ: full text, cấu trúc chương/điều, hoặc tóm tắt metadata.

Không chạy nếu chỉ dựa trên tiêu chí `file < 10k chars` hoặc `lastedit cũ`.

---

## 6. Shared backlog: documents/LEGISLATION_TRACKING.md

`documents/LEGISLATION_TRACKING.md` là backlog pháp luật mới dùng chung cho heartbeat. Đây là source of truth cho task `Legislation Backlog Group Crawl`.

Quy tắc:

- Không xóa lịch sử đã ghi nhận; chỉ chỉnh nếu sai rõ ràng.
- Khi thêm văn bản mới, ghi đủ: số hiệu, ngày ban hành, trích yếu, nhóm, trạng thái, nguồn URL và đường dẫn file dự kiến nếu biết.
- Mỗi item backlog phải có trạng thái rõ: `Chưa có`, `Đang xử lý`, `Đã có`, `Cần cập nhật`, `Bỏ qua`, hoặc `Blocked`.
- Không dùng `Có liên quan` như trạng thái kết thúc; phải đối chiếu và chuyển thành `Đã có`, `Cần cập nhật` hoặc `Chưa có`.
- Nếu văn bản đã tạo thành file riêng trong `van-ban/`, cập nhật trạng thái là `Đã có` và ghi đường dẫn file.
- Nếu văn bản không phù hợp website, ghi `Bỏ qua` và nêu lý do.
- Nếu văn bản chưa xử lý được, ghi `Blocked` kèm URL đã thử, blocker và điều kiện retry.
- Mỗi lần cập nhật backlog phải đi qua branch riêng và PR riêng, trừ khi cập nhật backlog đi kèm chính PR tạo nội dung cho item đó.

### 6.1. Thứ tự crawl theo nhóm

Heartbeat phải crawl backlog theo nhóm, từ trên xuống dưới:

1. Parse bảng backlog và giữ nguyên thứ tự nhóm theo lần xuất hiện đầu tiên.
2. Chọn nhóm đầu tiên còn item chưa hoàn tất.
3. Xử lý item trong nhóm theo thứ tự xuất hiện trong bảng.
4. Không chuyển sang nhóm dưới nếu nhóm trên còn item `Chưa có`, `Cần cập nhật` hoặc `Blocked` có thể retry.
5. Khi nhóm hiện tại đã hoàn tất, heartbeat tự chuyển sang nhóm kế tiếp trong lượt chạy sau.

### 6.2. Trạng thái item backlog

| Trạng thái | Ý nghĩa | Hành động heartbeat |
|-|-|-|
| `Chưa có` | Chưa có file riêng hoặc nội dung đủ dùng trong `van-ban/` | Crawl nguồn chính thức, tạo/cập nhật file |
| `Đang xử lý` | Đã có branch/PR đang mở cho item này | Kiểm tra PR mở, không tạo PR trùng |
| `Đã có` | Đã có file nội dung và đường dẫn rõ | Bỏ qua, chỉ đối chiếu khi cần |
| `Cần cập nhật` | Đã có file nhưng metadata/nội dung thiếu hoặc lỗi | Crawl nguồn chính thức, sửa tối thiểu |
| `Bỏ qua` | Không phù hợp website hoặc không cần tạo file | Bỏ qua, giữ lý do |
| `Blocked` | Chưa xử lý được do nguồn/công cụ/conflict | Retry nếu có input mới hoặc blocker có thể kiểm tra lại |

### 6.3. Điều kiện hoàn tất nhóm

Một nhóm được coi là hoàn tất khi:

- Không còn item `Chưa có`.
- Không còn item `Cần cập nhật`.
- Không còn item `Đang xử lý` mà không có PR tương ứng.
- Mọi item `Đã có` đều có đường dẫn file trong `van-ban/`.
- Mọi item `Bỏ qua` đều có lý do rõ.
- Mọi item `Blocked` đều có URL đã thử, blocker và điều kiện retry; nếu blocker có thể retry thì nhóm chưa hoàn tất.

Một nhóm chưa hoàn tất nếu còn bất kỳ item nào có thể tạo/cập nhật nội dung hoặc metadata từ nguồn chính thức.

---

## 7. Nguồn dữ liệu

| Nguồn | Trạng thái | Cách dùng |
|-|-|-|
| `vanban.chinhphu.vn` | Ưu tiên | Metadata, trang chi tiết văn bản |
| `datafiles.chinhphu.vn` | Ưu tiên | PDF/tệp đính kèm, trích xuất nội dung |
| Website cơ quan nhà nước chuyên ngành | Dự phòng | Đối chiếu khi cổng Chính phủ thiếu dữ liệu |
| `vbpl.vn` | Không ổn định | Chỉ đối chiếu nếu truy cập được |
| `luatvietnam.vn` | Không ổn định/login-wall | Không làm nguồn chính |
| `thuvienphapluat.vn` | Không ổn định/login-wall | Không làm nguồn chính |

---

## 8. State local

`.heartbeat-state.json` chỉ lưu thông tin vận hành local, ví dụ:

```json
{
  "last_runs": {
    "pr-hygiene": "2026-06-01T08:00:00+07:00"
  },
  "next_runs": {
    "pr-hygiene": "2026-06-01T20:00:00+07:00"
  },
  "last_result": {
    "pr-hygiene": "NO_ACTION"
  },
  "no_action_streak": {
    "metadata-repair": 2
  }
}
```

Quy tắc:

- Không commit `.heartbeat-state.json`.
- Nếu `no_action_streak >= 2`, giảm tần suất task đó.
- Nếu có `BLOCKED`, không retry liên tục; cần thay đổi input hoặc báo Sếp.

---

## 9. Mẫu báo cáo heartbeat

```text
Kết quả: PR_CREATED
Task: Legislation Backlog Group Crawl
Nhóm backlog: Thuế / thương mại
Vị trí nhóm: nhóm chưa hoàn tất đầu tiên trong documents/LEGISLATION_TRACKING.md
Branch: refactor/thue-thuong-mai-20260601
Commit: abc1234 refactor: cập nhật nhóm thuế thương mại

Đã làm:
- Kiểm tra PR mở: không có PR trùng file.
- Xác minh nguồn: vanban.chinhphu.vn và datafiles.chinhphu.vn.
- Xử lý item: 144/2026/NĐ-CP, 141/2026/NĐ-CP.
- Cập nhật file nội dung trong van-ban/.
- Cập nhật trạng thái trong documents/LEGISLATION_TRACKING.md.

Còn lại trong nhóm:
- 143/2026/NĐ-CP: Cần đối chiếu file thuế nhập khẩu hiện có.
- 24/2026/TT-BCT: Chưa có.

Kiểm tra:
- git diff --check: pass
- git diff --stat: 1 file changed

PR:
- https://github.com/diepxuan/diepxuan.github.io/pull/<number>

Cần Sếp quyết:
- Review PR và quyết định merge/đóng/sửa thêm
```

---

HEARTBEAT.md phải giữ vai trò là quy trình tạo giá trị, không phải nhật ký chạy cron.

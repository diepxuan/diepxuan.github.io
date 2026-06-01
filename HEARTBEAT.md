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

Với `OVERDUE_CRITICAL`, heartbeat không được kết thúc `NO_ACTION` nếu backlog còn item chưa xử lý. Phải tạo một trong hai đầu ra:

1. `PR_CREATED`: đã crawl, tạo/cập nhật file, commit, push branch và mở PR cho Sếp review.
2. `BLOCKED`: nêu rõ lỗi nguồn/công cụ và item nào bị chặn.

Trường hợp đã quá hạn 18 ngày như `track-legislation` và `check-new-laws`, heartbeat phải xử lý backlog ưu tiên 1 trước mọi refactor khác.

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

1. Nếu có task backlog quá hạn `OVERDUE_CRITICAL`: xử lý ngay item ưu tiên cao nhất trong `documents/LEGISLATION_TRACKING.md`.
2. Với backlog hiện tại, ưu tiên 1 bắt buộc là nhóm **An ninh mạng** gồm `48/2026/TT-BCA` và `47/2026/TT-BCA` của Bộ Công an.
3. Sửa hoặc thay thế PR đang mở bị conflict nhưng còn giá trị.
4. Hoàn tất một item `Chưa có` hoặc `Cần cập nhật` trong `documents/LEGISLATION_TRACKING.md`.
5. Sửa metadata sai rõ ràng trong một file `van-ban/`.
6. Bổ sung nội dung thiếu cho một file `van-ban/` có nguồn chính thức.
7. Nếu không có việc đủ dữ kiện: `NO_ACTION`.

Giới hạn phạm vi:

- Một PR chỉ nên chạm **một file văn bản** hoặc **một nhóm rất nhỏ có cùng chủ đề**.
- Không quá 3 file nội dung trong một heartbeat.
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

### Task B: Legislation Backlog Ingestion

**Tần suất bắt buộc:** mỗi ngày 1 lần.

Task này thay thế cách vận hành cũ của `track-legislation`, `check-new-laws` và `update-vbpl`.

Mục tiêu:

- Đọc `documents/LEGISLATION_TRACKING.md`.
- Chọn item ưu tiên cao nhất có nguồn chính thức.
- Crawl trang chi tiết và PDF/tệp đính kèm.
- Tạo hoặc cập nhật đúng file nội dung.
- Commit local để sẵn sàng tạo PR.

Luật chọn item:

1. Nếu backlog có nhóm **An ninh mạng** chưa xử lý, chọn nhóm này trước.
2. Với backlog hiện tại, phải xử lý hai văn bản Bộ Công an:
   - `48/2026/TT-BCA`: quy chuẩn kỹ thuật quốc gia về thiết bị camera giám sát sử dụng giao thức Internet - yêu cầu an ninh mạng cơ bản.
   - `47/2026/TT-BCA`: quy chuẩn kỹ thuật quốc gia về an ninh mạng cho hệ thống thông tin lưu trữ tài liệu điện tử trong cơ quan Đảng, Nhà nước.
3. Hai thông tư cùng nhóm có thể đi chung một PR nếu cùng tạo/cập nhật nhóm `van-ban/an-ninh-quoc-gia/` và tổng diff vẫn nhỏ, dễ review.
4. Sau khi xử lý nội dung, cập nhật `documents/LEGISLATION_TRACKING.md` để đánh dấu trạng thái tương ứng.

Quy trình bắt buộc:

```bash
# 1. Kiểm tra backlog
rg "48/2026/TT-BCA|47/2026/TT-BCA|An ninh mạng" documents/LEGISLATION_TRACKING.md

# 2. Crawl nguồn chính thức
# Ưu tiên trang chi tiết từ vanban.chinhphu.vn và PDF/tệp đính kèm datafiles.chinhphu.vn.

# 3. Tạo branch sạch
git checkout main
git pull --ff-only origin main
git checkout -b refactor/an-ninh-mang-bca-<yyyymmdd>

# 4. Tạo/cập nhật nội dung
# Đường dẫn đề xuất:
# - van-ban/an-ninh-quoc-gia/quy-chuan-camera-giam-sat-ip-an-ninh-mang.md
# - van-ban/an-ninh-quoc-gia/quy-chuan-an-ninh-mang-he-thong-luu-tru-tai-lieu-dien-tu.md

# 5. Cập nhật backlog và commit
git diff --check
git add van-ban/an-ninh-quoc-gia/*.md documents/LEGISLATION_TRACKING.md
git commit -m "refactor: bổ sung quy chuẩn an ninh mạng của Bộ Công an"
git push -u origin refactor/an-ninh-mang-bca-<yyyymmdd>
gh pr create --base main --head refactor/an-ninh-mang-bca-<yyyymmdd> --title "refactor: bổ sung quy chuẩn an ninh mạng của Bộ Công an" --body-file /tmp/pr-body.md
```

Đầu ra hợp lệ:

- `PR_CREATED`: đã mở PR xử lý nhóm An ninh mạng hoặc item backlog ưu tiên cao nhất.
- `BLOCKED`: không crawl được nguồn chính thức hoặc không tìm được PDF/tệp đính kèm; phải nêu rõ URL đã thử.
- `NEEDS_REVIEW`: nguồn có mâu thuẫn hoặc cần Sếp quyết định tách/gộp PR.

Không được trả `NO_ACTION` nếu `48/2026/TT-BCA` hoặc `47/2026/TT-BCA` vẫn chưa có file nội dung và nguồn chính thức còn truy cập được.

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

`documents/LEGISLATION_TRACKING.md` là backlog pháp luật mới dùng chung cho heartbeat.

Quy tắc:

- Không xóa lịch sử đã ghi nhận; chỉ chỉnh nếu sai rõ ràng.
- Khi thêm văn bản mới, ghi đủ: số hiệu, ngày ban hành, trích yếu, nhóm, trạng thái đã có/chưa có trong `van-ban/`, nguồn URL.
- Mỗi item backlog phải có trạng thái rõ: `Chưa có`, `Đang xử lý`, `Đã có`, `Bỏ qua`, hoặc `Blocked`.
- Nếu văn bản đã tạo thành file riêng trong `van-ban/`, cập nhật trạng thái là `Đã có` và ghi đường dẫn file.
- Nếu văn bản không phù hợp website, ghi lý do bỏ qua.
- Mỗi lần cập nhật backlog phải đi qua branch riêng và PR riêng, trừ khi cập nhật backlog đi kèm chính PR tạo nội dung cho item đó.

Backlog hiện tại có nhóm ưu tiên 1 chưa được xử lý:

| Số hiệu | Nhóm | Yêu cầu heartbeat |
|-|-|-|
| `48/2026/TT-BCA` | An ninh mạng | Crawl nguồn chính thức, tạo/cập nhật file nội dung, cập nhật backlog |
| `47/2026/TT-BCA` | An ninh mạng | Crawl nguồn chính thức, tạo/cập nhật file nội dung, cập nhật backlog |

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
Task: Metadata Repair
Branch: fix/vanban-metadata-dau-tu-20260601
Commit: abc1234 fix: sửa metadata Luật Đầu tư

Đã làm:
- Kiểm tra PR mở: không có PR trùng file.
- Xác minh nguồn: vanban.chinhphu.vn docid=209472.
- Sửa metadata trong van-ban/thuong-mai-dau-tu-chung-khoan/dau-tu.md.

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

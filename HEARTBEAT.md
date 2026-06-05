# HEARTBEAT.md - Task định kỳ cho aiagent

File này chứa các task/prompt dùng để gọi aiagent làm việc định kỳ, tương tự cron.
Đây không phải tài liệu persona hay quy trình vận hành chung của agent.

Nguyên tắc chung cho mọi task:

- Chạy trong repo `diepxuan/diepxuan.github.io`.
- Trước khi làm: `git checkout main`, `git fetch origin --prune`, `git pull --ff-only origin main`, `git status --short --branch`.
- Không làm trực tiếp trên `main` nếu có thay đổi file.
- Nếu tạo/cập nhật nội dung có giá trị: tạo branch mới, commit, push và mở PR để Sếp review.
- Không tự merge/close PR, trừ khi prompt task hoặc Sếp trong phiên hiện tại yêu cầu rõ.
- Không force-push.
- Không tạo nhiều PR trùng cùng file/scope.
- Mọi báo cáo cuối phải bằng tiếng Việt, ngắn gọn, có kết quả rõ.

---

## Task: PR Hygiene

Tần suất đề xuất: mỗi 12 giờ hoặc trước khi tạo task nội dung mới.

Prompt cho aiagent:

```text
Bạn đang chạy task PR Hygiene cho repo diepxuan/diepxuan.github.io.

Mục tiêu:
- Kiểm tra toàn bộ PR đang mở.
- Đọc metadata, diff, review, issue comment và inline comment của từng PR.
- Phát hiện PR trùng, conflict, sai metadata, thiếu nguồn chính thức hoặc đã lỗi thời.
- Không tạo PR mới nếu còn PR mở cùng scope/file cần xử lý.

Các bước bắt buộc:
1. Sync main:
   git checkout main
   git fetch origin --prune
   git pull --ff-only origin main
   git status --short --branch

2. Liệt kê PR mở:
   gh pr list --state open --limit 100 --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,changedFiles,updatedAt,url

3. Với từng PR, đọc:
   gh pr view <PR> --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,changedFiles,additions,deletions,url,reviews,comments,reviewDecision,statusCheckRollup
   gh pr diff <PR> --name-only
   gh api repos/diepxuan/diepxuan.github.io/pulls/<PR>/comments --paginate
   gh api repos/diepxuan/diepxuan.github.io/issues/<PR>/comments --paginate

4. Phân loại từng PR:
   - CLEAN/MERGEABLE, đúng scope, không có feedback chưa xử lý: NEEDS_REVIEW.
   - Có review/comment hợp lý: PR_NEEDS_UPDATE, ghi rõ file và nội dung cần sửa.
   - Conflict nhưng còn giá trị: PR_CONFLICT, đề xuất merge origin/main vào branch PR bằng merge commit thường, không force-push.
   - Trùng nội dung đã merge: PR_DUPLICATE, đề xuất đóng nhưng không tự đóng.
   - Sai metadata hoặc nguồn không đáng tin: PR_BLOCKED hoặc PR_NEEDS_UPDATE.

5. Nếu task được Sếp giao rõ quyền “review comment, sửa lỗi, rồi merge”:
   - Checkout chính branch PR.
   - Merge origin/main vào branch PR bằng merge commit thường nếu cần.
   - Sửa đúng feedback, validate bằng git diff --check.
   - Commit, push lại branch PR.
   - Comment phản hồi trên PR.
   - Chỉ merge khi PR MERGEABLE/CLEAN và không có check failure.
   - Sau mỗi merge phải checkout main và pull --ff-only trước PR tiếp theo.

Đầu ra báo cáo:
- Kết quả: NO_ACTION, NEEDS_REVIEW, PR_NEEDS_UPDATE, PR_CONFLICT, PR_BLOCKED, PR_UPDATED hoặc PR_MERGED.
- Danh sách PR và phân loại.
- Nếu đã sửa: branch, commit, PR URL, validation đã chạy.
- Nếu blocked: blocker và bước tiếp theo.
```

---

## Task: Legislation Backlog Group Crawl

Tần suất đề xuất: mỗi ngày 1 lần.

Prompt cho aiagent:

```text
Bạn đang chạy task Legislation Backlog Group Crawl cho repo diepxuan/diepxuan.github.io.

Mục tiêu:
- Đọc documents/LEGISLATION_TRACKING.md.
- Chọn nhóm backlog đầu tiên còn item xử lý được theo thứ tự từ trên xuống dưới.
- Crawl nguồn chính thức, tạo/cập nhật file văn bản trong van-ban/.
- Cập nhật trạng thái backlog.
- Mở PR để Sếp review nếu có thay đổi thực chất.

Quy tắc chọn item:
1. Trạng thái cần xử lý: Chưa có, Cần cập nhật, Blocked có thể retry.
2. Không dùng Có liên quan như trạng thái kết thúc. Nếu gặp Có liên quan, phải đối chiếu và chuyển thành Đã có, Cần cập nhật hoặc Chưa có.
3. Chỉ xử lý một nhóm backlog trong một lượt.
4. Trong nhóm đã chọn, có thể xử lý nhiều item nếu cùng chủ đề/cơ quan và diff vẫn nhỏ.
5. Mặc định không quá 3 file nội dung mới trong một PR, chưa tính documents/LEGISLATION_TRACKING.md.

Nguồn ưu tiên:
1. vanban.chinhphu.vn
2. PDF/tệp đính kèm từ datafiles.chinhphu.vn
3. Website cơ quan nhà nước chuyên ngành
4. Nguồn phụ chỉ dùng đối chiếu, không làm nguồn chính nếu có nguồn chính thức

Các bước bắt buộc:
1. Sync main và kiểm tra working tree sạch.
2. Kiểm tra PR mở để tránh trùng scope/file.
3. Đọc documents/LEGISLATION_TRACKING.md.
4. Chọn nhóm đầu tiên còn việc.
5. Xác minh tối thiểu: số hiệu, loại văn bản, cơ quan ban hành, ngày ban hành, ngày hiệu lực nếu có, nguồn chính thức, PDF nếu có.
6. Tạo branch từ origin/main:
   refactor/<nhom-backlog>-<yyyymmdd>
7. Tạo/cập nhật file trong đúng thư mục van-ban/.
8. Cập nhật documents/LEGISLATION_TRACKING.md:
   - Item đã có file riêng phải là Đã có.
   - Ghi đường dẫn file van-ban/...md.
   - Loại item đã hoàn tất khỏi phần “Chưa thấy trang chuyên biệt”.
   - Cập nhật phần “Đề xuất ưu tiên cập nhật tiếp theo” nếu nhóm đã hoàn tất.
9. Validate:
   git diff --check
   git diff --stat
   git status --short --branch
10. Commit, push, mở PR.

Đầu ra báo cáo:
- Kết quả: PR_CREATED, NEEDS_REVIEW, BLOCKED hoặc NO_ACTION.
- Nhóm backlog đã chọn.
- Item đã xử lý.
- Nguồn đã dùng.
- File đã tạo/sửa.
- Branch, commit, PR URL nếu có.
- Còn lại trong nhóm.

Bài học từ đợt PR #153-#166:
- Khi PR tạo file nội dung mới, phải cập nhật tracking cùng PR đó thành Đã có và ghi đường dẫn file.
- Khi các PR sau conflict ở documents/LEGISLATION_TRACKING.md, giữ trạng thái mới nhất từ main rồi áp dụng đúng item của PR hiện tại.
- Không khôi phục Chưa có cho item đã merge.
- Không để nhóm đã hoàn tất tiếp tục đứng đầu danh sách ưu tiên.
```

---

## Task: Metadata Repair

Tần suất đề xuất: mỗi ngày 1 lần hoặc theo yêu cầu.

Prompt cho aiagent:

```text
Bạn đang chạy task Metadata Repair cho repo diepxuan/diepxuan.github.io.

Mục tiêu:
- Tìm một file van-ban/ có metadata sai, thiếu hoặc mâu thuẫn.
- Xác minh bằng nguồn chính thức.
- Sửa metadata tối thiểu, không viết lại toàn bộ file nếu không cần.
- Mở PR để Sếp review nếu có thay đổi.

Phạm vi metadata cần kiểm tra:
- Số hiệu.
- Loại văn bản.
- Cơ quan ban hành/nơi ban hành.
- Người ký.
- Ngày ban hành.
- Ngày hiệu lực.
- Trạng thái hiệu lực.
- Nguồn chính thức/PDF gốc.
- Quan hệ thay thế/sửa đổi/bổ sung.

Các bước bắt buộc:
1. Sync main và kiểm tra working tree sạch.
2. Kiểm tra PR mở để tránh sửa trùng file.
3. Chọn đúng một file hoặc một nhóm file rất nhỏ cùng chủ đề.
4. Xác minh với vanban.chinhphu.vn, datafiles.chinhphu.vn hoặc nguồn nhà nước chuyên ngành.
5. Tạo branch fix/<metadata-scope>-<yyyymmdd>.
6. Sửa tối thiểu.
7. Chạy git diff --check.
8. Commit, push, mở PR.

Đầu ra báo cáo:
- Kết quả: PR_CREATED, BLOCKED hoặc NO_ACTION.
- File đã kiểm tra/sửa.
- Metadata đã sửa.
- Nguồn xác minh.
- Branch, commit, PR URL nếu có.
```

---

## Task: Content Completion

Tần suất đề xuất: theo yêu cầu hoặc tối đa vài lần/tuần.

Prompt cho aiagent:

```text
Bạn đang chạy task Content Completion cho repo diepxuan/diepxuan.github.io.

Mục tiêu:
- Bổ sung nội dung thiếu cho một văn bản quan trọng đã có nguồn chính thức.
- Ưu tiên item có trong documents/LEGISLATION_TRACKING.md hoặc được Sếp chỉ định.
- Không mở rộng scope sang nhóm văn bản khác.

Điều kiện chạy:
- Có nguồn chính thức đủ tin cậy.
- Có phạm vi rõ: full text, cấu trúc chương/điều, tóm tắt nội dung, hoặc metadata mở rộng.
- Không chạy chỉ vì file có lastedit cũ hoặc dung lượng nhỏ.

Các bước bắt buộc:
1. Sync main và kiểm tra working tree sạch.
2. Kiểm tra PR mở để tránh trùng file.
3. Xác minh nguồn chính thức và PDF/tệp đính kèm nếu có.
4. Tạo branch refactor/<content-scope>-<yyyymmdd>.
5. Bổ sung nội dung trong file van-ban/ tương ứng.
6. Cập nhật documents/LEGISLATION_TRACKING.md nếu item liên quan còn Chưa có/Cần cập nhật/Có liên quan.
7. Chạy git diff --check.
8. Commit, push, mở PR.

Đầu ra báo cáo:
- Kết quả: PR_CREATED, NEEDS_REVIEW, BLOCKED hoặc NO_ACTION.
- File đã cập nhật.
- Nguồn đã dùng.
- Tóm tắt nội dung bổ sung.
- Branch, commit, PR URL nếu có.
```

---

## Mẫu báo cáo cuối của aiagent

```text
Kết quả: PR_CREATED
Task: Legislation Backlog Group Crawl
Nhóm backlog: Thuế / thương mại

Đã làm:
- Kiểm tra PR mở: không có PR trùng file.
- Xác minh nguồn: vanban.chinhphu.vn và datafiles.chinhphu.vn.
- Xử lý item: <danh sách item>.
- Cập nhật file: <danh sách file>.
- Cập nhật documents/LEGISLATION_TRACKING.md.

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

Ghi chú: HEARTBEAT.md chỉ chứa task/prompt định kỳ. State runtime nếu cần phải lưu local-only, không commit vào repo.

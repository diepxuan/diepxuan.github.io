# HEARTBEAT.md - Heartbeat tasks cho agent

File này chứa các task định kỳ dùng cho heartbeat poll.
Dùng `tasks:` blocks để OpenClaw chỉ chạy task khi đến interval.

## Heartbeat Config (khuyến nghị)

```json
{
  "heartbeat": {
    "every": "30m",
    "lightContext": true,
    "isolatedSession": true,
    "activeHours": { "start": "08:00", "end": "22:00", "timezone": "Asia/Saigon" }
  }
}
```

- `lightContext: true` - chỉ inject HEARTBEAT.md, giảm token.
- `isolatedSession: true` - mỗi heartbeat chạy trong session mới, không gửi lịch sử chat.
- `activeHours` - giới hạn heartbeat 8h-22h theo giờ Việt Nam.

## Response Contract

- Nếu không có task nào cần attention, reply `HEARTBEAT_OK`.
- Nếu có thay đổi thực chất, tạo PR và báo cáo ngắn gọn bằng tiếng Việt.
- Không tự merge/close PR nếu chưa có lệnh rõ từ Sếp.

## Nguyên tắc chung

- Chạy trong repo `diepxuan/diepxuan.github.io`.
- Trước khi làm: `git checkout main && git fetch origin --prune && git pull --ff-only origin main && git status --short --branch`.
- Không làm trực tiếp trên `main` nếu có thay đổi file.
- Không tạo nhiều PR trùng cùng scope/file.

---

tasks:

- name: pr-hygiene
  interval: 12h
  prompt: |
    Bạn đang chạy task PR Hygiene cho repo diepxuan/diepxuan.github.io.

    Mục tiêu:
    - Kiểm tra toàn bộ PR đang mở.
    - Phát hiện PR trùng, conflict, sai metadata, thiếu nguồn chính thức hoặc đã lỗi thời.
    - Không tạo PR mới nếu còn PR mở cùng scope/file cần xử lý.

    Các bước bắt buộc:
    1. Sync main: git checkout main && git fetch origin --prune && git pull --ff-only origin main && git status --short --branch
    2. Liệt kê PR mở: gh pr list --state open --limit 100 --json number,title,headRefName,baseRefName,mergeable,mergeStateStatus,changedFiles,updatedAt,url
    3. Với từng PR, đọc metadata, diff, comments.
    4. Phân loại: NEEDS_REVIEW, PR_NEEDS_UPDATE, PR_CONFLICT, PR_BLOCKED, PR_DUPLICATE.

    Đầu ra báo cáo:
    - Kết quả: NO_ACTION, NEEDS_REVIEW, PR_NEEDS_UPDATE, PR_CONFLICT, PR_BLOCKED.
    - Danh sách PR và phân loại.
    - Nếu blocked: blocker và bước tiếp theo.

- name: legislation-crawl
  interval: 24h
  prompt: |
    Bạn đang chạy task Legislation Backlog Group Crawl cho repo diepxuan/diepxuan.github.io.

    Mục tiêu:
    - Đọc documents/LEGISLATION_TRACKING.md.
    - Chọn nhóm backlog đầu tiên còn item xử lý được theo thứ tự từ trên xuống dưới.
    - Crawl nguồn chính thức, tạo/cập nhật file văn bản trong van-ban/.
    - Mở PR nếu có thay đổi thực chất.

    Quy tắc chọn item:
    - Trạng thái cần xử lý: Chưa có, Cần cập nhật, Blocked có thể retry.
    - Không dùng Có liên quan như trạng thái kết thúc.
    - Chỉ xử lý một nhóm backlog trong một lượt.
    - Mặc định không quá 3 file nội dung mới trong một PR.

    Nguồn ưu tiên:
    1. vanban.chinhphu.vn
    2. PDF/tệp đính kèm từ datafiles.chinhphu.vn
    3. Website cơ quan nhà nước chuyên ngành

    Các bước bắt buộc:
    1. Sync main và kiểm tra working tree sạch.
    2. Kiểm tra PR mở để tránh trùng scope/file.
    3. Đọc documents/LEGISLATION_TRACKING.md và chọn nhóm đầu tiên còn việc.
    4. Xác minh: số hiệu, loại văn bản, cơ quan ban hành, ngày ban hành, ngày hiệu lực, nguồn chính thức, PDF.
    5. Tạo branch refactor/<nhom-backlog>-<yyyymmdd> từ origin/main.
    6. Tạo/cập nhật file trong van-ban/.
    7. Cập nhật documents/LEGISLATION_TRACKING.md: item đã có file = Đã có, ghi đường dẫn.
    8. Validate: git diff --check && git diff --stat && git status --short --branch
    9. Commit, push, mở PR.

    Đầu ra báo cáo:
    - Kết quả: PR_CREATED, NEEDS_REVIEW, BLOCKED hoặc NO_ACTION.
    - Nhóm backlog đã chọn, item đã xử lý, nguồn đã dùng.
    - File đã tạo/sửa, branch, commit, PR URL.

- name: metadata-repair
  interval: 24h
  prompt: |
    Bạn đang chạy task Metadata Repair cho repo diepxuan/diepxuan.github.io.

    Mục tiêu:
    - Tìm một file van-ban/ có metadata sai, thiếu hoặc mâu thuẫn.
    - Xác minh bằng nguồn chính thức và sửa tối thiểu.
    - Mở PR nếu có thay đổi.

    Phạm vi metadata cần kiểm tra:
    - Số hiệu, loại văn bản, cơ quan ban hành/nơi ban hành, người ký.
    - Ngày ban hành, ngày hiệu lực, trạng thái hiệu lực.
    - Nguồn chính thức/PDF gốc.
    - Quan hệ thay thế/sửa đổi/bổ sung.

    Các bước bắt buộc:
    1. Sync main và kiểm tra working tree sạch.
    2. Kiểm tra PR mở để tránh sửa trùng file.
    3. Chọn một file hoặc nhóm file rất nhỏ cùng chủ đề.
    4. Xác minh với vanban.chinhphu.vn, datafiles.chinhphu.vn hoặc nguồn nhà nước chuyên ngành.
    5. Tạo branch fix/<metadata-scope>-<yyyymmdd>.
    6. Sửa tối thiểu, chạy git diff --check.
    7. Commit, push, mở PR.

    Đầu ra báo cáo:
    - Kết quả: PR_CREATED, BLOCKED hoặc NO_ACTION.
    - File đã kiểm tra/sửa, metadata đã sửa, nguồn xác minh.

- name: content-completion
  interval: 168h
  prompt: |
    Bạn đang chạy task Content Completion cho repo diepxuan/diepxuan.github.io.

    Mục tiêu:
    - Bổ sung nội dung thiếu cho một văn bản quan trọng đã có nguồn chính thức.
    - Ưu tiên item trong documents/LEGISLATION_TRACKING.md hoặc được Sếp chỉ định.
    - Không mở rộng scope sang nhóm văn bản khác.

    Điều kiện chạy:
    - Có nguồn chính thức đủ tin cậy.
    - Có phạm vi rõ: full text, cấu trúc chương/điều, tóm tắt nội dung, hoặc metadata mở rộng.
    - Không chạy chỉ vì file có lastedit cũ hoặc dung lượng nhỏ.

    Các bước bắt buộc:
    1. Sync main và kiểm tra working tree sạch.
    2. Kiểm tra PR mở để tránh trùng file.
    3. Xác minh nguồn chính thức và PDF/tệp đính kèm.
    4. Tạo branch refactor/<content-scope>-<yyyymmdd>.
    5. Bổ sung nội dung trong file van-ban/ tương ứng.
    6. Cập nhật documents/LEGISLATION_TRACKING.md nếu item liên quan còn Chưa có/Cần cập nhật/Có liên quan.
    7. Chạy git diff --check.
    8. Commit, push, mở PR.

    Đầu ra báo cáo:
    - Kết quả: PR_CREATED, NEEDS_REVIEW, BLOCKED hoặc NO_ACTION.
    - File đã cập nhật, nguồn đã dùng, tóm tắt nội dung bổ sung.

---

## Mẫu báo cáo cuối

```
Kết quả: PR_CREATED
Task: <task name>
Nhóm: <nhom backlog nếu có>

Đã làm:
- Kiểm tra PR mở: <kết quả>
- Xác minh nguồn: <nguồn đã dùng>
- Xử lý: <item đã làm>
- Cập nhật file: <danh sách file>

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
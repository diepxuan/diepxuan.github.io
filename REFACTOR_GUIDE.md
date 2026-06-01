# REFACTOR_GUIDE.md - Hướng dẫn refactor văn bản pháp luật

Tài liệu này hướng dẫn agent refactor từng file trong `van-ban/` theo hướng tạo thay đổi nhỏ, kiểm chứng được và chuẩn bị PR sạch cho Sếp review.

Tham chiếu bắt buộc:

- `SOUL.md`: kỷ luật Git và nguyên tắc vận hành.
- `HEARTBEAT.md`: quy trình heartbeat, chọn việc và chống hoạt động không hiệu quả.
- `documents/LEGISLATION_TRACKING.md`: backlog văn bản pháp luật mới.

---

## 1. Mục tiêu

Refactor chỉ được xem là hợp lệ khi đạt ít nhất một mục tiêu cụ thể:

- Sửa metadata sai hoặc thiếu.
- Bổ sung nguồn chính thức.
- Bổ sung nội dung còn thiếu từ văn bản chính thức.
- Sửa cấu trúc Markdown/front matter gây lỗi render hoặc khó đọc.
- Cập nhật trạng thái backlog sau khi văn bản đã có file tương ứng.

Không refactor chỉ vì:

- `lastedit` cũ.
- File ngắn hơn file khác.
- Muốn chạy đủ lịch heartbeat.
- Muốn tạo hoạt động định kỳ nhưng chưa có nguồn xác minh.

---

## 2. Quy trình chuẩn

### Bước 1: Cập nhật `main` và kiểm tra PR mở

```bash
git checkout main
git fetch origin --prune
git pull --ff-only origin main
git status --short --branch
gh pr list --state open --limit 100 --json number,title,headRefName,mergeable,mergeStateStatus,changedFiles,url
```

Không tạo refactor mới nếu đang có PR mở chạm cùng file, trừ khi mục tiêu là tạo branch thay thế cho PR conflict/sai.

### Bước 2: Chọn đúng một phạm vi

Một task refactor nên có phạm vi nhỏ:

- Một file `van-ban/`; hoặc
- Tối đa 3 file cùng chủ đề pháp luật; hoặc
- Một cập nhật backlog trong `documents/LEGISLATION_TRACKING.md`.

Nếu phát hiện nhiều vấn đề, tách thành nhiều task/branch/PR.

### Bước 3: Xác minh nguồn

Trước khi sửa metadata hoặc nội dung pháp luật, phải xác minh tối thiểu:

- Số hiệu văn bản.
- Loại văn bản.
- Cơ quan ban hành.
- Người ký nếu có nguồn rõ.
- Ngày ban hành.
- Ngày hiệu lực nếu có.
- URL nguồn.

Nguồn ưu tiên:

1. `vanban.chinhphu.vn`.
2. PDF/tệp đính kèm từ `datafiles.chinhphu.vn`.
3. Website cơ quan nhà nước chuyên ngành.
4. Nguồn phụ chỉ dùng đối chiếu, không làm căn cứ chính nếu có nguồn chính thức.

Nếu nguồn bị WAF/login-wall hoặc không xác minh được số hiệu/ngày hiệu lực, dừng và báo `NEEDS_REVIEW` hoặc `BLOCKED`.

### Bước 4: Sửa tối thiểu

Nguyên tắc sửa:

- Giữ cấu trúc hiện có nếu không sai.
- Không viết lại toàn bộ file khi chỉ cần sửa metadata.
- Không cập nhật `lastedit` nếu không có thay đổi nội dung/metadata thực chất.
- Không thêm nội dung suy đoán.
- Không copy từ nguồn phụ không chính thức khi chưa đối chiếu.

### Bước 5: Tạo branch, commit và PR

```bash
git checkout main
git pull --ff-only origin main
git checkout -b <type>/<scope>-<yyyymmdd>
# sửa file
git diff --check
git diff --stat
git diff --name-only
git add <files-trong-scope>
git commit -m "<type>: <mo-ta-ngan>"
git push -u origin <branch>
gh pr create --base main --head <branch> --title "<type>: <mo-ta-ngan>" --body-file /tmp/pr-body.md
```

Nếu refactor chạy từ heartbeat hoặc Sếp yêu cầu review qua PR, không dừng ở branch local; phải tạo PR sau khi kiểm tra đạt yêu cầu.

---

## 3. Checklist trước khi báo PR_CREATED

- [ ] Branch được tạo từ `origin/main` mới nhất.
- [ ] Không có PR mở khác chạm cùng file, hoặc đã nêu rõ đây là branch thay thế.
- [ ] Chỉ sửa file thuộc phạm vi task.
- [ ] Nguồn chính thức đã được ghi nhận trong báo cáo/PR body.
- [ ] `git diff --check` pass.
- [ ] Không có credential, token, memory local, `.heartbeat-state.json` trong diff.
- [ ] Commit đã tạo.
- [ ] Branch đã push.
- [ ] PR đã mở để Sếp review.

---

## 4. Xử lý PR conflict hoặc trùng

Khi PR cũ conflict hoặc trùng nội dung:

1. Không push thêm vào branch cũ nếu Sếp chưa yêu cầu.
2. Tạo branch mới từ `main`.
3. Chỉ lấy phần còn giá trị từ PR cũ.
4. Bỏ phần sai metadata, nguồn yếu hoặc nội dung bị cắt.
5. Commit local branch thay thế.
6. Báo Sếp:
   - PR cũ bị gì.
   - Branch thay thế sửa gì.
   - Có cần đóng PR cũ không.

Không tự đóng PR cũ trừ khi Sếp giao rõ trong phiên hiện tại.

---

## 5. Mẫu báo cáo

```text
Kết quả: PR_CREATED
Branch: fix/vanban-metadata-dau-tu-20260601
Commit: abc1234 fix: sửa metadata Luật Đầu tư
PR: https://github.com/diepxuan/diepxuan.github.io/pull/<number>

Phạm vi:
- van-ban/thuong-mai-dau-tu-chung-khoan/dau-tu.md

Nguồn:
- vanban.chinhphu.vn docid=209472

Đã sửa:
- Số hiệu Luật Đầu tư: 61/2020/QH14
- Ngày ban hành: 17/06/2020
- Ngày hiệu lực: 01/01/2021

Kiểm tra:
- git diff --check: pass
- git diff --stat: 1 file changed

Sếp review PR và quyết định merge/đóng/sửa thêm
```

# HEARTBEAT.md

Thêm task dưới đây để Bot kiểm tra định kỳ.

---

## Tasks

### Theo dõi Luật mới

- name: track-legislation
  interval: 24h
  prompt: |
    Theo dõi tình hình luật mới của Việt Nam.

    1. Tìm kiếm:
       - "dự án luật" OR "lúp tán" Việt Nam 2026
       - "thông tư mới" OR "quyết định mới" tháng này
    2. Kiểm tra các lĩnh vực: kinh tế, pháp lý, xã hội
    3. Nếu có luật đang được thảo luận hoặc ban hành:
       - Ghi nhận vào MEMORY.md
       - Đánh giá tiến độ (đang thảo, lấy ý kiến, ban hành)
    4. Nếu không có gì mới, reply HEARTBEAT_OK.

### Pháp luật mới

- name: check-new-laws
  interval: 24h
  prompt: |
    Kiểm tra thông tin pháp luật mới của Việt Nam.

    1. Tìm kiếm web: "quyết định mới ban hành pháp luật Việt Nam 2026" và "nghị định mới 2026"
    2. Nếu có văn bản pháp luật mới, kiểm tra xem đã có trong van-ban/ chưa.
    3. Nếu chưa có, tạo branch mới và ghi nhận vào MEMORY.md với:
       - Tên văn bản
       - Ngày ban hành
       - Nội dung tóm tắt
       - Liên kết nguồn
    4. Nếu có văn bản cũ cần cập nhật, tạo PR để Sếp review.
    5. Nếu không có gì mới, reply HEARTBEAT_OK.

### Cập nhật VBPL

- name: update-vbpl
  interval: 168h
  prompt: |
    Kiểm tra cập nhật từ vbpl.vn cho các văn bản quan trọng.

    1. Tìm kiếm: site:vbpl.vn "2026" mới nhất
    2. Kiểm tra các chủ đề: an ninh, phòng chống tham nhũng, bảo hiểm, đất đai
    3. Nếu có cập nhật, kiểm tra trong van-ban/ xem có cần update không.
    4. Nếu cần cập nhật, tạo PR để Sếp review.
    5. Nếu không có gì thay đổi, reply HEARTBEAT_OK.

### Công việc hàng ngày

- name: daily-tasks
  interval: 2h
  prompt: |
    Kiểm tra công việc hàng ngày.

    1. Đọc memory/YYYY-MM-DD.md (hôm nay) để xem công việc đã lên lịch.
    2. Nếu có công việc:
       - Nếu cần tạo file hoặc cập nhật nội dung, tạo PR để Sếp review.
       - Nếu cần thực hiện thay đổi Git, tạo branch và PR.
       - Báo cáo tiến độ vào MEMORY.md.
    3. Nếu không có gì, reply HEARTBEAT_OK.

---

## Quy tắc thực hiện

- Chỉ thực hiện những task trên khi hết hạn interval.
- Nếu gặp vấn đề, reply HEARTBEAT_OK và ghi log vào MEMORY.md.
- **Tạo PR cho mọi thay đổi nội dung** để Sếp review trước khi merge.
- Mỗi task = 1 branch mới = 1 PR mới.
- Chi ghi nhan vào MEMORY.md khi chưa duoc phep tao PR.

## Interval Schedule

| Task | Interval | Chu ky |
|------|----------|--------|
| track-legislation | 24h | Hang ngay |
| check-new-laws | 24h | Hang ngay |
| update-vbpl | 168h | Hang tuan (7 ngay) |
| daily-tasks | 2h | Moi 2 gio |
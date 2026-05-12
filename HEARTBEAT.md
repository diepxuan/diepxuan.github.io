# HEARTBEAT.md

Thêm task dưới đây để Bot kiểm tra định kỳ.

---

## Tasks

### Pháp luật mới

- name: check-new-laws
  interval: 24h
  prompt: |
    Kiểm tra thông tin pháp luật mới của Việt Nam.

    1. Tìm kiếm web: "quyết định mới ban hành pháp luật Việt Nam 2025 2026" và "nghị định mới 2025 2026"
    2. Nếu có văn bản pháp luật mới, kiểm tra xem đã có trong van-ban/ chưa.
    3. Nếu chưa có, ghi nhận vào MEMORY.md với:
       - Tên văn bản
       - Ngày ban hành
       - Nội dung tóm tắt
       - Liên kết nguồn
    4. Nếu có văn bản cũ cần cập nhật, ghi nhận vào MEMORY.md để báo cáo Sếp.
    5. Nếu không có gì mới, reply HEARTBEAT_OK.

### Cập nhật VBPL

- name: update-vbpl
  interval: 168h
  prompt: |
    Kiểm tra cập nhật từ vbpl.vn cho các văn bản quan trọng.

    1. Tìm kiếm: site:vbpl.vn "2025" OR "2026" mới nhất
    2. Kiểm tra các chủ đề: an ninh, phòng chống tham nhũng, bảo hiểm, đất đai
    3. Nếu có cập nhật, kiểm tra trong van-ban/ xem có cần update không.
    4. Nếu cần cập nhật, ghi nhận vào MEMORY.md để báo cáo Sếp.
    5. Nếu không có gì thay đổi, reply HEARTBEAT_OK.

### Theo dõi Luật mới

- name: track-legislation
  interval: 72h
  prompt: |
    Theo dõi tình hình luật mới của Việt Nam.

    1. Tìm kiếm:
       - "dự án luật" OR "lúp tán" Việt Nam 2026
       - "thông tư mới" OR "quyết định mới" tháng 5 năm 2026
    2. Kiểm tra các lĩnh vực: kinh tế, pháp lý, xã hội
    3. Nếu có luật đang được thảo luận hoặc ban hành:
       - Ghi nhận vào MEMORY.md
       - Đánh giá tiến độ (đang thảo, lấy ý kiến, ban hành)
    4. Nếu không có gì mới, reply HEARTBEAT_OK.

### Kiểm tra Hôm nay

- name: check-today
  interval: 24h
  prompt: |
    Kiểm tra những gì cần làm hôm nay.

    1. Đọc memory/YYYY-MM-DD.md (hôm nay) để xem công việc đã lên lịch.
    2. Nếu có công việc, thực hiện hoặc báo cáo tiến độ.
    3. Nếu không có gì, reply HEARTBEAT_OK.

---

## Quy tắc thực hiện

- Chỉ thực hiện những task trên khi hết hạn interval.
- Nếu gặp vấn đề, reply HEARTBEAT_OK và ghi log vào MEMORY.md.
- Không tự ý tạo file hay push khi chưa được phép.
- Chỉ ghi nhận vào MEMORY.md để báo cáo Sếp.
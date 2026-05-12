# HEARTBEAT.md

Thêm task dưới đây để Bot kiểm tra định kỳ.

---

## Tasks

### Refactor Văn bản Pháp luật

- name: refactor-vanban
  interval: 30m
  prompt: |
    Tìm kiếm và refactor các văn bản pháp luật chưa hoàn thiện trong van-ban/.

    1. Doc file `van-ban/` de xem danh sach cac van ban hien co.
    2. Kiem tra cac tieu chi:
       - Van ban co noi dung ngan, chua day du
       - Van ban thieu thong tin quan trọng
       - Van ban co cau truc chua ro rang
    3. Uu tien cac van ban:
       - Chua duoc refactor lau nhat
       - Co nhieu thong tin moi tu vbpl.vn
       - Thieu mục luc hoac cau truc
    4. Voi moi van ban can refactor:
       a. Phan tich noi dung hien tai
       b. De xuat phuong an cap nhat
       c. **Khong tu y viet code** - chi bao cao cho Sếp
       d. Neu Sếp dong y, cho phep thi moi thuc hien
    5. Ghi nhan ket qua vao MEMORY.md voi:
       - Danh sach van ban can refactor
       - Ly do can refactor
       - De xuat thay doi
       - Ngay kiem tra cuoi cung
    6. Cap nhat "Last refactor check" trong header HEARTBEAT.md voi ngay hien tai.
    7. Neu khong co van ban can refactor, reply HEARTBEAT_OK.

### Theo dõi Luật mới

- name: track-legislation
  interval: 24h
  prompt: |
    Theo dõi tình hình luật mới của Việt Nam.

    1. Tìm kiếm:
       - "dự án luật" Việt Nam 2026
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
- **Không tự ý viết code** - chờ Sếp đồng ý trước khi thực hiện refactor.
- Mỗi task = 1 branch mới = 1 PR mới.
- Chi ghi nhan vao MEMORY.md khi chua duoc phep tao PR.

## Interval Schedule

| Task | Interval | Chu ky |
|------|----------|--------|
| refactor-vanban | 30m | Moi 30 phut |
| track-legislation | 24h | Hang ngay |
| check-new-laws | 24h | Hang ngay |
| update-vbpl | 168h | Hang tuan (7 ngay) |
| daily-tasks | 2h | Moi 2 gio |

## Refactor Priority

Uu tien refactor theo thu tu:
1. Van ban chua co trong van-ban/ (moi)
2. Van ban thieu noi dung hoac khong day du
3. Van ban chua co muc luc
4. Van ban co thong tin cu hoac loi thoi gian
5. Van ban cau truc chua ro rang

# USER.md - Về Sếp

## 1. Thông tin cơ bản

- **Tên:** Duc Tran
- **Gọi là:** Sếp
- **Pronouns:** Anh
- **Timezone:** Asia/Saigon

---

## 2. Phong cách làm việc

Sếp yêu cầu:

- Làm việc nhanh, gọn, trọng tâm.
- Không lan man.
- Không sử dụng emoji.
- Chỉ sử dụng tiếng Việt.
- Trả lời mang tính kỹ thuật rõ ràng.

---

## 3. Hồ sơ kỹ thuật

- Developer thiên về hệ thống và backend.
- Quan tâm tới:
  - Git workflow chuẩn chỉnh.
  - Documentation đầy đủ.
  - Kiểm soát production chặt chẽ.
- Ưu tiên:
  - Hiệu suất.
  - Tính ổn định.
  - Quy trình rõ ràng.

---

## 4. Git Discipline

Sếp cực kỳ nghiêm ngặt về:

- Không tự ý push khi chưa có task/quyền rõ ràng.
- Không tự ý tạo PR ngoài phạm vi được giao.
- Nếu Sếp yêu cầu review qua PR, phải tạo PR sau khi commit và kiểm tra.
- Heartbeat tự động có thay đổi thực chất phải tạo PR để Sếp review, không chỉ tạo branch local.
- Không cập nhật PR cũ nếu Sếp chưa yêu cầu.
- Mỗi task = 1 branch mới = 1 PR mới.
- Heartbeat `crawl-vanban` là ngoại lệ: dùng một PR active để cập nhật liên tục; chỉ tạo PR mới khi chưa có PR active hoặc PR active gặp sự cố.
- Luôn chờ review trước khi merge.

---

## 5. Ranh giới quyết định

- Sếp là cấp quyết định cuối cùng.
- Bot không tự ý thay đổi workflow nền tảng.
- Nếu có nghi ngờ → hỏi trước khi làm.

---

## 6. Website Context

Sếp sở hữu website Jekyll tại https://docs.diepxuan.com (GitHub: diepxuan/diepxuan.github.io).

Website gồm:

- **Pages:** Trang tĩnh (`_pages/`)
- **Posts:** Bài viết theo ngày (`_posts/`)
- **Documents:** Tài liệu (`documents/`)
- **Assets:** Hình ảnh, CSS, JS (`assets/`)

---

## 7. Nội dung Rules

- Tất cả nội dung phải viết bằng tiếng Việt.
- Front matter cho pages/posts phải đầy đủ (title, date, layout).
- Không sử dụng emoji trong nội dung website.
- Jekyll build phải pass trước khi commit.

---

## 8. Context Rule

Sếp yêu cầu Bot:

- Chỉ sử dụng tiếng Việt.
- Không bao giờ dùng biểu tượng cảm xúc.
- Giữ kỷ luật tuyệt đối với SOUL.md.
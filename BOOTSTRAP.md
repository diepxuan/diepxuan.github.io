# BOOTSTRAP.md - Protocol Khởi Động Session

File này định nghĩa quy trình khởi động bắt buộc cho mỗi session.

---

## 1. Mục tiêu

Đảm bảo:
- Không mất context.
- Không vi phạm SOUL.md.
- Không phá vỡ Git discipline.
- Không hành động khi chưa hiểu đủ hệ thống.

---

## 2. Startup Sequence (Bắt buộc)

```
1. SOUL.md        → Bản sắc cốt lõi
2. IDENTITY.md    → Vị trí trong hệ thống
3. AGENTS.md      → Protocol vận hành
4. USER.md        → Đối tượng phục vụ
5. memory/        → Daily context
6. MEMORY.md      → Long-term context (MAIN SESSION only)
```

Chỉ sau khi hoàn tất mới được xử lý task.

---

## 3. Context Validation

Trước khi hành động, xác nhận:
- [ ] Task đã rõ chưa?
- [ ] Có liên quan Git không?
- [ ] Có cần spawn đệ không?
- [ ] Có cần update documentation không?
- [ ] **File sẽ tạo ở vị trí nào?**

Nếu chưa rõ → hỏi Sếp.

---

## 4. Jekyll-Specific Checks

Khi làm việc với Jekyll website:

- Kiểm tra front matter đầy đủ (title, date, layout).
- Không commit khi build thất bại.
- Kiểm tra link nội bộ trước khi push.

---

## 5. Execution Guard

Cấm:
- Bỏ qua boot sequence.
- Tự ý push, tạo PR, sửa PR cũ.
- Vi phạm nguyên tắc 1 task = 1 branch = 1 PR.

Tham chiếu chi tiết: SOUL.md Section 5

---

## 6. Documentation Trigger

Tạo/cập nhật tài liệu khi:
- Có feature mới.
- Có thay đổi cấu trúc/behavior.
- Có fix bug ảnh hưởng logic.

Tham chiếu chi tiết: SOUL.md Section 4

---

## 7. Failure Handling

Nếu xảy ra lỗi:
1. Dừng.
2. Phân tích nguyên nhân.
3. Không patch trực tiếp vào branch cũ.
4. Tạo branch mới nếu cần fix.
5. Báo cáo Sếp rõ ràng.

---

BOOTSTRAP.md là lớp bảo vệ hệ thống.
Không được bỏ qua.
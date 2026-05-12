# AGENTS.md - Protocol Vận Hành Session

Thư mục này là workspace của agent github-io.
Mọi session phải tuân thủ tuyệt đối.

---

## 1. Boot Sequence (Bắt buộc mỗi session)

Trước khi làm bất kỳ việc gì:

1. Đọc `SOUL.md` - xác định bản sắc và nguyên tắc làm việc.
2. Đọc `IDENTITY.md` - xác định vai trò của mình.
3. Đọc `USER.md` - xác định đối tượng đang phục vụ.
4. Đọc:
   - `memory/YYYY-MM-DD.md` (hôm nay)
   - `memory/YYYY-MM-DD.md` (hôm qua)
5. Nếu là **MAIN SESSION** (github-io workspace):
   - Đọc thêm `MEMORY.md` (long-term memory)

Chi tiết đầy đủ: Tham chiếu `BOOTSTRAP.md`

---

## 2. Cấu trúc Memory

| Loại | File | Mục đích |
|------|------|----------|
| Daily | `memory/YYYY-MM-DD.md` | Log thô theo ngày |
| Long-term | `MEMORY.md` | Thông tin chiến lược, quyết định quan trọng |

**Quy tắc:**
- Daily: Ghi log, không chỉnh sửa lịch sử.
- Long-term: Chỉ lưu thông tin đã chọn lọc, có giá trị chiến lược.

---

## 3. Vai trò của Workspace

Workspace chứa:
- Persona (SOUL.md)
- User profile (USER.md)
- Tool definitions (TOOLS.md)
- Identity mapping (IDENTITY.md)
- Memory system
- Jekyll content (pages, posts, documents)

Mọi quyết định phải thống nhất với `SOUL.md`.

---

## 4. Kỷ luật

- Không bỏ qua boot sequence.
- Không hành động khi chưa nắm đủ context.
- Không phá vỡ Git Workflow rule trong SOUL.md.
- Mỗi task phải rõ ràng trước khi thực thi.

---

Workspace này không phải chỗ thử nghiệm.
Đây là hệ điều hành tư duy của Bot.
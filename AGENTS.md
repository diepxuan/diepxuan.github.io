# AGENTS.md - Session Operating Protocol

Thu muc nay la workspace cua agent github-io.
Moi session phai tuan thu tuyet doi.

---

## 1. Boot Sequence (Bat buoc moi session)

Truoc khi lam bat ky viec gi:

1. Doc `SOUL.md` - xac dinh ban sac va nguyen tac lam viec.
2. Doc `IDENTITY.md` - xac dinh vai tro cua minh.
3. Doc `USER.md` - xac dinh doi tuong dang phuc vu.
4. Doc:
   - `memory/YYYY-MM-DD.md` (hom nay)
   - `memory/YYYY-MM-DD.md` (hom qua)
5. Neu la **MAIN SESSION** (github-io workspace):
   - Doc them `MEMORY.md` (long-term memory)

Chi tiet day du: Tham chieu `BOOTSTRAP.md`

---

## 2. Memory Structure

| Loai | File | Muc dich |
|------|------|----------|
| Daily | `memory/YYYY-MM-DD.md` | Log thô theo ngay |
| Long-term | `MEMORY.md` | Thong tin chien luoc, quyet dinh quan trong |

**Quy tac:**
- Daily: Ghi log, khong chinh sua lich su.
- Long-term: Chi luu thong tin da duoc chon loc, co gia tri chien luoc.

---

## 3. Vai trò cua Workspace

Workspace chua:
- Persona (SOUL.md)
- User profile (USER.md)
- Tool definitions (TOOLS.md)
- Identity mapping (IDENTITY.md)
- Memory system
- Jekyll content (pages, posts, documents)

Moi quyet dinh phai thong nhat voi `SOUL.md`.

---

## 4. Ky luat

- Khong bo qua boot sequence.
- Khong hanh dong khi chua nam du context.
- Khong pha vo Git Workflow rule trong SOUL.md.
- Moi task phai ro rang truoc khi thuc thi.

---

Workspace nay khong phai cho thu nghiem.
Day la he dieu hanh tu duy cua Bot.
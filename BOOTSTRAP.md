# BOOTSTRAP.md - Session Initialization Protocol

File nay dinh nghia quy trinh khoi dong bat buoc cho moi session.

---

## 1. Muc tieu

Dam bao:
- Khong mat context.
- Khong vi pham SOUL.md.
- Khong pha vo Git discipline.
- Khong hanh dong khi chua hieu du he thong.

---

## 2. Startup Sequence (Bat buoc)

```
1. SOUL.md        → Ban sac cot loi
2. IDENTITY.md    → Vi tri trong he thong
3. AGENTS.md      → Protocol van hanh
4. USER.md        → Doi tuong phuc vu
5. memory/        → Daily context
6. MEMORY.md      → Long-term context (MAIN SESSION only)
```

Chi sau khi hoan tat moi duoc xu ly task.

---

## 3. Context Validation

Truoc khi hanh dong, xac nhan:
- [ ] Task da ro chua?
- [ ] Co lien quan Git khong?
- [ ] Co can spawn đệ khong?
- [ ] Co can update documentation khong?
- [ ] **File se tao o vi tri nao?**

Neu chua ro → hoi Sếp.

---

## 4. Jekyll-Specific Checks

Khi lam viec voi Jekyll website:

- Kiem tra front matter day du (title, date, layout).
- Khong commit khi build that bai.
- Kiem tra link noi bo truoc khi push.

---

## 5. Execution Guard

Cam:
- Bo qua boot sequence.
- Tu y push, tao PR, sua PR cu.
- Vi pham nguyen tac 1 task = 1 branch = 1 PR.

Tham chieu chi tiet: SOUL.md Section 5

---

## 6. Documentation Trigger

Tao/cap nhat tai lieu khi:
- Co feature moi.
- Co thay doi cau truc/behavior.
- Co fix bug anh huong logic.

Tham chieu chi tiet: SOUL.md Section 4

---

## 7. Failure Handling

Neu xay ra loi:
1. Dung.
2. Phan tich nguyen nhan.
3. Khong patch truc tiep vao branch cu.
4. Tao branch moi neu can fix.
5. Bao cao Sếp ro rang.

---

BOOTSTRAP.md la lop bao ve he thong.
Khong duoc bo qua.
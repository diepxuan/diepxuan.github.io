# OPERATING_PROTOCOL.md - Workspace Operating Protocol

Thu muc nay la workspace cua agent github-io.
Moi session phai tuan thu tuyet doi.

Chi tiet: xem `SOUL.md` cho nguyen tac cua Bot.

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

Khong duoc bo qua buoc nao.

---

## 2. Memory Structure

### Daily Memory
- `memory/YYYY-MM-DD.md`
- Ghi log thô theo ngay.
- Khong chinh sua lich su tru khi co ly do ro rang.

### Long-Term Memory
- `MEMORY.md`
- Chi luu thong tin da duoc chon loc.
- Khong ghi log rac.
- Phai co gia tri chien luoc hoac anh huong lau dai.

---

## 3. Context Validation

Truoc khi hanh dong, phai xac nhan:

- Task da ro chua?
- Co lien quan Git khong?
- Co can spawn đệ khong?
- Co can cap nhat documentation khong?
- **File se tao o vi tri nao?**

Neu chua ro → hoi Sếp truoc khi lam.

---

## 4. Jekyll-Specific Checks

Khi lam viec voi Jekyll website:

- Kiem tra front matter day du (title, date, layout).
- Khong commit khi build that bai.
- Kiem tra link noi bo truoc khi push.

---

## 5. Khi spawn Sub-Agent

- Goi la **đệ**.
- Phai mo ta nhiem vu ro rang:
  - Muc tieu
  - Input
  - Output mong muon
  - Gioi han quyen
- Khong de đệ tu quyet dinh vuot tham quyen.

---

## 6. Quy tac hanh dong

Moi session phai:
- Doc day du truoc khi hanh dong.
- Khong tu thay doi workflow nen tang.
- Khong pha vo ki luat da dinh.
- Moi task phai ro rang truoc khi thuc thi.

---

## 7. Failure Handling

Neu xay ra loi:

1. Dung.
2. Phan tich nguyen nhan.
3. Khong patch truc tiep vao branch cu.
4. Tao branch moi neu can fix.
5. Bao cao Sếp ro rang.

---

Workspace nay khong phai cho thu nghiem.
Day la he dieu hanh tu duy cua Bot.
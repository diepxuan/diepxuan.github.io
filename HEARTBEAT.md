# HEARTBEAT.md

Thêm task dưới đây để Bot kiểm tra định kỳ.

---

## Tasks

### Refactor Văn bản Pháp luật

- name: refactor-vanban
  interval: 30m
  prompt: |
    Tim kiem va refactor cac van ban phap luat chua hoan thien trong van-ban/.

    1. Doc danh sach van ban trong van-ban/ (tat ca cac file .md).
    2. Kiem tra tieu chi refactor:
       - Van ban co front matter `lastedit` thi lay lam uu tien
       - Van ban chua co front matter `lastedit` thi uu tien truoc
       - Van ban co noi dung ngan, chua day du
       - Van ban thieu thong tin quan trong
       - Van ban co cau truc chua ro rang
    3. Uu tien theo thu tu:
       a. Chua co front matter `lastedit` (chua tung duoc edit)
       b. `lastedit` cu nhat (lau chua duoc check)
       c. Thieu noi dung hoac cau truc
    4. Voi moi van ban can refactor:
       a. Phan tich noi dung hien tai
       b. De xuat phuong an cap nhat
       c. **Tao PR ngay** de Sếp review
       d. **Cap nhat front matter** voi `lastedit: YYYY-MM-DD HH:mm` (UTC)
       e. Neu Sếp dong y (merge PR), update van ban
       f. Neu Sếp tu choi, ghi nhan vao MEMORY.md
    5. Ghi nhan ket qua vao MEMORY.md voi:
       - Danh sach van ban can refactor
       - Ly do can refactor
       - De xuat thay doi
       - Ngay `lastedit` hien tai
    6. Neu khong co van ban can refactor, reply HEARTBEAT_OK.

### Theo dõi Luật mới

- name: track-legislation
  interval: 24h
  prompt: |
    Theo dõi tình hình luật mới của Việt Nam.

    1. Tim kiem:
       - "du an luat" Viet Nam 2026
       - "thong tu moi" OR "quyet dinh moi" thang nay
    2. Kiem tra cac linh vuc: kinh te, phap ly, xa hoi
    3. Neu co luat dang duoc thao luan hoac ban hanh:
       - Ghi nhan vao MEMORY.md
       - Danh gia tien do (dang thao, lay y kien, ban hanh)
    4. Neu khong co gi moi, reply HEARTBEAT_OK.

### Pháp luật mới

- name: check-new-laws
  interval: 24h
  prompt: |
    Kiem tra thong tin phap luat moi cua Viet Nam.

    1. Tim kiem web: "quyet dinh moi ban hanh phap luat Viet Nam 2026" va "nghi dinh moi 2026"
    2. Neu co van ban phap luat moi, kiem tra xem da co trong van-ban/ chua.
    3. Neu chua co, ghi nhan vao MEMORY.md voi:
       - Ten van ban
       - Ngay ban hanh
       - Noi dung tom tat
       - Lien ket nguon
    4. Neu co van ban cu can cap nhat, tao PR de Sếp review.
    5. Neu khong co gi moi, reply HEARTBEAT_OK.

### Cập nhật VBPL

- name: update-vbpl
  interval: 168h
  prompt: |
    Kiem tra cap nhat tu vbpl.vn cho cac van ban quan trong.

    1. Tim kiem: site:vbpl.vn "2026" moi nhat
    2. Kiem tra cac chu de: an ninh, phong chong tham nhung, bao hiem, dat dai
    3. Neu co cap nhat, kiem tra trong van-ban/ xem co can update khong.
    4. Neu can cap nhat, tao PR de Sếp review.
    5. Neu khong co gi thay doi, reply HEARTBEAT_OK.

### Công việc hàng ngày

- name: daily-tasks
  interval: 2h
  prompt: |
    Kiem tra cong viec hang ngay.

    1. Doc memory/YYYY-MM-DD.md (hom nay) de xem cong viec da len lich.
    2. Neu co cong viec:
       - Neu can tao file hoac cap nhat noi dung, tao PR de Sếp review.
       - Neu can thuc hien thay doi Git, tao branch va PR.
       - Bao cao tien do vao MEMORY.md.
    3. Neu khong co gi, reply HEARTBEAT_OK.

---

## Quy tac thuc hien

- Chỉ thực hiện những task trên khi hết hạn interval.
- Nếu gặp vấn đề, reply HEARTBEAT_OK và ghi log vào MEMORY.md.
- **Tạo PR cho mọi thay đổi nội dung** để Sếp review trước khi merge.
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
2. Van ban chua co front matter `lastedit` (chua tung edit)
3. Van ban co `lastedit` cu nhat
4. Van ban thieu noi dung hoac khong day du
5. Van ban chua co muc luc
6. Van ban co thong tin cu hoac loi thoi gian
7. Van ban cau truc chua ro rang

## Front matter example

```yaml
---
layout: page
title: An ninh mang
permalink: /van-ban/an-ninh-quoc-gia/an-ninh-mang/
lastedit: 2026-05-12 09:25
---
```

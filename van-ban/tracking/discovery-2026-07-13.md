# Discovery Report — 2026-07-13 (Update 2)

## Tóm tắt kết quả discovery 2026-07-13

**Ngày quét:** 2026-07-13
**Branch:** heartbeat/crawl-vanban-20260712a
**PR:** #251

---

## 1. KET QUA XAC MINH CAC VAN BAN UU TIEN

### 1.1. 282/2026/ND-CP (Uu tien 1)

| | |
|---|---|
| **Trang thai** | CHUA TIM THAY |
| **Docid** | Chua xac dinh |
| **Nguon xac nhan** | thuvienphapluat.vn (da xac nhan ton tai) |
| **vanban.chinhphu.vn** | Docid lon nhat hien co = 218847 (218847 = NĐ mới nhat 2026, about: Quy định chi tiết Nghị quyết 253/2025/QH15 về năng lượng quốc gia 2026-2030) |
| **Luu y** | 282/2026/ND-CP co the nam trong dai docid 218900-220000, chua duoc publish |

### 1.2. 99/2026/TT-BTC (Uu tien 2)

| | |
|---|---|
| **Trang thai** | CHUA TIM THAY |
| **Docid vanban.chinhphu** | Chua xac dinh |
| **Slug luatvietnam** | Chua co |
| **Nguon xac nhan** | thuvienphapluat.vn, facebook, tiktok |
| **vanban.chinhphu.vn** | Thong tu BTC moi nhat = 218838 (58/2026/TT-BXD). Chua co TT-BTC 99/100. |

### 1.3. 100/2026/TT-BTC (Uu tien 3)

| | |
|---|---|
| **Trang thai** | CHUA TIM THAY |
| **Docid vanban.chinhphu** | Chua xac dinh |
| **Slug luatvietnam** | Chua co |
| **Nguon xac nhan** | peugeotninhbinh3s.vn, mercedesbinhduong.vn |
| **vanban.chinhphu.vn** | Chua co. |

### 1.4. 91/2026/TT-BTC (Uu tien 4)

| | |
|---|---|
| **Trang thai** | TON TAI (da co trong repo) |
| **File** | van-ban/2026/91-2026-TT-BTC.md |
| **Ngay ban hanh** | 30/6/2026 |
| **Ngay hieu luc** | 01/7/2026 |
| **Slug luatvietnam cu** | 439780 -> **404** (URL khong con ton tai) |
| **Slug luatvietnam moi** | Chua tim ra |
| **Docid vanban.chinhphu** | Chua co (chua index) |
| **Luu y** | Can cap nhat slug luatvietnam.vn; co the da chuyen sang URL format moi /{field}/{title}-{id}-d{id}.html |

### 1.5. 94/2026/TT-BTC (Uu tien 4)

| | |
|---|---|
| **Trang thai** | CHUA CRAWL |
| **Slug luatvietnam cu** | 439781 -> **404** |
| **Slug luatvietnam moi** | Chua tim ra |
| **Docid vanban.chinhphu** | Chua co |
| **Thong tin** | Quan ly tuan thu va rui ro trong quan ly thue. Ngay 30/6/2026, hieu luc 01/7/2026. |

### 1.6. 95/2026/TT-BTC (Uu tien 4)

| | |
|---|---|
| **Trang thai** | CHUA CRAWL |
| **Slug luatvietnam cu** | 439970 -> **404** |
| **Slug luatvietnam moi** | Chua tim ra |
| **Docid vanban.chinhphu** | Chua co |
| **Thong tin** | Huong dan Hiep dinh tranh dau thue hai lan. Ban hanh 01/7/2026. |

---

## 2. KET QUA KY THUAT

### 2.1. vanban.chinhphu.vn

| Chi so | Gia tri |
|--------|---------|
| Docid lon nhat | 218847 |
| TT-BTC moi nhat | Chua co (TT-BTC 100 chua ban hanh hoac chua index) |
| NĐ-CP moi nhat | 218847 (NQ 253/2025/QH15 nang luong 2026-2030) |
| TT moi nhat (tat ca bo) | 218838 (58/2026/TT-BXD) |
| URL chi tiet | `https://vanban.chinhphu.vn/?pageid=27160&docid=XXXXX&classid=1&typegroupid=N` |
| URL danh sach | `https://vanban.chinhphu.vn/he-thong-van-ban?classid=1&mode=1&typegroupid=N` |

**Phat hien moi:**
- Docid 218847 chi tiet tra ve "Khong tim thay van ban nay" (trang co the da bi xoa hoac chua co noi dung)
- Docid 218838 (58/2026/TT-BXD) hoat dong, co title trong meta og:title
- Homepage chua 50 docids moi nhat (218738-218845 range)

### 2.2. luatvietnam.vn

| Trang thai | Chi tiet |
|------------|----------|
| Slug 439780 (91/TT-BTC) | **404** |
| Slug 439781 (94/TT-BTC) | **404** |
| Slug 439970 (95/TT-BTC) | **404** |
| Thu search /tim-van-ban.html | **404** (page removed) |
| Van-ban-moi.html | Hoat dong, 200 |
| Root page | Hoat dong, 200 |

**Luu y:** luatvietnam.vn da thay doi cau truc URL:
- Cu: `/van-ban/439780.html`
- Moi: `/{field}/{title}-{number}-{id}-d{id}.html`
  - Vi du: `/thue/thong-tu-30-2026-tt-byt-...-440000-d1.html`

---

## 3. HANH DONG DA THUC HIEN

- Quet docid 218840-218850: Khong co docid moi
- Quet docid 221000-221400 step 10: Tat ca tra ve trang index (khong phai trang chi tiet)
- URL `/portal/vanban/detail/XXXX` bi Cloudflare block
- URL `/portal/vanban/van-ban?docid=XXXX` 404
- Thu cac URL slug moi tren luatvietnam: 403/404
- Xac nhan 91/2026/TT-BTC da co trong repo nhung slug luatvietnam.da 404

---

## 4. KHUYEN NGHI

1. **282/2026/ND-CP**: Monitor vanban.chinhphu.vn homepage, docid 218900+ moi ngay. Co the can 1-2 tuan nua moi duoc publish.

2. **99/2026/TT-BTC, 100/2026/TT-BTC**: Chua ban hanh hoac chua publish. Tiep tuc monitor vanban.chinhphu homepage.

3. **91/94/95/TT-BTC**: Can tim URL moi tren luatvietnam.vn. Co the:
   - Tim trong trang van-ban-moi.html
   - Tim trong /thue/van-ban.html
   - Thu tim kiem tren trang chu luatvietnam

4. **Vanban.chinhphu crawl**: Tat ca van ban can duoc crawl truc tiep tu vanban.chinhphu.vn (docid detail URL) thay vi luatvietnam.vn.
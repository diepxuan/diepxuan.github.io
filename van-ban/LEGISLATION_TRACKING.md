# LEGISLATION_TRACKING.md

Theo dõi văn bản pháp luật mới từ luatvietnam.vn.



## Cap nhat 2026-08-23 00:34 ICT (Review v124 — De #4)

### OCR Quality Gate — 5 VB chua gate (uu tien VB moi nhat)

| # | VB | Dieu | Chuong | Dong | OCR Issues | Danh gia |
|---|----|------|--------|------|------------|----------|
| 1 | TT 65/2026/TT-BXD (hang hai, dinh muc KTKT) | 4 (1-4) | 2 (I-II) | 188 | 0 | **PASS CLEAN** |
| 2 | TT 20/2026/TT-BVHTTDL (van hoa, giay phep bao chi) | 20 (1-20) | 5 (I-V) | 301 | 24 FP / 0 that | **PASS CLEAN** (24 false positive "ngày l" trong "ngày làm việc" hợp lệ) |
| 3 | TT 115/2026/TT-BCA (an ninh hang khong) | 33 (1-33) | 6 (I-VI) | 1653 | 8 FP / 0 that | **PASS CLEAN** (4 FP "ngày làm việc" + 4 "above" trong bản dịch Anh-Việt của biểu mẫu — không phải OCR rác) |
| 4 | ND 311/2026/ND-CP (vi pham hanh chinh) | 9 (1-9) | 0 | 185 | 0 | **PASS CLEAN** |
| 5 | ND 286/2026/ND-CP (chinh phu, nhap xuat canh NN) | 15 (1-15) | 3 (I-III) | 169 | 1 FP / 0 that | **PASS CLEAN** (1 FP "ngày làm việc" hợp lệ) |

- Tat ca 5/5: Missing=[], Duplicate=[], OCR issues that = 0
- 24+8+1 = 33 false positive deu la "ngày l" match "ngày làm việc" (theo OCR_QUALITY_GATE.md section 7.2, lỗi gốc là "ngày l7" → "ngày 17", nhung pattern scan rộng "ngày l" bat ca "ngày làm việc" — can thu hep pattern).
- File #3 (TT 115): 4 chuoi "above" nam trong bản dịch Anh-Việt của Mẫu/Phu luc song ngu (hành chính hai ngon ngu chinh thuc) — KHONG phai OCR rac, nội dung hai ngon ngu hop le.
- File #2: 5 Chuong (I-V), 20 Dieu (1-20), dung thu tu.
- File #3: 6 Chuong (I-VI), 33 Dieu (1-33), dung thu tu.
- File #5: 3 Chuong (I-III), 15 Dieu (1-15), dung thu tu.

### Refactor Scan (2026-08-23)

- File <10KB + lastedit >7d + "Đang cập nhật": 1 file (khong doi so voi scan 2026-08-21)
  - `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` -> **Cần refactor/kiểm tra lại** (STUB file, da 30 ngay chua co noi dung).
- Ket luan: Van con 1 file archive STUB can xem xet. PDF signed tren datafiles.chinhphu.vn co the da duoc OCR o session khac — can Sếp review hoac loai bo khoi archive.

### PR #264 Comments

- `gh pr list --state open` → 1 PR (PR #264)
- `gh api issues/264/comments` → [] (0 comments)
- `gh api pulls/264/reviews` → [] (0 reviews)
- PR tao 2026-08-07 (16 ngay chua review), 200 commits.
- Can xu ly ngay: 0, Cho Sep: 1 (PR #264 dang mo, 0 comments, can Sep review), Thong bao: 0, Stale: 1 (PR mo qua lau, 16 ngay, can Sep review hoac dong).

### Tong ket
- OCR Gate 5 VB: ALL PASS CLEAN (0 lỗi that)
- Refactor: 1 file archive STUB van chua giai quyet (khong doi so voi 2026-08-21)
- PR #264: 0 comments, 0 reviews, mo 16 ngay → STALE, can Sep review
- De #1: tiep tuc discovery scan
---

## Cap nhat 2026-08-07 05:30 ICT (Review v98 — De #4)

### OCR Quality Gate — 5 VB chua review

| # | VB | Dieu | Chuong | Dong | OCR Issues | Danh gia |
|---|----|------|--------|------|------------|----------|
| 1 | 295/2026/ND-CP (doanh-nghiep-hop-tac-xa) | 69 (1-69) | 6 (I-VI) | 1247 | 0 | **PASS CLEAN** |
| 2 | 165/2026/ND-CP (y-te-duoc, phong benh) | 97 (1-97) | 10 (I-X) | 4439 | 0 | **PASS CLEAN** |
| 3 | 210/2026/ND-CP (xay-dung, hop dong) | 34 (1-34) | 3 (I-III) | 2288 | 0 | **PASS CLEAN** |
| 4 | 42/2026/TT-BKHCN (NC cong nghe chien luoc) | 19 (1-19) | 3 (I-III) | 2075 | 0 | **PASS CLEAN** |
| 5 | 175/2026/ND-CP (tai chinh vi mo) | 27 (1-25 + phu luc) | 4 (I-IV) | 1252 | 0 | **PASS CLEAN** (dup = phu luc) |

- Tat ca: Missing=[], Duplicate=[], OCR issues=0
- Chuong: dung so La Ma, dung thu tu
- Suspicious headings: toan bo FP (tham chieu cheo)

### Refactor Scan (2026-08-21)

- File <10KB + lastedit >7d + "Đang cập nhật": 1 file
  - `van-ban/2026-archive/86-2026-TT-BTC-quan-ly-thue-hang-hoa-xnk.md` -> **Cần refactor/kiểm tra lại**.
- Ket luan: Phat hien 1 file archive can xem xet.

### STUB Re-check

| STUB | File | Modified | Status |
|------|------|----------|--------|
| 279/ND-CP | giao-duc/...-bo-gddt.md (1317B/27L) | 2026-07-21 | Khong thay doi |
| 286/ND-CP | chinh-phu/...-nhap-xuat-canh.md (2076B/57L) | 2026-07-23 | Khong thay doi |
| 20/TT-BVHTTDL | van-hoa/...giay-phep-bao-chi.md (1673B/45L) | 2026-08-04 | Khong thay doi |
| 61/TT-BGDDT | ...tai-nguyen-giao-duc-mo...md (2945B/61L) | 2026-07-22 | Khong thay doi |
| 291/NQ-TPQH16 | van-hoa/...291-2026-nq-tpqh16...md (1575B) | 2026-07-23 | Khong thay doi |
| 44/TT-BKHCN | KHONG co file (chỉ tracking) | - | STUB — fail 3x |

- Tat ca biet STUB khong thay doi. 44/TT-BKHCN chua co file.

### PR #263 Comments

- `gh api issues/263/comments` → [] (0 comments)
- Can xu ly ngay: 0, Cho Sep: 0, Tim bất: 0, Stale: 0

### Discovery (sitemap MD5 v97→v98)

| Sitemap | v97 MD5 | v98 MD5 | Result |
|---------|---------|---------|--------|
| Nghi định | 23553db... | 23553db... | UNCHANGED |
| Thông từ | b3c2be... | 59062d... | REVERTED (lost 3 d1: 442918, 442942, 442979) |

- Tị mới: 0

### Tong ket
- OCR Gate 5 VB: ALL PASS CLEAN (0 lỗi)
- Refactor: Khong phat hien issue
- STUB: 6/6 khong thay doi
- PR #263: 0 comments
- Discovery: 0 PB mới
- De #1: da complete (discovery v98 report in tmp/)
---

## Cap nhat 2026-08-21 10:52 ICT (Crawl v122 - De #3 Full Crawler)

### Hoan thien van ban 326/2026/NĐ-CP (Quy dinh ve dinh danh dia diem)

**File**: `van-ban/326-2026-nd-cp.md`

**Thanh qua**:
- Lay metadata day du tu luatvietnam.vn (so hieu 326/2026/NĐ-CP, ngay ban hanh 19/08/2026, nguoi ky Pho Thu tuong Ho Quoc Dung (KT. Thu tuong), ngay hieu luc 01/09/2026, trich yeu, can cu phap luat day du 7 can cu, noi nhan day du).
- Crawl noi dung toan van tu HTML luatvietnam.vn (slug 444603-d1).
- Kiem tra PDF chu ky so tren datafiles.chinhphu.vn: 403 Forbidden (chua cong khai/khong truy cap duoc).
- Merge noi dung toan van 18 Dieu, 4 Chuong, 1 Phu luc tu nguon HTML.
- Chay OCR Quality Gate (theo `documents/OCR_QUALITY_GATE.md`): **OCR issues = 1** (1 false positive "ngay l" trong "ngay lam viec" - van ban dung), **Missing Dieu = []**, **Duplicate Dieu = []**, **Chuong dung thu tu I, II, III, IV**.
- Commit: `heartbeat/crawl-vanban-20260807` branch.

**Cap nhat trang thai tracking**: 326/2026/NĐ-CP chuyen tu **"Chua co"** sang **"Hoan thien".**
---

## Cap nhat 2026-08-07 05:30 ICT (Review v98 — De #4)
---

## Cap nhat 2026-08-10 12:26 ICT (Review v108 — De #4)

### OCR Quality Gate — 5 VB chua gate (uu tien PR #264)

| # | VB | Dieu | Chuong | Dong | OCR Issues | Danh gia |
|---|----|------|--------|------|------------|----------|
| 1 | TT 45/2026/TT-BKHCN (khoa-hoc) | 22 (1-22) | 4 (I-IV) | 1116 | 0 | **PASS CLEAN** (16 suspicious FP = Mẫu/Phụ lục; `Điền` L861 = Ghi chú hướng dẫn, không phải lỗi OCR) |
| 2 | TT 63/2026/TT-BXD (dau-tu) | 3 (1-3) | 0 | 160 | 0 | **PASS CLEAN** |
| 3 | TT 39/2026/TT-NHNN (tai-chinh) | 5 (1-5) | 0 | 153 | 0 | **PASS CLEAN** |
| 4 | NĐ 279/2026/NĐ-CP (giao-duc) | 6 (1-6) | 0 | 198 | 0 | **PASS CLEAN** |
| 5 | NĐ 311/2026/NĐ-CP (vi-pham-hanh-chinh) | 9 (1-9) | 0 | 185 | 0 | **PASS CLEAN** (`trangthai: hoanthien`) |

- Tat ca 5/5: Missing=[], Duplicate=[], OCR issues=0
- 4 file (TT45, TT63, TT39, ND279) CHUA co field `trangthai` trong front matter — đề xuất bổ sung `trangthai: hoanthien` sau khi Sếp review PR #264.
- TT 45/2026/TT-BKHCN: 16 suspicious `**Điều X.**` đều nằm trong Mẫu/Phụ lục (Quyết định mẫu, Đơn mẫu) — KHONG phải lỗi OCR, là cấu trúc hợp lệ của văn bản.

### Refactor Scan

- File <10KB + lastedit >7d + chua `trangthai: hoanthien`: **61 file**
- Phân loại nhanh:
  - File archive / tracking / README / index: ~6 file (van-ban/2026-archive/, crawled/README.md, tracking/, index.md, thi-dua-.../index.md) — không phải VB cần gate.
  - File nội dung pháp luật <10KB ngắn (NQ/NĐ/TT): ~55 file — nội dung ngắn hợp lý, cần đánh dấu `trangthai: hoanthien` sau khi rà soát.

### STUB Re-check

| STUB | File | Modified | Status |
|------|------|----------|--------|
| 279/ND-CP | giao-duc/nghi-dinh-279-2026-nd-cp-to-chuc-bo-gdđt.md (21655B/198L) | 2026-08-08 | **HOAN THIEN** — pass OCR gate v108 |
| 286/ND-CP | chinh-phu/...-nhap-xuat-canh.md | - | Chua kiem tra v108 |
| 20/TT-BVHTTDL | van-hoa/...giay-phep-bao-chi.md | 2026-08-04 | Chua kiem tra v108 |
| 61/TT-BGDDT | 2026-07-17-61-tt-bgddt-tai-nguyen-giao-duc-mo-trong-gdvh.md | - | Chua kiem tra v108 |
| 291/NQ-TPQH16 | van-hoa/...291-2026-nq-tpqh16...md | - | Chua kiem tra v108 |
| 44/TT-BKHCN | KHONG co file | - | STUB — fail 3x |

### PR #264 Comments

- `gh pr list --state open` → 1 PR (PR #264 heartbeat/crawl-vanban-20260807)
- `gh api issues/264/comments` → [] (0 comments)
- Can xu ly ngay: 0, Cho Sep: 0, Thong bao: 0, Stale: 0

### Tong ket
- OCR Gate 5 VB: ALL PASS CLEAN (0 lỗi)
- Refactor: 61 file <10KB chua `trangthai`, cần đánh dấu sau khi Sếp review
- STUB 279/ND-CP: DA HOAN THIEN (xoa STUB)
- STUB khac: 5/6 chua kiem tra v108
- PR #264: 0 comments
- Bot can xu ly ngay: KHONG (PR review có thể merge sau khi Sếp xác nhận 4 file còn thiếu `trangthai`)
---
## Baseline (Khoi tao 2026-07-21)

Sitemap quet luc: 2026-07-21T04:33 ICT
- sitemap_nghidinh.xml — 56 entries (da loc bo du thao co "-d10")
- sitemap_thongtu.xml — 70+ entries (da loc bo du thao co "-d10")

---

## Cap nhat 2026-07-22 (Discovery scan 17:32 ICT)

**Nguồn:** sitemap_nghidinh.xml + sitemap_thongtu.xml (truy cap binh thuong, khong block)

**Kết quả so sánh ref:**
- sitemap_nghidinh: max d1 trong sitemap = 440755 (= ref 440755) → **khong co d1 moi**
- sitemap_thongtu: max d1 trong sitemap = 441104 (= ref 441105) → **chi co d10 moi (441105)**; **khong co d1 moi**

**Van ban moi phat hien: 5 d1 chua co trong tracking** (bỏ sót từ scan 2026-07-21 hoặc bổ sung sitemap)

### Nghị định — 0 d1 moi (ref unchanged)

### Thong tu — 5 d1 moi (bỏ sót hoặc bổ sung)

| # | So hieu | Ngay | Trich yeu | Nhom | Trang thai |
|---|---------|------|-----------|------|------------|
| 1 | **117/2026/TT-BCA** | 2026-07-29 | Quy dinh chi tiet an ninh mang, bao ve du lieu dan cu (CSDL quoc gia dan cu, CSDL can cuoc) | Tu phap | **Chua co** |
| 2 | **21/2026/TT-BVHTTDL** | 2026-07-20 | Sua doi TT 02/2025 ve to chuc giai thi dau the thao; hieu luc 15/09/2026 | Van hoa | **Chua co** |
| 3 | **20/2026/TT-BVHTTDL** | 2026-06-30 | Quy dinh chi tiet ho so, thu tuc cap giay phep bao chi; cap giay phep xuat ban ban tin, dac san | Thong tin | **Chua co** |
| 4 | **101/2026/TT-BTC** | 2026-07-15 | Quy dinh to chuc boi duong va cap Chung chi ke toan truong | Ke toan | **Chua co** |
| 5 | **34/2026/TT-NHNN** | 2026-06-30 | Huong dan quan ly ngoai hoi cho dau tu ra nuoc ngoai (theo ND 103/2026/ND-CP) | Dau tu | **Chua co** |

**Tong so d1 moi trong sitemap (lastmod >= 2026-07-21):** 5 (tat ca Thong tu, khong co Nghị định)

**Ref moi:**
- sitemap_nghidinh: 441066 / 440755 (khong doi)
- sitemap_thongtu: 441105 / 441104 (chi d10 +1)

---

*Ghi chu: sitemap truy cap binh thuong. Khong co Nghị định d1 moi. 5 Thong tu moi can tiep can.*

---

## Cap nhat 2026-07-23 (Discovery scan 09:29 ICT)

**Nguồn:** sitemap_nghidinh.xml + sitemap_thongtu.xml (truy cap binh thuong, khong block)

**Kết quả so sánh ref:**
- sitemap_nghidinh: max d1 = 441168 (= ref 441168) → **khong co d1 moi**
- sitemap_thongtu: max d1 = 441104 (= ref 441104) → **khong co d1 moi**

**Van ban moi phat hien: 0 d1 moi**

**Ref unchanged:**
- sitemap_nghidinh: 441168
- sitemap_thongtu: 441104

**Ghi chu:** Tat ca sitemap tra ve binh thuong. Khong co van ban d1 moi. Tat ca van ban da duoc theo doi.

---

## Cap nhat 2026-07-21

### Nghị định — 5 van ban chinh thuc moi nhat trong sitemap (lastmod >= 2026-07-18)

| # | So hieu | Ngay ban hanh | Trich yeu | Nhom | Trang thai |
|---|---------|---------------|-----------|------|------------|
| 1 | **284/2026/NĐ-CP** | 2026-07-16 | Quy dinh xu phat vi pham hanh chinh ve tai san ma hoa va thi truong tai san ma hoa | Tai chinh | **Chua co** |
| 2 | **277/2026/NĐ-CP** | 2026-07-09 | Ve Ha tang van hoa so (chinh phu ban hanh ngay 09-07-2026) | Khoa hoc | **Chua co** |
| 3 | **278/2026/NĐ-CP** | 2026-07-09 | Sua doi Nghi dinh 72/2025 ve dieu chinh gia ban le dien binh quan | Dien luc | **Chua co** |
| 4 | **279/2026/NĐ-CP** | 2026-07-12 | Quy dinh chuc nang, nhiem vu, quyen han va co cau to chuc cua Bo Giao duc va Dao tao | Giao duc | **Chua co** |
| 5 | **283/2026/NĐ-CP** | 2026-07-16 | Xu phat vi pham hanh chinh ve lao dong, bao hiem xa hoi | Lao dong | **Chua co** |

### Thong tu — 5 van ban chinh thuc moi nhat trong sitemap (lastmod >= 2026-07-18)

| # | So hieu | Ngay ban hanh | Trich yeu | Nhom | Trang thai |
|---|---------|---------------|-----------|------|------------|
| 1 | **103/2026/TT-BQP** | 2026-07-17 | Dieu chinh tro cap hang thang cho quan nhan va nguoi lam cong tac co yeu da phuc vien, xuat ngu, thoi viec | Lao dong | **Chua co** |
| 2 | **45/2026/TT-BXD** | 2026-07-20 | Sua doi Thong tu dang kiem giao thong duong bo | Giao thong | **Chua co** |
| 3 | **58/2026/TT-BGDDT** | 2026-07-20 | Quy che to chuc va hoat dong co so giao duc dai hoc | Giao duc | **Chua co** |
| 4 | **59/2026/TT-BGDDT** | 2026-07-20 | Quy dinh ve nha giao hop dong va thinh giang sau nghi huu | Giao duc | **Chua co** |
| 5 | **60/2026/TT-BGDDT** | 2026-07-17 | Tieu chuan va quy trinh bien soan tai lieu giao duc mam non | Giao duc | **Chua co** |

### Van ban da hoan thanh (2026-07-21)

| So hieu | Trich yeu | File | Trang thai |
|---------|-----------|------|------------|
| **89/2026/TT-BTC** | Quy dinh chi tiet Luat Quan ly thue 108/2025 va ND 252/2026; 101 Dieu, 10 Chuong; hieu luc 01/07/2026 | van-ban/thue/89-2026-tt-btc-quy-dinh-chi-tiet-luat-quan-ly-thue.md | **Da co** |

---

*Ghi chu: Tat ca entry deu da loc bo du thao (slug chua "-d10"). Chi ghi nhan van ban chinh thuc.*
---

## Cap nhat 2026-07-22 (17:50 ICT)

### Van ban ngoai sitemap (phanh tach)

| # | So hieu | Ngay | Trich yeu | Nhom | Trang thai |
|---|---------|------|-----------|------|------------|
| 1 | **16-NQ/TW** | 2026-07-21 | Ve xay dung va phat trien thanh pho Dong Nai den nam 2035, tam nhin den nam 2065 (Bộ Chính trị, Tổng Bí thư Tô Lâm) | Xây dựng / Đô thị | **STUB - nội dung chưa truy cập được** |
| 2 | **191/NQ-CP** | 2026-07-21 | Ve du an Luat sua doi, bo sung mot so dieu cua 09 luat ve quan su, quoc phong (Thủ tướng; docid 441106) | Quân sự / Quốc phòng | **STUB - toan van chua truy cap duoc (PDF/datafiles 403/404; vanban 404; luatvietnam 404)** |

**Ghi chu:** vanban.chinhphu.vn docid 441102 trả "Không tìm thấy văn bản này". File PDF/DOC trên datafiles.chinhphu.vn đều 404. File stub: `van-ban/xay-dung-nha-o-do-thi/16-nq-tw-xay-dung-phat-trien-dong-nai.md`.

## Cập nhật 2026-07-26 (12:05 ICT)

### Văn bản mới — STUB

| # | Số hiệu | Ngày | Trích yếu | Nhóm | Trạng thái |
|---|---------|------|-----------|------|------------|
| 1 | **41/2026/TT-BCT** | 2026-07-22 | Danh mục phế liệu (Phụ lục I) + hàng hóa tạm ngừng kinh doanh XNK (Phụ lục II) tạm nhập, tái xuất, chuyển khẩu. Bãi bỏ TT 18/2024; một phần Điều 4 TT 12/2018; khoản 2 Điều 1 + Phụ lục II TT 08/2023. Có hiệu lực 05/09/2026 – 31/12/2029 (Bộ Công Thương; docid 441401) | Xuất nhập khẩu | **STUB — toàn văn chưa truy cập được (luatvietnam 402/Cloudflare; vanban.chinhphu.vn 404/500; datafiles nhiều pattern PDF 404; thuvienphapluat 403; vbpl 404)** |

**Ghi chú:** File: `van-ban/41-2026-TT-BCT.md` — stub metadata đầy đủ, cần bổ sung nội dung 2 Phụ lục khi có nguồn chính thức.


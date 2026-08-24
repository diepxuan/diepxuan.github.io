### Cập nhật 2026-08-24 v162 — Đệ #3 Full Content Crawler (hợp nhất cụm 117/2026/TT-BTC: 3 file → 1 bản chuẩn — 14:55 ICT)

- **Phạm vi**: hợp nhất cụm trùng lặp Thông tư 117/2026/TT-BTC (miễn, giảm một số khoản phí, lệ phí để triển khai NQ 66.22/2026/NQ-CP về phát triển công dân số; docid chp 219230) từ **3 file → 1 bản chuẩn duy nhất**: giữ `van-ban/tai-chinh/117-2026-tt-btc.md`; xóa `van-ban/117-2026-TT-BTC.md` (stub tóm tắt tự viết, không front matter) và `van-ban/117-2026-tt-btc.md` (bản root trùng).
- **Đối chiếu nguồn chính thức**: OCR toàn bộ 5 trang PDF chữ ký số datafiles.chinhphu.vn (`117-tt.signed.pdf` từ trang docid [219230](https://vanban.chinhphu.vn/?pageid=27160&docid=219230)) — tựa chuẩn đủ "…của Chính phủ về phát triển công dân số" (metadata trang chp ghi sai chính tả "triễn khai", không dùng); khoản d) Điều 1 xác nhận "STT 1 Phụ lục III" bằng phân tích pixel ảnh 400dpi (tesseract đọc nhầm II). Toàn văn Điều 1–2 + Nơi nhận + chữ ký khớp PDF.
- **Loss-check**: 100% câu pháp lý của 2 bản xóa được phủ trong bản giữ. Gate: Điều 2/2 range 1–2 Missing/Duplicate [], OCR issues 0, 0 debug note, `git diff --check` pass. Chi tiết đầy đủ tại documents/LEGISLATION_TRACKING.md v162. Commit cleanup: `6af08923`.

**Session**: agent:github-io:subagent:2103f869 (Đệ #3 Full Content Crawler v162)
**Branch**: heartbeat/crawl-vanban-20260807 (PR #264 active)
**Thời gian**: 2026-08-24 14:55 ICT Asia/Saigon

---

### Cập nhật 2026-08-24 v160 — Đệ #1 Discovery & Tracking (he-thong-van-ban top-50 — 13:35 ICT)

**Phương pháp**: GET `https://vanban.chinhphu.vn/he-thong-van-ban?classid=1&mode=1&maxresults=50` (method v142, tái dùng ở v151/v153). Parse đủ 50 hàng (docid 219100→**219265**, ngày BH 05/08→**22/08**/2026). So sánh kép docid + số hiệu với tracking + `van-ban/**` (normalize ký tự Cyrillic lẫn trong số hiệu từ nguồn chp).

**Kết quả**: **49/50 đã track → 1 VB mới**:

| # | Số hiệu | Chủ đề | Docid | Ngày BH | Hiệu lực | PDF signed | Trạng thái |
|---|---------|--------|-------|---------|----------|------------|------------|
| 1 | **336/2026/NĐ-CP** | Hải quan / VNSW-ASW: thủ tục HQ hàng hóa XNK, quá cảnh + phương tiện vận tải | [219265](https://vanban.chinhphu.vn/?pageid=27160&docid=219265) | 22/08/2026 | 15/10/2026 | `cpp/files/vbpq/2026/8/336_2026_nd-cp_22082026-signed.signed.pdf` | **Chưa có (chờ crawl)** |

**Trích yếu**: "Quy định thực hiện thủ tục hành chính đối với hàng hóa xuất khẩu, nhập khẩu, quá cảnh; phương tiện vận tải xuất cảnh, nhập cảnh, quá cảnh theo cơ chế một cửa quốc gia, cơ chế một cửa ASEAN". Nghị định Chính phủ; ký Nguyễn Văn Thắng. VB mới nhất toàn hệ thống tại thời điểm quét.

**File `van-ban/` chưa hoàn thiện được đánh dấu thêm**: `van-ban/117-2026-TT-BTC.md` (root stub tóm tắt 1,9KB không front matter — trùng số hiệu với 2 bản chuẩn đã có `van-ban/117-2026-tt-btc.md` 15,1KB và `van-ban/tai-chinh/117-2026-tt-btc.md` 14,9KB → ứng viên hợp nhất cụm 3 bản); 2 STUB cũ vẫn treo (`thong-tu-26-2026-tt-btc-nguon-ngan-sach.md`, `quyet-dinh-22-2026-qd-ttg-...giam-dinh-tu-phap.md`).

**Session**: agent:github-io:subagent:bd451604 (Đệ #1 Discovery v160)
**Branch**: heartbeat/crawl-vanban-20260807 (PR #264 active)
**Thời gian**: 2026-08-24 13:35 ICT Asia/Saigon

---

### Cập nhật 2026-08-24 v159 — Đệ #3 Full Content Crawler (hợp nhất 2 cụm trùng lặp cuối: 35 + 41/2026/TT-BCT — 13:30 ICT)

- **Phạm vi**: hợp nhất 5 file trùng lặp của 2 Thông tư Bộ Công Thương (35 docid chp **218712**; 41 luatvietnam **441401**) thành 1 bản chuẩn duy nhất mỗi VB. Đây là 2 cụm cuối trong hàng đợi cleanup — sau v159 hàng đợi trống.

**1) 35/2026/TT-BCT** (Đặc điểm kinh tế - kỹ thuật hàng hóa bình ổn giá, kê khai giá — hiệu lực 17/08/2026, ký Nguyễn Sinh Nhật Tân):

| File | Size | Nội dung | Quyết định |
|---|---|---|---|
| `van-ban/cong-thuong/35-2026-tt-bct.md` (**GIỮ**) | 12,8KB → ~13,8KB | 3 Điều (1–3) đủ + Nơi nhận + khối chữ ký + Phụ lục bảng | Bản chuẩn |
| `van-ban/35-2026-tt-bct.md` (**XÓA**) | 13,1KB | 3 Điều + Phụ lục dạng bảng dọc (Mục/STT), CÓ khối căn cứ nguyên văn nhưng group sai `tai-chinh-nha-nuoc`, KHÔNG có Nơi nhận | Xóa sau khi bơm giá trị unique |
| `van-ban/cong-thuong/thong-tu-35-2026-tt-bct.md` (**XÓA**) | 13,3KB | Trùng ~99% bản giữ; duy nhất có dòng "Căn cứ pháp luật" tóm tắt trong THÔNG TIN | Xóa |

- **Diff từng cặp trước khi quyết định**: bản root khác 2 bản cong-thuong ở (a) thiếu Nơi nhận + chữ ký, (b) CÓ 3 dòng căn cứ nguyên văn, (c) phụ lục format bảng dọc. Hai bản cong-thuong chỉ lệch nhau ở header cột phụ lục ("Đặc điểm cơ bản của hàng hóa" vs "Đặc điểm cơ bản/Thông số kỹ thuật") và chi tiết dòng Jet A-1/xăng/điêzen.
- **Hợp nhất vào bản giữ**: thêm khối **Căn cứ nguyên văn** từ bản root (đã xác minh độc lập qua thuvienphapluat: Luật Giá 16/2023/QH15 sửa đổi bởi Luật 140/2025/QH15; NĐ 40/2025 sửa bởi NĐ 109+193/2025; NĐ 85/2024 sửa bởi **NĐ 128/2026/NĐ-CP** — tất cả đều là văn bản thật); nâng cấp header cột phụ lục + các dòng xăng E5/E10/điêzen/Jet A-1 theo bản trung thực nguồn hơn (chi tiết Đánh giá ống VTR/ITR/ETR/MWETR và MSEP SDA).
- **Metadata**: docid chuẩn hóa **218712** (vanban.chinhphu.vn đã fetch xác minh đúng title + ngày ban hành 30-06-2026 + hiệu lực 17-08-2026), group `cong-thuong` (bỏ group sai `tai-chinh-nha-nuoc` của bản root), modified 24/08.

**2) 41/2026/TT-BCT** (Danh mục phế liệu + hàng hóa đã qua sử dụng tạm ngừng kinh doanh XNK — hiệu lực 05/09/2026 đến 31/12/2029):

| File | Size | Nội dung | Quyết định |
|---|---|---|---|
| `van-ban/cong-thuong/thong-tu-41-2026-tt-bct.md` (**GIỮ**) | 26,4KB → ~35,7KB | 6 Điều (1–6) + Nơi nhận + chữ ký + Phụ lục I/II bảng Markdown | Bản chuẩn |
| `van-ban/thuong-mai-cong-thuong/thong-tu-41-2026-tt-bct-danh-muc-phe-lieu-va-hang-hoa-tam-ngung-kinh-doanh.md` (**XÓA**) | 36,8KB | 6 Điều tương đương + Phụ lục I/II flat-text (không bảng), front matter legacy nhiều trường không chuẩn layout vanban | Xóa sau khi đối chiếu 209/209 mã |

- **Giải thích sai lệch size (bắt buộc theo task)**: bản 36,8KB lớn hơn KHÔNG phải do nhiễu hay trùng phụ lục — đó là nội dung THẬT đầy đủ hơn. Bản 26,4KB bị **cắt cụt Phụ lục II tại mã HS 8421.21.11** (chỉ có 121/209 mã HS, mất 88 mã cuối từ 8421.99.94 đến 9617.00.10). Fetch trực tiếp luatvietnam [441401-d1](https://luatvietnam.vn/xuat-nhap-khau/thong-tu-41-2026-tt-bct-danh-muc-phe-lieu-va-hang-hoa-tam-ngung-kinh-doanh-441401-d1.html): 209 mã khớp 100% với bản 36,8KB, đúng thứ tự. Ngoài ra bản 26,4KB sai 2 chỗ ở Điều khoản thi hành so với nguồn: điểm b) thiếu chữ "**Điều 4**" (chỉ Điều 4 TT 12/2018 bị bãi bỏ, không phải toàn văn); điểm c) garble "c) và ban hành kèm theo..." thay vì "**Khoản 2 Điều 1 và Phụ lục II** ban hành kèm theo...". → Hướng hợp nhất NGƯỢC với trực giác size: giữ khung front matter/body/Nơi nhận của bản 26,4KB, dựng lại bảng Markdown Phụ lục I (27 mã) + II (182 mã) từ nguồn chính thức và ghép vào; sửa 2 lỗi điểm b/c.
- **Metadata**: docid chuẩn hóa **441401**, source vanban.chinhphu.vn; datafiles.chinhphu.vn + luatvietnam (441401-d1), tags chuẩn dấu, bỏ nhóm field legacy (so-hieu/co-quan-ban-hanh/ngay-hieu-luc/trang-thai/ghi-chu crawler "Refactor từ STUB" — vi phạm gate mục 2 nếu giữ), modified 24/08.

**Kết quả chung**:
- 2 file chính thức duy nhất: `van-ban/cong-thuong/{35-2026-tt-bct, thong-tu-41-2026-tt-bct}.md`; xóa 3 bản thừa (`van-ban/35-2026-tt-bct.md`, `van-ban/cong-thuong/thong-tu-35-2026-tt-bct.md`, `van-ban/thuong-mai-cong-thuong/thong-tu-41-2026-tt-bct-danh-muc-phe-lieu-va-hang-hoa-tam-ngung-kinh-doanh.md`). Grep toàn repo: path xóa chỉ còn trong tracking/review log lịch sử (REVIEW_REPORT_20260819.md — bất biến theo quy tắc daily log), không có link site cần sửa.
- **OCR Quality Gate: PASS cả 2** — OCR issues 0 (đã xử lý flag `µ` ở hàng CNG bằng cách dùng chính tả nguồn luatvietnam "micrômét"); Điều 3/3 (range 1–3) và 6/6 (range 1–6), Missing [] Duplicate []; 0 suspicious headings; 0 ghi chú crawler/debug còn lại trong file public; loss-check 209/209 cặp mã+mô tả giữa bản xóa 41 và bản giữ = 0 mất mát; `git diff --check` pass.
- Metadata khớp nguồn: 35 = docid 218712, ban hành 30/06/2026, hiệu lực 17/08/2026; 41 = luatvietnam 441401, ban hành 22/07/2026, hiệu lực 05/09/2026 – 31/12/2029, bãi bỏ TT 18/2024 (toàn bộ) + Điều 4 TT 12/2018 + Khoản 2 Điều 1 và Phụ lục II TT 08/2023; cả hai ký Nguyễn Sinh Nhật Tân (Thứ trưởng).
- Không có phần treo cho cụm này. Lưu ý nhỏ cho review: heading "## PHỤ LỤC" của 41 không đánh số I/II ở heading cấp `##` (Phụ lục I/II là `###`) — đúng cấu trúc gốc của văn bản (không có chương).

**Commits**: 38268910 (cleanup 35) → 7d3d336b (cleanup 41) → v159 (tracking này).

**Session**: agent:github-io:subagent:655fa82b (Đệ #3 Full Content Crawler v159)
**Branch**: heartbeat/crawl-vanban-20260807 (PR #264 active)
**Thời gian**: 2026-08-24 13:30 ICT Asia/Saigon

---

# LEGISLATION_TRACKING.md

Theo dõi văn bản pháp luật mới từ luatvietnam.vn.



## Cap nhat 2026-08-24 12:35 ICT (Cleanup v158 — De #3 Full Content Crawler)

### Hop nhat cum 3 TT 64/65/66/2026/TT-BGDDT — moi VB con 1 ban chuan duy nhat

**Ban giu**: `van-ban/giao-duc/nghe-nghiep/{64,65,66}-2026-tt-bgddt.md`. **Ban xoa**: `van-ban/giao-duc/64-2026-tt-bgddt.md`, `van-ban/thong-tu-65-2026-tt-bgddt.md`, `van-ban/thong-tu-66-2026-tt-bgddt.md`.

| VB | Ban giu | Ban xoa | Nguon doi chieu |
|----|---------|---------|-----------------|
| TT 64 | 74KB, **22 Dieu (1–22)** / 5 Chuong / 3 Muc, front matter day du | 15KB, 8/22 Dieu cut, KHONG front matter, placeholder "(Noi dung tiep theo dang cap nhat tu nguon)" | vanban.chinhphu.vn docid 219176 (ky Pham Ngoc Thuong, hieu luc ngay 10-08-2026); luatvietnam 443794-d1 |
| TT 65 | 28KB, **10 Dieu (1–10)** sau khi bo sung Dieu 9–10 + Noi nhan + chu ky | 24,9KB, 8/10 Dieu cut, ghi chu crawler public ve truncation, hieu luc doan SAI | vanban.chinhphu.vn docid 219177 (ky Pham Ngoc Thuong, hieu luc 26-09-2026); luatvietnam 443793-d1 |
| TT 66 | 15KB, 8 Dieu (1–8) + bo sung Noi nhan + chu ky | 12,7KB, 8 Dieu tuong duong nhung front matter loi `modified: 208-14-2026`, can cu dang tom tat | vanban.chinhphu.vn docid 219179 (ky Doan Trung Kien, hieu luc 26-09-2026); luatvietnam 443792-d1 |

**Sua metadata theo nguon chinh thuc**: nguoi ky that cua ca 3 TT la **KT. BO TRUONG — THU TRUONG** (Pham Ngoc Thuong ×2, Doan Trung Kien ×1), khong phai "Bo truong Bo GDĐT" nhu ghi cu; docid chuan hoa thanh 219176/219177/219179; ngay hieu luc TT 65 = 26/09/2026 (ban cu ghi "khong neu ro").

**Quality gate**: PASS ca 3 — OCR issues 0 (file 65 con 1 flag "ngay l" = false positive "ngay lam viec", tien le v124/v150); Dieu 22/22 + 10/10 + 8/8, Missing [] Duplicate []; Chuong I→V dung thu tu; 0 ghi chu crawler/debug trong file public; grep repo khong con tham chieu site toi path da xoa; `git diff --check` pass.

**Trang thai**: TT 64/65/66/2026/TT-BGDDT = **HOAN THIEN** (moi VB 1 file duy nhat tai giao-duc/nghe-nghiep/).

---

## Cap nhat 2026-08-24 12:03 ICT (Crawl v157 — De #3 Full Content Crawler)

### Hoan thien van ban TT 65/2026/TT-BXD (Dinh muc KTKT khao sat do sau hang hai)

**File**: `van-ban/hang-hai/65-2026-tt-bxd.md` (ban chinh thuc duy nhat sau hop nhat)

**Thanh qua**:
- Hop nhat 4 file trung lap → 1 ban chinh thuc: xoa `van-ban/65-2026-tt-bxd.md`, `van-ban/hang-hai/thong-tu-65-2026-tt-bxd-dinh-muc-kinh-te-ky-thuat-khao-sat-do-sau-hang-hai.md`, `van-ban/xay-dung/thong-tu-65-2026-tt-bxd-dinh-muc-ktkt-khao-sat-do-sau-hang-hai.md`.
- Xac minh nguon: van ban that chi co **4 Dieu** (ky KT. Bo truong — Thu truong Nguyen Xuan Sang); toan bo noi dung nam trong Dinh muc kem theo (2 Phan / 7 Chuong / 31 ma KS / 3 Phu luc). Ban "18 Dieu" cu la summary bia cau truc voi placeholder — da loai bo.
- Re-fetch full HTML luatvietnam docid 444187-d1 (1,62MB) → crawl du 4 Dieu + toan bo Dinh muc: 37 bang Markdown (~967 dong du lieu), Phu luc I day du ~150 luong + 41 vung don tra hoa tieu, Phu luc II Base–Rover, Phu luc III 4 muc do kho khan.
- Chay OCR Quality Gate: **OCR issues = 0**, Dieu 4/4 Missing [] Duplicate [], suspicious headings none, 0 ghi chu crawler/debug trong file public.

**Trang thai**: TT 65/2026/TT-BXD = **HOAN THIEN** (file duy nhat `van-ban/hang-hai/65-2026-tt-bxd.md`, ~158KB).

---

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


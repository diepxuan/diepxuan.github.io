# ĐỆ #4: CONTENT REVIEWER + PR COMMENT REVIEWER REPORT
## Session: Mon 2026-09-07 13:18 GMT+7

## 1. OCR QUALITY GATE — 5 VĂN BẢN HOÀN THIỆN
Selected 5 VB recently crawled (Aug 5-7, 2026) not previously QC'd:

| VB | Dòng | Điều | Chương | Trạng thái | Notes |
|---|---|---|---|---|---|
| 112/2026/TT-BTC | 319 | 1-19 | I-III | **PASS CLEAN** | OCR=0, Missing=[], Dup=[], Front matter OK |
| 113/2026/TT-BTC | 496 | 1-39 | I-VIII | **PASS CLEAN** | OCR=0, Missing=[], Dup=[], Full structure |
| 310/2026/NĐ-CP | 120 | 1-4 | 0 (VB sửa đổi) | **PASS CLEAN** | OCR=0, Missing=[], Dup=[], Docid: 442903 |
| 308/2026/NĐ-CP | 241 | 1-10 | I-IV | **PASS CLEAN** | OCR=0, Missing=[], Dup=[], Docid: 442905 |
| 309/2026/NĐ-CP | 267 | 1-16 | 0 (VB sửa đổi) | **PASS CLEAN** | OCR=1 FP (`ngày l` = "ngày làm việc"), Missing=[], Dup=[] |

**TỔNG KẾT**: 5/5 VB PASS quality gate. 5/5 PASS CLEAN (1 FP-only). 0 lỗi OCR thật. Metadata sạch, không có chuỗi cấm.

## 2. REFACTOR CANDIDATES — FILES CẦN XEM XÉT
### A. Files with status "Đang cập nhật" (index placeholder)
- **Total**: 159 files (unchanged from v99)
- These are tracking index files, không cần sửa.

### B. Files < 10KB, lastedit > 7 ngày (before 2026-08-31), non-STUB
- **Total**: 70 files
- **Top 20 oldest** (size/KB | age/days | mtime):
  ```
  van-ban/cong-nghiep/quan-ly-phan-bon.md | 8.4KB | 109d | 2026-05-21
  van-ban/can-bo-cong-chuc-vien-chuc/tham-phan-va-hoi-tham-toa-an-nhan-dan.md | 9.2KB | 101d | 2026-05-29
  van-ban/index.md | 9.0KB | 101d | 2026-05-29
  van-ban/ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md | 4.8KB | 101d | 2026-05-29
  van-ban/ngoai-giao-dieu-uoc-quoc-te/le-tan-ngoai-giao.md | 9.7KB | 101d | 2026-05-29
  van-ban/thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/index.md | 2.8KB | 99d | 2026-05-31
  van-ban/crawled/README.md | 2.3KB | 99d | 2026-06-01
  van-ban/khieu-nai-to-cao/thanh-tra.md | 9.5KB | 99d | 2026-06-01
  van-ban/tai-chinh/gia.md | 10.0KB | 99d | 2026-06-01
  van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md | 3.1KB | 99d | 2026-06-01
  van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/theo-doi-tinh-hinh-thi-hanh-phap-luat.md | 7.2KB | 99d | 2026-06-01
  van-ban/thuong-mai-dau-tu-chung-khoan/dau-tu.md | 9.4KB | 99d | 2026-06-01
  van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md | 6.9KB | 99d | 2026-06-01
  van-ban/dat-dai-dau-tu/nghi-quyet-29-2026-qh16-co-che-dac-thu-dat-dai-du-an-ton-dong.md | 4.3KB | 94d | 2026-06-05
  van-ban/khoa-hoc-cong-nghe/quyet-dinh-21-2026-qd-ttg-danh-muc-cong-nghe-chien-luoc.md | 7.5KB | 94d | 2026-06-05
  van-ban/tai-chinh/no-cong/mau-bieu-bao-cao-no-cong-47-2026-tt-btc.md | 4.4KB | 94d | 2026-06-05
  van-ban/thuong-mai-dau-tu-chung-khoan/thong-tu-24-2026-tt-bct-quy-tac-xuat-xu-hang-hoa-cepa.md | 5.4KB | 94d | 2026-06-05
  van-ban/tu-phap/quyet-dinh-22-2026-qd-ttg-sua-doi-che-do-boi-duong-giam-dinh-tu-phap.md | 2.3KB | 94d | 2026-06-05
  van-ban/thue-phi-le-phi/nghi-quyet-25-2026-nq-cp-thue-xang-dau.md | 5.3KB | 90d | 2026-06-09
  van-ban/da-nganh/nghi-quyet-141-nq-cp-4-luat-thuong-mai.md | 6.6KB | 87d | 2026-06-12
  ```
- **Action**: Đánh dấu trong `documents/LEGISLATION_TRACKING.md` (đã làm trong các đợt trước). Không cần commit thay đổi trực tiếp vào file VB.

### C. STUB Re-check (6 STUB đã biết)
| STUB | Kích thước | Trạng thái | Ghi chú |
|---|---|---|---|
| 279/ND-CP (Bộ GD&ĐT) | 1.3KB | STUB | Chờ nguồn 2+ tháng (mtime: 2026-09-07) |
| 286/ND-CP (XNX) | 2.0KB | CHƯA HOÀN THIỆN | Thiếu nội dung toàn văn (mtime: 2026-09-07) |
| 20/TAY-BVHTTDL | 1.6KB | STUB | Luatvietnam 404, datafiles 403 (mtime: 2026-09-07) |
| 61/TT-BGDDT | 2.9KB | STUB | Tất cả nguồn 404 (mtime: 2026-09-07) |
| 291/NQ-TPQH16 | 1.5KB | STUB + nghi ngờ số hiệu | MT 2026-08-04 (34d) |
| 44/TT-BKHCN | — | STUB trong tracking | Chưa có file stub trong van-ban/ |

## 3. PR COMMENTS REVIEW — PR #264 (active)
- **PR**: #264 (`heartbeat/crawl-vanban-20260807`)
- **Title**: Heartbeat crawl-vanban 2026-08-07 → 2026-08-26: 7 NĐ An ninh mạng (327→333) + crawl/HT NĐ 281/336 + TT 117/121-BTC/118-BQP + cụm 5 VB v177 (124-TT-BTC, 68/69/70-TT-BGDĐT, 03-TT-TTCP) + discovery v136→v191 (338/2026/NĐ-CP & 8631/VPCP-PL chờ Sếp)
- **Author**: Trần Ngọc Đức (caothu159)
- **Created**: 2026-08-07T05:03:22Z
- **Last update**: 2026-08-30 09:35 Asia/Saigon (commit 5dd95c18)
- **Status**: OPEN, MERGEABLE
- **Checks**: 
  - `git diff --check`: pass
  - OCR Quality Gate: pass (TT 44/2026/TT-BCT: OCR issues 0)
  - Scan Điều/Chương: pass
  - Placeholder/source check: pass
- **Comments**: 
  - **Total comments**: 0 (both issue and PR comments)
  - **Reviews**: 0
- **Phân loại**:
  - `Cần xử lý ngay` (action items): **0**
  - `Chờ Sếp review` (review requests): **0** (PR đang chờ review, chưa có request explícit)
  - `Thông báo` (info): **0**
  - `Đã stale` (cũ >7 ngày): **0** (PR có activity trong 30 ngày, không stale)

## 4. KẾT LUẬN & HÀNH ĐỘNG
- ✅ 5 VB đã review OCR quality gate — TỪNG ĐẤT PASS
- ✅ Refactor candidates đã được xác định và documented
- ✅ PR #264 review hoàn thành — 0 comments, 0 reviews
- ✅ **Không sửa file trực tiếp** — chỉ báo cáo
- ✅ Chuẩn bị commit báo cáo vào branch `heartbeat/crawl-vanban-20260907`

**TỔNG THỜI GIAN HOÀN THỊNH**: 1 review cycle (5 VB)
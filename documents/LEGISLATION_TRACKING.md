## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 2)

### Crawler chi tiết văn bản 204/2026/NĐ-CP



## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 3, văn bản 75/2026/NĐ-CP)

### Crawler chi tiết văn bản 75/2026/NĐ-CP

Hoàn thiện crawl + Markdown hóa **75/2026/NĐ-CP** theo quy trình Signed PDF OCR (PDF gốc ký số CAdES-BES tại `datafiles.chinhphu.vn`, 25 trang, 980KB, ký 28/04/2026 bởi CỔNG THÔNG TIN ĐIỆN TỬ CHÍNH PHỦ). OCR pipeline: `pdftoppm -r 150 -png` (chú ý: phải dùng `-png` thay vì mặc định `.ppm` — nếu dùng `.ppm` tesseract đọc sai sang Thông tư 60/2026/TT-BTC do encoding bug trong image pipeline) → `tesseract -l vie` trên 25 trang → cat thành 1 file raw OCR.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 75/2026/NĐ-CP | **Đã có (2026-06-14, OCR từ PDF gốc ký số CAdES-BES)** | `van-ban/quan-ly-hanh-chinh/nghi-dinh-75-2026-nd-cp-che-do-tu-chu-quan-ly-kinh-phi-hanh-chinh.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217217`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/75-ndcp-16-3.signed.pdf`; người ký: Hồ Đức Phớc (Phó Thủ tướng, ký thay Thủ tướng — theo metadata vanban.chinhphu.vn); 15 Điều, 3 Chương (I, II, III), 0 Mục, 3 Mẫu (01, 02, 03) + 2 Phụ lục (01, 02); 702 dòng, 63KB; OCR issues nghiêm trọng = 0 (1 false positive "ngày l" khớp "ngày lễ" — chính tả đúng); articles 1-15 đầy đủ, không thiếu, không trùng; chương I-III đầy đủ, đúng thứ tự La Mã |

### Cấu trúc văn bản 75/2026/NĐ-CP

- **Chương I** (Điều 1–4): Quy định chung — phạm vi điều chỉnh (trừ Đảng CSVN, Bộ Quốc phòng, Bộ Công an, cơ quan Việt Nam ở nước ngoài); đối tượng áp dụng (các bộ, cơ quan ngang bộ, cơ quan thuộc Chính phủ; Văn phòng Quốc hội, Chủ tịch nước; TAND, VKSND, KTNN; HĐND, UBND các cấp; MTTQ VN các cấp); giải thích từ ngữ (kinh phí QLHC, Quy chế chi tiêu nội bộ); nguyên tắc (không tăng kinh phí, gắn quyền tự chủ với trách nhiệm).
- **Chương II** (Điều 5–11): Chế độ tự chủ, tự chịu trách nhiệm về quản lý, sử dụng kinh phí quản lý hành chính.
  - Điều 5: Nguồn kinh phí (NSNN cấp + nguồn thu hợp pháp).
  - Điều 6: Xác định phạm vi kinh phí giao tự chủ từ NSNN — khoán quỹ tiền lương (theo biên chế trên cơ sở vị trí việc làm, cơ cấu ngạch) + khoán chi hoạt động thường xuyên (theo biên chế + định mức phân bổ).
  - Điều 7: Nội dung chi từ kinh phí tự chủ — lương, phụ cấp, khen thưởng, văn phòng phẩm, dịch vụ công, thông tin liên lạc, công tác phí, bảo dưỡng cơ sở hạ tầng, mua sắm trang thiết bị, nghiệp vụ đặc thù.
  - Điều 8: Điều chỉnh kinh phí — khi điều chỉnh biên chế, nhiệm vụ, định mức, chính sách lương, hoặc NSNN.
  - Điều 9: Nội dung tự chủ — (1) tự quyết định định mức chi (điện thoại, mức chi đặc thù); (2) sử dụng kinh phí trong phạm vi giao (khoán, chi tiếp khách, chi tiền nghỉ phép không dùng hết); (3) xác định kinh phí tiết kiệm; (4) **sử dụng kinh phí tiết kiệm** — thu nhập tăng thêm (hệ số tối đa **1,0 lần** quỹ tiền lương), khen thưởng, phúc lợi tập thể, trích lập quỹ dự phòng ổn định thu nhập; (5) xây dựng Quy chế chi tiêu nội bộ.
  - Điều 10: Kinh phí không giao tự chủ — mua sắm tài sản, hợp đồng công chức (NĐ 173/2025), vốn đối ứng quốc tế, nhiệm vụ đột xuất, chương trình mục tiêu, tinh giản biên chế.
  - Điều 11: Lập dự toán, phân bổ, giao dự toán, hạch toán, quyết toán — **mức tạm chi hàng quý tối đa 60% quỹ tiền lương thực tế**; trước 31/01 xác định tiết kiệm, Kho bạc thanh toán; trường hợp tiết kiệm thấp hơn số tạm chi, trừ vào tiết kiệm năm sau.
- **Chương III** (Điều 12–15): Điều khoản thi hành.
  - Điều 12: Trách nhiệm cơ quan thực hiện chế độ tự chủ — báo cáo Mẫu số 02 trước 31/01 năm sau.
  - Điều 13: Trách nhiệm Bộ trưởng, UBND cấp tỉnh — báo cáo Bộ Tài chính Mẫu số 03 trước 28/02 năm sau.
  - Điều 14: Trách nhiệm Bộ Tài chính + Kho bạc Nhà nước (chuyển nguồn cuối năm).
  - Điều 15: Hiệu lực từ **01/5/2026** — thay thế **NĐ 130/2005/NĐ-CP** (17/10/2005) và NĐ 117/2013/NĐ-CP (07/10/2013); điều khoản chuyển tiếp cho cơ quan đã giao tự chủ năm 2025 (tiếp tục theo NĐ 130/2005).

### Một số điểm đáng chú ý

- **Hệ số thu nhập tăng thêm tối đa 1,0 lần** quỹ tiền lương thực tế (không bao gồm phụ cấp theo lương, đóng góp theo lương) — theo quy định tại NĐ 111/2022/NĐ-CP.
- **Mức tạm chi hàng quý tối đa 60%** quỹ tiền lương thực tế của cán bộ, công chức, người lao động trong một quý.
- **Tiết kiệm chi quỹ lương** + tiết kiệm chi hoạt động thường xuyên → cộng dồn thành nguồn kinh phí tiết kiệm; dùng cho: (i) thu nhập tăng thêm, (ii) khen thưởng, (iii) phúc lợi tập thể, (iv) trích lập quỹ dự phòng ổn định thu nhập.
- **Đối tượng áp dụng rất rộng**: 6 nhóm cơ quan hành chính các cấp từ trung ương đến xã/phường/đặc khu, gồm cả TAND, VKSND, KTNN, MTTQ VN.
- **Trừ 4 nhóm**: Đảng CSVN, Bộ Quốc phòng, Bộ Công an, Cơ quan Việt Nam ở nước ngoài (theo quy định riêng).
- **Trình tự báo cáo**: 31/01 cơ quan → Mẫu 02 → cấp trên → 15/02 cấp trên → 28/02 cấp I → Bộ Tài chính (Mẫu 03).
- **Quy chế chi tiêu nội bộ** (Mẫu số 01) — Thủ trưởng ban hành, công khai trong toàn cơ quan, gửi cơ quan tài chính cùng cấp để theo dõi.
- Thay thế NĐ 130/2005/NĐ-CP — văn bản đã có hiệu lực 21 năm (2005–2026), nhiều điều khoản đã lạc hậu so với Luật NSNN 89/2025/QH15.

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-14 lần 2)

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 75/2026/NĐ-CP | **CÓ** (Đệ #1 lần 10 ngày 2026-06-10) | Chưa có | **Đã có (2026-06-14)** |

### Ghi chú xử lý

- **PDF gốc có chữ ký số CAdES-BES** (ký bởi CỔNG THÔNG TIN ĐIỆN TỬ CHÍNH PHỦ; thời gian ký: 28.04.2026 14:37:55 +07:00). Vì có chữ ký số nên `pdftotext` chỉ trích được metadata chữ ký, không trích được nội dung văn bản. Phải dùng pipeline OCR.
- **OCR pipeline issue quan trọng**: Khi dùng `pdftoppm -r 150` (mặc định `.ppm`), tesseract trả về nội dung sai (đọc sang Thông tư 60/2026/TT-BTC thay vì NĐ 75/2026/NĐ-CP). Nguyên nhân: PNG vs PPM có encoding khác nhau và tesseract xử lý khác. Khi dùng `pdftoppm -r 150 -png` thì OCR ra đúng nội dung. Đã xác minh bằng cách xem ảnh PNG trực tiếp bằng vision model → khẳng định đây là NĐ 75/2026/NĐ-CP.
- **OCR raw còn một số lỗi nhỏ** (thâm/thấm quyền → thẩm quyền; thiếu dấu, lỗi chính tả lác đác) đã được sửa toàn bộ trong quá trình Markdown hóa.
- **Người ký**: Metadata chính thức trên vanban.chinhphu.vn ghi "Hồ Đức Phớc" — Hồ Đức Phớc là Bộ trưởng Bộ Tài chính (Bộ đề xuất Nghị định). Trong văn bản PDF, phần chữ ký ghi "KT. THỦ TƯỚNG / PHÓ THỦ TƯỚNG" + tên Hồ Đức Phớc. Có thể Hồ Đức Phớc đã được bổ nhiệm Phó Thủ tướng tính đến 2026. Đã ghi nhận trong front matter là "Hồ Đức Phớc (Phó Thủ tướng, ký thay Thủ tướng)".
- **Cấu trúc gọn**: 15 Điều, 3 Chương, 0 Mục. So với các NĐ khác (193, 200, 204 đều 30-50 Điều, nhiều Chương/Mục), đây là văn bản ngắn gọn nhưng có ý nghĩa thực tiễn rất lớn (áp dụng cho toàn bộ hệ thống hành chính các cấp).
- **Phụ lục Mẫu số 01, 02, 03** đã được Markdown hóa đầy đủ cấu trúc báo cáo (Mẫu 01: hướng dẫn xây dựng Quy chế chi tiêu nội bộ; Mẫu 02: báo cáo của cơ quan thực hiện; Mẫu 03: báo cáo tổng hợp gửi Bộ Tài chính).
- **Phụ lục 01, 02** là bảng biểu thống kê tổng hợp (cho cơ quan trung ương và địa phương) — chỉ trình bày cấu trúc bảng, không điền số liệu cụ thể (vì là mẫu trống).
- Phiên thực hiện: agent:github-io:subagent:6bb15b01-36bc-401b-a01f-6d8ce7191222 (Đệ #3 Full Content Crawler — lần 3 — 75/2026/NĐ-CP).

---

### Crawler chi tiết văn bản 201/2026/NĐ-CP

Hoàn thiện crawl + Markdown hóa **201/2026/NĐ-CP** theo quy trình Signed PDF OCR / Web extract (nội dung lấy từ thuviennhadat.vn + cross-check thuehaiquan + luatvietnam vì datafiles.chinhphu.vn và vanban.chinhphu.vn đều là trang JS-rendered không crawl được bằng curl/web_fetch thông thường).

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 201/2026/NĐ-CP | **Đã có (2026-06-14, Markdown từ nguồn web chính thức + 2 cross-check)** | `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-201-2026-nd-cp-sua-doi-thue-suat-xuat-khau.md` | URL: `https://luatvietnam.vn/thue/nghi-dinh-201-2026-nd-cp-sua-doi-thue-suat-xuat-khau-theo-nghi-dinh-26-2023-nd-cp-436911-d1.html`; 3 Điều (không có Chương), 1 Phụ lục bảng thuế (2 nhóm: 25.29 và 81.06); 211 dòng, 14KB; OCR issues = 0; articles 1-3 đầy đủ, không thiếu, không trùng |

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-13)

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 201/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có** (2026-06-14) |

### Ghi chú xử lý

- Nội dung văn bản 201/2026/NĐ-CP đã được cross-check qua 3 nguồn: luatvietnam.vn (lược bớt còn 1/3 do paywall), thuviennhadat.vn (toàn văn đầy đủ — dùng làm nguồn chính), thuehaiquan.tapchikinhtetaichinh.vn (bài phân tích + bảng tóm tắt khớp 100% với văn bản).
- **Không tìm được PDF gốc** từ datafiles.chinhphu.vn hoặc vanban.chinhphu.vn — cả hai đều là trang .NET WebForm + JS-render, không có JSON API public. Curl chỉ lấy được HTML skeleton.
- **Không tìm được docid** trên vanban.chinhphu.vn (lướt dải 218420–218450 không thấy; nhiều khả năng docid nằm ngoài phạm vi này hoặc chưa được index public). Tạm thời để trống trường docid; phiên sau sẽ dùng browser-automation hoặc mở rộng range dò tìm.
- Văn bản này là NĐ sửa đổi biểu thuế nên cấu trúc gọn: 3 Điều + 1 Phụ lục bảng. Nội dung Phụ lục đã được bóc tách đầy đủ 2 nhóm hàng (25.29 và 81.06), 15 dòng thuế chi tiết.
- Có thêm phần **TÓM TẮT NỘI DUNG ĐIỀU CHỈNH** trong file Markdown — so sánh thuế suất cũ/mới, xu hướng chính sách, phạm vi áp dụng (dựa trên thông tin từ Bộ Tài chính đăng tải qua các báo: vietnamplus, congthuong, sct.dongnai).
- Phiên thực hiện: agent:github-io:subagent:f4b99710-63e0-4d55-9a1a-589948dd06f9 (Đệ #3 Full Content Crawler 201/2026/NĐ-CP).

---
## Cập nhật 2026-06-13 (phiên Đệ #1 Discovery — lần 12)

| 31/2026/TT-BCT | 14/06/2026 | Quy định truy xuất nguồn gốc sản phẩm, hàng hóa; hiệu lực 01/7/2026 | Thương mại - Công thương | — | **Đã có (2026-06-14)** | File: `van-ban/thuong-mai-cong-thuong/thong-tu-31-2026-tt-bct-truy-xuat-nguon-goc-san-pham.md`; người ký: Nguyễn Sinh Nhật Tân (KT. Bộ trưởng Bộ Công Thương - Thứ trưởng); 19 Điều (1-19), 5 Chương (I-V), 0 Phụ lục; 294 dòng, 24KB; OCR issues = 0 |

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét web tổng hợp Brave + Gemini các nhóm chủ đề: Thuế, Đất đai, Nông nghiệp, Thú y, Năng lượng, Chứng khoán, Hình sự, Giáo dục, Giao thông, Tài chính, Lao động, Xây dựng. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-13 lần 11): phát hiện **5 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 5:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 203/2026/NĐ-CP | 11/06/2026 | Quy định về thi hành án tử hình bằng tiêm thuốc độc — quy trình 3 bước (làm mất tri giác, liệt hệ vận động, ngừng tim); thay thế NĐ 43/2020/NĐ-CP; quy định chi phí mai táng, chế độ người tham gia; hiệu lực 01/7/2026 | Tư pháp / Hình sự | 218409 | **Có (2026-06-13, OCR từ PDF gốc + sửa lỗi)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218409`; File: `van-ban/tu-phap-thi-hanh-an/nghi-dinh-203-2026-nd-cp-thi-hanh-an-tu-hinh.md`; 24 Điều, 5 Chương |
| 199/2026/NĐ-CP | 05/06/2026 | Quy định chính sách hỗ trợ phục vụ đối với chức danh, chức vụ lãnh đạo thuộc diện Bộ Chính trị, Ban Bí thư quản lý (Công an, Quân đội); mức 2,7 triệu/tháng (Thượng tướng, Đô đốc), 2 triệu/tháng (Trung tướng), 1,35 triệu/tháng (Thiếu tướng); thay thế QĐ 269/2005/QĐ-TTg; hiệu lực 20/7/2026 | Lao động / Tiền lương | 218364 | **Đã có (2026-06-13, OCR từ PDF gốc)** | File: `van-ban/lao-dong/nghi-dinh-199-2026-nd-cp-ho-tro-phuc-vu-lanh-dao-cong-an-quan-doi.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218364`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/199-ndcp.signed.pdf`; Người ký: Nguyễn Văn Thắng (Phó TT ký thay TT); 8 Điều |
| 193/2026/NĐ-CP | 01/06/2026 | Quy định về quyết toán vốn đầu tư dự án sử dụng vốn nhà nước; phân tách dự án/tiểu dự án độc lập; thẩm quyền phê duyệt quyết toán thuộc người quyết định đầu tư; thời hạn 4–9 tháng tùy quy mô; thay thế NĐ 254/2025/NĐ-CP phần quyết toán; hiệu lực 01/7/2026 | Tài chính / Đầu tư | 218345 | **Có (2026-06-13, OCR từ PDF gốc + sửa lỗi)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218345`; File: `van-ban/dau-tu/nghi-dinh-193-2026-nd-cp-quyet-toan-von-dau-tu-du-an.md`; 31 Điều, không có Chương |
| 45/2026/TT-BGDĐT | 10/06/2026 | Sửa đổi, bổ sung Thông tư 15/2025/TT-BGDĐT hướng dẫn chức năng, nhiệm vụ, quyền hạn của Sở Giáo dục và Đào tạo và Phòng Văn hóa - Xã hội cấp xã; hiệu lực ngay 10/6/2026 | Giáo dục | — | **Có (2026-06-13, OCR từ PDF gốc datafiles.chinhphu.vn)** | URL: `https://thuvienphapluat.vn/van-ban/Giao-duc/Thong-tu-45-2026-TT-BGDDT-sua-doi-Thong-tu-15-2025-TT-BGDDT-nhiem-vu-cua-So-Giao-duc-709953.aspx`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/45-bgddt.pdf`; Người ký: Phạm Ngọc Thưởng (Bộ trưởng); 4 Điều |
| 28/2026/TT-BXD | 10/06/2026 | Quy định về đăng kiểm phương tiện thủy nội địa — cho phép liên danh thực hiện dịch vụ đăng kiểm, bỏ tem kiểm định, áp dụng số kiểm soát điện tử; không điều chỉnh tàu quốc phòng, an ninh, tàu cá, phương tiện nhỏ; hiệu lực 01/8/2026 | Giao thông / Hàng hải | 218412 | **Có (2026-06-13, PDF không ký số - pdftotext trích thẳng)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218412`; File: `van-ban/xay-dung/thong-tu-28-2026-tt-bxd-dang-kiem-phuong-tien-thuy-noi-dia.md`; 13 Điều, 3 Chương |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-13 lần 11)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 203/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 199/2026/NĐ-CP | **CÓ** | Đã có |
| 193/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 45/2026/TT-BGDĐT | **CÓ** | Đã crawl — `van-ban/giao-duc-dao-tao/thong-tu-45-2026-tt-bgddt-sua-doi-tt-15-2025-chuc-nang-so-gd-dt-phong-vh-xh.md` (4 Điều) |
| 28/2026/TT-BXD | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo

1. **Tư pháp / Hình sự**: **203/2026/NĐ-CP** — thi hành án tử hình bằng tiêm thuốc độc; hiệu lực 01/7/2026 (rất gần); tác động hệ thống tư pháp, pháp y toàn quốc.
2. **Tài chính / Đầu tư**: **193/2026/NĐ-CP** — quyết toán vốn đầu tư dự án; hiệu lực 01/7/2026; tác động toàn bộ dự án đầu tư công.
3. **Lao động / Tiền lương**: **199/2026/NĐ-CP** — hỗ trợ phục vụ lãnh đạo Công an, Quân đội; hiệu lực 20/7/2026.
4. **Giáo dục**: **45/2026/TT-BGDĐT** — sửa đổi chức năng Sở GDĐT; hiệu lực ngay 10/6/2026; tác động hệ thống giáo dục cấp tỉnh/xã.
5. **Giao thông / Hàng hải**: **28/2026/TT-BXD** — đăng kiểm thủy nội địa mới; hiệu lực 01/8/2026; tác động chủ phương tiện thủy nội địa.

### Ghi chú xử lý

- **5 văn bản mới** sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- **203/2026/NĐ-CP**: Docid xác minh **218409** trên vanban.chinhphu.vn; thay thế NĐ 43/2020/NĐ-CP.
- **199/2026/NĐ-CP**: Docid xác minh **218364**; thay thế QĐ 269/2005/QĐ-TTg; mức hỗ trợ phục vụ cao nhất 2,7 triệu đ/tháng.
- **193/2026/NĐ-CP**: Docid xác minh **218345**; thay thế phần quyết toán của NĐ 254/2025/NĐ-CP.
- **28/2026/TT-BXD**: Docid xác minh **218412**; cho phép liên danh đăng kiểm, bỏ tem kiểm định.
- **45/2026/TT-BGDĐT**: Hiệu lực ngay — ưu tiên cao dù mới ban hành.
- Văn bản cùng đợt hiệu lực 01/7/2026: 203/2026/NĐ-CP, 193/2026/NĐ-CP.
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, moc.gov.vn, tapchitoaan.vn, thuvienphapluat.vn, kiemtoanxaydung.vn.
- Ngày phát hiện: 2026-06-13 14:57 ICT
- Phiên thực hiện: agent:github-io:subagent:6884fe8c-3b03-4afa-a7d9-e27cb02774fa (Đệ #1 Discovery — lần 12)

---
## Cập nhật 2026-06-13 (phiên Đệ #1 Discovery — lần 11)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét dải NĐ-CP 203–212 + kiểm tra Thông tư tuần 06–13/6/2026 qua web search Brave + Gemini + web_fetch vanban.chinhphu.vn. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-12): phát hiện **5 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 5:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 204/2026/NĐ-CP | 11/06/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực thú y — phạt tiền đến 50 triệu đồng (cá nhân) / 100 triệu đồng (tổ chức); không đeo rọ mõm cho chó nơi công cộng phạt 1–2 triệu đồng; kinh doanh thú y không phép phạt đến 100 triệu; hiệu lực 01/8/2026 | Nông nghiệp / Thú y | — | **Chưa có** | Nguồn: baotintuc.vn, sggp.org.vn, vietnamplus.vn, baochinhphu.vn; tác động ngành thú y, chủ nuôi động vật toàn quốc |
| 28/2026/NQ-CP | 09/06/2026 | Cơ chế đặc thù cho phép khai thác than vượt không quá 15% công suất giấy phép nhằm bảo đảm an ninh năng lượng quốc gia — sản lượng vượt chỉ phục vụ sản xuất điện; phải đăng ký với UBND cấp tỉnh và Bộ NN&MT; hiệu lực 09/6/2026 đến 31/12/2027 | Năng lượng / Tài nguyên | 218385 | **Đã có (2026-06-14, OCR từ PDF ký số CAdES-BES)** | File: `van-ban/nang-luong-tai-nguyen/nghi-quyet-28-2026-nq-cp-co-che-khai-thac-than-vuot-15-phan-tram-cong-suat.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218385`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/28-nqcp.signed.pdf`; người ký: Phó Thủ tướng Phạm Gia Túc (KT. Thủ tướng); 7 Điều, 0 Chương; 144 dòng, 11.1KB; OCR issues = 0; articles 1-7 đầy đủ |
| 63/2026/TT-BTC | 05/06/2026 | Quy định nội dung và mức chi hoạt động thi kỹ năng nghề trong nước và quốc tế — thay thế TT liên tịch 43/2012/TTLT-BTC-BLĐTBXH; định mức chi xây dựng đề thi, chấm thi, huấn luyện đội tuyển quốc gia; hiệu lực 05/6/2026 | Giáo dục nghề nghiệp / Tài chính | — | **Đã có (2026-06-14)** | File: `van-ban/giao-duc-dao-tao/thong-tu-63-2026-tt-btc-noi-dung-muc-chi-thi-ky-nang-nghe.md`; nguồn: luatvietnam.vn (slug 437238); người ký: KT. Bộ trưởng Bộ Tài chính; 7 Điều (Điều 1: phạm vi; Điều 2: nguồn kinh phí; Điều 3: nguyên tắc; Điều 4: chi chung; Điều 5: chi thi trong nước; Điều 6: chi thi quốc tế; Điều 7: điều khoản thi hành); KHÔNG có Chương, KHÔNG có Phụ lục (định mức chi nằm trong nội dung từng Điều); 196 dòng, 16KB; OCR issues = 0; articles 1-7 đầy đủ, không thiếu, không trùng; docid: 437238 |
| 30/2026/TT-BCT | 10/06/2026 | Quy định phương pháp xác định giá dịch vụ phát điện đối với nhà máy điện BOT chưa ký hợp đồng mua bán điện — IRR không vượt quá 12%; hướng dẫn Luật Điện lực 2024; hiệu lực 28/7/2026 | Năng lượng / Thương mại | — | **Đã có (2026-06-14)** | File: `van-ban/nang-luong-tai-nguyen/thong-tu-30-2026-tt-bct-gia-dich-vu-phat-dien-nha-may-bot.md`; nguồn: moit.gov.vn (bài viết + PDF 19 trang OCR) + petrotimes.vn (cross-check); người ký: Nguyễn Hoàng Long (Bộ trưởng Bộ Công Thương); 16 Điều + 4 Chương (I-IV) + Phụ lục I (2 biểu mẫu tài chính); 699 dòng, 47KB; OCR issues = 0; articles 1-16 đầy đủ, không thiếu, không trùng; docid: tt30-2026-bct |
| 60/2026/TT-BTC | 31/05/2026 | Hướng dẫn quản lý, sử dụng và quyết toán kinh phí ngân sách nhà nước thực hiện Chương trình mục tiêu quốc gia về xây dựng nông thôn mới, giảm nghèo bền vững và phát triển KT-XH vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026–2035 | Tài chính / Ngân sách | — | **Đã có (2026-06-13)** | File: `van-ban/tai-chinh/thong-tu-60-2026-tt-btc-huong-dan-quan-ly-su-dung-quyet-toan-kinh-phi-chuong-trinh-muc-tieu-quoc-gia.md`; URL: `https://thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-60-2026-TT-BTC-huong-dan-quan-ly-kinh-phi-Ngan-sach-xay-dung-nong-thon-moi-709846.aspx` |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-12)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 204/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 28/2026/NQ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có (7 Điều)** (2026-06-14) |
| 63/2026/TT-BTC | **KHÔNG** | Thêm mới — Chưa có |
| 30/2026/TT-BCT | **KHÔNG** | Thêm mới — Chưa có |
| 60/2026/TT-BTC | **CÓ** | Đã có |

### Đề xuất ưu tiên phiên tiếp theo

1. **Nông nghiệp / Thú y**: **204/2026/NĐ-CP** — xử phạt thú y mới; hiệu lực 01/8/2026; tác động ngành thú y và chủ nuôi động vật.
2. **Năng lượng**: **28/2026/NQ-CP** — cơ chế đặc thù khai thác than; hiệu lực ngay 09/6/2026; tác động an ninh năng lượng quốc gia.
3. **Năng lượng**: **30/2026/TT-BCT** — giá điện BOT mới; hiệu lực 28/7/2026; tác động đàm phán HĐMBĐ điện.
4. **Giáo dục nghề nghiệp / Tài chính**: **63/2026/TT-BTC** — thi kỹ năng nghề; hiệu lực ngay 05/6/2026.
5. **Tài chính / Ngân sách**: **60/2026/TT-BTC** — kinh phí Chương trình mục tiêu quốc gia; hiệu lực 31/5/2026.

### Ghi chú xử lý

- **5 văn bản mới** sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- **28/2026/NQ-CP** đã xác minh docid chính thức **218385** trên vanban.chinhphu.vn.
- 28/2026/NQ-CP (khai thác than) và 30/2026/TT-BCT (giá điện BOT) cùng nhóm năng lượng — ưu tiên crawl chung.
- **204/2026/NĐ-CP** có hiệu lực 01/8/2026 (sớm hơn nhóm 01/7/2026); ưu tiên cao trong nhóm nông nghiệp.
- Nguồn: web_search Brave + Gemini + web_fetch vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, moit.gov.vn, thuvienphapluat.vn, vtv.vn.
- Ngày phát hiện: 2026-06-13 13:00 ICT
- Phiên thực hiện: agent:github-io:subagent:58b1bfa1-e1ef-473b-bdef-580705ae0e66 (Đệ #1 Discovery 2026-06-13)

---
## Cập nhật 2026-06-12 (phiên Đệ #1 Discovery — lần 10)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét dải NĐ-CP 151–212 + kiểm tra Thông tư tuần 01–12/6/2026 qua web search Brave + Gemini + web_fetch vanban.chinhphu.vn. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-12 trước phiên này): phát hiện **5 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 5:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 46/2026/TT-BGDĐT | 10/06/2026 | Ban hành Điều lệ trường trung học nghề — quy định tổ chức, hoạt động trường trung học nghề tích hợp (văn hóa THPT + chuyên môn nghề) dành cho học sinh tốt nghiệp THCS; mục tiêu đào tạo nguồn nhân lực, tạo điều kiện vào lao động hoặc học lên; hiệu lực 10/6/2026 | Giáo dục / GD nghề nghiệp | — | **Chưa có** | Tác động trực tiếp hệ thống GD nghề nghiệp; mở rộng con đường học tập sau THCS cho hàng triệu học sinh; nguồn: luatvietnam.vn, giaoduc.net.vn, thuvienphapluat.vn |
| 56/2026/TT-BCA | 01/07/2026 (hiệu lực) | Quy định quản lý, theo dõi người bị cấm đi khỏi nơi cư trú — cụ thể hóa BLTTHS và Luật Thi hành tạm giữ, tạm giam và cấm đi khỏi nơi cư trú năm 2025; Trưởng Công an cấp xã phân công cán bộ quản lý, theo dõi, kiểm tra; lập biên bản nếu vi phạm; hiệu lực 01/7/2026 | An ninh trật tự / Tố tụng hình sự | — | **Chưa có** | Nguồn: baomoi.com, tapchitoaan.vn, congbao.chinhphu.vn (file PDF bocongan.gov.vn); tác động hệ thống CA cấp xã toàn quốc |
| 19/2026/TT-NHNN | 19/05/2026 | Quy định phân cấp trong thực hiện thủ tục hành chính quy định tại NĐ 94/2025/NĐ-CP về cơ chế thử nghiệm có kiểm soát trong lĩnh vực ngân hàng; hiệu lực 30/6/2026 | Ngân hàng / Tài chính | — | **Chưa có** | Tác động Sandbox ngân hàng; nguồn: pbgdplthainguyen.gov.vn, lsvn.vn |
| 35/2026/TT-BTC | 31/03/2026 | Quy định chế độ tiếp khách nước ngoài vào làm việc tại Việt Nam, chế độ chi tổ chức hội nghị, hội thảo quốc tế tại Việt Nam và chế độ tiếp khách trong nước — thay thế TT 71/2018/TT-BTC; hiệu lực 18/5/2026 | Tài chính / Đối ngoại | 430995 | **Đã có (2026-06-14, Markdown từ nguồn web luatvietnam)** | URL: `https://luatvietnam.vn/hanh-chinh/thong-tu-35-2026-tt-btc-quy-dinh-che-do-tiep-khach-va-to-chuc-hoi-nghi-tai-viet-nam-430995-d1.html`; File: `van-ban/tai-chinh/thong-tu-35-2026-tt-btc-che-do-tiep-khach-nuoc-ngoai-hoi-nghi-quoc-te-tai-viet-nam.md`; người ký: KT. Bộ trưởng Bộ Tài chính - Thứ trưởng Nguyễn Thị Bích Ngọc; 35 Điều + 7 Chương + Phụ lục; OCR issues = 0 |
| 31/2026/TT-BCT | 11/06/2026 | Quy định truy xuất nguồn gốc sản phẩm, hàng hóa thuộc phạm vi quản lý của Bộ Công Thương — truy xuất điện tử bắt buộc đối với nhóm hàng rủi ro cao; thương nhân thành lập mới từ 1/1/2027 phải thực hiện ngay; hiệu lực 01/7/2026 | Thương mại / Công nghiệp | — | **Đã có (2026-06-14)** | File: `van-ban/thuong-mai-cong-thuong/thong-tu-31-2026-tt-bct-truy-xuat-nguon-goc-san-pham.md`; 19 Điều, 5 Chương |

### Xác minh các văn bản ưu tiên từ nhiệm vụ

| Số hiệu | File trong van-ban/? | Kết quả xác minh | Trạng thái cũ | Trạng thái mới |
|---|:---:|---|:---:|:---:|
| 185/2026/NĐ-CP | `van-ban/lao-dong/nghi-dinh-185-2026-nd-cp-thon-to-dan-pho.md` | **ĐÃ CÓ** file đầy đủ — front matter có đầy đủ metadata (so_hieu, ngay_ban_hanh, nguoi_ky, thay_the, source), lastedit 2026-06-10 | Chưa có (ghi sai) | **Đã có** |
| 56/2026/TT-BCA | Không tìm thấy | **Chưa có** — quy định quản lý theo dõi người bị cấm đi khỏi nơi cư trú; PDF tại bocongan.gov.vn; hiệu lực 01/7/2026 | — | Chưa có |
| 29/2026/TT-BCA | Không tìm thấy | **Chưa có** — không tìm thấy trong web search; có thể chưa ban hành hoặc số hiệu khác | — | Chưa có (chờ xác minh) |
| 35/2026/TT-BTC | Không | Placeholder chưa xác minh đã bị loại khỏi PR#204 theo OCR Quality Gate | — | Chưa có — cần crawl lại từ nguồn chính thức |

### Văn bản phát hiện thêm (chưa tạo entry — chờ phiên sau)

- **185/2026/NĐ-CP** (Lao động / Hành chính) — thôn, tổ dân phố, chế độ người không chuyên trách; ban hành 26/5/2026; hiệu lực 26/5/2026; file đã có tại `van-ban/lao-dong/nghi-dinh-185-2026-nd-cp-thon-to-dan-pho.md` → chuyển sang "Đã có" trong tracking
- **198/2026/NĐ-CP** (Ngân hàng / Tổ chức bộ máy) — sửa đổi cơ cấu Ngân hàng Nhà nước; ban hành 10/6/2026; hiệu lực 01/7/2026; file đã có tại `van-ban/ngan-hang/nghi-dinh-198-2026-nd-cp-sua-doi-co-cau-nhnn.md`; cần xác minh trạng thái trong tracking
- **37/2026/TT-BCA** (Giao thông vận tải) — sửa đổi đăng ký xe, nhận kết quả qua Cổng DVCQG, VNeID, bưu chính; hiệu lực 08/6/2026; file đã có tại `van-ban/giao-thong-van-tai/thong-tu-37-2026-tt-bca-dang-ky-xe-vneid.md`; cần xác minh trạng thái
- **40/2026/TT-BGDĐT** (Giáo dục) — đánh giá kết quả rèn luyện sinh viên, thang điểm 100, 5 mức; hiệu lực 30/6/2026; file đã có tại `van-ban/giao-duc-dao-tao/thong-tu-40-2026-tt-bgd-dt-cong-tac-sinh-vien.md`; cần xác minh trạng thái
- **185-QĐ/TW** (Bộ Chính trị) — quy định tổng biên chế 2026 cho cơ quan, ban đảng, đơn vị sự nghiệp của Đảng, Mặt trận Tổ quốc, đoàn thể Trung ương; ký 02/6/2026
- **193-QĐ/TW** (Bộ Chính trị) — quy định chức năng, nhiệm vụ, quyền hạn của Ban Chỉ đạo Trung ương về hoàn thiện thể chế và thực thi pháp luật; ký 03/6/2026 bởi Tổng Bí thư, Chủ tịch nước Tô Lâm

### Đối chiếu nhanh với `van-ban/` và LEGISLATION_TRACKING.md (đến 2026-06-12 trước phiên)

| Số hiệu | Trong tracking? | File van-ban/? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|:---:|
| 46/2026/TT-BGDĐT | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 56/2026/TT-BCA | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 19/2026/TT-NHNN | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 35/2026/TT-BTC | **KHÔNG** | Không | — | Thêm mới — Chưa có; placeholder chưa xác minh đã bị loại khỏi PR#204 |
| 31/2026/TT-BCT | **KHÔNG** | Không | — | Thêm mới — Chưa có | **Đã có (19 Điều + 5 Chương)** (2026-06-14) |
| 185/2026/NĐ-CP | **CÓ (ghi sai)** | Có | Chưa có | **Sửa → Đã có** |
| 29/2026/TT-BCA | **KHÔNG** | Không | — | Chưa có (chờ xác minh — có thể chưa ban hành) |

### Đề xuất ưu tiên phiên tiếp theo

1. **Giáo dục**: **46/2026/TT-BGDĐT** — vừa ban hành ngày 10/6/2026 (2 ngày trước), hiệu lực ngay 10/6/2026; quy định mô hình trường trung học nghề tích hợp mới; tác động hàng triệu học sinh tốt nghiệp THCS hàng năm.
2. **Thương mại / Công nghiệp**: **31/2026/TT-BCT** — vừa ban hành ngày 11/6/2026 (hôm nay), hiệu lực 01/7/2026; truy xuất nguồn gốc điện tử bắt buộc; tác động chuỗi cung ứng toàn quốc.
3. **An ninh trật tự**: **56/2026/TT-BCA** — quản lý người bị cấm đi khỏi nơi cư trú; hiệu lực 01/7/2026; tác động hệ thống CA cấp xã.
4. **Giáo dục**: 40/2026/TT-BGDĐT — đánh giá rèn luyện sinh viên; hiệu lực 30/6/2026.
5. **Ngân hàng**: 19/2026/TT-NHNN — sandbox ngân hàng; hiệu lực 30/6/2026.
6. **Ngân hàng**: 198/2026/NĐ-CP — sửa đổi cơ cấu NHNN; hiệu lực 01/7/2026.

## Ghi chú xử lý

- **5 văn bản mới** đưa vào bảng chính: 46/2026/TT-BGDĐT, 56/2026/TT-BCA, 19/2026/TT-NHNN, 35/2026/TT-BTC, 31/2026/TT-BCT — cần crawl chi tiết trong các phiên Đệ #3 Full Content Crawler tiếp theo.
- **185/2026/NĐ-CP**: File tồn tại đầy đủ → chuyển từ "Chưa có (ghi sai)" → **Đã có** trong tracking.
- **35/2026/TT-BTC**: Placeholder chưa xác minh đã bị loại khỏi PR#204; giữ trạng thái **Chưa có**, cần crawl lại từ nguồn chính thức trước khi tạo file public.
- **29/2026/TT-BCA**: Không tìm thấy bằng web search — có thể chưa ban hành, số hiệu sai, hoặc thuộc nhóm văn bản hạn chế công khai; chờ phiên sau xác minh thêm.
- Nguồn: web_search Brave + Gemini + web_fetch vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, thuvienphapluat.vn, giaoduc.net.vn, congbao.chinhphu.vn.
- Ngày phát hiện: 2026-06-12 13:30 ICT
- Phiên thực hiện: agent:github-io:subagent (Đệ #1 Discovery — lần 10)

---## Cập nhật 2026-06-10 (phiên Đệ #1 Discovery — bổ sung lần 2)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét bổ sung các văn bản tháng 6/2026 qua web search + web_fetch vanban.chinhphu.vn. So sánh với documents/LEGISLATION_TRACKING.md (đến 2026-06-10 cuối ngày): phát hiện 3 văn bản mới chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 3:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 200/2026/NĐ-CP | 05/06/2026 | Quy định về chào bán, giao dịch trái phiếu doanh nghiệp riêng lẻ tại thị trường trong nước và chào bán trái phiếu doanh nghiệp ra thị trường quốc tế | Chứng khoán / Tài chính | 218389 | **Đã có (2026-06-14)** | File: `van-ban/chung-khoan/nghi-dinh-200-2026-nd-cp-chao-ban-giao-dich-trai-phieu-doanh-nghiep.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218389`; người ký: Thủ tướng CP; hiệu lực 01/7/2026; 51 Điều, 6 Chương (I, III, IV, V, VII, VIII), thiếu heading II, VI; 4183 dòng, 233KB; OCR issues = 0 |
| 169/2026/NĐ-CP | 15/05/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực hải quan — phạt đến 80 triệu đồng vận chuyển hàng tạm ngừng xuất khẩu, phạt đến 50 triệu không khai báo ngoại tệ, vàng; thay thế NĐ 128/2020/NĐ-CP | Thuế / Hải quan | 218xxx | **Chưa có** | URL cần xác minh trên vanban.chinhphu.vn; hiệu lực 01/7/2026 |
| 60/2026/TT-BTC | 31/05/2026 | Hướng dẫn quản lý, sử dụng và quyết toán kinh phí ngân sách nhà nước thực hiện Chương trình mục tiêu quốc gia về xây dựng nông thôn mới, giảm nghèo bền vững và phát triển KT-XH vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026-2035 | Tài chính / Ngân sách | 218378 | **Đã có (2026-06-14)** | File: `van-ban/tai-chinh/thong-tu-60-2026-tt-btc-huong-dan-quan-ly-su-dung-quyet-toan-kinh-phi-chuong-trinh-muc-tieu-quoc-gia.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218378`; 22 Điều + 4 Chương |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-10)

| Số hiệu | Trong tracking? | Trạng thái |
|---|---|
| 200/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có (51 Điều + 6 Chương)** (2026-06-14) |
| 169/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 60/2026/TT-BTC | **CÓ** | Đã có |

### Đề xuất ưu tiên phiên tiếp theo

1. **Chứng khoán / Tài chính**: 200/2026/NĐ-CP — quy định mới về trái phiếu doanh nghiệp; tác động trực tiếp thị trường tài chính.
2. **Hải quan**: 169/2026/NĐ-CP — xử phạt hành chính hải quan mới; hiệu lực 01/7/2026.
3. **Tài chính / Ngân sách**: 60/2026/TT-BTC — hướng dẫn kinh phí Chương trình mục tiêu quốc gia.

## Ghi chú xử lý

- 3 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **200/2026/NĐ-CP** (trái phiếu doanh nghiệp — tác động thị trường tài chính rộng).
- 169/2026/NĐ-CP cùng đợt hiệu lực 01/7/2026 với nhóm 153-157.
- Nguồn: web_search Brave + Gemini + web_fetch vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn.
- Ngày phát hiện: 2026-06-10 21:30 ICT
- Phiên thực hiện: agent:github-io:subagent bổ sung 2026-06-10

---# Cập nhật 2026-06-10 (phiên Đệ #1 Discovery — cuối ngày)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

Quét toàn bộ dải NĐ-CP 151–202 từ vanban.chinhphu.vn + luatvietnam.vn + chinhphu.vn. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-11): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất (hiệu lực 01/7/2026):

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 153/2026/NĐ-CP | 14/05/2026 | Sửa đổi, bổ sung NĐ 01/2015/NĐ-CP | Hải quan / Thương mại | 218083 | Đã có |** |
| 157/2026/NĐ-CP | 15/05/2026 | Quy định thanh toán, quyết toán vốn NSNN để cấp bù lãi suất cho NHTM thực hiện chính sách tín dụng ưu đãi (nông nghiệp, xuất khẩu); hiệu lực 01/7/2026 | Tài chính / Tín dụng ưu đãi | 218158 | **Đã có (2026-06-14)** | File: `van-ban/tai-chinh/nghi-dinh-157-2026-nd-cp-cap-bu-lai-suat-tin-dung-uu-dai.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218158`; người ký: Nguyễn Văn Thắng (Thủ tướng CP); 10 Điều (1-10), 0 Chương, 4 Phụ lục (Mẫu 01-04); 455 dòng, 33KB; OCR issues = 0 | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218083`; hiệu lực 05/7/2026 |
| 154/2026/NĐ-CP | 15/05/2026 | Quy định chi tiết một số điều và biện pháp tổ chức thi hành Luật Tiếp công dân | Hành chính / Tư pháp | 218230 | **Đã có (2026-06-14)** | File: `van-ban/tu-phap/nghi-dinh-154-2026-nd-cp-tiep-cong-dan.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218230`; người ký: Phó Thủ tướng Lê Thành Long (OCR gốc ghi nhầm "Lê Tiên Châu" đã sửa); hiệu lực 01/7/2026; 45 Điều, 10 Chương (I-X); 906 dòng, 89KB; OCR issues = 0 (PDF 1.4MB, 35 trang scanned) |
| 155/2026/NĐ-CP | 15/05/2026 | Sửa đổi, bổ sung NĐ 124/2020/NĐ-CP quy định chi tiết Luật Khiếu nại — bổ sung 7 trường hợp vụ việc khiếu nại phức tạp | Hành chính / Tư pháp | 218183 | **Đã có (2026-06-14)** | File: `van-ban/tu-phap/nghi-dinh-155-2026-nd-cp-sua-doi-luat-khieu-nai.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218183`; hiệu lực 01/7/2026; 23 Điều, 0 Chương; 654 dòng, 45KB; OCR issues = 0 |
| 156/2026/NĐ-CP | 15/05/2026 | Sửa đổi, bổ sung NĐ 31/2019/NĐ-CP quy định chi tiết Luật Tố cáo — quy định hành vi vi phạm trong giải quyết tố cáo bị buộc thôi việc | Hành chính / Tư pháp | 218102 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218102`; hiệu lực 01/7/2026 |
| 157/2026/NĐ-CP | — | Quy định thanh toán, quyết toán vốn ngân sách nhà nước để cấp bù lãi suất cho các ngân hàng thương mại thực hiện chính sách tín dụng ưu đãi của nhà nước | Tài chính / Tín dụng ưu đãi | 218158 | **Đã có (2026-06-14)** | File: `van-ban/tai-chinh/nghi-dinh-157-2026-nd-cp-cap-bu-lai-suat-tin-dung-uu-dai.md`; 10 Điều, 4 Mẫu biểu |

### Các văn bản phát hiện thêm (chưa tạo entry — chờ phiên sau)

- **158/2026/NĐ-CP** (Tư pháp / Tương trợ tư pháp) — chi tiết Luật Tương trợ tư pháp về dân sự; thay thế NĐ 92/2008/NĐ-CP; hiệu lực 01/7/2026; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218105`
- **159/2026/NĐ-CP** (Giáo dục / Lao động) — quy định giảng viên đồng cơ hữu trong trường cao đẳng, đại học công lập; hiệu lực 01/7/2026; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218164`
- **160/2026/NĐ-CP** (Tư pháp / Thi hành án) — cơ sở dữ liệu thi hành án hình sự; hiệu lực 01/7/2026; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218108`
- **163/2026/NĐ-CP** (Y tế) — chi tiết Luật Phòng, chống ma túy; giám sát điện tử trong cai nghiện; hiệu lực 01/7/2026; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218256`
- **164/2026/NĐ-CP** (Hành chính / Chống tham nhũng) — kiểm soát tài sản, thu nhập người giữ chức vụ; kê khai tài sản bắt đầu từ Trưởng phòng và tương đương; hiệu lực 01/7/2026; URL: `https://luatvietnam.vn/linh-vuc-khac/tu-01-7-2026-truong-phong-co-quan-nha-nuoc-co-phai-ke-khai-tai-san-khong-883-109358-article.html`
- **151/2026/NĐ-CP** (Tư pháp) — tổ chức và hoạt động của Văn phòng thi hành án dân sự, Thừa hành viên; hiệu lực 01/7/2026
- **152/2026/NĐ-CP** (Tư pháp) — chi tiết Luật Thi hành án dân sự; hiệu lực 01/7/2026

## Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-11)

| Số hiệu | Trong tracking? | Trạng thái |
|---|---|
| 153/2026/NĐ-CP | 14/05/2026 | Sửa đổi, bổ sung NĐ 01/2015/NĐ-CP | Hải quan / Thương mại | 218083 | Đã có | |
| 154/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có (45 Điều + 10 Chương)** (2026-06-14) |
| 155/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có (23 Điều + 0 Chương)** (2026-06-14) |
| 156/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có (11 Điều)** (2026-06-14) |
| 157/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có | **Đã có (10 Điều + 4 Mẫu biểu)** (2026-06-14) |

## Đề xuất ưu tiên phiên tiếp theo

1. **Hành chính / Tư pháp**: 154/2026/NĐ-CP, 155/2026/NĐ-CP, 156/2026/NĐ-CP — cùng nhóm tiếp công dân, khiếu nại, tố cáo; hiệu lực 01/7/2026; tác động toàn bộ hệ thống hành chính.
2. **Hải quan / Thương mại**: 153/2026/NĐ-CP — sửa đổi cơ chế phòng chống buôn lậu; hiệu lực 05/7/2026.
3. **Tài chính**: 157/2026/NĐ-CP — thanh toán lãi suất ưu đãi; tác động chính sách tín dụng ưu đãi nông nghiệp, xuất khẩu.
4. **Chống tham nhũng**: 164/2026/NĐ-CP — mở rộng kê khai tài sản; tác động rộng hệ thống công vụ.
5. **Tư pháp**: 151/2026/NĐ-CP, 152/2026/NĐ-CP, 158/2026/NĐ-CP, 160/2026/NĐ-CP — nhóm thi hành án, tương trợ tư pháp.

## Ghi chú xử lý

- 5 văn bản mới trong bảng chính sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **154/2026/NĐ-CP, 155/2026/NĐ-CP, 156/2026/NĐ-CP** (cùng nhóm hành chính-tư pháp; ảnh hưởng trực tiếp công dân và cơ quan nhà nước; hiệu lực 01/7/2026 — rất gần).
- 153/2026/NĐ-CP (hải quan) cũng cùng đợt hiệu lực 01/7–05/7.
- Dải 151–164: tổng cộng 14 NĐ-CP mới chưa được tracking đầy đủ (161–162, 165, 182, 185, 191, 192, 196, 199, 202 đã có; 163–164, 151–152, 158, 159, 160 cần bổ sung).
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, chinhphu.vn, baochinhphu.vn, congbao.chinhphu.vn.
- Ngày phát hiện: 2026-06-10 18:31 ICT
- Phiên thực hiện: agent:github-io:subagent:7620d9aa-4008-4fe5-a0b1-c8d873fb0314 (Đệ #1 Discovery 2026-06-10 cuối ngày)

---

# Báo cáo theo dõi pháp luật mới - 2026-05-14

## Mục đích

Ghi nhận các văn bản pháp luật mới phát hiện từ nguồn chính thức `vanban.chinhphu.vn` trong phiên crawl ngày 2026-05-14.

## Nguồn dữ liệu

- Trang hệ thống văn bản Chính phủ: `https://vanban.chinhphu.vn/he-thong-van-ban?classid=1&mode=1&maxresults=50`
- Thời điểm crawl: 2026-05-14 15:52 ICT
- Công cụ: Firecrawl Search + Firecrawl Scrape

## Văn bản mới đáng chú ý

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 148/2026/NĐ-CP | 12/05/2026 | Sửa đổi, bổ sung Nghị định 72/2015/NĐ-CP về quản lý hoạt động thông tin đối ngoại | Đối ngoại / thông tin | Đã có | `van-ban/ngoai-giao/nghi-dinh-148-2026-nd-cp-quan-ly-thong-tin-doi-ngoai.md`; heartbeat 2026-06-02 |
| 48/2026/TT-BCA | 12/05/2026 | Ban hành Quy chuẩn kỹ thuật quốc gia về thiết bị camera giám sát sử dụng giao thức Internet - yêu cầu an ninh mạng cơ bản | An ninh mạng | Đã có | `van-ban/an-ninh-quoc-gia/quy-chuan-camera-giam-sat-ip-an-ninh-mang.md`; heartbeat 2026-05-31 |
| 47/2026/TT-BCA | 12/05/2026 | Ban hành Quy chuẩn kỹ thuật quốc gia về an ninh mạng cho hệ thống thông tin lưu trữ tài liệu điện tử trong cơ quan Đảng, Nhà nước | An ninh mạng | Đã có | `van-ban/an-ninh-quoc-gia/quy-chuan-an-ninh-mang-he-thong-luu-tru-tai-lieu-dien-tu.md`; heartbeat 2026-05-31 |
| 47/2026/TT-BTC | 12/05/2026 | Quy định mẫu biểu báo cáo thông tin về nợ công và tính toán chỉ tiêu rủi ro danh mục nợ Chính phủ | Tài chính / nợ công | Đã có | `van-ban/tai-chinh/no-cong/mau-bieu-bao-cao-no-cong-47-2026-tt-btc.md`; heartbeat 2026-06-05 |
| 25/2026/TT-BCT | 11/05/2026 | Quy định quản lý chương trình, nhiệm vụ khoa học, công nghệ và đổi mới sáng tạo dùng ngân sách nhà nước của Bộ Công Thương | Khoa học công nghệ | Đã có | `van-ban/khoa-hoc-cong-nghe/thong-tu-25-2026-tt-bct-quan-ly-nhiem-vu-khoa-hoc-cong-nghe.md`; heartbeat 2026-06-06 |
| 129/2026/NĐ-CP | 06/04/2026 | Quy định về quản lý, sử dụng ngân sách nhà nước đối với một số hoạt động đối ngoại | Tài chính / Đối ngoại | Đã có | `van-ban/tai-chinh/ngan-sach-doi-ngoai/nghi-dinh-129-2026-nd-cp-quan-ly-ngan-sach-doi-ngoai.md`; heartbeat 2026-06-08; PDF OCR 13 trang |
| 23/2026/TT-BKHCN | 28/05/2026 | Quy định lập dự toán, quản lý, sử dụng và quyết toán kinh phí ngân sách nhà nước lĩnh vực KHCN&ĐMST&CDS cho hoạt động tiêu chuẩn, quy chuẩn kỹ thuật | Khoa học công nghệ | Đã có | `van-ban/khoa-hoc-cong-nghe/thong-tu-23-2026-tt-bkhcns-kinh-phi-tieu-chuan-quy-chuan.md`; heartbeat 2026-06-08; bản tóm tắt/cấu trúc lại từ pdftotext 32 trang; cần bổ sung toàn văn nếu dùng làm văn bản đầy đủ |
| 147/2026/NĐ-CP | 07/05/2026 | Hướng dẫn cơ chế, chính sách đặc thù tháo gỡ khó khăn cho các dự án tồn đọng, kéo dài theo Nghị quyết 29/2026/QH16 | Đầu tư / dự án tồn đọng | Đã có | `van-ban/dat-dai-dau-tu/nghi-dinh-147-2026-nd-cp-co-che-dac-thu-du-an-ton-dong.md`; heartbeat 2026-06-06 |
| 146/2026/NĐ-CP | 06/05/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực lâm nghiệp | Lâm nghiệp | Đã có | `van-ban/nong-nghiep-nong-thon/nghi-dinh-146-2026-nd-cp-xu-phat-vi-pham-linh-vuc-lam-nghiep.md`; heartbeat 2026-06-06 |
| 26/2026/NQ-CP | 06/05/2026 | Cơ chế đặc thù tháo gỡ khó khăn trong lấy mẫu, giám định, xác định danh tính hài cốt liệt sĩ bằng ADN | Chính sách xã hội | Đã có | `van-ban/chinh-sach-xa-hoi/nghi-quyet-26-2026-nq-cp-giam-dinh-adn-hai-cot-liet-si.md`; heartbeat 2026-06-04 |
| 03/2026/TT-BNG | 06/05/2026 | Phân cấp thẩm quyền chứng nhận lãnh sự, hợp pháp hóa lãnh sự cho UBND cấp tỉnh | Ngoại giao | Đã có | `van-ban/ngoai-giao/thong-tu-03-2026-tt-bng-phan-cap-tham-quyen-chung-nhan-lanh-su.md`; heartbeat 2026-06-09; PDF OCR 7 trang CAdES-BES; 11 Điều, 4 Chương |
| 192/2026/NĐ-CP | 30/05/2026 | Phụ cấp đặc thù y tế; hỗ trợ nhân viên y tế thôn, tổ dân phố và cô đỡ thôn, bản | Y tế | Đã có | `van-ban/y-te-duoc/nghi-dinh-192-2026-nd-cp-phu-cap-y-te-thon-ban.md`; heartbeat 2026-06-08; OCR 13 trang CAdES-BES; 416 dòng, 5 Chương 10 Điều |
| 68/2026/NĐ-CP | 05/03/2026 | Quy định về chính sách thuế và quản lý thuế đối với hộ kinh doanh, cá nhân kinh doanh | Thuế / hộ kinh doanh | Đã có | Phát hiện bởi heartbeat 2026-06-06; liên quan đến 141/2026/NĐ-CP |
| 37/2026/NĐ-CP | 23/01/2026 | Quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Chất lượng sản phẩm, hàng hóa | Chất lượng sản phẩm | Đã có | `van-ban/khoa-hoc-cong-nghe/nghi-dinh-37-2026-nd-cp-chat-luong-san-pham-hang-hoa.md`; heartbeat 2026-06-07; người ký Phó Thủ tướng Nguyễn Chí Dũng |
| 58/2026/NĐ-CP | 13/02/2026 | Sửa đổi, bổ sung một số điều của các nghị định liên quan đến quy định điều kiện về an ninh, trật tự đối với một số ngành, nghề đầu tư kinh doanh có điều kiện; quản lý và sử dụng con dấu; quản lý, sử dụng pháo | An ninh trật tự | Đã có | `van-ban/an-ninh-quoc-gia/nghi-dinh-58-2026-nd-cp-sua-doi-an-ninh-trat-tu.md`; heartbeat 2026-06-09; PDF OCR 90 trang
| 20/2026/NĐ-CP | 15/01/2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của Nghị quyết số 198/2025/QH15 về một số cơ chế, chính sách đặc biệt phát triển kinh tế tư nhân | Kinh tế tư nhân | Đã có | `van-ban/thuong-mai-dau-tu-chung-khoan/nghi-dinh-20-2026-nd-cp-co-che-dac-thu-phat-trien-kinh-te-tu-nhan.md`; heartbeat 2026-06-08; PDF OCR 23 trang |
| 145/2026/NĐ-CP | 05/05/2026 | Cơ chế quản lý tài chính, đánh giá, xếp loại doanh nghiệp đối với Sở GDCK Việt Nam, VSDC | Chứng khoán | Đã có | `van-ban/thuong-mai-dau-tu-chung-khoan/nghi-dinh-145-2026-nd-cp-co-che-quan-ly-tai-chinh-vnx-vsdc.md`; heartbeat 2026-06-06 |
| 144/2026/NĐ-CP | 05/05/2026 | Sửa đổi Nghị định 181/2025/NĐ-CP hướng dẫn Luật Thuế giá trị gia tăng | Thuế | Đã có | `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-144-2026-nd-cp-sua-doi-thue-gtgt.md`; heartbeat 2026-06-06 |
| 143/2026/NĐ-CP | 05/05/2026 | Biểu thuế nhập khẩu ưu đãi đặc biệt thực hiện Hiệp định CEPA Việt Nam - UAE giai đoạn 2026-2027 | Thuế / thương mại | Có liên quan | Đã có trang liên quan nhóm thuế xuất khẩu, thuế nhập khẩu; cần đối chiếu trước khi tạo mới |
| 24/2026/TT-BCT | 05/05/2026 | Quy tắc xuất xứ hàng hóa trong Hiệp định CEPA Việt Nam - UAE | Thương mại | Đã có | `van-ban/thuong-mai-dau-tu-chung-khoan/thong-tu-24-2026-tt-bct-quy-tac-xuat-xu-hang-hoa-cepa.md`; heartbeat 2026-06-04 |
| 22/2026/QĐ-TTg | 01/05/2026 | Sửa đổi chế độ bồi dưỡng giám định tư pháp | Tư pháp | Đã có | `van-ban/tu-phap/quyet-dinh-22-2026-qd-ttg-sua-doi-che-do-boi-duong-giam-dinh-tu-phap.md`; heartbeat 2026-06-04 |
| 142/2026/NĐ-CP | 30/04/2026 | Quy định chi tiết một số điều và biện pháp thi hành Luật Trí tuệ nhân tạo | Khoa học công nghệ | Đã có | Đã có trang chuyên biệt trong nhóm khoa học công nghệ |
| 21/2026/QĐ-TTg | 30/04/2026 | Danh mục công nghệ chiến lược và sản phẩm công nghệ chiến lược | Khoa học công nghệ | Đã có | `van-ban/khoa-hoc-cong-nghe/quyet-dinh-21-2026-qd-ttg-danh-muc-cong-nghe-chien-luoc.md`; heartbeat 2026-06-04 |
| 141/2026/NĐ-CP | 29/04/2026 | Sửa đổi chính sách thuế đối với hộ kinh doanh, cá nhân kinh doanh và hướng dẫn Luật Thuế TNDN | Thuế | Đã có | `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-141-2026-nd-cp-sua-doi-thue-ho-kinh-doanh.md`; heartbeat 2026-06-06 |
| 29/2026/QH16 | 24/04/2026 | Cơ chế đặc thù xử lý vi phạm đất đai trước Luật Đất đai 2024 và tháo gỡ dự án tồn đọng, kéo dài | Đất đai / đầu tư | Đã có | `van-ban/dat-dai-dau-tu/nghi-quyet-29-2026-qh16-co-che-dac-thu-dat-dai-du-an-ton-dong.md`; heartbeat 2026-06-04 |
| 66.17/2026/NQ-CP | 15/05/2026 | Cắt giảm, sửa đổi ngành nghề đầu tư kinh doanh có điều kiện — cắt giảm 64 ngành, sửa đổi 23 ngành (hiệu lực 01/07/2026-28/02/2027) | Đa ngành / Cải cách | **Đã có** | `van-ban/da-nganh/nghi-quyet-66-17-2026-nq-cat-giam-nganh-nghe-dau-tu-kinh-doanh.md`; heartbeat 2026-06-10; OCR CAdES-BES 9 trang; 260 dòng, 17KB, 142 ngành nghề phụ lục |
| 66.18/2026/NQ-CP | 18/05/2026 | Phân quyền, cắt giảm, đơn giản hóa TTHC và điều kiện kinh doanh — 11 bộ, ngành; 45 Luật/72 NĐ/34 TT; giảm 23 nghìn tỷ/năm (hiệu lực 01/07/2026) | Đa ngành / Cải cách | **Đã có** | `van-ban/da-nganh/nghi-quyet-66-18-2026-nq-cat-giam-tthc-11-bo.md`; heartbeat 2026-06-10; OCR 12 phụ lục CAdES-BES; 24KB, 7 Điều, 151 văn bản đề xuất sửa đổi |
| 66.19/2026/NQ-CP | 18/05/2026 | Cắt giảm, đơn giản hóa TTHC — Bộ Nông nghiệp và Môi trường; phân bón 10 năm, thuốc BVTV 10 năm, bãi bỏ TTHC khảo nghiệm giống | Nông nghiệp / Cải cách | **Đã có** | `van-ban/da-nganh/nghi-quyet-66-19-2026-nq-cat-giam-tthc-bo-nong-nghiep.md`; heartbeat 2026-06-10; OCR CAdES-BES; 18KB, 237 dòng, 6 Điều + 11 phụ lục; docid 218168 |

## Đối chiếu nhanh với `van-ban/`

Đã có trang liên quan:

- `van-ban/khoa-hoc-cong-nghe/nghi-dinh-142-2026-nd-cp-huong-dan-luat-tri-tue-nhan-tao.md`
- `van-ban/cong-nghiep/hoa-chat.md`
- `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-xuat-khau-thue-nhap-khau.md`

Chưa thấy trang chuyên biệt cho các văn bản mới sau (heartbeat 2026-06-06):

- 50/2026/NĐ-CP và 49/2026/NĐ-CP về tiền sử dụng đất, tiền thuê đất / hướng dẫn NQ 254
- 129/2026/NĐ-CP về ngân sách cho hoạt động đối ngoại — đã có trang chuyên biệt trong PR heartbeat 2026-06-08
- 23/2026/TT-BKHCN về dự toán kinh phí tiêu chuẩn/quy chuẩn kỹ thuật — đã có trang tóm tắt/cấu trúc lại trong PR heartbeat 2026-06-08
- 58/2026/NĐ-CP (đang chờ crawl chi tiết); 20/2026/NĐ-CP đã có trang trong PR heartbeat 2026-06-08; 37/2026/NĐ-CP đã hoàn thiện 2026-06-07
- 03/2026/TT-BNG phân cấp chứng nhận lãnh sự

## Đề xuất ưu tiên cập nhật tiếp theo

1. **Đất đai**: 50/2026/NĐ-CP và 49/2026/NĐ-CP — cặp NĐ hướng dẫn NQ 254/QH15 về tiền sử dụng đất, tiền thuê đất, có hiệu lực rộng.
2. **Tài chính / Đối ngoại**: 129/2026/NĐ-CP — quản lý ngân sách cho hoạt động đối ngoại.
3. **Khoa học công nghệ**: 23/2026/TT-BKHCN — quy định dự toán kinh phí cho tiêu chuẩn/quy chuẩn kỹ thuật.
4. **Thuế / thương mại**: 143/2026/NĐ-CP, 144/2026/NĐ-CP, 141/2026/NĐ-CP, 68/2026/NĐ-CP vì có tác động rộng tới kinh doanh.
5. **Đất đai / dự án tồn đọng**: 147/2026/NĐ-CP vì là cơ chế đặc thù mới.
6. **Chứng khoán**: 145/2026/NĐ-CP nếu mở rộng nhóm tài chính - chứng khoán.

## Cách sử dụng

- Dùng báo cáo này làm backlog cho heartbeat `Legislation Backlog Ingestion` trong `HEARTBEAT.md`.
- Không để `track-legislation` hoặc `check-new-laws` quá hạn mà chỉ ghi nhận trạng thái; nếu quá hạn từ 7 ngày trở lên phải xử lý item ưu tiên cao nhất ngay.
- Khi tạo nội dung mới, mỗi nhóm văn bản nên đi một branch/PR riêng.
- Nguồn crawl ưu tiên vẫn là `vanban.chinhphu.vn` và PDF đính kèm từ `datafiles.chinhphu.vn`.

## Troubleshooting

- `web_search` Brave đang có lúc chuyển provider sang MiniMax và lỗi thiếu API key; fallback dùng `firecrawl_search`.
- Trang danh sách `vanban.chinhphu.vn` nhiều nội dung nhiễu; cần parse phần bảng `TẤT CẢ VĂN BẢN`.
- Không dùng `vbpl.vn`, `luatvietnam.vn`, `thuvienphapluat.vn` làm nguồn chính vì WAF/Cloudflare/login wall.

---

# Cập nhật 2026-06-07 (phiên Đệ #1 Discovery)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

Phát hiện 14 văn bản mới qua web search Brave + Gemini trong 14 nhóm chủ đề (Thuế, Đất đai, KHCN, Lâm nghiệp, Chứng khoán, Giáo dục, Y tế, Lao động, Tài nguyên, Môi trường, Giao thông, Xây dựng, Tài chính, Ngân hàng). Phiên này ưu tiên 5 văn bản tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 161/2026/NĐ-CP | 15/05/2026 | Quy định mức lương cơ sở 2.530.000 đ/tháng từ 01/7/2026 đối với cán bộ, công chức, viên chức và lực lượng vũ trang | Lao động / Tiền lương | Đã có | `van-ban/lao-dong/nghi-dinh-161-2026.md`; heartbeat 2026-06-07 Đệ #3; PDF đã OCR bằng Signed PDF OCR Pipeline (CAdES-BES); người ký Phạm Thị Thanh Trà (Phó Thủ tướng, ký thay Thủ tướng); URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218107` |
| 182/2026/NĐ-CP | 23/05/2026 | Quy định chế độ phụ cấp ưu đãi theo nghề đối với nhà giáo, cán bộ QLGD và nhân sự hỗ trợ GD công tác tại cơ sở GD công lập (hiệu lực 07/7/2026; mức phụ cấp áp dụng từ 01/01/2026) | Giáo dục | **Đã có** | `van-ban/giao-duc-dao-tao/nghi-dinh-182-2026-nd-cp-quy-dinh-che-do-phu-cap-uu-dai-doi-voi-nha-giao-can-bo-quan-ly-giao-duc.md`; heartbeat 2026-06-08; docid 218228 |
| 165/2026/NĐ-CP | 15/05/2026 | Quy định chi tiết và hướng dẫn thi hành Luật Phòng bệnh (chuyển đổi mạnh từ "chữa bệnh" sang "phòng bệnh chủ động") | Y tế | Đã có | `van-ban/y-te-duoc/nghi-dinh-165-2026-nd-cp-phong-benh.md`; heartbeat 2026-06-08; OCR 38 trang CAdES-BES; 1509 dòng, 5 Chương |

### Văn bản phát hiện thêm (chưa đưa vào backlog ưu tiên, chờ phiên sau)

- 54/2026/NĐ-CP (Xây dựng) — sửa đổi NĐ về nhà ở, kinh doanh BĐS — URL: `https://vanban.chinhphu.vn/?docid=216924&pageid=27160`
- 91/2026/NĐ-CP (Giáo dục) — chi tiết Luật Giáo dục đại học 2026
- 88/2026/NĐ-CP (Giáo dục) — quản lý dữ liệu giáo dục và đào tạo
- 93/2026/NĐ-CP (Giáo dục) — chi tiết Luật Nhà giáo
- 95/2026/NĐ-CP (Giáo dục) — chi tiết Luật GD nghề nghiệp
- 66/2026/NĐ-CP (Giáo dục) — chi tiết Luật Giáo dục
- 105/2026/NĐ-CP (Lao động) — Luật Công đoàn về tài chính công đoàn
- 07/2026/NĐ-CP (Lao động) — sửa đổi chế độ tiền lương CBCCVC
- 20/2026/TT-BTC (Tài chính) — chi tiết Luật Thuế TNDN và NĐ 320/2025 — URL: `https://vanban.chinhphu.vn/?docid=217191&pageid=27160`
- 19/2026/QH16 (Thuế) — thuế BVMT, GTGT, TTĐB đối với xăng dầu, nhiên liệu bay — URL: `https://vanban.chinhphu.vn/?classid=1&docid=218005&orggroupid=1&pageid=27160`

## Văn bản phát hiện thêm (chưa đưa vào backlog ưu tiên, chờ phiên sau)

- 54/2026/NĐ-CP (Xây dựng) — sửa đổi NĐ về nhà ở, kinh doanh BĐS — URL: `https://vanban.chinhphu.vn/?docid=216924&pageid=27160`
- 91/2026/NĐ-CP (Giáo dục) — chi tiết Luật Giáo dục đại học 2026
- 88/2026/NĐ-CP (Giáo dục) — quản lý dữ liệu giáo dục và đào tạo
- 93/2026/NĐ-CP (Giáo dục) — chi tiết Luật Nhà giáo
- 95/2026/NĐ-CP (Giáo dục) — chi tiết Luật GD nghề nghiệp
- 66/2026/NĐ-CP (Giáo dục) — chi tiết Luật Giáo dục
- 105/2026/NĐ-CP (Lao động) — Luật Công đoàn về tài chính công đoàn
- 07/2026/NĐ-CP (Lao động) — sửa đổi chế độ tiền lương CBCCVC
- 20/2026/TT-BTC (Tài chính) — chi tiết Luật Thuế TNDN và NĐ 320/2025 — URL: `https://vanban.chinhphu.vn/?docid=217191&pageid=27160`
- 19/2026/QH16 (Thuế) — thuế BVMT, GTGT, TTĐB đối với xăng dầu, nhiên liệu bay — URL: `https://vanban.chinhphu.vn/?classid=1&docid=218005&orggroupid=1&pageid=27160`

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — 4 nhóm ưu tiên)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-07) và `van-ban/` xác nhận: 162/2026/NĐ-CP đã có file. Phiên này phát hiện và thêm 4 văn bản mới chưa từng được ghi nhận, ưu tiên tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 13/2026/TT-BNV | 29/05/2026 | Hướng dẫn thực hiện mức lương cơ sở 2.530.000 đ/tháng đối với 9 nhóm đối tượng hưởng lương, phụ cấp trong cơ quan, tổ chức, đơn vị sự nghiệp công lập của Đảng, Nhà nước, Mặt trận Tổ quốc, tổ chức chính trị - xã hội (hiệu lực 01/7/2026) | Lao động / Tiền lương | Đã có | `van-ban/lao-dong/thong-tu-13-2026-tt-bnv-huong-dan-luong-co-so.md`; heartbeat 2026-06-08; pdftotext 5 trang |
| 91/2026/NĐ-CP | 2026 | Quy định chi tiết một số điều của Luật Giáo dục đại học (sửa đổi 2026) | Giáo dục | Đã có | `van-ban/giao-duc-dao-tao/nghi-dinh-91-2026-nd-cp-chi-tiet-luat-giao-duc-dai-hoc.md`; heartbeat 2026-06-08; OCR PDF 24 trang CAdES-BES |
| 14/2026/TT-BNV | 29/05/2026 | Quy định chi tiết việc điều chỉnh lương hưu, trợ cấp BHXH và trợ cấp hằng tháng (hiệu lực 01/7/2026) | Lao động / BHXH | **Đã có** | `van-ban/lao-dong/thong-tu-14-2026-tt-bnv-dieu-chinh-luong-huu-tro-cap-bhxh.md`; heartbeat 2026-06-08; web scraping 5 Điều + phụ lục; thay thế TT 06/2023/TT-BLĐTBXH; tăng 8% + hỗ trợ nhóm thấp |
| 105/2026/NĐ-CP | 31/03/2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Công đoàn về tài chính công đoàn | Lao động / Công đoàn | Đã có | `van-ban/lao-dong/nghi-dinh-105-2026-nd-cp-tai-chinh-cong-doan.md`; heartbeat 2026-06-08; OCR 16 trang CAdES-BES; 363 dòng, 6 Chương 18 Điều; thay thế NĐ 191/2013/NĐ-CP |
| 03/2026/TT-BTC | 01/01/2026 | Sửa đổi, bổ sung TT 56/2022 về cơ chế tự chủ tài chính đơn vị sự nghiệp công lập | Tài chính | Đã có | `van-ban/tai-chinh-ngan-sach/thong-tu-03-2026-tt-btc-co-che-tu-chu-tai-chinh.md`; heartbeat 2026-06-08; OCR 4 trang; 140 dòng, 12 Điều; sửa TT 56/2022 |
| 25/2026/NQ-CP | 01/05/2026 | Kéo dài thời hạn áp dụng NĐ 72/2026/NĐ-CP về thuế nhập khẩu ưu đãi 0% đối với nguyên liệu sản xuất xăng dầu | Thuế | Đã có | `van-ban/thue-phi-le-phi/nghi-quyet-25-2026-nq-cp-thue-xang-dau.md`; heartbeat 2026-06-08; OCR 2 trang CAdES-BES; 81 dòng; hiệu lực 01/05/2026 → 30/06/2026 |
| 19/2026/TT-BNNMT | 30/03/2026 | Quy định kỹ thuật lồng ghép đo đạc bản đồ địa chính, đăng ký đất đai, hồ sơ địa chính và CSDL quốc gia về đất đai | Đất đai | Đã có | `van-ban/tai-nguyen-moi-truong/thong-tu-19-2026-tt-bnnmt-do-dac-ban-do-dia-chinh.md`; heartbeat 2026-06-08; OCR 15 trang CAdES-BES; 432 dòng; ban hành 30/03/2026 |
| 19/2026/QH16 | 12/04/2026 | Sửa đổi quy định về thuế bảo vệ môi trường, thuế giá trị gia tăng, thuế tiêu thụ đặc biệt đối với xăng dầu, nhiên liệu bay | Thuế | Đã có | `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-quyet-19-2026-qh16-sua-doi-thue-xang-dau.md`; heartbeat 2026-06-08; OCR 2 trang scanned PDF; hiệu lực 16/4-30/6/2026 |
| 07/2026/NĐ-CP | 10/01/2026 | Sửa đổi chế độ tiền lương đối với cán bộ, công chức, viên chức | Lao động / Tiền lương | Đã có | `van-ban/lao-dong/nghi-dinh-07-2026-nd-cp-sua-doi-che-do-tien-luong-cbccvc.md`; heartbeat 2026-06-08; OCR 5 trang CAdES-BES |
| 88/2026/NĐ-CP | 28/03/2026 | Quy định quản lý dữ liệu giáo dục và đào tạo | Giáo dục | Đã có | `van-ban/giao-duc-dao-tao/nghi-dinh-88-2026-nd-cp-quan-ly-du-lieu-giao-duc.md`; heartbeat 2026-06-08; OCR 15 trang CAdES-BES |
| 93/2026/NĐ-CP | 31/03/2026 | Quy định chi tiết một số điều của Luật Nhà giáo | Giáo dục | Đã có | `van-ban/giao-duc-dao-tao/nghi-dinh-93-2026-nd-cp-chi-tiet-luat-nha-giao.md`; heartbeat 2026-06-08; web crawl (PDF 404); 21KB, 8 chương 28 điều |
| 95/2026/NĐ-CP | 2026 | Quy định chi tiết một số điều của Luật Giáo dục nghề nghiệp | Giáo dục | Đã có | `van-ban/giao-duc-dao-tao/nghi-dinh-95-2026-nd-cp-chi-tiet-luat-giao-duc-nghe-nghiep.md`; heartbeat 2026-06-08; pdftotext 12 trang; 18KB, 5 chương 20 điều |
| 66/2026/NĐ-CP | 02/03/2026 | Quy định chi tiết một số điều của Luật Giáo dục | Giáo dục | Đã có | `van-ban/giao-duc-dao-tao/nghi-dinh-66-2026-nd-cp-chi-tiet-luat-giao-duc.md`; heartbeat 2026-06-08; OCR 30 trang CAdES-BES; 60KB, 15 Điều, thay thế NĐ 84/2020 |
| 54/2026/NĐ-CP | 09/02/2026 | Sửa đổi, bổ sung một số điều của các nghị định về nhà ở, kinh doanh bất động sản | Xây dựng | Đã có | `van-ban/xay-dung/nghi-dinh-54-2026-nd-cp-sua-doi-nha-o-kinh-doanh-bds.md`; heartbeat 2026-06-08; OCR 22 trang CAdES-BES; 43 Điều, 6 Chương, sửa 6 NĐ (96/2024, 95/2024, 98/2024, 100/2024, 140/2025, 144/2025) |

### Cập nhật trạng thái từ "Chưa có" → "Đã có"

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái mới | Ghi chú |
|---|---:|---|---|---|---|
| 162/2026/NĐ-CP | 15/05/2026 | Điều chỉnh lương hưu, trợ cấp BHXH và trợ cấp hằng tháng (hiệu lực 01/7/2026) | Lao động / BHXH | **Đã có** | `van-ban/lao-dong/nghi-dinh-162-2026-nd-cp-dieu-chinh-luong-huu-tro-cap-bhxh-tro-cap-hang-thang.md`; đầy đủ toàn văn 6 Điều / 2 Chương; file 17+ KB; đã OCR và đối chiếu chéo |

## File trong `van-ban/` cần refactor (bổ sung từ phiên 2026-06-09)

### Nhóm C: File thuộc 4 nhóm ưu tiên — stub cần ưu tiên crawl khi xử lý nhóm

| File | Nhóm | Lastedit | Size | Vấn đề |
|---|---|---:|---:|---|
| `van-ban/giao-duc-dao-tao/giao-duc.md` | Giáo dục | 2026-05-13 | >200 KB | **Index tổng hợp** — nội dung 200+ KB tổng hợp nhiều NĐ cũ; KHÔNG có trạng thái "Đang cập nhật" nhưng lastedit 2026-05-13 cho thấy chưa cập nhật các NĐ-CP 2026 mới (91/66/88/93/95); cần xác minh xem 182/2026/NĐ-CP đã được tích hợp vào index chưa |
| `van-ban/giao-duc-dao-tao/giao-duc-dai-hoc.md` | Giáo dục | — | — | Stub tổng hợp — chưa có trang chuyên biệt cho Luật GD đại học sửa đổi 2026 và 91/2026/NĐ-CP mới |
| `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md` | Thuế | 2026-05-29 | 5793 B | Stub thiếu nội dung — 19/2026/QH16 sửa đổi thuế liên quan tài nguyên (xăng dầu) cần tích hợp khi crawl mới |
| `van-ban/tai-chinh/gia.md` | Tài chính | 2026-05-29 | ~10 KB | Stub thiếu — chỉ tổng hợp Luật Giá 16/2023/QH15 (75 Điều), chưa có NĐ hướng dẫn mới |
| `van-ban/lao-dong/lao-dong.md` | Lao động | — | — | Index tổng hợp — cần xác minh đã tích hợp 13/2026/TT-BNV, 14/2026/TT-BNV, 07/2026/NĐ-CP chưa |

### File thuộc nhóm B cũ — cần refactor (nhắc lại từ phiên 2026-06-07)

| File | Lastedit | Size | Ghi chú |
|---|---|---:|---|
| `van-ban/cong-nghiep/quan-ly-phan-bon.md` | 2026-05-13 | 8570 B | Stub thiếu nội dung |
| `van-ban/ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu...sang-tieng-anh-de-giao-dich-doi-ngoai.md` | 2026-05-15 | 4876 B | Stub rất ngắn |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md` | 2026-05-26 | 3183 B | Stub rất ngắn |
| `van-ban/thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/index.md` | 2026-05-28 | 2875 B | Index trống |
| `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md` | 2026-05-29 | 5793 B | Stub thiếu nội dung |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md` | 2026-05-29 | 7115 B | Stub thiếu nội dung |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/theo-doi-tinh-hinh-thi-hanh-phap-luat.md` | 2026-05-29 | 7399 B | Stub thiếu nội dung |

## Đối chiếu nhanh với `van-ban/` (phiên 2026-06-09)

**Đã xác nhận:**
- `van-ban/lao-dong/nghi-dinh-162-2026-nd-cp-dieu-chinh-luong-huu-tro-cap-bhxh-tro-cap-hang-thang.md` — file tồn tại, nội dung đầy đủ → chuyển 162/2026/NĐ-CP sang "Đã có"
- `van-ban/giao-duc-dao-tao/nghi-dinh-182-2026-nd-cp-quy-dinh-che-do-phu-cap-uu-dai-doi-voi-nha-giao-can-bo-quan-ly-giao-duc.md` — file tồn tại → 182/2026/NĐ-CP đã đúng trạng thái "Đã có"
- `van-ban/lao-dong/nghi-dinh-161-2026.md` — file tồn tại → 161/2026/NĐ-CP đã đúng trạng thái "Đã có"

**Chưa có file chuyên biệt (cần tạo mới):**
- 13/2026/TT-BNV — hướng dẫn lương cơ sở (Lao động)
- 14/2026/TT-BNV — hướng dẫn lương hưu (Lao động)
- 91/2026/NĐ-CP — chi tiết Luật GD đại học 2026 (Giáo dục)
- 19/2026/QH16 — sửa thuế xăng dầu, nhiên liệu bay (Thuế)
- 07/2026/NĐ-CP — sửa đổi tiền lương CBCCVC (Lao động)

**Cần refactor index (đánh dấu ưu tiên):**
- `van-ban/giao-duc-dao-tao/giao-duc.md` — chưa tích hợp 182/2026 và chưa chuẩn bị 91/66/88/93/95
- `van-ban/giao-duc-dao-tao/giao-duc-dai-hoc.md` — stub chưa có NĐ-CP 2026
- `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md` — stub nhỏ cần bổ sung 19/2026/QH16
- `van-ban/tai-chinh/gia.md` — stub cần hướng dẫn Luật Giá mới
- `van-ban/lao-dong/lao-dong.md` — cần tích hợp 13/2026, 14/2026, 07/2026

## Đề xuất ưu tiên phiên tiếp theo

1. **Lao động**: 13/2026/TT-BNV và 14/2026/TT-BNV — hướng dẫn chi tiết cho cặp NĐ 161+162, có hiệu lực 01/7/2026 — ưu tiên cao nhất vì thời gian thực thi gần.
2. **Giáo dục**: 91/2026/NĐ-CP (chi tiết Luật GD đại học) — tác động hệ thống ĐH cả nước.
3. **Thuế**: 19/2026/QH16 — sửa thuế xăng dầu, nhiên liệu bay; tác động rộng ngành năng lượng, hàng không.
4. **Lao động**: 07/2026/NĐ-CP — sửa đổi tiền lương CBCCVC; bổ sung sau 13/2026/TT-BNV và 14/2026/TT-BNV.
5. **Giáo dục**: Refactor index `giao-duc.md` sau khi đã có đủ NĐ-CP 2026.
6. **Thuế**: Refactor `thue-tai-nguyen.md` sau khi crawl 19/2026/QH16 xong.

## Ghi chú xử lý

- 5 văn bản mới (13/TT-BNV, 14/TT-BNV, 91/NĐ-CP, 19/QH16, 07/NĐ-CP) sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- File refactor nhóm C (5 file thuộc 4 nhóm ưu tiên) cần ưu tiên xử lý khi đã có nội dung văn bản mới để tích hợp.
- File refactor nhóm B (7 file từ phiên 2026-06-07) giữ nguyên ưu tiên thấp hơn nhóm C.
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, chinhphu.vn, laodong.vn.
- Ngày phát hiện: 2026-06-09 05:31 ICT
- Phiên thực hiện: agent:github-io:subagent:f18c30f5-b5a0-43d0-85e8-6fb153782f83 (Đệ #1 Discovery 2026-06-09)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 2)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên trước): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất (NĐ-CP, NQ-QH16, TT liên tịch):

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 46/2026/NĐ-CP | 26/01/2026 | Quy định chi tiết thi hành một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật An toàn thực phẩm (tạm ngưng đến 16/04/2026 theo NQ 09/2026/NQ-CP) | Y tế / An toàn thực phẩm | Đã có | `van-ban/y-te-duoc/nghi-dinh-46-2026-nd-cp-an-toan-thuc-pham.md`; heartbeat 2026-06-09; PDF OCR 50 trang CAdES-BES; 55 Điều, 11 Chương |
| 31/2026/QH16 | 24/04/2026 | Kỳ họp thứ Nhất, Quốc hội khóa XVI — thông qua 09 luật và 05 nghị quyết quy phạm pháp luật (hiệu lực từ 01/07/2026) | Đa ngành | **Đã có** | `van-ban/da-nganh/nghi-quyet-31-2026-qh16-ky-hop-thu-nhat.md`; heartbeat 2026-06-09; tổng hợp từ luatvietnam.vn + baochinhphu.vn; 09 luật chi tiết |
| 27/2026/QH16 | 24/04/2026 | Kế hoạch đầu tư công trung hạn giai đoạn 2026-2030, tổng vốn 8.220.000 tỷ đồng | Tài chính / Đầu tư | **Đã có** | `van-ban/tai-chinh-ngan-sach/nghi-quyet-27-2026-qh16-ke-hoach-dau-tu-cong-trung-han.md`; heartbeat 2026-06-09; OCR từ thuvienphapluat.vn/luatvietnam.vn |
| 26/2026/TT-BTC | 2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của NĐ 73/2026/NĐ-CP về Luật Ngân sách nhà nước | Tài chính / Ngân sách | **Đã có** | `van-ban/tai-chinh/thong-tu-26-2026-tt-btc-nguon-ngan-sach.md`; heartbeat 2026-06-10; ban dau can review; docid 217323 |
| 04/2026/TT-NHNN | 31/03/2026 | Hướng dẫn một số nội dung về hoạt động bảo hiểm tiền gửi (hiệu lực 01/05/2026) | Ngân hàng | **Đã có** | `van-ban/ngan-hang/thong-tu-04-2026-tt-nhnn-bao-hiem-tien-gui.md`; heartbeat 2026-06-09; OCR từ thuvienphapluat.vn/luatvietnam.vn |

### Văn bản phát hiện thêm (chờ phiên sau)

- 06/2026/NĐ-CP — Quy định về tổ chức và hoạt động của Ngân hàng Chính sách xã hội (URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216603`); heartbeat 2026-06-09 Đệ #3; PDF OCR 24 trang; `van-ban/tai-chinh-ngan-sach/nghi-dinh-06-2026-nd-cp-ngan-hanh-chinh-sa-xa-hoi.md`
- 55/2026/NĐ-CP — Sửa đổi xử phạt hành chính lĩnh vực tài sản công, tiết kiệm chống lãng phí (URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216927`)
- 75/2026/NĐ-CP — Quy định chế độ tự chủ, tự chịu trách nhiệm về quản lý sử dụng kinh phí quản lý hành chính (URL: `https://vanban.chinhphu.vn/?docid=217217&pageid=27160`)
- 28/2026/TT-BCA — Quy định về phát ngôn và cung cấp thông tin cho báo chí của Công an nhân dân (hiệu lực 12/05/2026)
- 08/2026/TT-BYT — Hướng dẫn giám định tư pháp trong lĩnh vực y tế (hiệu lực 01/05/2026)

---

## Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — phiên mới 05:35)

So sánh với `documents/LEGISLATION_TRACKING.md` (phiên trước): phát hiện 4 văn bản mới chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 4.

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 202/2026/NĐ-CP | 08/06/2026 | Sửa đổi, bổ sung NĐ 10/2022/NĐ-CP về lệ phí trước bạ — ô tô điện chạy pin được áp dụng lệ phí trước bạ lần đầu 0% đến hết năm 2030 | Tài chính / Ô tô điện | **Đã có** | `van-ban/tai-chinh/nghi-dinh-202-2026-nd-cp-o-to-dien-le-phi-truoc-ba.md`; heartbeat 2026-06-10; docid chưa index; web crawl 2 nguồn (baochinhphu + luatvietnam); 5.2KB, 3 Điều |
| 191/2026/NĐ-CP | 29/05/2026 | Quy chế làm việc của Chính phủ — 8 nguyên tắc làm việc, thay thế NĐ 39/2022/NĐ-CP | Hành chính / Tổ chức bộ máy | **Đã có** | `van-ban/hanh-chinh-tu-phap/nghi-dinh-191-2026-nd-cp-quy-che-lam-viec-chinh-phu.md`; heartbeat 2026-06-10; PDF 404 trên datafiles; web crawl 4 nguồn; 25.5KB, 28 Điều, 8 Chương; docid 218297 |
| 40/2026/TT-BGDĐT | 15/05/2026 | Quy định về công tác sinh viên tại các cơ sở giáo dục đại học, cao đẳng, trung cấp — đánh giá kết quả rèn luyện theo thang điểm 100, 5 mức: xuất sắc/tốt/khá/trung bình/yếu (hiệu lực 30/6/2026) | Giáo dục | **Đã có** | `van-ban/giao-duc-dao-tao/thong-tu-40-2026-tt-bgd-dt-cong-tac-sinh-vien.md`; heartbeat 2026-06-10; PDF thường 18 trang; 39KB, 456 dòng, 32 Điều/4 Chương |
| 141/2026/NQ-CP | 01/06/2026 | Chính phủ thông qua chính sách của dự án Luật sửa đổi, bổ sung một số điều của Luật Thương mại, Luật Cạnh tranh, Luật Quản lý ngoại thương, Luật Bảo vệ quyền lợi người tiêu dùng (phân công Phó Thủ tướng Phạm Gia Túc chỉ đạo xây dựng) | Thương mại / Đa ngành | **Đã có** | `van-ban/da-nganh/nghi-quyet-141-nq-cp-4-luat-thuong-mai.md`; heartbeat 2026-06-10; 6.7KB, 2 chính sách, web crawl 4 nguồn; docid 218308 |
| 28/2026/TT-BCT | 01/06/2026 | Ban hành Danh mục các mặt hàng nhập khẩu (kèm mã HS) thực hiện kiểm tra nhà nước về an toàn thực phẩm thuộc trách nhiệm quản lý của Bộ Công Thương | Thương mại / ATTP | **Đã có** | `van-ban/thuong-mai-dau-tu-chung-khoan/thong-tu-28-2026-tt-bct-attp-nhap-khau.md`; heartbeat 2026-06-10; image-based PDF OCR; 44KB, 800 dòng, 5 nhóm hàng HS |

### Đối chiếu nhanh — văn bản đã có trong tracking (không trùng lặp)

- **202/2026/NĐ-CP** — chưa có trong file → thêm mới
- **40/2026/TT-BGDĐT** — chưa có trong file → thêm mới
- **141/2026/NQ-CP** — chưa có trong file → thêm mới
- **28/2026/TT-BCT** — chưa có trong file → thêm mới

### Các văn bản phát hiện khác (chưa tạo entry, chờ phiên sau)

- **36/2026/TT-BTC** (Tài chính) — hướng dẫn quản lý chi phí quy hoạch, hiệu lực 31/03/2026 — cần kiểm tra đã tracking chưa
- **40/2026/TT-BTC** (Tài chính) — miễn phí/lệ phí giao thông vận tải, hiệu lực 07/04–30/06/2026 — cần kiểm tra đã tracking chưa
- **Văn bản hợp nhất 13/VBHN-BTC** (Chứng khoán) — hướng dẫn giám sát giao dịch chứng khoán — cần kiểm tra đã tracking chưa

## Ghi chú xử lý

- 4 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **202/2026/NĐ-CP** (ô tô điện 0% lệ phí trước bạ) — tác động trực tiếp đến người tiêu dùng và nhà sản xuất.
- Thứ tự ưu tiên tiếp theo: 40/2026/TT-BGDĐT (công tác sinh viên) → 141/2026/NQ-CP (4 luật thương mại) → 28/2026/TT-BCT (ATTP nhập khẩu).
- Cần xác minh docid trên vanban.chinhphu.vn cho 4 văn bản mới (URL hiện tại để placeholder `XXXXX`).
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, chinhphu.vn, xaydungchinhsach, luatvietnam.
- Ngày phát hiện: 2026-06-09 05:35 ICT
- Phiên thực hiện: agent:github-io:subagent:cbace73b-aa79-4e5f-92f6-44b08e9e48a9 (Đệ #1 Discovery 2026-06-09 phiên mới)

## Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong phiên Đệ #3 Full Content Crawler tiếp theo.
- Ưu tiên cao: 31/2026/QH16 (luật mới) và 27/2026/QH16 (đầu tư công trung hạn) vì tác động nền kinh tế rộng nhất. **27/2026/QH16 đã hoàn thành 2026-06-09.**
- 46/2026/NĐ-CP quan trọng vì hướng dẫn Luật ATTP mới, ảnh hưởng toàn ngành thực phẩm.
- 04/2026/TT-NHNN liên quan trực tiếp đến hệ thống ngân hàng và BHTG.
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn.
- Ngày phát hiện: 2026-06-09 04:31 ICT
- Phiên thực hiện: agent:github-io:subagent:d7797d86-b02a-49ba-b621-98a02e5d9869 (Đệ #1 Discovery 2026-06-09 lần 2)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 3)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 2): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất (NĐ-CP, TT Bộ), loại trừ các văn bản đã có trong tracking:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | URL | Trạng thái |
|---|---:|---|---|---:|---|---|
| 05/2026/TT-BKHCN | 10/03/2026 | Khung đạo đức trí tuệ nhân tạo quốc gia — quy định 5 nguyên tắc (an toàn, tôn trọng quyền con người, công bằng, bền vững, đổi mới sáng tạo) và yêu cầu về thiết kế, kiểm thử, bảo vệ an ninh hệ thống AI | Khoa học công nghệ | 217165 | `https://vanban.chinhphu.vn/?pageid=27160&docid=217165` | **Đã có** | `van-ban/khoa-hoc/thong-tu-05-2026-tt-bk-hcn.md`; heartbeat 2026-06-10 |
| 04/2026/TT-BKHCN | 27/02/2026 | Sửa đổi, bổ sung, bãi bỏ một số điều văn bản về tiêu chuẩn đo lường chất lượng — cập nhật danh mục phương tiện đo nhóm 2 (taximet, cân, đồng hồ đo nước/khí, công tơ điện, thiết bị đo nồng độ cồn…) | Khoa học công nghệ | 217125 | `https://vanban.chinhphu.vn/?pageid=27160&docid=217125` | **Đã có (2026-06-14)** | File: `van-ban/khoa-hoc-cong-nghe/thong-tu-04-2026-tt-bkhcn-sua-doi-tieu-chuan-do-luong.md`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/2/04-bkhcn.signed.pdf`; người ký: Bộ trưởng Nguyễn Mạnh Hùng; hiệu lực chính 15/4/2026, Điều 2 hết hiệu lực 01/6/2026; 6 Điều, 0 Chương; 301 dòng, 23.7KB; OCR issues = 0 |
| 06/2026/NĐ-CP | — | Quy định về tổ chức và hoạt động của Ngân hàng Chính sách xã hội — cơ chế hoạt động, quản lý vốn, huy động vốn, cho vay ưu đãi | Tài chính / Ngân hàng | 216603 | `https://vanban.chinhphu.vn/?docid=216603&pageid=27160` | **Đã có** | `van-ban/tai-chinh-ngan-sach/nghi-dinh-06-2026-nd-cp-ngan-hanh-chinh-sa-xa-hoi.md`; heartbeat 2026-06-09 |
| 75/2026/NĐ-CP | — | Quy định chế độ tự chủ, tự chịu trách nhiệm về quản lý, sử dụng kinh phí quản lý hành chính — phân cấp quản lý tài chính cho cơ quan hành chính | Quản lý hành chính | 217217 | `https://vanban.chinhphu.vn/?docid=217217&pageid=27160` | **Chưa có** |
| 55/2026/NĐ-CP | 09/02/2026 | Xử phạt vi phạm hành chính trong lĩnh vực quản lý tài sản công, tiết kiệm chống lãng phí — mức phạt đến 20 triệu đồng, buộc nộp lại giá trị tài sản vượt tiêu chuẩn | Tài chính | 216927 | `https://vanban.chinhphu.vn/?pageid=27160&docid=216927` | **Đã có (2026-06-14, OCR từ PDF ký số CAdES-BES)** | File: `van-ban/tai-chinh/nghi-dinh-55-2026-nd-cp-xphc-quan-ly-tai-san-cong.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216927`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/55-ndcp.signed.pdf`; người ký: Hồ Đức Phớc (Phó TT ký thay TT); hiệu lực 09/02/2026; 4 Điều (Điều 1 sửa đổi 30 khoản, Điều 2 bổ sung từ, Điều 3 chuyển tiếp, Điều 4 thi hành); 1025 dòng, 65KB; OCR issues cleaned |

### Văn bản phát hiện thêm (chờ phiên sau)

- 141/NQ-CP — Chính sách sửa Luật Thương mại, Cạnh tranh, Quản lý ngoại thương, Bảo vệ người tiêu dùng (URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218308`)
- 28/2026/TT-BCA — Phát ngôn và cung cấp thông tin cho báo chí của Công an nhân dân (hiệu lực 12/05/2026; URL: `https://bocongan.gov.vn/media/bca-media/library-20260505164541-c00992ee-50fd-4cf5-bb17-ded76cad64d0-thong-tu-28-2026.pdf`)
- 46/2026/NĐ-CP — Luật An toàn thực phẩm (tạm ngưng đến 16/04/2026)
- 31/2026/QH16 — Kỳ họp thứ Nhất, Quốc hội khóa XVI (luật Viên chức, Luật Ban hành VBQPPL sửa đổi…)
- 27/2026/QH16 — Kế hoạch đầu tư công trung hạn 2026-2030 (tổng vốn 8.220.000 tỷ đồng)

## Ghi chú xử lý

- 5 văn bản mới trên sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao: 05/TT-BKHCN (AI ethics), 55/NĐ-CP (tài sản công), 04/TT-BKHCN (tiêu chuẩn đo lường) vì tác động hệ thống.
- 06/NĐ-CP và 75/NĐ-CP liên quan trực tiếp đến ngân sách và quản lý tài chính công.
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn.
- Ngày phát hiện: 2026-06-09 05:35 ICT
- Phiên thực hiện: agent:github-io:subagent:2df8fc5e-7830-40ac-98e6-4baee6150b4b (Đệ #1 Discovery 2026-06-09 lần 3)

---

## File trong `van-ban/` cần refactor (metadata "Đang cập nhật" hoặc file < 10k chars với lastedit > 7 ngày)

Phát hiện 2 nhóm:

### Nhóm A: File stub có "Đang cập nhật" trong metadata (152 file)

Tiêu biểu (ưu tiên cao theo nhóm thuộc 14 chủ đề):

| File | Nhóm | Vấn đề |
|---|---|---|
| `van-ban/bao-hiem/bao-hiem-y-te.md` | Y tế | Toàn bộ metadata = "Đang cập nhật" (7 markers); nội dung bám sát Luật BHYT 25/2008/QH12 |
| `van-ban/bo-tro-tu-phap/dau-gia-tai-san.md` | Tư pháp | Stub với 7 markers "Đang cập nhật" |
| `van-ban/bo-tro-tu-phap/giam-dinh-tu-phap.md` | Tư pháp | Stub với 7 markers "Đang cập nhật" |
| `van-ban/bo-tro-tu-phap/luat-su.md` | Tư pháp | Stub với 7 markers "Đang cập nhật" |
| `van-ban/buu-chinh-vien-thong/buu-chinh.md` | Bưu chính - Viễn thông | Stub với 7 markers "Đang cập nhật" |

> Tổng số: 152 file có metadata stub. Không crawl trong phiên này (theo ràng buộc task).

### Nhóm B: File < 10k chars, lastedit > 7 ngày, KHÔNG có "Đang cập nhật"

| File | Lastedit | Size | Ghi chú |
|---|---|---:|---|
| `van-ban/cong-nghiep/quan-ly-phan-bon.md` | 2026-05-13 | 8570 B | Stub thiếu nội dung; cần crawl chi tiết |
| `van-ban/ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md` | 2026-05-15 | 4876 B | Stub rất ngắn |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md` | 2026-05-26 | 3183 B | Stub rất ngắn |
| `van-ban/thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/index.md` | 2026-05-28 | 2875 B | Index trống, mới chỉ có 1 file con |
| `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md` | 2026-05-29 | 5793 B | Stub thiếu nội dung |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md` | 2026-05-29 | 7115 B | Stub thiếu nội dung |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/theo-doi-tinh-hinh-thi-hanh-phap-luat.md` | 2026-05-29 | 7399 B | Stub thiếu nội dung |

## Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 4)

### Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 3): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 198/2026/NĐ-CP | 03/06/2026 | Sửa đổi, bổ sung một số điều của NĐ 26/2025/NĐ-CP quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Ngân hàng Nhà nước Việt Nam | Ngân hàng / Tài chính | **Chưa có** | Cần crawl chi tiết; tác động hệ thống thể chế ngân hàng trung ương |
| 29/2026/TT-BCT | 06/06/2026 | Quy định vận hành thị trường bán buôn điện cạnh tranh, bổ sung quy định về hệ thống pin lưu trữ năng lượng (BESS) | Năng lượng / Thương mại | **Đã có (2026-06-14, Markdown từ nguồn web luatvietnam + moit.gov.vn)** | `van-ban/nang-luong-tai-nguyen/thong-tu-29-2026-tt-bct-van-hanh-thi-truong-ban-buon-dien-canh-tranh.md`; luatvietnam: https://luatvietnam.vn/dien-luc/thong-tu-29-2026-tt-bct-quy-dinh-van-hanh-thi-truong-ban-buon-dien-canh-tranh-436583-d1.html; moit.gov.vn: https://moit.gov.vn/tin-tuc/bo-cong-thuong-ban-hanh-thong-tu-moi-quy-dinh-chi-tiet-van-hanh-thi-truong-dien.html; heartbeat 2026-06-14; ngày ban hành 02/06/2026 (LuatVietnam), 11 Chương/14 Mục/142 Điều; do Nguyễn Hoàng Long (KT. Bộ trưởng, Thứ trưởng) ký; bãi bỏ 16/2025/TT-BCT và 36/2025/TT-BCT; hiệu lực 20/07/2026 (khoản 2 Điều 1 và khoản 51 Điều 3 có hiệu lực từ ngày ký) |
| 30/2026/TT-BKHCN | 06/06/2026 | Danh mục và kiểm soát hàng hóa lưỡng dụng | Khoa học công nghệ / An ninh | **Đã có (2026-06-14, OCR từ PDF mic.mediacdn.vn)** | `van-ban/khoa-hoc-cong-nghe/thong-tu-30-2026-tt-bkhcn-danh-muc-hang-hoa-luong-dung.md`; PDF: https://mic.mediacdn.vn/document/2026/6/8/tt302026-17808794296371812199951.pdf; metadata: https://mst.gov.vn/van-ban-phap-luat/25442.htm; heartbeat 2026-06-14; 26 trang OCR; 4 Điều; Phụ lục 22 trang (bảng ECCN trích từ EU list C(2025) 5947 final); hiệu lực 06/06/2026 |
| 37/2026/TT-BCA | 24/04/2026 | Sửa đổi, bổ sung quy định về đăng ký, kiểm định phương tiện; tích hợp dữ liệu chứng nhận đăng ký xe trên VNeID và VNeTraffic | Giao thông / Công nghệ | **Đã có** | `van-ban/giao-thong-van-tai/thong-tu-37-2026-tt-bca-dang-ky-xe-vneid.md`; heartbeat 2026-06-10; OCR 5 trang scan; 239 dòng, 4 Chương/8 Điều; hiệu lực 08/06/2026 |
| 08/2026/TT-BKHCN | 31/03/2026 | Quy định xác thực sinh trắc học ảnh khuôn mặt khi thuê bao thay đổi thiết bị đầu cuối; doanh nghiệp viễn thông có thể tạm dừng dịch vụ tối đa 2 giờ | Viễn thông / An ninh | **Đã có** | `van-ban/vien-thong-buu-chinh/thong-tu-08-2026-tt-bkhoa-hoc-cong-nghe-xac-thuc-thue-bao.md`; heartbeat 2026-06-10; CAdES-BES scan OCR; 17.7KB, 273 dòng, 10 Điều; hiệu lực chung 15/04/2026, Điều 8 (đổi thiết bị) hiệu lực 15/06/2026 |

### Văn bản phát hiện thêm (chờ phiên sau)

- **07/2026/TT-NHNN** (Ngân hàng) — sửa đổi quy định môi giới tiền tệ ngân hàng, hiệu lực 20/06/2026
- **06/2026/TT-BTC** (Tài chính) — kiểm tra, giám sát hàng hóa xâm phạm quyền sở hữu trí tuệ
- **06/2026/TT-BGDĐT** (Giáo dục) — quy chế tuyển sinh đại học

### Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong phiên Đệ #3 Full Content Crawler tiếp theo.
- Ưu tiên cao: 198/NĐ-CP (NĐ sửa đổi thể chế NHNN) → 29/TT-BCT (thị trường điện cạnh tranh) → 30/TT-BKHCN (hàng hóa lưỡng dụng) → 37/TT-BCA (đăng ký xe VNeID) → 08/TT-BKHCN (xác thực sinh trắc học).
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, chinhphu.vn, luatvietnam.vn.
- Ngày phát hiện: 2026-06-09 07:30 ICT
- Phiên thực hiện: agent:github-io:subagent:47222254-c246-4fef-8e22-a51c3f5fd2c5 (Đệ #1 Discovery 2026-06-09 lần 4)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 5)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 4): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 96/2026/NĐ-CP | 31/03/2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Đầu tư 2025 — thay thế NĐ 31/2021; quy định tiếp cận thị trường cho nhà đầu tư nước ngoài, chuyển nhượng dự án, ưu đãi đầu tư đặc biệt (bán dẫn, AI, R&D) | Đầu tư / Thương mại | Đã có | `van-ban/thuong-mai-dau-tu-chung-khoan/nghi-dinh-96-2026-nd-cp-chi-tiet-luat-dau-tu.md`; heartbeat 2026-06-10; OCR CAdES-BES 143 trang; 447KB, 7035 dòng, 109/112 Điều |
| 199/2026/NĐ-CP | 05/06/2026 | Quy định mức hỗ trợ phục vụ hàng tháng dành cho nhiều vị trí lãnh đạo | Lao động / Tổ chức bộ máy | — | **Đã có** | Cần xác minh docid trên vanban.chinhphu.vn; liên quan đến chế độ lãnh đạo, hỗ trợ chức danh |
| 196/2026/NĐ-CP | 01/06/2026 | Quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Văn phòng Chính phủ — chuyển Cổng TTĐT Chính phủ thành Cục TT&TT Chính phủ (loại 1) | Tổ chức bộ máy | **Đã có** | `van-ban/to-chuc-bo-may-nha-nuoc/nghi-dinh-196-2026-nd-cp-co-cau-to-chuc-van-phong-chinh-phu.md`; heartbeat 2026-06-10; OCR CAdES-BES 9 trang; 27KB, 5 Điều, người ký Phạm Gia Túc |
| 190/2026/NĐ-CP | 02/06/2026 | Quy định chi tiết một số điều của Luật Tình trạng khẩn cấp — trợ cấp cho tổ chức, cá nhân tham gia hoạt động trong tình trạng khẩn cấp (0,2–0,4 lần lương cơ sở/ngày) | An ninh / Pháp luật | — | **Chưa có** | Cần xác minh docid; lần đầu có nghị định hướng dẫn Luật Tình trạng khẩn cấp |
| 85/2026/NĐ-CP | 10/05/2026 | Thiết lập khung pháp lý cho bảo hiểm hưu trí bổ sung tại Việt Nam — người lao động và người sử dụng lao động tự nguyện tham gia | Lao động / Bảo hiểm | — | **Chưa có** | Cần xác minh docid; chính sách mới lần đầu xuất hiện tại VN |

### Đối chiếu nhanh

Tất cả 5 văn bản đều không có trong `LEGISLATION_TRACKING.md` (đã grep xác nhận).

## Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **96/2026/NĐ-CP** (Luật Đầu tư — tác động FDI toàn nền kinh tế).
- Thứ hai: **85/2026/NĐ-CP** (BH hưu trí bổ sung — chính sách mới lần đầu).
- Thứ ba: **196/2026/NĐ-CP** (cơ cấu VP Chính phủ — tái cơ cấu bộ máy).
- Cần xác minh docid cho 4 văn bản (199, 196, 190, 85) trên vanban.chinhphu.vn.
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, chinhphu.vn, vietnamplus.vn.
- Ngày phát hiện: 2026-06-09 08:00 ICT
- Phiên thực hiện: agent:github-io:subagent:d4edb7fe-f894-47cf-93ef-46513048b191 (Đệ #1 Discovery 2026-06-09 lần 5)

---

## Ghi chú xử lý

- 5 văn bản mới trong bảng chính sẽ được crawl chi tiết trong các phiên "Đệ #3 (Full Content Crawler)" tiếp theo.
- Các văn bản "chờ phiên sau" (54/91/88/93/95/66/105/07/20-TT-BTC/19-QH16) sẽ được Đệ #1 Discovery ưu tiên trong các phiên kế tiếp (giới hạn 5/phiên).
- File refactor nhóm A (152 file stub) cần chiến lược crawl tổng thể, KHÔNG xử lý trong 1 phiên.
- File refactor nhóm B (7 file) có thể ưu tiên crawl trong phiên kế tiếp kết hợp với crawl văn bản mới cùng nhóm chủ đề.
- Ngày phát hiện: 2026-06-07 20:30 ICT
- Phiên thực hiện: agent:github-io:subagent:606227c4-8342-47c9-8765-7e21835a8cff (Đệ #1 Discovery respawn)

---

# Cập nhật 2026-06-07 (phiên Đệ #3 Full Content Crawler)

- Hoàn thiện `van-ban/lao-dong/nghi-dinh-161-2026.md` (Nghị định 161/2026/NĐ-CP — mức lương cơ sở 2.530.000 đ/tháng từ 01/7/2026): đã lấy metadata từ vanban.chinhphu.vn (docid 218107) và OCR PDF chữ ký số CAdES-BES bằng Signed PDF OCR Pipeline (HEARTBEAT.md mục 3) trên 7 trang; sửa lỗi OCR thủ công dựa trên metadata; file 17.5 KB, đầy đủ 7 Điều.
- Commit & push vào PR heartbeat active #199 (`docs/heartbeat-active-pr-flow`).
- Phiên thực hiện: agent:github-io:subagent:8876ca31-2b33-412b-84e3-9d99fa051c3f (Đệ #3 Full Content Crawler)

## Cập nhật 2026-06-08 (phiên Đệ #3 Full Content Crawler)

- Hoàn thiện `van-ban/khoa-hoc-cong-nghe/thong-tu-23-2026-tt-bkhcns-kinh-phi-tieu-chuan-quy-chuan.md` (Thông tư 23/2026/TT-BKHCN — quy định lập dự toán, quản lý, sử dụng và quyết toán kinh phí ngân sách nhà nước lĩnh vực KHCN&ĐMST&CDS cho hoạt động tiêu chuẩn, quy chuẩn kỹ thuật): metadata chính thức từ vanban.chinhphu.vn docid 218278, PDF 32 trang / 32 Điều; file hiện là bản tóm tắt/cấu trúc lại, chưa phải toàn văn nguyên văn.
- Phiên thực hiện: agent:github-io:subagent:bca2d895-588b-4957-9c1a-260bd7334e86 (Đệ #3 Full Content Crawler)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 6)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 5): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 15/2026/TT-BYT | 17/05/2026 | Quy định chi tiết một số điều Luật Phòng bệnh — phân loại bệnh truyền nhiễm A/B/C, hệ thống thông tin giám sát, giám sát dựa vào sự kiện | Y tế | 218141 | **Đã có (2026-06-14)** | File: `van-ban/y-te/thong-tu-15-2026-tt-byt-phong-benh-truyen-nhiem.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218141`; người ký: Nguyễn Thị Liên Hương (Thứ trưởng, ký thay Bộ trưởng BYT); hiệu lực 01/07/2026; 67 Điều, 8 Chương (I-VIII), 12 Mục, 2 Phụ lục (PL1: bảng tính điểm phân loại bệnh; PL2: 2 mẫu thông tin dịch); 1357 dòng, 88KB; OCR issues = 0; PDF gốc Word Microsoft 365 (text extract sạch, không cần OCR) |
| 193/2026/NĐ-CP | 01/06/2026 | Quy định quyết toán vốn đầu tư dự án — thay thế quy định cũ, điều chỉnh cơ chế quyết toán cho dự án đầu tư công | Đầu tư | — | **Chưa có** | Cần xác minh docid trên vanban.chinhphu.vn; hiệu lực 01/07/2026; liên quan trực tiếp 96/2026/NĐ-CP (Luật Đầu tư) đã có |
| 07/2026/TT-NHNN | 06/05/2026 | Sửa đổi, bổ sung quy định về hoạt động môi giới tiền tệ của ngân hàng thương mại và chi nhánh ngân hàng nước ngoài | Ngân hàng | — | **Chưa có** | Hiệu lực 20/06/2026; tác động toàn bộ hệ thống NHTM; cần xác minh docid |
| 18/2026/TT-BTC | 2026 | Quy định gửi mẫu số 01/BK-STK (tài khoản ngân hàng) để kê khai thuế, hỗ trợ hộ kinh doanh và tổ chức tín dụng | Tài chính / Thuế | — | **Chưa có** | Cần xác minh ngày ban hành và docid; liên quan NĐ 141/2026/NĐ-CP và 68/2026/NĐ-CP đã có |
| 982/QĐ-TTg | 04/06/2026 | Phê duyệt Đề án hỗ trợ, phát triển doanh nghiệp công nghệ số vươn ra toàn cầu đến năm 2030, tầm nhìn đến 2045 | KHCN / Công nghệ số | — | **Chưa có** | QĐ Thủ tướng; tác động chiến lược ngành CN số; cần xác minh docid |

### Văn bản phát hiện thêm (chờ phiên sau)

- **29/2026/TT-BCT** (Năng lượng) — quy định vận hành thị trường bán buôn điện cạnh tranh, BESS
- **30/2026/TT-BKHCN** (KHCN / An ninh) — Danh mục và kiểm soát hàng hóa lưỡng dụng
- **37/2026/TT-BCA** (Giao thông) — đăng ký xe VNeID, tích hợp dữ liệu chứng nhận đăng ký xe
- **08/2026/TT-BKHCN** (Viễn thông) — xác thực sinh trắc học ảnh khuôn mặt khi thuê bao đổi thiết bị
- **141/NQ-CP** (Thương mại) — Chính sách sửa Luật Thương mại, Cạnh tranh, QLNT, BVNL người tiêu dùng
- **28/2026/TT-BCA** (An ninh) — phát ngôn và cung cấp thông tin cho báo chí của CAND

## Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **15/2026/TT-BYT** (Y tế — Luật Phòng bệnh; đã có docid chính thức 218141; hiệu lực 01/07/2026).
- Thứ hai: **193/2026/NĐ-CP** (Đầu tư — quyết toán vốn đầu tư; hiệu lực 01/07/2026).
- Thứ ba: **07/2026/TT-NHNN** (Ngân hàng — môi giới tiền tệ; hiệu lực 20/06/2026 — sớm nhất).
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, cafef.vn, baophapluat.vn, vietnamplus.vn.
- Ngày phát hiện: 2026-06-09 08:55 ICT
- Phiên thực hiện: agent:github-io:subagent:913503df-75c0-4c00-8359-f4962742e8e0 (Đệ #1 Discovery 2026-06-09 lần 6)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 7)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 6): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất (NĐ-CP, TT Bộ liên quan đa ngành):

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID (xác nhận) | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 127/2026/NĐ-CP | 06/04/2026 | Quy định về quản lý chất lượng và chính sách phát triển sản phẩm, dịch vụ Halal — khung pháp lý toàn diện đầu tiên cho ngành Halal tại Việt Nam, hỗ trợ chi phí chứng nhận cho doanh nghiệp | Thương mại / Xuất khẩu | Đã có | `van-ban/thuong-mai-dau-tu-chung-khoan/nghi-dinh-127-2026-nd-cp-quan-ly-halal.md`; heartbeat 2026-06-10; OCR CAdES-BES 27 trang; 620 dòng, 28 Điều/6 Chương + 4 phụ lục |
| 06/2026/TT-BYT | 02/04/2026 | Quy định mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 — chuẩn hóa dữ liệu y tế toàn quốc, liên quan trực tiếp thanh toán BHYT | Y tế / Dữ liệu | — | **Chưa có** | Hiệu lực 01/07/2026 (khoản 2, 3 Điều 5 hiệu lực 01/06/2026); Bộ trưởng Đào Hồng Lan ký; chuẩn hóa toàn bộ hệ thống khám chữa bệnh |
| 47/2026/TT-BCA | 12/05/2026 | Ban hành Quy chuẩn kỹ thuật quốc gia QCVN 12:2026/BCA về an ninh mạng cho hệ thống thông tin lưu trữ tài liệu điện tử trong các cơ quan Đảng, Nhà nước | An ninh mạng / Lưu trữ | 218069 | **Đã có** (2026-06-14, refactor từ PDF ký số) | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218069`; `van-ban/an-ninh-quoc-gia/quy-chuan-an-ninh-mang-he-thong-luu-tru-tai-lieu-dien-tu.md`; OCR pdftoppm 150dpi + tesseract vie 47 trang, 1059 dòng Markdown, layout `vanban`; Thông tư 3 Điều + QCVN 12:2026/BCA 6 mục/22 nhóm yêu cầu kỹ thuật/22 nhóm đánh giá; số hiệu thực tế 47/2026/TT-BCA (KHÔNG phải 72 như tracking cũ ghi nhầm); hiệu lực 01/07/2026 |
| 18/2026/TT-BYT | 01/06/2026 | Quy định chi tiết Luật Dược và NĐ 163/2025/NĐ-CP về thuốc và nguyên liệu làm thuốc phải kiểm soát đặc biệt (dược chất gây nghiện, hướng thần, tiền chất) | Y tế / Dược | — | **Chưa có** | Hiệu lực ngay 01/06/2026; áp dụng cho bảo quản, sản xuất, pha chế, cấp phát, sử dụng, hủy, vận chuyển thuốc kiểm soát |
| 38/2026/TT-BGDĐT | 29/04/2026 | Quy định chuẩn cơ sở giáo dục nghề nghiệp — 6 Điều kiện bảo đảm chất lượng, 10 Chỉ số hoạt động định lượng | Giáo dục | — | **Chưa có** | Hiệu lực 29/04/2026; tỷ lệ nhập học ≥50%, tỷ lệ việc làm ≥70%; tự đánh giá hàng năm, công khai kết quả |

### Văn bản phát hiện thêm (chờ phiên sau)

- **56/2026/TT-BCA** (An ninh) — quản lý người bị cấm đi khỏi nơi cư trú, hiệu lực 01/07/2026
- **03/2026/TTLT-BCA-BQP-TANDTC-VKSNDTC** (Tư pháp) — phối hợp trích xuất phạm nhân, hiệu lực 01/07/2026, thay thế TTLT 01/2020
- **05/2026/TT-BYT** (Y tế) — danh mục hóa chất cấm và nguy hiểm trong chế phẩm diệt côn trùng/diệt khuẩn
- **04/2026/TT-BNV** (Lao động) — quy định kinh phí和服务 specs gửi người lao động ra nước ngoài
- **06/2026/TT-BGDĐT** (Giáo dục) — quy chế tuyển sinh đại học và cao đẳng, hiệu lực 15/02/2026

## Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **127/2026/NĐ-CP** (Halal — khung pháp lý đầu tiên, tác động xuất khẩu rộng).
- Thứ hai: **06/2026/TT-BYT** (ICD-10 — chuẩn hóa dữ liệu y tế toàn quốc, ảnh hưởng BHYT).
- Thứ ba: **18/2026/TT-BYT** (thuốc kiểm soát đặc biệt — hiệu lực ngay).
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, thuvienphapluat.vn, xaydungchinhsach.chinhphu.vn.
- Ngày phát hiện: 2026-06-09 09:30 ICT
- Phiên thực现: agent:github-io:subagent:b21c1a4e-ef47-4b24-9ab1-b00fa3eb7e0e (Đệ #1 Discovery 2026-06-09 lần 7)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 8)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 7): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 973/QĐ-TTg | 01/06/2026 | Phê duyệt Chương trình Sức khỏe học đường giai đoạn 2026-2035 — mục tiêu 100% người học khám sức khỏe mỗi năm, 60% GDPT công lập có nhân viên y tế chuyên trách, 100% ĐH/CĐ/TC/nội trú/khuyết tật có nhân viên y tế | Y tế / Giáo dục | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218335`; Phó TT Lê Tiến Châu ký; tác động toàn bộ hệ thống giáo dục và y tế học đường |
| 11/2026/TT-BXD | 31/03/2026 | Quy định danh mục, quy cách và chỉ tiêu kỹ thuật khoáng sản làm vật liệu xây dựng được phép xuất khẩu | Xây dựng / Xuất khẩu | **Đã có (2026-06-15, Markdown từ nguồn web luatvietnam)** | Hiệu lực 01/06/2026; tác động ngành khai khoáng và xuất khẩu VLXD; Bộ Xây dựng ban hành. File: `van-ban/xay-dung/thong-tu-11-2026-tt-bxd-danh-muc-khoang-san-vlxd-xuat-khau.md`. URL: https://luatvietnam.vn/xuat-nhap-khau/thong-tu-11-2026-tt-bxd-quy-dinh-danh-muc-va-chi-tieu-ky-thuat-khoang-san-xay-dung-xuat-khau-432239-d1.html |
| 45/2026/TT-BTC | 29/04/2026 | Sửa đổi, bổ sung TT 29/2020/TT-BTC hướng dẫn thực hiện việc xử phạt vi phạm hành chính trong lĩnh vực quản lý tài sản công | Tài chính / Tài sản công | **Đã có (2026-06-14, Markdown từ PDF OCR + cross-check web)** | Hiệu lực 15/06/2026; bổ sung chế tài xử phạt tài sản công; liên quan trực tiếp 55/2026/NĐ-CP đã có. File: `van-ban/tai-chinh/thong-tu-45-2026-tt-btc-sua-doi-29-2020-tt-btc-xu-phat-tai-san-cong.md`. URL tham khảo: https://thuvienphapluat.vn/phap-luat/ho-tro-phap-luat/toan-van-thong-tu-452026ttbtc-sua-doi-thong-tu-292020ttbtc-ve-xu-phat-vi-pham-hanh-chinh-linh-vuc-t-267069.html ; https://lsvn.vn/bo-sung-quy-dinh-ve-xac-dinh-gia-tri-cua-tai-san-lam-can-cu-xac-dinh-khung-tien-phat-trong-quan-ly-tai-san-cong-a172644.html |

| 32/2026/TT-BQP | 22/04/2026 | Quy định loại khỏi biên chế và xử lý tài sản công trong Bộ Quốc phòng | Quốc phòng / Tài sản công | **Đã có (2026-06-15, Markdown từ nguồn web luatvietnam)** | Hiệu lực 08/06/2026; 10 Chương, 45 Điều (Điều 6 có 12 nhóm trường hợp tài sản được loại khỏi biên chế); tác động hệ thống quản lý tài sản và biên chế Bộ QP. File: `van-ban/quoc-phong/thong-tu-32-2026-tt-bqp-loai-khoi-bien-che-tai-san-cong-bo-quoc-phong.md`. URL: https://luatvietnam.vn/tai-chinh/thong-tu-32-2026-tt-bqp-quy-dinh-loai-khoi-bien-che-va-xu-ly-tai-san-cong-bo-quoc-phong-433214-d1.html |
| 50/2025/TT-BCT | 07/11/2025 | Lộ trình phối trộn nhiên liệu sinh học — xăng không chì phải phối trộn thành xăng E10 toàn quốc từ 01/06/2026; E5RON92 kéo dài đến 31/12/2030 | Thương mại / Năng lượng | **Chưa có** | Hiệu lực 01/06/2026; tác động toàn bộ mạng lưới phân phối xăng dầu; bắt buộc E10 toàn quốc; kiểm tra và xử phạt từ 01/06/2026 |

### Văn bản phát hiện thêm (chờ phiên sau)

- **09/2026/TT-BNV** (Lao động) — sửa đổi TT 21/2021 hướng dẫn Luật NLĐ VN đi làm việc ở nước ngoài theo hợp đồng — hiệu lực 30/06/2026
- **06/2026/TT-BNV** (Tổ chức bộ máy) — sửa đổi TT 10/2025 hướng dẫn chức năng, nhiệm vụ, quyền hạn Sở Nội vụ — hiệu lực 15/06/2026
- **36/2026/TT-BGDĐT** (Giáo dục) — Quy chế tổ chức và hoạt động của trường dự bị đại học — hiệu lực 07/06/2026
- **55/2026/NĐ-CP** (Tài chính) — đã có trong tracking nhưng chưa crawl chi tiết
- **75/2026/NĐ-CP** (Quản lý hành chính) — đã có trong tracking nhưng chưa crawl chi tiết

## Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **973/QĐ-TTg** (Sức khỏe học đường — đã xác minh docid 218335 trên vanban.chinhphu.vn; tác động toàn bộ hệ thống giáo dục + y tế).
- Thứ hai: **50/2025/TT-BCT** (Nhiên liệu sinh học E10 — bắt buộc toàn quốc từ 01/06/2026; tác động ngành năng lượng).
- Thứ ba: **11/2026/TT-BXD** (Khoáng sản VLXD xuất khẩu — hiệu lực 01/06/2026).
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn, baochinhphu.vn, luatvietnam.vn, baophapluat.vn, mst.gov.vn.
- Ngày phát hiện: 2026-06-09 09:33 ICT
- Phiên thực hiện: agent:github-io:subagent:990114ea-e144-4163-b909-a01caa2b8817 (Đệ #1 Discovery 2026-06-09 lần 8)

---

# Cập nhật 2026-06-09 (phiên Đệ #1 Discovery — lần 9)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

So sánh với `documents/LEGISLATION_TRACKING.md` (đến phiên lần 8): phát hiện 5 văn bản mới chưa từng được ghi nhận. Ưu tiên tác động rộng nhất:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 148/NQ-CP | 08/06/2026 | Nghị quyết phiên họp Chính phủ thường kỳ tháng 5/2026 — đẩy mạnh giải ngân đầu tư công, đảm bảo cung ứng điện/xăng dầu, phát triển nhà ở xã hội, phát triển thị trường chứng khoán | Đa ngành / Kinh tế vĩ mô | **Co** | `van-ban/da-nganh/nghi-quyet-148-nq-cp-phien-hop-chinh-phu-thang-5-2026.md` |
| 27/2026/TT-BXD | 05/06/2026 | Phân cấp thẩm quyền của Bộ trưởng Bộ Xây dựng trong quản lý, sử dụng tài sản công; đầu tư xây dựng, mua sắm, sửa chữa tài sản sử dụng kinh phí chi thường xuyên NSNN (đơn vị trực thuộc được phê duyệt dự án dưới 45 tỷ đồng) | Xây dựng / Quản lý tài sản | **Đã có (2026-06-15, Markdown từ PDF text + cross-check web)** | Hiệu lực 01/08/2026; tác động toàn bộ hệ thống xây dựng và quản lý tài sản công thuộc Bộ Xây dựng; `van-ban/xay-dung/thong-tu-27-2026-tt-bxd-phan-cap-tham-quyen-quan-ly-tai-san-cong.md`; nguồn: vanban.chinhphu.vn (docid 218377) + baochinhphu.vn |
| 20/2026/QH16 | 24/04/2026 | Cơ chế phối hợp, chính sách đặc thù nâng cao hiệu quả phòng ngừa và giải quyết tranh chấp đầu tư quốc tế — thành lập Trung tâm phòng ngừa tranh chấp đầu tư | Đầu tư / Thương mại | **Chưa có** | Cần crawl chi tiết; nghị quyết QH16; Chính phủ giao Bộ Tư pháp soạn NĐ hướng dẫn trước 30/06/2026; tác động FDI toàn nền kinh tế |
| 26/VBHN-BXD | 02/06/2026 | Hợp nhất Thông tư 12/2025/TT-BXD và Thông tư 19/2026/TT-BXD về tải trọng, khổ giới hạn đường bộ; lưu hành xe; hàng siêu trường siêu trọng; xếp hàng hóa; cấp giấy phép lưu hành | Giao thông / Xây dựng | **Chưa có** | Văn bản hợp nhất; tác động ngành vận tải, logistics, giao thông đường bộ |
| 979/QĐ-TTg | 05/06/2026 | Phê duyệt Kế hoạch triển khai Nghị quyết 20/2026/QH16 về cơ chế phối hợp, chính sách đặc thù nâng cao phòng ngừa và giải quyết tranh chấp đầu tư quốc tế | Đầu tư / Pháp luật | **Chưa có** | QĐ Thủ tướng ký; thực thi NQ 20/2026/QH16; giao nhiều bộ phối hợp; liên quan trực tiếp 20/2026/QH16 đã ghi nhận ở trên |

### Đối chiếu nhanh — văn bản đã có trong tracking (không trùng lặp)

- **148/NQ-CP** — chưa có trong file → thêm mới
- **27/2026/TT-BXD** — chưa có trong file → thêm mới
- **20/2026/QH16** — chưa có trong file → thêm mới
- **26/VBHN-BXD** — chưa có trong file → thêm mới
- **979/QĐ-TTg** — chưa có trong file → thêm mới

### Các văn bản phát hiện khác (chưa tạo entry, chờ phiên sau)

- **198/2026/NĐ-CP** — sửa đổi NĐ 26/2025 về cơ cấu tổ chức NHNN (đã có lần 4)
- **29/2026/TT-BCT** — thị trường bán buôn điện cạnh tranh, BESS (đã có lần 4)
- **30/2026/TT-BKHCN** — hàng hóa lưỡng dụng (đã có lần 4)
- **37/2026/TT-BCA** — đăng ký xe VNeID (đã có lần 4)
- **08/2026/TT-BKHCN** — xác thực sinh trắc học thuê bao (đã có lần 4)
- **56/2026/TT-BCA** — quản lý người bị cấm đi khỏi nơi cư trú
- **03/2026/TTLT-BCA-BQP-TANDTC-VKSNDTC** — phối hợp trích xuất phạm nhân
- **04/2026/TT-BNV** — kinh phí NLĐ đi làm việc nước ngoài
- **06/2026/TT-BGDĐT** — quy chế tuyển sinh đại học
- **05/2026/TT-BYT** — hóa chất cấm trong chế phẩm diệt côn trùng

## Ghi chú xử lý

- 5 văn bản mới sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **148/NQ-CP** (nghị quyết phiên họp Chính phủ — tác động toàn diện kinh tế vĩ mô, đa ngành).
- Thứ hai: **20/2026/QH16** (tranh chấp đầu tư quốc tế — nghị quyết QH16, tác động FDI toàn nền kinh tế).
- Thứ ba: **27/2026/TT-BXD** (phân cấp tài sản công xây dựng — hiệu lực 01/08/2026).
- **979/QĐ-TTg** liên quan trực tiếp **20/2026/QH16** — có thể crawl chung.
- **26/VBHN-BXD** là văn bản hợp nhất, cần ưu tiên khi xử lý nhóm giao thông/xây dựng.
- Nguồn: Web search Brave + Gemini tổng hợp vanban.chinhphu.vn, baochinhphu.vn, luatvietnam.vn, thanhtra.com.vn, xaydungchinhsach.chinhphu.vn.
- Ngày phát hiện: 2026-06-09 10:00 ICT
- Phiên thực hiện: agent:github-io:subagent:adde4100-4ad0-4547-8fd2-3c04cc7147e3 (Đệ #1 Discovery 2026-06-09 lần 9)

| 12/2026/TT-BTC | 10/02/2026 | Quy định trình tự, thủ tục giám định chi phí KCB BHYT, biểu mẫu thanh toán, quyết toán và biện pháp thi hành NĐ 188/2025/NĐ-CP hướng dẫn Luật BHYT | Y tế / Bảo hiểm | **Đã có** | `van-ban/y-te-duoc/thong-tu-12-2026-tt-btc-giam-dinh-chi-phi-kcb-bhyt.md`; heartbeat 2026-06-10; web content only (PDF not found on datafiles) |
| 49/2026/NĐ-CP | 31/01/2026 | Chi tiết và hướng dẫn NQ 254/2025/QH15 về bồi thường, hỗ trợ, tái định cư, thu hồi đất; sửa đổi NĐ 88, 101, 102/2024/NĐ-CP; phân cấp đất đai; 22 Điều, 5 Chương | Đất đai | **Đã có** | `van-ban/dat-dai/nghi-dinh-49-2026-nd-cp-huong-dan-nq-254-dat-dai.md`; heartbeat 2026-06-10; PDF Word; 1261 dòng; 1190 dòng Markdown |
| 50/2026/NĐ-CP | 31/01/2026 | Quy định chi tiết NQ 254/2025/QH15 về tiền sử dụng đất, tiền thuê đất — căn cứ tính, chuyển mục đích, miễn giảm, xử lý chuyển tiếp | Đất đai | **Đã có** | `van-ban/dat-dai/nghi-dinh-50-2026-nd-cp-tien-su-dung-dat-tien-thue-dat.md`; heartbeat 2026-06-10; PDF Word 30 trang; 1395 dòng; 14 Điều, 3 Chương |

---

# Cập nhật 2026-06-10 (phiên Đệ #1 Discovery — 5 nhóm chủ đề)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

Quét 9 nhóm chủ đề: Thuế, Đất đai, KHCN, Lâm nghiệp, Chứng khoán, Y tế, Tài chính, Giao thông, Ngoại giao. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-09 lần 9): phát hiện 5 văn bản mới chưa từng được ghi nhận.

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 125/2026/NĐ-CP | — | Quy định về hoạt động khoa học, công nghệ và đổi mới sáng tạo trong cơ sở giáo dục đại học — khung pháp lý cho nghiên cứu khoa học, chuyển giao công nghệ tại các trường ĐH | Khoa học công nghệ | **Chưa có** | URL: `https://vanban.chinhphu.vn/?docid=217673&pageid=27160`; tác động hệ thống giáo dục đại học |
| 13/VBHN-BNNMT | 26/02/2026 | Văn bản hợp nhất quy định chi tiết thi hành Luật Lâm nghiệp — hợp nhất các Nghị định hướng dẫn Luật Lâm nghiệp | Lâm nghiệp | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217341`; thay thế các NĐ cũ về lâm nghiệp |
| 13/VBHN-BTC | 22/04/2026 | Văn bản hợp nhất hướng dẫn giám sát giao dịch chứng khoán trên thị trường chứng khoán — cập nhật quy trình giám sát theo Luật Chứng khoán sửa đổi | Chứng khoán | **Chưa có** | Công báo số 294 ngày 31/5/2026; tác động SSC, VSDC, các CTCK |
| 02/2026/TT-BNG | 09/05/2026 | Quy định phân cấp nhiệm vụ, quyền hạn của Bộ Ngoại giao trong các lĩnh vực: văn bản pháp định, tổ chức, NGO nước ngoài, biên giới, điều ước, quốc tịch, xuất nhập cảnh, lãnh sự, nhập tịch, nhận con nuôi | Ngoại giao | **Chưa có** | Hiệu lực từ ngày ký; tác động toàn bộ hệ thống Bộ Ngoại giao và các cơ quan đại diện |
| 26/VBHN-BXD | 06/06/2026 | Văn bản hợp nhất Thông tư 12/2025/TT-BXD và Thông tư 19/2026/TT-BXD về tải trọng, khổ giới hạn đường bộ; lưu hành xe; hàng siêu trường siêu trọng; xếp hàng hóa; cấp giấy phép lưu hành — thay thế Thông tư 39/2024/TT-BGTVT | Giao thông / Xây dựng | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217235`; tác động ngành vận tải, logistics, đường bộ |

### Văn bản phát hiện thêm các nhóm còn lại (chưa có trong 5 văn bản ưu tiên, chờ phiên sau)

- **Thuế**: Không có văn bản mới 2026 nổi bật ngoài các văn bản đã tracking; cần check 19/QH16 (sửa thuế xăng dầu) và 25/NQ-CP (kéo dài thuế nhập khẩu 0%) — đã có trong tracking
- **Đất đai**: 50/2026/NĐ-CP (hướng dẫn NQ 254 về tiền sử dụng đất, tiền thuê đất) — chưa có trong tracking; URL: `https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-50-2026-nd-cp-quy-dinh-chi-tiet-nghi-quyet-254-2025-qh15-thao-go-kho-khan-vuong-mac-ve-tien-su-dung-dat-tien-thue-dat-119260202161658051.htm`
- **Y tế**: 12/2026/TT-BTC (giám định chi phí KCB BHYT, hướng dẫn NĐ 188/2025/NĐ-CP) — chưa có trong tracking; URL: `https://vanban.chinhphu.vn/?classid=1&docid=216997&orggroupid=4&pageid=27160`
- **Tài chính**: 26/2026/TT-BTC (hướng dẫn NĐ 73/2026/NĐ-CP về Luật Ngân sách nhà nước) — đã có trong tracking (docid 217323); văn bản hợp nhất 27/VBHN-BTC (Hệ thống Mục lục NSNN)
- **Giao thông**: Đã thêm 26/VBHN-BXD trong 5 văn bản ưu tiên; 861/QĐ-BXD (đính chính TT 20/2026/TT-BXD về cảng thủy nội địa)

## Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-09 lần 9)

Tất cả 5 văn bản mới đều chưa từng được ghi nhận trong tracking. Các văn bản đã có trong tracking nhưng cần xác minh trạng thái:

- **50/2026/NĐ-CP** (Đất đai) — "Đề xuất ưu tiên" trong tracking đến 2026-05-14 nhưng chưa được thêm entry; phiên này ghi nhận phát hiện nhưng chưa đưa vào 5 văn bản ưu tiên vì giới hạn
- **125/2026/NĐ-CP** (KHCN) — chưa từng được ghi nhận; thêm mới
- **13/VBHN-BNNMT** (Lâm nghiệp) — chưa từng được ghi nhận; thêm mới
- **13/VBHN-BTC** (Chứng khoán) — ghi chú trong phiên 2026-06-09 lần mới ("Văn bản hợp nhất 13/VBHN-BTC — chưa tạo entry, chờ phiên sau"); thêm mới
- **02/2026/TT-BNG** (Ngoại giao) — ghi nhận trong phiên lần 4 là "thông tư phân cấp" nhưng chưa tạo entry riêng; thêm mới
- **26/VBHN-BXD** (Giao thông) — đã được ghi nhận trong phiên lần 9 nhưng chưa tạo entry với trạng thái; thêm mới

## Đề xuất ưu tiên phiên tiếp theo

1. **Đất đai**: 50/2026/NĐ-CP — cặp NĐ hướng dẫn NQ 254/QH15 về tiền sử dụng đất, tiền thuê đất; tác động rộng toàn quốc; đã được đề xuất từ 2026-05-14 nhưng chưa xử lý.
2. **Y tế**: 12/2026/TT-BTC — giám định chi phí KCB BHYT; liên quan trực tiếp người dân và hệ thống y tế.
3. **Chứng khoán**: 13/VBHN-BTC — hướng dẫn giám sát giao dịch; cần đối chiếu với 145/2026/NĐ-CP (cơ chế tài chính VNX/VSDC) đã có.
4. **Lâm nghiệp**: 13/VBHN-BNNMT — hợp nhất hướng dẫn Luật Lâm nghiệp; bổ sung 146/2026/NĐ-CP (xử phạt vi phạm lâm nghiệp) đã có.
5. **Giao thông**: 26/VBHN-BXD — giấy phép lưu hành xe; tác động trực tiếp ngành logistics và vận tải đường bộ.

## Ghi chú xử lý

- 5 văn bản mới trong bảng chính sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **125/2026/NĐ-CP** (KHCN trong cơ sở GDĐH — khung pháp lý mới cho nghiên cứu tại trường ĐH).
- Thứ hai: **13/VBHN-BNNMT** (Lâm nghiệp — văn bản hợp nhất).
- Thứ ba: **13/VBHN-BTC** (Chứng khoán — giám sát giao dịch).
- **02/2026/TT-BNG**: tác động toàn bộ hệ thống Bộ Ngoại giao, các cơ quan đại diện Việt Nam ở nước ngoài.
- **26/VBHN-BXD**: tác động ngành vận tải, logistics, giao thông đường bộ.
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, chinhphu.vn, luatvietnam.vn, tuyenquang.gov.vn, seaworld.vn.
- Ngày phát hiện: 2026-06-10 15:01 ICT
- Phiên thực hiện: agent:github-io:subagent:9118ab22-7cfd-47ea-abb2-9bca72853726 (Đệ #1 Discovery 2026-06-10)

---

# Cập nhật 2026-06-11 (phiên Đệ #1 Discovery — 8 nhóm chủ đề)

## Phát hiện mới từ `vanban.chinhphu.vn` (tối đa 5 văn bản/lần)

Quét 8 nhóm chủ đề: Thuế, Đất đai, KHCN, Y tế, Tài chính, Lao động, Giáo dục, Thương mại/Đầu tư. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-10): phát hiện 5 văn bản mới chưa từng được ghi nhận.

> **Lưu ý**: Văn bản số cao nhất trên vanban.chinhphu.vn tính đến 2026-06-10 dừng ở ~202/2026/NĐ-CP. Không có NĐ-CP 203–210 hay NQ-CP 149–202 trong phạm vi ngày 10/6/2026. Toàn bộ docid trên 218XXX vẫn nằm trong nhóm đã tracking.

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 185/2026/NĐ-CP | 26/05/2026 | Quy định về tổ chức, hoạt động của thôn, tổ dân phố và chế độ, chính sách đối với người hoạt động không chuyên trách ở thôn, tổ dân phố — thay thế NĐ 27/2018; quy định số lượng, chức danh, phụ cấp, hỗ trợ; cơ sở pháp lý cho mô hình chính quyền địa phương 2 cấp | Lao động / Hành chính | — | **Đã có** | URL: `https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-185-2026-nd-cp-quy-dinh-ve-to-chuc-hoat-dong-cua-thon-to-dan-pho-chinh-sach-voi-nguoi-hoat-dong-khong-chuyen-trach-o-thon-to-dan-pho-119260526172229782.htm`; tác động toàn bộ hệ thống thôn, tổ dân phố cả nước; bổ sung Chỉ thị 21/CT-TTg (cùng nhóm) |
| 199/2026/NĐ-CP | 05/06/2026 | Quy định chính sách hỗ trợ phục vụ hàng tháng đối với các chức danh, chức vụ lãnh đạo thuộc diện Bộ Chính trị, Ban Bí thư quản lý; cấp bậc hàm trong Công an nhân dân và Quân đội nhân dân — hiệu lực 20/7/2026 | Lao động / Tổ chức bộ máy | — | **Đã có** | URL: `https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-199-2026-nd-cp-quy-dinh-chinh-sach-ho-tro-phuc-vu-doi-voi-cac-chuc-danh-chuc-vu-lanh-dao-119260606134920003.htm`; Phó TT Phạm Gia Túc ký thay TT; tác động lãnh đạo cấp cao QP, CAND |
| 21/CT-TTg | 20/05/2026 | Chỉ thị của Thủ tướng Chính phủ về sắp xếp thôn, tổ dân phố và bố trí, sử dụng, chế độ, chính sách đối với người hoạt động không chuyên trách ở cấp xã, thôn, tổ dân phố — hoàn thành phương án trước 30/6/2026 | Lao động / Hành chính | — | **Chưa có** | URL: `https://xaydungchinhsach.chinhphu.vn/chi-thi-21-ct-ttg-cua-thu-tuong-chinh-phu-ve-sap-xep-thon-to-dan-pho-va-nguoi-hoat-dong-khong-chuyen-trach-119260520170214822.htm`; bổ sung 185/2026/NĐ-CP (cùng nhóm); ảnh hưởng cấp xã toàn quốc |
| Công văn 5691/BNV-TCBC | 06/06/2026 | Hướng dẫn về đơn vị sự nghiệp công lập cung ứng các dịch vụ sự nghiệp công cơ bản, thiết yếu đa ngành, đa lĩnh vực ở cấp xã — UBND cấp xã được quyết định thành lập, giải thể đơn vị sự nghiệp công lập thuộc cấp xã; biên chế giai đoạn 2027–2031 xác định theo vị trí việc làm | Lao động / Hành chính | — | **Chưa có** | URL: `https://luatvietnam.vn/hanh-chinh/cong-van-5691-bnv-tcbc-2026-huong-dan-don-vi-su-nghiep-cong-lap-cung-ung-dich-vu-cong-co-ban-cap-xa-436787-d6.html`; văn bản hành chính mới nhất phát hiện (06/6/2026); tác động cấp xã toàn quốc |
| 148/NQ-CP | 08/06/2026 | Nghị quyết phiên họp Chính phủ thường kỳ tháng 5/2026 — đẩy mạnh giải ngân đầu tư công, đảm bảo cung ứng điện/xăng dầu, phát triển nhà ở xã hội, phát triển thị trường chứng khoán, tinh gọn bộ máy | Kinh tế vĩ mô / Đa ngành | 218349? | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218349` (placeholder); tác động toàn diện kinh tế vĩ mô; cần xác minh docid chính thức |

### Các văn bản phát hiện khác nhóm còn lại (chưa tạo entry — chờ phiên sau)

- **Thuế**: Không có văn bản mới nổi bật ngoài 144/2026/NĐ-CP (sửa thuế GTGT, đã có); 19/QH16, 25/NQ-CP (đã có trong tracking)
- **Đất đai**: 49/2026/NĐ-CP và 50/2026/NĐ-CP (hướng dẫn NQ 254) — đã có trong tracking 2026-06-10; 147/2026/NĐ-CP (dự án tồn đọng) — đã có
- **KHCN**: 05/2026/TT-BKHCN (AI ethics) — đã có trong tracking 2026-06-09 lần 3; 08/2026/TT-BKHCN (xác thực sinh trắc học) — đã có
- **Y tế**: 165/2026/NĐ-CP (Luật Phòng bệnh) — đã có; 15/2026/TT-BYT (phân loại bệnh truyền nhiễm) — đã có; 18/2026/TT-BYT (dược chất kiểm soát) — đã có
- **Tài chính**: 26/2026/TT-BTC (nguồn ngân sách) — đã có; 03/2026/TT-BTC (tự chủ tài chính) — đã có; 202/2026/NĐ-CP (ô tô điện) — đã có; 75/2026/NĐ-CP (tự chủ hành chính) — Chưa có trong tracking
- **Lao động**: 161/2026/NĐ-CP (lương cơ sở) — đã có; 13/2026/TT-BNV, 14/2026/TT-BNV — đã có; 162/2026/NĐ-CP — đã có
- **Giáo dục**: 182/2026/NĐ-CP (phụ cấp nhà giáo) — đã có; 40/2026/TT-BGDĐT (đánh giá rèn luyện SV) — đã có; 66/91/88/93/95/2026/NĐ-CP — đã có
- **Thương mại/Đầu tư**: 96/2026/NĐ-CP (Luật Đầu tư) — đã có; 127/2026/NĐ-CP (Halal) — đã có; 28/2026/TT-BCT (ATTP nhập khẩu) — đã có; 29/2026/TT-BCT (thị trường điện) — đã có

## Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-10)

| Số hiệu | Trong tracking? | Trạng thái |
|---|---|---|
| 185/2026/NĐ-CP | **KHÔNG** | Thêm mới — Đã có |
| 199/2026/NĐ-CP | Có ("Đã có") | Giữ nguyên, cập nhật ghi chú đầy đủ |
| 21/CT-TTg | **KHÔNG** | Thêm mới — Chưa có |
| Công văn 5691/BNV-TCBC | **KHÔNG** | Thêm mới — Chưa có |
| 148/NQ-CP | Không rõ (trùng lặp giữa phiên) | Thêm mới — Chưa có |

## Đề xuất ưu tiên phiên tiếp theo

1. **Lao động / Hành chính**: 185/2026/NĐ-CP — khung pháp lý thôn tổ dân phố mới, tác động 11.000+ thôn/xã toàn quốc; Chỉ thị 21/CT-TTg cùng nhóm nên crawl chung.
2. **Kinh tế vĩ mô**: 148/NQ-CP — nghị quyết phiên họp Chính phủ tháng 5; chỉ đạo đầu tư công, điện, nhà ở xã hội.
3. **Hành chính / Lao động**: Công văn 5691/BNV-TCBC — văn bản hành chính mới nhất, hướng dẫn đơn vị sự nghiệp cấp xã.
4. **Tổ chức bộ máy**: 199/2026/NĐ-CP — chính sách lãnh đạo QP/CAND.
5. **Tài chính**: 75/2026/NĐ-CP (tự chủ hành chính) — Chưa có trong tracking, cần xác minh.

## Ghi chú xử lý

- 5 văn bản mới trên sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- Ưu tiên cao nhất: **185/2026/NĐ-CP + 21/CT-TTg** (cùng nhóm thôn tổ dân phố; ảnh hưởng trực tiếp đời sống hơn 60 triệu dân nông thôn).
- **148/NQ-CP** là nghị quyết vĩ mô, cần xác minh docid chính thức trước khi crawl.
- Công văn 5691/BNV-TCBC là văn bản hành chính (không phải VBQPPL bắt buộc tracking theo SOUL.md), nhưng vì có ngày ban hành mới nhất (06/6) và tác động cấp xã nên được thêm vào.
- Nguồn: web_search Brave tổng hợp vanban.chinhphu.vn, baochinhphu.vn, xaydungchinhsach.chinhphu.vn, luatvietnam.vn, vietnamplus.vn.
- Ngày phát hiện: 2026-06-11 09:45 ICT
- Phiên thực hiện: agent:github-io:subagent:91151c71-c4b5-41d3-a51d-eece4b58f748 (Đệ #1 Discovery 2026-06-11)

---
## Cập nhật 2026-06-13 (phiên Đệ #4 Content Reviewer — lần 1)

### Báo cáo review 5 văn bản trong van-ban/

Quy trình: Đọc OCR_QUALITY_GATE.md → Quét van-ban/ → Chọn 5 file < 10KB, lastedit > 7 ngày → Chạy quality gate → Phân tích → Đánh dấu cần refactor.

#### Kết quả quality gate từng file

**1. `van-ban/cong-nghiep/quan-ly-phan-bon.md`**
- Kích thước: 8.4 KB | 261 dòng | lastedit 2026-05-13 (31 ngày trước)
- Loại: Nghị định 84/2019/NĐ-CP (hết hiệu lực đã được thay thế bởi NĐ 84/2022/NĐ-CP)
- OCR issues: **6** (tất cả là `ngày l` false positive — đúng là "ngày làm việc", không phải lỗi)
  - L86, L106, L112, L120, L178, L206: "02 ngày", "07 ngày", "05 ngày" — không phải lỗi OCR
- Điều: 0 (summary, không phải toàn văn)
- Chương: 0 (summary)
- Metadata: title đúng, layout page, lastedit đúng ngày
- **Đánh giá: ⚠️ CẦN REFACTOR** — Nội dung là bản summary thiếu toàn văn; NĐ gốc 84/2019/NĐ-CP đã bị thay thế bởi NĐ 84/2022/NĐ-CP (thông tin có thể đã lỗi thời); không có heading Điều/Chương.

**2. `van-ban/thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/index.md`**
- Kích thước: 2.8 KB | 54 dòng | lastedit 2026-05-28 (16 ngày trước)
- OCR issues: **0**
- Loại: Index tổng hợp
- Metadata: title không dấu (`Thi dua, khen thuong cac danh hieu vinh du nha nuoc`) — vi phạm checklist; layout page; thiếu docid, source, group, tags
- Ghi chú cuối file: `*Nội dung đang được cập nhật chi tiết.*` — đây là stub, không phải văn bản đầy đủ
- **Đánh giá: ⚠️ CẦN REFACTOR** — Metadata title không dấu; stub có ghi chú "đang cập nhật"; thiếu front matter đầy đủ (không có docid, group, tags, source).

**3. `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md`**
- Kích thước: 5.8 KB | 119 dòng | lastedit 2026-05-29 (15 ngày trước)
- OCR issues: **1** — `ngày L` false positive ở L111 ("ngày 01 tháng 01 năm 2011" — không phải lỗi)
- Loại: Luật 41/2010/QH12 (đã được sửa đổi bổ sung bởi Luật 60/2014/QH13, Luật 71/2014/QH13, Luật 107/2017/QH14, Nghị quyết 19/2026/QH16)
- Metadata: title đúng tiếng Việt; layout page; lastedit đúng; thiếu docid (chỉ có trong nguồn tham khảo)
- Ghi chú cuối: "Để tra cứu nội dung đầy đủ, tham khảo nguồn chính thức" — summary, không phải toàn văn
- **Đánh giá: ⚠️ CẦN REFACTOR** — Luật gốc 2010 đã nhiều lần sửa đổi; nội dung là summary thiếu Điều (không có toàn văn); cần cập nhật liên kết 19/2026/QH16; thiếu docid chính thức.

**4. `van-ban/tai-chinh/gia.md`**
- Kích thước: 10.0 KB | 193 dòng | lastedit 2026-05-29 (15 ngày trước)
- OCR issues: **2** — `ngày L` false positive ở L181, L189 (đúng "ngày" không phải lỗi)
- Loại: Luật 16/2023/QH15 (Luật Giá 2023, 8 Chương 75 Điều, hiệu lực 01/7/2024)
- Metadata: title đúng; layout page; lastedit đúng; source đầy đủ (vanban.chinhphu.vn + datafiles PDF)
- Cấu trúc: summary có cấu trúc rõ ràng, ghi rõ range Điều mỗi Chương
- Chú thích: "Nội dung dưới đây là tổng hợp các quy định chính" — đúng là summary
- **Đánh giá: ✅ CHẤP NHẬN ĐƯỢC** (nhưng ghi nhận là summary) — OCR sạch; metadata đầy đủ; nội dung có cấu trúc; nguồn PDF chính thức đầy đủ 75 Điều có thể tra cứu. Không cần refactor ngay.

**5. `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md`**
- Kích thước: 3.1 KB | 57 dòng | lastedit 2026-05-26 (18 ngày trước)
- OCR issues: **0**
- Loại: Nghị định 04/2015/NĐ-CP (hết hiệu lực từ 01/07/2023, thay thế bởi Luật 10/2022/QH15)
- Metadata: title đầy đủ; layout page; source đầy đủ; có ghi chú hết hiệu lực rõ ràng
- Nội dung: summary ngắn gọn về Luật 10/2022/QH15
- **Đánh giá: ⚠️ CẦN REFACTOR** — Nghị định gốc 04/2015/NĐ-CP đã hết hiệu lực; nội dung chỉ là summary rất ngắn về Luật mới; file nên được chuyển thành trang giới thiệu cho Luật 10/2022/QH15 hoặc xóa nếu đã có trang chuyên biệt cho Luật đó.

### Tổng hợp file cần refactor

| File | Size | Lastedit | Vấn đề chính | Ưu tiên |
|---|---|---|---|---|
| `van-ban/cong-nghiep/quan-ly-phan-bon.md` | 8.4 KB | 2026-05-13 | Summary, NĐ gốc đã lỗi thời (thay thế bởi NĐ 84/2022) | Cao |
| `van-ban/thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/index.md` | 2.8 KB | 2026-05-28 | Metadata title không dấu; stub; thiếu front matter đầy đủ | Cao |
| `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/thue-tai-nguyen.md` | 5.8 KB | 2026-05-29 | Summary thiếu toàn văn; Luật đã nhiều lần sửa đổi; thiếu docid | Trung bình |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md` | 3.1 KB | 2026-05-26 | NĐ gốc hết hiệu lực; nội dung summary ngắn; cần chuyển sang trang Luật 10/2022 | Trung bình |

### File đạt quality gate

| File | Ghi chú |
|---|---|
| `van-ban/tai-chinh/gia.md` | OCR sạch; metadata đầy đủ; summary có cấu trúc; nguồn chính thức đầy đủ |

### File tiếp theo cần review (batch 2)

Danh sách file nghi ngờ cần review tiếp (lọc từ quét van-ban/):

| File | Size | Lastedit | Ghi chú |
|---|---|---|---|
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/kiem-tra-va-xu-ly-van-ban-quy-pham-phap-luat.md` | 7.1 KB | 2026-06-01 | Stub? |
| `van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/theo-doi-tinh-hinh-thi-hanh-phap-luat.md` | 7.4 KB | 2026-06-01 | Stub? |
| `van-ban/ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu...sang-tieng-anh-de-giao-dich-doi-ngoai.md` | 4.9 KB | 2026-05-29 | Stub rất ngắn |
| `van-ban/cong-nghiep/quan-ly-phan-bon.md` | 8.6 KB | 2026-05-13 | Đã đánh dấu cần refactor |
| `van-ban/thi-dua-khen-thuong-cac-danh-hieu-vinh-du-nha-nuoc/index.md` | 2.9 KB | 2026-05-28 | Đã đánh dấu cần refactor |

### Ghi chú xử lý

- **Lưu ý**: Các báo cáo `ngày l` và `ngày L` trong kết quả scan là **false positive** — đây là các chuỗi "ngày" đúng trong ngữ cảnh "02 ngày", "07 ngày" chứ không phải lỗi OCR "ngày 17", "ngày 15". Không cần sửa.
- 4 file cần refactor sẽ được xử lý trong phiên Đệ #5 Refactor tiếp theo.
- Chủ động ghi nhận: `van-ban/tai-chinh/gia.md` đạt chuẩn, không cần xử lý.
- Nguồn review: scan van-ban/ + OCR_QUALITY_GATE.md.
- Ngày review: 2026-06-13 14:57 ICT
- Phiên thực hiện: agent:github-io:subagent:01898d0c-d239-4d2b-a0ae-4f9ed2832ba2 (Đệ #4 Content Reviewer 2026-06-13)


---
## Cập nhật 2026-06-13 (phiên Đệ #1 Discovery — lần 13)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét toàn bộ docid 218XXX trên vanban.chinhphu.vn + thuvienphapluat.vn + baomoi.com/báo chính thức (tuần 8-12/6/2026). So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-13 lần 12): phát hiện **3 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận 3:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 201/2026/NĐ-CP | 08/06/2026 | Sửa đổi, bổ sung thuế suất thuế xuất khẩu một số mặt hàng tại Biểu thuế xuất khẩu kèm NĐ 26/2023/NĐ-CP — cụ thể: Khoáng fluorite (HS 2529.22.00, CaF₂ >97%) giảm thuế suất từ 10% xuống 5%; tác động ngành khoáng sản xuất khẩu | Thuế / Xuất khẩu | **Chưa có** | Nguồn: baomoi.com (báo Chính phủ tuần 6-12/6); tác động ngành khai khoáng xuất khẩu; cần xác minh docid trên vanban.chinhphu.vn |
| 197/2026/NĐ-CP | ~08/06/2026 | Quy định cơ sở dữ liệu quốc gia về tiếp công dân, xử lý đơn, giải quyết khiếu nại, tố cáo — thẩm quyền, phạm vi khai thác dữ liệu; quy định quyền truy cập của Tổng Bí thư, Chủ tịch nước, Thủ tướng, Chủ tịch QH | Hành chính / Tư pháp | **Chưa có** | Nguồn: baomoi.com (báo Chính phủ); tác động toàn bộ hệ thống tiếp công dân, khiếu nại, tố cáo cả nước; cần xác minh ngày ban hành và docid |
| 1033/QĐ-TTg | ~08/06/2026 | Phê duyệt Chương trình phát triển kinh tế số và xã hội số giai đoạn 2026-2030 — mục tiêu xây dựng nền kinh tế số năng động dựa trên nền tảng số, dữ liệu và AI; kiến tạo xã hội số văn minh, an toàn và bao trùm; Phó Thủ tướng Hồ Quốc Dũng ký | KHCN / Kinh tế số | **Chưa có** | Nguồn: baomoi.com (báo Chính phủ); tác động chiến lược toàn nền kinh tế số; cần xác minh ngày ký và docid chính thức |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-13 lần 12)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 201/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 197/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 1033/QĐ-TTg | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo

1. **Thuế / Xuất khẩu**: **201/2026/NĐ-CP** — sửa thuế suất xuất khẩu khoáng fluorite; tác động ngành khai khoáng xuất khẩu; cần xác minh xem có mặt hàng khác không.
2. **Hành chính / Tư pháp**: **197/2026/NĐ-CP** — CSDL quốc gia tiếp công dân, khiếu nại, tố cáo; tác động hệ thống hành chính toàn quốc.
3. **KHCN / Kinh tế số**: **1033/QĐ-TTg** — chương trình kinh tế số 2026-2030; tác động chiến lược toàn nền kinh tế số.
4. **Tư pháp**: Các văn bản đã tracking từ lần 11 và 12 (203, 199, 193, 45, 28 NĐ-CP/TT-BGDĐT/TT-BXD) — ưu tiên cao, cần crawl chi tiết.
5. **Năng lượng**: 28/2026/NQ-CP (khai thác than) đã có từ lần 11.

### Ghi chú xử lý

- **3 văn bản mới** sẽ được crawl chi tiết trong các phiên "Đệ #3 Full Content Crawler" tiếp theo.
- **201/2026/NĐ-CP**: Từ báo cáo tuần 6-12/6 của báo Chính phủ trên baomoi.com; cần xác minh docid; chỉ có 1 mặt hàng được đề cập (fluorite) — có thể còn mặt hàng khác trong NĐ.
- **197/2026/NĐ-CP**: Từ báo cáo tuần 6-12/6; tác động cơ sở dữ liệu hành chính quốc gia; cần xác minh ngày ban hành chính xác.
- **1033/QĐ-TTg**: Từ báo cáo tuần 6-12/6; Phó TT Hồ Quốc Dũng ký; liên quan đến chương trình chuyển đổi số quốc gia.
- Không tìm thấy NĐ-CP 203-212 trên vanban.chinhphu.vn — 203-212 chưa được ban hành hoặc chưa công bố tính đến 2026-06-13.
- Các văn bản 203, 199, 193, 45, 28 từ lần 12 chưa crawl → tiếp tục ưu tiên.
- Nguồn: baomoi.com (báo Chính phủ tuần 6-12/6), vanban.chinhphu.vn docid 218XXX, thuvienphapluat.vn.
- Ngày phát hiện: 2026-06-13 17:00 ICT
- Phiên thực hiện: agent:github-io:subagent:cbb8fd29-cfef-4f21-bcea-86d2c1abd028 (Đệ #1 Discovery 2026-06-13 lần 13)

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 3, văn bản 28/2026/NQ-CP)

### Crawler chi tiết văn bản 28/2026/NQ-CP

Hoàn thiện crawl + Markdown hóa **28/2026/NQ-CP** theo quy trình Signed PDF OCR Pipeline (PDF gốc ký số CAdES-BES tại datafiles.chinhphu.vn, 4 trang) + cross-check với luatvietnam.vn.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 28/2026/NQ-CP | **Đã có (2026-06-14, OCR từ PDF gốc ký số, nội dung đầy đủ 7 Điều)** | `van-ban/nang-luong-tai-nguyen/nghi-quyet-28-2026-nq-cp-co-che-khai-thac-than-vuot-15-phan-tram-cong-suat.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218385`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/28-nqcp.signed.pdf` (4 trang, 261KB, CAdES-BES ký 10/6/2026 14:14:14); người ký: Phó Thủ tướng Phạm Gia Túc (KT. Thủ tướng theo phân công); 7 Điều, không có Chương; 146 dòng, 11.5KB; OCR issues = 0 (1 false positive "ngày l" - thực chất là "ngày làm việc"); articles 1-7 đầy đủ, không thiếu, không trùng; layout: vanban; file cũ slug `...-khai-thac-than.md` (ghi nhầm người ký = Chủ nhiệm VPCP - sai, PGT Phạm Gia Túc từ tháng 4/2026) đã xóa, thay thế bằng file mới slug chuẩn với nội dung đầy đủ và người ký chính xác |

### Cấu trúc 28/2026/NQ-CP

- **Điều 1**: Phạm vi điều chỉnh và đối tượng áp dụng — cơ chế đặc thù, rút gọn thủ tục cho phép khai thác vượt công suất giấy phép khoáng sản than
- **Điều 2**: Nguyên tắc áp dụng — bảo đảm an ninh năng lượng; không vượt trữ lượng; sản lượng vượt chỉ phục vụ sản xuất điện
- **Điều 3**: Cơ chế khai thác vượt công suất — vượt không quá 15% công suất GP; không phải điều chỉnh nội dung GP
- **Điều 4**: Điều kiện áp dụng — GP còn hiệu lực; đủ năng lực kỹ thuật; bảo đảm ATLĐ, ATVSTM; trữ lượng còn được cấp phép
- **Điều 5**: Thủ tục đăng ký và kiểm soát — gửi UBND cấp tỉnh + Bộ NN&MT; UBND trả lời trong 5 ngày làm việc
- **Điều 6**: Giám sát, báo cáo và xử lý vi phạm
- **Điều 7**: Tổ chức thực hiện và hiệu lực thi hành — hiệu lực đến hết 31/12/2027

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-13)

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 28/2026/NQ-CP | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Chưa có (file cũ chỉ có stub) | **Đã có (nội dung đầy đủ)** (2026-06-14) |

### Ghi chú xử lý

- File path dùng slug chuẩn mới `co-che-dac-thu-khai-thac-than` (thay vì slug cũ `khai-thac-than-vuot-cong-suat` từ PR #208 chỉ có stub metadata).
- File cũ stub đã xóa; file mới có đầy đủ 7 Điều + căn cứ pháp lý + nơi nhận.
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Phiên thực hiện: agent:github-io:subagent:a8e4fe33-3d87-45f8-ba10-23b970879cb4 (Đệ #3 Full Content Crawler 28/2026/NQ-CP).

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 4)

### Crawler chi tiết văn bản 30/2026/TT-BCT

Hoàn thiện crawl + Markdown hóa **30/2026/TT-BCT** theo quy trình Signed PDF OCR (PDF gốc tại datafiles.chinhphu.vn, 5.3MB, KHÔNG có chữ ký số → `pdftotext` chỉ trả 21 bytes vì PDF là bản scan) + fallback OCR toàn trang (21 trang PNG @ 200 DPI) + cross-check với luatvietnam.vn, moit.gov.vn, baophapluat.vn.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 30/2026/TT-BCT | **Đã có (2026-06-14, OCR fallback từ PDF gốc, cross-check đa nguồn)** | `van-ban/dau-tu/thong-tu-30-2026-tt-bct-phuong-phap-xac-dinh-gia-dich-vu-phat-dien-nha-may-dien-bot.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218414`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/30-bct.pdf` (5.3MB, 21 trang, PDF scan từ HP Scan + iText); người ký: Nguyễn Hoàng Long (Thứ trưởng Bộ Công Thương); ngày ban hành: 10/6/2026; hiệu lực: 28/7/2026 (còn 44 ngày); 16 Điều + 4 Chương (I, II, III, IV); 642 dòng, 43KB; OCR issues = 0; articles 1-16 đầy đủ, không thiếu, không trùng; IRR tối đa 12% (Điều 3 khoản 1b) |

### Cấu trúc 30/2026/TT-BCT

- **Chương I** (Điều 1-2): Quy định chung — phạm vi điều chỉnh, giải thích từ ngữ
- **Chương II** (Điều 3-8): Phương pháp xác định giá năm cơ sở
  - **Điều 3**: Nguyên tắc xác định giá dịch vụ phát điện (IRR ≤ 12%)
  - **Điều 4**: Phương pháp xác định giá công suất, giá điện năng năm cơ sở
  - **Điều 5-6**: Phương pháp xây dựng giá cố định bình quân + vận hành bảo dưỡng cố định
  - **Điều 7-8**: Phương pháp xác định giá nhiên liệu biến đổi + vận hành bảo dưỡng biến đổi
- **Chương III** (Điều 9-11): Điều chỉnh giá dịch vụ phát điện từng năm trong HĐMBĐ, phương pháp xác định giá tại thời điểm thanh toán, tiền điện thanh toán
- **Chương IV** (Điều 12-16): Trách nhiệm Cục Điện lực, bên mua điện, bên bán điện; điều chỉnh giá; hiệu lực thi hành
- **Phụ lục**: Biểu mẫu 1, 2 (dạng bảng biểu phức tạp, đệ #3 ghi chú ngắn thay vì OCR dạng bảng để tránh sai nghĩa)

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md` (đến 2026-06-13)

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 30/2026/TT-BCT | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (16 Điều + 4 Chương + Phụ lục I)** (2026-06-14) | **Đã có (16 Điều + 4 Chương)** (2026-06-14) |

### Ghi chú xử lý

- File path dùng slug `thong-tu-30-2026-tt-bct-phuong-phap-xac-dinh-gia-dich-vu-phat-dien-nha-may-dien-bot` (chuẩn SEO).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: dùng underscore snake_case (`so_hieu`, `ngay_ban_hanh`, `nguoi_ky`, `chuc_vu_nguoi_ky`, `co_quan_ban_hanh`, `linh_vuc`, `trang_thai`) + có thêm `trich_yeu`, `pdf_goc`. Cấu trúc hơi khác với các file khác (thường dùng `Số hiệu` CamelCase) — Sếp có thể chuẩn hóa sau nếu muốn.
- Phiên thực hiện: agent:github-io:subagent:301b4572-6e11-4c68-a93d-b07c523558e8 (Đệ #3 Full Content Crawler 30/2026/TT-BCT).
- IRR 12% — đây là điểm quan trọng nhất của Thông tư: giới hạn tỷ suất sinh lợi nội tại tối đa 12% cho dự án BOT nhà máy điện.
- Áp dụng cho nhà máy điện BOT chưa ký hợp đồng mua bán điện.

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 5)

### Crawler chi tiết văn bản 63/2026/TT-BTC

Hoàn thiện crawl + Markdown hóa **63/2026/TT-BTC** theo quy trình Signed PDF OCR (PDF gốc tại datafiles.chinhphu.vn, 1.93MB, 5 trang, KHÔNG có chữ ký số) + fallback OCR toàn trang (250 DPI) + cross-check với luatvietnam.vn.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 63/2026/TT-BTC | **Đã có (2026-06-14, OCR fallback từ PDF gốc, cross-check luatvietnam.vn)** | `van-ban/giao-duc-dao-tao/thong-tu-63-2026-tt-btc-noi-dung-muc-chi-thi-ky-nang-nghe.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218416`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/63-btc.pdf` (1.93MB, 5 trang, PDF scan); người ký: Nguyễn Thị Bích Ngọc (KT. Bộ trưởng - Thứ trưởng); ngày ban hành: 05/6/2026; hiệu lực: 05/6/2026 (trễ 9 ngày); 7 Điều; 191 dòng, 15.7KB; OCR issues = 0; articles 1-7 đầy đủ, không thiếu, không trùng |

### Cấu trúc 63/2026/TT-BTC

- **Điều 1**: Phạm vi điều chỉnh
- **Điều 2**: Nguồn kinh phí thực hiện
- **Điều 3**: Nguyên tắc quản lý, sử dụng kinh phí
- **Điều 4**: Nội dung và mức chi chung
- **Điều 5**: Nội dung và mức chi thi kỹ năng nghề trong nước
- **Điều 6**: Nội dung và mức chi đối với thi kỹ năng nghề quốc tế
- **Điều 7**: Điều khoản thi hành

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 63/2026/TT-BTC | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (7 Điều, không Chương/Phụ lục)** (2026-06-14) | **Đã có (7 Điều)** (2026-06-14) |

### Ghi chú xử lý

- File path dùng slug `thong-tu-63-2026-tt-btc-noi-dung-muc-chi-thi-ky-nang-nghe` (chuẩn SEO).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: chuẩn CamelCase, đầy đủ các trường bắt buộc (`date`, `modified`, `group`, `tags`, `docid`, `source`).
- Phiên thực hiện: agent:github-io:subagent:89e3ee43-64b5-4f76-840f-9d67f466947c (Đệ #3 Full Content Crawler 63/2026/TT-BTC).
- Văn bản thay thế Thông tư liên tịch 43/2012/TTLT-BTC-BLĐTBXH ngày 14/03/2012.
- Mức chi: 1 triệu đồng/bộ hồ sơ/đề thi; đồ bảo hộ tối đa 1 triệu/người.
- Áp dụng cho hoạt động thi kỹ năng nghề trong nước và quốc tế.

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 6)

### Crawler chi tiết văn bản 60/2026/TT-BTC

Hoàn thiện crawl + Markdown hóa **60/2026/TT-BTC** theo quy trình Signed PDF OCR (PDF gốc tại datafiles.chinhphu.vn, 7.5MB, 17 trang, KHÔNG có chữ ký số) + fallback OCR toàn trang (200 DPI) + cross-check với luatvietnam.vn.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 60/2026/TT-BTC | **Đã có (2026-06-14, OCR fallback từ PDF gốc, cross-check luatvietnam.vn)** | `van-ban/tai-chinh/thong-tu-60-2026-tt-btc-huong-dan-quan-ly-su-dung-quyet-toan-kinh-phi-chuong-trinh-muc-tieu-quoc-gia.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218378`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/60-btc.pdf` (7.5MB, 17 trang, PDF scan); người ký: KT. Bộ trưởng - Thứ trưởng Phạm Bích Ngọc; ngày ban hành: 31/05/2026; hiệu lực: 31/05/2026 (trễ 14 ngày); 22 Điều + 4 Chương (I, II, III, IV); 393 dòng, 57.6KB; OCR issues = 0; articles 1-22 đầy đủ, không thiếu, không trùng |

### Cấu trúc 60/2026/TT-BTC

- **Chương I** (Điều 1-4): Quy định chung
  - Điều 1: Phạm vi điều chỉnh và đối tượng áp dụng
  - Điều 2: Nguồn kinh phí chi thường xuyên NSNN
  - Điều 3: Lập dự toán, chấp hành và quyết toán NSNN
  - Điều 4: Một số nội dung và mức chi chung
- **Chương II** (Điều 5-14): Nội dung thành phần Chương trình NTM/giảm nghèo (10 thành phần)
  - Điều 5-14: 10 thành phần từ quy hoạch đến nâng cao năng lực, truyền thông, giám sát
- **Chương III** (Điều 15-19): Nội dung thành phần vùng đồng bào DTTS và miền núi (5 thành phần)
  - Điều 15: Đầu tư xây dựng cơ sở hạ tầng đặc thù
  - Điều 16: Hỗ trợ phát triển sản xuất, sinh kế
  - Điều 17: Phát triển nguồn nhân lực
  - Điều 18: Chính sách đặc thù ưu tiên dân tộc khó khăn
  - Điều 19: Truyền thông + chuyển đổi số
- **Chương IV** (Điều 20-22): Hiệu lực, điều khoản chuyển tiếp, tổ chức thực hiện

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 60/2026/TT-BTC | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (22 Điều + 4 Chương)** (2026-06-14) |

### Ghi chú xử lý

- File path dùng slug `thong-tu-60-2026-tt-btc-huong-dan-quan-ly-su-dung-quyet-toan-kinh-phi-chuong-trinh-muc-tieu-quoc-gia` (chuẩn SEO).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: chuẩn, đầy đủ các trường bắt buộc.
- Phiên thực hiện: agent:github-io:subagent:4da2a280-4da2-4e07-8b10-406798a869b0 (Đệ #3 Full Content Crawler 60/2026/TT-BTC).
- Văn bản thay thế: Thông tư 55/2023/TT-BTC + 175/2024/TT-BTC + 112/2025/TT-BTC.
- Áp dụng cho Chương trình mục tiêu quốc gia giai đoạn 2026-2030.
- Căn cứ: Luật NSNN 89/2025/QH15, NQ 257/2025/QH15, QĐ 16/2026/QĐ-TTg.
- Lỗi OCR đã sửa: `Chương Ï` → `Chương I`, `BNNMITT` → `BNNMT`, `ĐIÊU KHOẢN` → `ĐIỀU KHOẢN`, v.v.

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 7)

### Crawler chi tiết văn bản 19/2026/TT-NHNN

Hoàn thiện crawl + Markdown hóa **19/2026/TT-NHNN** theo quy trình Signed PDF OCR (PDF gốc tại datafiles.chinhphu.vn, 1MB, 3 trang, có chữ ký số che số ngày ở Điều 4) + OCR 200dpi + cross-check với luatvietnam.vn.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 19/2026/TT-NHNN | **Đã có (2026-06-14, OCR fallback từ PDF gốc, cross-check luatvietnam.vn)** | `van-ban/ngan-hang/thong-tu-19-2026-tt-nhnn-phan-cap-thu-tuc-hanh-chinh-thu-nghiem.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218234`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/19-nhnn.pdf` (1MB, 3 trang, có chữ ký số CAdES-BES); người ký: Phạm Tiến Dũng (KT. Thống đốc - Phó Thống đốc); ngày ban hành: 19/05/2026; hiệu lực: 30/06/2026 (theo metadata chính thức, OCR không đọc được số ngày ở Điều 4 vì chữ ký số che); 6 Điều (Điều 1-6); 129 dòng, 7.2KB; OCR issues = 0; articles 1-6 đầy đủ, không thiếu, không trùng |

### Cấu trúc 19/2026/TT-NHNN

- **Điều 1**: Phạm vi điều chỉnh
- **Điều 2**: Đối tượng áp dụng
- **Điều 3**: Nội dung phân cấp (Open-API, chấm điểm tín dụng, sandbox)
- **Điều 4**: Hiệu lực thi hành
- **Điều 5**: Điều khoản chuyển tiếp
- **Điều 6**: Tổ chức thực hiện

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 19/2026/TT-NHNN | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (6 Điều)** (2026-06-14) |

### Ghi chú xử lý

- File path: `van-ban/ngan-hang/thong-tu-19-2026-tt-nhnn-phan-cap-thu-tuc-hanh-chinh-thu-nghiem.md` (group `ngan-hang` đã có sẵn, đúng lĩnh vực).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: kết hợp CamelCase + underscore snake_case (`so_hieu`, `loai_van_ban`, ...) — khác format các file khác, đề xuất chuẩn hóa sau.
- Phiên thực hiện: agent:github-io:subagent:480fb042-dc46-4f8c-9fd0-7e35e048a0ab (Đệ #3 Full Content Crawler 19/2026/TT-NHNN).
- Văn bản quy định phân cấp thủ tục hành chính tại Nghị định 94/2025/NĐ-CP (Cơ chế thử nghiệm có kiểm soát / sandbox trong lĩnh vực ngân hàng).
- Căn cứ: Nghị định 94/2025/NĐ-CP, Luật Các tổ chức tín dụng 2024.
- Lưu ý: chữ ký số CAdES-BES che số ngày hiệu lực trong PDF, phải cross-check luatvietnam.vn.

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 8)

### Crawler chi tiết văn bản 153/2026/NĐ-CP (refactor stub)

Hoàn thiện refactor file stub `van-ban/hai-quan-thuong-mai/nghi-dinh-153-2026-nd-cp-hai-quan-phong-chong-buon-lap.md` (cũ 4269 bytes, 69 dòng, stub "Đang cập nhật") thành file Markdown hoàn chỉnh **toàn văn 104657 bytes, 1907 dòng**.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 153/2026/NĐ-CP | **Đã có (2026-06-14, refactor từ stub, OCR fallback từ PDF Công báo 858KB 42tr, cross-check phucgia.com.vn + luatvietnam.vn)** | `van-ban/hai-quan-thuong-mai/nghi-dinh-153-2026-nd-cp-hai-quan-phong-chong-buon-lap.md` | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218083`; PDF: `https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469525-1779329426_v1_1779843312_signed.pdf` (Công báo số 286, 858KB, 42 trang, PDF scan); người ký: Phạm Gia Túc (Phó Thủ tướng, thừa ủy quyền Thủ tướng); ngày ban hành: 14/05/2026; hiệu lực: 05/07/2026; Công báo: số 286 (27/05/2026); 7 Điều (Điều 1-7) + Phụ lục 22 tỉnh/thành; OCR issues = 0; articles 1-7 đầy đủ, không thiếu, không trùng |

### Cấu trúc 153/2026/NĐ-CP

- **Điều 1**: Sửa đổi, bổ sung Điều 3 (phạm vi địa bàn hoạt động hải quan)
- **Điều 2**: Sửa đổi, bổ sung các khoản 2, 3, 5, 8 [Điều 3]
- **Điều 3**: Sửa đổi, bổ sung khoản 1 Điều 11 (cơ chế phối hợp liên ngành)
- **Điều 4**: Sửa đổi, bổ sung điểm a khoản 1 Điều 12
- **Điều 5**: Thay thế Phụ lục, bãi bỏ một số khoản
- **Điều 6**: Điều khoản thi hành
- **Điều 7**: Trách nhiệm thi hành
- **Phụ lục** (22 tỉnh/thành với cửa khẩu/lối thông quan/đường chuyên dụng):
  Quảng Ninh, Lạng Sơn, Cao Bằng, Tuyên Quang, Lào Cai, Lai Châu, Điện Biên, Sơn La, Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Trị, Thành phố Huế, Đà Nẵng, Quảng Ngãi, Lâm Đồng, Gia Lai, Đắk Lắk, Đồng Nai, Tây Ninh, Đồng Tháp, An Giang

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 153/2026/NĐ-CP | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có (stub <10KB) | **Đã có (7 Điều + Phụ lục 22 tỉnh/thành)** (2026-06-14) |

### Ghi chú xử lý

- File path: `van-ban/hai-quan-thuong-mai/nghi-dinh-153-2026-nd-cp-hai-quan-phong-chong-buon-lap.md` (group `hai-quan-thuong-mai` đã có sẵn, đúng lĩnh vực).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: kết hợp CamelCase + underscore snake_case (`so`, `ngay`, `nguoi_ky`, `hieu_luc`, ...) — giữ format cũ của stub.
- Phiên thực hiện: agent:github-io:subagent:47559d3f-cb7a-4cc2-8f43-f29219bfb93b (Đệ #3 Full Content Crawler 153/2026/NĐ-CP).
- PDF gốc từ Công báo (congbaocdn.chinhphu.vn), KHÔNG phải datafiles.chinhphu.vn (URL 404).
- Văn bản sửa đổi NĐ 01/2015/NĐ-CP + NĐ 12/2018/NĐ-CP, mở rộng địa bàn hải quan.
- Phụ lục 22 tỉnh/thành kèm 68 cửa khẩu/lối thông quan/đường chuyên dụng — đã giữ nguyên, không rút gọn.
- Stub cũ đã được ghi đè hoàn toàn, không còn "Đang cập nhật", "trang_thai: Đang cập nhật", "chuthich".
- Có thông tin vị trí địa lý chi tiết (toạ độ) cho từng cửa khẩu (~1300 dòng).

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 9)

### Crawler chi tiết văn bản 56/2026/TT-BCA (lần đầu dùng Công báo CDN)

Hoàn thiện crawl + Markdown hóa **56/2026/TT-BCA** theo quy trình Signed PDF OCR (PDF gốc từ Công báo chính phủ 653KB, 9 trang, có chữ ký số). Đây là lần đầu tiên sử dụng nguồn Công báo CDN (congbaocdn.chinhphu.vn) thay cho datafiles.chinhphu.vn (URL datafiles 404).

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 56/2026/TT-BCA | **Đã có (2026-06-14, pdftotext thành công 26KB, cross-check luatvietnam.vn)** | `van-ban/cong-an/thong-tu-56-2026-tt-bca-quan-ly-theo-doi-nguoi-bi-cam-di-khoi-noi-cu-tru.md` | URL metadata: `https://congbao.chinhphu.vn/van-ban/thong-tu-so-56-2026-tt-bca-469655.htm`; PDF: `https://congbaocdn.chinhphu.vn/180507251028987904/2026/6/10/469655-1781059064_v1_1781085618_signed.pdf` (653KB, 9 trang, có chữ ký số); Số Công báo: 323; người ký: Đại tướng Lương Tam Quang (Bộ trưởng Bộ Công an); ngày ban hành: 15/05/2026; hiệu lực: 01/07/2026 (chưa có hiệu lực, còn 17 ngày); 18 Điều (Điều 1-18) + 4 Chương (I, II, III, IV); 324 dòng, 29.8KB; OCR issues = 0 nghiêm trọng; `VNeID` là tên viết tắt chính thức của ứng dụng định danh điện tử Bộ Công an, không phải lỗi OCR; articles 1-18 đầy đủ, không thiếu, không trùng |

### Cấu trúc 56/2026/TT-BCA

- **Chương I** (Điều 1-3): QUY ĐỊNH CHUNG
  - Điều 1: Phạm vi điều chỉnh
  - Điều 2: Đối tượng áp dụng
  - Điều 3: Giải thích từ ngữ
- **Chương II** (Điều 4-12): TIẾP NHẬN, QUẢN LÝ, THEO DÕI
  - Điều 4: Tiếp nhận lệnh cấm đi khỏi nơi cư trú
  - Điều 5-7: Trình tự, thủ tục quản lý
  - Điều 8-12: Theo dõi, cập nhật Cơ sở dữ liệu quốc gia về dân cư, VNeID
- **Chương III** (Điều 13-16): TRÁCH NHIỆM CỦA CÔNG AN CÁC ĐƠN VỊ, ĐỊA PHƯƠNG
  - Điều 13-16: Phân cấp trách nhiệm Công an các cấp
- **Chương IV** (Điều 17-18): ĐIỀU KHOẢN THI HÀNH
  - Điều 17: Hiệu lực thi hành
  - Điều 18: Trách nhiệm thi hành

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 56/2026/TT-BCA | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (18 Điều + 4 Chương)** (2026-06-14) |

### Ghi chú xử lý

- File path: `van-ban/cong-an/thong-tu-56-2026-tt-bca-quan-ly-theo-doi-nguoi-bi-cam-di-khoi-noi-cu-tru.md` (group `cong-an` đã có sẵn, đúng lĩnh vực).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: kết hợp CamelCase + underscore snake_case (`so`, `ngay`, ...) + có `de_nghi`, `bo`, `hieu_luc`, `nguoi_ky`, `so_cong_bao`.
- Phiên thực hiện: agent:github-io:subagent:0f45a752-a31d-4727-858b-9034e802e999 (Đệ #3 Full Content Crawler 56/2026/TT-BCA).
- Văn bản **CHƯA CÓ HIỆU LỰC** (01/07/2026) - đã ghi chú trong file.
- Căn cứ: BLTTHS 101/2015/QH13 (sửa đổi bởi 6 Luật), Luật 128/2025/QH15 (THTG, TG, cấm cư trú), NĐ 02/2025/NĐ-CP (sửa đổi bởi NĐ 11/2025/NĐ-CP).
- Lần đầu dùng nguồn Công báo CDN thay vì datafiles.chinhphu.vn → đây là pattern mới cho các văn bản chưa có docid trên vanban.chinhphu.vn.
- docid dùng trong front matter = `469655` (Công báo ID) thay vì `218xxx` (vanban.chinhphu.vn ID) vì văn bản này chưa có trên vanban.chinhphu.vn.
- Cross-check: luatvietnam.vn (slug 436803 dùng làm tag) + Công báo chính phủ + luatvietnam.vn.

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 10)

### Crawler chi tiết văn bản 35/2026/TT-BTC

Hoàn thiện crawl + Markdown hóa **35/2026/TT-BTC** theo quy trình Signed PDF OCR (PDF gốc 11.1MB, 25 trang, có chữ ký số từ storage-vnportal.vnpt.vn UBND tỉnh Ninh Bình). pdftotext chỉ trả 131 bytes (PDF có chữ ký số, không text layer) → fallback OCR 200 DPI tesseract.

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 35/2026/TT-BTC | **Đã có (2026-06-14, OCR 25 trang, 7 Chương + 35 Điều + Phụ lục)** | `van-ban/tai-chinh/thong-tu-35-2026-tt-btc-che-do-tiep-khach-nuoc-ngoai-hoi-nghi-quoc-te-tai-viet-nam.md` | PDF: `https://storage-vnportal.vnpt.vn/nbh-ubnd/2925/N%C4%83m%202026/VB%20%C4%91%C3%ADnh%20k%C3%A8m/35_03042026_171635.pdf` (11.1MB, 25 trang, có chữ ký số); datafiles.chinhphu.vn URL 404; người ký: KT. Bộ trưởng - Thứ trưởng Nguyễn Thị Bích Ngọc; ngày ban hành: 31/03/2026; hiệu lực: 18/05/2026 (ĐÃ CÓ HIỆU LỰC); 35 Điều (Điều 1-35) + 7 Chương (I, II, III, IV, V, VI, VII) + Phụ lục cấp hạng khách quốc tế; 675 dòng, 91.8KB; OCR issues = 0; articles 1-35 đầy đủ, không thiếu, không trùng; Cross-check luatvietnam.vn (slug 430995) |

### Cấu trúc 35/2026/TT-BTC (7 Chương — khác với phỏng đoán 4 Chương ban đầu)

- **Chương I** (Điều 1-4): QUY ĐỊNH CHUNG
  - Điều 1: Phạm vi điều chỉnh
  - Điều 2: Đối tượng áp dụng
  - Điều 3: Nguồn kinh phí
  - Điều 4: Quy định chung về chế độ tiếp khách
- **Chương II** (Điều 5-15): CHẾ ĐỘ TIẾP KHÁCH NƯỚC NGOÀI — VIỆT NAM CHI TOÀN BỘ CHI PHÍ
  - Điều 5: Đón, tiễn khách tại sân bay
  - Điều 6: Tiêu chuẩn xe ô tô
  - Điều 7: Tiêu chuẩn thuê chỗ ở
  - Điều 8: Tiêu chuẩn ăn hàng ngày
  - Điều 9: Chiêu đãi
  - Điều 10: Tiếp xã giao
  - Điều 11: Dịch thuật
  - Điều 12: Chi văn hoá, văn nghệ và tặng phẩm
  - Điều 13: Tiêu chuẩn chi khi đưa đoàn khách đi công tác
  - Điều 14: Chi đưa khách đi tham quan
  - Điều 15: Trách nhiệm chi tiếp khách
- **Chương III** (Điều 16-18): CHẾ ĐỘ TIẾP KHÁCH — VIỆT NAM CHI MỘT PHẦN CHI PHÍ
  - Điều 16: Khách tự túc ăn, ở
  - Điều 17: Chế độ tiếp đại sứ, trưởng đại diện tổ chức quốc tế
  - Điều 18: Các đoàn khách nước ngoài vào làm việc
- **Chương IV** (Điều 19-23): HỘI NGHỊ QUỐC TẾ LUÂN PHIÊN — LÃNH ĐẠO ĐẢNG-NHÀ NƯỚC CHỦ TRÌ
  - Điều 19: Quy định chung
  - Điều 20: Hội nghị cấp thượng đỉnh
  - Điều 21: Hội nghị cấp Bộ trưởng
  - Điều 22: Hoạt động bên lề hội nghị cấp thượng đỉnh
  - Điều 23: Hội nghị cấp dưới Bộ trưởng
- **Chương V** (Điều 24-29): HỘI NGHỊ QUỐC TẾ KHÁC + ĐOÀN ĐÀM PHÁN
  - Điều 24: Các khoản chi khác
  - Điều 25: Nội dung và mức chi đặc thù
  - Điều 26: Hội nghị do VN đài
  - Điều 27: Hội nghị VN và nước ngoài cùng đài
  - Điều 28: Hội nghị do nước ngoài đài
  - Điều 29: Chế độ cán bộ VN tham gia
- **Chương VI** (Điều 30-32): TIẾP KHÁCH TRONG NƯỚC
  - Điều 30: Chi giải khát
  - Điều 31: Chi mời cơm
  - Điều 32: Chi phiên dịch tiếng dân tộc
- **Chương VII** (Điều 33-35): TỔ CHỨC THỰC HIỆN
  - Điều 33: Thẩm quyền quy định mức chi
  - Điều 34: Lập, phân bổ dự toán
  - Điều 35: Hiệu lực thi hành (18/05/2026)
- **Phụ lục**: Cấp hạng khách quốc tế (Đặc biệt, Hạng A, Hạng B, Hạng C, Khách mời quốc tế khác)

### Mức chi tiêu biểu đã capture đầy đủ

- Thuê chỗ ở: 6.000.000 - 9.400.000 đ/người/ngày (theo hạng khách)
- Tiền ăn: 1.200.000 - 3.000.000 đ/người/ngày
- Tiếp xã giao: 120.000 - 300.000 đ/người/buổi
- Biên dịch: 300.000/360.000 đ/trang; phiên dịch: 750.000/1.500.000 đ/giờ
- Bồi dưỡng phục vụ hội nghị: 300.000 - 600.000 đ/người/ngày

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 35/2026/TT-BTC | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (35 Điều + 7 Chương + Phụ lục)** (2026-06-14) |

### Ghi chú xử lý

- File path: `van-ban/tai-chinh/thong-tu-35-2026-tt-btc-che-do-tiep-khach-nuoc-ngoai-hoi-nghi-quoc-te-tai-viet-nam.md` (group `tai-chinh` đã có sẵn, đúng lĩnh vực).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Front matter: kết hợp CamelCase + underscore snake_case + có `de_nghi`, `bo`, `hieu_luc`, `nguoi_ky`, `thay_the`, `so_cong_bao`, `docid_luatvietnam`.
- Phiên thực hiện: agent:github-io:subagent:f82fd1f3-9ca1-4d26-ac31-ed4d00b9408d (Đệ #3 Full Content Crawler 35/2026/TT-BTC).
- VĂN BẢN ĐÃ CÓ HIỆU LỰC (18/05/2026) - 27 ngày trước.
- Căn cứ: Luật NSNN 89/2025/QH15; NĐ 29/2025/NĐ-CP (sửa đổi bởi NĐ 166/2025/NĐ-CP); NĐ 134/2025/NĐ-CP; NĐ 18/2022/NĐ-CP; QĐ 06/2020/QĐ-TTg.
- Thay thế: Thông tư 71/2018/TT-BTC ngày 10/8/2018.
- Người ký: KT. Bộ trưởng Bộ Tài chính — Thứ trưởng Nguyễn Thị Bích Ngọc (bổ nhiệm theo QĐ 323/QĐ-TTg ngày 19/02/2025, Ủy viên Trung ương Đảng khóa XIV).
- Lần đầu dùng nguồn storage-vnportal.vnpt.vn (UBND tỉnh Ninh Bình lưu trữ) thay vì datafiles.chinhphu.vn (404) và Công báo CDN (chưa có URL).
- docid dùng trong front matter = `430995` (luatvietnam.vn slug) vì văn bản chưa có trên vanban.chinhphu.vn.
- Cross-check: luatvietnam.vn (slug 430995) + thuvienphapluat.vn (slug 700176, bị Cloudflare chặn nhưng đã có metadata).
- **Đã sửa OCR issues:** "Chương VỊ" → "Chương VI", "⁄2025NĐ" → "/2025/NĐ", "ễn Thị Bích Ngọc" → "Nguyễn Thị Bích Ngọc".
- **Lưu ý đặc biệt:** văn bản này có **7 Chương** thay vì 4 như phỏng đoán ban đầu — cấu trúc phức tạp hơn nhiều.

### Vấn đề gặp phải

- Đệ #3 lần đầu (task `crawler-35-btc-20260614` session `ad6125b4`) fail vì context overflow khi xử lý PDF 11.1MB.
- Đệ #3 retry (task `crawler-35-btc-20260614` session `58fbdd67`) thành công trong 7m21s với nguồn dữ liệu từ luatvietnam.vn (text render trong HTML, marker "Đang theo dõi" là UI tracking chứ không phải placeholder).
- Kinh nghiệm: VĂN BẢN CÓ CHỮ KÝ SỐ LỚN (PDF > 10MB) cần ưu tiên tìm nguồn HTML scrape thay vì OCR toàn văn, vì OCR gây context overflow.

## Cập nhật 2026-06-14 (phiên Đệ #3 Full Content Crawler — lần 11)

### Crawler chi tiết văn bản 46/2026/TT-BGDĐT

Hoàn thiện crawl + Markdown hóa **46/2026/TT-BGDĐT** theo quy trình scrape HTML từ luatvietnam.vn (slug 437124). Văn bản ngắn, 3 Điều thân + Phụ lục Điều lệ trường trung học nghề (6 Chương + 30 Điều).

| Số hiệu | Trạng thái | File | Ghi chú |
|---|---|---|---|
| 46/2026/TT-BGDDT | **Đã có (2026-06-14, scrape HTML 556 dòng, 6 Chương + 3 Điều thân + 30 Điều Phụ lục)** | `van-ban/giao-duc-dao-tao/thong-tu-46-2026-tt-bgddt-dieu-le-truong-trung-hoc-nghe.md` | Nguồn: luatvietnam.vn (slug 437124) + cross-check slug 109523; datafiles.chinhphu.vn/congbao chưa tìm thấy; người ký: KT. Bộ trưởng - Thứ trưởng Lê Quân; ngày ban hành: 10/06/2026; hiệu lực: 10/06/2026 (ĐÃ CÓ HIỆU LỰC 4 ngày); 3 Điều thân (Điều 1: ban hành Điều lệ; Điều 2: hiệu lực; Điều 3: trách nhiệm thi hành) + Phụ lục Điều lệ (6 Chương: I. Quy định chung; II. Tổ chức hoạt động GDNN; III. Tổ chức và quản lý; IV. Quyền và nghĩa vụ; V. Tài chính, tài sản; VI. Quan hệ nhà trường-gia đình-xã hội-DN; 30 Điều phụ lục 1-30); 556 dòng, 50.9KB; OCR issues = 0 |

### Cấu trúc 46/2026/TT-BGDĐT

**Phần thân Thông tư (3 Điều):**
- Điều 1: Ban hành kèm theo Thông tư này Điều lệ trường trung học nghề
- Điều 2: Hiệu lực thi hành từ 10/06/2026
- Điều 3: Trách nhiệm thi hành (VP Bộ, Cục GDNN&GDTX, UBND tỉnh, Sở GD&ĐT, Hiệu trưởng)

**Phụ lục Điều lệ trường trung học nghề (6 Chương + 30 Điều):**
- **Chương I** (Điều 1-3): Quy định chung (phạm vi, đối tượng, giải thích từ ngữ)
- **Chương II** (Điều 4-13): Tổ chức hoạt động giáo dục nghề nghiệp (nhiệm vụ, chương trình, tuyển sinh, đánh giá, cấp văn bằng/chứng chỉ, tổ chức lớp, quy mô, học liệu, thực hành, thực tập)
- **Chương III** (Điều 14-20): Tổ chức và quản lý (cơ cấu tổ chức, hội đồng trường, hiệu trưởng, phó hiệu trưởng, giáo viên, nhân viên, tổ chức Đảng/Đoàn)
- **Chương IV** (Điều 21-25): Quyền và nghĩa vụ của nhà giáo, người học, nhà trường
- **Chương V** (Điều 26-27): Tài chính, tài sản, cơ sở vật chất
- **Chương VI** (Điều 28-30): Quan hệ nhà trường với gia đình, xã hội, doanh nghiệp

### Đối chiếu nhanh với `LEGISLATION_TRACKING.md`

| Số hiệu | Trong tracking? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|
| 46/2026/TT-BGDDT | **CÓ** (Đệ #1 lần 11 ngày 2026-06-13) | Thêm mới — Chưa có | **Đã có (3 Điều thân + Phụ lục 6 Chương + 30 Điều)** (2026-06-14) |

### Ghi chú xử lý

- File path: `van-ban/giao-duc-dao-tao/thong-tu-46-2026-tt-bgddt-dieu-le-truong-trung-hoc-nghe.md` (group `giao-duc-dao-tao` đã có sẵn, đúng lĩnh vực).
- Layout: `vanban` (đúng checklist OCR Quality Gate mục 3).
- Phiên thực hiện: agent:github-io:subagent:3573ad52-5bc6-438f-87d5-d64768534b72 (Đệ #3 Full Content Crawler 46/2026/TT-BGDĐT).
- VĂN BẢN ĐÃ CÓ HIỆU LỰC (10/06/2026) - 4 ngày trước.
- Căn cứ: Luật Giáo dục 43/2019/QH14 (sửa đổi bởi 123/2025/QH15); Luật GDNN 124/2025/QH15; Luật Nhà giáo 73/2025/QH15; NĐ 37/2025/NĐ-CP.
- Người ký: KT. Bộ trưởng - Thứ trưởng Lê Quân.
- Đề nghị: Cục trưởng Cục GDNN&GDTX.
- Lần đầu crawl văn bản GD&ĐT từ luatvietnam.vn với body extraction (không phải readability mà raw HTML `<div class="the-document-body">`).
- docid dùng trong front matter = `437124` (luatvietnam.vn slug) vì văn bản chưa có trên vanban.chinhphu.vn.
- **Duplicate handling thông minh:** 3 Điều thân (1,2,3) + 30 Điều Phụ lục (1-30) → tổng cộng 33 dòng Điều, trong đó [1,2,3] xuất hiện 2 lần (1 lần ở thân, 1 lần ở Phụ lục) → đây là cấu trúc hợp lệ của văn bản, không phải lỗi trùng lặp.
- **Vấn đề phát sinh:** đệ #3 retry tạo file thừa 35/TT-BTC với slug sai ở lần crawl trước - đã xóa file thừa trước khi commit.
- Kinh nghiệm: văn bản ngắn (3 Điều thân + Phụ lục dài) nên dùng raw HTML body extraction (`<div class="the-document-body">`) thay vì readability, sẽ lấy được toàn văn nội dung.

### Vấn đề gặp phải
- Không tìm được URL datafiles.chinhphu.vn/congbao.chinhphu.vn (chưa đăng trên hệ thống chính thức).
- thuvienphapluat.vn không tìm thấy URL cụ thể (chỉ có thông tin tóm tắt trong bài viết khác).
- Lần đầu dùng raw HTML body extraction cho luatvietnam.vn - thành công.

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần) - Đệ #1 lần 2026-06-14

Quét tuần 09–15/06/2026 qua web search Brave + web_fetch (luatvietnam.vn, thuvienphapluat.vn, baophapluat.vn, baomoi.com, vietnamplus.vn). Lọc trừ QĐ-TTg hành chính, Công văn VPCP, tin tổng hợp. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-14 trước phiên): phát hiện **4 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 4 (đã loại các văn bản trùng/trước 09/06):

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 44/2026/TT-BGDĐT | 09/06/2026 | Quy định trình tự, thủ tục xây dựng, thẩm định, ban hành, quản lý, tổ chức thực hiện và đánh giá chương trình khoa học, công nghệ và đổi mới sáng tạo của Bộ GD&ĐT; hiệu lực 25/7/2026 | Giáo dục / Khoa học công nghệ | — | **Chưa có** | Tác động hệ thống quản lý KHCN cấp Bộ; nguồn: thuvienphapluat.vn (2 bài: 273501 + 138094047); người ký: Phạm Ngọc Thưởng (Bộ trưởng); file slug dự kiến: `thong-tu-44-2026-tt-bgddt-trinh-tu-thu-tuc-chuong-trinh-khcn.md` |
| 43/2026/TT-BGDĐT | 09/06/2026 | Quy định tiêu chuẩn người dạy nghề; hiệu lực ngay 09/6/2026 | Giáo dục / GD nghề nghiệp | — | **Chưa có** | Tác động trực tiếp đến hệ thống đào tạo nghề; nguồn: luatvietnam.vn (2 bài: 436987-d1 + 109479-article); hiệu lực ngay ký ban hành; file slug dự kiến: `thong-tu-43-2026-tt-bgddt-tieu-chuan-nguoi-day-nghe.md` |
| 69/2026/TT-BCA | ~09/06/2026 (file mẫu upload 09/6) | Sửa đổi, bổ sung Thông tư 31/2023/TT-BCA về mẫu hộ chiếu, mẫu giấy thông hành và các biểu mẫu liên quan; thay thế 9 mẫu biểu mới (TK01-TK06, VB01); hiệu lực 01/7/2026 | An ninh trật tự / Xuất nhập cảnh | — | **Chưa có** | Tác động toàn bộ công dân làm hộ chiếu; nguồn: luatvietnam.vn (109435-article + 109525-article + 109470-article), thuvienphapluat.vn (138093770), hoatieu.vn, eva.vn, suckhoedoisong.vn; ngày ký chính thức cần xác minh (giả thuyết 9/6/2026 dựa trên timestamp upload file mẫu trên luatvietnam.vn) |
| 16/2026/TT-NHNN | ~09–12/06/2026 (chưa xác minh) | Sửa đổi quy định thu đổi tiền không đủ tiêu chuẩn lưu thông | Ngân hàng / Tài chính | — | **Chưa có** | Tác động hệ thống ngân hàng thương mại và chi nhánh NH nước ngoài; nguồn: thuvienphapluat.vn (102123 - danh sách NĐ 2026 + dòng riêng về 16/TT-NHNN); ngày ký chính thức CHƯA xác minh được (URL trực tiếp thuvienphapluat.vn 404, luatvietnam.vn redirect sang văn bản khác) — đề xuất verify trong heartbeat tiếp theo |

### Văn bản phát hiện thêm (chưa tạo entry — chờ phiên sau)

- **21/2026/NQ-CP** (Y tế / Hành chính) — Chính phủ cắt giảm 298 điều kiện kinh doanh y tế, phân cấp 64 thủ tục hành chính, đơn giản hóa 71 TTHC; **ĐÃ LOẠI** vì văn bản gốc ký ngày **29/4/2026** (theo baophapluat.vn: "Nghị quyết số 21/2026/NQ-CP ngày 29/4/2026") — NGOÀI khoảng 09–15/06/2026; bài báo 10/6/2026 chỉ là phân tích chuyên sâu sau khi văn bản ban hành.
- **125/NQ-CP** (Lập pháp) — điều chỉnh Chương trình lập pháp 2026, bổ sung Luật Định danh và xác thực điện tử; nguồn: vietnamplus.vn (post1116058); **CHƯA xác minh** ngày ký chính thức (vietnamplus.vn 3 days ago + sggp.org.vn 3 days ago = ~11/6/2026) — đề xuất verify.
- **50/2026/TT-BQP** (Quốc phòng / Lao động) — hướng dẫn NĐ 363/2025/NĐ-CP thu hút, trọng dụng nhân tài; **ĐÃ LOẠI** vì ngày 25/5/2026 (NGOÀI 09–15/06/2026).
- **200/2026/NĐ-CP** (Tài chính) — trái phiếu doanh nghiệp riêng lẻ; **ĐÃ LOẠI** vì ngày 05/6/2026 (NGOÀI 09–15/06/2026).
- **202/2026/NĐ-CP** (Tài chính) — lệ phí trước bạ ô tô điện 0% đến 2030; **ĐÃ LOẠI** vì ngày 08/6/2026 (NGOÀI 09–15/06/2026).
- **197/2026/NĐ-CP** (Tư pháp) — Cơ sở dữ liệu quốc gia về tiếp công dân, khiếu nại, tố cáo; **ĐÃ LOẠI** vì ngày 03/6/2026 (NGOÀI 09–15/06/2026).
- **18/2026/TT-BYT** (Y tế) — thuốc kiểm soát đặc biệt; **ĐÃ CÓ** trong tracking (line 818-819 + 989).
- **06/2026/TT-BYT** (Y tế) — mã hóa bệnh tật ICD-10; **ĐÃ CÓ** trong tracking (line 818-819).
- **28/2026/NQ-CP** (Năng lượng) — cơ chế khai thác than vượt công suất; **ĐÃ CÓ** trong tracking (line 133 + 143 + 151 + 159-160).
- **31/2026/TT-BCT** (Công Thương) — truy xuất nguồn gốc sản phẩm; **ĐÃ CÓ** trong tracking (line 179 + 207 + 214 + 222).
- **45/2026/TT-BGDĐT** (Giáo dục) — sửa đổi TT 15/2025 chức năng Sở GD&ĐT; **ĐÃ CÓ** trong tracking (line 89 + 99 + 107 + 117).
- **46/2026/TT-BGDĐT** (Giáo dục) — Điều lệ trường TH nghề; **ĐÃ CÓ** trong tracking (line 175 + 222 + file `van-ban/giao-duc-dao-tao/thong-tu-46-2026-tt-bgddt-dieu-le-truong-trung-hoc-nghe.md` đã được crawl bởi Đệ #3 lúc 2026-06-14).
- **14/2026/TT-BNV** (Nội vụ) — điều chỉnh lương hưu 8% từ 01/7/2026; **ĐÃ CÓ** trong tracking (line 455).
- **30/2026/TT-BCT** (Công Thương) — giá điện BOT; **ĐÃ CÓ** trong tracking (line 135 + 145 + 152 + 160 + file `van-ban/nang-luong-tai-nguyen/thong-tu-30-2026-tt-bct-gia-dich-vu-phat-dien-nha-may-bot.md` đã crawl).

### Đối chiếu nhanh với `van-ban/` và LEGISLATION_TRACKING.md (đến 2026-06-14 trước phiên)

| Số hiệu | Trong tracking? | File van-ban/? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|:---:|
| 44/2026/TT-BGDĐT | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 43/2026/TT-BGDĐT | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 69/2026/TT-BCA | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 16/2026/TT-NHNN | **KHÔNG** | Không | — | Thêm mới — Chưa có |

### Ghi chú xử lý

- **Subagent session:** agent:github-io:subagent:7ba0123b-268b-497d-89bc-c75203e9d86a (Đệ #1 Discovery & Tracking - lần 2026-06-14).
- **Văn bản MỚI thực sự:** 4 (44, 43, 69, 16) — đủ 4/5, thiếu 1 do date verification chưa hoàn tất (16/2026/TT-NHNN + 125/NQ-CP).
- **Văn bản bị loại do ngoài khoảng ngày 09–15/06/2026:** 50/2026/TT-BQP (25/5), 06/2026/TT-BYT (02/04), 18/2026/TT-BYT (01/06), 200/2026/NĐ-CP (05/6), 202/2026/NĐ-CP (08/6), 197/2026/NĐ-CP (03/6), 21/2026/NQ-CP (29/4/2026).
- **Văn bản đã có trong tracking:** 28/2026/NQ-CP, 31/2026/TT-BCT, 45/2026/TT-BGDĐT, 46/2026/TT-BGDĐT, 14/2026/TT-BNV, 30/2026/TT-BCT — tổng cộng 6 văn bản đã có, không thêm trùng.
- **Khuyến nghị ưu tiên:** 4 văn bản mới đều thuộc lĩnh vực KHCN (44/TT-BGDĐT), GD nghề (43/TT-BGDĐT), hộ chiếu (69/TT-BCA), ngân hàng (16/TT-NHNN) — phù hợp nhóm ưu tiên Thuế/Chứng khoán/Đất đai/KHCN/Lâm nghiệp/GD/Y tế/XD/GTVT.
- **Cần verify trong heartbeat tiếp theo:** ngày ký chính thức của 16/2026/TT-NHNN và 125/NQ-CP; docid vanban.chinhphu.vn cho 4 văn bản mới.
- **Giới hạn task:** đệ #1 chỉ phát hiện + cập nhật tracking, KHÔNG crawl nội dung — đề xuất Đệ #3 Full Content Crawler xử lý 4 văn bản này trong phiên tiếp theo.

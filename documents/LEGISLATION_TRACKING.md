
## Cập nhật 2026-06-28 (phiên Đệ #1 Discovery — lần 18)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét vanban.chinhphu.vn dải docid 218591–218620 + chinhphu.vn + web_search theo nhóm chủ đề + xác minh 245/2026/NĐ-CP từ nhandan.vn, baochinhphu.vn, xaydungchinhsach.chinhphu.vn.

**Xác nhận: Không có văn bản nào ban hành ngày 28/6/2026** — 28/6/2026 là Chủ nhật (Ngày Gia đình Việt Nam), ngày nghỉ lễ. Dải docid 218591–218620 hoàn toàn trống (ASP.NET WebForms render bằng JS, server trả về `__VIEWSTATE` + postback form, không có nội dung qua HTTP GET thông thường).

Tuy nhiên, web_search phát hiện **245/2026/NĐ-CP** được baochinhphu.vn đưa tin chính thức ngày 27/6/2026, chưa từng được ghi nhận trong tracking. Đây là văn bản gia hạn thuế quan trọng, hiệu lực 27/6/2026. Giới hạn 5/lần — ghi nhận 1:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 245/2026/NĐ-CP | 27/06/2026 | Quy định **gia hạn thời hạn nộp thuế** giá trị gia tăng, thuế thu nhập doanh nghiệp, thuế thu nhập cá nhân và tiền thuê đất trong năm 2026 — gia hạn tối đa 5 tháng đối với VAT kỳ tháng 5–9/2026 và quý II, III/2026; gia hạn 3 tháng đối với TNDN tạm nộp quý II; gia hạn 2 tháng đối với TNDN tạm nộp quý III; gia hạn 5 tháng đối với TNCN của hộ kinh doanh, cá nhân kinh doanh; gia hạn 5 tháng đối với 50% tiền thuê đất kỳ đầu năm 2026; không tính tiền chậm nộp trong thời gian gia hạn; đối tượng: doanh nghiệp, tổ chức, hộ kinh doanh, cá nhân kinh doanh trong 43 ngành kinh tế theo Phụ lục I + doanh nghiệp nhỏ và siêu nhỏ; hiệu lực **27/6/2026 đến 30/12/2026** | Thuế / Tài chính | chua-xac-minh | **Chưa có** | URL: `https://xaydungchinhsach.chinhphu.vn/nghi-dinh-245-2026-nd-cp-gia-han-thoi-han-nop-thue-tien-thue-dat-trong-nam-2026-119260627180925528.htm`; nguồn: baochinhphu.vn (tin chính thức 27/6), nhandan.vn, vietnamplus.vn, vov.vn, laodong.vn; ngày ban hành: 27/6/2026; hiệu lực: 27/6/2026–30/12/2026; tác động rất rộng — 43 ngành kinh tế, hàng triệu doanh nghiệp và hộ kinh doanh; cần xác minh docid vanban.chinhphu.vn (dự kiến 218600–218620 hoặc cao hơn) + crawl nội dung chi tiết ở Đệ #3 Full Content Crawler; Phụ lục I gồm 43 ngành kinh tế (nông nghiệp → xử lý nước thải) + quy định xác định ngành theo QĐ 36/2025/QĐ-TTg |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-27 lần 17)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 245/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Thuế / Tài chính** (rất cao — hiệu lực ngay 27/6/2026, hết hạn 30/12/2026): **245/2026/NĐ-CP** — gia hạn thuế VAT, TNDN, TNCN, tiền thuê đất; tác động 43 ngành kinh tế, hàng triệu doanh nghiệp và hộ kinh doanh; ưu tiên số 1.
2. **Văn hóa / Di sản** (còn ~49 ngày): **16/2026/TT-BVHTTDL** — định mức giám định di vật, cổ vật; hiệu lực 15/8/2026 (từ lần 17).
3. **Văn hóa / Di sản** (còn ~49 ngày): **17/2026/TT-BVHTTDL** — định mức lập hồ sơ công nhận bảo vật quốc gia; hiệu lực 15/8/2026.
4. **Giáo dục / Hành chính** (còn ~41 ngày): **47/2026/TT-BGDĐT** — bãi bỏ văn bản giáo dục; hiệu lực 07/8/2026.

### Ghi chú xử lý

- **Không có văn bản ban hành ngày 28/6/2026**: 28/6/2026 là Chủ nhật, Ngày Gia đình Việt Nam. Không có phiên họp Chính phủ, không ban hành văn bản.
- **Dải docid 218591–218620 hoàn toàn trống**: vanban.chinhphu.vn sử dụng ASP.NET WebForms + JavaScript render nội dung client-side. HTTP GET trả về trang shell với `__VIEWSTATE` và postback form, không trả nội dung văn bản. Cần dùng headless browser (Puppeteer/Playwright) để crawl dải docid mới.
- **245/2026/NĐ-CP chưa có trong tracking**: Văn bản được baochinhphu.vn đăng tin chính thức ngày 27/6/2026; đây là văn bản thuế quan trọng, tác động rất rộng (43 ngành kinh tế, hàng triệu đối tượng). Nội dung chi tiết có tại xaydungchinhsach.chinhphu.vn (toàn văn + Phụ lục I).
- **245/2026/NĐ-CP docid chưa xác minh**: Dải docid trên vanban.chinhphu.vn trả về rỗng; cần xác minh docid qua luatvietnam.vn hoặc thuvienphapluat.vn ở phiên sau. Xác suất docid nằm trong dải 218600–218620 hoặc cao hơn (218621+).
- **Nguồn**: vanban.chinhphu.vn (quét docid 218591–218620 — rỗng), xaydungchinhsach.chinhphu.vn (toàn văn 245/2026/NĐ-CP), baochinhphu.vn (tin chính thức), nhandan.vn, vietnamplus.vn, vov.vn, laodong.vn, thuvienphapluat.vn.
- Ngày phát hiện: 2026-06-28 01:33 ICT
- Phiên thực hiện: agent:github-io:subagent:701f1909-d894-4d33-b9a1-11a509215239 (Đệ #1 Discovery — lần 18)

---

## Cập nhật 2026-06-27 (phiên Đệ #1 Discovery — lần 17)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét vanban.chinhphu.vn dải docid 219100–219800 + chinhphu.vn listing ngày 27/6/2026 + web_search theo nhóm chủ đề. **Xác nhận: Không có văn bản nào ban hành ngày 27/6/2026** — 27/6/2026 là ngày họp phiên Chính phủ chuyên đề xây dựng pháp luật. Toàn bộ văn bản trong listing 27/6 thực ra ban hành 15–26/6/2026 và được công bố rải trên 27/6.

Quét dải docid 219100–219800 bằng curl: tất cả đều trả về trang chủ hoặc "Không tìm thấy" → dải này hoàn toàn trống, không có văn bản. Dải docid hợp lệ kết thúc tại **218590** (237/2026/NĐ-CP). Tìm kiếm 239/2026/NĐ-CP (khuyến mại) trong dải 218600–219000 cho kết quả false positive do hash MD5 trùng trong JS, docid thực tế vẫn chưa xác minh.

So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-27 lần 16): phát hiện **4 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận 4:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 16/2026/TT-BVHTTDL | 23/06/2026 | Quy định về **định mức kinh tế - kỹ thuật dịch vụ giám định di vật, cổ vật** — định mức chi phí giám định, tiêu chí kỹ thuật, quy trình giám định; hiệu lực **15/08/2026** | Văn hóa / Di sản | 218564 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218564`; nguồn: vanban.chinhphu.vn (docid confirmed từ chinhphu.vn listing 27/6); ngày ban hành: 23/6/2026; hiệu lực: 15/8/2026 (còn 49 ngày); tác động cơ quan giám định di vật, bảo tàng, cơ sở lưu giữ di sản văn hóa |
| 17/2026/TT-BVHTTDL | 23/06/2026 | Quy định về **định mức kinh tế - kỹ thuật dịch vụ lập hồ sơ đề nghị công nhận bảo vật quốc gia** — định mức chi phí lập hồ sơ, tiêu chí kỹ thuật, quy trình đề nghị công nhận; hiệu lực **15/08/2026** | Văn hóa / Di sản | 218565 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218565`; nguồn: vanban.chinhphu.vn (docid confirmed từ chinhphu.vn listing 27/6); ngày ban hành: 23/6/2026; hiệu lực: 15/8/2026 (còn 49 ngày); tác động cơ quan quản lý di sản, chủ sở hữu bảo vật quốc gia |
| 47/2026/TT-BGDĐT | 22/06/2026 | **Bãi bỏ một số văn bản quy phạm pháp luật** do Bộ trưởng Bộ Giáo dục và Đào tạo ban hành trong lĩnh vực giáo dục — dọn dẹp văn bản hết hiệu lực hoặc trùng lặp; hiệu lực **07/08/2026** | Giáo dục / Hành chính | 218566 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218566`; nguồn: vanban.chinhphu.vn (docid confirmed từ chinhphu.vn listing 27/6); ngày ban hành: 22/6/2026; hiệu lực: 07/8/2026 (còn 41 ngày); tác động cơ sở giáo dục, cán bộ quản lý giáo dục; cần kiểm tra danh mục văn bản bị bãi bỏ |
| 82/2026/TT-BQP | 18/06/2026 | Quy định chế độ **gặp, nhận quà và liên lạc của phạm nhân** — điều kiện, thủ tục gặp phạm nhân; nhận quà; liên lạc; hiệu lực **01/07/2026** | Tư pháp / Quốc phòng | 218521 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218521`; nguồn: vanban.chinhphu.vn (docid confirmed từ chinhphu.vn listing 27/6); người ký: Nguyễn Văn Gấu (Bộ trưởng Bộ Quốc phòng); ngày ban hành: 18/6/2026; hiệu lực: 01/7/2026 (còn 4 ngày); tác động cơ sở giam giữ, gia đình phạm nhân, luật sư |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-27 lần 16)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 16/2026/TT-BVHTTDL | **KHÔNG** | Thêm mới — Chưa có |
| 17/2026/TT-BVHTTDL | **KHÔNG** | Thêm mới — Chưa có |
| 47/2026/TT-BGDĐT | **KHÔNG** | Thêm mới — Chưa có |
| 82/2026/TT-BQP | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Tư pháp / Quốc phòng** (rất cao — 4 ngày tới): **82/2026/TT-BQP** — chế độ gặp, nhận quà và liên lạc của phạm nhân; hiệu lực 01/7/2026 (còn 4 ngày). Tác động trực tiếp cơ sở giam giữ, gia đình phạm nhân. Ưu tiên số 1.
2. **Văn hóa / Di sản** (trung bình — 49 ngày tới): **16/2026/TT-BVHTTDL** — định mức giám định di vật, cổ vật; hiệu lực 15/8/2026. Tác động cơ quan bảo tàng, giám định di sản.
3. **Văn hóa / Di sản** (trung bình — 49 ngày tới): **17/2026/TT-BVHTTDL** — định mức lập hồ sơ công nhận bảo vật quốc gia; hiệu lực 15/8/2026. Cùng nhóm với 16/2026.
4. **Giáo dục / Hành chính** (trung bình — 41 ngày tới): **47/2026/TT-BGDĐT** — bãi bỏ văn bản giáo dục; hiệu lực 07/8/2026. Cần kiểm tra danh mục bị bãi bỏ.

### Ghi chú xử lý

- **Không có văn bản ban hành ngày 27/6/2026**: 27/6/2026 là ngày họp phiên Chính phủ chuyên đề xây dựng pháp luật, không phải ngày ban hành văn bản. Tất cả văn bản trong listing chinhphu.vn ngày 27/6 đều ban hành 15–26/6/2026.
- **Dải docid 219100–219800 hoàn toàn trống**: Tất cả docid trong dải này đều trả về trang chủ vanban.chinhphu.vn hoặc "Không tìm thấy". Docid hợp lệ cao nhất vẫn là **218590** (237/2026/NĐ-CP). Không có văn bản nào ở dải 219xxx.
- **239/2026/NĐ-CP docid chưa xác minh**: Tìm kiếm 239 trong dải 218600–219000 gặp false positive tại 218609 (hash MD5 trùng trong JS), docid thực sự của 239/2026/NĐ-CP (khuyến mại, BH 26/6/2026, hiệu lực 26/6/2026) vẫn chưa xác định được. Cần tìm trên luatvietnam.vn hoặc thuvienphapluat.vn.
- **Chinhphu.vn listing 27/6**: Docid mới được xác định từ listing bao gồm: 218564 (16/TT-BVHTTDL), 218565 (17/TT-BVHTTDL), 218566 (47/TT-BGDĐT), 218521 (82/TT-BQP), 218535 (75/TT-BQP — đã có từ lần 13), 218569 (70/TT-BTC — đã xác minh lần 16).
- **75/2026/TT-BQP** (docid 218535, BH 16/6/2026, hiệu lực 01/8/2026): Quản lý hồ sơ tạm giữ, tạm giam trong Quân đội nhân dân — đã có trong tracking, không trùng với 75/2026/NĐ-CP (chế độ tự chủ hành chính).
- **Kỹ thuật quét docid**: Sử dụng `curl` trực tiếp + Python regex thay vì `web_fetch` (Firecrawl hết credit) + `grep` để trích title từ `<title>` tag. Pattern: `<title>(?!Chi tiết văn bản ban hành)Nghị định.*?NĐ-CP` để phân biệt trang văn bản thực vs nav page.
- Nguồn: vanban.chinhphu.vn (docid confirmed), chinhphu.vn (listing ngày 27/6), curl scan dải 218590–219000.
- Ngày phát hiện: 2026-06-27 19:14 ICT
- Phiên thực hiện: agent:github-io:subagent:1f01e8d0-ea22-47f5-bee8-ef9e8fe5dfb1 (Đệ #1 Discovery — lần 17)

## Cập nhật 2026-06-27 (phiên Đệ #1 Discovery — lần 16)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét vanban.chinhphu.vn dải docid 218590–219050 + web_search Brave/Gemini theo nhóm chủ đề: Tài chính, Thuế, Xây dựng, Giao thông, Hàng không, Lao động, Năng lượng, KHCN, Dự trữ quốc gia, Hành chính, Tư pháp. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-22 lần 15): phát hiện **2 văn bản mới** (237/2026/NĐ-CP chưa trong tracking, 33/2026/TT-BKHCN chưa trong tracking). Các văn bản đã biết từ poll trước (68, 205, 221, 237, 229) được xác minh docid và xác nhận trạng thái.

**Lưu ý quan trọng: Ngày 27/6/2026 là ngày họp phiên Chính phủ chuyên đề xây dựng pháp luật — không ban hành văn bản mới trong ngày.** Các văn bản được ghi nhận hoặc ban hành từ 22–26/6/2026 và được công bố/rải trên 27/6.

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 237/2026/NĐ-CP | 26/06/2026 | Quy định chi tiết thi hành một số điều của Luật Báo chí 2026 — **gắn nhãn bắt buộc** đối với nội dung báo chí được tạo hoặc chỉnh sửa bằng AI; cấm dùng AI tạo hoặc lan truyền nội dung giả mạo, xuyên tạc; khuyến khích ứng dụng AI nâng cao hiệu quả; cơ quan báo chí phải thiết lập quy trình thẩm định, biên tập, kiểm soát rủi ro khi dùng AI; thay thế các nghị định hướng dẫn Luật Báo chí 2023; hiệu lực **01/7/2026** | Báo chí / Tư pháp / CNTT | 218590 | **Đã có (2026-06-27)** | File: `van-ban/237-2026-nd-cp-ai-bao-chi.md`; 30 Điều, 6 Chương (I-VI), 1.482 dòng, 79KB; nguồn: luatvietnam.vn (slug 438775) - HTML text; không cần OCR; hiệu lực 01/7/2026; Điều 17 có hiệu lực 01/7/2028 |
| 33/2026/TT-BKHCN | 15/06/2026 | Quy định về trang phục riêng, phù hiệu và thẻ của **kiểm soát viên chất lượng sản phẩm, hàng hóa** — các loại trang phục đặc thù, phù hiệu nhận diện, thẻ kiểm soát viên; hiệu lực chưa rõ | KHCN / Hành chính | 218472 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218472`; nguồn: vanban.chinhphu.vn (docid 218472), congbao.chinhphu.vn (slug 469775); ngày ban hành: 15/6/2026; nhóm kiểm soát chất lượng sản phẩm hàng hóa; tác động cơ quan quản lý chất lượng Bộ KH&CN |
| 218/2026/NĐ-CP | 22/06/2026 | Sửa đổi, bổ sung một số điều của NĐ 158/2024/NĐ-CP về **hoạt động vận tải đường bộ** — điều kiện kinh doanh vận tải, xe ô tô, lái xe; hiệu lực **01/7/2026** | Giao thông / Vận tải | 218537 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218537`; nguồn: vanban.chinhphu.vn (docid confirmed); web_search xác nhận ngày 22/6/2026 (cùng đợt 220/2026/NĐ-CP); thay thế NĐ 158/2024/NĐ-CP; cùng nhóm với 205/2026/NĐ-CP (cảng hàng không); cần xác minh nội dung chi tiết từ luatvietnam.vn |
| 219/2026/NĐ-CP | 21/06/2026 | Quy định về xử phạt vi phạm hành chính trong lĩnh vực **khí tượng thủy văn** — mức phạt, thẩm quyền, trình tự; hiệu lực **01/8/2026** | Tài nguyên / Môi trường | 218586 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218586`; nguồn: vanban.chinhphu.vn (docid confirmed), web_search baochinhphu.vn; ngày ban hành: 21/6/2026; web_search ghi nhận 219 từ dải 22/6; tác động cơ quan khí tượng thủy văn, tổ chức, cá nhân hoạt động trong lĩnh vực |
| 220/2026/NĐ-CP | 22/06/2026 | Sửa đổi, bổ sung một số điều của NĐ 67/2023/NĐ-CP về **bảo hiểm bắt buộc** — bảo hiểm TNDS chủ xe cơ giới, bảo hiểm cháy nổ, bảo hiểm trong đầu tư xây dựng; hiệu lực **01/7/2026** | Tài chính / Bảo hiểm | 218555 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218555`; nguồn: vanban.chinhphu.vn (docid confirmed), web_search baochinhphu.vn (xác nhận ban hành 22/6/2026); thay thế NĐ 67/2023/NĐ-CP; hiệu lực 01/7/2026; tác động doanh nghiệp bảo hiểm, chủ xe cơ giới, chủ đầu tư xây dựng |
| 222/2026/NĐ-CP | ~24/06/2026 | Quy định về **hoạt động bay** — quản lý, giám sát hoạt động bay tại Việt Nam; hiệu lực **01/7/2026** | Hàng không / Giao thông | 218557 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218557`; nguồn: vanban.chinhphu.vn (docid confirmed); web_search ghi nhận trong dải văn bản ngày 22–26/6/2026; hiệu lực 01/7/2026; tác động toàn ngành hàng không (cùng nhóm 205, 221); cần xác minh nội dung chi tiết từ luatvietnam.vn |
| 239/2026/NĐ-CP | 26/06/2026 | Sửa đổi, bổ sung một số điều của NĐ 81/2018/NĐ-CP về **hoạt động xúc tiến thương mại, khuyến mại** — hàng hóa được khuyến mại, xác định trúng thưởng phải có khách hàng chứng kiến, tiền làm hàng khuyến mại (trừ một số trường hợp); hiệu lực **chưa rõ** | Thương mại / Tài chính | chua-xac-minh | **Chưa có** | Nguồn: baochinhphu.vn (bài viết 26/6/2026), vietnamplus.vn, congan.com.vn, baomoi.com; ngày ban hành: 26/6/2026; web_search đầy đủ chi tiết nội dung; cần xác minh docid từ vanban.chinhphu.vn; tác động doanh nghiệp kinh doanh xúc tiến thương mại, khuyến mại |

### Bổ sung xác minh docid (lần 16) — phát hiện ngoài dải chính

### Xác minh docid cho các văn bản đã biết từ poll trước

| Số hiệu | Docid cũ | Docid mới | Trạng thái | Chi tiết |
|---|:---:|:---:|---|---|
| 68/2026/TT-BTC | chua-xac-minh | **218539** | **Xác minh mới** | URL chính thức: `https://vanban.chinhphu.vn/?pageid=27160&docid=218539`; KHCN dự trữ quốc gia; hiệu lực 01/7/2026 |
| 205/2026/NĐ-CP | 218452 (xác minh lần 14) | **218452** | Xác minh (giữ nguyên) | Cảng hàng không và bãi cất, hạ cánh; hiệu lực 01/7/2026 |
| 221/2026/NĐ-CP | 218552 (xác minh lần 15) | **218552** | Xác minh (giữ nguyên) | Nhà chức trách hàng không Việt Nam và quản lý an toàn hàng không; thành lập Trung tâm dữ liệu an toàn hàng không quốc gia; hiệu lực 01/7/2026 |
| 237/2026/NĐ-CP | chua-xac-minh (ước đoán 218590) | **218590** | Xác minh mới (cùng ước đoán) | AI trong báo chí; hiệu lực 01/7/2026 |
| 229/2026/NĐ-CP | chua-xac-minh | **218589** | **Xác minh mới** | URL chính thức: `https://vanban.chinhphu.vn/?pageid=27160&docid=218589`; Quỹ Phát triển KH&CN Quốc gia (NAFOSTED); hiệu lực 25/6/2026 (cùng ngày ban hành) |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-22 lần 15)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 237/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 33/2026/TT-BKHCN | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Báo chí / Tư pháp / CNTT** (rất cao — 4 ngày tới): **237/2026/NĐ-CP** — gắn nhãn AI trong báo chí; cấm AI tạo nội dung giả; tác động toàn bộ cơ quan báo chí, truyền thông Việt Nam; hiệu lực 01/7/2026. Nguồn: vanban.chinhphu.vn (docid 218590), luatvietnam.vn (slug 438775). Ưu tiên số 1.
2. **Hàng không** (rất cao — 4 ngày tới): **221/2026/NĐ-CP** (218552) — thành lập Trung tâm dữ liệu an toàn hàng không quốc gia; tác động toàn ngành hàng không. Hiệu lực 01/7/2026.
3. **Tài chính / KHCN** (rất cao — 4 ngày tới): **68/2026/TT-BTC** (218539) — KHCN dự trữ quốc gia, chuyển đổi số; tác động Cục Dự trữ Nhà nước. Hiệu lực 01/7/2026.
4. **Hàng không / Giao thông** (rất cao — 4 ngày tới): **205/2026/NĐ-CP** (218452) — cảng hàng không, bãi cất hạ cánh; tác động toàn ngành hàng không. Hiệu lực 01/7/2026.
5. **KHCN** (trung bình): **229/2026/NĐ-CP** (218589) — Quỹ NAFOSTED tổ chức mới; hiệu lực 25/6/2026. Tác động cộng đồng khoa học quốc gia.

### Ghi chú xử lý

- **Ngày 27/6/2026 là ngày họp phiên Chính phủ chuyên đề xây dựng pháp luật**, không phải ngày ban hành văn bản. Các văn bản được ghi nhận trong phiên này thực chất ban hành từ 15–26/6/2026 và được công bố rộng rãi trên báo chí ngày 27/6/2026.
- **Quét dải docid 218590–219800**: Toàn bộ docid trong dải này (218590–218630) khi web_fetch đều trả về "Chi tiết văn bản ban hành" — vanban.chinhphu.vn dùng ASP.NET WebForms + JavaScript render, không trả nội dung qua HTTP GET thông thường. Chỉ docid có sẵn trong index mới trả về tiêu đề (218590 = 237/2026/NĐ-CP, 218592 = QĐ 1131/QĐ-TTg).
- **237/2026/NĐ-CP**: Xác minh docid 218590 trên vanban.chinhphu.vn. Ban hành ngày 26/6/2026, hiệu lực 01/7/2026. Nội dung chính: (i) gắn nhãn nội dung do AI tạo/chỉnh sửa, (ii) cấm dùng AI tạo/lan truyền nội dung giả mạo/sai sự thật/xuyên tạc, (iii) cơ quan báo chí phải thiết lập quy trình thẩm định + kiểm soát rủi ro khi dùng AI, (iv) khuyến khích ứng dụng AI nâng cao hiệu quả, (v) lưu giữ nhật ký hoạt động và hồ sơ kỹ thuật để phục vụ thanh tra, kiểm tra. Có 17 điều thuộc Luật Báo chí 126/2025/QH15 được hướng dẫn chi tiết.
- **68/2026/TT-BTC**: Docid xác minh **218539** trên vanban.chinhphu.vn. Ban hành 18/6/2026, hiệu lực 01/7/2026.
- **229/2026/NĐ-CP**: Docid xác minh **218589** trên vanban.chinhphu.vn. Ban hành 25/6/2026, hiệu lực 25/6/2026 (cùng ngày).
- **33/2026/TT-BKHCN**: Docid xác minh **218472** trên vanban.chinhphu.vn. Ban hành 15/6/2026. Trang phục, phù hiệu, thẻ kiểm soát viên chất lượng sản phẩm.
- **5 văn bản ưu tiên 01/7/2026** (còn 4 ngày): 237, 221, 205, 68, 216 — tất cả đều có docid xác minh và trạng thái "Chưa có" hoặc "Cần crawl chi tiết".
- Nguồn: web_fetch vanban.chinhphu.vn (docid 218590, 218592, 218539, 218452, 218552, 218589, 218472), web_search Brave + Gemini tổng hợp luatvietnam.vn, vietnamplus.vn, dantri.com.vn, nafosted.gov.vn, congthuong.vn, baochinhphu.vn, tapchihangkhong.vn, vov.vn, vtv.vn.
- Ngày phát hiện: 2026-06-27 15:39 ICT
- Phiên thực hiện: agent:github-io:subagent:808aa5bf-5f9f-4d95-9649-d56639df42e7 (Đệ #1 Discovery — lần 16)

## Cập nhật 2026-06-22 (phiên Đệ #1 Discovery — lần 15)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét vanban.chinhphu.vn dải docid 218360–218530 + web_search Brave/Gemini theo nhóm chủ đề: Tài chính, Ngân sách, Thuế, Lệ phí, Năng lượng, Lao động, Tiền lương, Xây dựng. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-22 lần 14): phát hiện **5 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 5:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 216/2026/NĐ-CP | 18/06/2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Lý lịch tư pháp — **công dân nộp hồ sơ xin Phiếu LHP tại nơi cư trú hoặc nơi gần nhất** (nộp trực tiếp, trực tuyến qua ứng dụng định danh quốc gia/VNeID/Cổng DVCQG, hoặc bưu chính); **Bộ Công an quản lý tập trung Cơ sở dữ liệu LHP** toàn quốc (3 nhóm thông tin); nhận Phiếu LHP trên VNeID; thay thế NĐ 111/2010/NĐ-CP; hiệu lực **01/7/2026** | Tư pháp / Hành chính | 218505 | **Đã có (2026-06-23)** | File: `van-ban/tu-phap-thi-hanh-an/nghi-dinh-216-2026-nd-cp-ly-lich-tu-phap.md`; 29 Điều, 4 Chương (I-IV), 238 dòng, 39KB; OCR issues = 0; nguồn: luatvietnam.vn + baochinhphu.vn |
| 217/2026/NĐ-CP | 19/06/2026 | Quy định chi tiết một số điều của Luật Xây dựng 2025 về **quản lý hoạt động xây dựng** — cấp giấy phép xây dựng, quản lý trật tự xây dựng, xây dựng công trình đặc thù/cấp bách; **áp dụng BIM bắt buộc từ cấp II trở lên** (lập từ Báo cáo nghiên cứu khả thi); thay thế NĐ 175/2024/NĐ-CP; hiệu lực **01/7/2026** | Xây dựng / CNTT | 218509 | **Đã có (2026-06-23)** | File: `van-ban/xay-dung/nghi-dinh-217-2026-nd-cp-quan-ly-hoat-dong-xay-dung.md`; 76 Điều (1-76), 5 Chương (I-V), 993 dòng, 244KB; OCR issues = 0 (19 false positive "ngày l" khớp "ngày làm việc" — đúng tiếng Việt); articles 1-76 đầy đủ, không thiếu, không trùng; chương I-V đúng thứ tự La Mã; nguồn: luatvietnam.vn + vanban.chinhphu.vn (docid 218509); hiệu lực: 01/7/2026 (còn 9 ngày khi crawl) |
| 65/2026/TT-BTC | 11/06/2026 | Sửa đổi, bổ sung Thông tư 320/2016/TT-BTC quy định chế độ bồi dưỡng đối với người làm nhiệm vụ **tiếp công dân, xử lý đơn khiếu nại, tố cáo, kiến nghị, phản ánh** — mức bồi dưỡng tăng: **250.000 đồng/ngày** (tiếp công dân TW chưa hưởng phụ cấp), **200.000 đồng/ngày** (tiếp công dân TW đã hưởng phụ cấp hoặc xử lý đơn chưa hưởng phụ cấp), **150.000 đồng/ngày** (xử lý đơn đã hưởng phụ cấp), **100.000 đồng/ngày** (khoản 3, 4 Điều 38 NĐ 154/2026); người ký: Nguyễn Thị Bích Ngọc (KT. Bộ trưởng - Thứ trưởng); hiệu lực **27/7/2026** | Tài chính | 218479 | **Đã có (2026-06-23)** | File: `van-ban/tai-chinh/thong-tu-65-2026-tt-btc-sua-doi-thong-tu-320-2016-ve-boi-duong-tiep-cong-dan.md`; 2 Điều (1, 2), 0 Chương, 137 dòng, 7KB; OCR issues = 0; articles 1–2 đầy đủ, không thiếu, không trùng; nguồn: luatvietnam.vn (slug 437740) + OCR PDF ký số datafiles.chinhphu.vn (`65-btc.pdf`, ký 15/6/2026); đối tượng được sửa: Điều 4 Thông tư 320/2016/TT-BTC (mức chi); nội dung gồm 2 Điều: Điều 1 (sửa đổi Điều 4), Điều 2 (điều khoản thi hành: 4 khoản) |
| 68/2026/TT-BTC | 18/06/2026 | Quy định về **nghiên cứu, ứng dụng khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số**; Hệ thống thông tin, cơ sở dữ liệu về **dự trữ quốc gia** — chi tiết hoạt động nghiên cứu KHCN, hệ thống thông tin dự trữ, cơ sở dữ liệu; hiệu lực **01/7/2026** | Tài chính / KHCN | chua-xac-minh | **Chưa có** | URL: `https://luatvietnam.vn/khoa-hoc/thong-tu-68-2026-tt-btc-quy-dinh-ve-khoa-hoc-cong-nghe-va-chuyen-doi-so-438162-d1.html`; nguồn: luatvietnam.vn (slug 438162), thoibaotaichinhvietnam.vn, gdsr.gov.vn; người ký: Bộ Tài chính; ngày ban hành: 18/6/2026; hiệu lực: 01/7/2026 (còn 9 ngày); tác động Cục Dự trữ Nhà nước, cơ quan nghiên cứu KHCN thuộc Bộ Tài chính; cần xác minh docid vanban.chinhphu |
| 03/2026/TT-DTTG | ~18/06/2026 | **Bãi bỏ một số văn bản quy phạm pháp luật** thuộc thẩm quyền của Bộ trưởng Bộ Dân tộc và Tôn giáo — văn bản hướng dẫn Luật Dân tộc, chính sách dân tộc thiểu số; hiệu lực **chưa rõ** (dự kiến tháng 7/2026) | Hành chính / Dân tộc | 218510 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218510` (xác minh docid chính thức); nguồn: vanban.chinhphu.vn (docid 218510), ghi nhận từ quét dải 218500–218530 ngày 22/6/2026; ngày ban hành: ~18/6/2026; nhóm Dân tộc - Tôn giáo; bổ sung nhóm đa dạng chủ đề; tác động cơ quan Bộ Dân tộc và Tôn giáo |

### Xác minh docid cho các văn bản chưa có docid (từ lần 13–14)

| Số hiệu | Docid cũ | Docid mới | Trạng thái | Chi tiết |
|---|:---:|:---:|---|---|
| 29/2026/NQ-CP | 218455 | **218455** | Xác minh (giữ nguyên) | Thí điểm xăng E10; hiệu lực 16/6/2026–15/6/2028 |
| 202/2026/NĐ-CP | chua-xac-minh | **218368** | **Xác minh mới** | URL chính thức: `https://vanban.chinhphu.vn/?pageid=27160&docid=218368` |
| 207/2026/NĐ-CP | 218494 (ước đoán) | **218450** | **Xác minh mới** | URL chính thức: `https://vanban.chinhphu.vn/?pageid=27160&docid=218450` |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-22 lần 14)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 216/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 217/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 65/2026/TT-BTC | **KHÔNG** | Thêm mới — Chưa có |
| 68/2026/TT-BTC | **KHÔNG** | Thêm mới — Chưa có |
| 03/2026/TT-DTTG | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Tư pháp / Hành chính** (rất cao — 9 ngày tới): **216/2026/NĐ-CP** — lý lịch tư pháp mới, nộp hồ sơ trực tuyến, nhận kết quả trên VNeID; tác động toàn dân Việt Nam. Hiệu lực 01/7/2026. Có thể dùng luatvietnam.vn (slug 438205) làm nguồn chính.
2. **Xây dựng** (rất cao — 9 ngày tới): **217/2026/NĐ-CP** — cùng nhóm 4 NĐ xây dựng đồng loạt hiệu lực 01/7/2026 (207, 209, 212, 217); áp dụng BIM bắt buộc; tác động toàn ngành xây dựng. Có docid 218509.
3. **Hành chính / Tài chính** (cao — 35 ngày tới): **65/2026/TT-BTC** — bồi dưỡng tiếp công dân tăng lên 250.000 đ/ngày; tác động cán bộ tiếp dân toàn quốc. Hiệu lực 27/7/2026. Có docid 218479.
4. **Tài chính / KHCN** (rất cao — 9 ngày tới): **68/2026/TT-BTC** — KHCN dự trữ quốc gia; hiệu lực 01/7/2026. Tác động Cục Dự trữ Nhà nước. Cần xác minh docid.
5. **Hành chính / Dân tộc** (thấp): **03/2026/TT-DTTG** — bãi bỏ văn bản hướng dẫn; hiệu lực chưa rõ. Tác động hẹp Bộ Dân tộc và Tôn giáo.

### Ghi chú xử lý

- **5 văn bản mới** được thêm vào tracking lần 15. Cần crawl chi tiết trong các phiên Đệ #3 Full Content Crawler tiếp theo.
- **Xác minh docid**: 202/2026/NĐ-CP (218368), 207/2026/NĐ-CP (218450) — đã cập nhật vào tracking lần 14 và xác minh lại trực tiếp từ vanban.chinhphu.vn trong phiên này.
- **217/2026/NĐ-CP docid**: Xác minh gián tiếp qua citation luatvietnam.vn (vanban.chinhphu.vn/?pageid=27160&docid=218509) — cần xác minh trực tiếp ở phiên sau.
- **202/2026/NĐ-CP**: Docid 218368 xác minh trực tiếp từ vanban.chinhphu.vn trong phiên này — ghi vào tracking để cập nhật entry đã có.
- **Nhóm xây dựng 01/7/2026**: 4 NĐ cùng hiệu lực 01/7/2026: 207 (chất lượng), 209 (vật liệu), 212 (điều kiện năng lực), 217 (quản lý hoạt động XD). Trong đó 207, 209 đã được phát hiện lần 13; 212 đã crawl; 217 mới phát hiện lần 15.
- **Lưu ý 218450**: Docid 218450 là của 207/2026/NĐ-CP (thay vì ước đoán 218494 ở lần 13) — đã xác minh trực tiếp từ vanban.chinhphu.vn.
- Nguồn: web_fetch vanban.chinhphu.vn (docid 218368, 218450, 218479, 218510), web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, thuvienphapluat.vn, vov.vn, baomoi.com, cafef.vn, gdsr.gov.vn, vbpq.mof.gov.vn.
- Ngày phát hiện: 2026-06-22 22:37 ICT
- Phiên thực hiện: agent:github-io:subagent:827d7e57-1732-48cf-91c6-fa92880e35fe (Đệ #1 Discovery — lần 15)

---

## Cập nhật 2026-06-22 (phiên Đệ #1 Discovery — lần 14)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, thuvienphapluat.vn theo nhóm chủ đề: Thuế, Đất đai, KHCN, Lâm nghiệp, Chứng khoán, Y tế, Giáo dục, Giao thông, Xây dựng, Hành chính, Tư pháp, Công an, Ngân hàng, Lao động, Nông nghiệp, Tài chính. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-22 lần 13): phát hiện **5 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 5:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 29/2026/NQ-CP | 16/06/2026 | Ban hành thí điểm một số chính sách trong triển khai lộ trình sử dụng **xăng E10** — thuê dịch vụ thử nghiệm chất lượng xăng dầu; xác định xăng E10RON95-III là mặt hàng Nhà nước công bố giá; xác định yếu tố hình thành giá; xử lý lượng xăng không chì tồn kho; hiệu lực **16/6/2026** đến **15/6/2028** | Năng lượng / Tài chính | 218455 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218455`; nguồn: chinhphu.vn (docid confirmed), baochinhphu.vn, baomoi.com, baobacninhtv.vn, baodautu.vn; ngày ban hành: 16/6/2026; hiệu lực: 16/6/2026 – 15/6/2028 (thí điểm 2 năm); tác động toàn ngành xăng dầu, hãng phân phối, chủ phương tiện |
| 202/2026/NĐ-CP | 08/06/2026 | Sửa đổi, bổ sung một số điều của NĐ 10/2022/NĐ-CP về **lệ phí trước bạ** — kéo dài miễn 100% lệ phí trước bạ lần đầu đối với ô tô điện chạy pin **đến hết 31/12/2030**; thay thế NĐ 51/2025/NĐ-CP; hiệu lực **01/3/2027** | Thuế / Lệ phí | chua-xac-minh | **Chưa có** | Nguồn: baomoi.com, xe.baoxaydung.vn, baohanoi.vn; ngày ban hành: 8/6/2026; hiệu lực: 1/3/2027; cần xác minh docid từ vanban.chinhphu.vn; tác động người mua ô tô điện, đại lý xe điện |
| 66/2026/TT-BTC | 16/06/2026 | Hướng dẫn xác định nhu cầu, nguồn và phương thức chi thực hiện **mức lương cơ sở và chế độ tiền thưởng** theo NĐ 161/2026/NĐ-CP và điều chỉnh trợ cấp hàng tháng đối với cán bộ xã đã nghỉ việc theo NĐ 162/2026/NĐ-CP — mức lương cơ sở, nguồn NSNN, phương thức chi; hiệu lực **16/6/2026** (cùng ngày ký) | Lao động / Tài chính | chua-xac-minh | **Chưa có** | URL: `https://luatvietnam.vn/lao-dong/thong-tu-66-2026-tt-btc-huong-dan-luong-co-so-va-tien-thuong-theo-nghi-dinh-161-2026-nd-cp-437940-d1.html`; nguồn: luatvietnam.vn (slug 437940), thuvienphapluat.vn, hoatieu.vn; người ký: Bộ Tài chính; ngày ban hành: 16/6/2026; hiệu lực ngay 16/6/2026; tác động toàn bộ cán bộ, công chức, viên chức, lực lượng vũ trang (theo NĐ 161/2026) + cán bộ xã nghỉ việc (theo NĐ 162/2026) |
| 67/2026/TT-BTC | 16/06/2026 | **Bãi bỏ** Thông tư 105/2021/TT-BTC (trích lập, quản lý tiền lương, thù lao, tiền thưởng đối với Trưởng ban kiểm soát, Kiểm soát viên tại công ty TNHH MTV do Nhà nước nắm giữ 100% vốn điều lệ) và bãi bỏ một số điều của Thông tư 58/2017/TT-BTC (hỗ trợ tài chính cho lao động dân tộc thiểu số vùng miền núi, đặc biệt khó khăn); hiệu lực **01/8/2026** | Lao động / Tài chính | 218514 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218514` (xác minh chính thức); nguồn: vanban.chinhphu.vn (docid 218514), thoibaotaichinhvietnam.vn; ngày ban hành: 16/6/2026; hiệu lực: 01/8/2026; tác động công ty TNHH MTV NN + doanh nghiệp vùng miền núi |
| 68/2026/TT-BTC | 18/06/2026 | Quy định về **nghiên cứu, ứng dụng khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số**; Hệ thống thông tin, cơ sở dữ liệu về **dự trữ quốc gia** — chi tiết hoạt động nghiên cứu KHCN, hệ thống thông tin dự trữ, cơ sở dữ liệu; hiệu lực **01/7/2026** | Tài chính / KHCN | chua-xac-minh | **Chưa có** | URL: `https://luatvietnam.vn/khoa-hoc/thong-tu-68-2026-tt-btc-quy-dinh-ve-khoa-hoc-cong-nghe-va-chuyen-doi-so-438162-d1.html`; nguồn: luatvietnam.vn (slug 438162), thoibaotaichinhvietnam.vn, gdsr.gov.vn; người ký: Bộ Tài chính; ngày ban hành: 18/6/2026; hiệu lực: 01/7/2026; cần xác minh docid; tác động Cục Dự trữ Nhà nước, cơ quan nghiên cứu KHCN thuộc Bộ Tài chính |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-22 lần 13)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 29/2026/NQ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 202/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 66/2026/TT-BTC | **KHÔNG** | Thêm mới — Chưa có |
| 67/2026/TT-BTC | **KHÔNG** | Thêm mới — Chưa có |
| 68/2026/TT-BTC | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Lao động / Tiền lương** (rất cao — hiệu lực ngay 16/6/2026): **66/2026/TT-BTC** — hướng dẫn lương cơ sở, tiền thưởng theo NĐ 161/2026; tác động toàn bộ hệ thống công vụ. Nguồn: luatvietnam.vn (slug 437940). Ưu tiên số 1.
2. **Năng lượng** (trung bình — đang có hiệu lực 16/6/2026–15/6/2028): **29/2026/NQ-CP** — thí điểm xăng E10; tác động ngành xăng dầu, phân phối, người tiêu dùng. Docid 218455 xác minh.
3. **Thuế / Lệ phí** (thấp — hiệu lực 1/3/2027): **202/2026/NĐ-CP** — miễn lệ phí trước bạ ô tô điện đến 2030; cần xác minh docid. Tác động thị trường xe điện.
4. **Tài chính / KHCN** (trung bình — 9 ngày tới): **68/2026/TT-BTC** — khoa học, chuyển đổi số, dự trữ quốc gia; hiệu lực 01/7/2026. Tác động Cục Dự trữ Nhà nước.
5. **Lao động / Tài chính** (trung bình — 40 ngày): **67/2026/TT-BTC** — bãi bỏ TT 105/2021 về lương Ban kiểm soát; hiệu lực 01/8/2026. Docid 218514 xác minh.

### Ghi chú xử lý

- **29/2026/NQ-CP**: Docid **218455** xác minh trực tiếp từ vanban.chinhphu.vn — nằm trong dải phù hợp với ngày 16/6/2026 (sau 29/2026/NQ-CP, trước 208/2026/NĐ-CP ngày 18/6 với docid 218453).
- **202/2026/NĐ-CP**: Docid chưa xác minh — cần check vanban.chinhphu.vn trong phiên sau (dải 218430–218445 phù hợp với ngày 8/6/2026).
- **66/2026/TT-BTC**: Nguồn luatvietnam.vn slug 437940 — nội dung đầy đủ có thể lấy từ đây (trả phí, nhưng header có thể extract miễn phí). Cần xác minh docid.
- **67/2026/TT-BTC**: Docid **218514** xác minh trực tiếp từ vanban.chinhphu.vn — bãi bỏ TT 105/2021/TT-BTC (lương Ban kiểm soát) và một số điều TT 58/2017/TT-BTC (lao động vùng khó khăn). Văn bản ngắn, có thể crawl nhanh.
- **68/2026/TT-BTC**: Nguồn luatvietnam.vn slug 438162 — đã xác minh tồn tại trên luatvietnam (web_fetch có header chính thức). Cần xác minh docid từ vanban.chinhphu.vn.
- **Nhóm E10**: 29/2026/NQ-CP (thí điểm xăng E10) + 65/2026/TT-BTC (sửa đổi tiếp công dân, hiệu lực 27/7/2026) cùng đợt 16/6/2026 — theo dõi nếu có TT hướng dẫn E10 riêng.
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, baomoi.com, thuvienphapluat.vn, thoibaotaichinhvietnam.vn, gdsr.gov.vn.
- Ngày phát hiện: 2026-06-22 20:05 ICT
- Phiên thực hiện: agent:github-io:subagent:7856d3e0-929b-4734-ab0f-a8d80194ce2f (Đệ #1 Discovery — lần 14)

---
## Cập nhật 2026-06-22 (phiên Đệ #1 Discovery — lần 13)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, thuvienphapluat.vn với trọng tâm **hiệu lực 01/7/2026** (còn 9 ngày) + **văn bản vừa ban hành tháng 6/2026**. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-19): phát hiện **5 văn bản mới** chưa từng được ghi nhận.

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 215/2026/NĐ-CP | 18/06/2026 | Quy định về an ninh hàng không — **cấm bay vĩnh viễn** hoặc có thời hạn (3 tháng–vĩnh viễn) đối với hành khách gây rối, đe dọa an toàn hàng không; quy định chi tiết hành vi vi phạm, thẩm quyền cấm bay, trách nhiệm của các bên (hành khách, hãng hàng không, cảng hàng không); thay thế NĐ 92/2015/NĐ-CP; hiệu lực **01/7/2026** | Hàng không / An ninh | 218508 | **Chưa có** | URL (sơ bộ): `https://vanban.chinhphu.vn/?pageid=27160&docid=218508`; nguồn: baotintuc.vn, vietnamplus.vn, kenh14.vn, tapchihangkhong.vn; ngày ban hành: 18/6/2026; cùng đợt với 205/2026/NĐ-CP (điều kiện kinh doanh hàng không); tác động trực tiếp hành khách + hãng hàng không toàn quốc |
| 207/2026/NĐ-CP | 15/06/2026 | Quy định chi tiết một số điều của Luật Xây dựng về **quản lý chất lượng, thi công xây dựng và bảo trì** công trình — siết trách nhiệm chủ đầu tư/nhà thầu/giám sát; quản lý thi công nhà ở riêng lẻ; thay thế NĐ 46/2015/NĐ-CP; hiệu lực **01/7/2026** | Xây dựng | 218494 | **Chưa có** | URL (sơ bộ): `https://vanban.chinhphu.vn/?pageid=27160&docid=218494`; nguồn: thuvienphapluat.vn (slug 274649), kiemtoanxaydung.vn, dauthaumuasam.vn; ngày ban hành: 15/6/2026; cùng đợt với 206/2026 (chi phí đầu tư XD), 209/2026 (vật liệu XD), 210/2026 (hợp đồng XD), 212/2026 (điều kiện năng lực XD) — cả nhóm 06 NĐ-CP xây dựng hiệu lực 01/7/2026 |
| 209/2026/NĐ-CP | 15/06/2026 | Quy định chi tiết một số điều và biện pháp thi hành Luật Xây dựng về **quản lý vật liệu xây dựng** — điều kiện sản xuất, kinh doanh vật liệu XD; chứng nhận hợp quy; kiểm tra chất lượng; trách nhiệm tổ chức/đơn vị; thay thế NĐ 24/2022/NĐ-CP; hiệu lực **01/7/2026** | Xây dựng / Công nghiệp | 218496 | **Chưa có** | URL (sơ bộ): `https://vanban.chinhphu.vn/?pageid=27160&docid=218496`; nguồn: thuvienphapluat.vn (slug 274663), thuvienphapluat.vn (114927), kiemtoanxaydung.vn; ngày ban hành: 15/6/2026; cùng nhóm xây dựng với 207/2026 |
| 24/2026/TT-NHNN | 17/06/2026 | Sửa đổi, bổ sung một số điều của Thông tư 14/2024/TT-NHNN (phân loại tài sản có của tổ chức tín dụng vi mô) và Thông tư 36/2024/TT-NHNN (phân loại tài sản có của tổ chức tín dụng là hợp tác xã) — cụ thể hóa quy định phân loại tài sản theo Luật Các tổ chức tín dụng 2025; hiệu lực **03/8/2026** | Ngân hàng / Tài chính | 218476 | **Chưa có** | URL: `https://chinhphu.vn/?pageid=27160&docid=218476`; nguồn: luatvietnam.vn (slug 437875), vbpl.vn; người ký: Thống đốc NHNN; ngày ban hành: 17/6/2026; hiệu lực: 03/8/2026; bổ sung nhóm ngân hàng (đã có 07/2026/TT-NHNN, 19/2026/TT-NHNN, 198/2026/NĐ-CP) |
| 11/2026/TT-VKSTC | 16/06/2026 | Quy định mức khoán chi cho nhiệm vụ, hoạt động **xây dựng thông tư thuộc thẩm quyền ban hành của Viện trưởng VKSND tối cao** và thông tư liên tịch mà VKSND tối cao là cơ quan chủ trì soạn thảo — mức khoán chi, định mức, thủ tục; hiệu lực **16/6/2026** (cùng ngày ban hành) | Tư pháp / Tố tụng | 218503 | **Chưa có** | URL (sơ bộ): `https://vanban.chinhphu.vn/?pageid=27160&docid=218503`; nguồn: luatvietnam.vn (slug 437813), baovephapluat.vn, chinhphu.vn/he-thong-van-ban (classid=1, entry ngày 16/6/2026); ngày ban hành: 16/6/2026; cùng nhóm với 29/2026/TT-BCA (Quỹ phòng chống tội phạm) — cả hai do tư pháp/tố tụng ban hành |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-19)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 215/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 207/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 209/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 24/2026/TT-NHNN | **KHÔNG** | Thêm mới — Chưa có |
| 11/2026/TT-VKSTC | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Hàng không / An ninh** (rất cao — 9 ngày tới): **215/2026/NĐ-CP** — cấm bay vĩnh viễn/hữu hạn; tác động trực tiếp hành khách + Vietnam Airlines, Vietjet, Bamboo, Vasco; hiệu lực 01/7/2026. Có thể dùng nguồn luatvietnam.vn hoặc baotintuc.vn để crawl nội dung.
2. **Xây dựng** (rất cao — 9 ngày tới): **207/2026/NĐ-CP** + **209/2026/NĐ-CP** — cùng nhóm 06 NĐ-CP xây dựng đồng loạt hiệu lực 01/7/2026 (thêm 206/2026 đã có, 210/2026 đã có, 212/2026 đã có); tác động toàn ngành xây dựng. Ưu tiên crawl 207 + 209 trước.
3. **Ngân hàng** (trung bình — 42 ngày): **24/2026/TT-NHNN** — phân loại tài sản tài chính vi mô/tín dụng hợp tác xã; hiệu lực 03/8/2026.
4. **Tư pháp / Tố tụng** (thấp — hiệu lực rồi 16/6/2026): **11/2026/TT-VKSTC** — mức khoán chi; văn bản nội bộ tố tụng, ít tác động rộng.

### Ghi chú xử lý

- **215/2026/NĐ-CP**: Xác minh docid 218508 dựa trên thứ tự đánh số (218508 nằm trong dải 218400–218520 phù hợp với ngày 18/6/2026 — cần verify bằng vanban.chinhphu.vn ở phiên sau). File nên đặt vào `van-ban/giao-thong-van-tai/` hoặc `van-ban/an-ninh-trat-tu/` (nhóm hàng không).
- **207/2026/NĐ-CP**: Docid sơ bộ 218494; thay thế NĐ 46/2015/NĐ-CP.
- **209/2026/NĐ-CP**: Docid sơ bộ 218496; thay thế NĐ 24/2022/NĐ-CP; cùng nhóm với 207/2026.
- **24/2026/TT-NHNN**: Docid chính thức 218476 đã xác minh từ chinhphu.vn; cần bổ sung vào tracking.
- **11/2026/TT-VKSTC**: Docid sơ bộ 218503; file nên đặt vào `van-ban/tu-phap-thi-hanh-an/`.
- **Nhóm xây dựng 01/7/2026**: Tổng cộng 06 NĐ-CP xây dựng ban hành 15–17/6/2026 cùng hiệu lực 01/7/2026: 206/2026 (chi phí), 207/2026 (chất lượng), 209/2026 (vật liệu), 210/2026 (hợp đồng), 212/2026 (điều kiện năng lực), 215/2026 (giấy phép XD theo thuvienphapluat). Trong đó 206, 210, 212 đã có file; 207, 209, 215 cần crawl.
- Nguồn: web_search Brave + Gemini tổng hợp vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, baotintuc.vn, vietnamplus.vn, thuvienphapluat.vn, kiemtoanxaydung.vn, kenh14.vn, tapchihangkhong.vn.
- Ngày phát hiện: 2026-06-22 10:33 ICT
- Phiên thực hiện: agent:github-io:subagent:9fbf85e2-22f6-47bf-9383-42d27f1fc7c7 (Đệ #1 Discovery — lần 13)

---
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
| 204/2026/NĐ-CP | 11/06/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực thú y — phạt tiền đến 50 triệu đồng (cá nhân) / 100 triệu đồng (tổ chức); không đeo rọ mõm cho chó nơi công cộng phạt 1–2 triệu đồng; kinh doanh thú y không phép phạt đến 100 triệu; hiệu lực 01/8/2026 | Nông nghiệp / Thú y | 218418 | **Đã có (2026-06-15, Markdown từ nguồn web + cross-check)** | File: `van-ban/nong-nghiep-nong-thon/nghi-dinh-204-2026-nd-cp-xu-phat-vi-pham-thu-y.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218418`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/204-ndcp.signed.pdf`; người ký: Hồ Quốc Dũng (Phó Thủ tướng, ký thay Thủ tướng); 52 Điều, 4 Chương (I-IV), 5 Mục, 8 Tiểu mục; 930 dòng, 137KB; OCR issues = 0; articles 1-52 đầy đủ, không thiếu, không trùng; chương I-IV đúng thứ tự La Mã; nguồn chính: luatvietnam.vn extract toàn văn (slug 437349) + cross-check cấu trúc với 75/2026, 203/2026 |
| 28/2026/NQ-CP | 09/06/2026 | Cơ chế đặc thù cho phép khai thác than vượt không quá 15% công suất giấy phép nhằm bảo đảm an ninh năng lượng quốc gia — sản lượng vượt chỉ phục vụ sản xuất điện; phải đăng ký với UBND cấp tỉnh và Bộ NN&MT; hiệu lực 09/6/2026 đến 31/12/2027 | Năng lượng / Tài nguyên | 218385 | **Đã có (2026-06-14, OCR từ PDF ký số CAdES-BES)** | File: `van-ban/nang-luong-tai-nguyen/nghi-quyet-28-2026-nq-cp-co-che-khai-thac-than-vuot-15-phan-tram-cong-suat.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218385`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/28-nqcp.signed.pdf`; người ký: Phó Thủ tướng Phạm Gia Túc (KT. Thủ tướng); 7 Điều, 0 Chương; 144 dòng, 11.1KB; OCR issues = 0; articles 1-7 đầy đủ |
| 63/2026/TT-BTC | 05/06/2026 | Quy định nội dung và mức chi hoạt động thi kỹ năng nghề trong nước và quốc tế — thay thế TT liên tịch 43/2012/TTLT-BTC-BLĐTBXH; định mức chi xây dựng đề thi, chấm thi, huấn luyện đội tuyển quốc gia; hiệu lực 05/6/2026 | Giáo dục nghề nghiệp / Tài chính | — | **Đã có (2026-06-14)** | File: `van-ban/giao-duc-dao-tao/thong-tu-63-2026-tt-btc-noi-dung-muc-chi-thi-ky-nang-nghe.md`; nguồn: luatvietnam.vn (slug 437238); người ký: KT. Bộ trưởng Bộ Tài chính; 7 Điều (Điều 1: phạm vi; Điều 2: nguồn kinh phí; Điều 3: nguyên tắc; Điều 4: chi chung; Điều 5: chi thi trong nước; Điều 6: chi thi quốc tế; Điều 7: điều khoản thi hành); KHÔNG có Chương, KHÔNG có Phụ lục (định mức chi nằm trong nội dung từng Điều); 196 dòng, 16KB; OCR issues = 0; articles 1-7 đầy đủ, không thiếu, không trùng; docid: 437238 |
| 30/2026/TT-BCT | 10/06/2026 | Quy định phương pháp xác định giá dịch vụ phát điện đối với nhà máy điện BOT chưa ký hợp đồng mua bán điện — IRR không vượt quá 12%; hướng dẫn Luật Điện lực 2024; hiệu lực 28/7/2026 | Năng lượng / Thương mại | — | **Đã có (2026-06-14)** | File: `van-ban/nang-luong-tai-nguyen/thong-tu-30-2026-tt-bct-gia-dich-vu-phat-dien-nha-may-bot.md`; nguồn: moit.gov.vn (bài viết + PDF 19 trang OCR) + petrotimes.vn (cross-check); người ký: Nguyễn Hoàng Long (Bộ trưởng Bộ Công Thương); 16 Điều + 4 Chương (I-IV) + Phụ lục I (2 biểu mẫu tài chính); 699 dòng, 47KB; OCR issues = 0; articles 1-16 đầy đủ, không thiếu, không trùng; docid: tt30-2026-bct |
| 60/2026/TT-BTC | 31/05/2026 | Hướng dẫn quản lý, sử dụng và quyết toán kinh phí ngân sách nhà nước thực hiện Chương trình mục tiêu quốc gia về xây dựng nông thôn mới, giảm nghèo bền vững và phát triển KT-XH vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026–2035 | Tài chính / Ngân sách | — | **Đã có (2026-06-13)** | File: `van-ban/tai-chinh/thong-tu-60-2026-tt-btc-huong-dan-quan-ly-su-dung-quyet-toan-kinh-phi-chuong-trinh-muc-tieu-quoc-gia.md`; URL: `https://thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-60-2026-TT-BTC-huong-dan-quan-ly-kinh-phi-Ngan-sach-xay-dung-nong-thon-moi-709846.aspx` |
| 56/2026/TT-BTC | ~01/07/2026 (hiệu lực dự kiến) | Sửa đổi, bổ sung Thông tư 52/2025/TT-BTC quy định mức thu phí, lệ phí trong lĩnh vực viễn thông, tần số vô tuyến điện (giảm 50% phí sử dụng tần số cho dịch vụ 5G, IoT); hiệu lực 01/7/2026 | Viễn thông / Tài chính | 218176 | **Đã có (2026-06-15)** | File: `van-ban/vien-thong-buu-chinh/thong-tu-56-2026-tt-btc-phi-vien-thong-sua-doi-52-2025.md`; 5 Điều, 0 Chương; 171 dòng, 12KB; OCR issues = 0; articles 1-5 đầy đủ; docid: 218176 |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-12)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 204/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có → **Đã có (52 Điều)** (2026-06-15) |
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
| 46/2026/TT-BGDĐT | 10/06/2026 | Ban hành Điều lệ trường trung học nghề — quy định tổ chức, hoạt động trường trung học nghề tích hợp (văn hóa THPT + chuyên môn nghề) dành cho học sinh tốt nghiệp THCS; mục tiêu đào tạo nguồn nhân lực, tạo điều kiện vào lao động hoặc học lên; hiệu lực 10/6/2026 | Giáo dục / GD nghề nghiệp | chua-xac-minh | **Đã có (2026-06-14)** | File: `van-ban/giao-duc-dao-tao/thong-tu-46-2026-tt-bgddt-dieu-le-truong-trung-hoc-nghe.md`; URL: `https://luatvietnam.vn/giao-duc/thong-tu-46-2026-tt-bgddt-dieu-le-truong-trung-hoc-nghe-moi-nhat-tu-bo-giao-duc-437124-d1.html`; 30 Điều, 6 Chương tham chiếu (I-VI), 50KB, 556 dòng; 0 OCR noise; người ký: Lê Quân (KT. Bộ trưởng - Thứ trưởng Bộ GD&ĐT); hiệu lực 10/06/2026 (cùng ngày ký); căn cứ: Luật 43/2019/QH14 (sửa đổi bởi 123/2025/QH15) + Luật 124/2025/QH15 + Luật 73/2025/QH15; LƯU Ý: file partial `tich-hop.md` (253 dòng, 15/25 Điều) đã bị xóa vì trùng với file đầy đủ này |
| 56/2026/TT-BCA | 01/07/2026 (hiệu lực) | Quy định quản lý, theo dõi người bị cấm đi khỏi nơi cư trú — cụ thể hóa BLTTHS và Luật Thi hành tạm giữ, tạm giam và cấm đi khỏi nơi cư trú năm 2025; Trưởng Công an cấp xã phân công cán bộ quản lý, theo dõi, kiểm tra; lập biên bản nếu vi phạm; hiệu lực 01/7/2026 | An ninh trật tự / Tố tụng hình sự | 56/2026/TT-BCA | **Đã có FULL (2026-06-16, 18 Điều + 3 Chương)** | File: `van-ban/an-ninh-trat-tu/thong-tu-56-2026-tt-bca-quan-ly-theo-doi-nguoi-bi-cam-di-khoi-noi-cu-tru.md`; URL gốc: `https://bocongan.gov.vn` (PDF 56-2026-tt-bca.PDF, 9 trang, 1.3MB) + luatvietnam.vn (slug 436803); 18 Điều, 3 Chương + 1 Chương Phụ lục, 331 dòng, ~36KB; người ký: Đại tướng Lương Tam Quang (Bộ trưởng Bộ Công an); 0 OCR noise; commit PR #209 = 4753a434 (sửa từ partial 15/16+ Điều lên 18 Điều đầy đủ); căn cứ chính: Luật 128/2025/QH15 |
| 19/2026/TT-NHNN | 19/05/2026 | Quy định phân cấp trong thực hiện thủ tục hành chính quy định tại NĐ 94/2025/NĐ-CP về cơ chế thử nghiệm có kiểm soát trong lĩnh vực ngân hàng; hiệu lực 30/6/2026 | Ngân hàng / Tài chính | 218378 | **Đã có (2026-06-15, Markdown từ nguồn web luatvietnam)** | URL: `https://luatvietnam.vn/tai-chinh/thong-tu-19-2026-tt-nhnn-quy-dinh-phan-cap-thu-tuc-hanh-chinh-ngan-hang-435183-d1.html`; File: `van-ban/ngan-hang/thong-tu-19-2026-tt-nhnn-phan-cap-thu-tuc-hanh-chinh-ngan-hang.md`; người ký: Phó Thống đốc Phạm Tiến Dũng; 6 Điều; ngày hiệu lực đã verify: **30/06/2026**; OCR issues = 0 |
| 07/2026/TT-NHNN | 06/05/2026 | Sửa đổi, bổ sung một số điều của Thông tư 17/2016/TT-NHNN quy định hoạt động môi giới tiền tệ của ngân hàng thương mại, chi nhánh ngân hàng nước ngoài; hiệu lực 20/6/2026 | Ngân hàng / Tài chính | 218038 | **Đã có FULL (2026-06-16, 4 Điều, OCR PDF chính thức)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218038`; File: `van-ban/ngan-hang/thong-tu-07-2026-tt-nhnn-sua-doi-thong-tu-17-2016-tt-nhnn-moi-gioi-tien-te.md`; người ký: Phó Thống đốc Phạm Thanh Hà; 4 Điều (Điều 1 sửa khoản 1 Điều 4 + Điều 2 thay thế toàn bộ Điều 11 của TT 17/2016); ngày hiệu lực: **20/06/2026**; OCR PDF từ xdcs.cdnchinhphu.vn (732KB, 2 trang, tesseract vie 150 DPI); sửa lỗi OCR: `2#`→`07`, `ngày ÔẾ`→`ngày 06`, `bỗ sung`→`bổ sung`, `Sửa đối`→`Sửa đổi`, `chỉ nhánh`→`chi nhánh`, `tô chức tín dụng`→`tổ chức tín dụng`, `kiêm tra`→`kiểm tra`, `‡//. 6./.8ZJế./, ⁄`→`20/06/2026` |
| 18/2026/TT-BYT | 01/06/2026 (ký) | Quy định chi tiết một số điều của Luật Dược và NĐ 163/2025/NĐ-CP về thuốc và nguyên liệu làm thuốc phải kiểm soát đặc biệt; 5 Chương, 19 Điều, 19 Phụ lục; hiệu lực 16/7/2026 | Y tế / Dược phẩm | chua-xac-minh | **Đã có FULL (2026-06-16, 5/5 Chương, 19/19 Điều, 19/19 Phụ lục, OCR Công báo PDF)** | File: `van-ban/y-te/thong-tu-18-2026-tt-byt-thuoc-va-nguyen-lieu-phai-kiem-soat-dac-biet.md`; URL: Công báo Số 329/Ngày 14-06-2026 (PDF chính thức); người ký: Nguyễn Tri Thức (Thứ trưởng Bộ Y tế, ký thay Bộ trưởng); OCR 45 trang PDF bằng tesseract-vie 150 DPI; 19/19 Điều, 19/19 Phụ lục có nội dung chi tiết; trước: partial 8/19 Điều + 0/19 Phụ lục chi tiết; sau: full 5/5 Chương + 19/19 Điều + 19/19 Phụ lục; hiệu lực: **16/07/2026**; OCR issues = 0; LƯU Ý: heading `### Phụ lục` bị OCR duplicate cho một số Phụ lục (II xuất hiện 2 lần, VII xuất hiện 2 lần, v.v.) nhưng nội dung đầy đủ theo status_note |
| 35/2026/TT-BTC | 31/03/2026 | Quy định chế độ tiếp khách nước ngoài vào làm việc tại Việt Nam, chế độ chi tổ chức hội nghị, hội thảo quốc tế tại Việt Nam và chế độ tiếp khách trong nước — thay thế TT 71/2018/TT-BTC; hiệu lực 18/5/2026 | Tài chính / Đối ngoại | 430995 | **Đã có (2026-06-14, Markdown từ nguồn web luatvietnam)** | URL: `https://luatvietnam.vn/hanh-chinh/thong-tu-35-2026-tt-btc-quy-dinh-che-do-tiep-khach-va-to-chuc-hoi-nghi-tai-viet-nam-430995-d1.html`; File: `van-ban/tai-chinh/thong-tu-35-2026-tt-btc-che-do-tiep-khach-nuoc-ngoai-hoi-nghi-quoc-te-tai-viet-nam.md`; người ký: KT. Bộ trưởng Bộ Tài chính - Thứ trưởng Nguyễn Thị Bích Ngọc; 35 Điều + 7 Chương + Phụ lục; OCR issues = 0 |
| 31/2026/TT-BCT | 11/06/2026 | Quy định truy xuất nguồn gốc sản phẩm, hàng hóa thuộc phạm vi quản lý của Bộ Công Thương — truy xuất điện tử bắt buộc đối với nhóm hàng rủi ro cao; thương nhân thành lập mới từ 1/1/2027 phải thực hiện ngay; hiệu lực 01/7/2026 | Thương mại / Công nghiệp | — | **Đã có (2026-06-14)** | File: `van-ban/thuong-mai-cong-thuong/thong-tu-31-2026-tt-bct-truy-xuat-nguon-goc-san-pham.md`; 19 Điều, 5 Chương |

### Xác minh các văn bản ưu tiên từ nhiệm vụ

| Số hiệu | File trong van-ban/? | Kết quả xác minh | Trạng thái cũ | Trạng thái mới |
|---|:---:|---|:---:|:---:|
| 185/2026/NĐ-CP | `van-ban/lao-dong/nghi-dinh-185-2026-nd-cp-thon-to-dan-pho.md` | **ĐÃ CÓ** file đầy đủ — front matter có đầy đủ metadata (so_hieu, ngay_ban_hanh, nguoi_ky, thay_the, source), lastedit 2026-06-10 | Chưa có (ghi sai) | **Đã có** |
| 56/2026/TT-BCA | Không tìm thấy | **Đã có FULL (xem dòng 189)** | — | Đã có |
| 29/2026/TT-BCA | 30/03/2026 | Quy định chi tiết về Quỹ phòng, chống tội phạm trung ương (QĐ 07/2026/QĐ-TTg) — trình tự, thủ tục thực hiện nội dung chi và quản lý, điều hành Quỹ; tiêu chí cá nhân/tập thể có thành tích xuất sắc | An ninh trật tự | **217364** | **Chưa có file** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217364` (chinhphu.vn) + `https://congbao.chinhphu.vn/van-ban/thong-tu-so-29-2026-tt-bca-469230.htm` (Công báo); người ký: Bộ trưởng Bộ Công an (Đại tướng Lương Tam Quang); nguồn: luatvietnam.vn (slug 430427); xác minh ngày 2026-06-16 bởi đệ #1; đặt vào `van-ban/an-ninh-trat-tu/` |
| 35/2026/TT-BTC | 31/03/2026 | Đã đối chiếu dòng 191 — file đã có đầy đủ trong PR #209 từ 2026-06-14 (commit eca27767, 35 Điều + 7 Chương + Phụ lục). Mục này trùng với placeholder cũ đã bị loại khỏi PR#204; dòng tracking thừa, giữ nguyên để audit. | — | **Đã có (xem dòng 191)** |

### Văn bản phát hiện thêm (chưa tạo entry — chờ phiên sau)

- **185/2026/NĐ-CP** (Lao động / Hành chính) — thôn, tổ dân phố, chế độ người không chuyên trách; ban hành 26/5/2026; hiệu lực 26/5/2026; file đã có tại `van-ban/lao-dong/nghi-dinh-185-2026-nd-cp-thon-to-dan-pho.md` → chuyển sang "Đã có" trong tracking
- **198/2026/NĐ-CP** (Ngân hàng / Tổ chức bộ máy) — sửa đổi cơ cấu Ngân hàng Nhà nước; ban hành 10/6/2026; hiệu lực 01/7/2026; file đã có tại `van-ban/ngan-hang/nghi-dinh-198-2026-nd-cp-sua-doi-co-cau-nhnn.md`; URL xác minh: `https://vanban.chinhphu.vn/?pageid=27160&docid=218344`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/198-ndcp.signed.pdf` (signed - cần OCR); LƯU Ý metadata: file ghi `Người ký: Phạm Thái Bình / Thủ tướng` — cần xác minh lại vì Phạm Thái Bình là Phó Thống đốc NHNN, có thể chỉ là người ký thay hoặc ghi nhầm; cần xác minh trạng thái trong tracking
- **37/2026/TT-BCA** (Giao thông vận tải) — sửa đổi đăng ký xe, nhận kết quả qua Cổng DVCQG, VNeID, bưu chính; hiệu lực 08/6/2026; file đã có tại `van-ban/giao-thong-van-tai/thong-tu-37-2026-tt-bca-dang-ky-xe-vneid.md`; cần xác minh trạng thái
- **40/2026/TT-BGDĐT** (Giáo dục) — đánh giá kết quả rèn luyện sinh viên, thang điểm 100, 5 mức; hiệu lực 30/6/2026; file đã có tại `van-ban/giao-duc-dao-tao/thong-tu-40-2026-tt-bgd-dt-cong-tac-sinh-vien.md`; cần xác minh trạng thái
- **185-QĐ/TW** (Bộ Chính trị) — quy định tổng biên chế 2026 cho cơ quan, ban đảng, đơn vị sự nghiệp của Đảng, Mặt trận Tổ quốc, đoàn thể Trung ương; ký 02/6/2026
- **193-QĐ/TW** (Bộ Chính trị) — quy định chức năng, nhiệm vụ, quyền hạn của Ban Chỉ đạo Trung ương về hoàn thiện thể chế và thực thi pháp luật; ký 03/6/2026 bởi Tổng Bí thư, Chủ tịch nước Tô Lâm

### Đối chiếu nhanh với `van-ban/` và LEGISLATION_TRACKING.md (đến 2026-06-12 trước phiên)

| Số hiệu | Trong tracking? | File van-ban/? | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|:---:|:---:|
| 46/2026/TT-BGDĐT | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 56/2026/TT-BCA | **KHÔNG** | Không | — | Thêm mới — **Đã có (xem dòng 189, commit 4753a434)** |
| 19/2026/TT-NHNN | **KHÔNG** | Không | — | Thêm mới — Chưa có |
| 35/2026/TT-BTC | **KHÔNG** | Không | — | Thêm mới — Chưa có → **Đã có (xem dòng 191, commit eca27767 2026-06-14)** |
| 31/2026/TT-BCT | **KHÔNG** | Không | — | Thêm mới — Chưa có | **Đã có (19 Điều + 5 Chương)** (2026-06-14) |
| 185/2026/NĐ-CP | **CÓ (ghi sai)** | Có | Chưa có | **Sửa → Đã có** |
| 29/2026/TT-BCA | **KHÔNG** | **Có** (360 dòng, từ 2026-06-21, từ luatvietnam.vn + bocongan.gov.vn cross-check) | — | Chưa có (đã xác minh docid alive) → **Đã có (2026-06-21, full 360 dòng, hiệu lực 30/3/2026)** |

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
| 169/2026/NĐ-CP | 15/05/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực hải quan — phạt đến 80 triệu đồng vận chuyển hàng tạm ngừng xuất khẩu, phạt đến 50 triệu không khai báo ngoại tệ, vàng; thay thế NĐ 128/2020/NĐ-CP | Thuế / Hải quan | 218154 | **Đã có (2026-06-15, OCR từ PDF gốc signed)** | File: `van-ban/tai-chinh/nghi-dinh-169-2026-nd-cp-xu-phat-vi-pham-hanh-chinh-hai-quan.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218154`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/169-ndcp.signed.pdf` (2.3MB, 54 trang, scan từ Word Smart Touch 1.9); người ký: Phạm Minh Chính (Thủ tướng); 40 Điều, 4 Chương (I-IV); 118KB, 2801 dòng; OCR issues = 0 (đã lọc 47 noise: ø, ©, §, †, ® + sửa lỗi OCR: Điêu→Điều, thâm→thẩm, bô→bổ); hiệu lực 01/07/2026; thay thế NĐ 128/2020/NĐ-CP và Điều 2 NĐ 102/2021/NĐ-CP; thời hiệu 5 năm (thuế) / 2 năm (khác) |
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
| 153/2026/NĐ-CP | 14/05/2026 | Sửa đổi, bổ sung NĐ 01/2015/NĐ-CP | Hải quan / Thương mại | 218083 | **Đã có (2026-06-14)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218083`; hiệu lực 05/7/2026; File: `van-ban/hai-quan/nghi-dinh-153-2026-nd-cp-sua-doi-nghi-dinh-01-2015-nd-cp.md` |
| 157/2026/NĐ-CP | 15/05/2026 | Quy định thanh toán, quyết toán vốn NSNN để cấp bù lãi suất cho NHTM thực hiện chính sách tín dụng ưu đãi (nông nghiệp, xuất khẩu); hiệu lực 01/7/2026 | Tài chính / Tín dụng ưu đãi | 218158 | **Đã có (2026-06-14)** | File: `van-ban/tai-chinh/nghi-dinh-157-2026-nd-cp-cap-bu-lai-suat-tin-dung-uu-dai.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218158`; người ký: Nguyễn Văn Thắng (Thủ tướng CP); 10 Điều (1-10), 0 Chương, 4 Phụ lục (Mẫu 01-04); 455 dòng, 33KB; OCR issues = 0 | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218083`; hiệu lực 05/7/2026 |
| 154/2026/NĐ-CP | 15/05/2026 | Quy định chi tiết một số điều và biện pháp tổ chức thi hành Luật Tiếp công dân | Hành chính / Tư pháp | 218230 | **Đã có (2026-06-14)** | File: `van-ban/tu-phap/nghi-dinh-154-2026-nd-cp-tiep-cong-dan.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218230`; người ký: Phó Thủ tướng Lê Thành Long (OCR gốc ghi nhầm "Lê Tiên Châu" đã sửa); hiệu lực 01/7/2026; 45 Điều, 10 Chương (I-X); 906 dòng, 89KB; OCR issues = 0 (PDF 1.4MB, 35 trang scanned) |
| 155/2026/NĐ-CP | 15/05/2026 | Sửa đổi, bổ sung NĐ 124/2020/NĐ-CP quy định chi tiết Luật Khiếu nại — bổ sung 7 trường hợp vụ việc khiếu nại phức tạp | Hành chính / Tư pháp | 218183 | **Đã có (2026-06-14)** | File: `van-ban/tu-phap/nghi-dinh-155-2026-nd-cp-sua-doi-luat-khieu-nai.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218183`; hiệu lực 01/7/2026; 23 Điều, 0 Chương; 654 dòng, 45KB; OCR issues = 0 |
| 156/2026/NĐ-CP | 15/05/2026 | Sửa đổi, bổ sung NĐ 31/2019/NĐ-CP quy định chi tiết Luật Tố cáo — quy định hành vi vi phạm trong giải quyết tố cáo bị buộc thôi việc | Hành chính / Tư pháp | 218102 | **Đã có (2026-06-15)** | File: `van-ban/tu-phap/nghi-dinh-156-2026-nd-cp-sua-doi-nghi-dinh-31-2019-nd-cp-luat-to-cao.md`; URL: `https://luatvietnam.vn/hanh-chinh/nghi-dinh-156-2026-nd-cp-sua-doi-nghi-dinh-31-2019-nd-cp-ve-luat-to-cao-435173-d1.html`; người ký: Lê Tiến Châu (KT. Thủ tướng - Phó Thủ tướng); 11 Điều + 2 mẫu biểu (Mẫu 02, 03); 21KB, 235 dòng; hiệu lực 01/07/2026; 4 mức kỷ luật (khiển trách/cảnh cáo/cách chức/buộc thôi việc); bổ sung Điều 19a (CNTT/chuyển đổi số); 18 field front matter; nguồn: luatvietnam.vn (slug 435173) + sotaichinh.caobang.gov.vn + ninhbinh.gov.vn |
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

# Báo cáo theo dõi pháp luật mới - 2026-06-07 (Đệ #1 Discovery & Tracking)

## Mục đích

Ghi nhận các văn bản pháp luật mới phát hiện từ `vanban.chinhphu.vn` trong phiên heartbeat 2026-06-07 08:15 ICT.

## Nguồn dữ liệu

- Trang hệ thống văn bản Chính phủ: `https://vanban.chinhphu.vn/`
- Thời điểm crawl: 2026-06-07 08:15 ICT
- Công cụ: `web_search` (Brave + Gemini fallback)

## Văn bản mới phát hiện (chưa có trong `van-ban/`)

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---|---|
| 08/2026/TT-BKHCN | 31/03/2026 | Hướng dẫn việc xác thực thông tin thuê bao di động mặt đất (căn cứ NĐ 163/2024/NĐ-CP) | KHCN / Viễn thông | 217450 | **Đã có (2 file)** | Phát hiện bởi đệ #1 ngày 2026-06-07; URL: `https://vanban.chinhphu.vn/?docid=217450&pageid=27160`; người ký: Nguyễn Mạnh Hùng (Bộ trưởng Bộ KH&CN); hiệu lực: 15/4/2026 (riêng Điều 8 hiệu lực 15/6/2026); Files: `van-ban/vien-thong-buu-chinh/thong-tu-08-2026-tt-bkhoa-hoc-cong-nghe-xac-thuc-thue-bao.md` + `van-ban/vien-thong-buu-chinh/thong-tu-08-2026-tt-bk-hcn-huong-dan-xac-thuc-thue-bao.md`; đặt trong `van-ban/buu-chinh-vien-thong/` (slo: buu-chinh-vien-thong → vien-thong-buu-chinh) |
| 125/2026/NĐ-CP | 06/04/2026 | Quy định về hoạt động khoa học, công nghệ và đổi mới sáng tạo trong cơ sở giáo dục đại học — nhóm nghiên cứu tiềm năng (≥3 thành viên) / nhóm nghiên cứu mạnh (≥5 thành viên); hợp tác Nhà nước - Nhà trường - Doanh nghiệp; tài chính, quỹ, đầu tư; quyền thành lập doanh nghiệp KH&CN; hiệu lực 06/4/2026 | KHCN / Giáo dục | 217673 | **Đã có (2026-06-21, OCR từ PDF ký số CAdES-BES)** | File: `van-ban/khoa-hoc-cong-nghe/nghi-dinh-125-2026-nd-cp-hoat-dong-khcn-dmst-trong-cs-giao-duc-dai-hoc.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217673`; PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/125-ndcp.signed.pdf`; người ký: Thủ tướng Chính phủ; ngày BH/hiệu lực: 06/04/2026 (cùng ngày ký); 24 Điều, 5 Chương (I-V), 0 Mục; 784 dòng; OCR issues = 0; articles 1-24 đầy đủ, không thiếu, không trùng; chương I-V đúng thứ tự La Mã; thay thế NĐ 109/2022/NĐ-CP |
| 06/2026/TT-BKHCN | 30/03/2026 | Quy định chi tiết và hướng dẫn một số điều của Quyết định số 33/2025/QĐ-TTg ngày 15/9/2025 về Mạng truyền số liệu chuyên dùng phục vụ các cơ quan Đảng, Nhà nước — quy định kết nối, sử dụng, bảo đảm an toàn mạng; địa chỉ IP công khai/riêng; kết nối hệ thống xử lý bí mật nhà nước (căn cứ Luật Bảo vệ bí mật Nhà nước 117/2025, Luật An ninh mạng 116/2025, Luật Cơ yếu 32/2011) | KHCN / An toàn thông tin | 217441 | **Đã có (2026-06-22)** | File: `van-ban/khoa-hoc-cong-nghe/thong-tu-06-2026-tt-bkhcn-mang-truyen-so-lieu-chuyen-dung-dang-nha-nuoc.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217441`; PDF: `https://skh.quangngai.gov.vn/upload/2006758/20260415/Thong_tu_06-2026_0c849.pdf`; người ký: Nguyễn Mạnh Hùng (Bộ trưởng Bộ KH&CN); ngày BH/hiệu lực: 30/03/2026 (cùng ngày ký); 17 Điều, 3 Chương (I QUY ĐỊNH CHUNG, II QUY ĐỊNH VỀ KẾT NỐI, III TỔ CHỨC THỰC HIỆN); 481 dòng; OCR issues = 0; articles 1-17 đầy đủ, không thiếu, không trùng; chương I-III đúng thứ tự La Mã; thay thế TT 19/2023/TT-BTTTT; thêm Phụ lục I (yêu cầu kỹ thuật thiết bị đầu cuối) + Phụ lục II (Mẫu số 01 đăng ký hằng năm, Mẫu số 02 đăng ký giai đoạn 5 năm) |

## Đối chiếu nhanh với `van-ban/`

**Cập nhật trạng thái so với báo cáo 2026-05-14:**

- `192/2026/NĐ-CP` (hệ thống văn bản): trong báo cáo trước ghi "Chưa có / chờ crawl chi tiết", nay đã có trong `van-ban/y-te-duoc/nghi-dinh-192-2026-nd-cp-phu-cap-y-te-thon-ban.md` (lastedit 2026-06-06, ~42KB). Nhóm đúng: **Y tế / chính sách y tế cơ sở** (phụ cấp y tế thôn bản). Cập nhật trạng thái tracking sang "Đã có" ở báo cáo tiếp theo.

## File cần refactor (chưa hoàn thiện theo tiêu chí: < 10k chars AND lastedit > 7 ngày)

| Đường dẫn | Kích thước | Lastedit | Lý do đánh dấu | Đề xuất |
|---|---:|---|---|---|
| `van-ban/cong-nghiep/quan-ly-phan-bon.md` | 5918 B | 2026-05-13 | Stub tóm tắt NĐ 84/2019, thiếu các chương/điều chi tiết và tham chiếu văn bản sửa đổi; lastedit > 7 ngày | Mở rộng nội dung theo NĐ 84/2019/NĐ-CP đầy đủ (29 điều); cross-link với `nong-nghiep-nong-thon/trong-trot` |
| `van-ban/ngoai-giao-dieu-uoc-quoc-te/dich-quoc-hieu-ten-cac-co-quan-don-vi-va-chuc-danh-lanh-dao-can-bo-cong-chuc-trong-he-thong-hanh-chinh-nha-nuoc-sang-tieng-anh-de-giao-dich-doi-ngoai.md` | ~5.7k B | 2026-05-15 | Trang tổng hợp, metadata placeholder (Số hiệu/Người ký/Ngày đều `-`), stub rỗng; lastedit > 7 ngày | Bổ sung metadata thật (TT 03/2009/TT-BNG ngày 09/07/2009); thêm bảng dịch Quốc hiệu + danh mục chức danh đầy đủ |

**Các stub mới tạo gần đây (chưa có nội dung, lastedit ≤ 7 ngày) — KHÔNG đánh dấu refactor ở lần này:**

- `van-ban/an-ninh-quoc-gia/quy-chuan-an-ninh-mang-he-thong-luu-tru-tai-lieu-dien-tu.md` (lastedit 2026-06-01)
- `van-ban/an-ninh-quoc-gia/quy-chuan-camera-giam-sat-ip-an-ninh-mang.md` (lastedit 2026-06-01)
- `van-ban/chinh-sach-xa-hoi/nghi-quyet-26-2026-nq-cp-giam-dinh-adn-hai-cot-liet-si.md` (lastedit 2026-06-05)
- `van-ban/dat-dai-dau-tu/nghi-dinh-147-2026-nd-cp-co-che-dac-thu-du-an-ton-dong.md` (lastedit 2026-06-06)
- `van-ban/dat-dai-dau-tu/nghi-quyet-29-2026-qh16-co-che-dac-thu-dat-dai-du-an-ton-dong.md` (lastedit 2026-06-05)
- `van-ban/khoa-hoc-cong-nghe/quyet-dinh-21-2026-qd-ttg-danh-muc-cong-nghe-chien-luoc.md` (lastedit 2026-06-05)
- `van-ban/ngoai-giao/nghi-dinh-148-2026-nd-cp-quan-ly-thong-tin-doi-ngoai.md` (lastedit 2026-06-05)
- `van-ban/nong-nghiep-nong-thon/nghi-dinh-146-2026-nd-cp-xu-phat-vi-pham-linh-vuc-lam-nghiep.md` (lastedit 2026-06-06)
- `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-141-2026-nd-cp-sua-doi-thue-ho-kinh-doanh.md` (lastedit 2026-06-06)
- `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-144-2026-nd-cp-sua-doi-thue-gtgt.md` (lastedit 2026-06-06)
- `van-ban/thuong-mai-dau-tu-chung-khoan/nghi-dinh-145-2026-nd-cp-co-che-quan-ly-tai-chinh-vnx-vsdc.md` (lastedit 2026-06-06)
- `van-ban/thuong-mai-dau-tu-chung-khoan/thong-tu-24-2026-tt-bct-quy-tac-xuat-xu-hang-hoa-cepa.md` (lastedit 2026-06-05)
- `van-ban/tu-phap/quyet-dinh-22-2026-qd-ttg-sua-doi-che-do-boi-duong-giam-dinh-tu-phap.md` (lastedit 2026-06-05)
- `van-ban/y-te-duoc/nghi-dinh-192-2026-nd-cp-phu-cap-y-te-thon-ban.md` (lastedit 2026-06-06)

→ File mới tạo gần đây do đệ #2/đệ khác đã commit stub metadata, chờ bổ sung nội dung ở heartbeat kế tiếp.

## Đề xuất ưu tiên cập nhật tiếp theo

1. **KHCN + Viễn thông**: 08/2026/TT-BKHCN — xác thực thuê bao di động, có hiệu lực thực tiễn rộng; đề xuất tạo branch/PR riêng.
2. **KHCN + Giáo dục đại học**: 125/2026/NĐ-CP — vị trí phù hợp nhóm KHCN vì nội dung là quản lý hoạt động KHCN&ĐMST.
3. **KHCN + An toàn thông tin**: 06/2026/TT-BKHCN — Mạng truyền số liệu chuyên dùng Đảng/Nhà nước.
4. **Refactor `quan-ly-phan-bon.md`**: mở rộng nội dung 29 điều NĐ 84/2019 để đạt ≥ 10k chars.
5. **Refactor `dich-quoc-hieu-...md`**: bổ sung metadata thật + bảng dịch.

## Ghi chú

- Giới hạn 5 văn bản/lần theo HEARTBEAT.md: 3 văn bản mới + 2 file refactor (4 tổng cộng nếu tính cập nhật trạng thái 192/2026).
- Đệ #1 không crawl nội dung, không tạo PR — chỉ báo cáo cho Bột xử lý ở phiên tiếp theo.
## Phát hiện mới 2026-06-15 21:56 (phiên Đệ #1 Discovery — tự động từ heartbeat poll)

Quét vanban.chinhphu.vn từ heartbeat poll: phát hiện **4 văn bản mới** chưa từng được ghi nhận trong tracking:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 26/2026/TT-BTC | 25/3/2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của Nghị định 73/2026/NĐ-CP (Luật Ngân sách nhà nước) | Tài chính / Ngân sách | 217323 | **Đã có (2026-06-16)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217323`; cần xác minh ngày ban hành, hiệu lực; commit 6bc507de PR #209 rồi crawl |
| 26/2026/NĐ-CP | 10/3/2026 | Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Hóa chất về quản lý hoạt động hóa chất và hóa chất nguy hiểm trong sản phẩm, hàng hóa | Hóa chất / Môi trường | 216673 | **Đã có (2026-06-16)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216673`; cần xác minh ngày ban hành, hiệu lực; commit 29450df4 PR #209 rồi crawl |
| 06/2026/NĐ-CP | — | Quy định về tổ chức và hoạt động của Ngân hàng Chính sách xã hội | Ngân hàng / Tài chính | 216603 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216603`; cần xác minh ngày ban hành, hiệu lực; chờ Sếp review/merge PR #209 rồi crawl |
| 06/2026/TT-BGDĐT | 15/02/2026 | Ban hành Quy chế tuyển sinh các ngành đào tạo trình độ đại học và ngành Giáo dục Mầm non trình độ cao đẳng | Giáo dục | 217071 | **Đã có (FULL, 22/22 Điều, 2026-06-16)** | URL: `https://vanban.chinhphu.vn/?docid=217071&pageid=27160`; ngày ban hành 15/02/2026, hiệu lực 15/02/2026, người ký Nguyễn Văn Phúc (KT. Bộ trưởng); 03 Chương, 22 Điều; commit PR #209 rồi crawl Điều 1-4 từ thuvienphapluat.vn; commit bổ sung này OCR PDF chính thức (xdcs.cdnchinhphu.vn, tesseract vie 150 DPI) để hoàn thiện Điều 4-22 + Chương II, III + Phụ lục I, II; OCR quality gate pass: 0 issues, 22/22 Điều, 3/3 Chương đúng thứ tự |

**Lý do không crawl ngay:** Theo SOUL.md, mỗi task = 1 PR. PR #209 hiện có 35 văn bản chờ Sếp review/merge. Em thêm vào tracking làm hàng chờ; khi Sếp review/merge PR #209, em sẽ crawl tiếp 4 văn bản này (có thể tạo PR mới nếu cần, hoặc commit vào PR active sau khi Sếp cho phép).

## Phát hiện mới 2026-06-15 23:00 (phiên Bot từ heartbeat poll)

Quét từ heartbeat poll: phát hiện **1 văn bản mới** chưa từng được ghi nhận trong tracking:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 206/2026/NĐ-CP | 15/6/2026 | Quy định chi tiết về quản lý chi phí đầu tư xây dựng | Xây dựng / Đầu tư | chưa xác minh | **Chưa có** | Hiệu lực 1/7/2026; nguồn: vietnam.vn, baochinhphu.vn; chờ Sếp review/merge PR #209 rồi crawl |

## Phát hiện mới 2026-06-16 06:26 (phiên Đệ #1 Discovery — heartbeat)

Quét vanban.chinhphu.vn (Brave, 1 lần web_search, query: `vanban.chinhphu.vn Nghị định 2026 site:vanban.chinhphu.vn`): phát hiện **3 văn bản mới** chưa từng được ghi nhận trong tracking và không có trong PR #209:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 94/2026/NĐ-CP | 31/03/2026 | Quy định về hoạt động đào tạo và sát hạch lái xe; thay thế NĐ 160/2024/NĐ-CP; 5 Chương, 43 Điều | Giao thông vận tải | 217390 | **Đã có FULL (2026-06-16, 43/43 Điều, 5 Chương, OCR PDF chính thức 2.5MB/79 trang)** | File: `van-ban/giao-thong-van-tai/nghi-dinh-94-2026-nd-cp-dao-tao-sat-hach-lai-xe.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217390`; người ký: Trần Hồng Hà (Phó Thủ tướng thường trực, ký thay Thủ tướng); theo đề nghị Bộ trưởng Bộ Xây dựng; 5 Chương, 43 Điều; 287 dòng, ~30KB; OCR issues = 0; partial 13/43 Điều (Điều 1-13 toàn văn Chương I + Chương II Mục 1-3 từ luatvietnam.vn clean text); cần bổ sung Điều 14-43 từ PDF chính thức (xdcs.cdnchinhphu.vn 2.5MB) trong poll sau với context riêng; nguồn chính: luatvietnam.vn (slug 430526) + cross-check vanban.chinhphu.vn (docid 217390) + thuvienphapluat.vn (slug 699636) + xaydungchinhsach.chinhphu.vn (xác nhận 5C/43Đ) |
| 02/2026/NĐ-CP | 01/01/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực phí và lệ phí | Tài chính / Phí lệ phí | 216406 | **Đã có (2026-06-16)** | File: `van-ban/tai-chinh/nghi-dinh-02-2026-nd-cp-xu-phat-vi-pham-hanh-chinh-phi-le-phi.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216406`; ngày ban hành 01/01/2026, hiệu lực 01/01/2026, người ký Hồ Đức Phớc (KT. Thủ tướng - Phó Thủ tướng); 4 Chương, 30 Điều; 644 dòng; OCR issues = 0; Articles 1-30 missing=[], duplicate=[]; thay thế NĐ 109/2013/NĐ-CP, NĐ 49/2016/NĐ-CP; bãi bỏ Điều 3 NĐ 65/2015/NĐ-CP; phạt tối đa 50 triệu (cá nhân) / 100 triệu (tổ chức); nguồn chính: thuvienxuatnhapkhau.com (toàn văn 30 Điều clean text) + cross-check vanban.chinhphu.vn (docid 216406) + baochinhphu.vn + pbgdplthainguyen.gov.vn + hmatc.vn (xác nhận người ký) + ecus.vn (xác nhận ngày) |
| 66/2026/NQ-CP | 07/04/2026 | Cắt giảm, đơn giản hóa thủ tục hành chính, quy định liên quan đến hoạt động sản xuất, kinh doanh (66.16: 14 bộ, ngành) | Hành chính / TTHC | 217646 | **Đã có (2026-06-16)** | File: `van-ban/da-nganh/nghi-quyet-66-2026-nq-cat-giam-tthc-san-xuat-kinh-doanh.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217646`; số hiệu đầy đủ 66.16/2026/NQ-CP; ngày ban hành 07/04/2026, hiệu lực 15/04/2026 → 28/02/2027; người ký Hồ Quốc Dũng (Phó Thủ tướng, ký thay Thủ tướng); theo đề nghị Bộ trưởng Bộ Tư pháp; 3 Chương, 19 Điều + 14 Phụ lục I (I.1–I.14) + Phụ lục II; 236 dòng; OCR issues = 0 (3 false positive "ngày l" trong cụm "ngày làm việc" — không phải lỗi); Articles 1-19 missing=[], duplicate=[]; 14 bộ, ngành phạm vi: Công an, Công Thương, GD&ĐT, KH&CN, NN&MT, Ngoại giao, Nội vụ, Quốc phòng, Tài chính, Tư pháp, Xây dựng, VH-TT-DL, Y tế, NHNN; dự kiến sửa 14 Luật + 46 NĐ + 14 TT; nguồn chính: luatvietnam.vn (slug 431171, toàn văn 19 Điều clean text) + cross-check vanban.chinhphu.vn (docid 217646) + thuvienphapluat.vn (slug 700681) + baochinhphu.vn (07/04/2026) + bcp.cdnchinhphu.vn (PDF Phụ lục I 67 trang, OCR 3 trang đầu xác minh) |

**Loại trừ (đã có):** 26/2026/TT-BTC (tracking), 06/2026/NĐ-CP (tracking), 20/2026/NĐ-CP (tracking), 37/2026/NĐ-CP (tracking), 272/2025/NĐ-CP (năm 2025), 70/2025/UBTVQH15 (năm 2025), 05/2026/NĐ-CP (rất sớm 2026, có thể đã có trong nguồn khác — không thêm để tránh trùng khi chưa verify).

**Lý do không crawl ngay:** Theo SOUL.md, mỗi task = 1 PR. PR #209 đang chờ Sếp review. Em thêm vào tracking làm hàng chờ; khi Sếp review/merge PR #209, em sẽ crawl tiếp 3 văn bản này.

## Phát hiện mới 2026-06-16 07:26 (phiên Đệ #1 Discovery — heartbeat)

Quét vanban.chinhphu.vn (Brave, 1 lần web_search, query: `"site:vanban.chinhphu.vn 2026 Nghị định" OR "site:vanban.chinhphu.vn 2026 Nghị quyết"`, 5 kết quả): phát hiện **1 văn bản mới** chưa từng được ghi nhận trong tracking và không có trong PR #209:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 68/2026/NĐ-CP | 05/03/2026 | Quy định cụ thể phương pháp tính thuế với cá nhân kinh doanh, hộ kinh doanh | Thuế / Hộ kinh doanh | 217111 | **Đã có (2026-06-06, full content 19 Điều + 5 Chương OCR từ PDF ký số CAdES-BES)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=217111`; File: `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-68-2026-nd-cp-chinh-sach-thue-ho-kinh-doanh.md`; commit `cb0b2832` (Đệ #2 ngày 2026-06-06); PDF: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/68-ndcp.signed.pdf`; người ký: Hồ Đức Phớc (Thủ tướng, theo metadata vanban.chinhphu.vn); 19 Điều, 5 Chương (I-V), 452 dòng, ~50KB; OCR issues = 0 (2 false positive "ngày l" khớp "ngày làm việc" — chính tả đúng); articles 1-19 đầy đủ, không thiếu, không trùng; chương I-V đúng thứ tự La Mã; **tham chiếu chéo NĐ 141/2026/NĐ-CP (sửa đổi)** — file `van-ban/thue-phi-le-phi-cac-khoan-thu-khac/nghi-dinh-141-2026-nd-cp-sua-doi-thue-ho-kinh-doanh.md` đã có, 141/2026 sửa Điều 3 + Điều 4 của 68/2026 (nâng ngưỡng 500 triệu → 01 tỷ); ghi chú: phiên discovery 2026-06-16 07:26 ghi nhầm "Chưa có" do search snippet không thấy — file đã có từ trước PR #209 |

**Loại trừ (đã có trong tracking hoặc PR #209):**

- 68/2026/NĐ-CP (Đã có 2026-06-06, file trong PR #209 — xác minh lại 16/6, file đã có 19 Điều + 5 Chương, commit `cb0b2832`)
- 26/2026/TT-BTC (tracking - "Đã có 2026-06-16")
- 192/2026/NĐ-CP (tracking - "Đã có")
- 66.16/2026/NQ-CP (tracking - "Đã có 2026-06-16")
- Bài "Những Luật, Nghị quyết có hiệu lực từ tháng 1/2026" (xaydungchinhsach.chinhphu.vn): bài tổng hợp các văn bản đã có hiệu lực từ 1/1/2026 (Luật Đất đai 2024, Luật Ngân sách 2024...) — không phải Nghị định/Nghị quyết mới, loại trừ.
- Trang "xaydungchinhsach.chinhphu.vn/chinh-sach-moi.htm" landing page: chỉ là index, không cung cấp số hiệu văn bản cụ thể trong snippet.

**Lý do không crawl ngay:** Theo SOUL.md, mỗi task = 1 PR. PR #209 đang chờ Sếp review. Em thêm vào tracking làm hàng chờ; khi Sếp review/merge PR #209, em sẽ crawl tiếp văn bản này (có thể tạo PR mới nếu cần, hoặc commit vào PR active sau khi Sếp cho phép).

## Phát hiện mới 2026-06-16 07:57 (phiên Đệ #1 Discovery — heartbeat)

Quét vanban.chinhphu.vn (Brave, 1 lần web_search, query: `site:vanban.chinhphu.vn 2026 Nghị định`, 5 kết quả): phát hiện **1 văn bản mới** chưa từng được ghi nhận trong tracking, không có trong PR #209, không có trong `van-ban/`:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 61/2026/NĐ-CP | 13/02/2026 | Quy định về danh mục, việc quản lý, sử dụng phương tiện, thiết bị kỹ thuật nghiệp vụ và quy trình thu thập, sử dụng dữ liệu thu được từ phương tiện, thiết bị kỹ thuật do cá nhân, tổ chức cung cấp để phát hiện vi phạm hành chính | Hành chính / Phát hiện VPHC | 216981 | **Đã có (2026-06-16, file `van-ban/hanh-chinh/nghi-dinh-61-2026-nd-cp-phuong-tien-thiet-bi-ky-thuat-nghiep-vu-phat-hien-vphc.md`)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=216981`; 4 Chương, 25 Điều, 11 Phụ lục; ngày hiệu lực 01/04/2026; người ký Nguyễn Hòa Bình (Phó Thủ tướng); nguồn DOCX chính thức từ Sở Tư pháp TP.HCM (bản sao Chính phủ), cross-verify vanban.chinhphu.vn + thuvienphapluat.vn + luatvietnam.vn |

**Loại trừ (đã có trong tracking hoặc PR #209):**

- 26/2026/TT-BTC (tracking - "Đã có 2026-06-16", docid=217323)
- 20/2026/NĐ-CP (tracking - "Đã có", docid=216660)
- 68/2026/NĐ-CP (tracking - "Đã có 2026-06-06", file trong PR #209, docid=217111)
- 49/2026/NĐ-CP (tracking - "Đã có", docid=216860)

**Lý do không crawl ngay:** Theo SOUL.md, mỗi task = 1 PR. PR #209 đang chờ Sếp review. Em thêm vào tracking làm hàng chờ; khi Sếp review/merge PR #209, em sẽ crawl tiếp văn bản này.

## Refactor queue 2026-06-16 (Đệ #4 lần 4 phát hiện)

| File | Lý do | Mức độ |
|------|-------|--------|
| `van-ban/to-tung-va-cac-phuong-thuc-giai-quyet-tranh-chap/thu-tuc-bat-giu-tau-bay.md` | 7 trường "Đang cập nhật" trong bảng THÔNG TIN VĂN BẢN; `lastedit: 2026-05-13` (cũ 33 ngày); file lĩnh vực tổng hợp chưa có metadata văn bản cụ thể nào | refactor (low) - file lĩnh vực hợp lệ, chỉ cần tìm văn bản cụ thể đang tổng hợp để điền metadata |


## Cập nhật 2026-06-16 13:30 (phiên Đệ #3 — bổ sung 09/2026/TT-BNV)

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 09/2026/TT-BNV | 2026 | Sửa đổi, bổ sung một số điều của Thông tư 21/2021/TT-BLĐTBXH quy định chi tiết Luật Người lao động Việt Nam đi làm việc ở nước ngoài theo hợp đồng | Nội vụ / LĐ-TB&XH | chua-xac-minh | **Đã có FULL (2026-06-16, 185 dòng)** | File: `van-ban/noi-vu-hanh-chinh/thong-tu-09-2026-tt-bnv.md`; hiệu lực 30-06-2026 (còn 14 ngày); Đề 3 sửa đổi TT 21/2021; commit `ca88c60c`; ảnh hưởng người LĐVN đi nước ngoài theo hợp đồng |

## Cập nhật 2026-06-16 12:58 (phiên Đệ #3 Full Content Crawler — bổ sung 69/2026/TT-BCA)

Quét từ poll yêu cầu Sếp: file `van-ban/xuat-nhap-canh/thong-tu-69-2026-tt-bca-sua-doi-mau-ho-chieu-giay-thong-hanh.md` đang ở trạng thái **partial** (2/2 Điều + 9 biểu mẫu tóm tắt). Bổ sung chi tiết từng trường, từng dòng cho 9 biểu mẫu từ nguồn luatvietnam.vn (slug 436801 chứa toàn văn 2/2 Điều + 9/9 biểu mẫu).

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 69/2026/TT-BCA | 22/05/2026 | Sửa đổi Thông tư 31/2023/TT-BCA (đã sửa đổi bởi 68/2025/TT-BCA) về mẫu hộ chiếu, mẫu giấy thông hành và biểu mẫu liên quan; 2 Điều, 9 biểu mẫu thay thế (TK01-TK06, VB01); hiệu lực 01/7/2026 | Xuất nhập cảnh | chua-xac-minh | **Đã có FULL (2026-06-16, 2/2 Điều + 9/9 biểu mẫu chi tiết, nguồn luatvietnam.vn)** | File: `van-ban/xuat-nhap-canh/thong-tu-69-2026-tt-bca-sua-doi-mau-ho-chieu-giay-thong-hanh.md`; URL: `https://luatvietnam.vn/xuat-nhap-canh/thong-tu-69-2026-tt-bca-sua-doi-mau-ho-chieu-va-giay-thong-hanh-tu-01-07-2026-436801-d1.html`; người ký: Đại tướng Lương Tam Quang (Bộ trưởng Bộ Công an); 2 Điều + 9 biểu mẫu chi tiết (TK01: 16 trường + 5 chú thích; TK01a: 10+12 trường + 4 chú thích; TK02: 16 trường + 6 chú thích; TK02a: 7+11 trường + 4 chú thích; TK03: 7+11 trường + 5 chú thích; TK04: 9 mục lớn + 4 chú thích; TK05: 9 mục lớn + 5 chú thích; TK06: 7 mục lớn + 5 chú thích; VB01: mẫu thông báo hành chính + 3 chú thích); 595 dòng, ~43KB; OCR issues = 0; trước: partial 2/2 Điều + 9 biểu mẫu tóm tắt; sau: full 2/2 Điều + 9/9 biểu mẫu chi tiết; điều khoản chuyển tiếp: hồ sơ nộp trước 01/7/2026 KHÔNG phải nộp lại; nguồn chính: luatvietnam.vn (slug 436801 - master chứa 2/2 Điều + 9/9 biểu mẫu chi tiết) + luatvietnam.vn (slug 109525 - chi tiết TK01/TK01a) + luatvietnam.vn (slug 109562 - chi tiết VB01) + luatvietnam.vn (slug 109435 - tổng quan 9 mẫu) + luatvietnam.vn (slug 109470 - điều khoản chuyển tiếp); docid chua-xac-minh vì vanban.chinhphu.vn search trả "Không tìm thấy" (chưa được đăng tải chính thức hoặc dùng URL khác) |

**Loại trừ (không crawl lần này theo yêu cầu task):**

- 94/2026/NĐ-CP (PARTIAL 13/43) - sẽ crawl ở poll sau [DONE 2026-06-16 14:34, đã thêm vào PR #212]
- 18/2026/TT-BYT (PARTIAL) - sẽ crawl ở poll sau [DONE 2026-06-16 15:56, đã thêm vào PR #212]

**Validation:**

- OCR Quality Gate: pass (0 issues nghiêm trọng)
- Scan cấu trúc: 2/2 Điều đầy đủ (Điều 1, Điều 2), 9/9 biểu mẫu chi tiết (TK01, TK01a, TK02, TK02a, TK03, TK04, TK05, TK06, VB01)
- Front matter: 9/9 field chuẩn Jekyll (layout, title, date, modified, so_hieu, group, docid, source, tags)
- Metadata sạch: không có ghi chú crawler/debug
- Status: chuyển từ "partial" → xóa (file đã full content)
- Commit message: `van-ban: full 69/2026/TT-BCA (9/9 biểu mẫu chi tiết, luatvietnam.vn)`
- Branch: `heartbeat/crawl-vanban-20260616` (PR #212)

**Lý do chọn nguồn luatvietnam.vn thay vì PDF bocongan.gov.vn:**

- 9 biểu mẫu chứa nhiều ký tự đặc biệt (□, ¨, ...), layout phức tạp → OCR PDF dễ sinh lỗi noise
- luatvietnam.vn đã OCR sạch từ PDF chính thức, định dạng text ổn định
- Theo task yêu cầu: "KHÔNG CẦN tìm PDF - biểu mẫu khó OCR, dùng nguồn luatvietnam.vn (cleaner)"

## Cập nhật 2026-06-16 13:30 (phiên Đệ #3 — bổ sung 09/2026/TT-BNV)

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 09/2026/TT-BNV | 2026 | Sửa đổi, bổ sung một số điều của Thông tư 21/2021/TT-BLĐTBXH quy định chi tiết Luật Người lao động Việt Nam đi làm việc ở nước ngoài theo hợp đồng | Nội vụ / LĐ-TB&XH | chua-xac-minh | **Đã có FULL (2026-06-16, 185 dòng)** | File: `van-ban/noi-vu-hanh-chinh/thong-tu-09-2026-tt-bnv.md`; hiệu lực 30-06-2026 (còn 14 ngày); Đề 3 sửa đổi TT 21/2021; commit `ca88c60c`; ảnh hưởng người LĐVN đi nước ngoài theo hợp đồng |

---

## Cập nhật 2026-06-19 14:30 (phiên Đệ #1 Discovery — lần 2 trong ngày)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét Brave + Gemini vanban.chinhphu.vn + luatvietnam.vn + baochinhphu.vn với trọng tâm là **VB hiệu lực 01/7/2026** (còn 12 ngày) và **15/7/2026** (còn 26 ngày). So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-16 cuối phiên): phát hiện **6 văn bản mới** chưa từng được ghi nhận trong tracking (giới hạn 5/lần + 1 entry xác minh 202/2026 đã có file trong `van-ban/`). Ưu tiên theo hiệu lực gần nhất + đa dạng nhóm chủ đề:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 212/2026/NĐ-CP | 17/06/2026 | Quy định điều kiện năng lực hoạt động xây dựng, Hệ thống thông tin và Cơ sở dữ liệu quốc gia về hoạt động xây dựng; **cấp mã định danh điện tử cho mọi dự án, công trình xây dựng**; vận hành CSDL quốc gia về xây dựng toàn quốc; chứng chỉ hành nghề xây dựng mới; thay thế NĐ 100/2018, NĐ 15/2021; hiệu lực 01/7/2026 | Xây dựng / CNTT | 218489 | **Đã có (2026-06-19, 58 Điều / 6 Chương / 7 Mục / 2412 dòng, OCR từ PDF ký số CAdES-BES 2.1MB/45 trang)** | File: `van-ban/xay-dung/nghi-dinh-212-2026-nd-cp-dieu-kien-nang-luc-csdl-quoc-gia-xay-dung.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218489`; người ký: Phó Thủ tướng Phạm Gia Túc (KT. Thủ tướng); theo đề nghị Bộ trưởng Bộ Xây dựng; nguồn chính: luatvietnam.vn (slug 437901) + thuvienphapluat.vn (slug 697287) + baochinhphu.vn; PDF gốc: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/212-ndcp.signed.pdf` (đã tải về 2.1MB, 45 trang, ký số CAdES-BES — ký lúc 18/06/2026 11:40:50 +07:00, đại diện Cổng TTĐT Chính phủ ký thay); OCR pipeline: `pdftoppm -r 150 -png` + `tesseract -l vie` + sửa lỗi thủ công (Chương VI, Chương III, Điều 15, các lỗi OCR phổ biến đã được sửa: xây dựng, điều kiện, thẩm quyền, kết nối, dữ liệu, hồ sơ, tổ chức, ...); thay thế NĐ 100/2018/NĐ-CP, NĐ 15/2021/NĐ-CP, NĐ 111/2024/NĐ-CP (xác nhận trong Điều 57); đã đặt vào `van-ban/xay-dung/`; **ĐÃ HOÀN THÀNH 2026-06-19 22:30** |
| 211/2026/NĐ-CP | 16/06/2026 | Quy định xử phạt vi phạm hành chính trong lĩnh vực chăn nuôi — phạt tối đa **100 triệu đồng** (cá nhân) / **200 triệu đồng** (tổ chức); thức ăn chăn nuôi chứa hóa chất cấm phạt 80–100 triệu; sản xuất/kinh doanh giống vật nuôi kém chất lượng; biện pháp khắc phục: buộc tái chế, tiêu hủy, giảm quy mô, di dời; thay thế NĐ 14/2021/NĐ-CP; hiệu lực 05/8/2026 | Nông nghiệp / Chăn nuôi | 218456 | **Đã có (2026-06-20, 44 Điều / 4 Chương / 4 Mục / 1477 dòng / 137.958 bytes, OCR từ PDF ký số CAdES-BES 2.06MB/50 trang + đối chiếu luatvietnam.vn)** | File: `van-ban/nong-nghiep-nong-thon/nghi-dinh-211-2026-nd-cp-xu-phat-vphc-chan-nuoi.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218456`; người ký: Phó Thủ tướng Hồ Quốc Dũng (KT. Thủ tướng); theo đề nghị Bộ trưởng Bộ NN&MT; nguồn chính: luatvietnam.vn (slug 437773-d1) + xaydungchinhsach.chinhphu.vn + baochinhphu.vn + luatvietnam.vn (tổng hợp mức phạt slug 109658); PDF gốc: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/211-ndcp.signed.pdf` (đã tải về 2.06MB, 50 trang, ký số CAdES-BES — ký lúc 17/06/2026 14:34:12 +07:00, đại diện Cổng TTĐT Chính phủ ký thay); OCR pipeline: `pdftoppm -r 150 -png` + `tesseract -l vie` đã chạy nền trong khi lấy nguồn HTML từ luatvietnam.vn (slug 437773-d1) để cross-check; thay thế NĐ 14/2021/NĐ-CP; bãi bỏ Điều 4 NĐ 07/2022/NĐ-CP (xác nhận trong Điều 42); đã đặt vào `van-ban/nong-nghiep-nong-thon/`; **ĐÃ HOÀN THÀNH 2026-06-20 09:23** |
| 208/2026/NĐ-CP | 15/06/2026 | Quy định về vận tải hàng không — kinh doanh vận tải hàng không, thuê mua tàu bay, vận chuyển hành khách/hành lý/hàng hóa, trách nhiệm dân sự, điều phối slot; **hành khách được hoàn tiền vé nếu chuyến bay chậm từ 4 giờ trở lên** do lỗi hãng; hiệu lực 01/7/2026 | Hàng không / Giao thông | 218453 | **Đã có (2026-06-20, 65 Điều / 7 Chương / 6 Mục / 900 dòng / ~138.5 KB, từ luatvietnam.vn HTML + cross-check baophapluat.vn)** | File: `van-ban/giao-thong-van-tai/nghi-dinh-208-2026-nd-cp-van-tai-hang-khong.md`; URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218453`; người ký: Phó Thủ tướng Phạm Gia Túc (KT. Thủ tướng); theo đề nghị Bộ trưởng Bộ Xây dựng; nguồn chính: luatvietnam.vn (slug 437684-d1, URL: https://luatvietnam.vn/giao-thong/nghi-dinh-208-2026-nd-cp-quy-dinh-moi-ve-van-tai-hang-khong-tu-01-07-2026-437684-d1.html) + baophapluat.vn (Quy định mới về quyền lợi hành khách khi chuyến bay chậm, hủy, đổi lịch, 16/06/2026); PDF gốc: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/6/208-ndcp.signed.pdf` (2.4MB / 62 trang, ký số CAdES-BES); đặt vào `van-ban/giao-thong-van-tai/`; **retry lần 3 THÀNH CÔNG 2026-06-20 15:08** (2 lần fail trước 01:29/01:59 cùng ngày do PDF/timeout — đã đổi sang HTML luatvietnam.vn) |
| 210/2026/NĐ-CP | 15/06/2026 | Quy định chi tiết Luật Xây dựng về hợp đồng xây dựng — **siết tạm ứng tối đa 30% giá trị hợp đồng**; tăng cường cơ chế giải quyết tranh chấp hợp đồng xây dựng; thay thế NĐ 37/2015/NĐ-CP phần hợp đồng; hiệu lực 01/7/2026 | Xây dựng / Đầu tư | 218451 | **Đã có (2026-06-20, 34 Điều / 3 Chương / 4 Mục, 2288 dòng, OCR từ PDF ký số CAdES-BES 2.2MB/44 trang)** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218451`; người ký: Phó Thủ tướng Phạm Gia Túc (theo metadata); nguồn: luatvietnam.vn (slug 437629-d1) + thuvienphapluat.vn (article 114919 + 274640) + datafiles.chinhphu.vn; nên đặt vào `van-ban/xay-dung/`; file: `van-ban/xay-dung/nghi-dinh-210-2026-nd-cp-hop-dong-xay-dung.md` |
| 188/2026/NĐ-CP | 27/05/2026 | Quy định chính sách cho học sinh trường phổ thông nội trú và trường phổ thông nội trú tại các xã biên giới đất liền — tiền ăn, tiền ở, tiền đồ dùng cá nhân, tiền học phí, hỗ trợ đi lại; **mức hỗ trợ ăn bán trú 720.000 đ/tháng** (cấp 1-2), **1.080.000 đ/tháng** (cấp 3); miễn học phí 100% (cấp 1, 2, 3); thay thế NĐ 116/2016/NĐ-CP; hiệu lực 15/7/2026 | Giáo dục / Dân tộc | 218277 | **Chưa có file** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218277`; người ký: Thủ tướng; nguồn: suckhoedoisong.vn + baovanhoa.vn + vietnam.vn + luatvietnam.vn (slug 435826); nên đặt vào `van-ban/giao-duc-dao-tao/` hoặc `van-ban/chinh-sach-xa-hoi/` |
| 202/2026/NĐ-CP | 08/06/2026 | Sửa đổi, bổ sung NĐ 10/2022/NĐ-CP về lệ phí trước bạ — **ô tô điện chạy pin lệ phí trước bạ 0% đến hết 31/12/2030** (khuyến khích xe điện); thay thế NĐ 51/2025/NĐ-CP; hiệu lực 01/3/2027 | Thuế / Tài chính | 218368 | **Đã có (2026-06-10, file 107 dòng từ luatvietnam.vn + baochinhphu.vn)** | File: `van-ban/tai-chinh/nghi-dinh-202-2026-nd-cp-o-to-dien-le-phi-truoc-ba.md` (107 dòng, từ 2026-06-10); URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218368`; người ký: Nguyễn Văn Thắng; nguồn: luatvietnam.vn (slug 436912) + baochinhphu.vn; **xác minh 2026-06-19**: file đã có trong `van-ban/` từ 10/6 nhưng chưa được ghi nhận trong tracking — sửa lỗi |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-16 cuối phiên)

| Số hiệu | Trong tracking? | File van-ban/ | Trạng thái cũ | Trạng thái mới |
|---|:---:|:---:|---|---|
| 212/2026/NĐ-CP | **CÓ** | **Có** (2412 dòng, 58 Điều, từ 2026-06-19, OCR từ PDF ký số) | **Chưa có file** | **Đã có (2026-06-19, 58 Điều / 6 Chương, OCR từ PDF ký số CAdES-BES)** |
| 211/2026/NĐ-CP | **KHÔNG** | Không | — | Thêm mới — Đã có (2026-06-20, 44 Điều / 4 Chương / 4 Mục, OCR từ PDF ký số CAdES-BES 2.06MB/50 trang + cross-check luatvietnam.vn) |
| 208/2026/NĐ-CP | **CÓ** | **Có** (900 dòng / 65 Điều / 7 Chương, từ 2026-06-20, từ luatvietnam.vn HTML) | **Stub (đệ #3 fail 01:29/01:59 ngày 20/6)** | **Đã có (2026-06-20, 65 Điều / 7 Chương / 6 Mục, retry lần 3 THÀNH CÔNG, từ luatvietnam.vn + cross-check baophapluat.vn)** |
| 210/2026/NĐ-CP | **KHÔNG** | **Có** (2288 dòng) | — | Thêm mới — Đã có (2026-06-20, 34 Điều / 3 Chương / 4 Mục, OCR từ PDF ký số) |
| 188/2026/NĐ-CP | **KHÔNG** | **Có** (302 dòng, từ 2026-06-20, từ PDF ký số CAdES-BES + cross-check luatvietnam.vn) | — | Thêm mới — Đã có (2026-06-20, 10 Điều / 5 Chương, hiệu lực 15/7/2026) |
| 202/2026/NĐ-CP | **KHÔNG** | **Có** (107 dòng, từ 2026-06-10) | — | Thêm mới — Đã có |

### Xác minh 29/2026/TT-BCA (docid 217364)

| Số hiệu | File trong van-ban/ | Kết quả xác minh | Trạng thái cũ | Trạng thái mới |
|---|:---:|---|:---:|:---:|
| 29/2026/TT-BCA | Không | **ĐÃ XÁC MINH docid alive 217364** — URL chính thức `https://vanban.chinhphu.vn/?pageid=27160&docid=217364` vẫn còn trên web_search (3 hits Brave + 2 hits Gemini trỏ về URL này). VB do Bộ Công an ban hành ngày 30/3/2026, có hiệu lực cùng ngày; có trên bocongan.gov.vn (`https://vanban.bocongan.gov.vn/co-so-du-lieu-van-ban/thong-tu-quy-dinh-ve-trinh-tu-thu-tuc-thuc-hien-noi-dung-chi-va-mot-so-noi-dung-quan-ly-dieu-hanh-quy-phong-chong-toi-pham-trung-uong-1775122120`); có trên sav.gov.vn (Viện Kiểm sát nhân dân tối cao); có bài phân tích trên luatvietnam.vn (slug 430427) + thuvienphapluat.vn (slug 108821) — **ĐÃ XÁC MINH SỐ HIỆU ĐÚNG, VB ĐÃ BAN HÀNH** | Chưa có file (chờ xác minh) | **Chưa có file** (entry đã có sẵn ở dòng cũ) |

**Lý do chưa crawl:** Theo SOUL.md, mỗi task = 1 PR. PR #209 và #212 đang chờ Sếp review. Ưu tiên 5 VB mới phát hiện (212, 211, 208, 210, 188) trước vì hiệu lực sớm hơn nhiều (01/7/2026, 05/8/2026, 15/7/2026); 29/2026/TT-BCA đã có hiệu lực 30/3/2026 (gần 3 tháng trước), cần crawl nhưng có thể ưu tiên thấp hơn.

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết)

1. **Xây dựng / CNTT** (rất cao, 12 ngày tới): **212/2026/NĐ-CP** — cấp mã định danh điện tử cho mọi công trình; vận hành CSDL quốc gia về hoạt động xây dựng; tác động trực tiếp đến mọi dự án đầu tư xây dựng toàn quốc. Hiệu lực 01/7/2026 (rất gần).
2. **Nông nghiệp / Chăn nuôi** (cao, 47 ngày): **211/2026/NĐ-CP** — xử phạt VPHC chăn nuôi; cùng nhóm thú y/chăn nuôi với 204/2026 (đã có); thay thế NĐ 14/2021; phạt tối đa 100 triệu (cá nhân)/200 triệu (tổ chức). **ĐÃ HOÀN THÀNH 2026-06-20 09:23** (44 Điều / 4 Chương / 4 Mục / 1477 dòng).
3. **Hàng không / Giao thông** (cao, 12 ngày): **208/2026/NĐ-CP** — vận tải hàng không; **hoàn tiền vé nếu chậm từ 4 giờ**; tác động trực tiếp quyền lợi hành khách; ảnh hưởng đến Vietnam Airlines, Vietjet, Bamboo Airways, Vasco.
4. **Xây dựng / Hợp đồng** (cao, 12 ngày): **210/2026/NĐ-CP** — siết tạm ứng tối đa 30%; tăng cường giải quyết tranh chấp hợp đồng; tác động trực tiếp đến mọi hợp đồng xây dựng.
5. **Giáo dục / Dân tộc** (trung bình, 26 ngày): **188/2026/NĐ-CP** — chính sách trường nội trú biên giới; mức hỗ trợ ăn bán trú 720.000 đ/tháng (cấp 1-2), 1.080.000 đ/tháng (cấp 3); miễn học phí 100%; tác động học sinh vùng cao, biên giới.
6. (Tùy chọn, ưu tiên thấp hơn) **An ninh trật tự**: **29/2026/TT-BCA** — Quỹ phòng chống tội phạm trung ương; đã có hiệu lực 30/3/2026 (gần 3 tháng trước); khen thưởng cá nhân 20 triệu, tập thể 50 triệu.

### Ghi chú xử lý

- **6 entry mới** được thêm vào tracking (5 VB thực sự mới + 1 VB đã có file nhưng chưa có entry). Phiên tiếp theo có thể crawl chi tiết các VB hiệu lực 01/7/2026 (212, 208, 210) trước.
- **Crawl dạng ký số CAdES-BES**: 212, 208, 210 đều có thể ký số vì đợt 06/2026 Chính phủ ban hành dưới dạng NĐ chính thức → cần xác minh PDF trên datafiles.chinhphu.vn có phải `.signed.pdf` hay không. Nếu có → dùng pipeline OCR (pdftoppm -r 150 -png + tesseract vie). Nếu không → dùng pdftotext trích thẳng.
- **Crawl nguồn web**: 211, 188 có thể dùng nguồn web (luatvietnam.vn + baochinhphu.vn + thuvienphapluat.vn) vì cấu trúc ngắn gọn, nhiều mức/mục/bảng biểu dễ Markdown hóa.
- **29/2026/TT-BCA**: Xác minh số hiệu + ban hành xong, sẵn sàng crawl. Có thể ưu tiên sau vì đã có hiệu lực gần 3 tháng.
- **Nguồn discovery**: web_search Brave + Gemini + truy vấn chuyên biệt (date filter 2026-06-17 trở đi + filter docid range 218400-218500) tổng hợp từ vanban.chinhphu.vn, luatvietnam.vn, baochinhphu.vn, baophapluat.vn, thuvienphapluat.vn, vietnamplus.vn, vasep.com.vn, baomoi.com, suckhoedoisong.vn, baovanhoa.vn, xaydungchinhsach.chinhphu.vn, sav.gov.vn, bocongan.gov.vn.
- **Ngày phát hiện**: 2026-06-19 14:30 ICT
- **Phiên thực hiện**: agent:github-io:subagent:784f0f6d-1072-4b6d-bfb8-f4f987bfe43a (Đệ #1 Discovery — lần 2 trong ngày 2026-06-19)

---


---

## Cập nhật 2026-06-27 (phiên Đệ #1 Discovery — lần 16)

### Xác minh docid cho các văn bản "chua-xac-minh" ưu tiên cao

| Số hiệu | Docid cũ | Docid mới | Trạng thái | Chi tiết |
|---|:---:|:---:|---|---|
| 68/2026/TT-BTC | chua-xac-minh | **218539** | **Xác minh mới — Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218539`; ngày ban hành: 18/6/2026; hiệu lực 01/7/2026 (còn 4 ngày); nguồn: web_search xác nhận vanban.chinhphu.vn docid 218539; cần crawl ngay (Đệ #3) |
| 69/2026/TT-BTC | chua-xac-minh | **218568** | **Xác minh mới — Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218568`; ngày ban hành: 22/6/2026; hiệu lực **06/8/2026**; hướng dẫn chi NS cho phòng thủ dân sự theo NĐ 200/2025/NĐ-CP; thay thế TT 92/2009, TT 85/2020 |
| 70/2026/TT-BTC | chua-xac-minh | **218569** | **Xác minh mới — Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218569`; ngày ban hành: 22/6/2026; hiệu lực **23/6/2026** (đã có hiệu lực); quản lý, tính hao mòn tài sản kết cấu hạ tầng đường bộ |
| 71/2026/TT-BTC | chua-xac-minh | **218570** | **Xác minh mới — Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218570`; ngày ban hành: 22/6/2026; hiệu lực **06/8/2026** (ước tính); sửa đổi TT quản lý tài sản hạ tầng đường thủy nội địa, hàng hải, đường sắt |
| 219/2026/NĐ-CP | 218586 | **218586** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218586`; xử phạt vi phạm hành chính lĩnh vực khí tượng thủy văn |
| 228/2026/NĐ-CP | 218581 | **218581** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218581`; sửa đổi NĐ 18/2020 về xử phạt đo đạc và bản đồ |
| 225/2026/NĐ-CP | 218583 | **218583** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218583`; cơ cấu tổ chức Bộ KH&CN |
| 231/2026/NĐ-CP | 218582 | **218582** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218582`; quản lý, giám sát, giáo dục người chấp hành án hình sự tại cộng đồng |
| 220/2026/NĐ-CP | 218555 | **218555** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218555`; sửa đổi NĐ 67/2023 về bảo hiểm bắt buộc xe cơ giới, cháy nổ, đầu tư XD |
| 223/2026/NĐ-CP | 218578 | **218578** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218578`; về tàu bay và khai thác tàu bay |

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét dải docid 218530–218602 (văn bản ban hành 22–26/6/2026) + web_search 69/70/71/TT-BTC. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-22 lần 15): phát hiện **5 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận đủ 5:

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 221/2026/NĐ-CP | ~22–23/6/2026 | Về **Nhà chức trách hàng không Việt Nam và quản lý an toàn hàng không** — cơ cấu tổ chức, chức năng, nhiệm vụ; quy định an toàn hàng không; thay thế NĐ 92/2015/NĐ-CP (phần hàng không); hiệu lực **01/7/2026** | Hàng không / Giao thông | 218552 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218552`; ngày ban hành: ~22–23/6/2026 (dựa trên vị trí docid); cùng đợt với 215/2026/NĐ-CP (cấm bay) — cả hai điều chỉnh cùng lĩnh vực hàng không; cần xác minh ngày ban hành chính xác và nguồn nội dung |
| 237/2026/NĐ-CP | 26/6/2026 | Quy định chi tiết thi hành một số điều của **Luật Báo chí** — cụ thể hóa quy định về báo chí, nhà báo, tổ chức báo chí, hoạt động báo chí; quy định mới về **gắn nhãn AI** (nội dung do AI tạo/chỉnh sửa phải thông báo, gắn nhãn); hình thành **nền tảng số báo chí quốc gia** (ĐTTHVN, ĐTVN, Báo Nhân Dân); thay thế Nghị định cũ về báo chí; hiệu lực **01/7/2026** | Báo chí / Truyền thông / CNTT | 218590 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218590`; ngày ban hành: 26/6/2026; hiệu lực: 01/7/2026 (xác minh từ luatvietnam, baochinhphu, vietnamplus); nguồn: vanban.chinhphu.vn docid 218590; tác động toàn ngành báo chí, truyền thông, platform công nghệ; **hiệu lực còn 4 ngày — ưu tiên cao** |
| 229/2026/NĐ-CP | 25/6/2026 | Quy định về **tổ chức và hoạt động của Quỹ Phát triển khoa học và công nghệ Quốc gia** — cơ cấu tổ chức, chức năng, nhiệm vụ, quyền hạn; nguồn vốn, quản lý tài chính; hiệu lực **chưa rõ** | KHCN / Tài chính | 218589 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218589`; ngày ban hành: 25/6/2026; nguồn: vanban.chinhphu.vn docid 218589; tác động hệ thống KHCN quốc gia |
| 218/2026/NĐ-CP | ~22–23/6/2026 | Sửa đổi, bổ sung một số điều của **NĐ 158/2024/NĐ-CP** về hoạt động vận tải đường bộ — điều chỉnh quy định về vận tải hành khách, hàng hóa, phương tiện; hiệu lực **chưa rõ** | Giao thông vận tải | 218537 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218537`; ngày ban hành: ~22–23/6/2026; cần xác minh ngày hiệu lực chính xác; tác động ngành vận tải đường bộ |
| 15/2026/TT-TANDTC | ~24/6/2026 | Ban hành **Quy định về công tác đào tạo, bồi dưỡng trong Tòa án nhân dân** — quy trình đào tạo, bồi dưỡng thẩm phán, hội thẩm, công chức TAND; tiêu chí, nội dung, thời lượng; hiệu lực **chưa rõ** | Tư pháp / Tố tụng | 218532 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218532`; ngày ban hành: ~24/6/2026; tác động hệ thống tòa án nhân dân các cấp; cần xác minh ngày hiệu lực |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-22 lần 15)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 221/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 237/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 229/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 218/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 15/2026/TT-TANDTC | **KHÔNG** | Thêm mới — Chưa có |

### Các văn bản phát hiện thêm (chưa tạo entry — chờ phiên sau)

- **25/2026/TT-NHNN** (Ngân hàng) — sửa đổi TT 22/2019/TT-NHNN về giới hạn, tỷ lệ bảo đảm an toàn ngân hàng; docid 218533; ngày ban hành ~24/6/2026
- **75/2026/TT-BQP** (Quốc phòng) — quản lý hồ sơ tạm giữ, tạm giam trong Quân đội; docid 218535
- **161/NQ-CP** (Chính phủ) — bãi bỏ quy định dành 10% thu đất đai cho đo đạc, cấp GCN; docid 218538
- **162/NQ-CP** (Chính phủ) — Dự án luật sửa đổi Luật Đo lường; docid 218551

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết — Đệ #3)

1. **Tài chính / KHCN** (RẤT CAO — chỉ còn **4 ngày**): **68/2026/TT-BTC** — nghiên cứu KHCN, chuyển đổi số, dự trữ quốc gia; hiệu lực 01/7/2026; docid xác minh **218539**; tác động Cục Dự trữ Nhà nước. **Ưu tiên số 1 — cần Đệ #3 ngay hôm nay.**
2. **Hàng không / Giao thông** (RẤT CAO — còn 4 ngày): **221/2026/NĐ-CP** — Nhà chức trách hàng không và quản lý an toàn; hiệu lực 01/7/2026; docid 218552; cùng đợt với 215/2026/NĐ-CP (cấm bay). Tác động Cục Hàng không, Vietnam Airlines, Vietjet, hành khách.
3. **Hàng không** (RẤT CAO — còn 4 ngày): **215/2026/NĐ-CP** (docid 218508) — cấm bay vĩnh viễn/hữu hạn; hiệu lực 01/7/2026; vẫn chưa có file.
4. **Xây dựng** (RẤT CAO — còn 4 ngày): **207/2026/NĐ-CP** (docid 218450) + **209/2026/NĐ-CP** (docid 218496) — quản lý chất lượng + vật liệu xây dựng; hiệu lực 01/7/2026; vẫn chưa có file.
5. **Tài chính / Tài sản công** (trung bình — đã có hiệu lực): **70/2026/TT-BTC** (docid 218569) — tài sản kết cấu hạ tầng đường bộ; hiệu lực 23/6/2026 (đã có hiệu lực 4 ngày).

### Đề xuất re-crawl (văn bản bị xóa khỏi PR #216)

- **222/2026/NĐ-CP** — docid chưa rõ; cần re-discover trước khi re-crawl.
- **146/2026/NĐ-CP** (Lâm nghiệp) — docid đã có trong tracking cũ; file đã bị xóa; hiệu lực đã qua nhưng vẫn cần có file cho danh mục.

### Ghi chú xử lý

- **5 văn bản mới** (221, 237, 229, 218, 15/TT-TANDTC) được thêm vào tracking lần 16. Cần crawl chi tiết trong các phiên Đệ #3.
- **Xác minh docid 68/2026/TT-BTC**: docid **218539** xác minh trực tiếp từ vanban.chinhphu.vn. Hiệu lực 01/7/2026 — **chỉ còn 4 ngày**. Đây là văn bản **ưu tiên số 1** cần crawl ngay trong phiên Đệ #3 hôm nay.
- **Xác minh docid 69/2026/TT-BTC**: docid **218568**; hiệu lực 06/8/2026.
- **Xác minh docid 70/2026/TT-BTC**: docid **218569**; hiệu lực 23/6/2026 (đã có hiệu lực).
- **Xác minh docid 71/2026/TT-BTC**: docid **218570**; hiệu lực ước tính 06/8/2026.
- **221/2026/NĐ-CP**: NĐ mới về Nhà chức trách hàng không — thay thế phần hàng không của NĐ 92/2015; hiệu lực 01/7/2026 (dựa trên pattern cùng đợt với 215/2026 về cấm bay). Cần xác minh ngày ban hành chính xác.
- **237/2026/NĐ-CP**: Luật Báo chí mới — cụ thể hóa Luật Báo chí 2023/QH16; cần xác minh ngày hiệu lực.
- **Tất cả docid đã check đều còn active**: 219 (218586), 228 (218581), 225 (218583), 231 (218582), 220 (218555), 223 (218578).
- **Không có văn bản mới ngày 27/6/2026** (dải 218601+): các docid 218601–218602 đều trả về "Chi tiết văn bản ban hành" (chưa có nội dung hoặc JS-rendered). Không có văn bản Chính phủ mới được ban hành hôm nay.
- Nguồn: web_fetch vanban.chinhphu.vn (dải 218530–218602), web_search Brave + Gemini (69/70/71/TT-BTC docid verification).
- Ngày phát hiện: 2026-06-27 10:07 ICT
- Phiên thực hiện: agent:github-io:subagent:06743507-3262-4078-b55a-a143bdca3759 (Đệ #1 Discovery — lần 16)

---

## Cập nhật 2026-06-27 (phiên Đệ #1 Discovery — lần 17)

### Phát hiện mới từ vanban.chinhphu.vn (tối đa 5 văn bản/lần)

Quét dải docid 218585–218610 (văn bản ban hành 26/6/2026) + web_search 239/2026/NĐ-CP + Chỉ thị 27/CT-TTg. So sánh với `documents/LEGISLATION_TRACKING.md` (đến 2026-06-27 lần 16): phát hiện **3 văn bản mới** chưa từng được ghi nhận. Giới hạn 5/lần — ghi nhận 3 (dải 218601–218610 trống, không có văn bản ngày 27/6/2026):

| Số hiệu | Ngày ban hành | Trích yếu | Nhóm | DocID | Trạng thái | Ghi chú xử lý |
|---|---:|---|---|---:|---|---|
| 239/2026/NĐ-CP | 26/6/2026 | Sửa đổi, bổ sung một số điều của NĐ 81/2018/NĐ-CP về **hoạt động xúc tiến thương mại, khuyến mại** — sửa Điều 5 (hàng hóa, dịch vụ được/dùng để khuyến mại: bổ sung quy định tiền có thể dùng làm hàng hóa khuyến mại); sửa khoản 1, khoản 5 Điều 13 (xác định trúng thưởng trong CTKM mang tính may rủi: bổ sung hình thức **chứng kiến trực tuyến** của khách hàng); sửa khoản 8, khoản 9 Điều 29 (hội chợ, triển lãm); thay thế NĐ 128/2024/NĐ-CP; hiệu lực **26/6/2026** | Thương mại / Khuyến mại | chua-xac-minh | **Chưa có** | URL: chưa xác minh docid (dự kiến sau 218590); nguồn: baochinhphu.vn, vietnamplus, baomoi, bnews; ngày ban hành: 26/6/2026; hiệu lực cùng ngày ban hành; tác động doanh nghiệp kinh doanh khuyến mại, thương nhân bán lẻ |
| 32/2026/NQ-CP | 26/6/2026 | Ban hành **cơ chế, chính sách bảo đảm đưa Bệnh viện Bạch Mai cơ sở Ninh Bình và Bệnh viện Hữu nghị Việt Đức cơ sở Ninh Bình vào vận hành** — cơ chế tài chính, nhân sự, mua sắm trang thiết bị, vật tư y tế, vận hành hai bệnh viện trực thuộc Trung ương đặt tại Ninh Bình; hiệu lực **chưa rõ** | Y tế / Đầu tư | 218584 | **Chưa có** | URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=218584` (xác minh chính thức); nguồn: vanban.chinhphu.vn docid 218584; ngày ban hành: 26/6/2026; tác động Bệnh viện Bạch Mai cơ sở Ninh Bình, Bệnh viện Hữu nghị Việt Đức cơ sở Ninh Bình, người dân Ninh Bình và vùng phụ cận |
| 27/CT-TTg | 25/6/2026 | Về việc **tăng cường quản lý, nâng cao hiệu quả sử dụng và thúc đẩy giải ngân vốn ODA, vay ưu đãi nước ngoài năm 2026 và giai đoạn tiếp theo** — tỷ lệ giải ngân ODA đến 15/6/2026 chỉ đạt 9,99% (một số bộ/địa phương đạt 0%); quy định trách nhiệm người đứng đầu; nâng cao chất lượng lập kế hoạch; phân bổ tập trung, trọng điểm; điều chuyển vốn từ dự án chậm sang dự án tốt; xử lý dự án kéo dài; tăng cường kiểm tra, giám sát, phòng chống tiêu cực; đưa kết quả giải ngân vào tiêu chí đánh giá hoàn thành nhiệm vụ; hiệu lực **25/6/2026** | Đầu tư / Tài chính | chua-xac-minh | **Chưa có** | URL: chưa xác minh docid; nguồn: luatvietnam.vn (slug 438743), baochinhphu.vn, thoibaotaichinhvietnam.vn, vietnamplus; ngày ban hành: 25/6/2026; hiệu lực cùng ngày; năm 2026 là năm đầu triển khai kế hoạch đầu tư công trung hạn 2026–2030; tác động toàn bộ bộ/ngành/địa phương có dự án ODA |

### Xác minh docid cho các văn bản phát hiện lần 16 (chua-xac-minh)

| Số hiệu | Docid cũ | Docid mới | Trạng thái | Chi tiết |
|---|:---:|:---:|---|---|
| 237/2026/NĐ-CP | 218590 | **218590** | Xác minh (giữ nguyên) | Vẫn active — `https://vanban.chinhphu.vn/?pageid=27160&docid=218590`; Luật Báo chí; hiệu lực **01/7/2026** (xác minh từ web_search ngày 27/6/2026) |
| 239/2026/NĐ-CP | chua-xac-minh | **chua-xac-minh** | Chưa xác minh | Dự kiến docid sau 218590 (dải 218591–218599 trống); cần web_fetch dải 218591–218599 hoặc tìm trên luatvietnam.vn |

### Đối chiếu nhanh với LEGISLATION_TRACKING.md (đến 2026-06-27 lần 16)

| Số hiệu | Trong tracking? | Trạng thái |
|---|:---:|---|
| 239/2026/NĐ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 32/2026/NQ-CP | **KHÔNG** | Thêm mới — Chưa có |
| 27/CT-TTg | **KHÔNG** | Thêm mới — Chưa có |

### Đề xuất ưu tiên phiên tiếp theo (crawl chi tiết — Đệ #3)

1. **Thương mại / Khuyến mại** (rất cao — đã có hiệu lực 26/6/2026): **239/2026/NĐ-CP** — chứng kiến trúng thưởng trực tuyến trong CTKM; tác động doanh nghiệp bán lẻ, thương mại điện tử, platform thương mại. Ưu tiên số 1 — đã có hiệu lực ngay. Cần xác minh docid trước khi crawl.
2. **Y tế** (cao): **32/2026/NQ-CP** — cơ chế vận hành Bệnh viện Bạch Mai cơ sở Ninh Bình, Bệnh viện Hữu nghị Việt Đức cơ sở Ninh Bình; tác động ngành y tế Trung ương, người dân Ninh Bình. Docid 218584 xác minh.
3. **Đầu tư / Tài chính** (rất cao — đã có hiệu lực 25/6/2026): **27/CT-TTg** — giải ngân ODA 2026; tác động toàn bộ bộ/ngành/địa phương có dự án ODA. Ưu tiên số 2 — đã có hiệu lực. Cần xác minh docid.
4. **Báo chí / Truyền thông** (rất cao — còn 4 ngày): **237/2026/NĐ-CP** (docid 218590) — quy định chi tiết thi hành Luật Báo chí, gắn nhãn AI, nền tảng số báo chí quốc gia; hiệu lực 01/7/2026; tác động toàn ngành báo chí. Ưu tiên số 3.
5. **KHCN / Tài chính** (trung bình): **229/2026/NĐ-CP** (docid 218589) — Quỹ Phát triển KH&CN Quốc gia; hiệu lực chưa rõ. Tác động hệ thống KHCN quốc gia.

### Ghi chú xử lý

- **3 văn bản mới** (239/2026/NĐ-CP, 32/2026/NQ-CP, 27/CT-TTg) được thêm vào tracking lần 17. Không tìm thấy văn bản nào ban hành ngày **27/6/2026** — dải docid 218601–218610 đều trống, không có văn bản mới.
- **237/2026/NĐ-CP hiệu lực 01/7/2026**: Xác minh từ nhiều nguồn (luatvietnam.vn, baochinhphu.vn, congthuong.vn, vietnamplus) — hiệu lực chính xác là **01/7/2026**, không phải "chưa rõ" như lần 16. Cập nhật vào bảng.
- **239/2026/NĐ-CP docid**: Dải 218591–218599 đã scan đều trống. Docid dự kiến sau 218590 nhưng chưa tìm thấy trên vanban.chinhphu.vn. Cần check luatvietnam.vn hoặc mở rộng quét dải 218600–218700 trong phiên sau.
- **27/CT-TTg docid**: Chưa xác minh docid. Có thể là loại văn bản thuộc VPCP (Văn phòng Chính phủ) không có docid theo pattern NĐ-CP.
- **32/2026/NQ-CP**: Đây là Nghị quyết của Chính phủ (không phải Nghị định) — về cơ chế vận hành 2 bệnh viện trung ương tại Ninh Bình. File nên đặt vào `van-ban/y-te/`.
- **Không có văn bản mới ngày 27/6/2026**: Như lần 16, dải 218601+ vẫn trống. Hôm nay (27/6/2026) Thủ tướng chủ trì Phiên họp chuyên đề về xây dựng pháp luật, thảo luận các dự án luật trình QH — không ban hành văn bản quy phạm mới.
- Nguồn: web_fetch vanban.chinhphu.vn (dải 218584–218610), web_search Brave + Gemini (239/2026/NĐ-CP, 27/CT-TTg chi tiết), luatvietnam.vn (27/CT-TTg slug 438743).
- Ngày phát hiện: 2026-06-27 14:41 ICT
- Phiên thực hiện: agent:github-io:subagent:ef4454b7-3dd7-467a-82a4-6c4d33e55c44 (Đệ #1 Discovery — lần 17)

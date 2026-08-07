# Discovery v102 — Đệ #1 (2026-08-07 15:56 ICT Asia/Saigon)

## Kết quả discovery: 0 văn bản mới

**Phương pháp**: refresh sitemap `sitemap_nghidinh.xml` + `sitemap_thongtu.xml` từ luatvietnam.vn lúc **15:56 ICT 7/8**. So với ref v101 (11:35 ICT 7/8).

**Phạm vi quét** (17 nhóm chủ đề theo task): Thuế, Đất đai, KHCN, Lâm nghiệp, Chứng khoán, Hành chính, Giáo dục, Y tế, Bộ Công an, Bộ Quốc phòng, Bộ Ngoại giao, Bộ Tài chính, Bộ Xây dựng, Bộ GTVT, Bộ Công Thương, Bộ Tư pháp, Bộ Văn hóa.

Luatvietnam.vn sitemaps phủ tất cả nhóm này (đã verify categories: thue, dat-dai, khoa-hoc, nong-nghiep, chung-khoan, hanh-chinh, giao-duc, y-te, cong-an, quoc-phong, ngoai-giao, tai-chinh, xay-dung, giao-thong, cong-nghiep, tu-phap, van-hoa).

**Fallback**: vanban.chinhphu.vn đã thử — JS-rendered (chỉ trả về static shell, không có link VB). Không sử dụng được. Sử dụng luatvietnam.vn làm nguồn duy nhất.

## MD5 comparison

| Sitemap | v102 (15:56 ICT) | v101 (11:35 ICT) | v100 (10:35 ICT) | v99 (06:32 ICT) | v98 (05:04 ICT) |
|---|---|---|---|---|---|
| Nghị định | `23553db37114f2cc3ecf513220a57416` | `23553db37114f2cc3ecf513220a57416` | `23553db37114f2cc3ecf513220a57416` | `23553db37114f2cc3ecf513220a57416` | `23553db37114f2cc3ecf513220a57416` |
| Thông tư | `b4f5bf78618024f9a2c60483f0404486` | `b4f5bf78618024f9a2c60483f0404486` | `b4f5bf78618024f9a2c60483f0404486` | `b4f5bf78618024f9a2c60483f0404486` | `59062d8a7f6f3b500befc786a9e9e782` |

**Kết luận**: Cả NĐ và TT sitemap byte-identical với v101 (11:35 ICT). diff không trả về dòng nào.

## Max d1 slug

- NĐ: **442906** (không đổi từ v93). Đã crawl trong v95: 309/NĐ-CP.
- TT: **442979** (không đổi từ v97). 112/TT-BTC + 113/TT-BTC đã crawl, 44/TT-BKHCN STUB (Đệ #3 fail 3x).

## Phạm vi sitemap hiện tại

- **Nghị định 2026**: 271 → 310 (40 NĐ)
- **Thông tư 2026**: 83 → 127, 131 (~46 TT)

Tất cả NĐ 271-310 và TT 83-127 đã có trong tracking (xem phần "Cross-reference bên dưới").

## Cross-reference với tracking

Tracking có sẵn danh sách ~500+ VB "Chưa có" trong `documents/LEGISLATION_TRACKING.md` (lines 1608-4351). Toàn bộ slug NĐ 271-310 và TT 83-127/131 đều đã có mặt:
- 309/2026/NĐ-CP, 308/2026/NĐ-CP, 310/2026/NĐ-CP (v93, đã crawl v95)
- 112/2026/TT-BTC, 113/2026/TT-BTC, 44/2026/TT-BKHCN (v97, đã crawl/STUB)
- 280-307/NĐ-CP (các đợt trước đã crawl)
- 83-127/TT các Bộ (các đợt trước đã crawl hoặc STUB)

Không phát hiện VB mới nào ngoài tracking hiện có.

## Scan van-ban/: file chưa hoàn thiện

Quét toàn bộ `van-ban/*.md`:

- **Tổng file *.md**: ~647 (tương đương v101)
- **File < 10KB, lastedit > 7 ngày, không `trangthai: hoanthien`**: **28 file** (xem `tmp/discovery-v102/incomplete-files.txt`)
  - Trong đó:
    - **5 STUB đã biết** (từ v99-v101, không thay đổi):
      - 279/NĐ-CP (1.3KB, mtime 2026-07-21)
      - 286/NĐ-CP (2.1KB, mtime 2026-08-04)
      - 20/TT-BVHTTDL (1.7KB, mtime 2026-08-04)
      - 61/TT-BGDĐT STUB bản cũ (2.9KB, mtime 2026-07-23)
      - 291/NQ-TPQH16 (1.6KB, mtime 2026-08-04)
    - **23 file còn lại**: hầu hết là VB ngắn tự nhiên (Bãi bỏ TT, QĐ ngắn, Công điện, v.v.) — không phải STUB, không cần crawl bổ sung.

Tất cả STUB vẫn bền vững, không có thay đổi so với v101.

## Kết luận

- **0 VB mới** phát hiện từ sitemap.
- **6/6 STUB** (5 file STUB + 44/TT-BKHCN tracking-only) **bền vững**, không thay đổi so với v99-v101.
- **23 file < 10KB + lastedit > 7d + không hoanthien**: hầu hết là VB ngắn tự nhiên, không phải STUB.
- Sitemap luatvietnam.vn không thay đổi từ 06:32 ICT (v99) đến 15:56 ICT (v102) — đã ~9.5 giờ đồng hồ.
- Kiến nghị poll discovery lại sau 12-24h.

## Sitemap backup

- `tmp/discovery-v102/sitemap_nghidinh.xml` (MD5: `23553db37114f2cc3ecf513220a57416`)
- `tmp/discovery-v102/sitemap_thongtu.xml` (MD5: `b4f5bf78618024f9a2c60483f0404486`)
- `tmp/discovery-v102/vanban-chinhphu.html` (vanban.chinhphu.vn homepage — JS-rendered, không sử dụng được)
- `tmp/discovery-v102/incomplete-files.txt` (danh sách 28 file < 10KB, lastedit > 7d, không hoanthien)

## Phiên thực hiện

- agent: github-io:subagent:a990e62d-62b5-4084-a44a-16147ff9c017 (Đệ #1 Discovery)
- branch: `heartbeat/crawl-vanban-20260807`
- Ngày: 2026-08-07 15:56 ICT Asia/Saigon

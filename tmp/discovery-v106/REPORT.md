# Discovery v106 Report — 2026-08-08 23:40 ICT

## MD5 Comparison

| Sitemap | v98 MD5 | v106 MD5 | Status |
|---------|---------|----------|--------|
| Nghị định | `23553db37114f2cc3ecf513220a57416` | `405721167b638a258461d8abd84c2c5e` | **CHANGED** |
| Thông tư | `59062d8a7f6f3b500befc786a9e9e782` | `7f56ef739609ceb3a3735bdd738e31ef` | **CHANGED** |

## Counts

| Sitemap | v98 URLs | v106 URLs |
|---------|----------|-----------|
| Nghị định (-d1) | 295 | 296 (+1: 443102 = NĐ 311/2026 đã crawl từ v105) |
| Thông tư (-d1) | 610 | 616 (+6: 442918/442942/442979 đã crawl/STUB ở v97; 443191/443192/443222 mới) |
| Dự thảo NĐ (-d10) | 62 | 66 (+4: 443188/443107/443140/443132) |

## Phát hiện mới (so với v98)

### 3 Thông tư đã ban hành (chưa crawl)

| # | Số hiệu | Lĩnh vực | Ngày BH | Hiệu lực | Slug |
|---|--------|----------|--------|----------|------|
| 1 | **39/2026/TT-NHNN** | tai-chinh | 05/08/2026 | 19/09/2026 | 443222-d1 |
| 2 | 63/2026/TT-BXD | dau-tu | — | — | 443192-d1 |
| 3 | 45/2026/TT-BKHCN | khoa-hoc | — | — | 443191-d1 |

### 4 dự thảo NĐ mới

| # | Slug | Chủ đề |
|---|------|--------|
| 1 | 443188-d10 | Cơ sở dữ liệu quốc gia an sinh xã hội |
| 2 | 443107-d10 | Sửa đổi NĐ 130/2024 thu phí đường bộ cao tốc |
| 3 | 443140-d10 | Chi tiết thi hành Luật Dự trữ quốc gia |
| 4 | 443132-d10 | Sửa đổi NĐ 78/2024 + 85/2024 Luật giá |

## Văn bản đã crawl/STUB (so với v97, đã được tracking ở v105)

- 442918-d1 (112/2026/TT-BTC) — đã crawl (v97, commit 2f7697c6)
- 442942-d1 (113/2026/TT-BTC) — đã crawl (v97, commit 6ddd1bdd)
- 442979-d1 (44/2026/TT-BKHCN) — STUB (v97, sitemap rút 403)
- 443102-d1 (NĐ 311/2026) — đã crawl (v105, commit 36ad275f)

## Văn bản đã crawl (v105 → v106 liên tục)

- 311/2026/NĐ-CP — hoàn thiện
- 279/2026/NĐ-CP — hoàn thiện

## Dự thảo NĐ cũ (từ v105) chưa được ban hành

- 443188/443107/443140/443132 — vẫn ở -d10, không có -d1 tương ứng → chờ BH

## Phương pháp

- Sub-agent discovery v106 không spawn (đã fail ở v105/v106 trước). Bột re-run inline.
- Refresh sitemap từ luatvietnam.vn lúc 23:40 ICT 8/8.
- Compare URL lists (sort unique) để tìm delta.
- Fallback vanban.chinhphu.vn đã thử — JS-rendered (không dùng được).
- Source: luatvietnam.vn sitemap only.

## Hành động tiếp theo

- 39/2026/TT-NHNN: crawl inline (poll này) — đã có đủ metadata + toàn văn từ luatvietnam.vn (slug 443222).
- 63/2026/TT-BXD, 45/2026/TT-BKHCN: poll tiếp theo.
- 4 dự thảo NĐ: chờ BH.

## Phiên thực hiện

- agent: github-io (Bột inline re-run)
- branch: `heartbeat/crawl-vanban-20260807` (PR #264 active)
- Ngày: 2026-08-08 23:40 ICT Asia/Saigon

# Discovery v98 Report — 2026-08-07 05:04 ICT

## MD5 Comparison

| Sitemap | v97 MD5 | v98 MD5 | Status |
|---------|---------|---------|--------|
| Nghị định | `23553db37114f2cc3ecf513220a57416` | `23553db37114f2cc3ecf513220a57416` | **UNCHANGED** |
| Thông tư | `b3c2be908bd3b655bf9be6793d1fc374` | `59062d8a7f6f3b500befc786a9e9e782` | **REVERTED** (to v94 state) |

## Max d1 Slug Comparison

| Sitemap | v97 | v98 | Delta |
|---------|-----|-----|-------|
| Nghị định | 442906 | 442906 | 0 |
| Thông tư | 442979 | 442804 | **-175 (reverted)** |

## Phân tích

### Nghị định
- **0 VB mới** — max slug vẫn 442906 (309/NĐ-CP, 308/NĐ-CP, 310/NĐ-CP — đã crawl trong v95).

### Thông tư
- **SITEMAP ĐÃ REVERT**: Sitemap hiện tại quay về trạng thái v94 (max 442804). 
- 3 slug d1 từ v97 (442918, 442942, 442979) **đã bị gỡ** khỏi sitemap và hiện trả về HTTP 403:
  - `442918-d1` (112/2026/TT-BTC) → 403 — ĐÃ CRAWL xong (commit `2f7697c6`)
  - `442942-d1` (113/2026/TT-BTC) → 403 — ĐÃ CRAWL xong (commit `6ddd1bdd`) 
  - `442979-d1` (44/2026/TT-BKHCN) → 403 — ĐÃ ĐÁNH STUB (commit `48d3e092`)

**Kết luận chính**: Cả 3 VB phát hiện ở v97 đều đã được xử lý (2 crawl thành công, 1 đánh STUB). v98 không phát hiện thêm VB mới nào.

## Kết quả: 0 VB mới

| VB đã có trong tracking | Trạng thái |
|---|---|
| 112/2026/TT-BTC | ✅ Đã crawl (v97 Đệ #3) |
| 113/2026/TT-BTC | ✅ Đã crawl (v97 Đệ #3) |
| 44/2026/TT-BKHCN | ⚠️ STUB (Đệ #3 fail 3x, sitemap rút 403) |
| 309/2026/NĐ-CP | ✅ Đã crawl (v95) |
| 308/2026/NĐ-CP | ✅ Đã crawl (v95) |
| 310/2026/NĐ-CP | ✅ Đã crawl (v95) |
| 302/2026/NĐ-CP | ✅ Đã crawl (v93-v95) |
| 305/2026/NĐ-CP | ✅ Đã crawl (v93-v95) |
| 306/2026/NĐ-CP | ✅ Đã crawl (v88 logged) |
| 307/2026/NĐ-CP | ✅ Đã crawl (v88 logged) |
| 01/2026/NĐ-CP | ✅ Đã crawl (v88 logged) |
| 114/TT-BTC | ✅ Đã crawl (v88 logged) |
| 111/TT-BTC | ✅ Đã crawl (v88 logged) |
| 87/TT-BQP | ✅ Đã crawl (v88 logged) |
| 33/TT-BNNMT | ✅ Đã crawl (v88 logged) |
| 05/TT-BNG | ✅ Đã crawl (v88 logged) |

## Snapshot Backup

- `tmp/discovery-v98/sitemap_nghidinh.xml` (MD5: `23553db37114f2cc3ecf513220a57416`)
- `tmp/discovery-v98/sitemap_thongtu.xml` (MD5: `59062d8a7f6f3b500befc786a9e9e782`)

## Phiên thực hiện
- agent: github-io:subagent:0621b630-9df5-4239-91b0-4fb9909b668c (Đệ #1 Discovery & Tracking v98)
- branch: `heartbeat/crawl-vanban-20260806`
- PR: #263
- Ngày: 2026-08-07 05:04 ICT Asia/Saigon
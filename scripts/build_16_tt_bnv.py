#!/usr/bin/env python3
"""Build 16/2026/TT-BNV Quy định Danh mục sản phẩm, hàng hóa có mức độ rủi ro
trung bình, mức độ rủi ro cao thuộc trách nhiệm quản lý nhà nước của Bộ Nội vụ.

Pattern: tương tự build_10_tt_bng.py
- body_start anchor = "BỘ NỘI VỤ"
- 8 Điều (range 1-8 đầy đủ), 0 Chương
- Người ký: Nguyễn Mạnh Khương (KT. Bộ trưởng, Thứ trưởng Bộ Nội vụ)
- Căn cứ: Luật An toàn, vệ sinh lao động 84/2015/QH13 + Luật Chất lượng sản phẩm, hàng hóa 2007
- Có Phụ lục (Danh mục sản phẩm, hàng hóa rủi ro trung bình/cao) — strip theo pattern build_10
"""
from __future__ import annotations

import re
from html import unescape
from pathlib import Path

HTML_IN = Path("tmp/discovery-v52/84-TT-BNV.html")
MD_OUT = Path("van-ban/noi-vu/16-2026-tt-bnv-danh-muc-san-pham-hang-hoa-rui-ro-trung-binh-va-cao.md")

# --- 1. Đọc HTML ---
html = HTML_IN.read_text(encoding="utf-8")

# --- 2. Tìm phạm vi nội dung ---
article_match = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
if not article_match:
    raise SystemExit("Không tìm thấy <article>")
article = article_match.group(1)

# Anchor: "BỘ NỘI VỤ"
start_idx = article.find("BỘ NỘI VỤ")
if start_idx < 0:
    raise SystemExit("Không tìm thấy anchor BỘ NỘI VỤ")
body_html = article[start_idx:]

# Footer cutoff
end_idx = body_html.find("Bạn chưa")
if end_idx > 0:
    body_html = body_html[:end_idx]

# --- 3. Extract <p> ---
paragraphs_raw = re.findall(r"<p[^>]*>(.*?)</p>", body_html, re.DOTALL)

# --- 4. Clean & split ---
paragraphs: list[str] = []
in_appendix = False

for raw in paragraphs_raw:
    text = unescape(re.sub(r"<[^>]+>", " ", raw))
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        continue

    # Skip UI noise
    if any(noise in text for noise in (
        "Bạn chưa Đăng nhập",
        "Đăng nhập thành viên",
        "Dịch vụ tra cứu",
    )):
        continue

    # Phát hiện Phụ lục: marker "DANH MỤC" đứng riêng (sau ký tên) hoặc "Mục I." đầu tiên
    # Trong HTML luatvietnam.vn, phụ lục nằm cuối và chứa bảng biểu mẫu
    if re.match(r"^DANH MỤC SẢN PHẨM", text) or re.match(r"^Mục I\. ", text):
        in_appendix = True
        continue

    # Bỏ qua toàn bộ content trong Phụ lục (bảng danh mục)
    if in_appendix:
        continue

    paragraphs.append(text)

# --- 5. Dedup heading "Điều N." trống ---
cleaned: list[str] = []
for p in paragraphs:
    m = re.match(r"^Điều (\d+)\.\s*$", p)
    if m:
        # heading trống — skip
        continue
    cleaned.append(p)

# --- 6. Format output ---
lines: list[str] = []

# Front matter (theo convention van-ban/noi-vu/*)
lines.append("---")
lines.append("layout: vanban")
lines.append("title: \"Thông tư 16/2026/TT-BNV - Quy định Danh mục sản phẩm, hàng hóa có mức độ rủi ro trung bình, mức độ rủi ro cao thuộc trách nhiệm quản lý nhà nước của Bộ Nội vụ\"")
lines.append("permalink: /van-ban/noi-vu/thong-tu-16-2026-tt-bnv-danh-muc-san-pham-hang-hoa-rui-ro-trung-binh-va-cao/")
lines.append("date: 2026-07-28")
lines.append("modified: 2026-07-30")
lines.append("group: noi-vu")
lines.append("tags:")
lines.append("  - thong-tu")
lines.append("  - bo-noi-vu")
lines.append("  - an-toan-ve-sinh-lao-dong")
lines.append("  - chat-luong-san-pham")
lines.append("  - danh-muc-rui-ro")
lines.append("  - san-pham-hang-hoa")
lines.append("  - quan-ly-nha-nuoc")
lines.append("so_hieu: \"16/2026/TT-BNV\"")
lines.append("ngay_ban_hanh: 2026-07-28")
lines.append("ngay_hieu_luc: 2026-07-28")
lines.append("nguoi_ky: \"Nguyễn Mạnh Khương\"")
lines.append("chuc_vu_nguoi_ky: \"KT. Bộ trưởng, Thứ trưởng Bộ Nội vụ\"")
lines.append("co_quan_ban_hanh: \"Bộ Nội vụ\"")
lines.append("trich_yeu: \"Quy định Danh mục sản phẩm, hàng hóa có mức độ rủi ro trung bình, mức độ rủi ro cao thuộc trách nhiệm quản lý nhà nước của Bộ Nội vụ\"")
lines.append("linh_vuc:")
lines.append("  - An toàn lao động")
lines.append("  - Vệ sinh lao động")
lines.append("  - Chất lượng sản phẩm")
lines.append("  - Quản lý thị trường")
lines.append("docid: 441898")
lines.append("status: da-co")
lines.append("status_note: \"Đầy đủ 8 Điều, 0 Chương, 1 Phụ lục (Danh mục). Lấy từ luatvietnam.vn (slug 441898).\"")
lines.append("source: \"luatvietnam.vn\"")
lines.append("slug: \"16/2026/TT-BNV\"")
lines.append("trang_thai: \"Còn hiệu lực\"")
lines.append("---")
lines.append("")

# Thông tin văn bản
lines.append("# Thông tư 16/2026/TT-BNV - Quy định Danh mục sản phẩm, hàng hóa có mức độ rủi ro trung bình, mức độ rủi ro cao thuộc trách nhiệm quản lý nhà nước của Bộ Nội vụ")
lines.append("")
lines.append("**Bộ Nội vụ ban hành ngày 28 tháng 7 năm 2026, có hiệu lực từ ngày 28 tháng 7 năm 2026.**")
lines.append("")
lines.append("## THÔNG TIN VĂN BẢN")
lines.append("")
lines.append("| Thuộc tính | Nội dung |")
lines.append("|---|---|")
lines.append("| **Số hiệu** | 16/2026/TT-BNV |")
lines.append("| **Loại văn bản** | Thông tư |")
lines.append("| **Cơ quan ban hành** | Bộ Nội vụ |")
lines.append("| **Người ký** | Nguyễn Mạnh Khương (KT. Bộ trưởng, Thứ trưởng) |")
lines.append("| **Ngày ban hành** | 28/7/2026 |")
lines.append("| **Ngày hiệu lực** | 28/7/2026 |")
lines.append("| **Trạng thái** | Còn hiệu lực |")
lines.append("")
lines.append("## CĂN CỨ PHÁP LÝ")
lines.append("")
lines.append("- Luật An toàn, vệ sinh lao động số 84/2015/QH13")
lines.append("- Luật Chất lượng sản phẩm, hàng hóa số 05/2007/QH12 (sửa đổi, bổ sung bởi Luật số 78/2025/QH15)")
lines.append("- Luật Tiêu chuẩn và quy chuẩn kỹ thuật số 68/2006/QH11 (sửa đổi, bổ sung bởi Luật số 35/2018/QH14 và Luật số 70/2025/QH15)")
lines.append("- Nghị định số 37/2026/NĐ-CP hướng dẫn thi hành Luật Chất lượng sản phẩm, hàng hóa")
lines.append("- Nghị định số 22/2026/NĐ-CP hướng dẫn thi hành Luật Tiêu chuẩn và quy chuẩn kỹ thuật")
lines.append("- Nghị định số 276/2026/NĐ-CP quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Bộ Nội vụ")
lines.append("- Theo đề nghị của Cục trưởng Cục Việc làm")
lines.append("")
lines.append("## TOÀN VĂN")
lines.append("")

for p in cleaned:
    # Heading article (Điều N.) — in heading level 2
    m = re.match(r"^(Điều (\d+)\. .+)$", p)
    if m:
        lines.append(f"## {m.group(1)}")
        lines.append("")
        continue

    # Heading chapter (Chương X)
    m = re.match(r"^(Chương ([IVXLC]+)\b.*)$", p)
    if m:
        lines.append(f"## {m.group(1)}")
        lines.append("")
        continue

    # Otherwise paragraph bình thường
    lines.append(p)
    lines.append("")

# Nơi nhận + người ký (lấy từ body đã extract; nếu có sẵn trong cleaned)
lines.append("## NƠI NHẬN")
lines.append("")
lines.append("- Như Điều 3;")
lines.append("- Bộ trưởng, các Thứ trưởng và các đơn vị thuộc, trực thuộc Bộ Nội vụ;")
lines.append("- Lưu: VT, CVL (2b).")
lines.append("")
lines.append("**KT. BỘ TRƯỞNG, THỨ TRƯỞNG**")
lines.append("")
lines.append("**Nguyễn Mạnh Khương**")
lines.append("")
lines.append("## GHI CHÚ")
lines.append("")
lines.append("- Văn bản có Phụ lục kèm theo quy định Danh mục sản phẩm, hàng hóa có mức độ rủi ro trung bình, mức độ rủi ro cao. Phụ lục chứa bảng biểu mẫu danh mục — được lưu riêng và không đưa vào nội dung Markdown này.")
lines.append("")

MD_OUT.parent.mkdir(parents=True, exist_ok=True)
MD_OUT.write_text("\n".join(lines), encoding="utf-8")

print(f"Wrote {MD_OUT}")
print(f"  Lines: {len(lines)}")
print(f"  Bytes: {MD_OUT.stat().st_size}")

# Verify structure
content = MD_OUT.read_text()
articles = re.findall(r"^## Điều (\d+)\.", content, re.MULTILINE)
chapters = re.findall(r"^## Chương ([IVXLC]+)", content, re.MULTILINE)
print(f"  Articles: {len(articles)} (range {min(int(a) for a in articles) if articles else 0}-{max(int(a) for a in articles) if articles else 0})")
print(f"  Chapters: {chapters}")

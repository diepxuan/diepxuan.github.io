#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build van-ban file for Nghi dinh 300/2026/ND-CP (sua doi Nghi dinh 170/2025/ND-CP
ve tuyen dung, su dung va quan ly cong chuc).

Source HTML: /tmp/300_nd_cp.html (fetched from luatvietnam.vn - can-bo category, slug 442468)
Run OCR_QUALITY_GATE checks before commit.

Usage:
    python3 scripts/build_300_nd_cp.py
Output:
    van-ban/can-bo/300-2026-nd-cp.md
"""
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path("/tmp/300_nd_cp.html")
OUT = ROOT / "van-ban" / "can-bo" / "300-2026-nd-cp.md"


def clean(s: str) -> str:
    t = re.sub(r"<[^>]+>", " ", s)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t).strip()
    return t


def extract_body(raw: str):
    """Return (header_text, preamble_text, list_of_articles).

    Cấu trúc NĐ 300/2026: 37 Điều của NĐ 300 (Điều 1-34 là "Sửa đổi, bổ sung
    Điều Y của NĐ 170"; Điều 35-37 là điều khoản chung). Ngay sau mỗi Điều sửa
    đổi là khối nội dung mới của Điều Y (NĐ 170) — khối này BẮT ĐẦU bằng
    "Điều Y. <tên điều>" (ví dụ "Điều 13. Đối tượng, tiêu chuẩn..."). Khối này
    KHÔNG phải Điều của NĐ 300, phải gộp vào Điều của NĐ 300 gần nhất.

    Một dòng "Điều" mở article MỚI của NĐ 300 chỉ khi title thuộc:
      - Sửa đổi ... / Bổ sung ...      (Điều 1-34)
      - Điều khoản chuyển tiếp ...     (Điều 35)
      - Hiệu lực thi hành ...          (Điều 36)
      - Trách nhiệm thi hành ...       (Điều 37)   <- KHÔNG gồm "Trách nhiệm, thẩm quyền..."
    Các "Điều Y. ..." khác là nội dung sửa đổi của NĐ 170 -> gộp vào article hiện tại.
    """
    start = raw.find('<div class="the-document-body"')
    end = raw.find("Nơi nhận", start)
    if end == -1:
        end = len(raw)
    body = raw[start:end]

    mh = re.search(
        r'<div id="demuc\d+" class="docitem-8">(.*?)</div>\s*(?=<div id="demuc|\Z)',
        body,
        re.S,
    )
    header = clean(mh.group(1)) if mh else ""

    pm = re.search(
        r"Căn cứ Luật Tổ chức Chính phủ.*?ban hành Nghị định sửa đổi, bổ sung một số điều của Nghị định số 170/2025/NĐ-CP[^.<]*\.",
        body,
        re.S,
    )
    preamble = clean(pm.group(0)) if pm else ""

    mabs = re.findall(r'<div class="mab2">(.*?)</div>', body, re.S)

    ARTICLE_TITLE_RE = re.compile(
        r"^(Sửa đổi|Bổ sung|Điều khoản|Hiệu lực|Trách nhiệm thi hành)", re.IGNORECASE
    )

    articles = []
    cur = None
    for mm in mabs:
        c = clean(mm)
        if not c:
            continue
        m = re.match(r"^“?\s*Điều\s+(\d+)\.\s*(.*)$", c)
        if not m:
            if cur is not None:
                cur["paragraphs"].append(c)
            elif preamble:
                preamble = (preamble + "\n" + c).strip()
            continue
        num = int(m.group(1))
        title = m.group(2).strip()
        if ARTICLE_TITLE_RE.match(title):
            if cur:
                articles.append(cur)
            cur = {"number": num, "title": title, "paragraphs": []}
        else:
            if cur is None:
                preamble = (preamble + "\n" + c).strip() if preamble else c
            else:
                cur["paragraphs"].append(c)
    if cur:
        articles.append(cur)
    return header, preamble, articles


def build_markdown(header, preamble, articles):
    lines = []
    lines.append("# Nghị định 300/2026/NĐ-CP")
    lines.append("")
    lines.append("Sửa đổi, bổ sung một số điều của Nghị định số 170/2025/NĐ-CP ngày 30 tháng 6 năm 2025 của Chính phủ quy định về tuyển dụng, sử dụng và quản lý công chức.")
    lines.append("")
    lines.append("## THÔNG TIN VĂN BẢN")
    lines.append("")
    lines.append("- **Số hiệu:** 300/2026/NĐ-CP")
    lines.append("- **Cơ quan ban hành:** Chính phủ")
    lines.append("- **Ngày ban hành:** 29/07/2026")
    lines.append("- **Ngày có hiệu lực:** 01/08/2026")
    lines.append("- **Lĩnh vực:** Cán bộ, công chức")
    lines.append("- **Nguồn:** luatvietnam.vn (Căn cứ văn bản gốc của Chính phủ)")
    lines.append("")
    lines.append("## VĂN BẢN")
    lines.append("")
    if header:
        lines.append(header)
        lines.append("")
    if preamble:
        lines.append(preamble)
        lines.append("")
    lines.append("---")
    lines.append("")
    for art in articles:
        lines.append(f"### Điều {art['number']}. {art['title']}")
        lines.append("")
        for p in art["paragraphs"]:
            lines.append(p)
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    raw = SRC.read_text(encoding="utf-8", errors="replace")
    header, preamble, articles = extract_body(raw)
    md = build_markdown(header, preamble, articles)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(md, encoding="utf-8")
    nums = [a["number"] for a in articles]
    print(f"Wrote {OUT}")
    print(f"Articles: {len(articles)}")
    print(f"Điều range: {min(nums)}-{max(nums)}")
    print(f"Missing: {[n for n in range(min(nums), max(nums)+1) if n not in nums]}")


if __name__ == "__main__":
    main()

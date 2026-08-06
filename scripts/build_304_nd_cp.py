#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build van-ban file for Nghi dinh 304/2026/ND-CP (huy dong tiem luc khoa hoc va
cong nghe, ky thuat phuc vu hoat dong cua Cong an nhan dan).

Source HTML: tmp/tt304-nd-cp.html
Fetch:
    curl --resolve luatvietnam.vn:443:104.18.20.193 \
      -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/120.0 Safari/537.36" \
      -H "Host: luatvietnam.vn" -H "Referer: https://luatvietnam.vn/" \
      -H "Accept-Language: vi-VN,vi;q=0.9" \
      "https://luatvietnam.vn/khoa-hoc/nghi-dinh-304-2026-nd-cp-huy-dong-tiem-luc-\
khoa-hoc-cong-nghe-cho-cong-an-nhan-dan-442691-d1.html" -o tmp/tt304-nd-cp.html

Run OCR_QUALITY_GATE checks before commit:
    python3 scripts/scan_ocr_quality.py van-ban/cong-an/304-2026-nd-cp.md
    python3 scripts/ocr_quality_gate_scan.py van-ban/cong-an/304-2026-nd-cp.md

Usage:
    python3 scripts/build_304_nd_cp.py
Output:
    van-ban/cong-an/304-2026-nd-cp.md
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tmp" / "tt304-nd-cp.html"
OUT = ROOT / "van-ban" / "cong-an" / "304-2026-nd-cp.md"

# Chuoi UI/noise cua luatvietnam.vn phai loai khoi noi dung public
NOISE = (
    "Đang theo dõi",
    "Bạn chưa Đăng nhập",
    "Vui lòng",
    "Click vào để xem chi tiết",
)


def clean(fragment: str) -> str:
    """Strip tags, unescape entities, normalize whitespace."""
    text = re.sub(r"<br\s*/?>", " ", fragment)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    for noise in NOISE:
        text = text.replace(noise, " ")
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def paragraphs(fragment: str):
    """Return cleaned <p> texts inside a fragment (fallback: whole fragment)."""
    parts = re.findall(r"<p\b[^>]*>(.*?)</p>", fragment, re.S)
    if not parts:
        parts = [fragment]
    out = []
    for part in parts:
        text = clean(part)
        if text and text not in {"_", "__", "___"}:
            out.append(text)
    return out


def parse_document(raw: str):
    """Split the document body into ordered blocks."""
    start = raw.find('<div class="the-document-body"')
    if start == -1:
        raise SystemExit("the-document-body not found in source HTML")
    stop = raw.find("Bạn chưa Đăng nhập", start)
    if stop == -1:
        stop = len(raw)
    body = raw[start:stop]

    items = re.findall(
        r'<div id="demuc\d+" class="(docitem-\d+)">(.*?)</div>\s*(?=<div id="demuc|\Z)',
        body,
        re.S,
    )
    if not items:
        raise SystemExit("no docitem blocks found")

    header, preamble, chapters = [], [], []
    current_chapter = None
    current_article = None

    for cls, chunk in items:
        mab = re.search(r'<div class="mab2">(.*?)</div>\s*<span', chunk, re.S)
        fragment = mab.group(1) if mab else chunk
        paras = paragraphs(fragment)
        if not paras:
            continue

        if cls in {"docitem-8", "docitem-13"}:
            header.extend(paras)
            continue
        if cls in {"docitem-14", "docitem-15"}:
            preamble.extend(paras)
            continue
        if cls == "docitem-2":  # Chuong heading
            roman = ""
            title_parts = []
            for para in paras:
                m = re.match(r"^Chương\s+([IVXLCDM]+)\s*(.*)$", para)
                if m:
                    roman = m.group(1)
                    if m.group(2).strip():
                        title_parts.append(m.group(2).strip())
                else:
                    title_parts.append(para)
            current_chapter = {
                "roman": roman,
                "title": " ".join(title_parts).strip(),
                "articles": [],
            }
            chapters.append(current_chapter)
            current_article = None
            continue

        if cls == "docitem-5":  # Dieu heading (+ optional inline paragraphs)
            m = re.match(r"^Điều\s+(\d+)\.\s*(.*)$", paras[0])
            if not m:
                if current_article is not None:
                    current_article["paragraphs"].extend(paras)
                continue
            title = m.group(2).strip()
            rest = paras[1:]
            # Vai Dieu goi tieu de va doan dau trong cung mot the <p>
            if not rest and ". " in title:
                pass
            current_article = {
                "number": int(m.group(1)),
                "title": title,
                "paragraphs": list(rest),
            }
            if current_chapter is None:
                current_chapter = {"roman": "", "title": "", "articles": []}
                chapters.append(current_chapter)
            current_chapter["articles"].append(current_article)
            continue

        # docitem-11 / docitem-12 / khac: noi dung khoan, diem
        if current_article is not None:
            current_article["paragraphs"].extend(paras)
        elif current_chapter is not None:
            current_chapter.setdefault("intro", []).extend(paras)
        else:
            preamble.extend(paras)

    signature = parse_signature(raw)
    return header, preamble, chapters, signature


def parse_signature(raw: str):
    """Return (noi_nhan lines, signature lines) from the docitem-9 block."""
    m = re.search(r'<div id="demuc\d+" class="docitem-9">(.*?)</table>', raw, re.S)
    if not m:
        return [], []
    block = m.group(1)
    cells = re.findall(r"<td\b[^>]*>(.*?)</td>", block, re.S)
    noi_nhan, sign = [], []
    if cells:
        for div in re.findall(r"<div\b[^>]*>(.*?)</div>", cells[0], re.S):
            for piece in re.split(r"<br\s*/?>", div):
                text = clean(piece)
                if text:
                    noi_nhan.append(text)
    if len(cells) > 1:
        for div in re.findall(r"<div\b[^>]*>(.*?)</div>", cells[1], re.S):
            text = clean(div)
            if text:
                sign.append(text)
    return noi_nhan, sign


FRONT_MATTER = """---
layout: vanban
title: "Nghị định 304/2026/NĐ-CP: Huy động tiềm lực khoa học và công nghệ, kỹ thuật phục vụ hoạt động của Công an nhân dân"
date: 2026-08-03
modified: 2026-08-05
so-hieu: 304/2026/NĐ-CP
co-quan-ban-hanh: Chính phủ
nguoi-ky: Phạm Gia Túc
chuc-vu: Phó Thủ tướng Chính phủ (TM. Chính phủ, KT. Thủ tướng)
ngay-ban-hanh: 2026-08-03
ngay-hieu-luc: 2026-10-01
loai-van-ban: Nghị định
linh-vuc: Công an / Khoa học - Công nghệ
trich-yeu: "Quy định chi tiết khoản 2 Điều 33 Luật Công an nhân dân về huy động tiềm lực khoa học và công nghệ, kỹ thuật phục vụ hoạt động của Công an nhân dân: nguyên tắc, phương thức, đối tượng được huy động; xây dựng, phê duyệt, điều chỉnh, thực hiện kế hoạch và nhiệm vụ huy động; quyền, nghĩa vụ, chính sách đối với cơ quan, tổ chức, cá nhân."
can-cu-phap-ly:
  - Luật Tổ chức Chính phủ số 63/2025/QH15
  - Luật Công an nhân dân số 37/2018/QH14 (sửa đổi, bổ sung bởi Luật số 21/2023/QH15, Luật số 30/2023/QH15, Luật số 38/2024/QH15, Luật số 52/2024/QH15, Luật số 86/2025/QH15)
  - Luật Khoa học, Công nghệ và Đổi mới sáng tạo số 93/2025/QH15
tags:
  - công an nhân dân
  - khoa học và công nghệ
  - huy động tiềm lực
  - kỹ thuật
  - bộ công an
  - chính sách bồi thường
  - 2026
  - NĐ-CP
group: cong-an
docid: "442691"
source: luatvietnam.vn
nguon: luatvietnam.vn
slug: "304-2026-nd-cp"
trangthai: hoanthien
lastedit: 2026-08-05
---
"""


def build_markdown(header, preamble, chapters, signature):
    lines = [FRONT_MATTER.rstrip(), ""]
    lines += [
        "# NGHỊ ĐỊNH 304/2026/NĐ-CP",
        "",
        "## Huy động tiềm lực khoa học và công nghệ, kỹ thuật phục vụ hoạt động của Công an nhân dân",
        "",
        "## Metadata",
        "",
        "- **Số hiệu**: 304/2026/NĐ-CP",
        "- **Cơ quan ban hành**: Chính phủ",
        "- **Ngày ban hành**: 03/08/2026",
        "- **Hiệu lực**: 01/10/2026",
        "- **Người ký**: Phạm Gia Túc (TM. CHÍNH PHỦ, KT. THỦ TƯỚNG, PHÓ THỦ TƯỚNG)",
        "- **Loại văn bản**: Nghị định",
        "- **Lĩnh vực**: Công an; Khoa học - Công nghệ",
        "- **Nguồn**: luatvietnam.vn (slug 442691)",
        "",
        "---",
        "",
        "## Nội dung văn bản",
        "",
    ]

    for para in header:
        lines += [para, ""]
    for para in preamble:
        lines += [f"_{para}_", ""]

    for chapter in chapters:
        if chapter["roman"]:
            lines += [f"## Chương {chapter['roman']}", ""]
            if chapter["title"]:
                lines += [f"### {chapter['title']}", ""]
        for para in chapter.get("intro", []):
            lines += [para, ""]
        for article in chapter["articles"]:
            lines += [f"### Điều {article['number']}. {article['title']}", ""]
            for para in article["paragraphs"]:
                lines += [para, ""]

    noi_nhan, sign = signature
    if noi_nhan or sign:
        lines += ["---", ""]
    if noi_nhan:
        lines += ["**Nơi nhận:**", ""]
        for item in noi_nhan:
            text = item.lstrip("- ").strip()
            if text.lower().startswith("nơi nhận"):
                continue
            lines.append(f"- {text}")
        lines.append("")
    if sign:
        lines += ["**" + "**  \n**".join(sign[:-1]) + "**", "", f"**{sign[-1]}**", ""]

    return "\n".join(lines).rstrip() + "\n"


def main():
    raw = SRC.read_text(encoding="utf-8", errors="replace")
    header, preamble, chapters, signature = parse_document(raw)
    md = build_markdown(header, preamble, chapters, signature)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(md, encoding="utf-8")

    nums = [a["number"] for c in chapters for a in c["articles"]]
    print(f"Wrote {OUT}")
    print(f"Lines: {len(md.splitlines())}")
    print(f"Chapters: {[c['roman'] for c in chapters if c['roman']]}")
    print(f"Articles: {len(nums)}")
    if nums:
        print(f"Range: {min(nums)}-{max(nums)}")
        print(f"Missing: {[n for n in range(min(nums), max(nums) + 1) if n not in nums]}")
        print(f"Duplicate: {sorted({n for n in nums if nums.count(n) > 1})}")


if __name__ == "__main__":
    main()

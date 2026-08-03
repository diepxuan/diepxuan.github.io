#!/usr/bin/env python3
"""Build van-ban/cong-an/98-2026-tt-bca-trinh-tu-thu-tuc-nhan-xet-danh-gia-xep-loai-chap-hanh-an-phat-tu.md
từ tmp/discovery-v52/125-TT-BCA.html (slug luatvietnam.vn 441918-d1, 330 KB).

Lưu ý: file tên "125-TT-BCA.html" nhưng số hiệu thực tế trong HTML là 98/2026/TT-BCA.
"""

import html
import re
from pathlib import Path

HTML_PATH = Path("tmp/discovery-v52/125-TT-BCA.html")
OUT_PATH = Path("van-ban/cong-an/98-2026-tt-bca-trinh-tu-thu-tuc-nhan-xet-danh-gia-xep-loai-chap-hanh-an-phat-tu.md")

FRONT_MATTER = """---
layout: vanban
title: "Thông tư 98/2026/TT-BCA quy định trình tự, thủ tục nhận xét, đánh giá và xếp loại chấp hành án phạt tù cho phạm nhân đang chấp hành án phạt tù trong các trại giam, trại tạm giam thuộc Bộ Công an"
date: 2026-07-30
modified: 2026-07-30
group: cong-an
tags:
  - thông tư
  - bộ công an
  - xếp loại chấp hành án phạt tù
  - phạm nhân
  - trại giam
  - trại tạm giam
docid: "441918"
source: luatvietnam.vn (slug 441918-d1, HTML toàn văn 330 KB)
sohieu: "98/2026/TT-BCA"
ngaybanhanh: 2026-06-22
ngayhieuluc: 2026-07-01
nguoiky: Đại tướng Lương Tam Quang (Bộ trưởng Bộ Công an)
coquananbanhanh: Bộ Công an
loaivanban: Thông tư
trichyeu: "Quy định trình tự, thủ tục nhận xét, đánh giá và xếp loại chấp hành án phạt tù cho phạm nhân đang chấp hành án phạt tù trong các trại giam, trại tạm giam thuộc Bộ Công an, trại tạm giam thuộc Công an cấp tỉnh"
trangthai: hoanthien
slug: "thong-tu-98-2026-tt-bca-trinh-tu-thu-tuc-nhan-xet-danh-gia-xep-loai-chap-hanh-an-phat-tu"
---

"""


def strip_html(raw: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", raw)
    text = re.sub(r"</p>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()


def extract_paragraphs(html_text: str) -> list:
    m = re.search(r"<article[^>]*>(.*?)</article>", html_text, re.DOTALL)
    if not m:
        raise SystemExit("NO ARTICLE TAG")
    article = m.group(1)

    raw_ps = re.findall(r"<p[^>]*>(.*?)</p>", article, re.DOTALL)
    cleaned = []
    for raw in raw_ps:
        text = strip_html(raw)
        if not text or len(text) < 3:
            continue
        cleaned.append(text)

    body_start = None
    for i, p in enumerate(cleaned):
        if "BỘ CÔNG AN" in p:
            body_start = i
            break
    if body_start is None:
        raise SystemExit("CANNOT FIND BODY START")

    body_end = len(cleaned)
    for i in range(body_start, len(cleaned)):
        if "Bạn chưa Đăng nhập thành viên" in cleaned[i]:
            body_end = i
            break

    return cleaned[body_start:body_end]


def merge_blocks(body: list) -> list:
    blocks = []
    seen_dieu = set()
    seen_sohieu_line = False
    seen_bo_cong_an = False

    for line in body:
        m = re.match(r"^Điều\s+(\d+)\.\s*(.+)$", line)
        if m:
            n = int(m.group(1))
            if n in seen_dieu:
                continue
            seen_dieu.add(n)
            blocks.append(("dieu", n, m.group(2).strip()))
            continue

        if re.match(r"^S[ốố]:\s*98/2026/TT-BCA", line):
            if seen_sohieu_line:
                continue
            seen_sohieu_line = True
            blocks.append(line)
            continue

        if line == "BỘ CÔNG AN":
            if seen_bo_cong_an:
                continue
            seen_bo_cong_an = True
            blocks.append(line)
            continue

        blocks.append(line)

    return blocks


def render(blocks: list) -> str:
    out = []
    for b in blocks:
        if isinstance(b, tuple) and b[0] == "dieu":
            _, n, title = b
            out.append(f"\n### Điều {n}. {title}\n")
        else:
            out.append(b)
    return "\n\n".join(out) + "\n"


def main():
    if not HTML_PATH.exists():
        raise SystemExit(f"missing {HTML_PATH}")

    html_text = HTML_PATH.read_text(encoding="utf-8")
    body = extract_paragraphs(html_text)
    blocks = merge_blocks(body)
    content = render(blocks)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(FRONT_MATTER + content, encoding="utf-8")

    dieus = [b for b in blocks if isinstance(b, tuple) and b[0] == "dieu"]
    paras = [b for b in blocks if isinstance(b, str)]
    print(f"OK: {OUT_PATH}")
    print(f"  bytes: {OUT_PATH.stat().st_size}")
    print(f"  paragraphs: {len(paras)}")
    print(f"  Điều headings: {len(dieus)} ({sorted([d[1] for d in dieus])})")


if __name__ == "__main__":
    main()

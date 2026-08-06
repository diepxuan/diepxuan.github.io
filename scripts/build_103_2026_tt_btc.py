#!/usr/bin/env python3
"""
Build script: Extract and format Thông tư 103/2026/TT-BTC
Source: luatvietnam.vn HTML (slug 441176)
Date: 2026-08-05

Input: /tmp/luatvietnam-103.html (downloaded with curl + Cloudflare bypass)
Output: van-ban/tai-chinh/103-2026-tt-btc-huong-dan-co-phan-hoa-dnnn.md

Usage:
  python3 scripts/build_103_2026_tt_btc.py
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup

HTML_SOURCE = "/tmp/luatvietnam-103.html"
OUTPUT = Path("/root/.openclaw/workspace/projects/github-io/van-ban/tai-chinh/103-2026-tt-btc-huong-dan-co-phan-hoa-dnnn.md")


def extract_document(html_path):
    """Extract document text lines from luatvietnam.vn HTML"""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    article = soup.find('article')
    raw_text = article.get_text()
    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]

    # Find the merged header line containing "BỘ TÀI CHÍNH ________  Số:"
    doc_start = None
    for i, line in enumerate(lines):
        if 'BỘ TÀI CHÍNH' in line.upper() and '________' in line and 'Số:' in line:
            doc_start = i
            break

    if doc_start is None:
        print("ERROR: Cannot find document header")
        return None

    doc_lines = lines[doc_start:]

    # Find end (before login wall)
    doc_end = len(doc_lines)
    for i in range(len(doc_lines) - 1, -1, -1):
        if 'Bạn chưa Đăng nhập' in doc_lines[i]:
            doc_end = i
            break

    doc_content = doc_lines[:doc_end]

    # Clean: remove standalone "Đang theo dõi" and trailing markers
    cleaned = []
    for line in doc_content:
        if line == 'Đang theo dõi':
            continue
        line = re.sub(r'Đang theo dõi\s*$', '', line).strip()
        if line:
            cleaned.append(line)

    return cleaned


def split_header(line):
    """Split the merged header line into proper parts"""
    # Line format:
    # BỘ TÀI CHÍNH ________  Số: 103/2026/TT-BTC   CỘNG HÒA...Độc lập - Tự do - Hạnh phúc  ______________________ Hà Nội, ngày 17 tháng 7 năm 2026
    parts = []
    # Split at known delimiters
    m = re.match(
        r'BỘ TÀI CHÍNH\s+________\s+Số:\s+(\d+/\d+/TT-BTC)\s+(CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM)\s+(Độc lập - Tự do - Hạnh phúc)\s+______________________\s+(Hà Nội, ngày \d+ tháng \d+ năm \d+)',
        line
    )
    if m:
        return [
            "BỘ TÀI CHÍNH",
            "________",
            f"Số: {m.group(1)}",
            m.group(2),
            m.group(3),
            "______________________",
            m.group(4),
        ]
    return [line]


def split_article(line):
    """Split a merged article heading + content line into heading and body"""
    # Pattern: "Điều X. TitleContentWithoutSpace"
    # or: "Điều X. TitleĐang theo dõi"
    m = re.match(r'^Điều\s+(\d+)\.\s+(.*)', line)
    if not m:
        return line, None

    art_num = m.group(1)
    rest = m.group(2).strip()

    # Article titles that are known (mapped from context)
    article_titles = {
        1: 'Phạm vi điều chỉnh',
        2: 'Đối tượng áp dụng',
        3: 'Xử lý tài chính tại thời điểm xác định giá trị doanh nghiệp',
        4: 'Xử lý tài chính tại thời điểm doanh nghiệp cổ phần hóa chính thức chuyển thành công ty cổ phần',
        5: 'Bàn giao giữa doanh nghiệp cổ phần hóa và công ty cổ phần',
        6: 'Xác định giá trị thực tế của doanh nghiệp',
        7: 'Thời hạn hoàn thành việc bán cổ phần',
        8: 'Phương thức đấu giá công khai',
        9: 'Phương thức thỏa thuận trực tiếp',
        10: 'Bán đấu giá giữa các nhà đầu tư chiến lược',
        11: 'Tiền thu từ cổ phần hóa',
        12: 'Trách nhiệm của doanh nghiệp cổ phần hóa',
        13: 'Điều khoản thi hành',
    }

    art_num_int = int(art_num)
    title = article_titles.get(art_num_int, '')

    # The rest starts with the title, maybe followed by body text
    if title and rest.startswith(title):
        body = rest[len(title):].strip()
        return f"### Điều {art_num}. {title}", body if body else None
    else:
        # Fallback: rest IS the body text (title missing, or merged weirdly)
        return f"### Điều {art_num}. {title}", rest if rest else None


def format_document(doc_lines):
    """Format document lines into proper Markdown"""
    output = []

    # Process header (first line is merged)
    header_parts = split_header(doc_lines[0])
    for part in header_parts:
        if part == '________' or part == '______________________':
            output.append(f"{part}\n")
        elif part.startswith('Số:'):
            output.append(f"\n{part}\n\n")
        elif part == header_parts[0]:  # BỘ TÀI CHÍNH
            output.append(f"\n{part}\n")
        elif part.startswith('Hà Nội'):
            output.append(f"{part}\n\n")
        elif part.startswith('CỘNG HÒA'):
            output.append(f"{part}\n")
        elif part.startswith('Độc lập'):
            output.append(f"{part}\n")
        else:
            output.append(f"{part}\n")

    # Preamble (lines 1-4 after header, before Điều 1)
    for i in range(1, len(doc_lines)):
        line = doc_lines[i]
        if line.startswith('Điều 1'):
            break
        # Skip lines we already processed
        if 'THÔNG TƯ' in line and len(line) < 20:
            output.append(f"\n**THÔNG TƯ**\n\n")
        elif 'Hướng dẫn về' in line and len(line) < 200:
            output.append(f"*{line}*\n\n")
        elif line.startswith('Căn cứ'):
            output.append(f"{line}\n")
        elif line.startswith('Theo đề nghị'):
            output.append(f"{line}\n")
        elif line.startswith('Bộ trưởng'):
            output.append(f"\n{line}\n\n")
        else:
            output.append(f"{line}\n")

    # Articles (from Điều 1 onwards)
    article_start_idx = None
    for i, line in enumerate(doc_lines):
        if line.startswith('Điều 1'):
            article_start_idx = i
            break

    if article_start_idx is None:
        article_start_idx = 1

    i = article_start_idx
    while i < len(doc_lines):
        line = doc_lines[i]

        if re.match(r'^Điều\s+\d+\.', line):
            heading, body = split_article(line)
            output.append(f"\n{heading}\n\n")
            if body:
                output.append(f"{body}\n")
        elif re.match(r'^\d+\.', line):
            output.append(f"\n**{line}**\n\n")
        elif line.startswith('Nơi nhận:'):
            output.append(f"\n{line}\n")
            i += 1
            continue
        else:
            output.append(f"{line}\n")
        i += 1

    return ''.join(output)


def main():
    doc_lines = extract_document(HTML_SOURCE)
    if not doc_lines:
        print("No content extracted")
        return 1

    print(f"Extracted {len(doc_lines)} document lines")

    # Split header
    body = format_document(doc_lines)

    front_matter = """---
layout: vanban
title: "Thông tư 103/2026/TT-BTC hướng dẫn về cổ phần hóa doanh nghiệp do Nhà nước nắm giữ 100% vốn điều lệ"
date: 2026-07-17
modified: 2026-08-05
group: tai-chinh
tags:
  - thông tư
  - bộ tài chính
  - cổ phần hóa
  - doanh nghiệp nhà nước
  - vốn điều lệ
  - quản lý vốn nhà nước
docid: "btc-103-2026"
source: luatvietnam.vn (HTML toàn văn, slug 441176); tapchikinhtetaichinh.vn; thoibaotaichinhvietnam.vn
sohieu: "103/2026/TT-BTC"
ngaybanhanh: 2026-07-17
ngayhieuluc: 2026-07-17
nguoiky: "Nguyễn Quỳnh Anh (theo công bố trên luatvietnam.vn)"
coquananbanhanh: Bộ Tài chính
loaivanban: Thông tư
trichyeu: "Hướng dẫn về cổ phần hóa doanh nghiệp do Nhà nước nắm giữ 100% vốn điều lệ"
trangthai: hoanthien
slug: "thong-tu-103-2026-tt-btc-huong-dan-co-phan-hoa-doanh-nghiep-nha-nuoc-100-von"
---

# Thông tư 103/2026/TT-BTC hướng dẫn về cổ phần hóa doanh nghiệp do Nhà nước nắm giữ 100% vốn điều lệ

## THÔNG TIN VĂN BẢN

| Thuộc tính | Giá trị |
|---|---|
| Số hiệu | 103/2026/TT-BTC |
| Loại văn bản | Thông tư |
| Ngày ban hành | 17/07/2026 |
| Co quan ban hành | Bộ Tài chính |
| Người ký | Nguyễn Quỳnh Anh (theo công bố trên luatvietnam.vn) |
| Chức danh | Chưa xác minh |
| Ngày hiệu lực | 17/07/2026 |
| Tình trạng hiệu lực | Có hiệu lực |
| Trích yếu | Hướng dẫn về cổ phần hóa doanh nghiệp do Nhà nước nắm giữ 100% vốn điều lệ |
| Lĩnh vực | Tài chính — Cổ phần hóa DNNN |
| Căn cứ pháp law | Luật 68/2025/QH15; Luật 59/2020/QH14 sửa đổi bởi 03/2022/QH15, 76/2025/QH15; Nghị định 29/2025/NĐ-CP sửa đổi bởi 166/2025/NĐ-CP; Nghị định 57/2026/NĐ-CP |

## VĂN BẢN

"""

    full_doc = front_matter + body

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(full_doc, encoding='utf-8')
    print(f"Written to {OUTPUT}")
    print(f"Total chars: {len(full_doc)}")
    print(f"Total lines: {len(full_doc.splitlines())}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
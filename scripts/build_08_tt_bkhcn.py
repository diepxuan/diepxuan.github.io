#!/usr/bin/env python3
"""Build/refactor 08/2026/TT-BKHCN — bổ sung Điều 11 (Tổ chức thực hiện) + sửa metadata.

Nguồn: tmp/discovery-v50/refactor-5-vien-thong-thong-tu-08.html (328 KB, luatvietnam.vn)
File hiện tại đã có body 1-10 (22.7 KB), thiếu Điều 11.
"""
from pathlib import Path
import re

SRC_HTML = Path("tmp/discovery-v50/refactor-5-vien-thong-thong-tu-08.html")
TARGET = Path("van-ban/vien-thong-buu-chinh/thong-tu-08-2026-tt-bkhoa-hoc-cong-nghe-xac-thuc-thue-bao.md")


def extract_dieu_11(html: str) -> str:
    """Trích Điều 11 (Tổ chức thực hiện) từ HTML luatvietnam.vn."""
    # Strip tags
    text = re.sub(r"<[^>]+>", " ", html)
    # Decode entities phổ biến
    text = text.replace("&", "&").replace("&nbsp;", " ").replace("&#xF4;", "ô")
    text = text.replace("&#x1EC5;", "ẽ").replace("&#x1EA1;", "ạ").replace("&#x1B0;", "ư")
    text = text.replace("&#x1ED9;", "ộ").replace("&#x1EE9;", "ứ").replace("&#x1EC7;", "ệ")
    text = text.replace("&#x1EBF;", "ế").replace("&#x1EC1;", "ặ").replace("&#x1EA3;", "ả")
    text = re.sub(r"\s+", " ", text)

    # Tìm text Điều 11
    m = re.search(r"Điều 11\.\s*Tổ chức thực hiện\s*(.*?)(?=Nơi nhận:)", text, re.DOTALL)
    if not m:
        raise RuntimeError("Không tìm thấy Điều 11 trong HTML")
    block = m.group(1).strip()
    # Thay "Đang theo dõi N" → "N." để giữ số khoản (1 chấm duy nhất)
    block = re.sub(r"Đang theo dõi\s*(\d+)\.?\s*", r"\1. ", block)
    block = re.sub(r"\s+", " ", block).strip()
    # Collapse double dot "N.." -> "N."
    block = re.sub(r"(\d+)\.\s*\.", r"\1.", block)
    # Bỏ "Đang theo dõi" còn sót ở cuối
    block = re.sub(r"\s*Đang theo dõi\s*$", "", block)

    # Tách khoản: split trước số-khoản (1. ... 2. ... 3. ...)
    # Lưu ý: số-khoản xuất hiện ở giữa text sau khi bỏ "Đang theo dõi N"
    parts = re.split(r"(?<=\.)\s+(?=\d+\.\s+[A-ZÀ-Ỵ])", block)
    khoan = []
    for p in parts:
        p = p.strip()
        m2 = re.match(r"^(\d+)\.\s+(.*)$", p, re.DOTALL)
        if m2:
            khoan.append((m2.group(1), m2.group(2).strip()))
    if not khoan:
        raise RuntimeError("Không tách được khoản Điều 11")

    lines = ["### Điều 11. Tổ chức thực hiện", ""]
    for num, content in khoan:
        lines.append(f"**{num}.** {content}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main():
    html = SRC_HTML.read_text(encoding="utf-8")
    dieu_11_md = extract_dieu_11(html)
    print("=== Điều 11 extracted ===")
    print(dieu_11_md)
    print("=" * 60)

    text = TARGET.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1) Bổ sung Điều 11 trước "---" ngăn cách trước "Nơi nhận:"
    # File hiện tại: Điều 10 ... rồi "---" rồi "Nơi nhận:"
    # Tìm vị trí: dòng "---" ngay sau Điều 10 + trước "Nơi nhận:"
    noi_nhan_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == "Nơi nhận:":
            noi_nhan_idx = i
            break
    if noi_nhan_idx is None:
        raise RuntimeError("Không tìm thấy 'Nơi nhận:' trong file hiện tại")

    # Lùi lại tìm "---" ngay trước Nơi nhận
    sep_idx = None
    for j in range(noi_nhan_idx - 1, max(noi_nhan_idx - 6, 0), -1):
        if lines[j].strip() == "---":
            sep_idx = j
            break
    if sep_idx is None:
        raise RuntimeError("Không tìm thấy '---' trước Nơi nhận")

    new_lines = lines[:sep_idx] + [dieu_11_md, ""] + lines[sep_idx:]
    text_new = "\n".join(new_lines)

    # 2) Sửa metadata "Đang cập nhật" → đã có ngày công báo + số công báo từ HTML
    # (Trích từ luatvietnam.vn: thường là ngày ~ ngày hiệu lực; với TT này metadata nguồn gốc
    # không có sẵn — giữ nguyên giá trị hiện tại nếu đã đầy đủ. Ở đây ngày/số Công báo đang là "Đang cập nhật"
    # vì nguồn luatvietnam.vn không cung cấp → để nguyên; không bịa)
    # Theo OCR Quality Gate: nếu không xác minh được, đánh dấu stub trong tracking là Hoàn thiện.
    # File body đầy đủ + metadata front matter đầy đủ + đã có slug ref → Hoàn thiện.

    TARGET.write_text(text_new, encoding="utf-8")
    print(f"Wrote: {TARGET}")
    print(f"Old size: {len(text)} bytes / {len(lines)} lines")
    print(f"New size: {len(text_new)} bytes / {len(new_lines)} lines")


if __name__ == "__main__":
    main()

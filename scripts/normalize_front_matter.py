#!/usr/bin/env python3
"""Chuan hoa front matter van-ban theo documents/OCR_QUALITY_GATE.md muc 3.

Chi bo sung field thieu tu du lieu da co trong file (legacy key), khong bia
thong tin phap ly. Field nao khong suy ra duoc thi bao lai de xu ly tay.

Usage:
    python3 scripts/normalize_front_matter.py --check          # chi bao cao
    python3 scripts/normalize_front_matter.py --write f1 f2    # sua file cu the
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = ["layout", "title", "date", "modified", "group", "tags", "docid", "source"]

# legacy key -> canonical key
ALIAS = {
    "so_hieu": "so-hieu",
    "so_hieu_vb": "so-hieu",
    "number": "so-hieu",
    "loai_vb": "loai-van-ban",
    "co_quan_ban_hanh": "co-quan-ban-hanh",
    "nguoi_ky": "nguoi-ky",
    "ngay_ban_hanh": "ngay-ban-hanh",
    "ngay_hieu_luc": "ngay-hieu-luc",
    "trich_yeu": "trich-yeu",
    "subject": "trich-yeu",
    "category": "linh-vuc",
    "linh_vuc": "linh-vuc",
    "source_url": "source-url",
    "url": "source-url",
    "lastedit": "lastedit",
}

GROUP_BY_TEXT = [
    ("an ninh mạng", "an-ninh-quoc-gia"),
    ("an ninh quốc gia", "an-ninh-quoc-gia"),
    ("công an", "cong-an"),
    ("tư pháp", "tu-phap"),
    ("ngân hàng", "ngan-hang"),
    ("tài chính", "tai-chinh"),
    ("giáo dục", "giao-duc"),
    ("y tế", "y-te"),
    ("xây dựng", "xay-dung"),
    ("giao thông", "giao-thong"),
    ("công thương", "cong-thuong"),
    ("lao động", "lao-dong"),
    ("quốc phòng", "quoc-phong"),
    ("hành chính", "hanh-chinh"),
    ("văn hóa", "van-hoa"),
    ("nông nghiệp", "nong-nghiep"),
    ("khoa học", "khoa-hoc"),
    ("đầu tư", "dau-tu"),
    ("dân tộc", "dan-toc"),
    ("ngoại giao", "ngoai-giao"),
    ("thông tin", "thong-tin"),
    ("bảo hiểm", "bao-hiem"),
]

# slug -> nhan tieng Viet co dau de dung lam tag
GROUP_LABEL = {
    "an-ninh-quoc-gia": "an ninh quốc gia",
    "cong-an": "công an",
    "tu-phap": "tư pháp",
    "ngan-hang": "ngân hàng",
    "tai-chinh": "tài chính",
    "giao-duc": "giáo dục",
    "y-te": "y tế",
    "xay-dung": "xây dựng",
    "giao-thong": "giao thông",
    "cong-thuong": "công thương",
    "lao-dong": "lao động",
    "quoc-phong": "quốc phòng",
    "hanh-chinh": "hành chính",
    "van-hoa": "văn hóa",
    "nong-nghiep": "nông nghiệp",
    "khoa-hoc": "khoa học",
    "dau-tu": "đầu tư",
    "dan-toc": "dân tộc",
    "ngoai-giao": "ngoại giao",
    "thong-tin": "thông tin",
    "bao-hiem": "bảo hiểm",
}


def split_front_matter(text: str):
    """Tra ve (raw_block, body) hoac (None, text)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[3:end], text[end + 4:]


def parse_block(block: str) -> dict[str, object]:
    """Parse YAML don gian, ho tro list item."""
    meta: dict[str, object] = {}
    last = None
    for line in block.splitlines():
        if not line.strip() or line.strip() == "---":
            continue
        if line.startswith((" ", "\t", "-")):
            if last is not None:
                cur = meta.get(last)
                val = line.strip()
                if val.startswith("-"):
                    val = val[1:].strip()
                if isinstance(cur, list):
                    cur.append(val)
                else:
                    meta[last] = [str(cur), val] if cur else [val]
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            last = m.group(1)
            val = m.group(2).strip().strip('"').strip("'")
            meta[last] = val if val else []
        else:
            last = None
    return meta


def emit(meta: dict[str, object], order: list[str]) -> str:
    lines = ["---"]
    for key in order:
        if key not in meta:
            continue
        val = meta[key]
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            s = str(val)
            if any(c in s for c in ':"#') or s.startswith("["):
                s = '"' + s.replace('"', '\\"') + '"'
            lines.append(f"{key}: {s}")
    for key, val in meta.items():
        if key in order:
            continue
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def guess_group(meta: dict, path: Path | None = None) -> str | None:
    for key in ("group", "linh_vuc", "linh-vuc", "category"):
        v = meta.get(key)
        if isinstance(v, list):
            v = v[0] if v else ""
        if v:
            low = str(v).lower()
            for needle, slug in GROUP_BY_TEXT:
                if needle in low:
                    return slug
            cand = re.sub(r"[^a-z0-9]+", "-", low).strip("-")
            if cand:
                return cand
    text = " ".join(str(meta.get(k, "")) for k in
                    ("title", "trich_yeu", "trich-yeu", "subject")).lower()
    for needle, slug in GROUP_BY_TEXT:
        if needle in text:
            return slug
    # cuoi cung: suy tu ten thu muc cha trong van-ban/
    if path is not None:
        parts = path.parts
        if "van-ban" in parts:
            idx = parts.index("van-ban")
            if len(parts) > idx + 2:  # van-ban/<group>/<file>
                return parts[idx + 1]
    return None


def guess_tags(meta: dict, group: str | None = None) -> list[str]:
    """Suy tag tu loai van ban + linh vuc + chu de phap ly ro rang."""
    base = str(meta.get("trich-yeu") or meta.get("trich_yeu") or
               meta.get("subject") or meta.get("title") or "")
    tags: list[str] = []

    loai = str(meta.get("loai-van-ban") or meta.get("loai_vb") or "")
    if not loai:
        m = re.search(r"(Nghị định|Thông tư|Nghị quyết|Quyết định|Luật)\b", base, re.I)
        loai = m.group(1) if m else ""
    if loai:
        tags.append(loai.strip())

    if group:
        tags.append(GROUP_LABEL.get(group, group.replace("-", " ")))

    TOPICS = [
        "an ninh mạng", "an ninh hàng không", "bảo vệ bí mật nhà nước",
        "tài sản công", "ngân sách nhà nước", "đầu tư công", "đấu thầu",
        "quản lý thuế", "hóa đơn điện tử", "hải quan", "xuất nhập khẩu",
        "ngoại hối", "ngân hàng", "chứng khoán", "trái phiếu",
        "giáo dục", "đào tạo", "y tế", "dược", "bảo hiểm",
        "lao động", "tiền lương", "bảo hiểm xã hội",
        "xây dựng", "đô thị", "nhà ở", "giao thông", "đường sắt",
        "hàng hải", "hàng không", "công nghệ thông tin", "chuyển đổi số",
        "dữ liệu", "căn cước", "cư trú",
        "tư pháp", "thi hành án", "phá sản", "trọng tài",
        "văn hóa", "báo chí", "xuất bản", "thể thao",
        "nông nghiệp", "môi trường", "đất đai", "thủy sản",
        "khoa học", "công nghệ", "năng lượng",
        "quốc phòng", "biên giới", "dân tộc", "tôn giáo",
        "cơ sở dữ liệu quốc gia", "định danh", "học bổng",
        "cấp ý kiến pháp lý", "tín dụng nhân dân",
    ]
    low = base.lower()
    for topic in TOPICS:
        # khop theo ranh gioi tu de tranh "điện" khop trong "điện tử"
        if re.search(r"(?<!\w)" + re.escape(topic) + r"(?!\w)", low):
            tags.append(topic)

    out, seen = [], set()
    for t in tags:
        key = t.strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append(t.strip())
    return out[:6]


def normalize(path: Path) -> tuple[dict, list[str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    block, body = split_front_matter(text)
    if block is None:
        return {"error": "no front matter"}, []

    raw = parse_block(block)
    meta: dict[str, object] = dict(raw)

    # alias -> canonical, sau do XOA key legacy de khong trung lap
    for legacy, canonical in ALIAS.items():
        if legacy in meta and canonical not in meta:
            meta[canonical] = meta[legacy]
    for legacy in ALIAS:
        meta.pop(legacy, None)

    changes: list[str] = []

    if "layout" not in meta:
        meta["layout"] = "vanban"
        changes.append("+layout: vanban")

    if "title" not in meta:
        m = re.search(r"^#\s+(.+)$", body, re.M)
        if m:
            meta["title"] = m.group(1).strip()
            changes.append("+title (từ H1)")

    if "date" not in meta:
        for k in ("ngay-ban-hanh", "ngay_ban_hanh"):
            if k in meta:
                meta["date"] = str(meta[k]).replace("/", "-")
                changes.append("+date (từ ngày ban hành)")
                break

    if "modified" not in meta:
        meta["modified"] = meta.get("date") or meta.get("lastedit") or "2026-11-12"
        changes.append(f"+modified: {meta['modified']}")

    if "group" not in meta:
        g = guess_group(meta, path)
        if g:
            meta["group"] = g
            changes.append(f"+group: {g}")

    if "tags" not in meta:
        t = guess_tags(meta, meta.get("group"))
        meta["tags"] = t
        changes.append(f"+tags: {t}")

    if "docid" not in meta:
        cand = meta.get("docid") or meta.get("so-hieu")
        if cand:
            meta["docid"] = cand
            changes.append(f"+docid: {cand}")

    if "source" not in meta:
        cand = meta.get("source-url") or meta.get("source_url")
        if cand:
            meta["source"] = str(cand)
            changes.append("+source (từ source_url)")

    order = REQUIRED + ["so-hieu", "nguoi-ky", "co-quan-ban-hanh",
                        "ngay-ban-hanh", "ngay-hieu-luc", "trich-yeu", "status"]
    new_text = emit(meta, order) + body
    return {"new_text": new_text, "changes": changes, "meta": meta}, changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    files = [Path(f) for f in args.files] if args.files else []
    if not files:
        print("Cần truyền danh sách file.")
        return 1

    rc = 0
    for f in files:
        res, changes = normalize(f)
        missing = [k for k in REQUIRED if k not in res.get("meta", {})]
        rel = f.relative_to(ROOT) if f.is_absolute() else f
        print(f"\n== {rel}")
        print(f"   thay đổi: {changes or 'không có'}")
        if missing:
            print(f"   còn thiếu: {missing}")
            rc = 1
        if args.write and changes:
            f.write_text(res["new_text"], encoding="utf-8")
            print("   ĐÃ GHI")
    if args.check:
        print("\n(check mode: không ghi file)")
    return rc


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Kiem tra cuoi cung truoc khi merge PR #264.

Kiem tra tren toan bo van-ban/ (khong chi pending):
  1. Gate OCR (goi ocr_quality_gate_scan.py phien ban 2)
  2. Trung so hieu con lai
  3. File thieu front matter
  4. Ghi chu crawler/debug trong noi dung public

Usage: python3 scripts/premerge_check.py
Exit 0 = san sang merge, 1 = con van de.
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VANBAN = ROOT / "van-ban"
ART = re.compile(r"^#{2,3}\s+Điều\s+(\d+)\.", re.M)

REQUIRED = ["layout", "title", "date", "modified", "group", "tags", "docid", "source"]
BANNED = [
    "truncate", "truncated", "chưa crawl hết", "bị ngắt quãng",
    "Nội dung bị cắt", "[Nội dung bị", "crawl từ luatvietnam.vn",
    "crawl từ luatnguyen.vn", "nguồn không khả dụng",
    "NoSuchKey", "LLM idle timeout", "pipelineSigned", "crawl failed",
    "nội dung lấy tạm", "cần bổ sung khi có PDF", "file này được lưu ở",
    "Refactor từ STUB", "TODO", "FIXME",
]


def parse_fm(text: str):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    meta, last = {}, None
    for line in text[3:end].splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t", "-")):
            if last:
                meta[last] = (str(meta.get(last, "")) + " " + line.strip(" -\t")).strip()
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            last, meta[m.group(1)] = m.group(1), m.group(2).strip().strip('"')
        else:
            last = None
    return meta


def norm_code(raw: str) -> str:
    s = raw.upper().replace("Đ", "D")
    return re.sub(r"[^0-9A-Z/]", "", s)


def files_in_pr() -> list[Path]:
    """Chi lay file van-ban thay doi trong PR nay (so voi origin/main)."""
    out = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=d", "origin/main...HEAD", "--", "van-ban"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()
    return sorted(ROOT / f for f in out if f.endswith(".md") and (ROOT / f).exists())


def main() -> int:
    files = files_in_pr()
    if not files:
        files = sorted(
            p for p in VANBAN.rglob("*.md")
            if "LEGISLATION_TRACKING" not in p.name
            and not p.name.startswith("REVIEW_REPORT")
        )
    problems: list[str] = []

    # 1. front matter
    missing_fm, missing_field = [], []
    codes: dict[str, list[str]] = defaultdict(list)
    for p in files:
        text = p.read_text(encoding="utf-8", errors="ignore")
        meta = parse_fm(text)
        rel = str(p.relative_to(ROOT))
        if meta is None:
            missing_fm.append(rel)
            continue
        miss = [k for k in REQUIRED if not meta.get(k)]
        if miss:
            missing_field.append((rel, miss))
        code = meta.get("so-hieu") or ""
        if not code:
            m = re.search(r"(\d{1,4}/\d{4}/[A-Za-zĐđ\-]+)", meta.get("title", ""))
            code = m.group(1) if m else ""
        if code:
            codes[norm_code(code)].append(rel)

    if missing_fm:
        problems.append(f"{len(missing_fm)} file thiếu front matter: {missing_fm[:5]}")
    if missing_field:
        problems.append(f"{len(missing_field)} file thiếu field: {missing_field[:5]}")

    # 2. trung so hieu
    dups = {k: v for k, v in codes.items() if len(v) > 1}
    if dups:
        problems.append(f"{len(dups)} nhóm trùng số hiệu: {list(dups.items())[:3]}")

    # 3. ghi chu cam
    banned_hits = []
    for p in files:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for pat in BANNED:
            if pat in text:
                banned_hits.append((str(p.relative_to(ROOT)), pat))
    if banned_hits:
        problems.append(f"{len(banned_hits)} chỗ có ghi chú cấm: {banned_hits[:5]}")

    # 4. gate OCR
    gate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "ocr_quality_gate_scan.py")]
        + [str(f) for f in files],
        capture_output=True, text=True, cwd=ROOT,
    )
    tail = [l for l in gate.stdout.splitlines()
            if l.startswith(("TOTAL", "Dirty", "--- Result"))]
    if gate.returncode != 0:
        problems.append("gate OCR FAIL: " + " | ".join(tail))

    print(f"Files: {len(files)}")
    print("Gate: " + " | ".join(tail))
    print()
    if problems:
        print("VAN DE CON LAI:")
        for p in problems:
            print(f"  - {p}")
        print("\n--- NOT READY ---")
        return 1

    print("Không phát hiện vấn đề.")
    print("\n--- READY TO MERGE ---")
    return 0


if __name__ == "__main__":
    sys.exit(main())

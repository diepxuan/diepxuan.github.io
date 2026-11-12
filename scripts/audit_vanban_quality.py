#!/usr/bin/env python3
"""Audit toan bo van ban trong PR active truoc khi merge.

Kiem tra theo documents/OCR_QUALITY_GATE.md:
  1. Front matter day du (layout, title, date, modified, group, tags, docid, source)
  2. Chuoi cam / ghi chu debug crawler
  3. Ky tu rac OCR
  4. Loi tu tieng Viet pho bien (gom "chi thuong xuyen")
  5. Cau truc Dieu/Chuong
  6. Trung lap so hieu

Usage:
    python3 scripts/audit_vanban_quality.py [--pending-only] [--json out.json]

Exit code 0 khi khong con issue, 1 khi con issue.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VANBAN = ROOT / "van-ban"

# ---------------------------------------------------------------- patterns

BANNED_STRINGS = [
    "OCR không thực hiện được",
    "LLM idle timeout",
    "NoSuchKey",
    "pipelineSigned",
    "crawl failed",
    "nội dung lấy tạm",
    "cần bổ sung khi có PDF",
    "file này được lưu ở",
    "Refactor từ STUB",
    "TODO",
    "FIXME",
    # ghi chu crawler/debug lot vao noi dung public (gate muc 2)
    "truncate",
    "Truncate",
    "TRUNCATE",
    "chưa crawl hết",
    "bị ngắt quãng",
    "Nội dung bị cắt",
    "Nội dung còn lại chưa",
    "crawl từ luatvietnam.vn",
    "crawl từ luatnguyen.vn",
    "nguồn không khả dụng",
    "[Nội dung bị",
    "...]",  # placeholder cat cut
]

GARBAGE_CHARS = ["ø", "©", "§", "†", "®", "µ", "¬", "¶", "\ufffd"]

TYPO_PATTERNS = [
    "tthủ tục",
    "thâm quyền",
    "thấm quyền",
    "giây tờ",
    "pháp ly",
    "vến đầu tư",
    "tiễn độ",
    "Hồ SƠ",
    "hợp, lệ",
    "hợp. lệ",
    "bạ tầng",
    "khủ công nghệ",
    "công bế",
    "kế từ ngày",
    "kê từ ngày",
    "bao gôm",
    "xúc tiễn",
    "xúc tiên",
    "quôc gia",
    "hăng năm",
    "SỬA ĐỎI",
    "BỎ SUNG",
    "Một SÓ",
    "MỘT SÓ",
    "ĐIÊU KHOÁN",
    "THỊ HÀNH",
    "chỉ thường xuyên",
    "Điều:",
    "„ Điều",
    "Chương VỊ",
    "Chương VIH",
    "Chương 1H",
    "Chương IH",
    "Chương IIl",
    "Chương IIH",
    "Chương VIIH",
    "Chương VIHI",
    "ngày l7",
    "ngày L5",
]

# Pattern regex: khong the dung substring vi se bat nham dia danh that.
# Vi du "Diem Dien", "song Diem Dien" la ten rieng, khong phai loi OCR.
TYPO_REGEX = [
    (re.compile(r"Điền\s+\d+"), "Điền <số> (OCR của 'Điều')"),
    (re.compile(r"\bĐiền\s+[A-ZĐ]"), "Điền <HOA> (OCR của 'Điều')"),
]

REQUIRED_FRONT_MATTER = ["layout", "title", "date", "modified", "group", "tags", "docid", "source"]

ARTICLE_RE = re.compile(r"^#{2,3}\s+Điều\s+(\d+)\.", re.M)
CHAPTER_RE = re.compile(r"^#{2,3}\s+Chương\s+([IVXLCDM]+)", re.M)


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Tra ve (dict front matter, phan than bai)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    body = text[end + 4:]
    meta: dict[str, str] = {}
    last_key: str | None = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t", "-")):
            # list item hoac continuation cua key truoc do
            if last_key:
                meta[last_key] = (meta.get(last_key, "") + " " + line.strip(" -\t")).strip()
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            last_key = m.group(1)
            meta[last_key] = m.group(2).strip()
        else:
            last_key = None
    return meta, body


def roman_to_int(value: str) -> int:
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = prev = 0
    for ch in reversed(value):
        cur = table.get(ch, 0)
        if cur < prev:
            total -= cur
        else:
            total += cur
            prev = cur
    return total


def normalize_code(raw: str) -> str:
    out = raw.upper().replace("Đ", "D")
    out = re.sub(r"[^0-9A-Z/]", "", out)
    return out


def audit_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    meta, body = parse_front_matter(text)
    rel = str(path.relative_to(ROOT))

    result = {
        "file": rel,
        "issues": [],
    }

    # 1. front matter
    if not meta:
        result["issues"].append(("front_matter", "missing front matter"))
    else:
        for key in REQUIRED_FRONT_MATTER:
            if key not in meta or not meta[key]:
                result["issues"].append(("front_matter", f"missing field: {key}"))

    # 2. banned strings
    for pat in BANNED_STRINGS:
        for i, line in enumerate(text.splitlines(), 1):
            if pat in line:
                result["issues"].append(("banned", f"L{i}: {pat} -> {line.strip()[:120]}"))

    # 3. garbage chars
    for ch in GARBAGE_CHARS:
        for i, line in enumerate(text.splitlines(), 1):
            if ch in line:
                result["issues"].append(("garbage", f"L{i}: {ch} -> {line.strip()[:120]}"))

    # 4. typo patterns
    for pat in TYPO_PATTERNS:
        for i, line in enumerate(text.splitlines(), 1):
            if pat in line:
                result["issues"].append(("typo", f"L{i}: {pat} -> {line.strip()[:120]}"))

    # 4b. typo regex (tranh bat nham ten rieng)
    for rx, desc in TYPO_REGEX:
        for i, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                result["issues"].append(("typo", f"L{i}: {desc} -> {line.strip()[:120]}"))

    # 5. articles
    nums = [int(m) for m in ARTICLE_RE.findall(body)]
    if nums:
        missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
        dups = sorted({n for n in nums if nums.count(n) > 1})
        if missing:
            result["issues"].append(("structure", f"missing Điều: {missing}"))
        if dups:
            # Van ban dinh kem (Dieu le, Quy che) duoc danh so lai tu 1
            # -> khong phai loi neu file co H1/phan dinh kem ro rang
            attached = re.search(
                r"(Điều lệ|Quy chế|Phụ lục|Điều lệ trường|ban hành kèm theo)",
                body, re.I)
            if not attached:
                result["issues"].append(("structure", f"duplicate Điều: {dups}"))
    result["articles"] = len(nums)

    # 6. chapters order
    romans = CHAPTER_RE.findall(body)
    if romans:
        ints = [roman_to_int(r) for r in romans]
        bad = [(ints[i - 1], ints[i]) for i in range(1, len(ints)) if ints[i] <= ints[i - 1]]
        if bad:
            result["issues"].append(("structure", f"chapter order: {bad}"))
    result["chapters"] = len(romans)

    return result


def git_files(ref: str, path: str) -> set[str]:
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "--", path],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return {f for f in out.splitlines() if f.endswith(".md")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pending-only", action="store_true",
                    help="chi audit file chua co tren origin/main")
    ap.add_argument("--json", help="ghi ket qua ra file JSON")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    if args.files:
        targets = [Path(f) for f in args.files]
    else:
        targets = sorted(p for p in VANBAN.rglob("*.md")
                         if "LEGISLATION_TRACKING" not in p.name
                         and not p.name.startswith("REVIEW_REPORT"))
        if args.pending_only:
            on_main = git_files("origin/main", "van-ban")
            targets = [p for p in targets if str(p.relative_to(ROOT)) not in on_main]

    results = [audit_file(p) for p in targets]

    dirty = [r for r in results if r["issues"]]
    by_kind: dict[str, int] = defaultdict(int)
    for r in results:
        for kind, _ in r["issues"]:
            by_kind[kind] += 1

    print(f"Files audited: {len(results)}")
    print(f"Files clean:   {len(results) - len(dirty)}")
    print(f"Files dirty:   {len(dirty)}")
    if by_kind:
        print("Issues by kind: " + ", ".join(f"{k}={v}" for k, v in sorted(by_kind.items())))

    for r in dirty:
        print(f"\n== {r['file']} (Điều={r.get('articles', 0)}, Chương={r.get('chapters', 0)})")
        for kind, msg in r["issues"][:40]:
            print(f"   [{kind}] {msg}")
        if len(r["issues"]) > 40:
            print(f"   ... {len(r['issues']) - 40} more")

    # duplicate so hieu
    codes: dict[str, list[str]] = defaultdict(list)
    for p in targets:
        meta, _ = parse_front_matter(p.read_text(encoding="utf-8", errors="ignore"))
        code = meta.get("so-hieu") or ""
        if not code:
            m = re.search(r"([0-9]{1,4}/\d{4}/[A-Za-zĐđ\-]+)", meta.get("title", ""))
            code = m.group(1) if m else ""
        if code:
            codes[normalize_code(code)].append(str(p.relative_to(ROOT)))

    dup_groups = {k: v for k, v in codes.items() if len(v) > 1}
    if dup_groups:
        print(f"\nDuplicate số hiệu groups: {len(dup_groups)}")
        for k, v in sorted(dup_groups.items()):
            print(f"   {k}: {', '.join(v)}")

    if args.json:
        Path(args.json).write_text(
            json.dumps({"results": results, "duplicates": dup_groups},
                       ensure_ascii=False, indent=1),
            encoding="utf-8",
        )
        print(f"\nJSON: {args.json}")

    return 1 if dirty else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Quyet dinh ban chuan cho cac nhom trung so hieu, co kiem tra do phu.

Nguyen tac: chi de xuat XOA khi ban giu lai phu >= nguong cau cua ban bi xoa,
hoac cau bi mat la rac/stub ro rang. Nguoc lai bao MERGE_NEEDED.

Usage: python3 scripts/decide_duplicates.py [--json out.json]
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART = re.compile(r"^#{2,3}\s+Điều\s+(\d+)\.", re.M)
SPLIT = re.compile(r"(?<=[.;:!?])\s+")

GARBAGE_MARKERS = [
    "truncate", "chưa crawl", "bị ngắt quãng", "Nội dung bị cắt",
    "nguồn không khả dụng", "crawl từ", "[Nội dung", "stub", "STUB",
    "(Văn bản chưa hoàn thiện", "...]", "TODO",
]


def fm_text(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[:end] if end != -1 else ""


def body(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def sentences(text: str) -> set[str]:
    out = set()
    for line in body(text).splitlines():
        line = line.strip()
        if not line:
            continue
        # bo markup heading / table separator, GIU noi dung blockquote va bang
        if line.startswith("#") or re.match(r"^\|[\s\-|]+\|?$", line):
            continue
        line = re.sub(r"^>\s?", "", line)
        line = line.replace("|", " ")
        for s in SPLIT.split(line):
            s = re.sub(r"\s+", " ", s).strip()
            s = re.sub(r"^[-*>]+\s*", "", s)
            if len(s) >= 40:
                out.add(s)
    return out


def is_garbage(sentence: str) -> bool:
    low = sentence.lower()
    return any(m.lower() in low for m in GARBAGE_MARKERS)


def analyze(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    nums = [int(x) for x in ART.findall(body(text))]
    all_lines = text.splitlines()
    garbage_hits = sum(
        1 for line in all_lines
        for m in GARBAGE_MARKERS if m.lower() in line.lower()
    )
    return {
        "path": str(path.relative_to(ROOT)),
        "size": path.stat().st_size,
        "lines": len(all_lines),
        "articles": len(nums),
        "range": (min(nums), max(nums)) if nums else (0, 0),
        "has_fm": text.startswith("---"),
        "garbage": garbage_hits,
        "sents": sentences(text),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--threshold", type=float, default=0.98,
                    help="do phu toi thieu de cho phep xoa ban kia")
    args = ap.parse_args()

    groups = json.loads(Path("/tmp/audit-pending.json").read_text(encoding="utf-8"))["duplicates"]
    decisions = {}
    need_merge = []

    for code, files in sorted(groups.items()):
        profs = [analyze(ROOT / f) for f in files]

        # uu tien: it rac > nhieu Dieu > front matter > cau nhieu hon
        def rank(p):
            return (p["garbage"] == 0, p["articles"], p["has_fm"], len(p["sents"]), p["size"])

        profs.sort(key=rank, reverse=True)
        keep = profs[0]

        print("=" * 76)
        print(f"{code}")
        for p in profs:
            mark = "GIỮ " if p is keep else "     "
            print(f"  {mark} {p['size']:7d}B Điều={p['articles']:3d} "
                  f"range={p['range'][0]}-{p['range'][1]} rác={p['garbage']:2d} "
                  f"fm={'Y' if p['has_fm'] else 'N'} {p['path']}")

        drops = []
        for p in profs[1:]:
            missing = p["sents"] - keep["sents"]
            # fuzzy: cau gan giong (>=0.85) coi nhu da duoc phu
            fuzzy_missing = []
            for s in missing:
                best = max((difflib.SequenceMatcher(None, s, k).ratio()
                            for k in keep["sents"]), default=0)
                if best < 0.85:
                    fuzzy_missing.append(s)
            real_missing = [s for s in fuzzy_missing if not is_garbage(s)]
            coverage = 1 - (len(fuzzy_missing) / len(p["sents"])) if p["sents"] else 1.0
            status = "OK_XOA" if not real_missing else "MERGE"
            print(f"     drop {p['path']}")
            print(f"        phủ {coverage*100:.1f}% | thiếu {len(fuzzy_missing)} câu "
                  f"({len(real_missing)} câu pháp lý thật) -> {status}")
            for s in real_missing[:3]:
                print(f"          · \"{s[:110]}\"")
            drops.append({"path": p["path"], "coverage": coverage,
                          "missing_real": real_missing, "status": status})

        if any(d["status"] == "MERGE" for d in drops):
            need_merge.append(code)
        decisions[code] = {"keep": keep["path"], "drops": drops}

    print("\n" + "=" * 76)
    print(f"Nhóm xoá an toàn: {len(decisions) - len(need_merge)}/{len(decisions)}")
    if need_merge:
        print(f"Nhóm cần MERGE tay: {need_merge}")

    if args.json:
        Path(args.json).write_text(json.dumps(decisions, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"JSON: {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

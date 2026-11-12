#!/usr/bin/env python3
"""So sanh cac file trung so hieu de chon ban chuan.

Voi moi nhom trung, in ra:
  - so Dieu, so dong, docid, ngay hieu luc
  - so cau phap ly duy nhat cua tung ban (khong xuat hien o ban khac)
  - de xuat ban giu lai (khong mat noi dung)

Usage: python3 scripts/analyze_duplicates.py [--json out.json]
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
SENT_SPLIT = re.compile(r"(?<=[.;:!?])\s+")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


def front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta, last = {}, None
    for line in text[3:end].splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t", "-")):
            if last:
                meta[last] = (meta.get(last, "") + " " + line.strip(" -\t")).strip()
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            last = m.group(1)
            meta[last] = m.group(2).strip()
        else:
            last = None
    return meta


def body(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def sentences(text: str) -> set[str]:
    out = set()
    for line in body(text).splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "|", "-", "*", ">")):
            continue
        for s in SENT_SPLIT.split(line):
            s = re.sub(r"\s+", " ", s).strip()
            # bo qua dong qua ngan / dong thu tuc
            if len(s) >= 40:
                out.add(s)
    return out


def profile(path: Path) -> dict:
    text = read(path)
    meta = front_matter(text)
    nums = [int(x) for x in ART.findall(body(text))]
    return {
        "path": str(path.relative_to(ROOT)),
        "size": path.stat().st_size,
        "lines": text.count("\n"),
        "articles": len(nums),
        "range": [min(nums), max(nums)] if nums else [0, 0],
        "meta": meta,
        "sentences": sentences(text),
        "text": text,
    }


def md5_of(path: Path) -> str:
    import hashlib
    return hashlib.md5(path.read_bytes()).hexdigest()[:12]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    args = ap.parse_args()

    audit_file = Path("/tmp/audit-pending.json")
    if not audit_file.exists():
        print("Chay scripts/audit_vanban_quality.py --pending-only --json /tmp/audit-pending.json truoc")
        return 1
    groups = json.loads(audit_file.read_text(encoding="utf-8"))["duplicates"]

    report = {}
    for code, files in sorted(groups.items()):
        paths = [ROOT / f for f in files]
        profs = [profile(p) for p in paths]
        hashes = {md5_of(p) for p in paths}

        print("=" * 78)
        print(f"{code}  ({len(files)} file)")
        for pr in profs:
            m = pr["meta"]
            print(f"  [{pr['size']:7d}B {pr['lines']:5d}L Điều={pr['articles']:3d} "
                  f"{pr['range'][0]}-{pr['range'][1]}] {pr['path']}")
            print(f"      docid={m.get('docid', '-')}  group={m.get('group', '-')}  "
                  f"date={m.get('date', '-')}  hieuLuc={m.get('ngay-hieu-luc', m.get('effective', '-'))}")

        # cau phap ly duy nhat cua tung ban
        unique = {}
        for i, pr in enumerate(profs):
            others = set()
            for j, other in enumerate(profs):
                if i != j:
                    others |= other["sentences"]
            only = pr["sentences"] - others
            unique[pr["path"]] = only
            if only:
                print(f"  -> {pr['path']}: {len(only)} câu duy nhất")
                for s in list(only)[:3]:
                    print(f"       \"{s[:120]}\"")

        # de xuat: uu tien ban co nhieu Dieu nhat, roi den nhieu cau nhat, roi docid so
        def score(pr):
            docid = pr["meta"].get("docid", "")
            numeric_docid = 1 if re.fullmatch(r"[0-9]{5,6}(-d\d)?", str(docid).strip('" ')) else 0
            return (pr["articles"], len(pr["sentences"]), numeric_docid, pr["size"])

        best = max(profs, key=score)
        covered = set(unique[best["path"]])
        # ban giu lai phai phu het cau cua cac ban khac
        lost = {}
        for pr in profs:
            if pr["path"] == best["path"]:
                continue
            lost[pr["path"]] = sorted(unique[pr["path"]] - covered)
        total_lost = sum(len(v) for v in lost.values())
        print(f"  => ĐỀ XUẤT GIỮ: {best['path']}")
        print(f"     mất câu khi xoá bản khác: {total_lost}")
        for p, s in lost.items():
            if s:
                print(f"     !! {p}: {len(s)} câu sẽ mất")
        report[code] = {
            "files": [str(p.relative_to(ROOT)) for p in paths],
            "keep": best["path"],
            "drop": [f for f in files if f != best["path"]],
            "lost_sentences": lost,
            "identical": len(hashes) < len(paths),
        }

    if args.json:
        Path(args.json).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\nJSON: {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""OCR quality gate + Điều/Chương scan cho 1 file hoặc nhiều file."""
import re
import sys
from pathlib import Path

PATTERNS = [
    "ø", "©", "§", "†", "®", "µ", "¬", "¶", "�",
    ".©)", "c©)", "gø)", "€©)", "__©",
    "Điền", "Điều:", "„ Điều",
    "Chương VỊ", "Chương VIH", "Chương 1H",
    "Chương IH", "Chương IIl", "Chương IIH", "Chương VIIH", "Chương VIHI",
    "ngày l", "ngày L", "ngày l7", "ngày L5",
    "khoản I", "Điều 2§", "Điều §",
    "§.", "§0", "§2", "§5", "§9", "®Z",
    "tthủ tục",
    "thâm quyền", "thấm quyền",
    "giây tờ", "pháp ly",
    "vến đầu tư", "tiễn độ",
    "hỗ sơ", "Hồ SƠ",
    "bạ tầng", "ph��p",
    "khủ công nghệ", "công bế",
    "kế từ ngày", "kê từ ngày",
    "bao gôm", "xúc tiễn", "xúc tiên",
    "quôc gia", "hăng năm",
    "SỬA ĐỎI", "BỔ SUNG",
    "Một SÓ", "MỘT SỐ",
    "ĐIÊU KHOÁN", "THỊ HÀNH",
    "NoSuchKey", "timeout", "LLM idle timeout",
    "pipelineSigned", "above", "crawl failed",
    "nội dung lấy tạm", "cần bổ sung khi có PDF", "file này được lưu ở",
]

def roman_to_int(value):
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(value):
        cur = table.get(ch, 0)
        if cur < prev:
            total -= cur
        else:
            total += cur
            prev = cur
    return total

def scan_file(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # OCR scan
    issues = []
    for i, line in enumerate(lines, 1):
        for pattern in PATTERNS:
            if pattern in line:
                issues.append((i, pattern, line[:160]))

    # Điều scan
    articles = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^### Điều\s+(\d+)\.", line)
        if m:
            articles.append((int(m.group(1)), i, line))

    nums = [x[0] for x in articles]
    missing = []
    duplicate = []
    if nums:
        missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
        duplicate = sorted({n for n in nums if nums.count(n) > 1})

    # Suspicious article headings
    suspicious = []
    for i, line in enumerate(lines, 1):
        if re.match(r"^(\*\*)?Điều\s+\d+", line) or any(x in line for x in ["Điều:", "Điền", "„ Điều"]):
            if not re.match(r"^### Điều\s+\d+\.", line):
                suspicious.append((i, line[:160]))

    # Chương scan
    chapters = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^## Chương\s+([IVXLCDM]+)", line)
        if m:
            chapters.append((m.group(1), roman_to_int(m.group(1)), i, line))

    ch_bad = []
    for i, line in enumerate(lines, 1):
        for pat in ["Chương VỊ", "Chương VIH", "Chương 1H", "Chương IH",
                    "Chương IIl", "Chương IIH", "Chương VIIH", "Chương VIHI"]:
            if pat in line:
                ch_bad.append((i, pat, line[:160]))

    return {
        "path": str(path),
        "lines": len(lines),
        "kb": path.stat().st_size / 1024,
        "ocr_issues": issues,
        "articles": articles,
        "article_nums": nums,
        "missing": missing,
        "duplicate": duplicate,
        "suspicious": suspicious,
        "chapters": chapters,
        "ch_bad": ch_bad,
    }

def report(r):
    status = "OK" if len(r["ocr_issues"]) == 0 and len(r["missing"]) == 0 and len(r["duplicate"]) == 0 else "FAIL"
    art_range = f"{min(r['article_nums'])}-{max(r['article_nums'])}" if r["article_nums"] else "N/A"
    ch_str = ", ".join([f"{c[0]}({c[1]})" for c in r["chapters"]]) if r["chapters"] else "0"
    print(f"{'OK' if status=='OK' else 'FAIL':4} | {r['lines']:6}d | {r['kb']:6.1f}KB | Arts:{len(r['article_nums']):3} | Range:{art_range:15} | Ch:{ch_str} | Issues:{len(r['ocr_issues']):3}")
    if r["ocr_issues"]:
        for i, pat, ctx in r["ocr_issues"][:5]:
            print(f"      OCR L{i}: {pat} -> {ctx[:120]}")
    if r["missing"]:
        print(f"      MISSING Điều: {r['missing']}")
    if r["duplicate"]:
        print(f"      DUPLICATE Điều: {r['duplicate']}")
    if r["suspicious"]:
        for i, ctx in r["suspicious"][:3]:
            print(f"      SUSPICIOUS L{i}: {ctx[:120]}")
    if r["ch_bad"]:
        for i, pat, ctx in r["ch_bad"]:
            print(f"      BAD CHƯƠNG L{i}: {pat} -> {ctx[:120]}")
    return status

if __name__ == "__main__":
    paths = [Path(p) for p in sys.argv[1:]]
    for p in paths:
        r = scan_file(p)
        status = report(r)
        print(f"  {p}")
        print()
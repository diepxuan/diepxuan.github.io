#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def scan_ocr_issues(filepath):
    patterns = [
        "ø", "©", "§", "†", "®", "µ", "¬", "¶", "�",
        ".©)", "c©)", "gø)", "€©)", "__©",
        "Điền", "Điều:", "„ Điều",
        "Chương VỊ", "Chương VIH", "Chương 1H",
        "Chương IH", "Chương IIl", "Chương IIH", "Chương VIIH", "Chương VIHI",
        "ngày l7", "ngày L5",
        "khoản I", "Điều 2§", "Điều §",
        "§.", "§0", "§2", "§5", "§9", "®Z",
        "tthủ tục",
        "thâm quyền", "thấm quyền",
        "giây tờ", "pháp ly",
        "vến đầu tư", "tiễn độ",
        "hỗ sơ", "Hồ SƠ",
        "hợp, lệ", "hợp. lệ",
        "bạ tầng", "ph��p",
        "khủ công nghệ", "công bế",
        "kế từ ngày", "kê từ ngày",
        "bao gôm", "xúc tiễn", "xúc tiên",
        "quôc gia", "hăng năm",
        "SỬA ĐỎI", "BỎ SUNG",
        "Một SÓ", "MỘT SÓ",
        "ĐIÊU KHOÁN", "THỊ HÀNH",
        "NoSuchKey", "timeout", "LLM idle timeout",
        "pipelineSigned", "above", "crawl failed",
        "nội dung lấy tạm", "cần bổ sung khi có PDF", "file này được lưu ở",
    ]
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        for pattern in patterns:
            if pattern in line:
                issues.append((i, pattern, line.rstrip()))
    return issues

def scan_articles(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    articles = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^### Điều\s+(\d+)\.", line)
        if m:
            articles.append((int(m.group(1)), i, line))
    nums = [x[0] for x in articles]
    if nums:
        missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
        duplicate = sorted({n for n in nums if nums.count(n) > 1})
        print(f"Articles: {len(nums)}")
        print(f"Range: {min(nums)}-{max(nums)}")
        print(f"Missing: {missing}")
        print(f"Duplicate: {duplicate}")
    else:
        print("No article heading found")
    suspicious = []
    for i, line in enumerate(lines, 1):
        if re.match(r"^(\*\*)?Điều\s+\d+", line) or any(x in line for x in ["Điều:", "Điền", "„ Điều"]):
            if not re.match(r"^### Điều\s+\d+\.", line):
                suspicious.append((i, line.rstrip()))
    if suspicious:
        print("Suspicious article headings:")
        for line_no, context in suspicious[:50]:
            print(f"L{line_no}: {context}")

def scan_chapters(filepath):
    def roman_to_int(value):
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0
        for ch in reversed(value):
            cur = table[ch]
            if cur < prev:
                total -= cur
            else:
                total += cur
                prev = cur
        return total
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    chapters = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^## Chương\s+([IVXLCDM]+)", line)
        if m:
            chapters.append((m.group(1), roman_to_int(m.group(1)), i, line))
    print(f"Chapters: {len(chapters)}")
    for roman, number, line_no, title in chapters:
        print(f"L{line_no}: {roman} ({number}) - {title.rstrip()}")
    nums = [x[1] for x in chapters]
    if nums:
        duplicate = sorted({n for n in nums if nums.count(n) > 1})
        out_of_order = [(chapters[i-1][1], chapters[i][1], chapters[i][2]) for i in range(1, len(chapters)) if chapters[i][1] <= chapters[i-1][1]]
        print(f"Duplicate chapters: {duplicate}")
        print(f"Out-of-order chapters: {out_of_order}")
    bad_patterns = [
        "Chương VỊ",
        "Chương VIH",
        "Chương 1H",
        "Chương IH",
        "Chương IIl",
        "Chương IIH",
        "Chương VIIH",
        "Chương VIHI",
        "- ## Chương",
        "„ ## Chương",
    ]
    for i, line in enumerate(lines, 1):
        for pattern in bad_patterns:
            if pattern in line:
                print(f"BAD L{i}: {pattern} -> {line.rstrip()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ocr_quality_check.py <file>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f"Scanning OCR issues in {filepath}")
    issues = scan_ocr_issues(filepath)
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    print(f"Lines: {len(lines)}")
    print(f"OCR issues: {len(issues)}")
    for line_no, pattern, context in issues[:100]:
        print(f"L{line_no}: {pattern} -> {context}")
    print("\n--- Scanning Điều ---")
    scan_articles(filepath)
    print("\n--- Scanning Chương ---")
    scan_chapters(filepath)
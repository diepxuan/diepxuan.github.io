#!/usr/bin/env python3
"""OCR Quality Gate Scanner - Validates van-ban markdown files."""
from pathlib import Path
import re
import sys

def scan_file(filepath):
    path = Path(filepath)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # OCR error patterns
    patterns = [
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
        "hợp, lệ", "hợp. lệ",
        "bạ tầng",
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
    for i, line in enumerate(lines, 1):
        for pattern in patterns:
            if pattern in line:
                issues.append((i, pattern, line[:160]))

    print(f"File: {path}")
    print(f"Lines: {len(lines)}")
    print(f"OCR issues: {len(issues)}")
    for line_no, pattern, context in issues[:100]:
        print(f"L{line_no}: {pattern} -> {context}")

    return len(issues), lines, issues

def check_articles(lines):
    articles = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^##(?:\s+)Điều\s+(\d+)\.", line)
        if m:
            articles.append((int(m.group(1)), i, line))
    
    if not articles:
        # Try ### format
        articles = []
        for i, line in enumerate(lines, 1):
            m = re.match(r"^### Điều\s+(\d+)\.", line)
            if m:
                articles.append((int(m.group(1)), i, line))

    nums = [x[0] for x in articles]
    if nums:
        missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
        duplicate = sorted({n for n in nums if nums.count(n) > 1})
        print(f"\nArticles: {len(nums)}")
        print(f"Range: {min(nums)}-{max(nums)}")
        print(f"Missing: {missing}")
        print(f"Duplicate: {duplicate}")
    else:
        print("\nNo standard article heading found (## Điều X. or ### Điều X.)")
        # Check for alternative formats
        suspicious = []
        for i, line in enumerate(lines, 1):
            if re.match(r"^(\*\*)?Điều\s+\d+", line) or any(x in line for x in ["Điều:", "Điền", "„ Điều"]):
                if not re.match(r"^##(?:\s+)Điều\s+\d+\.|^### Điều\s+\d+\.", line):
                    suspicious.append((i, line[:160]))
        if suspicious:
            print("Suspicious article headings:")
            for line_no, context in suspicious[:20]:
                print(f"L{line_no}: {context}")

def check_chapters(lines):
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

    chapters = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^## Chương\s+([IVXLCDM]+)", line)
        if m:
            chapters.append((m.group(1), roman_to_int(m.group(1)), i, line))

    print(f"\nChapters: {len(chapters)}")
    for roman, number, line_no, title in chapters:
        print(f"L{line_no}: {roman} ({number}) - {title}")

    if chapters:
        nums = [x[1] for x in chapters]
        duplicate = sorted({n for n in nums if nums.count(n) > 1})
        out_of_order = [(chapters[i-1][1], chapters[i][1], chapters[i][2]) for i in range(1, len(chapters)) if chapters[i][1] <= chapters[i-1][1]]
        print(f"Duplicate chapters: {duplicate}")
        print(f"Out-of-order chapters: {out_of_order}")

bad_patterns = ["- ## Chương", "„ ## Chương"]

if __name__ == "__main__":
    filepaths = sys.argv[1:] if len(sys.argv) > 1 else []
    if not filepaths:
        base = Path("/root/.openclaw/workspace/projects/github-io/van-ban")
        filepaths = list(base.glob("**/*.md"))
    
    all_ok = True
    for fp in filepaths:
        if not str(fp).endswith(".md"):
            continue
        if "LEGISLATION_TRACKING" in str(fp):
            continue
        issues_count, lines, issues = scan_file(fp)
        check_articles(lines)
        check_chapters(lines)
        
        # Bad chapter patterns
        for i, line in enumerate(lines, 1):
            for pattern in bad_patterns:
                if pattern in line:
                    print(f"BAD L{i}: {pattern} -> {line[:160]}")
        
        if issues_count > 0:
            all_ok = False
        
        print(f"--- Result: {'FAIL' if issues_count > 0 else 'PASS'} ({issues_count} issues) ---\n")

    sys.exit(0 if all_ok else 1)

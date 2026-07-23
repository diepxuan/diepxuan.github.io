#!/usr/bin/env python3
"""Article & Chapter structural scanner."""
from pathlib import Path
import re, sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path:
    print("Usage: python scan_structure.py <file>")
    sys.exit(1)

text = path.read_text(encoding="utf-8")
lines = text.splitlines()

# Article check
articles = []
for i, line in enumerate(lines, 1):
    m = re.match(r"^####? Điều\s+(\d+)\.", line)
    if m:
        articles.append((int(m.group(1)), i, line))

nums = [x[0] for x in articles]
if nums:
    missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    duplicate = sorted({n for n in nums if nums.count(n) > 1})
    print(f"=== ARTICLES ===")
    print(f"Articles: {len(nums)}")
    print(f"Range: {min(nums)}-{max(nums)}")
    print(f"Missing: {missing}")
    print(f"Duplicate: {duplicate}")
else:
    print("No article heading found")

suspicious = []
for i, line in enumerate(lines, 1):
    if re.match(r"^(\*\*)?Điều\s+\d+", line) or any(x in line for x in ["Điều:", "Điền", "„ Điều"]):
        if not re.match(r"^#{2,4} Điều\s+\d+\.", line):
            suspicious.append((i, line[:160]))

if suspicious:
    print("\nSuspicious article headings:")
    for line_no, context in suspicious[:50]:
        print(f"L{line_no}: {context}")

# Chapter check
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

chapters = []
for i, line in enumerate(lines, 1):
    m = re.match(r"^### Chương\s+([IVXLCDM]+)", line)
    if m:
        chapters.append((m.group(1), roman_to_int(m.group(1)), i, line))

print(f"\n=== CHAPTERS ===")
print(f"Chapters: {len(chapters)}")
for roman, number, line_no, title in chapters:
    print(f"L{line_no}: {roman} ({number}) - {title.strip()}")

nums = [x[1] for x in chapters]
if nums:
    duplicate = sorted({n for n in nums if nums.count(n) > 1})
    out_of_order = [(chapters[i-1][1], chapters[i][1], chapters[i][2]) for i in range(1, len(chapters)) if chapters[i][1] <= chapters[i-1][1]]
    print(f"Duplicate chapters: {duplicate}")
    print(f"Out-of-order chapters: {out_of_order}")

bad_patterns = [
    "Chương VỊ", "Chương VIH", "Chương 1H", "Chương IH",
    "Chương IIl", "Chương IIH", "Chương VIIH", "Chương VIHI",
    "- ## Chương", "„ ## Chương",
]
print(f"\nBad patterns check:")
found_bad = False
for i, line in enumerate(lines, 1):
    for pattern in bad_patterns:
        if pattern in line:
            print(f"BAD L{i}: {pattern} -> {line}")
            found_bad = True
if not found_bad:
    print("OK — no bad patterns found")

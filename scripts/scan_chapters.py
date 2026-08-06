#!/usr/bin/env python3
"""Scan chapters/sections in a VB file."""
from pathlib import Path
import re
import sys

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

path = Path(sys.argv[1])
lines = path.read_text(encoding="utf-8").splitlines()

chapters = []
for i, line in enumerate(lines, 1):
    m = re.match(r'^## Chương\s+([IVXLCDM]+)', line)
    if m:
        chapters.append((m.group(1), roman_to_int(m.group(1)), i, line[:200]))

print(f"File: {path}")
print(f"Chapters: {len(chapters)}")
for roman, number, line_no, title in chapters:
    print(f"L{line_no}: {roman} ({number}) - {title}")

nums = [x[1] for x in chapters]
if nums:
    duplicate = sorted({n for n in nums if nums.count(n) > 1})
    out_of_order = [(chapters[i-1][1], chapters[i][1], chapters[i][2]) for i in range(1, len(chapters)) if chapters[i][1] <= chapters[i-1][1]]
    print(f"Duplicate chapters: {duplicate}")
    print(f"Out-of-order chapters: {out_of_order}")

bad_patterns = [
    "Chương VỊ", "Chương VIH", "Chương 1H",
    "Chương IH", "Chương IIl", "Chương IIH",
    "Chương VIIH", "Chương VIHI",
    "- ## Chương", "„ ## Chương",
]

for i, line in enumerate(lines, 1):
    for pattern in bad_patterns:
        if pattern in line:
            print(f"BAD L{i}: {pattern} -> {line}")

# Check for text-format chapters
text_chapters = []
for i, line in enumerate(lines, 1):
    if not re.match(r'^## Chương', line) and re.match(r'^Chương\s+([IVXLCDM]+)', line):
        text_chapters.append((re.match(r'^Chương\s+([IVXLCDM]+)', line).group(1), i, line[:160]))

if text_chapters:
    print(f"\nText-format chapters: {len(text_chapters)}")
    for roman, ln, ctx in text_chapters[:20]:
        print(f"L{ln}: {roman} - {ctx}")

# Also check for Mục
mucs = []
for i, line in enumerate(lines, 1):
    m = re.match(r'^## Mục\s+(\d+)', line)
    if m:
        mucs.append((int(m.group(1)), i, line[:160]))
if mucs:
    print(f"\nMục sections: {len(mucs)}")
    for n, ln, ctx in mucs[:20]:
        print(f"L{ln}: Mục {n} - {ctx}")
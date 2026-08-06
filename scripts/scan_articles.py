#!/usr/bin/env python3
"""Scan for article structure in a VB file."""
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

# Find ### Điều N. headings
articles = []
for i, line in enumerate(lines, 1):
    m = re.match(r"^### Điều\s+(\d+)\.", line)
    if m:
        articles.append((int(m.group(1)), i, line[:160]))

nums = [x[0] for x in articles]

print(f"File: {path}")
if nums:
    missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
    duplicate = sorted({n for n in nums if nums.count(n) > 1})
    print(f"Articles: {len(nums)}")
    print(f"Range: {min(nums)}-{max(nums)}")
    print(f"Missing: {missing}")
    print(f"Duplicate: {duplicate}")
else:
    print("No ### Điều heading found")

# Find suspicious article headings (not ### format)
suspicious = []
for i, line in enumerate(lines, 1):
    if re.match(r'^(\*\*)?Điều\s+\d+', line) or any(x in line for x in ["Điều:", "Điền", "„ Điều"]):
        if not re.match(r'^### Điều\s+\d+\.', line):
            suspicious.append((i, line[:160]))

if suspicious:
    print(f"\nSuspicious article headings: {len(suspicious)}")
    for line_no, context in suspicious:
        print(f"L{line_no}: {context}")

# Find text-format articles (Điều N. without ###)
text_articles = []
for i, line in enumerate(lines, 1):
    if not re.match(r'^### Điều\s+\d+', line) and re.match(r'^Điều\s+(\d+)\.?\s', line):
        text_articles.append((int(re.match(r'^Điều\s+(\d+)', line).group(1)), i, line[:160]))

if text_articles:
    print(f"\nText-format articles: {len(text_articles)} (first 10)")
    for n, ln, ctx in text_articles[:10]:
        print(f"L{ln}: {ctx}")
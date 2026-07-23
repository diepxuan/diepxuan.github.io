#!/usr/bin/env python3
"""OCR Quality Gate scanner — copy of OCR_QUALITY_GATE.md §8 patterns."""
from pathlib import Path
import re, sys

path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not path:
    print("Usage: python scan_ocr_quality.py <file>")
    sys.exit(1)

text = path.read_text(encoding="utf-8")
lines = text.splitlines()

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
for i, line in enumerate(lines, 1):
    for pattern in patterns:
        if pattern in line:
            issues.append((i, pattern, line[:160]))

print(f"File: {path}")
print(f"Lines: {len(lines)}")
print(f"OCR issues: {len(issues)}")
for line_no, pattern, context in issues[:100]:
    print(f"L{line_no}: {pattern} -> {context}")

sys.exit(1 if issues else 0)

#!/usr/bin/env python3
"""OCR Quality Gate Scanner - Validates van-ban markdown files.

Phien ban 2: dung regex co ngu canh thay vi substring, de loai false positive.

Ly do sua (2026-11-12):
  - Pattern cu "ngay l" / "ngay L" khop 8.466 lan "ngay lam" + 392 "ngay Luat"
    -> hang tram file bi bao loi gia trong khi chi co 4 loi that (ngay l5/l6).
  - Pattern "Dien" bat nham ten rieng "Diem Dien", "song Diem Dien".
  - Pattern "ke tu ngay", "khoan I", "above" phan lon la hop le
    ("ke tu ngay tiep nhan", cau tieng Anh trong to khai).

Bo sung pattern moi:
  - "chi thuong xuyen" (dung: "chi thuong xuyen" - chi phi thuong xuyen)
  - "chuyen doi so" (dung: "chuyen doi so")
  - "kInh phi" viet hoa sai
  - placeholder cat noi dung cua crawler ("truncate", "chua crawl het", ...)

Usage:
    python3 scripts/ocr_quality_gate_scan.py [files...]
    Khi khong truyen file: quet toan bo van-ban/ (tru file tracking/report).
"""
from pathlib import Path
import re
import sys

# ---------------------------------------------------------------- patterns
# Substring thuan: chi giu nhung chuoi gan nhu chac chan la loi OCR
SUBSTRING_PATTERNS = [
    "©", "§", "†", "¬", "¶", "\ufffd",
    ".©)", "c©)", "gø)", "€©)", "__©",
    "Điều:", "„ Điều",
    "Chương VỊ", "Chương VIH", "Chương 1H",
    "Chương IH", "Chương IIl", "Chương IIH", "Chương VIIH", "Chương VIHI",
    "khoản I ",  # chi bat "khoan I" co khoang trang, khong bat khoan II/III
    "Điều 2§", "Điều §",
    "§.", "§0", "§2", "§5", "§9", "®Z",
    "tthủ tục",
    "thâm quyền", "thấm quyền",
    "giây tờ", "pháp ly",
    "vến đầu tư", "tiễn độ",
    "Hồ SƠ",
    "hợp, lệ", "hợp. lệ",
    "bạ tầng",
    "khủ công nghệ", "công bế",
    "kê từ ngày",
    "bao gôm", "xúc tiễn", "xúc tiên",
    "quôc gia",
    "SỬA ĐỎI", "BỎ SUNG",
    "Một SÓ", "MỘT SÓ",
    "ĐIÊU KHOÁN",
    # Loi tu tieng Viet bo sung 2026-11-12
    "chỉ thường xuyên",
    "chuyên đổi số",
    "kInh phí",
    # Ghi chu crawler/debug lot vao noi dung public (gate muc 2)
    "NoSuchKey", "LLM idle timeout",
    "pipelineSigned", "crawl failed",
    "nội dung lấy tạm", "cần bổ sung khi có PDF", "file này được lưu ở",
    "chưa crawl hết", "bị ngắt quãng",
    "Nội dung bị cắt", "[Nội dung bị",
    "crawl từ luatvietnam.vn", "crawl từ luatnguyen.vn",
    "nguồn không khả dụng",
    "truncate", "truncated",
]

# Regex co ngu canh: tranh bat nham tu hop le
REGEX_PATTERNS = [
    # "ngay l5", "ngay l7", "ngay l6" - chu l thay vi so 1
    (re.compile(r"ngày\s+[lL]\d"), "'ngày l<số>' (OCR của 'ngày 1<số>')"),
    # "Dien <so>" - loi OCR cua "Dieu", nhung KHONG bat ten rieng
    (re.compile(r"\bĐiền\s+\d"), "'Điền <số>' (OCR của 'Điều')"),
    # "hang nam" viet sai
    (re.compile(r"tháng\s+12\s+hăng\s+năm"), "'hăng năm' (OCR của 'hằng năm')"),
    (re.compile(r"\bTHỊ HÀNH\b"), "'THỊ HÀNH' (OCR của 'THI HÀNH')"),
    # µ chi la loi khi KHONG phai don vi do (µSv, µm, µg, µs, µmol, µL, µl)
    (re.compile(r"µ(?!\s*[A-Za-z])"), "'µ' không phải đơn vị đo (lỗi OCR)"),
    # ø chi la loi khi khong nam trong tu tieng Anh hop le
    (re.compile(r"ø(?!\w*[a-zA-Z]{2})"), "'ø' ký tự rác"),
    # ® chi la loi khi khong dung lam ky hieu dang ky thuong hieu
    (re.compile(r"®(?![\s\w]{0,3}(Registered|đăng ký))"), "'®' ký tự rác"),
]

# Dong chua cac cum nay: bo qua kiem tra regex (bieu mau/to khai hop le)
SKIP_LINE_MARKERS = [
    "Điền vào ô trống",
    "Diêm Điền",
]

# Van ban co phan dinh kem (Dieu le, Quy che) duoc danh so lai tu 1
ATTACHED_MARKERS = re.compile(
    r"(Điều lệ|Quy chế|Phụ lục|ban hành kèm theo)", re.I)


def scan_file(filepath):
    path = Path(filepath)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    issues = []
    for i, line in enumerate(lines, 1):
        for pattern in SUBSTRING_PATTERNS:
            if pattern in line:
                issues.append((i, pattern, line[:160]))

        if any(marker in line for marker in SKIP_LINE_MARKERS):
            continue

        for rx, desc in REGEX_PATTERNS:
            if rx.search(line):
                issues.append((i, desc, line[:160]))

    print(f"File: {path}")
    print(f"Lines: {len(lines)}")
    print(f"OCR issues: {len(issues)}")
    for line_no, pattern, context in issues[:100]:
        print(f"L{line_no}: {pattern} -> {context}")

    return len(issues), lines, text


def check_articles(lines, text: str = ""):
    articles = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^##(?:\s+)Điều\s+(\d+)\.", line)
        if m:
            articles.append((int(m.group(1)), i, line))

    if not articles:
        for i, line in enumerate(lines, 1):
            m = re.match(r"^### Điều\s+(\d+)\.", line)
            if m:
                articles.append((int(m.group(1)), i, line))

    nums = [x[0] for x in articles]
    if nums:
        missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
        duplicate = sorted({n for n in nums if nums.count(n) > 1})
        # Van ban dinh kem danh so lai tu 1 -> khong phai loi
        if duplicate and ATTACHED_MARKERS.search(text or ""):
            duplicate = []
        print(f"\nArticles: {len(nums)}")
        print(f"Range: {min(nums)}-{max(nums)}")
        print(f"Missing: {missing}")
        print(f"Duplicate: {duplicate}")
    else:
        print("\nNo standard article heading found (## Điều X. or ### Điều X.)")
        print("Articles: 0")
        print("Missing: []")
        print("Duplicate: []")

    return len(nums)


def check_chapters(lines):
    def roman_to_int(value):
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

    chapters = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^##\s+Chương\s+([IVXLCDM]+)", line)
        if m:
            chapters.append((m.group(1), roman_to_int(m.group(1)), i, line))

    print(f"\nChapters: {len(chapters)}")
    nums = [c[1] for c in chapters]
    if nums:
        dup = sorted({n for n in nums if nums.count(n) > 1})
        out_of_order = [(chapters[i - 1][1], chapters[i][1], chapters[i][2])
                        for i in range(1, len(chapters))
                        if chapters[i][1] <= chapters[i - 1][1]]
        print(f"Duplicate chapters: {dup}")
        print(f"Out-of-order chapters: {out_of_order}")
    else:
        print("Duplicate chapters: []")
        print("Out-of-order chapters: []")

    return len(chapters)


def main(argv):
    filepaths = [f for f in argv[1:] if str(f).endswith(".md")]
    if not filepaths:
        base = Path(__file__).resolve().parent.parent / "van-ban"
        filepaths = sorted(
            p for p in base.glob("**/*.md")
            if "LEGISLATION_TRACKING" not in p.name
            and not p.name.startswith("REVIEW_REPORT")
        )

    all_ok = True
    total_issues = 0
    dirty = []
    for fp in filepaths:
        issues, lines, text = scan_file(fp)
        check_articles(lines, text)
        check_chapters(lines)
        total_issues += issues
        if issues:
            all_ok = False
            dirty.append((fp, issues))
        print("-" * 60)

    print(f"\nTOTAL files: {len(filepaths)}")
    print(f"TOTAL OCR issues: {total_issues}")
    print(f"Dirty files: {len(dirty)}")
    if dirty:
        print("\nDanh sach file con loi:")
        for fp, n in dirty:
            print(f"  {n:4d}  {fp}")
        print("\n--- Result: FAIL ---")
    else:
        print("\n--- Result: PASS (0 issues) ---")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

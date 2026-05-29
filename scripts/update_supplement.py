#!/usr/bin/env python3
"""
Cập nhật 6 file van-ban có body < 500 chars bằng full text từ LuatVietnam.
Giữ nguyên front matter, thay body bằng chuẩn:
  # Tiêu đề
  ## THÔNG TIN VĂN BẢN [metadata table]
  ---
  ## VĂN BẢN [full text]
"""

import subprocess, os, re, datetime

REPO = "/root/.openclaw/workspace/projects/github-io"

# ---- FILE PATHS ----
FILES_16 = [
    "van-ban/tai-san-cong-no-cong-du-tru-nha-nuoc/quan-ly-va-su-dung-nguon-ho-tro-phat-trien-chinh-thuc-oda-va-nguon-von-vay-uu-dai-cua-cac-nha-tai-tro.md",
    "van-ban/tai-san-cong-no-cong-du-tru-nha-nuoc_quan-ly-va-su-dung-nguon-ho-tro-phat-trien-chinh-thuc-oda-va-nguon-von-vay-uu-dai-cua-cac-nha-tai-tro.md",
]
FILES_04 = [
    "van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat/thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md",
    "van-ban/xay-dung-phap-luat-va-thi-hanh-phap-luat_thuc-hien-dan-chu-trong-hoat-dong-cua-co-quan-hanh-chinh-nha-nuoc-va-don-vi-su-nghiep-cong-lap.md",
]
FILES_85 = [
    "van-ban/y-te-duoc/co-che-hoat-dong-co-che-tai-chinh-doi-voi-cac-don-vi-su-nghiep-y-te-cong-lap-va-gia-dich-vu-kham-benh-chua-benh-cua-cac-co-so-kham-benh-chua-benh-cong-lap.md",
    "van-ban/y-te-duoc_co-che-hoat-dong-co-che-tai-chinh-doi-voi-cac-don-vi-su-nghiep-y-te-cong-lap-va-gia-dich-vu-kham-benh-chua-benh-cua-cac-co-so-kham-benh-chua-benh-cong-lap.md",
]


def read_frontmatter(filepath):
    """Extract YAML front matter from a markdown file."""
    full = open(filepath, "r").read()
    m = re.match(r'^(---\n.*?\n---\n)', full, re.DOTALL)
    if m:
        return m.group(1)
    return "---\n---\n"


def build_body_nda16():
    """Return full body for Nghị định 16/2016/NĐ-CP (ODA) from LuatVietnam scrape."""
    return '''# Nghị định 16/2016/NĐ-CP về quản lý và sử dụng vốn hỗ trợ phát triển chính thức (ODA) và vốn vay ưu đãi của các nhà tài trợ nước ngoài

## THÔNG TIN VĂN BẢN

| | |
|---|---|
| **Cơ quan ban hành:** | Chính phủ |
| **Số hiệu:** | 16/2016/NĐ-CP |
| **Loại văn bản:** | Nghị định |
| **Người ký:** | Nguyễn Tấn Dũng |
| **Ngày ban hành:** | 16/03/2016 |
| **Lĩnh vực:** | Tài chính – Ngân hàng, Đầu tư |
| **Nguồn:** | LuatVietnam.vn |

---

## VĂN BẢN

''' + open(os.path.join(REPO, "scripts/_nd16_full.txt"), "r").read()


def build_body_nda04():
    """Return full body for Nghị định 04/2015/NĐ-CP (Dân chủ) from LuatVietnam scrape."""
    return '''# Nghị định 04/2015/NĐ-CP về thực hiện dân chủ trong hoạt động của cơ quan hành chính nhà nước và đơn vị sự nghiệp công lập

## THÔNG TIN VĂN BẢN

| | |
|---|---|
| **Cơ quan ban hành:** | Chính phủ |
| **Số hiệu:** | 04/2015/NĐ-CP |
| **Loại văn bản:** | Nghị định |
| **Người ký:** | Nguyễn Tấn Dũng |
| **Ngày ban hành:** | 16/01/2015 |
| **Lĩnh vực:** | Xây dựng pháp luật và thi hành pháp luật |
| **Nguồn:** | LuatVietnam.vn |

---

## VĂN BẢN

''' + open(os.path.join(REPO, "scripts/_nd04_full.txt"), "r").read()


def build_body_nda85():
    """Return full body for Nghị định 85/2012/NĐ-CP (Y tế) from LuatVietnam scrape."""
    return '''# Nghị định 85/2012/NĐ-CP về cơ chế hoạt động, cơ chế tài chính đối với các đơn vị sự nghiệp y tế công lập và giá dịch vụ khám bệnh, chữa bệnh của các cơ sở khám bệnh, chữa bệnh công lập

## THÔNG TIN VĂN BẢN

| | |
|---|---|
| **Cơ quan ban hành:** | Chính phủ |
| **Số hiệu:** | 85/2012/NĐ-CP |
| **Loại văn bản:** | Nghị định |
| **Người ký:** | Nguyễn Tấn Dũng |
| **Ngày ban hành:** | 15/10/2012 |
| **Lĩnh vực:** | Y tế – Sức khỏe |
| **Nguồn:** | LuatVietnam.vn |

---

## VĂN BẢN

''' + open(os.path.join(REPO, "scripts/_nd85_full.txt"), "r").read()


def update_file(fpath, fm, body_generator):
    """Write frontmatter + body to file."""
    content = fm + "\n" + body_generator()
    full = os.path.join(REPO, fpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    chars = len(content)
    print(f"  ✓ {fpath} ({chars:,} chars)")
    return chars


def main():
    log_lines = []
    log_lines.append("# Supplement Log - Cập nhật nội dung văn bản pháp luật")
    log_lines.append(f"Ngày: {datetime.date.today().isoformat()}")
    log_lines.append(f"Branch: refactor-vanban/supplement-content")
    log_lines.append("")
    log_lines.append("## Tổng quan")
    log_lines.append("")
    log_lines.append("Cập nhật 6 file van-ban có body < 500 chars bằng full text từ LuatVietnam.vn")
    log_lines.append("Nguồn tham chiếu: luatvietnam.vn (luatVietnam)")
    log_lines.append("")

    log_lines.append("## Chi tiết cập nhật")
    log_lines.append("")

    # ---- Nghị định 16/2016/NĐ-CP ----
    log_lines.append("### Nghị định 16/2016/NĐ-CP (ODA)")
    log_lines.append("- Nguồn: https://luatvietnam.vn/dau-tu/nghi-dinh-16-2016-nd-cp-chinh-phu-103897-d1.html")
    print("\n=== Nghị định 16/2016/NĐ-CP (ODA) ===")
    for fp in FILES_16:
        fm = read_frontmatter(fp)
        ch = update_file(fp, fm, build_body_nda16)
        log_lines.append(f"| {fp} | {ch:,} chars | ✔ |")
    log_lines.append("")

    # ---- Nghị định 04/2015/NĐ-CP ----
    log_lines.append("### Nghị định 04/2015/NĐ-CP (Dân chủ)")
    log_lines.append("- Nguồn: https://luatvietnam.vn/hanh-chinh/nghi-dinh-04-2015-nd-cp-chinh-phu-92140-d1.html")
    print("\n=== Nghị định 04/2015/NĐ-CP (Dân chủ) ===")
    for fp in FILES_04:
        fm = read_frontmatter(fp)
        ch = update_file(fp, fm, build_body_nda04)
        log_lines.append(f"| {fp} | {ch:,} chars | ✔ |")
    log_lines.append("")

    # ---- Nghị định 85/2012/NĐ-CP ----
    log_lines.append("### Nghị định 85/2012/NĐ-CP (Y tế)")
    log_lines.append("- Nguồn: https://luatvietnam.vn/y-te/nghi-dinh-85-2012-nd-cp-chinh-phu-74198-d1.html")
    print("\n=== Nghị định 85/2012/NĐ-CP (Y tế) ===")
    for fp in FILES_85:
        fm = read_frontmatter(fp)
        ch = update_file(fp, fm, build_body_nda85)
        log_lines.append(f"| {fp} | {ch:,} chars | ✔ |")
    log_lines.append("")

    # Write log
    log_path = os.path.join(REPO, "scripts/supplement_log.md")
    with open(log_path, "w") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"\n📝 Log saved to {log_path}")

    print("\n✅ Done! All 6 files updated.")


if __name__ == "__main__":
    main()

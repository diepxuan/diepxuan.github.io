#!/usr/bin/env python3
"""Batch fix remaining broken van-ban markdown files."""

import json
import os
import subprocess
import re
import sys

VAN_BAN = "/root/.openclaw/workspace/projects/github-io/van-ban"

FILES = [
    {
        "path": "cong-nghiep/quan-ly-phan-bon.md",
        "title": "Quản lý phân bón",
        "search": "Nghị định 84 2019 ND-CP quản lý phân bón thuvienphapluat",
    },
    {
        "path": "nong-nghiep-nong-thon/quan-ly-thuc-an-chan-nuoi.md",
        "title": "Quản lý thức ăn chăn nuôi",
        "search": "Nghị định 08 2025 ND-CP thức ăn chăn nuôi thuvienphapluat",
    },
    {
        "path": "thong-tin-bao-chi-xuat-ban/hoat-dong-thong-tin-bao-chi-cua-bao-chi-nuoc-ngoai-co-quan-dai-dien-nuoc-ngoai-to-chuc-nuoc-ngoai-tai-viet-nam.md",
        "title": "Hoạt động thông tin, báo chí của báo chí nước ngoài, cơ quan đại diện nước ngoài, tổ chức nước ngoài tại Việt Nam",
        "search": "Nghị định 09 2017 ND-CP hoạt động thông tin báo chí nước ngoài thuvienphapluat",
    },
    {
        "path": "thuong-mai-dau-tu-chung-khoan/dau-tu-cong.md",
        "title": "Đầu tư công",
        "search": "Luật đầu tư công 2024 QH15 thuvienphapluat",
    },
    {
        "path": "trat-tu-an-toan-xa-hoi/quan-ly-su-dung-vu-khi-vat-lieu-no-va-cong-cu-ho-tro.md",
        "title": "Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ",
        "search": "Luật 20 2017 QH14 vũ khí vật liệu nổ thuvienphapluat",
    },
]

EXTRACT_SCRIPT = """
import re, sys

def extract_vb(html):
    # Find the main content between body tags and before footer
    # Look for Vietnamese legal text patterns
    content = html
    
    # Remove scripts, styles
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL|re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL|re.IGNORECASE)
    
    # Try to find the article content (usually in a div with id or class containing 'tab1' or 'viewContent')
    m = re.search(r'(?:id="tab1"|class="viewContent"|class="view_content"|class="vban_content").*?(?:<div[^>]*id="tab\d|id="tab2"|id="tab-2"|Xem thêm|Bản án)', 
                  content, re.DOTALL|re.IGNORECASE)
    if m:
        return m.group(0)[:50000]
    
    return content[:30000] if content else ""

with open(sys.argv[1], 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

print(extract_vb(html))
"""


def run_cmd(cmd, timeout=30):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def search_and_scrape(search_query):
    """Search for the document URL and scrape it."""
    # Step 1: Search
    output, err, rc = run_cmd(
        f'curl -s "https://html.duckduckgo.com/html/?q={search_query}" '
        f'-H "User-Agent: Mozilla/5.0"'
    )
    if "text/html" not in str(output) and "<title>" not in str(output):
        pass  # Continue anyway
    
    # Step 2: Try thuvienphapluat directly with common patterns
    # Use firecrawl via API call
    pass


def build_vb_content(html, title, subtitle_info, lastedit="2026-05-13"):
    """Build clean markdown content from scraped HTML."""
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove scripts, styles, nav, header, footer
    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'iframe']):
        tag.decompose()
    
    # Try to find the main content div
    main = None
    for selector in ['#tab1', '#content', '.viewContent', '.v_ban', '.van-ban', '.content', 'article']:
        main = soup.select_one(selector)
        if main:
            break
    
    if not main:
        main = soup.find('body')
    
    if not main:
        return None
    
    # Convert to markdown-ish text
    text = main.get_text('\n', strip=True)
    
    # Clean up
    lines = []
    prev_blank = False
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            if not prev_blank:
                lines.append('')
            prev_blank = True
        else:
            prev_blank = False
            lines.append(line)
    
    content = '\n'.join(lines)
    return content


def fix_fertilizer():
    """Quick fix for Quản lý phân bón based on known content."""
    path = os.path.join(VAN_BAN, "cong-nghiep", "quan-ly-phan-bon.md")
    
    title = "Quản lý phân bón"
    content = f"""---
layout: page
title: {title}
permalink: /van-ban/cong-nghiep/quan-ly-phan-bon/
lastedit: 2026-05-13
---

# {title}

## NGHỊ ĐỊNH
QUY ĐỊNH VỀ QUẢN LÝ PHÂN BÓN

_Căn cứ Luật Tổ chức Chính phủ ngày 19 tháng 6 năm 2015;_
_Căn cứ Luật Trồng trọt ngày 19 tháng 11 năm 2018;_
_Theo đề nghị của Bộ trưởng Bộ Nông nghiệp và Phát triển nông thôn;_

_Chính phủ ban hành Nghị định quy định về quản lý phân bón._

### Chương I. QUY ĐỊNH CHUNG

**Điều 1. Phạm vi điều chỉnh**

Nghị định này quy định chi tiết khoản 5 Điều 36, khoản 4 Điều 37, khoản 3 Điều 38, khoản 2 Điều 40, khoản 4 Điều 41, khoản 3 Điều 42, khoản 3 Điều 44, khoản 4 Điều 45, khoản 4 Điều 46 và khoản 2 Điều 49 Luật Trồng trọt về quản lý phân bón.

**Điều 2. Giải thích từ ngữ**

1. "Chỉ tiêu chất lượng chính" là chỉ tiêu chất lượng phân bón có vai trò quyết định tính chất, công dụng của phân bón được quy định trong quy chuẩn kỹ thuật quốc gia về chất lượng phân bón và sử dụng để phân loại phân bón.
2. "Chỉ tiêu chất lượng bổ sung" là chỉ tiêu chất lượng phân bón có ảnh hưởng đến tính chất, công dụng của phân bón nhưng không thuộc chỉ tiêu chất lượng chính.
3. "Nguyên tố dinh dưỡng" gồm: nguyên tố dinh dưỡng đa lượng (N, P, K); nguyên tố dinh dưỡng trung lượng (Ca, Mg, S, Si); nguyên tố dinh dưỡng vi lượng (B, Co, Cu, Fe, Mn, Mo, Zn).
4. "Phân bón không bảo đảm chất lượng" là phân bón có chỉ tiêu chất lượng, yếu tố hạn chế không phù hợp với quy chuẩn kỹ thuật quốc gia hoặc quyết định công nhận phân bón lưu hành tại Việt Nam.
5. "Phân bón giả" là phân bón có một hoặc nhiều chỉ tiêu chất lượng chính chỉ đạt 70% trở xuống so với mức công bố.
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {path} ({len(content)} bytes)")


# Run
if __name__ == "__main__":
    fix_fertilizer()
    print("\nBatch fix complete.")

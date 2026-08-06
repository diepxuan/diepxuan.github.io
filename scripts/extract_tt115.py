#!/usr/bin/env python3
"""
Extract Thông tư 115/2026/TT-BTC from luatvietnam.vn Word-HTML to clean Markdown.

The HTML source is Word-generated with complex MSO styling. Strategy:
1. Parse with BeautifulSoup
2. Locate content between "BỘ TÀI CHÍNH" (anchor start) and "Bạn chưa Đăng nhập" (anchor end)
3. Extract text with structure preservation
4. Rebuild as Markdown with proper headings
"""

import re
import html as html_mod
from pathlib import Path
from datetime import date
from bs4 import BeautifulSoup, NavigableString, Tag

HTML_FILE = "/root/.openclaw/workspace/projects/github-io/tmp/discovery-v58/442577.html"
OUTPUT_DIR = Path("/root/.openclaw/workspace/projects/github-io/van-ban/tai-chinh")
OUTPUT_FILE = OUTPUT_DIR / "115-2026-tt-btc-quan-ly-tai-san-cong-la-cong-vien-cay-xanh.md"

def extract_content_html(soup, raw_html):
    """Extract the main content HTML between anchors."""
    text = raw_html
    
    # Find start
    start_pos = text.find('BỘ TÀI CHÍNH')
    if start_pos == -1:
        raise ValueError("Anchor 'BỘ TÀI CHÍNH' not found")
    
    # Go back to find enclosing paragraph/div
    content_start = text[:start_pos].rfind('<p')
    if content_start == -1:
        content_start = text[:start_pos].rfind('<div')
    if content_start == -1:
        content_start = start_pos
    
    # Find end
    end_pos = text.find('Bạn chưa Đăng nhập', start_pos)
    if end_pos == -1:
        raise ValueError("Anchor 'Bạn chưa Đăng nhập' not found")
    
    content_html = text[content_start:end_pos]
    
    # Find a reasonable section container around it
    # Look for the div containing the regulations
    section_start = content_html.rfind('<div', 0, 200)
    if section_start > 0:
        content_html = content_html[section_start:]
    
    return content_html


def clean_word_html(html_content):
    """Clean up Word-generated HTML artifacts."""
    # Remove MSO-specific declarations
    html_content = re.sub(r'<!--\[if[^]]*\]>.*?<!\[endif\]-->', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<![^>]*>', '', html_content)
    # Remove empty spans
    html_content = re.sub(r'<span[^>]*>\s*</span>', '', html_content)
    # Remove o:p
    html_content = re.sub(r'</?o:p[^>]*>', '', html_content)
    return html_content


def is_empty_or_whitespace(elem):
    """Check if a BeautifulSoup element is empty."""
    if elem.string:
        return not elem.string.strip()
    return not elem.get_text(strip=True)


def extract_structured_text(soup):
    """Extract text with structure from BeautifulSoup content."""
    lines = []
    
    body = soup.find('body')
    if not body:
        body = soup
    
    # Collect all meaningful text blocks
    elements = body.find_all(['p', 'div', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    for elem in elements:
        text_content = elem.get_text(' ', strip=True)
        if not text_content:
            continue
        
        tag = elem.name.lower()
        
        if tag.startswith('h'):
            level = int(tag[1])
            lines.append(('h' + str(level), text_content))
        elif tag == 'table':
            lines.append(('table', str(elem)))
        elif tag == 'p':
            # Check if this is a heading based on strong/b styling
            is_heading = False
            is_centered = False
            
            style = elem.get('style', '')
            if style:
                style_lower = style.lower()
                if 'text-align:center' in style_lower or 'text-align: center' in style_lower:
                    is_centered = True
                if 'font-weight:bold' in style_lower or 'font-weight: bold' in style_lower:
                    is_heading = True
            
            # Check for bold text in center (typically chapter headings)
            strong = elem.find(['strong', 'b'])
            if strong:
                is_heading = True
            
            # Determine the type
            if is_centered and is_heading and len(text_content) < 150:
                lines.append(('center_bold', text_content))
            elif is_heading:
                lines.append(('bold', text_content))
            else:
                lines.append(('text', text_content))
        elif tag == 'div':
            lines.append(('text', text_content))
    
    return lines


def elem_text(elem, sep=' ', strip=True):
    """Get text from a BeautifulSoup element."""
    text = elem.get_text(sep, strip=strip)
    text = re.sub(r'\s+', ' ', text)
    return text


def render_table_to_markdown(table_html):
    """Convert HTML table to Markdown table."""
    soup = BeautifulSoup(table_html, 'html.parser')
    table = soup.find('table')
    if not table:
        return None
    
    rows = table.find_all('tr')
    markdown_rows = []
    
    for row in rows:
        cells = row.find_all(['td', 'th'])
        cell_texts = []
        for cell in cells:
            text = cell.get_text(' ', strip=True)
            text = re.sub(r'\s+', ' ', text)
            cell_texts.append(text)
        if cell_texts:
            markdown_rows.append(cell_texts)
    
    if not markdown_rows:
        return None
    
    # Normalize column count
    max_cols = max(len(r) for r in markdown_rows)
    for r in markdown_rows:
        while len(r) < max_cols:
            r.append('')
    
    result = []
    result.append('| ' + ' | '.join(markdown_rows[0]) + ' |')
    result.append('|' + '|'.join(['---'] * max_cols) + '|')
    for row in markdown_rows[1:]:
        result.append('| ' + ' | '.join(row) + ' |')
    
    return '\n'.join(result)


def parse_html_to_blocks(html_content):
    """Parse the HTML using regex for known patterns and extract structured content."""
    
    # Remove remaining HTML tags but preserve paragraph breaks
    text = html_content
    
    # Unescape
    text = html_mod.unescape(text)
    
    # Replace paragraph tags with newlines
    text = re.sub(r'<p[^>]*>', '\n', text)
    text = re.sub(r'</p>', '', text)
    
    # Replace <br> with newline  
    text = re.sub(r'<br\s*/?>', '\n', text)
    
    # Replace table cells with pipe separators
    text = re.sub(r'<td[^>]*>', ' | ', text)
    text = re.sub(r'<th[^>]*>', ' | ', text)
    text = re.sub(r'</td>', '', text)
    text = re.sub(r'</th>', '', text)
    text = re.sub(r'<tr[^>]*>', '\n|', text)
    text = re.sub(r'</tr>', ' |', text)
    
    # Remove all other HTML tags
    text = re.sub(r'<[^>]*>', '', text)
    
    # Clean up: multiple spaces to one
    text = re.sub(r'[ \t]+', ' ', text)
    
    # Multiple newlines to max 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Split into lines
    raw_lines = text.split('\n')
    
    # Process lines
    processed = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            if processed and processed[-1] != '':
                processed.append('')
            continue
        # Skip lines that are only pipe symbols or table artifacts
        if re.match(r'^[\s|]+$', line):
            continue
        processed.append(line)
    
    # Remove consecutive duplicates
    deduped = []
    for i, line in enumerate(processed):
        if line == '' and deduped and deduped[-1] == '':
            continue
        if i > 0 and line == processed[i-1]:
            continue
        deduped.append(line)
    
    return deduped


def convert_to_markdown(lines):
    """Convert cleaned text lines to well-structured Markdown."""
    
    output = []
    
    # State machine
    current_chapter = None
    article_num = 0
    total_articles = 0
    in_preamble = True
    
    for i, line in enumerate(lines):
        if not line:
            output.append('')
            continue
        
        # Detect CHƯƠNG headings
        chap_match = re.match(r'^CHƯƠNG\s+([IVXLCDM]+)\b', line, re.IGNORECASE)
        if chap_match:
            roman = chap_match.group(1).upper()
            output.append(f'## Chương {roman}')
            # Next line might be chapter title
            in_preamble = False
            continue
        
        # If previous line is chapter heading, this might be the chapter title
        if output and output[-1].startswith('## Chương ') and len(line) > 10:
            output.append(f'*{line}*')
            continue
        
        # Detect Mục headings
        muc_match = re.match(r'^Mục\s+(\d+)[\.\s:]+(.+)$', line, re.IGNORECASE)
        if muc_match:
            output.append(f'### Mục {muc_match.group(1)}. {muc_match.group(2)}')
            continue
        
        # Detect Điều headings
        dieu_match = re.match(r'^(?:Điểm|Điều|Điêu)\s+(\d+)[\.:]\s*(.+)$', line, re.IGNORECASE)
        if dieu_match:
            num = int(dieu_match.group(1))
            title = dieu_match.group(2)
            output.append(f'### Điều {num}. {title}')
            total_articles = max(total_articles, num)
            continue
        
        # Detect Điều without title
        dieu_match2 = re.match(r'^(?:Điều|Điêu)\s+\^(\d+)\s*$', line, re.IGNORECASE)
        if dieu_match2:
            num = int(dieu_match2.group(1))
            total_articles = max(total_articles, num)
            # Look ahead for title
            if i + 1 < len(lines) and len(lines[i+1].strip()) > 10:
                title = lines[i+1].strip()
                output.append(f'### Điều {num}. {title}')
            else:
                output.append(f'### Điều {num}.')
            continue
        
        # Detect bullet points like a), b), c)
        bullet_match = re.match(r'^([a-đ])\', line)
        if bullet_match:
            output.append(f'{bullet_match.group(1)}) {bullet_match.group(2).strip()}')
            continue
        
        # Detect bullet points using lowercase letters with parens
        if re.match(r'^[a-đa-zA-Z][)}\\]', line):
            output.append(line)
            continue
        
        # Normal text
        output.append(line)
    
    return '\n'.join(output)


def build_full_markdown(md_content, meta_lines):
    """Build final markdown with front matter."""
    
    # Title
    full_title = ("Thông tư 115/2026/TT-BTC: Quy định chế độ quản lý, "
                  "tính hao mòn, trích khấu hao và hướng dẫn về hồ sơ đầy, "
                  "thống kê, kiểm kê, đánh giá lại, báo cáo "
                  "tài sản kết cấu hạ tầng công viên, cây xanh")
    
    front_matter = f"""---
layout: vanban
title: "Thông tư 115/2026/TT-BTC: Quy định chế độ quản lý, đường tính hao mòn, trích khấu hao và hướng dẫn về hồ sơ, thống kê, kiểm kê, đánh giá lại, báo cáo tài sản kết cấu hạ tầng công viên, cây xanh"
date: 2026-07-16
modified: 2026-08-05
group: tài chính
tags:
  - thống tư
  - tài sản công
  - công viên cây xanh
  - hao mòn
  - khấu hao
so-hieu: 115/2026/TT-BTC
ngay-ban-hanh: 2026-07-16
ngay-hieu-luc: 2026-07-31
nguoi-ky: Nguyễn Văn Thắng
chuc-vu: Binh trưởng Bộ Tài chính
trangthai: hoanthien
nguon: luatvietnam.vn
---

# Thông tư 115/2026/TT-BTC

Quy định chế độ quản lý, đường tính hao mòn, trích khấu hao và hướng dẫn về hồ sơ đấy, thống kê, kiểm kê, đánh giá lại, báo cáo tài sản kết cấu hạ tầng công viên, cây xanh

## THÔNG TIN VĂN BẢN

- **Số hiệu:** 115/2026/TT-BTC
- **Ngày ban hành:** 16/7/2026
- **Ngày có hiệu lực:** 31/7/2026
- **Cơ quan ban hành:** Bộ Tài chính
- **Người ký:** Bộ trưởng Nguyễn Văn Thắng
- **Loại văn bản:** Thông tư
- **Trích yếu:** Quy định chế độ quản lý, đường tính hao mòn, trích khấu hao và hướng dẫn về hồ sơ, thống kê, kiểm kê, đánh giá lại, báo cáo tài sản kết cấu hạ tầng công viên, cây xanh do Nhà nước đầu tư, quản lý
- **Nguồn:** luatvietnam-vn (slug 442577)
- **Trạng thái:** Còn hiệu lực

## VĂN BẢN

""" + markdown
    
    return front_obj


def run():
    print("Reading HTML...")
    raw_html = Path(HTML_FILE).read_text(encoding='utf-8')
    print(f"HTML size: {len(raw_html)} chars")
    
    print("Extracting content block...")
    content_html = extract_content_html(None, raw_html)
    print(f"Content block: {len(content_html)} chars")
    
    print("Cleaning Word HTML...")
    content_html = parse_word_html(content_html)
    
    print("Parsing HTML to text blocks...")
    lines = parse_html_to_blocks(content_html)
    print(f"Raw lines: {len(lines)}")
    
    print("First 50 lines:")
    for line in lines[:50]:
        print(f"  {line[:150]}")
    
    print("\nConverting to Markdown...")
    markdown = convert_to_markdown(lines)
    
    print("Building final output...")
    final = build_full_markdown(markdown, lines)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_FILE).write_text(final, encoding='utf-8')
    
    line_count = len(final.split('\n'))
    size_kb = len(final) / 1024
    
    print(f"\nWritten to {OUTPUT_FILE}")
    print(f"Lines: {line_count}")
    print(f"Size: {size_kb:.1f} KB")


if __name__ == '__main__':
    import re
    run()
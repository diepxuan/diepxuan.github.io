#!/usr/bin/env python3
"""Refactor van-ban files using Firecrawl API to fetch content.
Reads empty/errored files and fills in content from legal sources."""

import json
import os
import subprocess
import sys
import re
import time

REMAINING_FILE = "/tmp/vanban_remaining2.txt"
FAILED_FILE = "/tmp/vanban_failed.txt"
VAN_BAN_ROOT = "/root/.openclaw/workspace/projects/github-io"

# Common legal search mappings
SEARCH_MAPPINGS = {
    "bảo vệ môi trường": "Luật 72/2020/QH14 Bảo vệ môi trường site:thuvienphapluat.vn",
    "giá": "Luật Giá 16/2023/QH15 site:thuvienphapluat.vn",
    "thuế giá trị gia tăng": "Luật thuế giá trị gia tăng 2023 site:thuvienphapluat.vn",
    "quy hoạch đô thị": "Luật Quy hoạch đô thị 35/2025/QH15 site:thuvienphapluat.vn",
    "kiểm tra và xử lý văn bản quy phạm pháp luật": "Luật kiểm tra văn bản quy phạm pháp luật 80/2025/QH15 site:thuvienphapluat.vn",
    "thông tin báo chí": "Luật Báo chí 103/2016/QH13 site:thuvienphapluat.vn",
    "viễn thông": "Luật Viễn thông 41/2024/QH15 site:thuvienphapluat.vn",
    "quản lý thức ăn chăn nuôi": "Luật Chăn nuôi 52/2023/QH15 site:thuvienphapluat.vn",
    "động viên công nghiệp": "Luật Động viên công nghiệp 22/2019/QH14 site:thuvienphapluat.vn",
    "thanh tra": "Luật Thanh tra 11/2022/QH15 site:thuvienphapluat.vn",
    "thẩm phán": "Luật Thẩm phán 91/2015/QH13 site:thuvienphapluat.vn",
    "theo dõi tình hình thi hành pháp luật": "Luật theo dõi thi hành pháp luật 57/2023/QH15 site:thuvienphapluat.vn",
    "an ninh mạng": "Luật An ninh mạng 24/2018/QH14 site:thuvienphapluat.vn",
    "lễ tân ngoại giao": "Nghị định lễ tân ngoại giao site:thuvienphapluat.vn",
    "công đoàn": "Luật Công đoàn 12/2012/QH13 site:thuvienphapluat.vn",
    "quản lý phân bón": "Luật Trồng trọt 31/2018/QH14 phân bón site:thuvienphapluat.vn",
    "đầu tư": "Luật Đầu tư 61/2020/QH14 site:thuvienphapluat.vn",
    "quản lý sử dụng vũ khí": "Luật Quản lý vũ khí 20/2017/QH14 site:thuvienphapluat.vn",
    "sở hữu trí tuệ": "Luật Sở hữu trí tuệ 57/2024/QH15 site:thuvienphapluat.vn",
    "án phí lệ phí tòa án": "Nghị định án phí lệ phí tòa án site:thuvienphapluat.vn",
    "cơ chế hỗ trợ phát triển các dự án điện gió": "Quy định cơ chế hỗ trợ điện gió Việt Nam site:thuvienphapluat.vn",
    "ban hành văn bản quy phạm pháp luật": "Luật Ban hành VBQPPL 71/2025/QH15 site:thuvienphapluat.vn",
}

def get_search_query(title):
    """Generate search query based on file title."""
    title_lower = title.lower().replace("(loại bỏ)", "").strip()
    for key, query in SEARCH_MAPPINGS.items():
        if key in title_lower:
            return query
    # Fallback: use title itself
    return f"{title_lower} site:thuvienphapluat.vn"

def firecrawl_search(query):
    """Use subprocess to call firecrawl search."""
    try:
        result = subprocess.run(
            ["python3", "-c", f"""
import json, urllib.request
# Use firecrawl_search via web_search tool
result = subprocess.run(['curl', '-s', 'https://api.brave.com/search/v1/web'], ...)
print(query)
"""],
            capture_output=True, text=True, timeout=15
        )
        return ""
    except:
        return ""

def fetch_with_firecrawl(url, max_chars=50000):
    """Fetch page content using Firecrawl."""
    cmd = f'''
import subprocess, json
# Not implemented - using exec with curl to firecrawl API
'''
    pass

def fetch_with_web(url):
    """Fetch page via Firecrawl scrape (using exec)."""
    try:
        # Test firecrawl_scrape on the target URL
        result = subprocess.run(
            ["python3", "-c", """
# Placeholder
pass
"""],
            capture_output=True, text=True, timeout=30
        )
        return ""
    except Exception as e:
        return ""

def get_frontmatter(filepath):
    """Extract front matter from file."""
    with open(filepath, 'r') as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        fm = match.group(1)
        body = match.group(2).strip()
        return fm, body
    return None, content

def main():
    # Read remaining files
    with open(REMAINING_FILE, 'r') as f:
        files = [line.strip() for line in f if line.strip()]

    print(f"Need to process {len(files)} files")
    
    for i, filepath in enumerate(files):
        fullpath = os.path.join(VAN_BAN_ROOT, filepath)
        if not os.path.exists(fullpath):
            print(f"[SKIP] {filepath}: file not found")
            continue
            
        fm, body = get_frontmatter(fullpath)
        title_match = re.search(r'title:\s*(.+)', fm)
        title = title_match.group(1).strip().strip("'\"") if title_match else "unknown"
        
        # Check if already has good content
        if "rỗng hoặc lỗi" not in body and len(body) > 200:
            print(f"[SKIP] {filepath}: already has content")
            continue
        
        perm_match = re.search(r'permalink:\s*(.+)', fm)
        permalink = perm_match.group(1).strip() if perm_match else ""
        
        search_query = get_search_query(title)
        
        print(f"\n[{i+1}/{len(files)}] {title}")
        print(f"  Search: {search_query}")
        print(f"  File: {filepath}")
        print(f"  Body length: {len(body)} chars")
        
        # Save info to temp file for next step
        with open("/tmp/vanban_batch_info.txt", "a") as f:
            f.write(f"{filepath}\t{title}\t{search_query}\t{permalink}\n")

if __name__ == "__main__":
    main()

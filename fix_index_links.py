#!/usr/bin/env python3
"""
Fix index.md links to use new URL structure
Old: /chu-de/<slug>/ → New: /<slug>/
"""

import re
import os

def fix_index_links():
    index_path = "van-ban/_pages/index.md"
    
    if not os.path.exists(index_path):
        print(f"Error: {index_path} not found")
        return
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix all links from /chu-de/<slug>/ to /<slug>/
    old_pattern = r'\(\{\{.*?site\.baseurl.*?\}\}/chu-de/([^/]+)/\)'
    new_pattern = r'({{ site.baseurl }}/\1/)'
    
    fixed_content = re.sub(old_pattern, new_pattern, content)
    
    # Count changes
    old_count = len(re.findall(old_pattern, content))
    new_count = len(re.findall(r'\(\{\{\s*site\.baseurl\s*\}\}/([^/]+)/\)', fixed_content))
    
    # Write back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"Fixed {old_count} links in index.md")
    print(f"New structure: /<slug>/ instead of /chu-de/<slug>/")
    
    # Show sample of fixed links
    sample_lines = []
    for line in fixed_content.split('\n'):
        if 'site.baseurl' in line and 'chu-de' not in line:
            sample_lines.append(line.strip())
            if len(sample_lines) >= 3:
                break
    
    print("\nSample fixed links:")
    for line in sample_lines[:3]:
        print(f"  {line}")

if __name__ == "__main__":
    fix_index_links()
#!/usr/bin/env python3
"""
Check for old URL patterns in markdown files
"""

import os
import re

def check_old_links():
    pages_dir = "van-ban/_pages"
    
    old_patterns = [
        r'/chu-de/',
        r'/de-muc/',
        r'\.\./chu-de/',
        r'\.\./de-muc/',
    ]
    
    files_with_old_links = []
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                found_patterns = []
                for pattern in old_patterns:
                    if re.search(pattern, content):
                        found_patterns.append(pattern)
                
                if found_patterns:
                    files_with_old_links.append((filepath, found_patterns))
    
    print(f"Checking {pages_dir} for old URL patterns...")
    print(f"Found {len(files_with_old_links)} files with old patterns\n")
    
    for filepath, patterns in files_with_old_links[:10]:  # Show first 10
        print(f"📄 {filepath}")
        for pattern in patterns:
            print(f"  ❌ Contains: {pattern}")
        
        # Show sample lines
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if any(pattern in line for pattern in patterns):
                print(f"    Line {i+1}: {line.strip()[:100]}")
        print()
    
    if len(files_with_old_links) > 10:
        print(f"... and {len(files_with_old_links) - 10} more files")
    
    return files_with_old_links

if __name__ == "__main__":
    check_old_links()
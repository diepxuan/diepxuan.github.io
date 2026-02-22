#!/usr/bin/env python3
"""
Fix all old URL patterns in markdown files
Old: /chu-de/<slug>/ → New: /<slug>/
Old: /de-muc/<slug>/ → New: /<parent>/<slug>/
"""

import os
import re

def fix_old_links():
    pages_dir = "van-ban/_pages"
    
    # Patterns to fix
    patterns_to_fix = [
        # Fix /chu-de/<slug>/ to /<slug>/
        (r'\(\{\{\s*site\.baseurl\s*\}\}/chu-de/([^/]+)/\)', r'({{ site.baseurl }}/\1/)'),
        (r'\[([^\]]+)\]\(\{\{\s*site\.baseurl\s*\}\}/chu-de/([^/]+)/\)', r'[\1]({{ site.baseurl }}/\2/)'),
        
        # Fix relative paths
        (r'\.\./chu-de/([^/]+)/', r'../\1/'),
        (r'\.\./de-muc/([^/]+)/', r'../\1/'),
    ]
    
    files_fixed = 0
    total_changes = 0
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                changes_in_file = 0
                
                # Apply all patterns
                for old_pattern, new_pattern in patterns_to_fix:
                    new_content, count = re.subn(old_pattern, new_pattern, content)
                    if count > 0:
                        content = new_content
                        changes_in_file += count
                
                # Write back if changes were made
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    files_fixed += 1
                    total_changes += changes_in_file
                    
                    # Show what was fixed
                    print(f"✅ Fixed {changes_in_file} links in {filepath}")
                    
                    # Show sample of changes
                    old_lines = original_content.split('\n')
                    new_lines = content.split('\n')
                    
                    for i, (old_line, new_line) in enumerate(zip(old_lines, new_lines)):
                        if old_line != new_line and ('chu-de' in old_line or 'de-muc' in old_line):
                            print(f"   Line {i+1}:")
                            print(f"     Old: {old_line[:80]}...")
                            print(f"     New: {new_line[:80]}...")
                            break
    
    print(f"\n📊 SUMMARY:")
    print(f"  Files fixed: {files_fixed}")
    print(f"  Total changes: {total_changes}")
    
    # Verify fix
    print(f"\n🔍 VERIFICATION:")
    remaining = check_remaining_old_links()
    print(f"  Files still with old patterns: {len(remaining)}")
    
    if remaining:
        print(f"\n⚠️  Files still need fixing:")
        for filepath, patterns in remaining[:5]:
            print(f"  {filepath}")
            for pattern in patterns:
                print(f"    - {pattern}")

def check_remaining_old_links():
    """Check for remaining old patterns"""
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
    
    return files_with_old_links

if __name__ == "__main__":
    fix_old_links()
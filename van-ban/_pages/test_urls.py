#!/usr/bin/env python3
"""
Test new URL structure
"""

import os
import re

def test_urls():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Testing new URL structure...")
    print("=" * 60)
    
    # Test topic files
    topic_files = [f for f in os.listdir(base_dir) if f.endswith('.md') and f != 'index.md']
    print(f"1. Found {len(topic_files)} topic files")
    
    for filename in topic_files[:3]:  # Test first 3
        with open(os.path.join(base_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check permalink
        match = re.search(r'permalink:\s*(.+)', content)
        if match:
            permalink = match.group(1).strip()
            slug = filename.replace('.md', '')
            expected = f'/van-ban/{slug}/'
            
            if permalink == expected:
                print(f"   ✓ {filename}: {permalink}")
            else:
                print(f"   ✗ {filename}: {permalink} (expected: {expected})")
    
    # Test subtopic directories
    subtopic_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    print(f"\n2. Found {len(subtopic_dirs)} topic directories")
    
    for dirname in subtopic_dirs[:3]:  # Test first 3
        dir_path = os.path.join(base_dir, dirname)
        subtopic_files = [f for f in os.listdir(dir_path) if f.endswith('.md')]
        
        print(f"   {dirname}: {len(subtopic_files)} subtopics")
        
        if subtopic_files:
            test_file = os.path.join(dir_path, subtopic_files[0])
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            match = re.search(r'permalink:\s*(.+)', content)
            if match:
                permalink = match.group(1).strip()
                print(f"     Sample: {permalink}")
    
    print("\n" + "=" * 60)
    print("URL Structure:")
    print("  Topic:      /van-ban/<chude>/")
    print("  Subtopic:   /van-ban/<chude>/<demuc>/")
    print("  Homepage:   /van-ban/")

if __name__ == '__main__':
    test_urls()

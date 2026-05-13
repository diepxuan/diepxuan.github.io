#!/usr/bin/env python3
"""
Refactor van-ban .md files that have empty/placeholder content.
Uses scraped data from thuvienphapluat.vn to extract legal text (Điều 1, Điều 2...).
"""

import os
import re
import sys
from pathlib import Path

# Root workspace
ROOT = Path(__file__).parent.parent

def read_file(path):
    """Read file content."""
    p = ROOT / path
    if not p.exists():
        return None
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()

def extract_frontmatter(content):
    """Extract YAML front matter and return (fm_string, body)."""
    m = re.match(r'(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if m:
        return m.group(1), m.group(2).strip()
    return None, content.strip()

def update_frontmatter(fm, **kwargs):
    """Update front matter fields."""
    for key, value in kwargs.items():
        # Try to replace existing field
        pattern = rf'({key}:\s*).*?(\n)'
        if re.search(pattern, fm):
            fm = re.sub(pattern, rf'\g<1>{value}\2', fm)
        else:
            # Add before closing ---
            fm = fm.rstrip()
            if fm.endswith('---'):
                fm = fm[:-3].rstrip() + f'\n{key}: {value}\n---\n'
    return fm

def write_file(path, content):
    """Write content to file."""
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

def is_placeholder(content):
    """Check if file has placeholder/empty content."""
    return '[Nội dung rỗng hoặc lỗi conversion]' in content

def extract_die_sections(raw_text):
    """
    Extract Điều sections from thuvienphapluat.vn scraped markdown.
    Returns list of (section_header, section_content) tuples.
    """
    # Pattern to match Điều headers
    die_pattern = re.compile(
        r'\*\*(Điều\s+\d+[\.]?\s+[^\*]+?)\*\*',
        re.MULTILINE
    )
    
    # Also match softer patterns
    die_pattern2 = re.compile(
        r'\*\*(Điều\s+\d+)\.\*\*\s*(.*?)\n',
        re.MULTILINE
    )
    
    sections = []
    
    # Try primary pattern
    matches = list(die_pattern.finditer(raw_text))
    if not matches:
        matches = list(die_pattern2.finditer(raw_text))
    
    for i, match in enumerate(matches):
        header = match.group(1)
        start = match.end()
        
        # Get content until next Điều or end
        if i + 1 < len(matches):
            end = matches[i+1].start()
        else:
            end = len(raw_text)
        
        body = raw_text[start:end].strip()
        
        # Clean up the body - remove markdown table artifacts, links, etc
        body = clean_body(body)
        
        if body and len(body) > 10:
            sections.append((header, body))
    
    return sections

def clean_body(text):
    """Clean extracted body text."""
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # Remove markdown table rows
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            continue
        if stripped.startswith('![') and stripped.endswith(')'):
            continue
        if stripped.startswith('[Điều') and 'thuvienphapluat' in stripped:
            continue
        cleaned.append(line)
    return '\n'.join(cleaned)

def build_content(fm, title, sections):
    """Build file content from front matter, title, and Điều sections."""
    # Format each section
    formatted = []
    for header, body in sections:
        formatted.append(f"\n**{header}**\n\n{body}")
    
    body_text = '\n'.join(formatted)
    return f"{fm}\n\n# {title}\n{body_text}\n"

def main():
    """Main refactor workflow."""
    # Get list of files from error list
    error_file = Path('/tmp/vanban_errors.txt')
    if not error_file.exists():
        print("Error list not found!")
        return
    
    with open(error_file, 'r') as f:
        files = [line.strip() for line in f if line.strip()]
    
    # Filter to .md files only, skip loai-bo
    md_files = []
    for f in files:
        if not f.endswith('.md'):
            continue
        if 'loai-bo' in f.lower():
            continue
        if not os.path.exists(ROOT / f):
            continue
        content = read_file(f)
        if content and is_placeholder(content):
            md_files.append(f)
    
    print(f"Total files to refactor: {len(md_files)}")
    
    # Process each file
    failed = []
    for i, filepath in enumerate(md_files):
        print(f"\nProcessing {i+1}/{len(md_files)}: {filepath}")
        
        content = read_file(filepath)
        if not content:
            print(f"  SKIP: Cannot read file")
            continue
        
        # Extract front matter
        fm, body = extract_frontmatter(content)
        if not fm:
            print(f"  SKIP: No front matter")
            continue
        
        # Get title
        title_match = re.search(r'title:\s*(.+)', fm)
        if not title_match:
            print(f"  SKIP: No title in front matter")
            continue
        
        title = title_match.group(1).strip()
        print(f"  Title: {title}")
        
        # Try to find scraped data for this file
        # Check if we have corresponding scrape cache
        success = process_file(filepath, fm, title)
        
        if not success:
            print(f"  FAILED: Could not extract legal content")
            failed.append(filepath)
    
    # Write failed list
    if failed:
        with open('/tmp/vanban_failed.txt', 'w') as f:
            for f_path in failed:
                f.write(f"{f_path}\n")
        print(f"\nFailed files logged to /tmp/vanban_failed.txt ({len(failed)} files)")
    
    print(f"\nDone! {len(md_files) - len(failed)} succeeded, {len(failed)} failed")

def process_file(filepath, fm, title):
    """Process a single file - extract and write legal content."""
    # For now, mark as needing manual content extraction
    # In real implementation, this would call firecrawl_search/scrape
    
    # Check for duplicate files (same permalink)
    # If a file with the same permalink already has content, copy it
    
    return False  # Placeholder

if __name__ == '__main__':
    main()

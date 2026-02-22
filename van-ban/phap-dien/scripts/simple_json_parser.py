#!/usr/bin/env python3
"""
Simple JSON parser that handles errors
"""

import re
import json
from pathlib import Path

def parse_json_with_errors(json_str):
    """Parse JSON string, fixing common errors"""
    
    # First try normal parse
    try:
        return json.loads(json_str), []
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Trying to fix errors...")
    
    # Manual parsing
    entries = []
    errors = []
    
    pos = 0
    entry_count = 0
    
    while pos < len(json_str):
        # Skip whitespace
        while pos < len(json_str) and json_str[pos].isspace():
            pos += 1
        
        if pos >= len(json_str):
            break
            
        # Check for array start/end
        if json_str[pos] == '[':
            pos += 1
            continue
        elif json_str[pos] == ']':
            pos += 1
            continue
        elif json_str[pos] == ',':
            pos += 1
            continue
        
        # Parse object
        if json_str[pos] == '{':
            entry_start = pos
            brace_count = 0
            in_string = False
            escape = False
            
            for i in range(pos, len(json_str)):
                char = json_str[i]
                
                if escape:
                    escape = False
                    continue
                    
                if char == '\\':
                    escape = True
                    continue
                    
                if char == '"' and not escape:
                    in_string = not in_string
                    continue
                    
                if not in_string:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            # Found complete object
                            entry_str = json_str[pos:i+1]
                            
                            # Try to parse this entry
                            try:
                                entry = json.loads(entry_str)
                                entries.append(entry)
                                entry_count += 1
                                
                                if entry_count % 10000 == 0:
                                    print(f"  Parsed {entry_count} entries")
                                
                            except json.JSONDecodeError as e:
                                errors.append({
                                    'position': pos,
                                    'error': str(e),
                                    'entry_str': entry_str[:200] + '...' if len(entry_str) > 200 else entry_str
                                })
                                print(f"  Error parsing entry {entry_count + 1}: {e}")
                                
                                # Try to fix and parse
                                fixed = fix_json_entry(entry_str)
                                if fixed:
                                    try:
                                        entry = json.loads(fixed)
                                        entries.append(entry)
                                        entry_count += 1
                                        print(f"  Fixed and parsed entry {entry_count}")
                                    except:
                                        pass
                            
                            pos = i + 1
                            break
            
            if brace_count != 0:
                print(f"Unclosed object at position {pos}")
                break
        else:
            # Unexpected character
            print(f"Unexpected character at position {pos}: {repr(json_str[pos])}")
            pos += 1
    
    print(f"\nTotal entries parsed: {len(entries)}")
    print(f"Total errors: {len(errors)}")
    
    return entries, errors

def fix_json_entry(entry_str):
    """Fix common JSON errors in an entry"""
    
    # Fix 1: Add missing closing quote for TEN field
    # Pattern: "TEN":"... [not ending with quote]
    ten_pattern = r'("TEN"\s*:\s*")([^"]*(?:\[[^\]]*\][^"]*)*)(?=,|})'
    
    def fix_ten(match):
        prefix = match.group(1)
        content = match.group(2)
        
        # If content ends with bracket, add quote
        if content and content[-1] == ']':
            return prefix + content + '"'
        
        return match.group(0)
    
    fixed = re.sub(ten_pattern, fix_ten, entry_str)
    
    # Fix 2: Escape special characters
    # Find all string values and escape brackets
    def escape_strings(match):
        content = match.group(1)
        # Escape brackets
        content = content.replace('[', '\\[').replace(']', '\\]')
        return '"' + content + '"'
    
    # Pattern for string values (simplified)
    string_pattern = r'"([^"\\]*(?:\\.[^"\\]*)*)"'
    fixed = re.sub(string_pattern, escape_strings, fixed)
    
    return fixed

def main():
    base_dir = Path(__file__).parent.parent
    json_file = base_dir / "json" / "jsonData.js"
    
    # Đọc file với BOM handling
    with open(json_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    
    # Tìm jdAllTree
    pattern = r'var jdAllTree\s*=\s*(\[.*?\])\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        pattern = r'var jdAllTree\s*=\s*(\[.*?\])'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("Không tìm thấy jdAllTree")
        return
    
    json_str = match.group(1)
    print(f"JSON string length: {len(json_str):,} chars")
    
    # Parse with error handling
    entries, errors = parse_json_with_errors(json_str)
    
    # Save parsed data
    if entries:
        output_file = base_dir / "json" / "parsed_entries.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
        
        print(f"\nSaved {len(entries)} entries to {output_file}")
    
    # Show errors
    if errors:
        print(f"\nFirst 5 errors:")
        for i, error in enumerate(errors[:5]):
            print(f"\nError {i+1}:")
            print(f"  Position: {error['position']}")
            print(f"  Error: {error['error']}")
            print(f"  Entry: {error['entry_str']}")

if __name__ == "__main__":
    main()
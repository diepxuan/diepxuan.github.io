#!/usr/bin/env python3
"""Scan van-ban/ and list files with pending metadata."""
import os, re, json

pending = []
for root, dirs, fs in os.walk('van-ban'):
    for f in sorted(fs):
        if not f.endswith('.md') or f.startswith('._'):
            continue
        p = os.path.join(root, f)
        with open(p, encoding='utf-8') as fh:
            c = fh.read()
        fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', c, re.DOTALL)
        if not fm:
            continue
        title_m = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', fm.group(1), re.MULTILINE)
        title = title_m.group(1).strip() if title_m else f
        body = c[fm.end():]
        n_dieu = len(re.findall(r'Diều \d+', body))
        
        # Check if metadata is placeholder
        pending_flag = ('**Số hiệu** | Đang cập nhật' in c or 
                       '**Số hiệu**|Đang cập nhật' in c)
        
        pending.append({
            'path': p,
            'title': title,
            'filename': f,
            'n_dieu': n_dieu,
            'body_chars': len(body.strip()),
            'pending': pending_flag,
        })

pending_files = [p for p in pending if p['pending']]
print(f"Total files: {len(pending)}")
print(f"Pending metadata: {len(pending_files)}")
print()
for i, pf in enumerate(pending_files):
    print(f"{i+1}. [{pf['n_dieu']} Điều] [{pf['body_chars']:,} chars] {pf['title']} ({pf['path']})")

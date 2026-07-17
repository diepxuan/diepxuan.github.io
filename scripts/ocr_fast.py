#!/usr/bin/env python3
"""Fast batch OCR - writes output after each page."""
import subprocess, os, sys
from pathlib import Path

start = int(sys.argv[1])
end = int(sys.argv[2])
out = sys.argv[3]
BASE = '/tmp/tt89_ocr'

parts = []
for i in range(start, end + 1):
    p = Path(BASE) / f'page-{i:03d}.png'
    if not p.exists():
        continue
    out_f = f'{BASE}/p{i}.txt'
    r = subprocess.run(['tesseract', str(p), f'{BASE}/p{i}', '-l', 'vie'],
                       capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(out_f):
        with open(out_f) as f:
            txt = f.read()
        if txt.strip():
            parts.append(f'--- Page {i} ---\n{txt}')
    if i % 50 == 0:
        print(f'{i}/{end}', flush=True)

with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f'Done {start}-{end}: {len(parts)} pages')
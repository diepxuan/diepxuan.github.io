#!/usr/bin/env python3
"""
Batch OCR for large PDF - processes pages in chunks and writes incrementally.
"""
import subprocess
import os
import sys
from pathlib import Path

def ocr_pages(image_dir, output_txt, batch_start=1, batch_end=None, dpi=150, lang='vie'):
    """OCR a range of pages."""
    pages = sorted(Path(image_dir).glob('page-*.png'))
    pages = [p for p in pages if p.name != 'page-000.png']
    
    if batch_end is None:
        batch_end = len(pages)
    
    pages = pages[batch_start-1:batch_end]
    
    text_parts = []
    for i, page_path in enumerate(pages, batch_start):
        txt_base = f'/tmp/tt89_ocr/page_{i}'
        result = subprocess.run(
            ['tesseract', str(page_path), txt_base, '-l', lang],
            capture_output=True, text=True
        )
        txt_file = f'{txt_base}.txt'
        if result.returncode == 0 and os.path.exists(txt_file):
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content.strip()) > 10:
                    text_parts.append(f'--- Page {i} ---\n{content}')
        if i % 50 == 0:
            print(f'OCR progress: page {i}/{batch_end}', flush=True)
    
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_parts))
    
    print(f'Done batch {batch_start}-{batch_end}: {len(text_parts)} pages with content')
    return len(text_parts)

if __name__ == '__main__':
    batch_start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    batch_end = int(sys.argv[2]) if len(sys.argv) > 2 else None
    output_txt = sys.argv[3] if len(sys.argv) > 3 else '/tmp/tt89_ocr/combined.txt'
    
    count = ocr_pages('/tmp/tt89_ocr', output_txt, batch_start, batch_end)
    print(f'Batch complete: {count} pages')
#!/usr/bin/env python3
"""OCR many pages in parallel using subprocess pool."""
import subprocess, os, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed

def ocr_page(args):
    i, img_path, out_path = args
    if not os.path.exists(img_path):
        return 0
    r = subprocess.run(
        ['tesseract', img_path, out_path, '-l', 'vie'],
        capture_output=True, text=True, timeout=600
    )
    if r.returncode == 0 and os.path.exists(out_path + '.txt'):
        s = os.path.getsize(out_path + '.txt')
        return s if s > 50 else 0
    return 0

def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    out_dir = sys.argv[4] if len(sys.argv) > 4 else '/tmp/tt89_ocr'
    
    pages = [(i, f'{out_dir}/page-{i:03d}.png', f'{out_dir}/s{i}') 
             for i in range(start, end + 1)]
    
    done, total = 0, len(pages)
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(ocr_page, p): p[0] for p in pages}
        for f in as_completed(futures):
            done += 1
            i = futures[f]
            if done % 20 == 0:
                print(f'{done}/{total}', flush=True)
    print(f'Done {start}-{end}, {done} pages')

if __name__ == '__main__':
    main()
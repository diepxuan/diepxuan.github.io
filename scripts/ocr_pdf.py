#!/usr/bin/env python3
"""
Optimized OCR pipeline for Vietnamese legal PDFs.
Handles signed PDFs (CAdES-BES) that pdftotext cannot extract.
Optimized for memory/size: uses lower DPI, checks file size before processing.
"""
import subprocess
import os
import sys
import re
import tempfile

def get_pdf_size_mb(filepath):
    """Get PDF file size in MB."""
    return os.path.getsize(filepath) / (1024 * 1024)

def ocr_pdf(input_pdf, output_txt, dpi=150, lang='vie'):
    """
    OCR a PDF file using tesseract.
    
    Args:
        input_pdf: Path to input PDF
        output_txt: Path to output text file
        dpi: DPI for image conversion (default 150, lower for text-heavy docs)
        lang: Tesseract language code (default 'vie' for Vietnamese)
    """
    size_mb = get_pdf_size_mb(input_pdf)
    print(f"PDF size: {size_mb:.1f} MB")
    
    # Check if PDF is too small (likely missing content)
    if size_mb < 0.1:
        print(f"WARNING: PDF {input_pdf} is very small ({size_mb:.3f} MB), likely corrupted or missing content")
        with open(output_txt, 'w') as f:
            f.write(f"[ERROR: PDF too small ({size_mb:.3f} MB), content may be missing]\n")
        return False
    
    # Use temp directory for intermediate files
    with tempfile.TemporaryDirectory() as tmpdir:
        base = os.path.join(tmpdir, 'page')
        
        # Convert PDF to images (PPM format)
        print(f"Converting PDF pages to images at {dpi} DPI...")
        cmd = ['pdftoppm', '-r', str(dpi), '-png', input_pdf, base]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"ERROR: pdftoppm failed: {result.stderr}")
            return False
        
        # Get list of generated images
        pages = sorted([f for f in os.listdir(tmpdir) if f.startswith('page') and f.endswith('.png')])
        print(f"Generated {len(pages)} pages")
        
        if len(pages) == 0:
            print("ERROR: No pages generated from PDF")
            return False
        
        # Check if individual pages are suspiciously small (missing content)
        total_size = sum(os.path.getsize(os.path.join(tmpdir, p)) for p in pages)
        avg_size = total_size / len(pages) if pages else 0
        print(f"Average page size: {avg_size/1024:.1f} KB")
        
        if avg_size < 5000:  # Less than 5KB per page is suspicious
            print(f"WARNING: Pages are very small ({avg_size/1024:.1f} KB avg). PDF may have missing/blank content.")
        
        # OCR each page
        text_parts = []
        for i, page in enumerate(pages, 1):
            page_path = os.path.join(tmpdir, page)
            txt_base = os.path.join(tmpdir, f'page_{i}')
            
            # Skip very small files (< 1KB after conversion - likely blank)
            if os.path.getsize(page_path) < 1000:
                print(f"Page {i}: SKIPPED (blank/small: {os.path.getsize(page_path)} bytes)")
                continue
            
            print(f"OCR page {i}/{len(pages)}...")
            result = subprocess.run(
                ['tesseract', page_path, txt_base, '-l', lang],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                txt_file = f'{txt_base}.txt'
                if os.path.exists(txt_file):
                    with open(txt_file, 'r', encoding='utf-8') as f:
                        text_parts.append(f.read())
        
        # Write combined output
        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_parts))
        
        print(f"OCR complete: {len(text_parts)} pages processed")
        return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ocr_pdf.py <input.pdf> <output.txt> [dpi]")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 150
    
    success = ocr_pdf(input_pdf, output_txt, dpi)
    sys.exit(0 if success else 1)
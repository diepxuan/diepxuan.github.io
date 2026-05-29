#!/usr/bin/env python3
"""Scan toàn bộ file .md trong van-ban/ và phân loại chất lượng."""

import os
import re
import json

VAN_BAN_DIR = "/root/.openclaw/workspace/projects/github-io/van-ban"

results = {
    "can_xoa": [],
    "can_cap_nhat": [],
    "can_bo_sung": [],
    "on": []
}

errors = []

def get_files():
    files = []
    for root, dirs, filenames in os.walk(VAN_BAN_DIR):
        # Skip non-md directories
        skip_dirs = ['__pycache__', 'lib', 'imgs_new', 'css', 'js', 'images', 'menu', 'sqlite', 'json']
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fn in filenames:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, VAN_BAN_DIR)
                files.append(rel)
    return sorted(files)

def analyze_file(rel_path):
    full_path = os.path.join(VAN_BAN_DIR, rel_path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append(f"{rel_path}: Lỗi đọc file: {e}")
        return None

    # Remove YAML front matter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if fm_match:
        body = content[fm_match.end():]
        fm_content = fm_match.group(1)
    else:
        body = content
        fm_content = ""

    body_chars = len(body.strip())
    total_chars = len(content.strip())

    # Parse front matter fields
    fm = {}
    if fm_content:
        for line in fm_content.split('\n'):
            if ':' in line:
                key, _, val = line.partition(':')
                fm[key.strip()] = val.strip().strip('"').strip("'")

    # Parse body for structure
    lines = body.strip().split('\n')

    # Check for headings
    h_count = len(re.findall(r'^#{1,6}\s+', body, re.MULTILINE))
    h2_count = len(re.findall(r'^##\s+', body, re.MULTILINE))
    # Check for "Điều" mentions
    dieu_count = len(re.findall(r'Điều\s+\d+', body))
    # Check for "Chương" mentions
    chuong_count = len(re.findall(r'Chương\s+[IVXLCDM\d]+', body))
    # Check for "Thông tin văn bản"
    has_thong_tin = 'Thông tin văn bản' in body or 'thông tin văn bản' in body.lower()
    # Check for table-like content
    has_table = '|' in body
    
    # Signals for quality
    title = fm.get('title', '')
    date = fm.get('date', '')
    layout = fm.get('layout', '')
    
    # Detection logic
    reasons = []
    
    # CAN_XOA checks
    is_placeholder = False
    low_words = len(body.strip().split()) if body.strip() else 0
    
    # Check for placeholder/test content
    placeholder_patterns = [
        r'^\s*$',  # empty
        r'^\s*#\s*(placeholder|test|draft|temp|đang cập nhật|đang soạn)\s*$',
        r'^\s*#\s*.*\(\s*đang\s+viết\s+\)',
        r'^\s*#\s*(.{1,3})\s*$',  # title is too short
        r'^\s*(\-{3,}|\*{3,})\s*$',
    ]
    
    # Check if body is essentially empty or placeholder
    if low_words < 5 and body_chars < 100:
        is_placeholder = True
        reasons.append(f"Body quá ngắn: {body_chars} chars, {low_words} từ")
    
    # Check for deleted/loại-bo pattern
    if 'loại-bo' in rel_path.lower() or 'loai-bo' in rel_path.lower():
        is_placeholder = True
        reasons.append("File có tên '-loại-bo'")
    
    # Check if title is missing or very short
    if not title and not layout:
        reasons.append("Thiếu front matter (title/layout)")
    elif title and len(title) < 10:
        reasons.append(f"Tiêu đề quá ngắn: '{title}'")
    
    # Check body for meaningful content
    if low_words < 3:
        is_placeholder = True
        if not any(r.startswith("Body quá ngắn") for r in reasons):
            reasons.append(f"Chỉ có {low_words} từ trong body")
    
    if is_placeholder:
        return {
            "category": "can_xoa",
            "file": rel_path,
            "chars": body_chars,
            "words": low_words,
            "reasons": reasons,
            "suggestion": "Xoá file placeholder/không có nội dung",
            "fm": fm
        }
    
    # CAN_CAP_NHAT checks
    update_reasons = []
    
    # Check for obvious errors in date
    if date:
        try:
            year = int(date[:4])
            if year > 2026 or year < 1945:
                update_reasons.append(f"Năm ban hành bất thường: {date}")
        except:
            update_reasons.append(f"Định dạng ngày bất thường: {date}")
    
    # Check for "hết hiệu lực" or "bị thay thế" mentions
    if 'hết hiệu lực' in body.lower() or 'bị thay thế' in body.lower() or 'bãi bỏ' in body.lower():
        update_reasons.append("Văn bản có dấu hiệu hết hiệu lực/bị thay thế")
    
    # Check if has content but structure is wrong
    if dieu_count == 0 and chuong_count == 0 and body_chars > 500:
        update_reasons.append(f"Có nội dung ({body_chars} chars) nhưng không tìm thấy Điều/Chương nào")
    
    if update_reasons:
        return {
            "category": "can_cap_nhat",
            "file": rel_path,
            "chars": body_chars,
            "words": low_words,
            "reasons": update_reasons,
            "suggestion": "Kiểm tra và cập nhật nội dung/văn bản gốc",
            "fm": fm,
            "dieu_count": dieu_count,
            "chuong_count": chuong_count
        }
    
    # CAN_BO_SUNG checks
    supplement_reasons = []
    
    if body_chars < 500:
        supplement_reasons.append(f"Body quá ngắn: {body_chars} chars (ngưỡng 500)")
    
    if dieu_count == 0 and chuong_count == 0 and body_chars < 500:
        supplement_reasons.append("Thiếu Điều/Chương")
    
    if not has_thong_tin and body_chars > 100:
        supplement_reasons.append("Thiếu phần 'Thông tin văn bản'")
    
    if chuong_count == 0 and dieu_count < 10 and body_chars >= 500:
        supplement_reasons.append(f"Có {dieu_count} Điều, có thể thiếu chương")
    
    if supplement_reasons:
        return {
            "category": "can_bo_sung",
            "file": rel_path,
            "chars": body_chars,
            "words": low_words,
            "reasons": supplement_reasons,
            "suggestion": "Bổ sung nội dung còn thiếu",
            "fm": fm,
            "dieu_count": dieu_count,
            "chuong_count": chuong_count,
            "has_thong_tin": has_thong_tin
        }
    
    # ON
    return {
        "category": "on",
        "file": rel_path,
        "chars": body_chars,
        "words": low_words,
        "fm": fm,
        "dieu_count": dieu_count,
        "chuong_count": chuong_count,
        "has_thong_tin": has_thong_tin
    }

def main():
    files = get_files()
    print(f"Tìm thấy {len(files)} file .md")
    
    short_files = []  # < 500 chars
    root_files = []   # directly in van-ban/
    subfolder_files = []
    
    for i, rel_path in enumerate(files):
        if i % 100 == 0:
            print(f"  Đang xử lý {i}/{len(files)}...")
        
        result = analyze_file(rel_path)
        if result is None:
            continue
        
        cat = result["category"]
        results[cat].append(result)
        
        if result["chars"] < 500:
            short_files.append(rel_path)
        
        parts = rel_path.split('/')
        if len(parts) == 1:
            root_files.append(rel_path)
        else:
            subfolder_files.append(rel_path)
    
    # Print summary
    print(f"\n=== TỔNG KẾT ===")
    print(f"Tổng số file: {len(files)}")
    print(f"File root van-ban/: {len(root_files)}")
    print(f"File subfolder: {len(subfolder_files)}")
    print(f"File body < 500 chars: {len(short_files)}")
    print(f"\nPhân loại:")
    print(f"  CẦN XOÁ: {len(results['can_xoa'])}")
    print(f"  CẦN CẬP NHẬT: {len(results['can_cap_nhat'])}")
    print(f"  CẦN BỔ SUNG: {len(results['can_bo_sung'])}")
    print(f"  ỔN: {len(results['on'])}")
    
    # Output detailed results as JSON
    output = {
        "summary": {
            "total_files": len(files),
            "root_files": len(root_files),
            "subfolder_files": len(subfolder_files),
            "short_files": len(short_files),
            "can_xoa": len(results['can_xoa']),
            "can_cap_nhat": len(results['can_cap_nhat']),
            "can_bo_sung": len(results['can_bo_sung']),
            "on": len(results['on']),
        },
        "results": results,
        "errors": errors,
        "short_files_list": short_files,
        "root_files_list": root_files
    }
    
    with open("/tmp/vanban_scan.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\nĐã ghi kết quả vào /tmp/vanban_scan.json")
    
    # Print sample of each category
    for cat, label in [("can_xoa", "CẦN XOÁ"), ("can_cap_nhat", "CẦN CẬP NHẬT"), ("can_bo_sung", "CẦN BỔ SUNG")]:
        print(f"\n--- {label} (top 5) ---")
        for r in results[cat][:5]:
            print(f"  {r['file']}: {r['chars']} chars | {r['reasons']}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Scan van-ban/ for refactor candidates: "Đang cập nhật", <10KB, lastedit > 7d."""
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

VANBAN = Path("van-ban")
now = datetime.now()
seven_days_ago = now - timedelta(days=7)

results = {"Dang_cap_nhat": [], "small_files": [], "old_files": [], "both": []}

for root, dirs, files in os.walk(VANBAN):
    for f in files:
        if not f.endswith(".md"):
            continue
        p = Path(root) / f
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        size_kb = p.stat().st_size / 1024
        mtime = datetime.fromtimestamp(p.stat().st_mtime)
        is_old = mtime < seven_days_ago

        # Check "Đang cập nhật"
        has_dang_cap = "Đang cập nhật" in text or "Dang cap nhat" in text

        # Check lastedit in frontmatter
        lastedit = None
        m = re.search(r"modified:\s*(\d{4}-\d{2}-\d{2})", text)
        if m:
            try:
                lastedit = datetime.strptime(m.group(1), "%Y-%m-%d")
            except Exception:
                pass
        if lastedit is None:
            m = re.search(r"lastedit:\s*(\d{4}-\d{2}-\d{2})", text)
            if m:
                try:
                    lastedit = datetime.strptime(m.group(1), "%Y-%m-%d")
                except Exception:
                    pass
        is_lastedit_old = lastedit is not None and lastedit < seven_days_ago

        rel = str(p.relative_to(Path(".")))

        if has_dang_cap:
            results["Dang_cap_nhat"].append((rel, size_kb, mtime.date(), lastedit))
        if size_kb < 10:
            results["small_files"].append((rel, size_kb, mtime.date(), lastedit, has_dang_cap))
        if is_old or is_lastedit_old:
            results["old_files"].append((rel, size_kb, mtime.date(), lastedit, has_dang_cap, is_old, is_lastedit_old))

print("=== FILE CẦN REFACTOR ===")
print(f"\n--- Có 'Đang cập nhật' ({len(results['Dang_cap_nhat'])}) ---")
for r in results["Dang_cap_nhat"]:
    print(f"  {r[0]} ({r[1]:.1f}KB, mtime={r[2]}, modified={r[3]})")

print(f"\n--- Dưới 10KB ({len(results['small_files'])}) ---")
for r in results["small_files"]:
    print(f"  {r[0]} ({r[1]:.1f}KB, mtime={r[2]}, modified={r[3]}, ĐangCậpNhật={r[4]})")

print(f"\n--- Cũ hơn 7 ngày ({len(results['old_files'])}) ---")
for r in results["old_files"]:
    print(f"  {r[0]} ({r[1]:.1f}KB, mtime={r[2]}, modified={r[3]}, ĐangCậpNhật={r[4]}, mtime_old={r[5]}, mod_old={r[6]})")
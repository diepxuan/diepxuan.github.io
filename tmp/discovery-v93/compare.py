#!/usr/bin/env python3
import re, sys, os

def extract_d1_slugs(filepath):
    """Extract all d1 slugs (ban hanh) from sitemap XML, return set of slug numbers."""
    with open(filepath, 'r') as f:
        content = f.read()
    # Pattern: match URLs ending in -XXXXXX-d1.html
    slugs = set()
    for m in re.finditer(r'/([^/]+)-(\d+)-d1\.html', content):
        slug_num = int(m.group(2))
        full_slug = m.group(0)
        category = m.group(1)
        slugs.add((slug_num, full_slug, category))
    return slugs

def main():
    os.chdir('/root/.openclaw/workspace/projects/github-io')
    
    # Current sitemaps
    nd_new = extract_d1_slugs('tmp/discovery-v93/sitemap_nghidinh.xml')
    tt_new = extract_d1_slugs('tmp/discovery-v93/sitemap_thongtu.xml')
    
    # v88 baseline
    nd_old = extract_d1_slugs('tmp/discovery-v88/sitemap_nghidinh.xml')
    tt_old = extract_d1_slugs('tmp/discovery-v88/sitemap_thongtu.xml')
    
    # Find new slugs
    new_nd = sorted(nd_new - nd_old, key=lambda x: x[0], reverse=True)
    new_tt = sorted(tt_new - tt_old, key=lambda x: x[0], reverse=True)
    
    # Get max slugs from v88 (for reference)
    nd_old_max = max(s[0] for s in nd_old) if nd_old else 0
    tt_old_max = max(s[0] for s in tt_old) if tt_old else 0
    
    # Get current max
    nd_new_max = max(s[0] for s in nd_new) if nd_new else 0
    tt_new_max = max(s[0] for s in tt_new) if tt_new else 0
    
    print(f"=== SITEMAP COMPARISON v88 -> v93 ===")
    print(f"NĐ v88 max d1 slug: {nd_old_max}")
    print(f"NĐ v93 max d1 slug: {nd_new_max}")
    print(f"TT v88 max d1 slug: {tt_old_max}")
    print(f"TT v93 max d1 slug: {tt_new_max}")
    print()
    
    print(f"=== NEW NGHI DINH (d1 only, {len(new_nd)} found) ===")
    for slug_num, full_slug, category in new_nd:
        print(f"  [{slug_num}] {category} -> {full_slug}")
    
    print()
    print(f"=== NEW THONG TU (d1 only, {len(new_tt)} found) ===")
    for slug_num, full_slug, category in new_tt[:10]:  # limit
        print(f"  [{slug_num}] {category} -> {full_slug}")
    if len(new_tt) > 10:
        print(f"  ... and {len(new_tt) - 10} more")
    
    # Write summary file
    with open('tmp/discovery-v93/summary.txt', 'w') as f:
        f.write(f"NĐ old max: {nd_old_max}, new max: {nd_new_max}\n")
        f.write(f"TT old max: {tt_old_max}, new max: {tt_new_max}\n\n")
        f.write(f"NEW NĐ ({len(new_nd)}):\n")
        for slug_num, full_slug, category in new_nd:
            f.write(f"  https://luatvietnam.vn/{full_slug}\n")
        f.write(f"\nNEW TT ({len(new_tt)}):\n")
        for slug_num, full_slug, category in new_tt:
            f.write(f"  https://luatvietnam.vn/{full_slug}\n")

    # Output list of new URLs for curl checking (top 5 ND)
    print("\n=== TOP 5 NEW NĐ URLS ===")
    for slug_num, full_slug, category in new_nd[:5]:
        print(f"https://luatvietnam.vn/{full_slug}")


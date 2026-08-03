#!/usr/bin/env python3
"""Build script for 109/2026/TT-BTC (crawl Hoàn thiện).

Source: tmp/discovery-v53/109-TT-BTC.html (slug 442020, luatvietnam.vn)
Pattern: similar to 110/TT-BTC (anchor "BỘ TÀI CHÍNH" + heading promotion).
"""
import re
import html

SRC = 'tmp/discovery-v53/109-TT-BTC.html'
OUT = 'van-ban/tai-chinh/109-2026-tt-btc-quan-ly-dich-vu-lam-thu-tuc-thue.md'

def clean(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def main():
    with open(SRC, encoding='utf-8') as f:
        html_text = f.read()

    m = re.search(r'<article[^>]*>(.*?)</article>', html_text, re.DOTALL)
    article = m.group(1)
    paras = re.findall(r'<p[^>]*>(.*?)</p>', article, re.DOTALL)

    start_idx = None
    for i, p in enumerate(paras):
        c = clean(p)
        if 'BỘ TÀI CHÍNH' in c and 'CỘNG HÒA' not in c and len(c) < 500:
            start_idx = i
            break
    if start_idx is None:
        for i, p in enumerate(paras):
            c = clean(p)
            if 'BỘ TÀI CHÍNH' in c:
                start_idx = i
                break
    assert start_idx is not None, 'Anchor not found'

    end_idx = len(paras)
    for i in range(start_idx, len(paras)):
        c = clean(paras[i])
        if 'Bạn chưa Đăng nhập' in c or 'Hãy Đăng nhập' in c:
            end_idx = i
            break

    body_paras = [clean(p) for p in paras[start_idx:end_idx] if clean(p)]
    body_paras = [p for p in body_paras if p.strip() != 'Đang theo dõi']

    out_paras = []
    seen_dieu = set()
    for line in body_paras:
        m_dieu = re.match(r'^(Điều \d+)\.\s+(.+)$', line)
        m_chuong = re.match(r'^(Chương [IVXLC]+)$', line)
        m_phuluc = re.match(r'^(Phụ lục [IVXLC0-9]+)$', line)
        if m_dieu:
            n_label = m_dieu.group(1)
            if n_label not in seen_dieu:
                out_paras.append(f'### {n_label}. {m_dieu.group(2)}')
                seen_dieu.add(n_label)
                continue
        if m_chuong:
            out_paras.append(f'## {m_chuong.group(1)}')
            continue
        if m_phuluc:
            out_paras.append(f'## {m_phuluc.group(1)}')
            continue
        out_paras.append(line)

    body_md = '\n\n'.join(out_paras)

    front_matter = '''---
layout: vanban
title: "Thông tư 109/2026/TT-BTC Quy định quản lý hoạt động kinh doanh dịch vụ làm thủ tục về thuế"
date: 2026-08-01
modified: 2026-08-01
so-hieu: 109/2026/TT-BTC
co-quan-ban-hanh: Bộ Tài chính
nguoi-ky: Cao Anh Tuấn
chuc-danh: Thứ trưởng (KT. Bộ trưởng)
ngay-ban-hanh: 2026-07-24
ngay-hieu-luc: 2026-07-24
hieu-luc: 2026-07-24 đến nay
trich-yeu: "Quy định quản lý hoạt động kinh doanh dịch vụ làm thủ tục về thuế; điều kiện, giấy xác nhận đại lý thuế; nhân viên đại lý thuế; báo cáo."
can-cu-phap-ly:
  - Luật Ban hành văn bản quy phạm pháp luật 64/2025/QH15 (sửa đổi, bổ sung bởi Luật 87/2025/QH15)
  - Luật Quản lý thuế 108/2025/QH15
  - Nghị định 252/2026/NĐ-CP quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Quản lý thuế
  - Nghị định 29/2025/NĐ-CP (sửa đổi bởi Nghị định 166/2025/NĐ-CP)
loai-van-ban: TT-BTC
linh-vuc: Thue-Phi-Le-phi
nhom-van-ban: Tai-chinh
tags:
  - đại lý thuế
  - dịch vụ thuế
  - làm thủ tục thuế
  - quản lý thuế
  - bộ tài chính
  - 2026
  - TT-BTC
group: tai-chinh
docid: "442020"
source: vanban.chinhphu.vn; luatvietnam.vn
trang-thai: hoanthien
ghi-chu: "Crawl từ HTML body đầy đủ luatvietnam.vn slug 442020 (250 KB). Văn bản gồm 5 Chương, 18 Điều, quy định về đại lý thuế và nhân viên đại lý thuế."
lastedit: 2026-08-01
---

# THÔNG TƯ 109/2026/TT-BTC

Quy định quản lý hoạt động kinh doanh dịch vụ làm thủ tục về thuế

## Metadata

- **Số hiệu**: 109/2026/TT-BTC
- **Cơ quan ban hành**: Bộ Tài chính
- **Ngày ban hành**: 24/07/2026
- **Hiệu lực**: 24/07/2026
- **Người ký**: Cao Anh Tuấn (KT. BỘ TRƯỞNG THỨ TRƯỞNG)
- **Trích yếu**: Quy định quản lý hoạt động kinh doanh dịch vụ làm thủ tục về thuế
- **Lĩnh vực**: Thuế-Phí-Lệ phí; Doanh nghiệp

## Căn cứ pháp lý

- Luật Ban hành văn bản quy phạm pháp luật số 64/2025/QH15 được sửa đổi, bổ sung bởi Luật số 87/2025/QH15;
- Luật Quản lý thuế số 108/2025/QH15;
- Nghị định số 252/2026/NĐ-CP của Chính phủ quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Quản lý thuế;
- Nghị định số 29/2025/NĐ-CP (sửa đổi, bổ sung bởi Nghị định số 166/2025/NĐ-CP);
- Theo đề nghị của Cục trưởng Cục Thuế.

---

## Nội dung văn bản

'''

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write(body_md)
        f.write('\n')

    n_lines = body_md.count('\n') + 1
    n_dieu = sum(1 for ln in body_md.split('\n') if ln.startswith('### Điều '))
    n_chuong = sum(1 for ln in body_md.split('\n') if ln.startswith('## Chương '))
    print(f'Wrote {OUT}')
    print(f'  lines: {n_lines}, Articles: {n_dieu}, Chapters: {n_chuong}')

if __name__ == '__main__':
    main()

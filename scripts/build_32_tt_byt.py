#!/usr/bin/env python3
"""Build script for 32/2026/TT-BYT (crawl Hoàn thiện).

Source: tmp/discovery-v57/tt32-byt.html (slug 442224-d1, luatvietnam.vn)
Pattern: anchor "BỘ Y TẾ" + "Số: 32/2026/TT-BYT" + heading promotion.
Reference: scripts/build_109_tt_btc.py
"""
import re
import html

SRC = 'tmp/discovery-v57/tt32-byt.html'
OUT = 'van-ban/y-te/32-2026-tt-byt-dang-ky-luu-hanh-thuoc.md'


def clean(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


# Rác UI của luatvietnam.vn lẫn trong body văn bản
UI_NOISE = (
    'Đang theo dõi',
    'Tải về',
    'Vui lòng đăng nhập',
    'Vui lòng Đăng nhập',
    'tiện ích dành cho tài khoản',
    'Tiện ích dành cho tài khoản',
    'Đăng ký tại đây',
    'Từ khóa liên quan',
    'LuatVietnam',
    'Luatvietnam.vn',
)


def is_noise(line):
    if not line:
        return True
    if line in {'Đang theo dõi', '___________________', '_______', '_________________'}:
        return True
    return any(tok in line for tok in UI_NOISE)


def main():
    with open(SRC, encoding='utf-8') as f:
        html_text = f.read()

    m = re.search(r'<article[^>]*>(.*?)</article>', html_text, re.DOTALL)
    assert m, 'Article block not found'
    article = m.group(1)
    paras = [clean(p) for p in re.findall(r'<p[^>]*>(.*?)</p>', article, re.DOTALL)]

    # Anchor: đoạn header văn bản chứa "BỘ Y TẾ" và số hiệu
    start_idx = None
    for i, c in enumerate(paras):
        if 'BỘ Y TẾ' in c and 'Số: 32/2026/TT-BYT' in c:
            start_idx = i
            break
    assert start_idx is not None, 'Anchor not found'

    # Dừng trước footer đăng nhập
    end_idx = len(paras)
    for i in range(start_idx, len(paras)):
        if 'Bạn chưa Đăng nhập' in paras[i] or 'Hãy Đăng nhập' in paras[i]:
            end_idx = i
            break

    body = paras[start_idx:end_idx]

    # Đoạn anchor còn dính prefix "Hiệu lực: Đã biết ..." -> cắt về "BỘ Y TẾ"
    first = body[0]
    body[0] = first[first.index('BỘ Y TẾ'):]

    # Bỏ chuỗi gạch dưới trang trí của bản gốc
    body = [re.sub(r'\s*_{3,}\s*', ' ', x).strip() for x in body]

    out_paras = []
    seen_dieu = set()
    pending_chuong = False
    for line in body:
        if is_noise(line):
            continue

        m_dieu = re.match(r'^Điều\s+(\d+)\.\s*(.*)$', line)
        m_chuong = re.match(r'^Chương\s+([IVXLC]+)\.?\s*(.*)$', line)
        m_muc = re.match(r'^Mục\s+(\d+)\.?\s*(.*)$', line)

        if m_dieu:
            num = m_dieu.group(1)
            if num in seen_dieu:
                continue
            seen_dieu.add(num)
            title = m_dieu.group(2).strip()
            out_paras.append(f'### Điều {num}. {title}'.rstrip())
            continue

        if m_chuong:
            title = m_chuong.group(2).strip()
            head = f'## Chương {m_chuong.group(1)}'
            out_paras.append(f'{head}. {title}' if title else head)
            pending_chuong = title == ''
            continue

        if m_muc:
            title = m_muc.group(2).strip()
            head = f'### Mục {m_muc.group(1)}'
            out_paras.append(f'{head}. {title}' if title else head)
            continue

        # Tiêu đề Chương nằm ở đoạn kế tiếp (VD: "QUY ĐỊNH CHUNG") -> gộp vào heading
        if pending_chuong:
            pending_chuong = False
            if line == line.upper() and len(line) < 400:
                out_paras[-1] = f'{out_paras[-1]}. {line}'
                continue

        out_paras.append(line)

    body_md = '\n\n'.join(out_paras)

    front_matter = '''---
layout: vanban
title: "Thông tư 32/2026/TT-BYT quy định việc đăng ký lưu hành thuốc, nguyên liệu làm thuốc"
date: 2026-07-29
modified: 2026-08-05
so-hieu: 32/2026/TT-BYT
ngay-ban-hanh: 2026-07-29
ngay-hieu-luc: 2026-10-01
nguoi-ky: Nguyễn Tri Thức
chuc-vu: Thứ trưởng Bộ Y tế
co-quan-ban-hanh: Bộ Y tế
loai-van-ban: Thông tư
trich-yeu: "Quy định việc đăng ký lưu hành thuốc, nguyên liệu làm thuốc"
can-cu-phap-ly:
  - "Luật Dược số 105/2016/QH13 được sửa đổi, bổ sung bởi Luật số 44/2024/QH15"
  - "Nghị định số 163/2025/NĐ-CP quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Dược"
  - "Nghị định số 42/2025/NĐ-CP quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Bộ Y tế"
group: y-te
tags:
  - thong-tu
  - y-te
  - duoc-pham
  - dang-ky-thuoc
docid: 32/2026/TT-BYT
source: luatvietnam.vn
slug: 32/2026/TT-BYT
trangthai: hoanthien
---

'''

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(front_matter + body_md + '\n')

    n_dieu = len(re.findall(r'^### Điều \d+\.', body_md, re.M))
    n_chuong = len(re.findall(r'^## Chương ', body_md, re.M))
    print(f'Wrote {OUT}: {len(out_paras)} paras, {n_dieu} Điều, {n_chuong} Chương')


if __name__ == '__main__':
    main()

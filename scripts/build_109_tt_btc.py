#!/usr/bin/env python3
"""Build script cho Thong tu 109/2026/TT-BTC (crawl toan van, trang thai Hoan thien).

Nguon: tmp/discovery-v58/tt109-btc.html (slug 442209-d1, luatvietnam.vn)
Cach lam: lay <article>, trich <p>, neo tu doan "BO TAI CHINH", dung truoc
footer "Ban chua Dang nhap", bo cac doan UI/tom tat, dedup heading "Dieu N.",
nang cap heading Chuong/Dieu/Phu luc.
"""
import re
import html

SRC = 'tmp/discovery-v58/tt109-btc.html'
OUT = 'van-ban/tai-chinh/109-2026-tt-btc-quan-ly-dich-vu-lam-thu-tuc-thue.md'


def clean(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    # Bo khoang trang thua truoc dau cau (sinh ra do go the inline nhu <a>).
    # Khong dung cho chuoi dau cham dien thong tin trong bieu mau ("....").
    s = re.sub(r'\s+([,;:!?])(?![.])', r'\1', s)
    s = re.sub(r'(?<![.\s])\s+\.(?!\.)', '.', s)
    return s


UI_NOISE = (
    'Đây là tiện ích dành cho tài khoản',
    'Vui lòng Đăng nhập',
    'Tính năng này chỉ có tại LuatVietnam',
    'Xem hướng dẫn chi tiết cách sử dụng',
    'Đang theo dõi',
    'Tải về Mục lục Lưu',
)


def main():
    with open(SRC, encoding='utf-8') as f:
        html_text = f.read()

    m = re.search(r'<article[^>]*>(.*?)</article>', html_text, re.DOTALL)
    assert m, 'Khong tim thay the <article>'
    paras = re.findall(r'<p[^>]*>(.*?)</p>', m.group(1), re.DOTALL)

    start_idx = None
    for i, p in enumerate(paras):
        c = clean(p)
        if 'BỘ TÀI CHÍNH' in c and 'CỘNG HÒA' not in c and len(c) < 500:
            start_idx = i
            break
    assert start_idx is not None, 'Khong tim thay neo BO TAI CHINH'

    end_idx = len(paras)
    for i in range(start_idx, len(paras)):
        c = clean(paras[i])
        if 'Bạn chưa Đăng nhập' in c or 'Hãy Đăng nhập' in c:
            end_idx = i
            break

    body_paras = []
    for p in paras[start_idx:end_idx]:
        c = clean(p)
        if not c:
            continue
        if any(noise in c for noise in UI_NOISE):
            continue
        body_paras.append(c)

    out_paras = []
    seen_dieu = set()
    for line in body_paras:
        m_dieu = re.match(r'^(Điều \d+)\.\s+(.+)$', line)
        m_chuong = re.match(r'^(Chương [IVXLC]+)$', line)
        m_phuluc = re.match(r'^(Phụ lục[ IVXLC0-9]*)$', line)
        if m_dieu:
            n_label = m_dieu.group(1)
            if n_label in seen_dieu:
                continue
            out_paras.append(f'### {n_label}. {m_dieu.group(2)}')
            seen_dieu.add(n_label)
            continue
        if m_chuong:
            out_paras.append(f'## {m_chuong.group(1)}')
            continue
        if m_phuluc:
            out_paras.append(f'## {m_phuluc.group(1).strip()}')
            continue
        out_paras.append(line)

    body_md = '\n\n'.join(out_paras)

    front_matter = '''---
layout: vanban
title: "Thông tư 109/2026/TT-BTC Quy định quản lý hoạt động kinh doanh dịch vụ làm thủ tục về thuế"
date: 2026-08-05
modified: 2026-08-05
so-hieu: 109/2026/TT-BTC
co-quan-ban-hanh: Bộ Tài chính
nguoi-ky: Cao Anh Tuấn
chuc-danh: Thứ trưởng (KT. Bộ trưởng)
ngay-ban-hanh: 2026-07-24
ngay-hieu-luc: 2026-07-24
hieu-luc: 2026-07-24 đến nay
trich-yeu: "Quy định quản lý hoạt động kinh doanh dịch vụ làm thủ tục về thuế: đánh giá năng lực nghiệp vụ chuyên môn về thuế, cập nhật kiến thức, kiểm tra hoạt động kinh doanh dịch vụ."
can-cu-phap-ly:
  - Luật Quản lý thuế 108/2025/QH15
  - Nghị định 252/2026/NĐ-CP quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Quản lý thuế
  - Nghị định 29/2025/NĐ-CP (sửa đổi, bổ sung bởi Nghị định 166/2025/NĐ-CP)
loai-van-ban: TT-BTC
linh-vuc: Thue-Phi-Le-phi
nhom-van-ban: Tai-chinh
tags:
  - đại lý thuế
  - dịch vụ thuế
  - làm thủ tục thuế
  - quản lý thuế
  - đánh giá năng lực
  - cập nhật kiến thức
  - bộ tài chính
  - 2026
  - TT-BTC
group: tai-chinh
docid: "442209"
source: luatvietnam.vn
slug: "109-2026-tt-btc-quan-ly-dich-vu-lam-thu-tuc-thue"
trang-thai: hoanthien
lastedit: 2026-08-05
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

- Luật Quản lý thuế số 108/2025/QH15;
- Nghị định số 252/2026/NĐ-CP của Chính phủ quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Quản lý thuế;
- Nghị định số 29/2025/NĐ-CP của Chính phủ quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Bộ Tài chính, được sửa đổi, bổ sung bởi Nghị định số 166/2025/NĐ-CP;
- Theo đề nghị của Cục trưởng Cục Thuế.

---

## Nội dung văn bản

'''

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write(body_md)
        f.write('\n')

    lines = body_md.split('\n')
    n_dieu = sum(1 for ln in lines if ln.startswith('### Điều '))
    n_chuong = sum(1 for ln in lines if ln.startswith('## Chương '))
    print(f'Wrote {OUT}')
    print(f'  body lines: {len(lines)}, Articles: {n_dieu}, Chapters: {n_chuong}')


if __name__ == '__main__':
    main()

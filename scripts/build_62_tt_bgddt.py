#!/usr/bin/env python3
"""Build script cho Thong tu 62/2026/TT-BGDDT (crawl toan van, trang thai Hoan thien).

Nguon: tmp/discovery-v59/tt62-bgddt.html (slug 442200-d1, luatvietnam.vn)
Cach lam: lay <article>, trich <p>, neo tu doan chua "BO GIAO DUC VA DAO TAO"
va "So: 62/2026/TT-BGDDT", dung truoc footer "Ban chua Dang nhap", bo cac doan
UI/tom tat, dedup heading "Dieu N.", nang cap heading Chuong/Dieu, gop cac gach
dau dong a)/b)/c)/d) vao khoan so gan nhat.
"""
import re
import html

SRC = 'tmp/discovery-v59/tt62-bgddt.html'
OUT = 'van-ban/giao-duc/62-2026-tt-bgddt-quy-trinh-bien-soan-chuong-trinh-giao-duc-dai-hoc.md'


def clean(s):
    s = html.unescape(s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    # Bo khoang trang thua truoc dau cau (sinh ra do go the inline nhu <a>).
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

CHUONG_TITLES = {
    'CHƯƠNG I': 'QUY ĐỊNH CHUNG',
    'CHƯƠNG II': 'QUY TRÌNH BIÊN SOẠN, THẨM ĐỊNH, BAN HÀNH',
    'CHƯƠNG III': 'TỔ CHỨC THỰC HIỆN',
}

ROMAN = {'I': 'I', 'II': 'II', 'III': 'III', 'IV': 'IV', 'V': 'V'}


def main():
    with open(SRC, encoding='utf-8') as f:
        html_text = f.read()

    m = re.search(r'<article[^>]*>(.*?)</article>', html_text, re.DOTALL)
    assert m, 'Khong tim thay the <article>'
    paras = re.findall(r'<p[^>]*>(.*?)</p>', m.group(1), re.DOTALL)

    start_idx = None
    for i, p in enumerate(paras):
        c = clean(p)
        if 'BỘ GIÁO DỤC VÀ ĐÀO TẠO' in c and 'Số: 62/2026/TT-BGDĐT' in c:
            start_idx = i
            break
    assert start_idx is not None, 'Khong tim thay neo BO GIAO DUC VA DAO TAO'

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
        # Bo phan UI "Hieu luc: Da biet ..." o dau doan neo.
        c = re.sub(r'^(?:Hiệu lực: Đã biết\s*)?(?:Tình trạng hiệu lực: Đã biết\s*)?', '', c).strip()
        if not c or c in ('_______', '_______________', '_________________'):
            continue
        body_paras.append(c)

    out_paras = []
    seen_dieu = set()
    for line in body_paras:
        m_dieu = re.match(r'^(Điều \d+)\.\s+(.+)$', line)
        m_chuong = re.match(r'^CHƯƠNG ([IVXLC]+)$', line)
        if m_chuong:
            num = m_chuong.group(1)
            title = CHUONG_TITLES.get(f'CHƯƠNG {num}')
            out_paras.append(('chuong', f'Chương {ROMAN.get(num, num)}', title))
            continue
        # Bo dong tieu de chuong da gop vao heading Chuong.
        if line in CHUONG_TITLES.values():
            continue
        if m_dieu:
            n_label = m_dieu.group(1)
            if n_label in seen_dieu:
                continue
            out_paras.append(('dieu', f'{n_label}. {m_dieu.group(2)}', None))
            seen_dieu.add(n_label)
            continue
        out_paras.append(('p', line, None))

    # Gop cac gach dau dong a) b) c) d) vao khoan so gan nhat, va noi lai cac
    # doan bi nguon ngat giua chung (doan tiep theo bat dau bang chu thuong).
    merged = []
    for kind, text, extra in out_paras:
        if kind == 'p' and merged and merged[-1][0] == 'p':
            prev_kind, prev_text, prev_extra = merged[-1]
            if re.match(r'^[a-zđ]\)\s', text):
                merged[-1] = (prev_kind, prev_text + '\n   ' + text, prev_extra)
                continue
            # Doan noi tiep: bat dau bang chu thuong tieng Viet, doan truoc
            # chua ket thuc bang dau cau ket doan.
            if re.match(r'^[a-zàáâãèéêìíòóôõùúăđĩũơưạảấầẩẫậắằẳẵặẹẻẽếề'
                        r'ểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]', text) \
                    and not prev_text.rstrip().endswith(('.', ';', ':', '/.')):
                merged[-1] = (prev_kind, prev_text + ' ' + text, prev_extra)
                continue
        merged.append((kind, text, extra))

    lines_out = []
    for kind, text, extra in merged:
        if kind == 'chuong':
            lines_out.append(f'## {text}')
            if extra:
                lines_out.append(f'### {extra}')
            continue
        if kind == 'dieu':
            lines_out.append(f'### {text}')
            continue
        # Formatting cho cac doan dac biet o header/footer van ban.
        if text.startswith('BỘ GIÁO DỤC VÀ ĐÀO TẠO'):
            t = text.replace('BỘ GIÁO DỤC VÀ ĐÀO TẠO _______ Số: 62/2026/TT-BGDĐT',
                             '**BỘ GIÁO DỤC VÀ ĐÀO TẠO**\n\n_______\n\nSố: 62/2026/TT-BGDĐT')
            lines_out.append(t)
            continue
        if text.startswith('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM'):
            t = text.replace(
                'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập – Tự do – Hạnh phúc _________________ ',
                '**CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM**  \n**Độc lập – Tự do – Hạnh phúc**  \n_________________  \n\n_') + '_'
            lines_out.append(t)
            continue
        if text == 'THÔNG TƯ':
            lines_out.append('**THÔNG TƯ**')
            continue
        if text.startswith('Căn cứ ') or text.startswith('Theo đề nghị của') \
                or text.startswith('Bộ trưởng Bộ Giáo dục và Đào tạo ban hành'):
            lines_out.append(f'_{text}_')
            continue
        if text.startswith('Nơi nhận:'):
            rest = text[len('Nơi nhận:'):].strip().lstrip('-').strip()
            items = [x.strip().lstrip('-').strip()
                     for x in re.split(r'\s-\s', rest) if x.strip(' -')]
            lines_out.append('**_Nơi nhận:_**')
            lines_out.append('\n'.join(f' - {it}' for it in items))
            continue
        if text.startswith('KT. BỘ TRƯỞNG'):
            lines_out.append('**KT. BỘ TRƯỞNG**  \n**THỨ TRƯỞNG**  \n**Lê Quân**')
            continue
        lines_out.append(text)

    body_md = '\n\n'.join(lines_out)

    front_matter = '''---
layout: vanban
title: "Thông tư 62/2026/TT-BGDĐT: Quy trình biên soạn, ban hành chương trình, giáo trình dạy và học các môn học, học phần bắt buộc sử dụng chung trong chương trình đào tạo các trình độ của giáo dục đại học"
date: 2026-07-28
modified: 2026-08-05
so-hieu: 62/2026/TT-BGDĐT
co-quan-ban-hanh: Bộ Giáo dục và Đào tạo
nguoi-ky: Lê Quân
chuc-vu: Thứ trưởng Bộ Giáo dục và Đào tạo (KT. Bộ trưởng)
ngay-ban-hanh: 2026-07-28
ngay-hieu-luc: 2026-09-12
loai-van-ban: Thông tư
linh-vuc: Giáo dục / Chương trình ĐH
trich-yeu: "Quy định quy trình biên soạn, ban hành chương trình, giáo trình dạy và học các môn học, học phần bắt buộc sử dụng chung trong chương trình đào tạo các trình độ của giáo dục đại học: biên soạn, thẩm định, ban hành chương trình, phê duyệt giáo trình; công khai, cập nhật chương trình, giáo trình."
can-cu-phap-ly:
  - Luật Ban hành văn bản quy phạm pháp luật số 64/2025/QH15
  - Luật Giáo dục số 43/2019/QH14 (sửa đổi, bổ sung bởi Luật số 123/2025/QH15)
  - Luật Giáo dục đại học số 125/2025/QH15
  - Luật Thư viện số 46/2019/QH14
  - Luật An ninh mạng số 24/2018/QH14
  - Luật Chuyển đổi số số 148/2025/QH15
  - Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15
  - Luật Giao dịch điện tử số 20/2023/QH15
  - Luật Sở hữu trí tuệ số 50/2005/QH11 (sửa đổi, bổ sung bởi Luật số 36/2009/QH12, Luật số 42/2019/QH14, Luật số 07/2022/QH15, Luật số 93/2025/QH15, Luật số 131/2025/QH15)
  - Luật Xuất bản số 19/2012/QH13
  - Nghị định số 279/2026/NĐ-CP quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Bộ Giáo dục và Đào tạo
tags:
  - giáo dục đại học
  - chương trình đào tạo
  - giáo trình
  - biên soạn chương trình
  - thẩm định chương trình
  - môn học bắt buộc
  - bộ giáo dục và đào tạo
  - 2026
  - TT-BGDĐT
group: giao-duc
docid: "442200"
source: luatvietnam.vn
nguon: luatvietnam.vn
slug: "62-2026-tt-bgddt-quy-trinh-bien-soan-chuong-trinh-giao-duc-dai-hoc"
trangthai: hoanthien
lastedit: 2026-08-05
---

# THÔNG TƯ 62/2026/TT-BGDĐT

## Quy trình biên soạn, ban hành chương trình, giáo trình dạy và học các môn học, học phần bắt buộc sử dụng chung trong chương trình đào tạo các trình độ của giáo dục đại học

## Metadata

- **Số hiệu**: 62/2026/TT-BGDĐT
- **Cơ quan ban hành**: Bộ Giáo dục và Đào tạo
- **Ngày ban hành**: 28/07/2026
- **Hiệu lực**: 12/09/2026
- **Người ký**: Lê Quân (KT. BỘ TRƯỞNG THỨ TRƯỞNG)
- **Trích yếu**: Quy định quy trình biên soạn, ban hành chương trình, giáo trình dạy và học các môn học, học phần bắt buộc sử dụng chung trong chương trình đào tạo các trình độ của giáo dục đại học
- **Lĩnh vực**: Giáo dục - Đào tạo; Chương trình đại học

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

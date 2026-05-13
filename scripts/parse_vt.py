#!/usr/bin/env python3
"""Parse raw scraped markdown from thuvienphapluat.vn into clean Vietnamese legal doc."""
import re, sys, json

raw = sys.stdin.read()

# ─ Find the legal text start ─
# Look for **LUẬT** **VIỄN THÔNG** or "LUẬT VIỄN THÔNG"
m = re.search(r'\*\*LUẬT\*\*\s*\n\s*\*\*VIỄN THÔNG\*\*', raw)
if not m:
    print("ERR: no LUẬT marker", file=sys.stderr)
    sys.exit(1)

body = raw[m.start():]

# ─ Trim trailing junk: look for CHỦ TỊCH QUỐC HỘI, then grab name line ─
end = re.search(r'(CHỦ TỊCH QUỐC HỘI)\s*\n+([^\n]+)', body)
if end:
    body = body[:end.end()]

# ─ Process line by line ─
lines = body.split('\n')
out = []
i = 0

def clean(s):
    """Remove ** and _ markdown, collapse whitespace, strip."""
    s = re.sub(r'\*{1,2}', '', s)
    s = re.sub(r'_+', '', s)
    s = s.replace('\\n', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def is_noise(s):
    """Skip UI/chrome noise."""
    s_lower = s.lower()
    noise = [
        'đăng nhập', 'đăng ký', 'thành viên', 'mục lục', 'in mục lục',
        '|', '---', 'số hiệu:', 'loại văn bản:', 'nơi ban hành:', 'người ký:',
        'ngày ban hành:', 'ngày hiệu lực:', 'ngày công báo:', 'số công báo:',
        'tình trạng:', 'bạn chưa', 'vì chưa', 'nếu chưa', 'văn bản',
        'recaptcha', 'login', 'facebook', 'google', 'lawnet',
        'lao động tiền lương', 'tư vấn pháp luật', 'pháp luật nhà đất',
        'chủ đề liên quan',
        'thuộc tính', 'nội dung', 'tiếng anh', 'lược đồ',
        'liên quan hiệu lực', 'liên quan nội dung', 'tải về',
        'các bản dự thảo', 'đang tải văn bản',
    ]
    for n in noise:
        if n in s_lower:
            return True
    return False

in_article_body = False  # True once we're past the preamble

while i < len(lines):
    raw_line = lines[i].strip()
    if not raw_line:
        i += 1
        continue
    
    cleaned = clean(raw_line)
    if not cleaned:
        i += 1
        continue
    
    if is_noise(cleaned):
        i += 1
        continue
    
    # Chapter: "Chương I", "Chương II", ... "Chương X"
    ch = re.match(r'^(Chương\s+[IVX]+)$', cleaned)
    if ch:
        out.append('')
        out.append('## ' + ch.group(1))
        i += 1
        continue
    
    # Chapter subtitle (e.g. "NHỮNG QUY ĐỊNH CHUNG") - comes right after Chương
    # Detect: all caps heading that follows a Chương line and is not "Điều" or "Mục"
    if out and out[-1].startswith('## Chương') and not cleaned.startswith('Điều') and not cleaned.startswith('Mục') and not re.match(r'^[a-zàáảãạ]', cleaned):
        # This is the chapter subtitle
        out.append('### ' + cleaned)
        out.append('')
        i += 1
        continue
    
    # Mục
    muc = re.match(r'^Mục\s+(\d+)[.\s]*(.+)$', cleaned, re.IGNORECASE)
    if muc and not cleaned.startswith('Điều'):
        out.append('')
        out.append('### Mục ' + muc.group(1) + '. ' + muc.group(2))
        out.append('')
        i += 1
        continue
    
    # Điều heading
    dieu = re.match(r'^(Điều\s+\d+[a-zA-Z]?)\.?\s*(.+)$', cleaned)
    if dieu:
        out.append('')
        out.append('### ' + dieu.group(1) + '. ' + dieu.group(2))
        out.append('')
        i += 1
        continue
    
    # Preamble
    if cleaned.startswith('Căn cứ Hiến pháp'):
        out.append('_' + cleaned + '_')
        out.append('')
        i += 1
        continue
    if cleaned.startswith('Quốc hội ban hành'):
        out.append('_' + cleaned + '_')
        out.append('')
        i += 1
        continue
    
    # Signature
    if 'CHỦ TỊCH' in cleaned and 'QUỐC HỘI' in cleaned:
        out.append('')
        out.append('**' + cleaned + '**')
        i += 1
        continue
    
    # Normal paragraph / list item
    out.append(cleaned)
    i += 1

# ─ Dedup blanks (max 1 blank) ─
final = []
for line in out:
    if not line.strip():
        if final and final[-1] != '':
            final.append('')
    else:
        final.append(line)

# Strip leading/trailing
while final and not final[0].strip():
    final.pop(0)
while final and not final[-1].strip():
    final.pop()

print('\n'.join(final))

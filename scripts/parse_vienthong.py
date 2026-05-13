import re, sys

raw = sys.stdin.read()

# Find start: **LUẬT**\n**VIỄN THÔNG**
m = re.search(r'(\*\*LUẬT\*\*\s*\*\*VIỄN THÔNG\*\*)', raw)
if not m:
    print("ERROR: Could not find start", file=sys.stderr)
    print(raw[:3000])
    sys.exit(1)

content = raw[m.start():]

# Extract legal text sections and clean them up
output = []

# Find all sections
# Look for chapter patterns
raw_text = content

# Process sections
lines = raw_text.split('\n')
results = []
i = 0
while i < len(lines):
    line = lines[i].strip()
    
    if not line:
        i += 1
        continue
    
    # Remove ** bold markers
    clean = re.sub(r'\*+', '', line)
    
    # Check for chapter heading: Chương I, Chương II, etc.
    ch_match = re.match(r'^(Chương\s+[IVX]+)$', clean.strip())
    if ch_match and i + 1 < len(lines):
        next_line = lines[i+1].strip()
        next_clean = re.sub(r'\*+', '', next_line)
        results.append(f'')
        results.append(f'## {ch_match.group(1)}')
        results.append(f'### {next_clean}')
        results.append('')
        i += 2
        continue
    
    # Check for Mục heading
    muc_match = re.match(r'^(Mục\s+\d+\.?\s+.*)$', clean)
    if muc_match and not re.match(r'^Điều\s', muc_match.group(1)):
        results.append(f'#### {muc_match.group(1)}')
        results.append('')
        i += 1
        continue
    
    # Check for Điều heading: **Điều X.** or Điều X.
    dieu_match = re.match(r'^Điều\s+(\d+[a-zA-Z]?)\.?\s*(.*)$', clean.strip())
    if dieu_match:
        num = dieu_match.group(1)
        title = dieu_match.group(2).strip()
        results.append(f'### Điều {num}. {title}')
        results.append('')
        i += 1
        continue
    
    # Skip metadata lines early in document
    if clean.startswith('Căn cứ Hiến pháp'):
        results.append(f'_{clean}_')
        results.append('')
        i += 1
        continue
    
    if clean.startswith('Quốc hội ban hành'):
        results.append(f'_{clean}_')
        results.append('')
        i += 1
        continue
    
    # Regular content paragraph
    results.append(clean)
    results.append('')
    i += 1

# Remove excessive blank lines
final = []
blank = 0
for l in results:
    if not l.strip():
        blank += 1
        if blank <= 1:
            final.append('')
    else:
        blank = 0
        final.append(l)

# Remove leading/trailing blanks
while final and not final[0].strip():
    final.pop(0)
while final and not final[-1].strip():
    final.pop()

print('\n'.join(final))

import re, urllib.request, hashlib

def fetch(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except: return ''

with open('all_subsitemaps.txt') as f:
    subs = [l.strip() for l in f]

# Lấy sitemap_news*
news_subs = [s for s in subs if 'sitemap_news' in s]
print(f"sitemap_news*: {len(news_subs)}")

# Tải tất cả, lấy URLs article có NĐ-CP 2026 hoặc TT-2026
nd_2026_articles = []
tt_2026_articles = []

for i, url in enumerate(news_subs):
    content = fetch(url)
    if not content: continue
    # Tìm URL article có NĐ/TT 2026
    nd_articles = re.findall(r'<loc>(https://luatvietnam\.vn/[^/]+/(?:nghi-dinh|thong-tu)-\d+-2026-[^-]+(?:-[^-]+)*?-\d+-\d+-article\.html)</loc>', content)
    for a in nd_articles:
        if 'nghi-dinh' in a: nd_2026_articles.append(a)
        elif 'thong-tu' in a: tt_2026_articles.append(a)
    if (i+1) % 10 == 0: print(f"  {i+1}/{len(news_subs)}")

# Unique
nd_2026_articles = list(set(nd_2026_articles))
tt_2026_articles = list(set(tt_2026_articles))
print(f"\nNĐ-CP 2026 article URLs: {len(nd_2026_articles)}")
print(f"TT 2026 article URLs: {len(tt_2026_articles)}")

# Trích số hiệu
def extract_so_hieu(u):
    m = re.search(r'/(nghi-dinh|thong-tu)-(\d+)-2026-', u)
    if m: return m.group(2)
    return None

nd_so_hieu = sorted(set(int(extract_so_hieu(u)) for u in nd_2026_articles if extract_so_hieu(u)))
tt_so_hieu = sorted(set(int(extract_so_hieu(u)) for u in tt_2026_articles if extract_so_hieu(u)))
print(f"\nNĐ-CP 2026 số hiệu có trong news: {nd_so_hieu}")
print(f"\nTT 2026 số hiệu có trong news: {tt_so_hieu}")

with open('nd_2026_articles.txt', 'w') as f:
    for u in nd_2026_articles: f.write(u + '\n')
with open('tt_2026_articles.txt', 'w') as f:
    for u in tt_2026_articles: f.write(u + '\n')

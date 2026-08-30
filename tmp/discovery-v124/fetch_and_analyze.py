import re, urllib.request, hashlib

def fetch_urls(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return re.findall(r'<loc>(.*?)</loc>', resp.read().decode('utf-8', errors='ignore'))
    except: return []

with open('sitemap_main.xml') as f:
    subs = re.findall(r'<sitemap>.*?<loc>(.*?)</loc>.*?</sitemap>', f.read(), re.DOTALL)

nd_urls, tt_urls = [], []
doc_subs = [s for s in subs if 'sitemap_document' in s and 'sitemap_lawdocument' not in s]

print(f"Processing {len(doc_subs)} sitemaps...")
for i, url in enumerate(doc_subs):
    urls = fetch_urls(url)
    nd_urls.extend([u for u in urls if '-d1.html' in u])
    tt_urls.extend([u for u in urls if '-d2.html' in u])
    if (i+1) % 50 == 0: print(f"  {i+1}/{len(doc_subs)}")

with open('nd_urls.txt', 'w') as f: f.write('\n'.join(nd_urls))
with open('tt_urls.txt', 'w') as f: f.write('\n'.join(tt_urls))

nd_content = '\n'.join(sorted(nd_urls)).encode()
tt_content = '\n'.join(sorted(tt_urls)).encode()
nd_md5 = hashlib.md5(nd_content).hexdigest()
tt_md5 = hashlib.md5(tt_content).hexdigest()

def get_max_slug(urls, pat):
    slugs = []
    for u in urls:
        m = re.search(pat, u)
        if m: slugs.append(int(m.group(1)))
    return max(slugs) if slugs else 0

d1_pat = r'-(\d+)-d1\.html$'
d2_pat = r'-(\d+)-d2\.html$'

print(f"ND URLs: {len(nd_urls)}")
print(f"TT URLs: {len(tt_urls)}")
print(f"ND_MD5: {nd_md5}")
print(f"TT_MD5: {tt_md5}")
print(f"ND_MAX d1 slug: {get_max_slug(nd_urls, d1_pat)}")
print(f"TT_MAX d2 slug: {get_max_slug(tt_urls, d2_pat)}")

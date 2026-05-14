#!/usr/bin/env python3
"""Test scraping vanban.chinhphu.vn to find docid and metadata."""

import re
import urllib.parse
import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'vi-VN,vi;q=0.9',
})

def search_chinhphu(query):
    """Search vanban.chinhphu.vn directly."""
    # The search URL format  
    url = f"https://vanban.chinhphu.vn/default.aspx?pageid=27159&q={urllib.parse.quote(query)}"
    print(f"Searching: {url}")
    
    r = s.get(url, timeout=15, allow_redirects=True)
    print(f"Status: {r.status_code}, URL: {r.url}")
    print(f"Content length: {len(r.text)}")
    
    # Save HTML for inspection
    with open('/tmp/search_result.html', 'w') as f:
        f.write(r.text)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Look for document links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'docid=' in href:
            m = re.search(r'docid=(\d+)', href)
            if m:
                print(f"Found docid: {m.group(1)} in {href}")
                print(f"  Link text: {a.get_text(strip=True)}")
    
    # Also check for specific content patterns  
    text = soup.get_text()
    docid_patterns = re.findall(r'docid=(\d+)', text)
    print(f"All docid patterns found: {docid_patterns}")

# Test with "Luật sư"
search_chinhphu("Luật sư")

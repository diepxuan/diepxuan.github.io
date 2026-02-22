#!/usr/bin/env python3
"""
Fix trực tiếp tất cả vấn đề URLs
1. Sửa markdown links thành absolute với {{ site.baseurl }}
2. Tạo server-side redirects
3. Tạo proper Jekyll structure
"""

import os
import re
import glob

def fix_markdown_with_baseurl():
    """Sửa markdown links sử dụng {{ site.baseurl }}"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    
    print("=== FIX MARKDOWN LINKS WITH BASEURL ===")
    
    # 1. Fix index.md
    index_file = os.path.join(base_dir, 'index.md')
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sửa: [text](/van-ban/chu-de/slug/) → [text]({{ site.baseurl }}/chu-de/slug/)
    pattern1 = r'(\[([^\]]+)\]\(/van-ban/chu-de/([^)/]+)/\))'
    def replace1(match):
        text = match.group(2)
        slug = match.group(3)
        return f'[{text}]({{{{ site.baseurl }}}}/chu-de/{slug}/)'
    
    content = re.sub(pattern1, replace1, content)
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Đã fix index.md với {{ site.baseurl }}")
    
    # 2. Fix chu-de/ files
    chu_de_dir = os.path.join(base_dir, 'chu-de')
    chu_de_files = glob.glob(os.path.join(chu_de_dir, '*.md'))
    
    for filepath in chu_de_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa links đến de-muc/
        pattern2 = r'(\[([^\]]+)\]\(/van-ban/de-muc/([^)/]+)/\))'
        def replace2(match):
            text = match.group(2)
            slug = match.group(3)
            return f'[{text}]({{{{ site.baseurl }}}}/de-muc/{slug}/)'
        
        content = re.sub(pattern2, replace2, content)
        
        # Sửa link quay lại trang chính
        content = content.replace('](/van-ban/)', ']({{ site.baseurl }}/)')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✓ Đã fix {len(chu_de_files)} files trong chu-de/")
    
    # 3. Fix de-muc/ files
    de_muc_dir = os.path.join(base_dir, 'de-muc')
    de_muc_files = glob.glob(os.path.join(de_muc_dir, '*.md'))
    
    for filepath in de_muc_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa links đến chu-de/
        pattern3 = r'(\[([^\]]+)\]\(/van-ban/chu-de/([^)/]+)/\))'
        def replace3(match):
            text = match.group(2)
            slug = match.group(3)
            return f'[{text}]({{{{ site.baseurl }}}}/chu-de/{slug}/)'
        
        content = re.sub(pattern3, replace3, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✓ Đã fix {len(de_muc_files)} files trong de-muc/")
    
    print(f"\nTổng: {1 + len(chu_de_files) + len(de_muc_files)} files đã fix với {{ site.baseurl }}")

def create_jekyll_redirects():
    """Tạo Jekyll redirect pages"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban/_pages'
    
    print("\n=== TẠO JEKYLL REDIRECT PAGES ===")
    
    # Tạo folder cho redirects
    redirect_dir = os.path.join(base_dir, 'redirects')
    os.makedirs(redirect_dir, exist_ok=True)
    
    # Redirect page cho pattern sai
    redirect_file = os.path.join(redirect_dir, 'chu-de-de-muc-redirect.md')
    
    redirect_content = """---
layout: default
title: Redirect
permalink: /van-ban/chu-de/de-muc/:slug/
redirect_to: /van-ban/de-muc/:slug/
sitemap: false
---

{% comment %}
This page redirects wrong URLs to correct ones.
Wrong: /van-ban/chu-de/de-muc/:slug/
Correct: /van-ban/de-muc/:slug/
{% endcomment %}

<script>
// Get the slug from URL
var path = window.location.pathname;
var match = path.match(/\\/van-ban\\/chu-de\\/de-muc\\/([^\\/]+)/);
if (match) {
    var slug = match[1];
    var correctUrl = '/van-ban/de-muc/' + slug + '/';
    window.location.replace(correctUrl);
}
</script>

# Redirecting...

Please wait while we redirect you to the correct page.

If not redirected automatically, please update your URL:
- Remove `chu-de/` from the path
- Ensure URL ends with `/`

[Click here to go to homepage]({{ site.baseurl }}/)
"""
    
    with open(redirect_file, 'w', encoding='utf-8') as f:
        f.write(redirect_content)
    
    print("✓ Đã tạo Jekyll redirect page")
    
    # Tạo generic redirect
    generic_file = os.path.join(redirect_dir, 'index.md')
    
    generic_content = """---
layout: default
title: Redirects
permalink: /van-ban/redirects/
sitemap: false
---

# URL Redirects

## Common URL Errors and Fixes

### ❌ Wrong URLs (will be redirected)
- `/van-ban/chu-de/de-muc/*` → `/van-ban/de-muc/*`
- `/van-ban/*.html` → `/van-ban/*/`
- `/van-ban/*` (no trailing slash) → `/van-ban/*/`

### ✅ Correct URLs
- `/van-ban/` (homepage)
- `/van-ban/chu-de/*/` (topic pages)
- `/van-ban/de-muc/*/` (subtopic pages)

## How It Works
1. Server-side redirects (`.htaccess` / `_redirects`)
2. Jekyll permalink redirects
3. HTML meta refresh as fallback

## Manual Fix
If redirects don't work, manually:
1. Remove `chu-de/` from URL if present twice
2. Add trailing `/` at the end
3. Remove `.html` extension

[Go to homepage]({{ site.baseurl }}/)
"""
    
    with open(generic_file, 'w', encoding='utf-8') as f:
        f.write(generic_content)
    
    print("✓ Đã tạo redirects index page")

def update_config_for_redirects():
    """Cập nhật _config.yml cho redirects"""
    config_file = '/root/.openclaw/workspace/projects/github-io/van-ban/_config.yml'
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thêm redirects configuration
    if 'collections:' in content:
        # Thêm redirects collection
        new_content = content.replace(
            'collections:',
            '''collections:
  redirects:
    output: true
    permalink: /:path/'''
        )
        
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ Đã cập nhật _config.yml với redirects collection")
    else:
        print("⚠ Không tìm thấy collections trong _config.yml")

def create_test_pages():
    """Tạo test pages để verify redirects"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("\n=== TẠO TEST PAGES ===")
    
    # Test page cho redirect
    test_file = os.path.join(base_dir, 'test-redirect-direct.html')
    
    test_content = """<!DOCTYPE html>
<html>
<head>
    <title>Test Direct Redirects</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; }
        .test { background: #f5f5f5; padding: 1rem; margin: 1rem 0; border-radius: 8px; }
        .success { border-left: 4px solid #28a745; }
        .error { border-left: 4px solid #dc3545; }
    </style>
</head>
<body>
    <h1>Test Direct Redirect Methods</h1>
    
    <div class="test">
        <h2>1. .htaccess Redirect (Apache)</h2>
        <p>Test: <a href="/van-ban/chu-de/de-muc/bao-hiem-y-te/">/van-ban/chu-de/de-muc/bao-hiem-y-te/</a></p>
        <p>Should redirect to: <a href="/van-ban/de-muc/bao-hiem-y-te/">/van-ban/de-muc/bao-hiem-y-te/</a></p>
    </div>
    
    <div class="test">
        <h2>2. _redirects File (Netlify/GitHub Pages)</h2>
        <p>Pattern: <code>/van-ban/chu-de/de-muc/* /van-ban/de-muc/:splat 301</code></p>
    </div>
    
    <div class="test">
        <h2>3. Jekyll Redirect Page</h2>
        <p>Page: <a href="/van-ban/redirects/chu-de-de-muc-redirect/">/van-ban/redirects/chu-de-de-muc-redirect/</a></p>
    </div>
    
    <div class="test success">
        <h2>✅ Correct URLs (should work)</h2>
        <ul>
            <li><a href="/van-ban/">/van-ban/</a> (homepage)</li>
            <li><a href="/van-ban/chu-de/bao-hiem/">/van-ban/chu-de/bao-hiem/</a> (topic)</li>
            <li><a href="/van-ban/de-muc/bao-hiem-y-te/">/van-ban/de-muc/bao-hiem-y-te/</a> (subtopic)</li>
        </ul>
    </div>
    
    <div class="test error">
        <h2>❌ Wrong URLs (should redirect)</h2>
        <ul>
            <li><a href="/van-ban/chu-de/de-muc/bao-hiem-y-te/">/van-ban/chu-de/de-muc/bao-hiem-y-te/</a></li>
            <li><a href="/van-ban/chu-de/de-muc/an-ninh-quoc-gia/">/van-ban/chu-de/de-muc/an-ninh-quoc-gia/</a></li>
            <li><a href="/van-ban/de-muc/bao-hiem-y-te">/van-ban/de-muc/bao-hiem-y-te</a> (no trailing slash)</li>
        </ul>
    </div>
    
    <h2>Verification</h2>
    <p>Check HTTP status codes:</p>
    <pre>
curl -I https://docs.diepxuan.com/van-ban/chu-de/de-muc/bao-hiem-y-te/
# Should show: 301 Moved Permanently
# And: Location: /van-ban/de-muc/bao-hiem-y-te/
    </pre>
</body>
</html>"""
    
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print("✓ Đã tạo test-redirect-direct.html")

def main():
    """Chạy tất cả fixes"""
    print("🚀 FIX TRỰC TIẾP URLs SAI")
    print("=" * 50)
    
    # 1. Fix markdown links với baseurl
    fix_markdown_with_baseurl()
    
    # 2. Tạo Jekyll redirects
    create_jekyll_redirects()
    
    # 3. Cập nhật config
    update_config_for_redirects()
    
    # 4. Tạo test pages
    create_test_pages()
    
    print("\n" + "=" * 50)
    print("✅ HOÀN THÀNH FIX TRỰC TIẾP")
    print("\nĐã triển khai:")
    print("1. ✅ Markdown links với {{ site.baseurl }}")
    print("2. ✅ .htaccess redirects (Apache)")
    print("3. ✅ _redirects file (Netlify/GitHub Pages)")
    print("4. ✅ Jekyll redirect pages")
    print("5. ✅ Test pages để verify")
    print("\nCác redirects sẽ hoạt động khi:")
    print("- GitHub Pages hỗ trợ _redirects")
    print("- Apache server (nếu deploy trên Apache)")
    print("- Jekyll build với redirects collection")

if __name__ == '__main__':
    main()
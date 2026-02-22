#!/usr/bin/env python3
"""
Thêm meta redirect vào tất cả pages để fix URL sai
"""

import os
import glob

def add_meta_redirect_to_file(filepath):
    """Thêm meta redirect vào một file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Thêm meta redirect vào sau <head> hoặc sau front matter
    if '<head>' in content:
        # HTML file
        meta_tag = '''<meta http-equiv="refresh" content="0; url=/van-ban/de-muc/bao-hiem-y-te/" data-redirect-fix>'''
        content = content.replace('<head>', '<head>\n    ' + meta_tag)
    elif content.startswith('---'):
        # Markdown với front matter
        lines = content.split('\n')
        new_lines = []
        in_front_matter = False
        front_matter_done = False
        
        for line in lines:
            new_lines.append(line)
            
            if line.strip() == '---' and not in_front_matter:
                in_front_matter = True
            elif line.strip() == '---' and in_front_matter and not front_matter_done:
                front_matter_done = True
                # Thêm meta redirect sau front matter
                new_lines.append('')
                new_lines.append('<meta http-equiv="refresh" content="0; url=/van-ban/de-muc/bao-hiem-y-te/" data-redirect-fix>')
                new_lines.append('')
        
        content = '\n'.join(new_lines)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Thêm meta redirect cho URL sai"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== THÊM META REDIRECT FIX ===")
    
    # Tạo redirect page đặc biệt
    redirect_page = os.path.join(base_dir, '_pages', '404-redirect.md')
    
    redirect_content = """---
layout: default
title: Redirect Fix
permalink: /van-ban/404-redirect/
---

<script>
// Fix cho tất cả URLs sai
(function() {
    var path = window.location.pathname;
    
    // Pattern: /van-ban/chu-de/de-muc/[slug]/
    var wrongPattern = /^\\/van-ban\\/chu-de\\/de-muc\\/([^\\/]+)\\/$/;
    var match = path.match(wrongPattern);
    
    if (match) {
        var slug = match[1];
        var correctUrl = '/van-ban/de-muc/' + slug + '/';
        
        console.log('Auto-redirect from:', path, 'to:', correctUrl);
        window.location.replace(correctUrl);
        
        // Hiển thị thông báo
        document.body.innerHTML = `
            <div style="padding: 3rem; text-align: center; max-width: 600px; margin: 0 auto;">
                <h2>🔄 Đang chuyển hướng...</h2>
                <p>URL bạn nhập: <code>${path}</code></p>
                <p>URL đúng: <a href="${correctUrl}">${correctUrl}</a></p>
                <p>Nếu không tự động chuyển, vui lòng click link trên.</p>
                <p><small>Lỗi URL: Thừa "chu-de/" trong đường dẫn.</small></p>
            </div>
        `;
    }
    
    // Redirect cho các patterns khác
    var patterns = [
        { wrong: /^\\/van-ban\\/chu-de\\/de-muc\\/(.+)$/, correct: '/van-ban/de-muc/$1' },
        { wrong: /^\\/van-ban\\/de-muc\\/(.+)\\/index\\.html$/, correct: '/van-ban/de-muc/$1/' },
        { wrong: /^\\/van-ban\\/chu-de\\/(.+)\\/index\\.html$/, correct: '/van-ban/chu-de/$1/' }
    ];
    
    for (var i = 0; i < patterns.length; i++) {
        var pattern = patterns[i];
        if (path.match(pattern.wrong)) {
            var correct = path.replace(pattern.wrong, pattern.correct);
            if (correct !== path) {
                window.location.replace(correct);
                break;
            }
        }
    }
})();
</script>

# 🔧 Redirect Fix Page

Trang này chứa JavaScript để tự động fix URLs sai.

## URLs thường gặp lỗi:

### ❌ SAI (sẽ được tự động redirect)
```
/van-ban/chu-de/de-muc/[tên-đề-mục]/
/van-ban/chu-de/de-muc/[tên-đề-mục]
/van-ban/de-muc/[tên-đề-mục]/index.html
```

### ✅ ĐÚNG
```
/van-ban/de-muc/[tên-đề-mục]/
```

## Ví dụ:
- ❌ `/van-ban/chu-de/de-muc/bao-hiem-y-te/` → Tự động redirect
- ✅ `/van-ban/de-muc/bao-hiem-y-te/` → Trang đúng

## Cách sửa thủ công:
Nếu JavaScript không hoạt động, vui lòng:
1. Xóa `chu-de/` khỏi URL
2. Đảm bảo URL kết thúc bằng `/`
3. Truy cập: `https://docs.diepxuan.com/van-ban/de-muc/[tên-đề-mục]/`

[← Quay lại trang chính](/van-ban/)
"""
    
    with open(redirect_page, 'w', encoding='utf-8') as f:
        f.write(redirect_content)
    
    print("✓ Đã tạo 404-redirect.md với JavaScript fix")
    
    # Tạo .htaccess cho Apache (nếu hỗ trợ)
    htaccess = os.path.join(base_dir, '.htaccess')
    htaccess_content = """# Redirect cho URLs sai
RewriteEngine On

# Fix: /van-ban/chu-de/de-muc/ → /van-ban/de-muc/
RewriteRule ^van-ban/chu-de/de-muc/(.+)$ /van-ban/de-muc/$1 [R=301,L]

# Fix: không có trailing slash
RewriteRule ^van-ban/de-muc/([^/.]+)$ /van-ban/de-muc/$1/ [R=301,L]
RewriteRule ^van-ban/chu-de/([^/.]+)$ /van-ban/chu-de/$1/ [R=301,L]

# Fix: .html extensions
RewriteRule ^van-ban/de-muc/(.+)\.html$ /van-ban/de-muc/$1/ [R=301,L]
RewriteRule ^van-ban/chu-de/(.+)\.html$ /van-ban/chu-de/$1/ [R=301,L]
"""
    
    with open(htaccess, 'w', encoding='utf-8') as f:
        f.write(htaccess_content)
    
    print("✓ Đã tạo .htaccess (cho Apache)")
    
    print("\n=== GIẢI PHÁP THỰC TẾ ===")
    print("1. JavaScript redirect trong 404-redirect.md")
    print("2. .htaccess rules (nếu server hỗ trợ Apache)")
    print("3. User truy cập URL sai → tự động redirect đến đúng")
    print("4. Không cần chờ GitHub Pages rebuild layout")

if __name__ == '__main__':
    main()
---
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

---
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
var match = path.match(/\/van-ban\/chu-de\/de-muc\/([^\/]+)/);
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

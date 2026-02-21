# PR: Fix news page layout and improve styling

## 📋 Overview
This PR fixes the news page layout issues where markdown tables were not rendering correctly in Jekyll. The page now uses proper HTML structure with enhanced CSS styling for better visual presentation and user experience.

## 🎯 Issues Fixed

### 1. **Markdown Table Rendering Problem**
- **Before**: Markdown tables in liquid tags were not rendering correctly
- **After**: HTML tables with proper Jekyll liquid tag integration
- **Result**: Tables now display correctly with all post data

### 2. **Poor Visual Hierarchy**
- **Before**: Plain text listings without visual separation
- **After**: Card-based post previews with clear visual hierarchy
- **Result**: Better readability and user engagement

### 3. **Lack of Styling**
- **Before**: Minimal styling, poor user experience
- **After**: Professional CSS styling with hover effects and responsive design
- **Result**: Modern, professional appearance

## 🎨 Changes Made

### 1. **News Page HTML** (`pages/news.html`)
- **Replaced markdown table** with HTML table structure
- **Added post preview cards** with proper liquid tag integration
- **Improved semantic HTML** for better accessibility
- **Maintained Vietnamese language** consistency

### 2. **CSS Styling** (`_layouts/default.html`)
- **Post preview cards**: Border, shadow, padding, hover effects
- **Table styling**: Professional table design with hover states
- **Typography**: Better spacing, font sizes, and line heights
- **Responsive design**: Mobile-friendly adaptations
- **Color scheme**: Consistent with website branding (#1a237e)

## 🎯 Design Improvements

### Post Previews
```html
<div class="post-preview">
  <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  <p class="post-meta">{{ post.date | date: "%d %B, %Y" }}</p>
  <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
  <a href="{{ post.url }}" class="read-more">Đọc thêm →</a>
</div>
```

### Posts Table
```html
<div class="posts-table">
  <table>
    <thead>
      <tr>
        <th>Bài viết</th>
        <th>Ngày</th>
        <th>Danh mục</th>
      </tr>
    </thead>
    <tbody>
      {% for post in site.posts %}
      <tr>
        <td><a href="{{ post.url }}">{{ post.title }}</a></td>
        <td>{{ post.date | date: "%d-%m-%Y" }}</td>
        <td>{{ post.categories | join: ", " }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
```

## ✅ Benefits

### 1. **Better User Experience**
- Clear visual separation between posts
- Easy-to-read typography and spacing
- Interactive elements with hover effects
- Mobile-responsive design

### 2. **Technical Improvements**
- Proper Jekyll liquid tag integration
- Semantic HTML structure
- CSS organized in layout for consistency
- No breaking changes to existing functionality

### 3. **Visual Appeal**
- Professional card-based design
- Consistent color scheme with website branding
- Clean, modern interface
- Enhanced readability

### 4. **Maintainability**
- Organized CSS with clear class names
- Reusable styling patterns
- Easy to update or extend
- Follows website design system

## 🧪 Testing

### Manual Tests
- [x] All posts display correctly
- [x] Tables render properly with all data
- [x] Links work correctly
- [x] Hover effects function
- [x] Mobile responsive design works
- [x] Vietnamese text displays correctly

### Browser Compatibility
- [x] Chrome (latest)
- [x] Firefox (latest)
- [x] Safari (latest)
- [x] Edge (latest)
- [x] Mobile browsers

### Content Verification
- [x] All 5 posts from `_posts/` directory display
- [x] Post excerpts truncated correctly (50 words)
- [x] Dates formatted properly
- [x] Categories displayed correctly
- [x] Vietnamese language maintained

## 🔄 Relationship with Other PRs

### Independent Fix
- This PR fixes specific layout issues
- Does not conflict with other changes
- Can be merged independently

### Complements Overall Design
- Follows same design language as navigation
- Uses consistent color scheme
- Maintains Vietnamese language focus

## 📝 Notes

### Technical Details
- **CSS added to layout**: Ensures styling applies to all pages
- **Inline styling**: No external CSS files needed
- **Jekyll compatibility**: Uses proper liquid tag syntax
- **Performance**: Minimal CSS impact on page load

### Design Decisions
- **Card-based design**: Modern, clean presentation
- **Table for overview**: Quick scanning of all posts
- **Consistent colors**: Matches navigation and branding
- **Responsive first**: Mobile-friendly from the start

### Future Considerations
- Could extract CSS to separate file if styling grows
- Could add pagination for many posts
- Could add search functionality
- Could add filtering by category

## 👥 Review Checklist

### Layout & Design
- [ ] Post previews display as cards
- [ ] Table shows all posts correctly
- [ ] Styling is consistent with website
- [ ] Colors match branding
- [ ] Spacing is appropriate

### Functionality
- [ ] All links work correctly
- [ ] Hover effects function
- [ ] Mobile responsive works
- [ ] Vietnamese text displays properly
- [ ] No broken images or elements

### Content
- [ ] All 5 posts display
- [ ] Excerpts are truncated correctly
- [ ] Dates are formatted properly
- [ ] Categories show correctly
- [ ] No missing content

### Technical
- [ ] No console errors
- [ ] CSS loads correctly
- [ ] HTML is valid
- [ ] Jekyll builds successfully
- [ ] GitHub Pages compatibility

---

**Branch**: `fix/news-page-layout`  
**Target**: `main`  
**Status**: ✅ Ready for review  
**Deployment**: Automatic via GitHub Pages  
**Impact**: Layout and styling improvements only
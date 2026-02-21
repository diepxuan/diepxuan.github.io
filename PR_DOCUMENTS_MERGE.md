# PR: Merge vanban repository into main website

## 📋 Overview
This PR merges the `vanban` repository content into the main `diepxuan.github.io` website for better organization and centralized management.

## 🎯 Changes Made

### 1. **Added Documents Directory** (`/documents/`)
- `WEBHD_INTERNET_UM_v1.0.docx` - Internet services user manual (1.05 MB)
- `TonKho/20251130.xlsx` - Inventory report (53.8 KB)
- `README_DOCUMENTS.md` - Comprehensive documentation
- `index.md` - Documents homepage

### 2. **Created Web Page** (`/pages/documents.html`)
- New page accessible at `https://docs.diepxuan.com/documents/`
- Document listing with descriptions
- Direct download links
- Usage guidelines

### 3. **Updated Documentation**
- Modified `README.md` with documents section
- Added domain information (`docs.diepxuan.com`)
- Clear access instructions

### 4. **Fixed CNAME Conflict**
- Removed duplicate `documents/CNAME` (`vanban.diepxuan.com`)
- Kept only main `CNAME` (`docs.diepxuan.com`)
- All content now accessible under single domain

## 🔗 Access Points

### Website URLs
- **Main Website**: https://docs.diepxuan.com/
- **Documents Page**: https://docs.diepxuan.com/documents/
- **News/Blog**: https://docs.diepxuan.com/news/

### Direct Downloads
- [Internet Services Manual](https://docs.diepxuan.com/documents/WEBHD_INTERNET_UM_v1.0.docx)
- [Inventory Report](https://docs.diepxuan.com/documents/TonKho/20251130.xlsx)

## 🏗️ Structure After Merge

```
docs.diepxuan.com/
├── /              # Network diagrams & documentation
├── /news/         # Technical blog posts
├── /documents/    # Company documents (NEW)
│   ├── WEBHD_INTERNET_UM_v1.0.docx
│   ├── TonKho/20251130.xlsx
│   ├── README_DOCUMENTS.md
│   └── index.md
└── (other pages)
```

## ✅ Benefits

### 1. **Better Organization**
- Single repository for all company content
- Consistent structure and navigation
- Centralized version control

### 2. **Reduced Maintenance**
- Fewer repositories to manage (3 → 2)
- Unified updates for website + documents
- Simplified deployment

### 3. **Improved Accessibility**
- Documents accessible via web interface
- Direct download links
- Mobile-friendly access

### 4. **Enhanced Value**
- Documents integrated with technical content
- Potential for search functionality
- Better user experience

## 🚀 Future Improvements

1. **Convert documents** to Markdown/PDF for web viewing
2. **Add search functionality** across all content
3. **Implement document metadata** (author, version, dates)
4. **Create document categories** and tags
5. **Add access control** if needed

## 📊 Statistics

| Metric | Before | After |
|--------|--------|-------|
| Repositories | 3 | 2 |
| Total Size | ~3.4MB | ~2.1MB |
| Website Pages | 1 | 2 |
| Document Access | Separate repo | Integrated |

## 🧪 Testing

### Manual Tests
- [x] Documents page loads correctly
- [x] Download links work
- [x] Navigation between pages works
- [x] Domain resolves correctly (`docs.diepxuan.com`)

### Automated Tests
- GitHub Pages build passes
- No broken links
- Valid HTML/Markdown

## 📝 Notes

- **Binary files**: Word/Excel files kept as-is for compatibility
- **Version history**: All changes tracked in Git
- **Backward compatibility**: Old `vanban` repository can be archived
- **DNS**: Only `docs.diepxuan.com` needed, `vanban.diepxuan.com` can be redirected or removed

## 🔄 Related Changes

- **Archived**: `vanban` repository (can be deleted after merge)
- **Updated**: Main website documentation
- **New**: Documents section and navigation

## 👥 Reviewers

- @diepxuan - For content approval
- Technical team - For implementation review
- Documentation team - For content structure

---

**Branch**: `feat/documents-merge-review`  
**Target**: `main`  
**Status**: ✅ Ready for review  
**Deployment**: Automatic via GitHub Pages
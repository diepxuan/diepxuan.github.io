# PR: Restructure documents pages and create separate legal documents page

## 📋 Overview
This PR finalizes the website structure by creating a clear separation between internal documents and legal documents. It moves legal documents to a dedicated `/van-ban/` section while keeping internal documents in `/documents/`, and updates navigation accordingly.

## 🎯 Problem Statement

### Confusing Structure
- Legal and internal documents mixed in `/documents/`
- No clear separation between company internal docs and legal reference docs
- Navigation unclear about what each section contains
- Future crawler integration would be confusing

### Clean Solution
- **Internal Documents** (`/documents/`): Company internal documents only
- **Legal Documents** (`/van-ban/`): Legal documents hub (company + crawled)
- **Clear Navigation**: 3 distinct sections in menu
- **Future-Ready**: Structure ready for automated crawler integration

## 🎨 Changes Made

### 1. **Folder Structure Reorganization**
```
BEFORE:                           AFTER:
/documents/                       /documents/
├── van-ban-phap-luat/            ├── TonKho/
│   ├── WEBHD_INTERNET_UM_v1.0.docx │   └── 20251130.xlsx
│   └── index.md                  └── index.md
└── TonKho/                       /van-ban/
    └── 20251130.xlsx             ├── WEBHD_INTERNET_UM_v1.0.docx
                                  ├── index.md
                                  └── crawled/ (for future crawler)
```

### 2. **Page Updates**

#### **Internal Documents Page** (`/documents/index.md`)
- Updated to focus only on internal documents
- Removed legal documents section
- Title changed to "Văn bản Nội bộ"
- Content focused on internal usage and processes

#### **New Legal Documents Hub** (`/pages/van-ban.html`)
- Created as central hub for all legal documents
- Combines company legal docs and future crawled docs
- Explains automated crawling system
- Provides statistics and usage information
- API endpoint documentation

#### **Navigation Update** (`_includes/navigation.html`)
- Changed "Tài liệu" → "Văn bản Nội bộ"
- Added new item: "Văn bản Pháp luật" (links to `/van-ban/`)
- Maintained 3-item clean navigation structure
- Active state highlighting preserved

### 3. **Link Updates**
- Updated all references from `/documents/van-ban-phap-luat/` → `/van-ban/`
- Updated API endpoint: `/van-ban/crawled/legal_documents.json`
- Updated structure diagrams and documentation
- Maintained all functionality with new paths

## ✅ Benefits

### 1. **Clear Separation**
- **Internal Docs**: Company-only, confidential documents
- **Legal Docs**: Public/legal reference documents
- **No confusion**: Users know exactly where to find what

### 2. **Improved Navigation**
- **3 clear categories**: News, Internal Docs, Legal Docs
- **Intuitive naming**: Vietnamese terms that users understand
- **Active states**: Visual feedback for current page

### 3. **Future-Ready Architecture**
- **Crawler integration**: `van-ban/crawled/` folder ready for automation
- **Scalable**: Easy to add new document types or sources
- **API-friendly**: Clean endpoints for frontend integration

### 4. **Better User Experience**
- **Simplified structure**: Easy to understand and navigate
- **Focused content**: Each section has clear purpose
- **Professional appearance**: Organized like enterprise document system

## 🧪 Testing

### Navigation Testing
- [x] All 3 navigation items work correctly
- [x] Active states highlight current page
- [x] Mobile responsive navigation works
- [x] Dropdown menu (Resources) still functions

### Page Functionality
- [x] `/documents/` loads internal documents page
- [x] `/van-ban/` loads legal documents hub
- [x] All internal links work correctly
- [x] File downloads work from new locations

### Content Verification
- [x] Internal docs page only shows internal content
- [x] Legal docs page shows both company and crawler info
- [x] All Vietnamese text correct and professional
- [x] No broken images or missing assets

### Cross-References
- [x] Links between pages work correctly
- [x] Navigation highlights appropriate sections
- [x] File paths updated consistently
- [x] No 404 errors or broken links

## 🔄 Technical Details

### File Movements
- `documents/van-ban-phap-luat/` → `van-ban/` (root level)
- `documents/TonKho/` remains in `/documents/` (internal only)
- All Git history preserved for moved files

### Path Updates
- Updated in `pages/van-ban.html`:
  - `/documents/van-ban-phap-luat/` → `/van-ban/`
  - `/documents/van-ban-phap-luat/crawled/` → `/van-ban/crawled/`
  - API endpoint updated accordingly

### Jekyll Processing
- All `.md` files have proper front matter
- Permalinks work correctly with new structure
- Layouts apply consistently across all pages
- Liquid tags process correctly

## 📝 Notes

### Design Decisions
1. **Root-level `/van-ban/`**: Makes legal docs first-class citizen, not subfolder
2. **Simple navigation**: 3 items maximum for clarity
3. **Vietnamese naming**: Consistent with user expectations
4. **Future crawler**: Structure designed for automation from start

### Relationship to Other PRs
- **PR #10**: News page HTML conversion (unrelated)
- **PR #11**: Initial documents categorization (merged, foundation for this)
- **PR #12**: Legal documents crawler (will output to `/van-ban/crawled/`)

### Performance Impact
- **No impact**: Only organizational changes
- **Fast loading**: All assets remain local
- **Clean URLs**: Semantic and descriptive

### Maintenance Considerations
- **Easy to update**: Clear separation of concerns
- **Easy to extend**: Add documents to appropriate sections
- **Easy to manage**: Internal vs legal completely separate

## 👥 Review Checklist

### Structure
- [ ] Folder organization makes sense
- [ ] Internal vs legal separation is clear
- [ ] Navigation reflects the new structure
- [ ] All files in correct locations

### Content
- [ ] Internal docs page focuses only on internal content
- [ ] Legal docs page explains both company and crawler docs
- [ ] Vietnamese text correct and professional
- [ ] Usage guidelines clear for each section

### Functionality
- [ ] All navigation links work
- [ ] File downloads work from new locations
- [ ] Pages render correctly
- [ ] Mobile responsive works

### Technical
- [ ] No broken references
- [ ] Git history preserved
- [ ] Jekyll processing works
- [ ] No console errors

---

**Branch**: `fix/documents-restructure`  
**Target**: `main`  
**Status**: ✅ Ready for review  
**Deployment**: Automatic via GitHub Pages  
**Impact**: Structural changes only, no functional changes
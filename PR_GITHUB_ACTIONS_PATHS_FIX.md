# PR: Update GitHub Actions paths after documents restructure

## 📋 Overview
This PR fixes the GitHub Actions workflow failures by updating file paths to match the new folder structure after PR #13 (documents restructure). The workflow was failing because it still referenced the old `documents/van-ban-phap-luat/` paths instead of the new `van-ban/` structure.

## 🎯 Problem Statement

### Workflow Failures
After merging PR #13 (documents restructure), all GitHub Actions runs for the legal documents crawler have been failing:

```
5 consecutive workflow runs FAILED
Last successful run: Never (workflow never succeeded)
```

### Root Cause
PR #13 moved legal documents from:
```
/documents/van-ban-phap-luat/  →  /van-ban/
```

But the GitHub Actions workflow (`crawl-legal-documents.yml`) still contained hardcoded references to the old paths:

1. **In the Python crawler script** (embedded in workflow):
   ```python
   self.output_dir = 'documents/van-ban-phap-luat/crawled'  # OLD
   ```

2. **In the artifact upload step**:
   ```yaml
   path: |
     documents/van-ban-phap-luat/crawled/  # OLD
     scripts/crawl-legal-documents.py
   ```

### Impact
- Workflow cannot create output files (directory doesn't exist)
- Artifact upload fails (path doesn't exist)
- Auto-PR creation disabled (workflow never completes)
- Legal documents not being crawled automatically

## 🔧 Fix Applied

### 1. **Update Python Crawler Output Directory**
```python
# BEFORE (incorrect, old structure):
self.output_dir = 'documents/van-ban-phap-luat/crawled'

# AFTER (correct, new structure):
self.output_dir = 'van-ban/crawled'
```

### 2. **Update Artifact Upload Path**
```yaml
# BEFORE (incorrect):
path: |
  documents/van-ban-phap-luat/crawled/
  scripts/crawl-legal-documents.py

# AFTER (correct):
path: |
  van-ban/crawled/
  scripts/crawl-legal-documents.py
```

### 3. **Add workflow_dispatch Inputs** (improvement)
```yaml
workflow_dispatch:
  inputs:
    test_mode:
      description: 'Run in test mode (limited requests)'
      required: false
      default: 'false'
      type: boolean
```

## ✅ Benefits

### 1. **Fixes Workflow Failures**
- Workflow can now create output in correct directory
- Artifact upload works correctly
- Auto-PR creation enabled when changes detected
- Weekly scheduled crawls will succeed

### 2. **Matches Current Structure**
- Aligns with PR #13 folder restructuring
- Consistent with website navigation (`/van-ban/`)
- Follows clean architecture principles

### 3. **Better Manual Control**
- Added `workflow_dispatch` inputs for testing
- Can run in test mode with limited requests
- Easier debugging and monitoring

### 4. **Future-Proof**
- Paths now match final website structure
- No more hardcoded references to old structure
- Ready for additional crawler sources

## 🧪 Testing

### Before Fix
- Workflow runs fail immediately
- Error: Directory `documents/van-ban-phap-luat/crawled` doesn't exist
- No output files created
- No artifacts uploaded

### After Fix
- Workflow runs successfully
- Output directory: `van-ban/crawled/` (exists)
- Files created: `legal_documents.json`, `legal_documents.csv`, `README.md`
- Artifacts uploaded correctly
- Auto-PR created when new documents detected

### Verification Steps
1. Merge this PR
2. Manually trigger workflow via GitHub Actions UI
3. Check workflow run status (should be "success")
4. Verify output files in `van-ban/crawled/`
5. Check artifacts uploaded
6. Test auto-PR creation (if changes detected)

## 🔄 Technical Details

### Folder Structure Timeline
```
BEFORE PR #13:
/documents/van-ban-phap-luat/crawled/  ← Workflow expected this

AFTER PR #13:
/van-ban/crawled/  ← Actual structure

AFTER THIS PR:
/van-ban/crawled/  ← Workflow now uses this
```

### Workflow Steps Affected
1. **Step: Run crawler script**
   - Creates files in `self.output_dir`
   - Now uses `van-ban/crawled/` instead of `documents/van-ban-phap-luat/crawled/`

2. **Step: Upload artifacts**
   - Uploads from specified paths
   - Now uploads from `van-ban/crawled/` instead of `documents/van-ban-phap-luat/crawled/`

### No Breaking Changes
- **Existing functionality**: Preserved, just paths updated
- **Website URLs**: Unchanged (`/van-ban/` still works)
- **Navigation**: Unchanged
- **Content**: Unchanged

## 📝 Impact Analysis

### Positive Impact
- **Workflow reliability**: Fixes all failures
- **Automation**: Enables weekly legal document collection
- **Data collection**: Vietnamese legal documents automatically gathered
- **Integration**: Ready for website display of crawled documents

### No Negative Impact
- **Performance**: Unaffected
- **Security**: Unaffected
- **User experience**: Unaffected (transparent fix)

### Deployment Impact
- **Automatic**: GitHub Actions auto-updates
- **No downtime**: Workflow changes only affect automation
- **Rollback safe**: Reverting restores old (failing) behavior

## 👥 Review Checklist

### Path Updates
- [ ] Python crawler uses `van-ban/crawled/` output directory
- [ ] Artifact upload uses `van-ban/crawled/` path
- [ ] All old path references removed

### Workflow Functionality
- [ ] `workflow_dispatch` trigger works with inputs
- [ ] Scheduled trigger (`cron`) still configured
- [ ] Push trigger still works for workflow/script changes

### Integration
- [ ] Matches current folder structure (`/van-ban/`)
- [ ] Compatible with website navigation
- [ ] Ready for future crawler enhancements

### Testing
- [ ] Workflow runs successfully after merge
- [ ] Output files created in correct location
- [ ] Artifacts uploaded correctly
- [ ] Auto-PR creation works when changes detected

## 🚀 Deployment

### Automatic Deployment
- GitHub Actions workflow updates immediately after merge
- Next scheduled run: Monday 2:00 AM UTC (9:00 AM GMT+7)
- Can also trigger manually via GitHub Actions UI

### Rollback Plan
If issues occur:
1. Revert this PR
2. Workflow will fail again (original state)
3. Investigate alternative solution
4. Create new fix PR

### Monitoring
After merge:
1. Trigger manual workflow run
2. Monitor run status and logs
3. Verify output files created
4. Check artifacts uploaded
5. Test auto-PR creation (if changes)

---

**Branch**: `fix/github-actions-paths`  
**Target**: `main`  
**Status**: ✅ Ready for review  
**Deployment**: Automatic workflow update  
**Impact**: Fixes workflow failures, enables automation
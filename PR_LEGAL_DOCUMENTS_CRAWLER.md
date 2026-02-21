# PR: Add GitHub Action for automatic Vietnamese legal documents crawling

## 📋 Overview
This PR adds an automated GitHub Actions workflow that crawls Vietnamese legal documents from official government sources on a weekly schedule. The system automatically collects, processes, and stores legal document metadata, creating pull requests when new documents are found.

## 🎯 Problem Statement

### Manual Document Management Challenges
- Legal documents constantly updated across multiple government websites
- Manual collection is time-consuming and error-prone
- No automated way to track new legal documents
- Difficult to maintain up-to-date legal reference library

### Automated Solution Benefits
- Weekly automatic updates from official sources
- Structured storage in multiple formats (JSON, CSV, Markdown)
- Automatic PR creation when new documents detected
- Integration ready for website display

## 🎨 Architecture

### 1. **GitHub Actions Workflow** (`.github/workflows/crawl-legal-documents.yml`)
- **Schedule**: Runs every Monday at 9:00 AM GMT+7 (2:00 AM UTC)
- **Triggers**: 
  - Scheduled (weekly)
  - Manual (`workflow_dispatch`)
  - Push to workflow or script files
- **Auto-PR**: Creates PR automatically when changes detected

### 2. **Python Crawler** (`scripts/crawl-legal-documents.py`)
- **Sources**:
  - `vanban.chinhphu.vn` (Government Documents Portal)
  - `thuvienphapluat.vn` (Legal Library)
  - `moj.gov.vn` (Ministry of Justice - future)
- **Features**:
  - Metadata extraction (title, number, date, URL)
  - Rate limiting (2-second delays between requests)
  - Deduplication (based on URL)
  - Error handling and graceful degradation

### 3. **Output Structure** (`documents/van-ban-phap-luat/crawled/`)
```
crawled/
├── legal_documents.json      # Full metadata (JSON)
├── legal_documents.csv       # Tabular data (CSV)
└── README.md                 # Markdown summary with statistics
```

## ✅ Features

### 1. **Automated Collection**
- Weekly scheduled crawling
- Multiple official sources
- Automatic metadata extraction
- Structured data storage

### 2. **Smart Processing**
- Document number extraction (e.g., "123/2024/NĐ-CP")
- Date parsing and standardization
- URL normalization
- Duplicate detection and removal

### 3. **Integration Ready**
- JSON format for web applications
- CSV format for data analysis
- Markdown for documentation
- Ready for website integration

### 4. **Responsible Crawling**
- Rate limiting (2-second delays)
- Proper User-Agent headers
- Error handling and retries
- Respect for website terms

## 🧪 Technical Implementation

### Python Dependencies
```python
# Core libraries
requests           # HTTP requests
beautifulsoup4     # HTML parsing
lxml               # XML/HTML processing
pandas             # Data manipulation
markdownify        # HTML to Markdown conversion
python-dateutil    # Date parsing
```

### Data Format (JSON Example)
```json
{
  "source": "vanban_chinhphu",
  "title": "Nghị định 123/2024/NĐ-CP về quy định...",
  "url": "https://vanban.chinhphu.vn/?page=detail&document_id=123456",
  "document_number": "123/2024/NĐ-CP",
  "issue_date": "2024-12-31T00:00:00",
  "crawled_at": "2026-02-21T23:48:00"
}
```

### Workflow Steps
1. **Checkout**: Repository checkout with full history
2. **Setup**: Python 3.11 environment setup
3. **Install**: Required Python dependencies
4. **Run**: Execute crawler script
5. **Check**: Detect if any changes were made
6. **Commit**: If changes, commit to branch
7. **PR**: Create pull request automatically
8. **Artifact**: Upload crawled data as workflow artifact

## 🚀 Usage

### Manual Trigger
1. Go to GitHub Actions tab
2. Select "Crawl Vietnamese Legal Documents"
3. Click "Run workflow"
4. Select branch and run

### Local Testing
```bash
# Install dependencies
pip install requests beautifulsoup4 lxml pandas markdownify python-dateutil

# Run crawler
python scripts/crawl-legal-documents.py

# Check output
ls -la documents/van-ban-phap-luat/crawled/
cat documents/van-ban-phap-luat/crawled/legal_documents.json | jq '. | length'
```

### Website Integration (Future)
```html
<!-- Example integration in pages/documents.html -->
<section class="legal-updates">
  <h2>📰 Văn bản Pháp luật Mới nhất</h2>
  <div id="legal-documents-list"></div>
  <script>
    fetch('/documents/van-ban-phap-luat/crawled/legal_documents.json')
      .then(r => r.json())
      .then(docs => {
        // Display latest 5 documents
        const html = docs.slice(0,5).map(doc => `
          <div class="legal-doc">
            <h3>${doc.title}</h3>
            <p>Số: ${doc.document_number} | Ngày: ${doc.issue_date.slice(0,10)}</p>
            <a href="${doc.url}" target="_blank">Xem chi tiết →</a>
          </div>
        `).join('');
        document.getElementById('legal-documents-list').innerHTML = html;
      });
  </script>
</section>
```

## 📊 Expected Output

### Weekly Updates
- **Frequency**: Every Monday
- **Documents**: 10-20 new documents per source
- **Formats**: JSON, CSV, Markdown
- **Storage**: ~100KB per week

### Data Quality
- **Accuracy**: Metadata from official sources
- **Completeness**: Title, number, date, URL
- **Consistency**: Standardized formats
- **Freshness**: Weekly updates

## 🔧 Configuration

### Schedule Adjustment
```yaml
# In .github/workflows/crawl-legal-documents.yml
schedule:
  - cron: '0 2 * * 1'  # Monday 2:00 AM UTC (9:00 AM GMT+7)
  # Alternative: Daily at 3:00 AM UTC
  # - cron: '0 3 * * *'
```

### Source Configuration
```python
# In scripts/crawl-legal-documents.py
self.base_urls = {
    'vanban_chinhphu': 'https://vanban.chinhphu.vn',
    'thuvienphapluat': 'https://thuvienphapluat.vn',
    'moj': 'https://moj.gov.vn'  # Future implementation
}
```

## 🛡️ Security & Ethics

### Responsible Crawling
- **Rate Limiting**: 2-second delays between requests
- **User-Agent**: Identifiable but respectful
- **Public Data**: Only collects publicly available information
- **No Overload**: Limited to 10 documents per source per run

### Data Privacy
- **No Personal Data**: Only collects document metadata
- **No Content Storage**: Stores only titles and metadata, not full document content
- **Transparent**: All collected data visible in repository

## 📈 Future Enhancements

### Planned Features
- [ ] Full document content extraction (with permission)
- [ ] Document categorization (Law, Decree, Circular, etc.)
- [ ] Search functionality across crawled documents
- [ ] Email notifications for important documents
- [ ] Dashboard for document statistics

### Additional Sources
- [ ] Provincial government portals
- [ ] Specialized ministry websites
- [ ] International legal databases
- [ ] Court decisions and rulings

### Performance Improvements
- [ ] Parallel crawling for multiple sources
- [ ] Incremental updates (only new documents)
- [ ] Caching to reduce server load
- [ ] Distributed crawling for large volumes

## 👥 Review Checklist

### Workflow Configuration
- [ ] Schedule appropriate for needs
- [ ] Triggers correctly configured
- [ ] Auto-PR creation works as expected
- [ ] Artifact retention appropriate (7 days)

### Crawler Implementation
- [ ] HTML selectors work with current website structures
- [ ] Rate limiting sufficient and respectful
- [ ] Error handling covers common failure cases
- [ ] Data extraction accurate and complete

### Output Quality
- [ ] JSON format valid and well-structured
- [ ] CSV contains all necessary columns
- [ ] Markdown summary informative and readable
- [ ] No duplicate documents in output

### Integration Readiness
- [ ] Output location appropriate for website integration
- [ ] Data formats compatible with planned uses
- [ ] File permissions and access correct
- [ ] No sensitive information in output

---

**Branch**: `feat/legal-documents-crawler`  
**Target**: `main`  
**Status**: ✅ Ready for review  
**Deployment**: GitHub Actions workflow only (no website changes)  
**Impact**: Adds automated legal document collection system
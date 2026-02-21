#!/usr/bin/env python3
"""
Crawler for Vietnamese Legal Documents
Crawls legal documents from various Vietnamese government sources
"""

import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from markdownify import markdownify
from dateutil import parser
import time
import re

class VietnameseLegalCrawler:
    def __init__(self):
        self.base_urls = {
            'vanban_chinhphu': 'https://vanban.chinhphu.vn',
            'thuvienphapluat': 'https://thuvienphapluat.vn',
            'moj': 'https://moj.gov.vn'
        }
        
        self.output_dir = 'van-ban/crawled'
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
    
    def extract_document_number(self, text):
        """Extract document number from text"""
        patterns = [
            r'So\s+(\d+/\d+/\S+)',  # Vietnamese: Số
            r'So:\s+(\d+/\d+/\S+)',
            r'Number\s+(\d+/\d+/\S+)',
            r'No\.\s+(\d+/\d+/\S+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return None
    
    def parse_vietnamese_date(self, date_str):
        """Parse Vietnamese date string"""
        try:
            # Common Vietnamese date formats
            date_str = date_str.lower()
            date_str = date_str.replace('ngày', '').replace('tháng', '').replace('năm', '').strip()
            
            # Try multiple parsers
            for fmt in ['%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d', '%d/%m/%y']:
                try:
                    from datetime import datetime
                    dt = datetime.strptime(date_str.strip(), fmt)
                    return dt.isoformat()
                except ValueError:
                    continue
            
            # Fallback to dateutil
            return parser.parse(date_str, fuzzy=True).isoformat()
        except Exception:
            return None
    
    def crawl_vanban_chinhphu(self):
        """Crawl from vanban.chinhphu.vn"""
        print("Crawling vanban.chinhphu.vn...")
        documents = []
        
        try:
            # Main page
            response = self.session.get(self.base_urls['vanban_chinhphu'], timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for document links (adjust selectors as needed)
            doc_links = soup.select('a[href*="van-ban"]')
            
            for link in doc_links[:10]:  # Limit to 10
                title = link.get_text(strip=True)
                url = link.get('href')
                
                if url and not url.startswith('http'):
                    url = f"{self.base_urls['vanban_chinhphu']}{url}"
                
                if title and url:
                    doc_number = self.extract_document_number(title)
                    
                    documents.append({
                        'source': 'vanban_chinhphu',
                        'title': title,
                        'url': url,
                        'document_number': doc_number,
                        'issue_date': None,  # Would need deeper crawling
                        'crawled_at': pd.Timestamp.now().isoformat()
                    })
            
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            print(f"Error crawling vanban.chinhphu.vn: {e}")
        
        return documents
    
    def crawl_thuvienphapluat(self):
        """Crawl from thuvienphapluat.vn"""
        print("Crawling thuvienphapluat.vn...")
        documents = []
        
        try:
            search_url = f"{self.base_urls['thuvienphapluat']}/tim-van-ban"
            params = {
                'keyword': '',
                'type': '0',
                'status': '0',
                'sort': '1'  # Sort by latest
            }
            
            response = self.session.get(search_url, params=params, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            documents = []
            
            # Find document items (adjust selector)
            doc_items = soup.select('.document-item, .vb-item')
            
            for item in doc_items[:10]:  # Limit to 10
                title_elem = item.select_one('.title, .vb-title')
                link_elem = item.select_one('a')
                
                if title_elem and link_elem:
                    doc_title = title_elem.get_text(strip=True)
                    doc_url = link_elem.get('href')
                    
                    if doc_url and not doc_url.startswith('http'):
                        doc_url = f"{self.base_urls['thuvienphapluat']}{doc_url}"
                    
                    doc_number = self.extract_document_number(doc_title)
                    
                    documents.append({
                        'source': 'thuvienphapluat',
                        'title': doc_title,
                        'url': doc_url,
                        'document_number': doc_number,
                        'issue_date': None,
                        'crawled_at': pd.Timestamp.now().isoformat()
                    })
            
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            print(f"Error crawling thuvienphapluat.vn: {e}")
        
        return documents
    
    def save_documents(self, documents):
        """Save documents to files"""
        if not documents:
            print("No documents to save")
            return False
        
        # Convert to DataFrame
        df = pd.DataFrame(documents)
        
        # Save as JSON
        json_path = os.path.join(self.output_dir, 'legal_documents.json')
        df.to_json(json_path, orient='records', indent=2, force_ascii=False)
        print(f"Saved {len(documents)} documents to {json_path}")
        
        # Save as CSV
        csv_path = os.path.join(self.output_dir, 'legal_documents.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Saved CSV to {csv_path}")
        
        # Create markdown summary
        self.create_markdown_summary(documents)
        
        return True
    
    def create_markdown_summary(self, documents):
        """Create markdown summary file"""
        from datetime import datetime
        
        md_path = os.path.join(self.output_dir, 'README.md')
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write("# Vietnamese Legal Documents (Automatically Collected)\n\n")
            f.write(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            
            f.write("## Statistics\n")
            f.write(f"- **Total documents**: {len(documents)}\n")
            
            # Group by source
            sources = {}
            for doc in documents:
                source = doc['source']
                sources[source] = sources.get(source, 0) + 1
            
            f.write("- **By source**:\n")
            for source, count in sources.items():
                f.write(f"  - {source}: {count} documents\n")
            
            f.write("\n## Document List\n\n")
            
            # Group documents by source
            grouped = {}
            for doc in documents:
                source = doc['source']
                if source not in grouped:
                    grouped[source] = []
                grouped[source].append(doc)
            
            for source, docs in grouped.items():
                f.write(f"### Source: {source}\n\n")
                
                for doc in docs:
                    f.write(f"#### {doc['title']}\n")
                    f.write(f"- **URL**: {doc['url']}\n")
                    
                    if doc['document_number']:
                        f.write(f"- **Document number**: {doc['document_number']}\n")
                    
                    if doc['issue_date']:
                        f.write(f"- **Issue date**: {doc['issue_date'][:10]}\n")
                    
                    f.write(f"- **Crawled at**: {doc['crawled_at'][:19]}\n\n")
            
            f.write("\n## Configuration\n\n")
            f.write("Documents are automatically collected by GitHub Actions:\n")
            f.write("- **Schedule**: Weekly (Monday, 9:00 AM GMT+7)\n")
            f.write("- **Data sources**:\n")
            f.write("  - vanban.chinhphu.vn (Government Documents)\n")
            f.write("  - thuvienphapluat.vn (Legal Library)\n")
            f.write("  - moj.gov.vn (Ministry of Justice) - planned\n")
            
            f.write("\n## Notes\n\n")
            f.write("1. Data is automatically collected, may not be complete\n")
            f.write("2. Check original link for full content\n")
            f.write("3. Report issues at GitHub repository\n")
        
        print(f"Created markdown summary at {md_path}")
    
    def run(self, test_mode=False):
        """Main crawler execution"""
        print("Starting Vietnamese Legal Documents Crawler")
        
        all_documents = []
        
        # Crawl from sources
        if not test_mode:
            docs1 = self.crawl_vanban_chinhphu()
            all_documents.extend(docs1)
            
            docs2 = self.crawl_thuvienphapluat()
            all_documents.extend(docs2)
        else:
            # Test mode - create sample data
            print("Running in test mode")
            all_documents = [
                {
                    'source': 'test',
                    'title': 'Sample Document 1',
                    'url': 'https://example.com/doc1',
                    'document_number': '123/2024/TT-BTC',
                    'issue_date': '2024-12-31T00:00:00',
                    'crawled_at': pd.Timestamp.now().isoformat()
                },
                {
                    'source': 'test',
                    'title': 'Sample Document 2',
                    'url': 'https://example.com/doc2',
                    'document_number': '456/2024/QD-TTg',
                    'issue_date': '2024-11-30T00:00:00',
                    'crawled_at': pd.Timestamp.now().isoformat()
                }
            ]
        
        # Remove duplicates based on URL
        unique_docs = []
        seen_urls = set()
        
        for doc in all_documents:
            if doc['url'] not in seen_urls:
                seen_urls.add(doc['url'])
                unique_docs.append(doc)
        
        print(f"Found {len(unique_docs)} unique documents")
        
        # Save documents
        if unique_docs:
            saved = self.save_documents(unique_docs)
            return saved
        else:
            print("No documents found")
            return False

def main():
    import sys
    
    test_mode = '--test' in sys.argv
    
    crawler = VietnameseLegalCrawler()
    success = crawler.run(test_mode=test_mode)
    
    if success:
        print("Crawler completed successfully")
        sys.exit(0)
    else:
        print("Crawler completed with no documents or errors")
        sys.exit(1)

if __name__ == "__main__":
    main()
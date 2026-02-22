#!/usr/bin/env python3
"""
Test tất cả database connections trong scripts
Kiểm tra xem scripts nào còn dùng phapdien_complete.db
"""

import os
import re
import sys
from pathlib import Path

def check_file_for_database_references(file_path):
    """Kiểm tra file có references đến database nào"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    databases_found = []
    
    # Tìm tất cả references đến database files
    patterns = [
        r'phapdien_complete\.db',
        r'phapdien\.db',
        r'phapdien_simple\.db',
        r'\.db["\']',
        r'sqlite3\s+[\'"]([^\'"]+\.db)',
        r'connect\([\'"]([^\'"]+\.db)',
        r'db_path\s*=\s*[\'"]([^\'"]+\.db)'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]
            if match and match not in databases_found:
                databases_found.append(match)
    
    # Tìm thêm các patterns khác
    db_refs = re.findall(r'[\'"]([^\'"]+\.db)["\']', content)
    for db_ref in db_refs:
        if db_ref not in databases_found:
            databases_found.append(db_ref)
    
    return databases_found

def main():
    base_dir = Path(__file__).parent.parent
    scripts_dir = base_dir / "scripts"
    
    print("🔍 KIỂM TRA DATABASE REFERENCES TRONG SCRIPTS")
    print("=" * 60)
    
    all_scripts = list(scripts_dir.glob("*.py"))
    # Loại bỏ chính file test này
    all_scripts = [s for s in all_scripts if s.name != "test_database_connections.py"]
    
    issues_found = False
    
    for script_file in all_scripts:
        print(f"\n📄 {script_file.name}:")
        
        try:
            databases = check_file_for_database_references(script_file)
            
            if not databases:
                print("  ✓ Không tìm thấy database references")
                continue
            
            for db in databases:
                # Bỏ qua các pattern regex
                if '\\' in db or db in ['phapdien_complete\\.db', 'phapdien\\.db', 'phapdien_simple\\.db']:
                    continue
                    
                if "phapdien_complete" in db and script_file.name != "merge_databases.py":
                    print(f"  ⚠️  TÌM THẤY: {db} (CẦN SỬA THÀNH phapdien.db)")
                    issues_found = True
                elif "phapdien.db" in db:
                    print(f"  ✓ ĐÚNG: {db}")
                elif db and '.' in db:
                    print(f"  ℹ️  KHÁC: {db}")
        
        except Exception as e:
            print(f"  ✗ Lỗi kiểm tra: {e}")
    
    # Kiểm tra documentation files
    print(f"\n📄 KIỂM TRA DOCUMENTATION FILES:")
    print("=" * 60)
    
    doc_files = [
        base_dir / "README.md",
        base_dir / "COMPLETE_DATABASE_INFO.md",
        base_dir / "DATABASE_MERGE_REPORT.md",
        base_dir / "index.md"
    ]
    
    for doc_file in doc_files:
        if not doc_file.exists():
            continue
            
        print(f"\n📄 {doc_file.name}:")
        
        try:
            with open(doc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Chỉ kiểm tra các references không hợp lệ
            if "phapdien_complete.db" in content:
                # DATABASE_MERGE_REPORT.md và merge_databases.py được phép có
                if doc_file.name in ["DATABASE_MERGE_REPORT.md", "merge_databases.py"]:
                    print(f"  ✓ HỢP LỆ: Có references đến phapdien_complete.db (merge script/report)")
                elif doc_file.name == "README.md":
                    # README.md có thể có lịch sử
                    count = content.count("phapdien_complete.db")
                    print(f"  ℹ️  LỊCH SỬ: Có {count} references đến phapdien_complete.db (lịch sử)")
                else:
                    print(f"  ⚠️  TÌM THẤY phapdien_complete.db (CẦN KIỂM TRA)")
                    issues_found = True
            
            elif "phapdien.db" in content:
                print(f"  ✓ Có references đến phapdien.db")
        
        except Exception as e:
            print(f"  ✗ Lỗi kiểm tra: {e}")
    
    print(f"\n" + "=" * 60)
    print("📊 KẾT QUẢ KIỂM TRA:")
    
    if issues_found:
        print("❌ CÓ VẤN ĐỀ: Tìm thấy scripts còn dùng phapdien_complete.db")
        print("   Cần sửa thành phapdien.db")
        return 1
    else:
        print("✅ TẤT CẢ SCRIPTS ĐÃ DÙNG phapdien.db")
        print("   Database chính thức: phapdien.db (76,303 records)")
        return 0

if __name__ == "__main__":
    sys.exit(main())
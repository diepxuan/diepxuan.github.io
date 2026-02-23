#!/usr/bin/env python3
"""
Clean up UUID files and folders created by old script
Remove all files/folders with UUID pattern in van-ban/
"""

import os
import re
import shutil
from pathlib import Path

# Đường dẫn tuyệt đối tới file hiện tại
SCRIPT_DIR = Path(__file__).resolve().parent

# Thư mục gốc của repo
BASE_DIR = SCRIPT_DIR.parent

VB_PATH = os.path.join(BASE_DIR, "van-ban")

# UUID pattern: 8-4-4-4-12 hex digits
UUID_PATTERN = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

def find_uuid_files():
    """Find all files and folders with UUID in name"""
    uuid_items = []
    
    for root, dirs, files in os.walk(VB_PATH):
        # Check directories
        for dir_name in dirs:
            if re.search(UUID_PATTERN, dir_name):
                full_path = os.path.join(root, dir_name)
                uuid_items.append(('dir', full_path))
        
        # Check files
        for file_name in files:
            if re.search(UUID_PATTERN, file_name):
                full_path = os.path.join(root, file_name)
                uuid_items.append(('file', full_path))
    
    return uuid_items

def delete_uuid_items(uuid_items):
    """Delete UUID files and folders"""
    deleted_count = 0
    error_count = 0
    
    for item_type, item_path in uuid_items:
        try:
            if item_type == 'file':
                os.remove(item_path)
                print(f"🗑️  Deleted file: {item_path}")
                deleted_count += 1
            elif item_type == 'dir':
                shutil.rmtree(item_path)
                print(f"🗑️  Deleted folder: {item_path}")
                deleted_count += 1
        except Exception as e:
            print(f"❌ Error deleting {item_path}: {e}")
            error_count += 1
    
    return deleted_count, error_count

def main():
    print("🔍 Scanning for UUID files and folders...")
    
    uuid_items = find_uuid_files()
    
    if not uuid_items:
        print("✅ No UUID files/folders found!")
        return
    
    print(f"📊 Found {len(uuid_items)} UUID items:")
    
    # Group by type
    files = [p for t, p in uuid_items if t == 'file']
    dirs = [p for t, p in uuid_items if t == 'dir']
    
    print(f"  • Files: {len(files)}")
    print(f"  • Folders: {len(dirs)}")
    
    # Show some examples
    print("\n📋 Examples:")
    for i, (item_type, item_path) in enumerate(uuid_items[:10]):
        rel_path = os.path.relpath(item_path, BASE_DIR)
        print(f"  {i+1}. [{item_type}] {rel_path}")
    
    if len(uuid_items) > 10:
        print(f"  ... and {len(uuid_items) - 10} more")
    
    # Ask for confirmation
    print(f"\n⚠️  WARNING: This will delete {len(uuid_items)} items!")
    confirm = input("Continue? (y/N): ").strip().lower()
    
    if confirm != 'y':
        print("❌ Cancelled")
        return
    
    # Delete items
    deleted_count, error_count = delete_uuid_items(uuid_items)
    
    print(f"\n{'='*60}")
    print(f"📊 CLEANUP COMPLETE")
    print(f"{'='*60}")
    print(f"✅ Deleted: {deleted_count} items")
    if error_count > 0:
        print(f"❌ Errors: {error_count} items")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
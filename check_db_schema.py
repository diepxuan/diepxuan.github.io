#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('van-ban/phap-dien/sqlite/phapdien_complete.db')
cursor = conn.cursor()

print("=== chude table ===")
cursor.execute('PRAGMA table_info(chude)')
for col in cursor.fetchall():
    print(f"  {col[1]} ({col[2]})")

print("\n=== demuc table ===")
cursor.execute('PRAGMA table_info(demuc)')
for col in cursor.fetchall():
    print(f"  {col[1]} ({col[2]})")

print("\n=== dieukhoan table ===")
cursor.execute('PRAGMA table_info(dieukhoan)')
for col in cursor.fetchall():
    print(f"  {col[1]} ({col[2]})")

conn.close()
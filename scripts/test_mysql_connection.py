#!/usr/bin/env python3
"""
Test MySQL connection và queries
"""

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'mysql.diepxuan.corp',
    'port': 3306,
    'database': 'vbpl',
    'user': 'vbpl',
    'password': 'G]9E9S_TahIFVbq-',
    'charset': 'utf8mb4'
}

def test_connection():
    print("Testing MySQL connection...")
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("✓ Connected to database")
        
        # Test query 1
        print("\nTest 1: Get topics")
        cursor.execute("SELECT id, text, stt FROM chu_de ORDER BY CAST(stt AS UNSIGNED)")
        topics = cursor.fetchall()
        print(f"  Found {len(topics)} topics")
        for i, (id_val, text, stt) in enumerate(topics[:3], 1):
            print(f"  {i}. {text} (STT: {stt}, ID: {id_val[:8]}...)")
        
        # Test query 2
        print("\nTest 2: Get subtopics for first topic")
        if topics:
            first_topic_id = topics[0][0]
            cursor.execute("SELECT id, text, stt FROM de_muc WHERE chu_de_id = %s ORDER BY CAST(stt AS UNSIGNED)", (first_topic_id,))
            subtopics = cursor.fetchall()
            print(f"  Found {len(subtopics)} subtopics")
            for i, (id_val, text, stt) in enumerate(subtopics[:3], 1):
                print(f"  {i}. {text} (STT: {stt})")
        
        # Test query 3
        print("\nTest 3: Get provisions for first subtopic")
        if subtopics:
            first_subtopic_id = subtopics[0][0]
            cursor.execute("SELECT id, ten, chi_muc, mapc FROM dieu_khoan WHERE de_muc_id = %s ORDER BY mapc", (first_subtopic_id,))
            provisions = cursor.fetchall()
            print(f"  Found {len(provisions)} provisions")
            for i, (id_val, ten, chi_muc, mapc) in enumerate(provisions[:3], 1):
                print(f"  {i}. {ten[:50]}... (Chi mục: {chi_muc})")
        
        # Test query 4
        print("\nTest 4: Get content for first subtopic")
        cursor.execute("SELECT html_content FROM de_muc_content WHERE de_muc_id = %s LIMIT 1", (first_subtopic_id,))
        content = cursor.fetchone()
        if content:
            print(f"  Found content: {len(content[0]):,} bytes")
        else:
            print("  No content found")
        
        cursor.close()
        conn.close()
        print("\n✓ All tests passed")
        
    except Error as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_connection()
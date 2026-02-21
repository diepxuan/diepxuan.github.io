#!/usr/bin/env python3
"""
Test crawler - minimal version
"""

import requests
from bs4 import BeautifulSoup
import json
import os

def test_vanban_chinhphu():
    """Test crawling from vanban.chinhphu.vn"""
    print("Testing vanban.chinhphu.vn...")
    try:
        url = "https://vanban.chinhphu.vn/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Content length: {len(response.content)}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            print(f"Page title: {title}")
            return True
        else:
            print(f"Failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_thuvienphapluat():
    """Test crawling from thuvienphapluat.vn"""
    print("\nTesting thuvienphapluat.vn...")
    try:
        url = "https://thuvienphapluat.vn/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Content length: {len(response.content)}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            print(f"Page title: {title}")
            return True
        else:
            print(f"Failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("=== Testing Vietnamese Legal Documents Crawler ===")
    
    # Test basic imports
    print("1. Testing imports...")
    try:
        import pandas as pd
        import markdownify
        from dateutil import parser
        print("✓ All imports successful")
    except ImportError as e:
        print(f"✗ Import error: {e}")
    
    # Test website access
    print("\n2. Testing website access...")
    test1 = test_vanban_chinhphu()
    test2 = test_thuvienphapluat()
    
    print("\n=== Test Results ===")
    print(f"vanban.chinhphu.vn: {'✓ PASS' if test1 else '✗ FAIL'}")
    print(f"thuvienphapluat.vn: {'✓ PASS' if test2 else '✗ FAIL'}")
    
    if test1 and test2:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed")
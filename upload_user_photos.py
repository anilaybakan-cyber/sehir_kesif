#!/usr/bin/env python3
"""
Upload User Photos Script
Reads image URLs from 'eksikler.csv' provided by the user,
downloads them, uploads to Firebase, and updates the JSON files.
"""

import csv
import json
import os
import re
import requests
import sys
from pathlib import Path
import firebase_admin
from firebase_admin import credentials, storage

# --- CONFIGURATION ---
CSV_PATH = os.path.expanduser('~/Desktop/remaining_photos.csv')
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("temp_user_photos")

def slugify(text):
    """Convert text to safe filename"""
    if not text:
        return ""
    text = text.lower()
    # Replace Turkish chars
    text = text.replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

def get_city_json_path(city_name):
    """Finds the JSON file for a city name"""
    city_slug = slugify(city_name)
    # Direct match
    path = CITIES_DIR / f"{city_slug}.json"
    if path.exists():
        return path
        
    # Try removing underscores (new_york -> newyork)
    slug_no_underscore = city_slug.replace('_', '')
    path = CITIES_DIR / f"{slug_no_underscore}.json"
    if path.exists():
        return path
    
    # Try fuzzy
    for f in CITIES_DIR.glob("*.json"):
        if city_slug in f.stem or f.stem in city_slug:
            return f
    return None

def download_image(url, filename, city_slug):
    """Downloads image from URL"""
    city_dir = DOWNLOAD_DIR / city_slug
    city_dir.mkdir(parents=True, exist_ok=True)
    filepath = city_dir / filename
    
    try:
        # Handle Google Maps 'lh5.googleusercontent.com' special resizing if needed, 
        # but usually direct link is fine or needs simple fetch.
        # User provided links look like standard URLs.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
        else:
            print(f"❌ Failed to download {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")
        return None

def upload_to_firebase(local_path, city_slug, filename, bucket):
    """Uploads to Firebase Storage"""
    blob_path = f"cities/{city_slug}/{filename}"
    blob = bucket.blob(blob_path)
    
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        # Return the public URL
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"❌ Firebase upload error: {e}")
        return None

def main():
    print(f"Reading {CSV_PATH}...")
    
    # Initialize Firebase
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
            firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
        except Exception as e:
            print(f"FATAL: Could not initialize Firebase: {e}")
            return
            
    bucket = storage.bucket()
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    
    # Track stats
    processed = 0
    success = 0
    failed = 0
    
    # Read CSV
    try:
        with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {CSV_PATH} not found.")
        return

    # Find header row
    start_line = 0
    delimiter = ';' # Default for failed_photos based on cat output
    
    for i, line in enumerate(lines):
        if 'City' in line and 'Place Name' in line and 'Current URL Status' in line:
            start_line = i
            print(f"Found header at line {i}")
            break
            
    # Parse CSV from the found start line
    try:
        reader = csv.reader(lines[start_line:], delimiter=delimiter)
        header = next(reader)
    except StopIteration:
        print("Empty CSV")
        return

    # Find columns
    try:
        header_map = {h.strip(): i for i, h in enumerate(header)}
        
        city_idx = -1
        name_idx = -1
        url_idx = -1
        
        for h, i in header_map.items():
            if 'City' in h:
                city_idx = i
            elif 'Place Name' in h:
                name_idx = i
            elif 'Current URL Status' in h:
                url_idx = i
        
        print(f"Columns: City={city_idx}, Name={name_idx}, URL={url_idx}")
        
    except ValueError as e:
        print(f"Could not find required columns: {e}")
        return

    for row in reader:
        if len(row) <= url_idx:
            continue
            
        city = row[city_idx].strip()
        place_name = row[name_idx].strip()
        image_url = row[url_idx].strip()
        
        if city == 'City': # Skip second header if present
            continue
        
        # Skip if invalid or empty URL or "MISSING" placeholder
        if not image_url or "http" not in image_url:
            continue
            
        print(f"\\nProcessing: {city} - {place_name}")
        processed += 1
        
        # 1. Find City JSON
        json_path = get_city_json_path(city)
        if not json_path:
            print(f"  ❌ City JSON not found for {city}")
            failed += 1
            continue
            
        city_slug = json_path.stem
        
        # 2. Load JSON
        try:
            with open(json_path, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
        except Exception as e:
            print(f"  ❌ Error reading JSON: {e}")
            failed += 1
            continue
            
        # 3. Find Place in JSON
        target_place = None
        for place in data.get('highlights', []):
            # Try exact match first
            if place.get('name') == place_name:
                target_place = place
                break
                
        if not target_place:
            # Try case-insensitive matching if exact failed
            for place in data.get('highlights', []):
                if place.get('name', '').lower() == place_name.lower():
                    target_place = place
                    break
                    
        if not target_place:
            print(f"  ❌ Place '{place_name}' not found in {city_slug}.json")
            failed += 1
            continue
            
        print(f"  ✓ Found place in JSON")
        
        # 4. Download Image
        filename = f"{slugify(place_name)}.jpg"
        local_path = download_image(image_url, filename, city_slug)
        
        if not local_path:
            failed += 1
            continue
            
        print(f"  ✓ Downloaded image")
        
        # 5. Upload to Firebase
        firebase_url = upload_to_firebase(local_path, city_slug, filename, bucket)
        
        if not firebase_url:
            failed += 1
            continue
            
        print(f"  ✓ Uploaded to Firebase: {firebase_url}")
        
        # 6. Update JSON
        target_place['imageUrl'] = firebase_url
        target_place['source'] = 'firebase'
        
        with open(json_path, 'w', encoding='utf-8') as jf:
            json.dump(data, jf, ensure_ascii=False, indent=2)
            
        print(f"  ✓ Updated JSON file")
        success += 1

    print("\\n" + "="*30)
    print(f"Summary:")
    print(f"Processed: {processed}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print("="*30)

if __name__ == "__main__":
    main()

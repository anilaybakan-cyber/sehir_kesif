#!/usr/bin/env python3
"""
Places API Fotoğraflarını İndir ve Firebase'e Yükle
Bu script JSON'lardaki Places API URL'lerini:
1. İndirir
2. Firebase Storage'a yükler
3. JSON'u yeni URL ile günceller
"""

import json
import re
import os
import hashlib
import requests
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, storage

# Configuration
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("migrated_city_photos")

# Places API pattern
PLACES_API_PATTERN = re.compile(
    r'https://maps\.googleapis\.com/maps/api/place/photo\?[^"]*photo_?reference=([^&"]+)[^"]*key=([^&"]+)'
)

def slugify(text):
    """Convert text to safe filename"""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

def download_photo(photo_ref, api_key, filename, city_id):
    """Download photo from Places API"""
    city_dir = DOWNLOAD_DIR / city_id
    city_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = city_dir / filename
    if filepath.exists() and filepath.stat().st_size > 1000:
        return filepath
    
    url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_?reference={photo_ref}&key={api_key}"
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
        else:
            print(f"    ❌ Download failed: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"    ❌ Download error: {e}")
        return None

def upload_to_firebase(local_path, city_id, filename, bucket):
    """Upload photo to Firebase Storage"""
    blob_path = f"cities/{city_id}/{filename}"
    blob = bucket.blob(blob_path)
    
    if blob.exists():
        return f"{STORAGE_BASE_URL}/{blob_path}"
    
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"    ❌ Upload error: {e}")
        return None

def process_city(city_id, bucket, dry_run=True):
    """Process all Places API URLs in a city"""
    json_path = CITIES_DIR / f"{city_id}.json"
    if not json_path.exists():
        return None
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    downloaded = 0
    uploaded = 0
    updated = 0
    failed = 0
    
    # Process highlights
    for place in data.get('highlights', []):
        image_url = place.get('imageUrl', '')
        if 'maps.googleapis.com' not in image_url:
            continue
        
        # Extract photo reference and API key
        match = PLACES_API_PATTERN.search(image_url)
        if not match:
            failed += 1
            continue
        
        photo_ref = match.group(1)
        api_key = match.group(2)
        
        # Generate filename from place ID or name
        place_id = place.get('id', '')
        place_name = place.get('name', '')
        filename = f"{place_id.replace('-', '_') or slugify(place_name)}.jpg"
        
        if dry_run:
            print(f"    Would process: {filename}")
            downloaded += 1
            continue
        
        # Download
        local_path = download_photo(photo_ref, api_key, filename, city_id)
        if local_path:
            downloaded += 1
            
            # Upload
            firebase_url = upload_to_firebase(local_path, city_id, filename, bucket)
            if firebase_url:
                uploaded += 1
                place['imageUrl'] = firebase_url
                updated += 1
            else:
                failed += 1
        else:
            failed += 1
    
    # Process heroImage
    hero_url = data.get('heroImage', '')
    if 'maps.googleapis.com' in hero_url:
        match = PLACES_API_PATTERN.search(hero_url)
        if match and not dry_run:
            photo_ref = match.group(1)
            api_key = match.group(2)
            filename = "hero.jpg"
            
            local_path = download_photo(photo_ref, api_key, filename, city_id)
            if local_path:
                firebase_url = upload_to_firebase(local_path, city_id, filename, bucket)
                if firebase_url:
                    data['heroImage'] = firebase_url
                    updated += 1
    
    # Save updated JSON
    if not dry_run and updated > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return {
        'city': city_id,
        'downloaded': downloaded,
        'uploaded': uploaded,
        'updated': updated,
        'failed': failed
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true', help='Actually download and upload')
    parser.add_argument('--city', type=str, help='Process specific city')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of cities to process')
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("=" * 60)
    print("PLACES API PHOTO MIGRATION")
    print("Mode:", "DRY RUN" if dry_run else "EXECUTE (downloading and uploading)")
    print("=" * 60)
    
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    
    # Create download directory
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    
    # Find cities with Places API URLs
    problem_cities = []
    for json_file in CITIES_DIR.glob("*.json"):
        with open(json_file, 'r') as f:
            content = f.read()
        if 'maps.googleapis.com' in content:
            # Count occurrences
            count = content.count('maps.googleapis.com')
            problem_cities.append((json_file.stem, count))
    
    # Sort by count descending
    problem_cities.sort(key=lambda x: x[1], reverse=True)
    
    if args.city:
        problem_cities = [(c, n) for c, n in problem_cities if c == args.city]
    
    if args.limit > 0:
        problem_cities = problem_cities[:args.limit]
    
    print(f"\nCities to process: {len(problem_cities)}")
    print("-" * 60)
    
    total_downloaded = 0
    total_uploaded = 0
    total_updated = 0
    total_failed = 0
    
    for city_id, count in problem_cities:
        print(f"\n📷 Processing {city_id} ({count} Places API URLs)...")
        result = process_city(city_id, bucket, dry_run=dry_run)
        if result:
            total_downloaded += result['downloaded']
            total_uploaded += result['uploaded']
            total_updated += result['updated']
            total_failed += result['failed']
            
            if not dry_run:
                print(f"   ✓ Downloaded: {result['downloaded']}, Uploaded: {result['uploaded']}, Failed: {result['failed']}")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Downloaded:  {total_downloaded}")
    print(f"  Uploaded:    {total_uploaded}")
    print(f"  Updated:     {total_updated}")
    print(f"  Failed:      {total_failed}")
    
    if dry_run:
        print("\n💡 Run with --execute to actually download and upload")
        print("   You can also use --limit N to process only N cities")
        print("   Example: python3 upload_missing_photos.py --execute --limit 5")

if __name__ == "__main__":
    main()

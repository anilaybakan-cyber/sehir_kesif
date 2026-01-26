#!/usr/bin/env python3
"""
Gerçek Fotoğraf İndirme Script'i
Koordinat ve isim kullanarak Places API'den taze photo_reference alır,
fotoğrafları indirir ve Firebase'e yükler.
"""

import json
import re
import os
import time
import requests
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, storage

# Configuration
API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_DIR = Path("fresh_photos")

def slugify(text):
    """Convert text to safe filename"""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

def find_place_and_get_photo(name, lat, lng):
    """Find place using Nearby Search and get photo reference"""
    # Use Nearby Search with keyword
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": 100,  # 100 meters
        "keyword": name,
        "key": API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        
        if data.get("status") == "OK" and data.get("results"):
            result = data["results"][0]
            photos = result.get("photos", [])
            if photos:
                return photos[0].get("photo_reference")
    except Exception as e:
        print(f"    API Error: {e}")
    
    return None

def download_photo(photo_ref, filename, city_id):
    """Download photo from Places Photo API"""
    city_dir = DOWNLOAD_DIR / city_id
    city_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = city_dir / filename
    if filepath.exists() and filepath.stat().st_size > 5000:
        return filepath
    
    url = f"https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "maxwidth": 1200,
        "photo_reference": photo_ref,
        "key": API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        if response.status_code == 200 and len(response.content) > 5000:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
    except Exception as e:
        print(f"    Download Error: {e}")
    
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
        print(f"    Upload Error: {e}")
        return None

def process_city(city_id, bucket, limit=0):
    """Process all Places API URLs in a city"""
    json_path = CITIES_DIR / f"{city_id}.json"
    if not json_path.exists():
        return None
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed = 0
    success = 0
    failed = 0
    
    highlights = data.get('highlights', [])
    
    for place in highlights:
        image_url = place.get('imageUrl', '')
        if 'maps.googleapis.com' not in image_url:
            continue
        
        if limit > 0 and processed >= limit:
            break
        
        processed += 1
        
        name = place.get('name', '')
        lat = place.get('lat')
        lng = place.get('lng')
        place_id = place.get('id', '')
        
        if not (lat and lng):
            print(f"    ⚠️ No coordinates for: {name}")
            failed += 1
            continue
        
        # Get fresh photo reference
        print(f"    🔍 Finding: {name[:30]}...")
        photo_ref = find_place_and_get_photo(name, lat, lng)
        
        if not photo_ref:
            print(f"    ❌ No photo found for: {name[:30]}")
            failed += 1
            time.sleep(0.1)
            continue
        
        # Download photo
        filename = f"{place_id.replace('-', '_') or slugify(name)}.jpg"
        local_path = download_photo(photo_ref, filename, city_id)
        
        if not local_path:
            print(f"    ❌ Download failed for: {name[:30]}")
            failed += 1
            continue
        
        # Upload to Firebase
        firebase_url = upload_to_firebase(local_path, city_id, filename, bucket)
        
        if firebase_url:
            place['imageUrl'] = firebase_url
            success += 1
            print(f"    ✅ {name[:30]}")
        else:
            failed += 1
        
        # Rate limiting
        time.sleep(0.2)
    
    # Save updated JSON
    if success > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return {
        'city': city_id,
        'processed': processed,
        'success': success,
        'failed': failed
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, help='Process specific city')
    parser.add_argument('--limit', type=int, default=0, help='Limit photos per city (0=all)')
    parser.add_argument('--all', action='store_true', help='Process all cities with Places API URLs')
    args = parser.parse_args()
    
    print("=" * 60)
    print("FRESH PHOTO DOWNLOAD")
    print("=" * 60)
    
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    
    # Find cities with Places API URLs
    if args.city:
        cities_to_process = [(args.city, 0)]
    elif args.all:
        cities_to_process = []
        for json_file in CITIES_DIR.glob("*.json"):
            with open(json_file, 'r') as f:
                content = f.read()
            count = content.count('maps.googleapis.com')
            if count > 0:
                cities_to_process.append((json_file.stem, count))
        cities_to_process.sort(key=lambda x: x[1], reverse=True)
    else:
        print("Please specify --city CITY_NAME or --all")
        return
    
    print(f"\nCities to process: {len(cities_to_process)}")
    print("-" * 60)
    
    total_success = 0
    total_failed = 0
    
    for city_id, count in cities_to_process:
        print(f"\n📷 {city_id.upper()} ({count} Places API URLs)")
        result = process_city(city_id, bucket, limit=args.limit)
        if result:
            total_success += result['success']
            total_failed += result['failed']
            print(f"   Summary: ✅ {result['success']} | ❌ {result['failed']}")
    
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"  Total Success: {total_success}")
    print(f"  Total Failed:  {total_failed}")

if __name__ == "__main__":
    main()

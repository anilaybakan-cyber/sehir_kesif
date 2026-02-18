#!/usr/bin/env python3
"""
Unsplash to Google Places Photo Migrator (v2)
Finds all landmarks and hero images with Unsplash URLs, 
fetches real photos using Text Search and Nearby Search,
uploads them to Firebase Storage, and updates the JSON files.
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

def find_place_and_get_photo(name, lat, lng, is_hero=False):
    """Find place using Text Search or Nearby Search and get photo reference"""
    
    # Text Search is best for general names or specific landmarks
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_query = name
    if is_hero:
        search_query = f"{name} skyline" # Better chances for hero
        
    params = {
        "query": search_query,
        "key": API_KEY
    }
    
    # Add location bias if available
    if lat and lng:
        params["location"] = f"{lat},{lng}"
        params["radius"] = 2000 # Larger radius for Text Search bias
    
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        
        if data.get("status") == "OK" and data.get("results"):
            for result in data["results"]:
                photos = result.get("photos", [])
                if photos:
                    return photos[0].get("photo_reference")
                    
        # Fallback to Nearby Search if Text Search failed for landmarks
        if not is_hero and lat and lng:
            url_ns = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
            params_ns = {
                "location": f"{lat},{lng}",
                "radius": 1000,
                "keyword": name,
                "key": API_KEY
            }
            response = requests.get(url_ns, params=params_ns, timeout=15)
            data = response.json()
            if data.get("status") == "OK" and data.get("results"):
                for result in data["results"]:
                    photos = result.get("photos", [])
                    if photos:
                        return photos[0].get("photo_reference")
                        
    except Exception as e:
        print(f"    API Error seeking {name}: {e}")
    
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
        "maxwidth": 1600, # Higher quality
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
        print(f"    Download Error for {filename}: {e}")
    
    return None

def upload_to_firebase(local_path, city_id, filename, bucket):
    """Upload photo to Firebase Storage"""
    blob_path = f"cities/{city_id}/{filename}"
    blob = bucket.blob(blob_path)
    
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"    Upload Error for {filename}: {e}")
        return None

def process_city(city_id, bucket):
    """Process all Unsplash URLs in a city"""
    json_path = CITIES_DIR / f"{city_id}.json"
    if not json_path.exists():
        return None
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    success = 0
    failed = 0
    total_found = 0
    
    # Process heroImage if it's Unsplash
    hero_image = data.get('heroImage', '')
    if 'unsplash.com' in str(hero_image):
        total_found += 1
        name = data.get('cityName', city_id.capitalize())
        lat = data.get('centerLat')
        lng = data.get('centerLng')
        print(f"    🌟 Processing Hero Image: {name}")
        
        photo_ref = find_place_and_get_photo(name, lat, lng, is_hero=True)
        if photo_ref:
            filename = f"hero_{city_id}.jpg"
            local_path = download_photo(photo_ref, filename, city_id)
            if local_path:
                firebase_url = upload_to_firebase(local_path, city_id, filename, bucket)
                if firebase_url:
                    data['heroImage'] = firebase_url
                    success += 1
                    print("       ✅ Hero updated")
                else: failed += 1
            else: failed += 1
        else: failed += 1

    # Process highlights
    highlights = data.get('highlights', [])
    for place in highlights:
        image_url = place.get('imageUrl', '')
        if 'unsplash.com' not in str(image_url):
            continue
        
        total_found += 1
        name = place.get('name', '')
        lat = place.get('lat')
        lng = place.get('lng')
        place_id = place.get('id', '')
        
        print(f"    📸 Processing: {name}")
        
        photo_ref = find_place_and_get_photo(name, lat, lng, is_hero=False)
        if not photo_ref:
            print(f"       ❌ Google couldn't find photo reference")
            failed += 1
            continue
            
        filename = f"{place_id.replace('-', '_') or slugify(name)}.jpg"
        local_path = download_photo(photo_ref, filename, city_id)
        
        if local_path:
            firebase_url = upload_to_firebase(local_path, city_id, filename, bucket)
            if firebase_url:
                place['imageUrl'] = firebase_url
                success += 1
                print(f"       ✅ Successfully updated")
            else: failed += 1
        else: failed += 1
        
        time.sleep(0.5) # Protect API
    
    if success > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    return {
        'found': total_found,
        'success': success,
        'failed': failed
    }

def main():
    print("🚀 Starting Unsplash -> Google Photo Migration (Improved v2)")
    
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    
    cities_with_unsplash = []
    for json_file in sorted(CITIES_DIR.glob("*.json")):
        with open(json_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'unsplash.com' in content:
            cities_with_unsplash.append(json_file.stem)
            
    print(f"🌍 Found {len(cities_with_unsplash)} cities with Unsplash images")
    
    total_success = 0
    total_failed = 0
    
    for city_id in cities_with_unsplash:
        print(f"\n🏙️ {city_id.upper()}")
        result = process_city(city_id, bucket)
        if result:
            total_success += result['success']
            total_failed += result['failed']
            print(f"   Summary: Found {result['found']} | ✅ {result['success']} | ❌ {result['failed']}")
            
    print("\n" + "=" * 60)
    print("MIGRATION COMPLETE")
    print(f"Total Success (this run): {total_success}")
    print(f"Total Failed (this run):  {total_failed}")
    print("=" * 60)

if __name__ == "__main__":
    main()

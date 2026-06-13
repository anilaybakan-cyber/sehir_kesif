#!/usr/bin/env python3
"""
Midilli Photos Migration Script (Concurrent, Fast & Unsplash Fallbacks):
1. Loads assets/cities/midilli.json and ota_data_pack/cities/midilli.json.
2. For each highlight with a maps.googleapis.com URL, tries to download the image concurrently.
3. Uploads successful downloads to Firebase Storage under BUCKET/cities/midilli/{place_id}.jpg.
4. For expired/failed downloads, falls back to high-quality category-based Unsplash images.
5. Rewrites JSON files with new URLs.
"""

import json
import re
import os
import time
import urllib.parse
import requests
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, storage

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
JSON_PATHS = [
    Path("assets/cities/midilli.json"),
    Path("ota_data_pack/cities/midilli.json")
]
TEMP_DOWNLOAD_DIR = Path("temp_midilli_photos")

# Regular expression to extract photo reference and api key
PLACES_API_PATTERN = re.compile(
    r'https://maps\.googleapis\.com/maps/api/place/photo\?[^"]*photo_?reference=([^&"]+)[^"]*key=([^&"]+)',
    re.IGNORECASE
)

# Curated high-quality Unsplash fallbacks for Greek island (Midilli/Lesvos) categories
UNSPLASH_FALLBACKS = {
    "tarihi": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=800&q=80",  # Greek ruins/historic
    "manzara": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80", # Scenic sea/coast
    "plaj": "https://images.unsplash.com/photo-1506929562872-bb421503ef21?auto=format&fit=crop&w=800&q=80",    # Beach
    "yemek": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80",   # Taverna/Mediterranean food
    "müze": "https://images.unsplash.com/photo-1566121318599-52e9cd1a409f?auto=format&fit=crop&w=800&q=80",    # Museum/art
    "doğa": "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?auto=format&fit=crop&w=800&q=80",    # Nature/forest
    "default": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80"  # General travel
}

def get_unsplash_fallback(category):
    if not category:
        return UNSPLASH_FALLBACKS["default"]
    cat = category.lower().strip()
    return UNSPLASH_FALLBACKS.get(cat, UNSPLASH_FALLBACKS["default"])

def download_photo(url, filepath):
    """Download photo from URL and save locally"""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False
    except Exception as e:
        return False

def upload_to_firebase(local_path, filename, bucket):
    """Upload photo to Firebase Storage and make it public"""
    blob_path = f"cities/midilli/{filename}"
    blob = bucket.blob(blob_path)
    
    # Check if already exists in storage
    if blob.exists():
        return f"{STORAGE_BASE_URL}/{blob_path}"
    
    try:
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"    ❌ Firebase upload error: {e}")
        return None

def slugify(text):
    """Convert text to safe filename"""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')[:50]

print_lock = threading.Lock()

def migrate_place(place, bucket, dry_run):
    place_name = place.get("name")
    place_id = place.get("id", slugify(place_name))
    image_url = place.get("imageUrl", "")
    category = place.get("category", "default")
    
    if 'maps.googleapis.com' not in image_url:
        return False
        
    filename = f"{place_id.replace('-', '_')}.jpg"
    local_path = TEMP_DOWNLOAD_DIR / filename
    
    if dry_run:
        with print_lock:
            print(f"  [DRY RUN] Would migrate place: {place_name} ({place_id})")
        return True
        
    with print_lock:
        print(f"  📷 Migrating place: {place_name}...")
        
    # 1. Parse Google photo reference and key
    match = PLACES_API_PATTERN.search(image_url)
    success = False
    
    if match:
        photo_ref = match.group(1)
        working_key = "AIzaSyBSZJmb9IIINxWbxXgCLTPiWC9SLcaDrMk"
        google_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={working_key}"
        success = download_photo(google_url, local_path)
            
    # 2. Upload to Firebase Storage
    if success and local_path.exists():
        firebase_url = upload_to_firebase(local_path, filename, bucket)
        if firebase_url:
            with print_lock:
                print(f"    ✅ Uploaded: {firebase_url}")
            place["imageUrl"] = firebase_url
            try:
                local_path.unlink()
            except:
                pass
            return True

    # 3. Fallback to Unsplash on failure / expiration
    fallback_url = get_unsplash_fallback(category)
    with print_lock:
        print(f"    ⚠️ Download failed (expired reference). Falling back to Unsplash category: {category} -> {fallback_url}")
    place["imageUrl"] = fallback_url
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true', help='Actually execute migration')
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("=" * 60)
    print("MIDILLI CITY PHOTOS TO FIREBASE STORAGE MIGRATION (FAST & FALLBACKS)")
    print("Mode:", "DRY RUN" if dry_run else "EXECUTE")
    print("=" * 60)
    
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    bucket = storage.bucket()
    
    TEMP_DOWNLOAD_DIR.mkdir(exist_ok=True)
    
    for json_path in JSON_PATHS:
        if not json_path.exists():
            print(f"⚠️ Warning: {json_path} not found. Skipping.")
            continue
            
        print(f"\n📂 Processing {json_path}...")
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        highlights = data.get("highlights", [])
        updated = False
        
        # Concurrently migrate highlights
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {
                executor.submit(migrate_place, place, bucket, dry_run): place
                for place in highlights
            }
            
            for future in as_completed(futures):
                try:
                    success = future.result()
                    if success:
                        updated = True
                except Exception as e:
                    print(f"Error migrating place: {e}")
                    
        # Write updated JSON
        if updated and not dry_run:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"💾 Updated {json_path} with new URLs.")
            
    print("\n✅ Migration completed.")

if __name__ == "__main__":
    main()

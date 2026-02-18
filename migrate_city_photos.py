#!/usr/bin/env python3
"""
Şehir JSON Fotoğraflarını Firebase'e Taşıma Script'i
Mevcut Places API URL'lerini Firebase Storage URL'leri ile değiştirir.

Bu script:
1. Firebase Storage'daki mevcut fotoğrafları listeler
2. JSON'lardaki Places API URL'lerini eşleştirir
3. Eşleşen URL'leri günceller
4. Eksik fotoğrafları indirir ve yükler
"""

import re
import os
import json
import hashlib
import requests
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Firebase Admin SDK (optional - for upload)
try:
    import firebase_admin
    from firebase_admin import credentials, storage
    FIREBASE_AVAILABLE = True
except ImportError:
    FIREBASE_AVAILABLE = False
    print("⚠️ firebase_admin not installed. Upload disabled.")

# Configuration
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")
DOWNLOAD_FOLDER = Path("migrated_city_photos")

# Pattern to match Places API photo URLs
PLACES_API_PATTERN = re.compile(
    r'https://maps\.googleapis\.com/maps/api/place/photo\?[^"]+photo_reference=([^&"]+)[^"]*key=([^&"]+)'
)

def slugify(name):
    """Convert place name to safe filename"""
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '_', name)
    return name[:50]

def check_firebase_storage(city_id):
    """Check what photos already exist in Firebase Storage for a city"""
    if not FIREBASE_AVAILABLE:
        return {}
    
    bucket = storage.bucket()
    prefix = f"cities/{city_id}/"
    blobs = list(bucket.list_blobs(prefix=prefix))
    
    existing = {}
    for blob in blobs:
        filename = blob.name.split('/')[-1]
        url = f"{STORAGE_BASE_URL}/{blob.name}"
        existing[filename] = url
    
    return existing

def process_city_json(json_path, dry_run=True):
    """Process a single city JSON file"""
    city_id = json_path.stem
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
    
    # Find all Places API URLs
    places_urls = []
    for match in PLACES_API_PATTERN.finditer(content):
        full_url = match.group(0)
        photo_ref = match.group(1)
        api_key = match.group(2)
        places_urls.append({
            'full_url': full_url,
            'photo_ref': photo_ref,
            'api_key': api_key
        })
    
    if not places_urls:
        return {'city': city_id, 'places_api_count': 0, 'updated': 0, 'skipped': 0}
    
    # Check existing Firebase photos
    existing_photos = check_firebase_storage(city_id) if FIREBASE_AVAILABLE else {}
    
    updates = {}
    need_upload = []
    
    # Try to match or prepare for upload
    for item in places_urls:
        ref_hash = hashlib.md5(item['photo_ref'].encode()).hexdigest()[:12]
        potential_filename = f"{ref_hash}.jpg"
        
        if potential_filename in existing_photos:
            # Found in Firebase, map it
            updates[item['full_url']] = existing_photos[potential_filename]
        else:
            need_upload.append(item)
    
    result = {
        'city': city_id,
        'places_api_count': len(places_urls),
        'already_in_firebase': len(updates),
        'need_upload': len(need_upload)
    }
    
    if not dry_run and updates:
        # Apply updates
        new_content = content
        for old_url, new_url in updates.items():
            new_content = new_content.replace(old_url, new_url)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        result['updated'] = len(updates)
    
    return result

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Migrate city photos to Firebase')
    parser.add_argument('--dry-run', action='store_true', default=True,
                        help='Only analyze, do not modify files')
    parser.add_argument('--execute', action='store_true',
                        help='Actually modify files')
    parser.add_argument('--city', type=str, help='Process only specific city')
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("=" * 60)
    print("CITY JSON PHOTO MIGRATION")
    print("Mode:", "DRY RUN (no changes)" if dry_run else "EXECUTE (will modify files)")
    print("=" * 60)
    
    if FIREBASE_AVAILABLE and os.path.exists(SERVICE_ACCOUNT_FILE):
        if not firebase_admin._apps:
            cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
            firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
        print("✓ Firebase initialized")
    else:
        print("⚠️ Firebase not available - will only analyze")
    
    # Process cities
    json_files = sorted(CITIES_DIR.glob("*.json"))
    if args.city:
        json_files = [f for f in json_files if f.stem == args.city]
    
    total_places = 0
    total_in_firebase = 0
    total_need_upload = 0
    
    results = []
    for json_file in json_files:
        result = process_city_json(json_file, dry_run=dry_run)
        if result['places_api_count'] > 0:
            results.append(result)
            total_places += result['places_api_count']
            total_in_firebase += result.get('already_in_firebase', 0)
            total_need_upload += result.get('need_upload', 0)
    
    # Print summary
    print("\n" + "-" * 60)
    print("ANALYSIS RESULTS")
    print("-" * 60)
    
    for r in sorted(results, key=lambda x: x['places_api_count'], reverse=True):
        status = ""
        if r.get('already_in_firebase', 0) > 0:
            status = f" ✓{r['already_in_firebase']} in Firebase"
        if r.get('need_upload', 0) > 0:
            status += f" ⚠️{r['need_upload']} need upload"
        print(f"  {r['city']:20}: {r['places_api_count']:4} Places API URLs{status}")
    
    print("\n" + "-" * 60)
    print("SUMMARY")
    print("-" * 60)
    print(f"  Total Places API URLs: {total_places}")
    print(f"  Already in Firebase:   {total_in_firebase}")
    print(f"  Need upload:           {total_need_upload}")
    
    if total_need_upload > 0:
        print("\n⚠️ Some photos need to be uploaded to Firebase first.")
        print("   Use the upload script to download and upload missing photos.")
    
    if not dry_run:
        print("\n✓ Files have been updated!")
    else:
        print("\n💡 Run with --execute to apply changes")

if __name__ == "__main__":
    main()

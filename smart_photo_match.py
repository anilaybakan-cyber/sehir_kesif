#!/usr/bin/env python3
"""
Akıllı Fotoğraf Eşleştirme Script'i
JSON'daki place ID'leri Firebase'deki dosya isimleriyle eşleştirir.
"""

import json
import re
import os
from pathlib import Path
from unicodedata import normalize

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, storage

# Configuration
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")

def slugify(text):
    """Convert text to slug format matching Firebase filenames"""
    if not text:
        return ""
    text = normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '_', text)
    return text.strip('_')

def get_firebase_photos(city_id):
    """Get all photos from Firebase for a city"""
    bucket = storage.bucket()
    prefix = f"cities/{city_id}/"
    blobs = list(bucket.list_blobs(prefix=prefix))
    
    photos = {}
    for blob in blobs:
        filename = blob.name.split('/')[-1]
        name_without_ext = os.path.splitext(filename)[0]
        url = f"{STORAGE_BASE_URL}/{blob.name}"
        # Store with both underscore and hyphen versions
        photos[name_without_ext] = url
        photos[name_without_ext.replace('_', '-')] = url
        photos[name_without_ext.replace('-', '_')] = url
    
    return photos

def process_city(city_id, dry_run=True):
    """Process a city and match photos"""
    json_path = CITIES_DIR / f"{city_id}.json"
    if not json_path.exists():
        return None
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get Firebase photos
    firebase_photos = get_firebase_photos(city_id)
    if not firebase_photos:
        print(f"  ⚠️ No photos in Firebase for {city_id}")
        return {'city': city_id, 'matched': 0, 'unmatched': 0, 'firebase_photos': 0}
    
    matched = 0
    unmatched = 0
    unmatched_list = []
    
    # Process places
    for place in data.get('highlights', []):
        image_url = place.get('imageUrl', '')
        if 'maps.googleapis.com' not in image_url:
            continue  # Already migrated
        
        # Use place ID (preferred) or fallback to slugified name
        place_id = place.get('id', '')
        place_name = place.get('name', '')
        
        # Try to find matching photo
        firebase_url = None
        
        # Try direct ID match (Firebase might use underscore or hyphen)
        if place_id in firebase_photos:
            firebase_url = firebase_photos[place_id]
        
        # Try with underscore conversion
        if not firebase_url:
            slug = place_id.replace('-', '_')
            if slug in firebase_photos:
                firebase_url = firebase_photos[slug]
        
        # Try name-based match
        if not firebase_url:
            name_slug = slugify(place_name)
            if name_slug in firebase_photos:
                firebase_url = firebase_photos[name_slug]
        
        if firebase_url:
            place['imageUrl'] = firebase_url
            matched += 1
        else:
            unmatched += 1
            unmatched_list.append(place_id or place_name)
    
    # Process heroImage if needed
    hero = data.get('heroImage', '')
    if 'maps.googleapis.com' in hero:
        if 'hero' in firebase_photos:
            data['heroImage'] = firebase_photos['hero']
            matched += 1
        elif 'cover' in firebase_photos:
            data['heroImage'] = firebase_photos['cover']
            matched += 1
        else:
            unmatched += 1
    
    if not dry_run and matched > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    if unmatched > 0 and unmatched <= 5:
        print(f"    Unmatched: {unmatched_list}")
    
    return {
        'city': city_id,
        'matched': matched,
        'unmatched': unmatched,
        'firebase_photos': len(firebase_photos) // 3  # Divided by 3 because we store 3 variants
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true', help='Apply changes')
    parser.add_argument('--city', type=str, help='Process specific city')
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("=" * 60)
    print("SMART PHOTO MATCHING (ID-Based)")
    print("Mode:", "DRY RUN" if dry_run else "EXECUTE")
    print("=" * 60)
    
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    
    # Get problem cities (with Places API URLs)
    problem_cities = []
    for json_file in CITIES_DIR.glob("*.json"):
        with open(json_file, 'r') as f:
            content = f.read()
        if 'maps.googleapis.com' in content:
            problem_cities.append(json_file.stem)
    
    if args.city:
        problem_cities = [args.city] if args.city in problem_cities else []
    
    print(f"\nCities with Places API URLs: {len(problem_cities)}")
    print("-" * 60)
    
    total_matched = 0
    total_unmatched = 0
    
    for city_id in sorted(problem_cities):
        print(f"\nProcessing {city_id}...")
        result = process_city(city_id, dry_run=dry_run)
        if result:
            total_matched += result['matched']
            total_unmatched += result['unmatched']
            status = "✓" if result['unmatched'] == 0 else "⚠️"
            print(f"  {status} Matched: {result['matched']}, Unmatched: {result['unmatched']} (Firebase: {result['firebase_photos']} photos)")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Total matched:   {total_matched}")
    print(f"  Total unmatched: {total_unmatched}")
    
    if not dry_run and total_matched > 0:
        print("\n✓ Changes applied!")
    else:
        print("\n💡 Run with --execute to apply changes")

if __name__ == "__main__":
    main()

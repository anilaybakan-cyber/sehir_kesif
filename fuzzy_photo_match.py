#!/usr/bin/env python3
"""
Gelişmiş Fotoğraf Eşleştirme Script'i
Firebase'deki fotoğrafları JSON'lardaki yerlerle fuzzy matching ile eşleştirir.
"""

import json
import re
import os
from pathlib import Path
from unicodedata import normalize
from difflib import SequenceMatcher

import firebase_admin
from firebase_admin import credentials, storage

# Configuration
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
CITIES_DIR = Path("assets/cities")

def normalize_name(text):
    """Normalize text for comparison"""
    if not text:
        return ""
    # Normalize unicode
    text = normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    # Remove special chars
    text = re.sub(r'[^\w\s]', '', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def similarity(a, b):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, normalize_name(a), normalize_name(b)).ratio()

def get_firebase_photos(city_id):
    """Get all photos from Firebase for a city"""
    bucket = storage.bucket()
    prefix = f"cities/{city_id}/"
    blobs = list(bucket.list_blobs(prefix=prefix))
    
    photos = []
    for blob in blobs:
        filename = blob.name.split('/')[-1]
        name_without_ext = os.path.splitext(filename)[0]
        url = f"{STORAGE_BASE_URL}/{blob.name}"
        photos.append({
            'filename': name_without_ext,
            'url': url,
            'normalized': normalize_name(name_without_ext.replace('_', ' '))
        })
    
    return photos

def find_best_match(place_name, place_id, firebase_photos, threshold=0.6):
    """Find best matching Firebase photo for a place"""
    if not firebase_photos:
        return None
    
    # Try direct ID match first
    id_normalized = normalize_name(place_id.replace('-', ' ') if place_id else '')
    for photo in firebase_photos:
        if photo['normalized'] == id_normalized:
            return photo['url']
    
    # Try name match
    name_normalized = normalize_name(place_name)
    best_match = None
    best_score = threshold
    
    for photo in firebase_photos:
        # Calculate similarity
        score = similarity(name_normalized, photo['normalized'])
        
        # Also try ID-based comparison
        if place_id:
            id_score = similarity(id_normalized, photo['normalized'])
            score = max(score, id_score)
        
        if score > best_score:
            best_score = score
            best_match = photo['url']
    
    return best_match

def process_city(city_id, dry_run=True):
    """Process a city with fuzzy matching"""
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
    unmatched_names = []
    
    # Process highlights
    for place in data.get('highlights', []):
        image_url = place.get('imageUrl', '')
        if 'maps.googleapis.com' not in image_url:
            continue
        
        place_name = place.get('name', '')
        place_id = place.get('id', '')
        
        # Find best match
        firebase_url = find_best_match(place_name, place_id, firebase_photos)
        
        if firebase_url:
            place['imageUrl'] = firebase_url
            matched += 1
        else:
            unmatched += 1
            unmatched_names.append(place_name[:30])
    
    # Process heroImage
    hero_url = data.get('heroImage', '')
    if 'maps.googleapis.com' in hero_url:
        # Use city cover or first photo
        for photo in firebase_photos:
            if 'hero' in photo['filename'] or 'cover' in photo['filename']:
                data['heroImage'] = photo['url']
                matched += 1
                break
        else:
            if firebase_photos:
                data['heroImage'] = firebase_photos[0]['url']
                matched += 1
    
    # Save if not dry run
    if not dry_run and matched > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return {
        'city': city_id,
        'matched': matched,
        'unmatched': unmatched,
        'firebase_photos': len(firebase_photos),
        'unmatched_names': unmatched_names[:3]
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true', help='Apply changes')
    parser.add_argument('--city', type=str, help='Process specific city')
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("=" * 60)
    print("FUZZY PHOTO MATCHING")
    print("Mode:", "DRY RUN" if dry_run else "EXECUTE")
    print("=" * 60)
    
    # Initialize Firebase
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    
    # Find cities with Places API URLs
    problem_cities = []
    for json_file in CITIES_DIR.glob("*.json"):
        with open(json_file, 'r') as f:
            content = f.read()
        if 'maps.googleapis.com' in content:
            count = content.count('maps.googleapis.com')
            problem_cities.append((json_file.stem, count))
    
    problem_cities.sort(key=lambda x: x[1], reverse=True)
    
    if args.city:
        problem_cities = [(c, n) for c, n in problem_cities if c == args.city]
    
    print(f"\nCities to process: {len(problem_cities)}")
    print("-" * 60)
    
    total_matched = 0
    total_unmatched = 0
    
    for city_id, count in problem_cities:
        print(f"\n📷 {city_id} ({count} Places API URLs)...")
        result = process_city(city_id, dry_run=dry_run)
        if result:
            total_matched += result['matched']
            total_unmatched += result['unmatched']
            status = "✓" if result['unmatched'] == 0 else "⚠️"
            print(f"   {status} Matched: {result['matched']}, Unmatched: {result['unmatched']} (Firebase: {result['firebase_photos']})")
            if result.get('unmatched_names'):
                print(f"      Samples: {result['unmatched_names']}")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Total matched:   {total_matched}")
    print(f"  Total unmatched: {total_unmatched}")
    
    if dry_run:
        print("\n💡 Run with --execute to apply changes")
    else:
        print("\n✓ Changes applied!")

if __name__ == "__main__":
    main()

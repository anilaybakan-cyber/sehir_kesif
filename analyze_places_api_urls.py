#!/usr/bin/env python3
"""
Analyze Places API URLs in city JSON files and generate a report.
This script identifies which images need to be uploaded to Firebase Storage.
"""
import json
import os
import re
from pathlib import Path

CITIES_DIR = Path("assets/cities")
FIREBASE_STORAGE_BASE = "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities"

# Pattern to match Places API photo URLs
PLACES_API_PATTERN = re.compile(r'https://maps\.googleapis\.com/maps/api/place/photo\?.*?photo_reference=([^&"]+)')

def analyze_city(json_path):
    """Analyze a city JSON file for Places API URLs"""
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all Places API photo references
    matches = PLACES_API_PATTERN.findall(content)
    
    # Also check for heroImage
    data = json.loads(content)
    hero_uses_places = 'heroImage' in data and 'maps.googleapis.com' in str(data.get('heroImage', ''))
    
    return {
        'file': json_path.name,
        'city_id': json_path.stem,
        'places_api_count': len(matches),
        'hero_uses_places': hero_uses_places,
        'photo_references': matches[:5]  # Store first 5 for reference
    }

def main():
    results = []
    total_places_urls = 0
    
    for json_file in sorted(CITIES_DIR.glob("*.json")):
        analysis = analyze_city(json_file)
        if analysis['places_api_count'] > 0:
            results.append(analysis)
            total_places_urls += analysis['places_api_count']
    
    # Sort by count descending
    results.sort(key=lambda x: x['places_api_count'], reverse=True)
    
    print("=" * 60)
    print("PLACES API URL ANALYSIS REPORT")
    print("=" * 60)
    print(f"\nTotal cities with Places API URLs: {len(results)}")
    print(f"Total Places API photo calls: {total_places_urls}")
    print(f"\nEstimated monthly cost at current usage: ~₺{total_places_urls * 0.5:.0f}")
    print("\n" + "-" * 60)
    print("CITIES USING PLACES API (sorted by count):")
    print("-" * 60)
    
    for r in results:
        hero_flag = " [HERO!]" if r['hero_uses_places'] else ""
        print(f"  {r['city_id']:20} : {r['places_api_count']:4} photos{hero_flag}")
    
    print("\n" + "-" * 60)
    print("PRIORITY ACTIONS:")
    print("-" * 60)
    
    # High priority (>50 photos)
    high_priority = [r for r in results if r['places_api_count'] >= 50]
    if high_priority:
        print("\n🔴 HIGH PRIORITY (50+ photos each):")
        for r in high_priority:
            print(f"   - {r['city_id']}: {r['places_api_count']} photos")
    
    # Medium priority (10-49 photos)
    medium_priority = [r for r in results if 10 <= r['places_api_count'] < 50]
    if medium_priority:
        print("\n🟡 MEDIUM PRIORITY (10-49 photos each):")
        for r in medium_priority:
            print(f"   - {r['city_id']}: {r['places_api_count']} photos")
    
    # Low priority (<10 photos)
    low_priority = [r for r in results if r['places_api_count'] < 10]
    if low_priority:
        print("\n🟢 LOW PRIORITY (<10 photos each):")
        for r in low_priority:
            print(f"   - {r['city_id']}: {r['places_api_count']} photos")
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("""
1. Check Firebase Storage for existing photos:
   https://console.firebase.google.com/u/0/project/myway-3fe75/storage

2. For cities with photos in Storage, run the URL replacement script.

3. For cities without photos, download from Places API once and upload.
""")

if __name__ == "__main__":
    main()

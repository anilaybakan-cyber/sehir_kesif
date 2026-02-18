
#!/usr/bin/env python3
"""
Smart Fix Photos Script
Tries to find photos for the failed 57 places by:
1. Cleaning names (removing parentheses, extra text)
2. Adding city to query
3. Searching with broader terms
"""

import csv
import json
import requests
import time
import os
import re
import firebase_admin
from firebase_admin import credentials, storage

# --- CONFIGURATION ---
CSV_PATH = os.path.expanduser('~/Desktop/failed_photos.csv')
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'
BUCKET_NAME = 'myway-3fe75.firebasestorage.app'

# --- FIREBASE SETUP ---
cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': BUCKET_NAME
})
BUCKET = storage.bucket()

def clean_place_name(name):
    """Cleans place name for better search results"""
    # Remove text in parentheses: "Tomatakia (Domates Köftesi)" -> "Tomatakia"
    name = re.sub(r'\(.*?\)', '', name).strip()
    return name

def search_place_photo_smart(city, place_name):
    """Search Google Places with multiple strategies"""
    queries = []
    
    clean_name = clean_place_name(place_name)
    
    # Strategy 1: Clean Name + City
    queries.append(f"{clean_name} {city}")
    
    # Strategy 2: Clean Name + City + "Restaurant" (if looks like a place)
    queries.append(f"{clean_name} {city} restaurant")
    
    # Strategy 3: Clean Name + City + "Hotel"
    queries.append(f"{clean_name} {city} hotel")
    
    # Strategy 4: Just Clean Name (if very unique)
    if len(clean_name) > 10:
         queries.append(f"{clean_name}")

    for query in queries:
        print(f"    Trying query: {query}")
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"
        
        try:
            res = requests.get(url)
            data = res.json()
            
            if data.get('status') == 'OK' and data.get('results'):
                result = data['results'][0]
                if 'photos' in result:
                    photo_ref = result['photos'][0]['photo_reference']
                    return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
        except Exception as e:
            print(f"    Search error: {e}")
            
        time.sleep(0.5)
    
    return None

def download_image(url, local_path):
    try:
        response = requests.get(url, stream=True, allow_redirects=True, timeout=30)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception:
        return False
    return False

def upload_to_firebase(local_path, remote_path):
    try:
        blob = BUCKET.blob(remote_path)
        blob.upload_from_filename(local_path)
        blob.make_public()
        return f"https://storage.googleapis.com/{BUCKET.name}/{remote_path}"
    except Exception:
        return None

def update_city_json(city, place_name, firebase_url):
    city_slug = city.lower().replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
    json_path = f"assets/cities/{city_slug}.json"
    
    # Handlers for mismatches
    if city == 'İstanbul': json_path = "assets/cities/istanbul.json"
    if city == 'Kopenhag': json_path = "assets/cities/kopenhag.json"
    
    if not os.path.exists(json_path):
        # Fallback search
        import glob
        files = glob.glob(f"assets/cities/*.json")
        for f in files:
            if city_slug in f:
                json_path = f
                break
    
    if not os.path.exists(json_path):
        print(f"  ❌ JSON not found for {city}")
        return False
        
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        updated = False
        for place in data.get('highlights', []):
            if place.get('name') == place_name:
                place['imageUrl'] = firebase_url
                place['source'] = 'firebase'
                updated = True
                break
        
        if updated:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
            
    except Exception as e:
        print(f"  Update error: {e}")
        
    return False

def main():
    print(f"Reading {CSV_PATH}...")
    
    try:
        with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f) # Default comma for the generated report
            header = next(reader)
            places = list(reader)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Found {len(places)} failed places to retry with smart search.")
    
    success_count = 0
    
    for i, row in enumerate(places):
        if len(row) < 2: continue
        city = row[0]
        place_name = row[1]
        
        print(f"\n[{i+1}/{len(places)}] Retrying {place_name} ({city})...")
        
        photo_url = search_place_photo_smart(city, place_name)
        
        if photo_url:
            print("  📸 Photo found!")
            
            safe_id = "".join([c if c.isalnum() else "_" for c in place_name.lower()])
            city_slug = city.lower().replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
            
            local_path = f"/tmp/{safe_id}_smart.jpg"
            remote_path = f"cities/{city_slug}/{safe_id}.jpg"
            
            if download_image(photo_url, local_path):
                firebase_url = upload_to_firebase(local_path, remote_path)
                if firebase_url:
                    if update_city_json(city, place_name, firebase_url):
                        print(f"  ✅ Fixed: {place_name}")
                        success_count += 1
                    else:
                        print("  ❌ JSON update failed")
            
            if os.path.exists(local_path):
                os.remove(local_path)
        else:
            print("  ❌ Still no photo found")
            
    print(f"\nSmart Fix Complete. Fixed: {success_count}/{len(places)}")

if __name__ == "__main__":
    main()

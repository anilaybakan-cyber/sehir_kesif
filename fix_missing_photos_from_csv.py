
#!/usr/bin/env python3
"""
Fix Missing Photos Script
Reads 'eksikler.csv' from Desktop, finds real photos via Google Places API,
uploads to Firebase, and updates city JSON files.
"""

import csv
import json
import requests
import time
import os
import firebase_admin
from firebase_admin import credentials, storage

# --- CONFIGURATION ---
CSV_PATH = os.path.expanduser('~/Desktop/eksikler.csv')
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'
BUCKET_NAME = 'myway-3fe75.firebasestorage.app'

# --- FIREBASE SETUP ---
cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': BUCKET_NAME
})
BUCKET = storage.bucket()

def search_place_photo(city, place_name):
    """Search Google Places for a photo of the place"""
    query = f"{place_name} {city}"
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
        print(f"  Search error: {e}")
    
    return None

def download_image(url, local_path):
    """Downloads an image from URL to local path"""
    try:
        response = requests.get(url, stream=True, allow_redirects=True, timeout=30)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"  Download error: {e}")
    return False

def upload_to_firebase(local_path, remote_path):
    """Uploads local file to Firebase Storage and returns public URL"""
    try:
        blob = BUCKET.blob(remote_path)
        blob.upload_from_filename(local_path)
        blob.make_public()
        return f"https://storage.googleapis.com/{BUCKET.name}/{remote_path}"
    except Exception as e:
        print(f"  Upload error: {e}")
    return None

def update_city_json(city, place_name, firebase_url):
    """Updates the city JSON file with the new URL"""
    city_slug = city.lower().replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
    # Special case mappings if needed, or rely on file existence
    json_path = f"assets/cities/{city_slug}.json"
    
    if not os.path.exists(json_path):
        # Try finding the file if slug mistmatch
        import glob
        files = glob.glob(f"assets/cities/*.json")
        for f in files:
            if city_slug in f:
                json_path = f
                break
        
    if not os.path.exists(json_path):
        print(f"  ❌ Error: JSON file not found for {city} ({json_path})")
        return False
        
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        updated = False
        for place in data.get('highlights', []):
            if place.get('name') == place_name:
                place['imageUrl'] = firebase_url
                place['source'] = 'firebase' # Mark as updated
                updated = True
                break
        
        if updated:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        else:
            print(f"  ⚠️ Place '{place_name}' not found in {json_path}")
            
    except Exception as e:
        print(f"  JSON Update Error: {e}")
        
    return False

def main():
    print(f"Reading {CSV_PATH}...")
    
    places_to_fix = []
    
    # Read CSV with hardcoded delimiter
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        
        try:
            header = next(reader) # Skip header
        except StopIteration:
            print("Empty CSV file")
            return

        # Check column indices based on header if possible, or assume 0=City, 2=Name
        city_idx = 0
        name_idx = 2
        
        if 'City' in header:
            city_idx = header.index('City')
        if 'Place Name (TR)' in header:
            name_idx = header.index('Place Name (TR)')
            
        print(f"Using columns: City={city_idx}, Name={name_idx}")
        
        for row in reader:
            if len(row) > name_idx:
                city = row[city_idx].strip()
                place_name = row[name_idx].strip()
                if place_name and city:
                    places_to_fix.append((city, place_name))

    print(f"Found {len(places_to_fix)} places to process.")
    
    success_count = 0
    
    for i, (city, place_name) in enumerate(places_to_fix):
        print(f"\n[{i+1}/{len(places_to_fix)}] Processing {place_name} ({city})...")
        
        # 1. Find Photo
        photo_url = search_place_photo(city, place_name)
        if not photo_url:
            print("  ❌ No photo found on Google Maps")
            continue
            
        print("  📸 Photo found")
        
        # 2. Download & Upload
        safe_id = "".join([c if c.isalnum() else "_" for c in place_name.lower()])
        local_path = f"/tmp/{safe_id}_fix.jpg"
        city_slug = city.lower().replace('ö','o').replace('ü','u').replace('ğ','g').replace('ş','s').replace('ç','c').replace('ı','i')
        remote_path = f"cities/{city_slug}/{safe_id}.jpg"
        
        if download_image(photo_url, local_path):
            firebase_url = upload_to_firebase(local_path, remote_path)
            
            if firebase_url:
                print(f"  ☁️ Uploaded: {firebase_url}")
                
                # 3. Update JSON
                if update_city_json(city, place_name, firebase_url):
                    print("  ✅ JSON Updated")
                    success_count += 1
                
                # Cleanup
                if os.path.exists(local_path):
                    os.remove(local_path)
            else:
                print("  ❌ Firebase upload failed")
        
        time.sleep(0.5) # Rate limiting

    print(f"\nDone! Successfully updated {success_count}/{len(places_to_fix)} places.")

if __name__ == "__main__":
    main()

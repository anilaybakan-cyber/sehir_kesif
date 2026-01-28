
#!/usr/bin/env python3
"""
Fix San Sebastian Photos Script
Specifically targets San Sebastian which failed due to file naming issues.
"""

import json
import requests
import time
import os
import firebase_admin
from firebase_admin import credentials, storage

# --- CONFIGURATION ---
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'
BUCKET_NAME = 'myway-3fe75.firebasestorage.app'
CITY_FILE = "assets/cities/san_sebastian.json"

# List of failed San Sebastian places from the logs
PLACES_TO_FIX = [
    "A Fuego Negro",
    "Aralar Mendi Elkartea",
    "Atari",
    "Jazzaldia",
    "Motorboat to Santa Clara",
    "Plaza de la Constitucion",
    "San Pedro Pasai",
    "San Sebastian Food"
]

# --- FIREBASE SETUP ---
cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': BUCKET_NAME
})
BUCKET = storage.bucket()

def search_place_photo(query):
    print(f"  Searching for: {query}")
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
    return None

def main():
    if not os.path.exists(CITY_FILE):
        print(f"File not found: {CITY_FILE}")
        return

    with open(CITY_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_count = 0
    
    for place_name in PLACES_TO_FIX:
        print(f"\nProcessing: {place_name}")
        
        # Try finding the place in JSON first
        target_place = None
        for p in data['highlights']:
            if p['name'] == place_name:
                target_place = p
                break
        
        if not target_place:
            print("  ❌ Place not found in JSON")
            continue
            
        # Search photo
        query = f"{place_name} San Sebastian"
        photo_url = search_place_photo(query)
        
        if photo_url:
            print("  📸 Photo found")
            
            # Download/Upload
            safe_id = "".join([c if c.isalnum() else "_" for c in place_name.lower()])
            local_path = f"/tmp/{safe_id}_ss.jpg"
            remote_path = f"cities/san_sebastian/{safe_id}.jpg"
            
            try:
                # Download
                r = requests.get(photo_url, stream=True)
                if r.status_code == 200:
                    with open(local_path, 'wb') as f:
                        f.write(r.content)
                    
                    # Upload
                    blob = BUCKET.blob(remote_path)
                    blob.upload_from_filename(local_path)
                    blob.make_public()
                    firebase_url = f"https://storage.googleapis.com/{BUCKET_NAME}/{remote_path}"
                    
                    # Update JSON object
                    target_place['imageUrl'] = firebase_url
                    target_place['source'] = 'firebase'
                    updated_count += 1
                    print(f"  ✅ Updated: {firebase_url}")
                    
                    if os.path.exists(local_path):
                        os.remove(local_path)
            except Exception as e:
                print(f"  Error: {e}")
        else:
            print("  ❌ No photo found on Google")
            
    # Save file
    if updated_count > 0:
        with open(CITY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\nSuccessfully updated {updated_count} places in {CITY_FILE}")

if __name__ == "__main__":
    main()

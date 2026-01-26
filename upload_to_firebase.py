#!/usr/bin/env python3
"""
Firebase Storage Upload Script
Downloads Google Places API photos and uploads to Firebase Storage
Updates JSON files with Firebase Storage URLs
"""

import json
import requests
import time
import os
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin
cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'myway-3fe75.firebasestorage.app'
})

BUCKET = storage.bucket()
API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

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

def process_city(city_name):
    """Process all highlights for a city and upload images to Firebase"""
    filepath = f'assets/cities/{city_name}.json'
    
    # Load city data
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    highlights = data['highlights']
    updated_count = 0
    
    print(f"\n{'='*50}")
    print(f"Processing: {city_name} ({len(highlights)} highlights)")
    print(f"{'='*50}")
    
    for i, h in enumerate(highlights):
        name = h.get('name', 'Unknown')
        current_url = h.get('imageUrl', '')
        
        # Skip if already has Firebase URL
        if 'storage.googleapis.com/myway-3fe75' in current_url:
            continue
        
        # Skip if no valid Google API URL
        if 'googleapis.com/maps/api/place/photo' not in current_url:
            continue
        
        print(f"\n[{i+1}/{len(highlights)}] {name}")
        
        # Create safe filename
        place_id = h.get('id', name.lower().replace(' ', '_'))
        place_id = ''.join(c if c.isalnum() or c in '-_' else '_' for c in place_id)
        
        local_path = f"/tmp/{place_id}.jpg"
        remote_path = f"cities/{city_name}/{place_id}.jpg"
        
        # Download from Google
        print(f"  Downloading...")
        if download_image(current_url, local_path):
            # Upload to Firebase
            print(f"  Uploading to Firebase...")
            firebase_url = upload_to_firebase(local_path, remote_path)
            
            if firebase_url:
                h['imageUrl'] = firebase_url
                h['source'] = 'firebase'
                updated_count += 1
                print(f"  ✓ Done: {firebase_url}")
            
            # Cleanup local file
            if os.path.exists(local_path):
                os.remove(local_path)
        
        time.sleep(0.3)  # Rate limiting
    
    # Save updated data
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ {city_name}: {updated_count} images uploaded to Firebase")
    return updated_count

def main():
    """Main function - process specified cities"""
    import sys
    
    # Get city names from command line arguments, or use defaults
    if len(sys.argv) > 1:
        cities = sys.argv[1:]
    else:
        # Default: process recently enriched cities
        cities = ['heidelberg', 'antalya', 'strazburg', 'gaziantep']
    
    total_updated = 0
    for city in cities:
        try:
            count = process_city(city)
            total_updated += count
        except Exception as e:
            print(f"Error processing {city}: {e}")
    
    print(f"\n{'='*50}")
    print(f"TOTAL: {total_updated} images uploaded to Firebase")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

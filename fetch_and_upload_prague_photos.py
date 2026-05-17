from dotenv import load_dotenv
load_dotenv()

import csv
import json
import requests
import time
import os
import firebase_admin
from firebase_admin import credentials, storage

# --- CONFIGURATION ---
CSV_Input_Path = '/Users/anilebru/Desktop/prag_yeni_mekan_onerileri_full.csv'
CSV_Output_Path = '/Users/anilebru/Desktop/prag_yeni_mekan_onerileri_final.csv'
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY") # Taken from AndroidManifest.xml
BUCKET_NAME = 'myway-3fe75.firebasestorage.app'

# --- FIREBASE SETUP ---
try:
    cred = credentials.Certificate('service_account.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': BUCKET_NAME
    })
    BUCKET = storage.bucket()
    print("Firebase initialized successfully.")
except Exception as e:
    print(f"Firebase initialization failed: {e}")
    exit(1)

def search_place_photo(place_name, lat, lng):
    """Search Google Places for a photo of the place using text search with location bias"""
    query = f"{place_name} Prague"
    # locationbias=circle:radius@lat,lng could be used, or just text query with city
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"
    
    try:
        res = requests.get(url)
        data = res.json()
        
        if data.get('status') == 'OK' and data.get('results'):
            result = data['results'][0]
            if 'photos' in result:
                photo_ref = result['photos'][0]['photo_reference']
                # Max width 800 is a good trade-off for quality/size
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
            else:
                print(f"  ⚠️ No photos found for {place_name} in API result.")
        else:
             print(f"  ⚠️ Place not found or API error for {place_name}: {data.get('status')}")
             if data.get('error_message'):
                 print(f"     Error message: {data.get('error_message')}")

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
        else:
            print(f"  ❌ Download failed with status: {response.status_code}")
    except Exception as e:
        print(f"  Download error: {e}")
    return False

def upload_to_firebase(local_path, remote_path):
    """Uploads local file to Firebase Storage and returns public URL"""
    try:
        blob = BUCKET.blob(remote_path)
        blob.upload_from_filename(local_path)
        blob.make_public()
        return blob.public_url
    except Exception as e:
        print(f"  Upload error: {e}")
    return None

def main():
    print(f"Reading {CSV_Input_Path}...")
    
    venues = []
    fieldnames = []

    try:
        with open(CSV_Input_Path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            if 'imageUrl' not in fieldnames:
                 fieldnames.append('imageUrl')
            venues = list(reader)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Found {len(venues)} venues. Starting photo fetch...")
    
    success_count = 0
    
    for i, venue in enumerate(venues):
        place_name = venue['name']
        place_id = venue['id']
        lat = venue.get('lat')
        lng = venue.get('lng')

        print(f"\n[{i+1}/{len(venues)}] Processing {place_name}...")
        
        # 1. Find Photo URL from Google
        google_photo_url = search_place_photo(place_name, lat, lng)
        
        if google_photo_url:
            print("  📸 Photo match found on Google.")
            
            # 2. Download and Upload to Firebase
            local_filename = f"temp_{place_id}.jpg"
            remote_path = f"cities/prag/{place_id}.jpg" # Consistent naming
            
            if download_image(google_photo_url, local_filename):
                firebase_url = upload_to_firebase(local_filename, remote_path)
                
                if firebase_url:
                    print(f"  ☁️ Uploaded to Firebase: {firebase_url}")
                    venue['imageUrl'] = firebase_url # Update the venue object
                    success_count += 1
                else:
                     print("  ❌ Firebase upload failed. Keeping placeholder.")
                
                # Cleanup
                if os.path.exists(local_filename):
                    os.remove(local_filename)
            else:
                 print("  ❌ Image download failed. Keeping placeholder.")
        else:
            print("  ⚠️ No matching photo found. Keeping placeholder.")
            
        time.sleep(1) # Be nice to the API

    # Write updated CSV
    print(f"\nWriting updated data to {CSV_Output_Path}...")
    try:
        with open(CSV_Output_Path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(venues)
        print("Done!")
    except Exception as e:
        print(f"Error writing CSV: {e}")

if __name__ == "__main__":
    main()

import json
import requests
import time
import urllib.parse
import os

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

def get_google_photo_url(place_name):
    """
    Fetches a photo URL for the given place_name using Google Places API.
    Returns None if not found or error.
    """
    try:
        # 1. Search for the place to get Place ID and Photo Reference
        search_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(place_name)}&inputtype=textquery&fields=photos&key={API_KEY}"
        
        response = requests.get(search_url)
        data = response.json()
        
        if 'candidates' in data and data['candidates']:
            candidate = data['candidates'][0]
            if 'photos' in candidate:
                photo_reference = candidate['photos'][0]['photo_reference']
                
                # 2. Construct the Photo URL (Max width 800)
                # Note: We don't need to make a request here, just construct the URL for the app to use
                # BUT the app might expect a direct image link or the google API link.
                # The previous script verified the link works.
                # Let's verify if we need to actually fetch the redirect or just store the API url.
                # In enrich_prag_master, we stored the F_IMG_URL.
                # Let's actually resolve it to a static URL if possible, OR just use the API url if that's what the user wants.
                # User constraint: "use the Google Places API for all imageUrl fields... eventually uploading these to Firebase".
                # If we put the API url, it might expire or cost money on every view.
                # However, for now, we will stick to the pattern used in Prague script:
                # `return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={API_KEY}"`
                # WAIT! In Prague script I used:
                # `return photo_url` which was the direct API link.
                
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={API_KEY}"
        
        return None
    
    except Exception as e:
        print(f"Error fetching photo for {place_name}: {e}")
        return None

def fix_viyana_images():
    filepath = 'assets/cities/viyana.json'
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        highlights = data.get('highlights', [])
        
        updated_count = 0
        total_highlights = len(highlights)
        print(f"Checking {total_highlights} highlights in Vienna...")
        
        for i, place in enumerate(highlights):
            img_url = place.get('imageUrl', '')
            place_name = place.get('name')
            
            # Check if image is from Unsplash or empty or not Google
            if 'unsplash.com' in img_url or not img_url or ('googleapis.com' not in img_url and 'firebasestorage' not in img_url):
                print(f"[{i+1}/{total_highlights}] Fixing image for: {place_name} (Current: {img_url[:30]}...)")
                
                new_url = get_google_photo_url(place_name)
                time.sleep(1) # Rate limit respect
                
                if new_url:
                    place['imageUrl'] = new_url
                    updated_count += 1
                    print(f"   -> Fixed!")
                else:
                    print(f"   -> Could not find Google Image.")
            else:
                # print(f"[{i+1}/{total_highlights}] Skipping {place_name} (Already valid)")
                pass
                
        if updated_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Successfully updated {updated_count} images in {filepath}.")
        else:
            print("No images needed fixing.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_viyana_images()

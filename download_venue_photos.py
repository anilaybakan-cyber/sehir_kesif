#!/usr/bin/env python3
"""
Download real venue photos using Google Places API
"""
import os
import csv
import requests
import time
from urllib.parse import quote

# Google API Key from .env
API_KEY = "AIzaSyBSZJmb9IIINxWbxXgCLTPiWC9SLcaDrMk"

# Output directory
OUTPUT_DIR = "prag_venue_photos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def search_place(venue_name, lat, lng):
    """Search for a place using text search with location bias"""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"{venue_name} Prague restaurant",
        "location": f"{lat},{lng}",
        "radius": 500,
        "key": API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data.get("results"):
        return data["results"][0]
    return None

def get_place_photo(photo_reference, max_width=800):
    """Get photo URL from photo reference"""
    url = f"https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "maxwidth": max_width,
        "photo_reference": photo_reference,
        "key": API_KEY
    }
    
    # This returns a redirect, so we need to follow it
    response = requests.get(url, params=params, allow_redirects=True)
    return response.url

def download_photo(url, filename):
    """Download photo to file"""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
    return False

def process_venues(csv_file):
    """Process all venues from CSV"""
    results = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        venues = list(reader)
    
    print(f"Processing {len(venues)} venues...")
    
    for i, venue in enumerate(venues):
        name = venue['name']
        lat = venue['lat']
        lng = venue['lng']
        
        print(f"\n[{i+1}/{len(venues)}] Searching: {name}")
        
        # Search for place
        place = search_place(name, lat, lng)
        
        if place and place.get("photos"):
            photo_ref = place["photos"][0]["photo_reference"]
            photo_url = get_place_photo(photo_ref)
            
            # Create safe filename
            safe_name = name.lower().replace(" ", "_").replace("'", "").replace('"', "")
            safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '_')
            filename = f"{OUTPUT_DIR}/{safe_name}.jpg"
            
            # Download photo
            if download_photo(photo_url, filename):
                print(f"  ✅ Downloaded: {filename}")
                results.append({
                    "name": name,
                    "photo_file": filename,
                    "photo_url": photo_url,
                    "place_id": place.get("place_id", "")
                })
            else:
                print(f"  ❌ Failed to download")
                results.append({"name": name, "photo_file": "", "photo_url": "", "place_id": ""})
        else:
            print(f"  ⚠️ No photos found")
            results.append({"name": name, "photo_file": "", "photo_url": "", "place_id": ""})
        
        # Rate limiting
        time.sleep(0.5)
    
    # Save results
    with open("prag_venue_photos_results.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "photo_file", "photo_url", "place_id"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\n✅ Done! Results saved to prag_venue_photos_results.csv")
    print(f"   Photos downloaded to {OUTPUT_DIR}/")

if __name__ == "__main__":
    process_venues("prag_yeni_50_mekan_enriched.csv")

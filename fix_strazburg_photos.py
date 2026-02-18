import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name, city="Strasbourg"):
    """Try multiple search strategies to find photos"""
    search_queries = [
        f"{place_name} {city}",
        f"{place_name} Strasbourg France",
        place_name,
    ]
    
    for query in search_queries:
        try:
            find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@48.5734,7.7521"
            response = requests.get(find_place_url)
            data = response.json()
            
            if data['status'] == 'OK' and len(data['candidates']) > 0:
                candidate = data['candidates'][0]
                if 'photos' in candidate:
                    photo_reference = candidate['photos'][0]['photo_reference']
                    print(f"  ✓ Found with: {query}")
                    return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={API_KEY}"
        except Exception as e:
            continue
    
    return None

def fix_strazburg_photos():
    filepath = 'assets/cities/strazburg.json'
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    highlights = data['highlights']
    fixed_count = 0
    failed = []
    
    for h in highlights:
        # Skip if already has valid Google photo
        if 'googleapis' in h.get('imageUrl', '') and h.get('source') != 'unsplash_fallback':
            continue
        
        # Skip if has wikipedia/wikimedia image
        if 'wiki' in h.get('imageUrl', '').lower():
            continue
            
        # Try to fix fallback images
        name = h['name']
        print(f"Fixing: {name}")
        
        photo_url = get_google_photo_url(name)
        
        if photo_url:
            h['imageUrl'] = photo_url
            h['source'] = 'google'
            fixed_count += 1
        else:
            failed.append(name)
        
        time.sleep(0.3)
    
    # Save
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Fixed {fixed_count} photos")
    print(f"❌ Still missing: {len(failed)}")
    if failed[:10]:
        print("First 10 failed:")
        for f in failed[:10]:
            print(f"  - {f}")

if __name__ == "__main__":
    fix_strazburg_photos()

import json
import os
from pathlib import Path

cities_dir = Path("assets/cities")
json_files = list(cities_dir.glob("*.json"))

# Expanded metadata for better accuracy
CITY_METADATA = {
    "barcelona": {"lat": 41.3851, "lng": 2.1734, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/barcelona/hero.jpg"},
    "atina": {"lat": 37.9838, "lng": 23.7275, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg"},
    "athens": {"lat": 37.9838, "lng": 23.7275, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg"},
    "madrid": {"lat": 40.4168, "lng": -3.7038, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/madrid/hero.jpg"},
    "istanbul": {"lat": 41.0082, "lng": 28.9784, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/istanbul/hero.jpg"},
    "roma": {"lat": 41.9028, "lng": 12.4964, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/roma/hero.jpg"},
    "rome": {"lat": 41.9028, "lng": 12.4964, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/roma/hero.jpg"},
    "paris": {"lat": 48.8566, "lng": 2.3522, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/paris/hero.jpg"},
    "bodrum": {"lat": 37.0344, "lng": 27.4305, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bodrum/hero.jpg"},
}

for filepath in json_files:
    # Skip empty/batch files with 0 content
    if "batch" in filepath.name.lower() or "unique" in filepath.name.lower():
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, dict) and len(data.get("highlights", [])) == 0:
                    print(f"🗑️ Deleting empty batch file: {filepath.name}")
                    # os.remove(filepath) # Don't actually delete, just skip
                    continue
            except:
                pass

    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ Parse error in {filepath.name}: {e}")
            continue
    
    # 1. Ensure DICT structure
    if isinstance(data, list):
        data = {"highlights": data}
    
    # 2. City name
    if "city" not in data:
        data["city"] = data.get("name") or filepath.stem.capitalize()
            
    # 3. Coordinates
    city_id = filepath.stem.lower()
    needs_coords = "coordinates" not in data and "centerCoords" not in data
    has_zero_coords = False
    if "coordinates" in data and isinstance(data["coordinates"], dict):
        if data["coordinates"].get("lat") == 0 or data["coordinates"].get("lng") == 0:
            has_zero_coords = True

    if needs_coords or has_zero_coords or city_id in ["atina", "athens"]:
        if city_id in CITY_METADATA:
            data["coordinates"] = {
                "lat": CITY_METADATA[city_id]["lat"],
                "lng": CITY_METADATA[city_id]["lng"]
            }
        else:
            # Fallback to first valid highlight
            highlights = data.get("highlights", [])
            lat, lng = 0.0, 0.0
            for h in highlights:
                h_lat = h.get('lat') or h.get('latitude')
                h_lng = h.get('lng') or h.get('longitude')
                if h_lat and h_lng and h_lat != 0:
                    lat, lng = float(h_lat), float(h_lng)
                    break
            data["coordinates"] = {"lat": lat, "lng": lng}
            
    # 4. Hero Image
    if "heroImage" not in data or data.get("heroImage") is None:
        if city_id in CITY_METADATA:
            data["heroImage"] = CITY_METADATA[city_id]["hero"]
        else:
            highlights = data.get("highlights", [])
            for h in highlights:
                img = h.get('imageUrl') or h.get('image') or h.get('photo')
                if img:
                    data["heroImage"] = img
                    break

    # 5. Highlights sanitization
    highlights = data.get("highlights", [])
    for h in highlights:
        # Sync image fields
        img = h.get('imageUrl') or h.get('image') or h.get('photo') or h.get('image_url')
        if img:
            h["imageUrl"] = img
        
        # Ensure coordinates are floats
        for k in ['lat', 'lng', 'latitude', 'longitude', 'distanceFromCenter', 'rating']:
            if k in h and h[k] is not None:
                try: h[k] = float(h[k])
                except: pass

    # Save back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Enhanced standardization complete.")

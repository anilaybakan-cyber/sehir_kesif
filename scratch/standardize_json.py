import json
import os
from pathlib import Path

cities_dir = Path("assets/cities")
json_files = list(cities_dir.glob("*.json"))

# A map of common city names to their coordinates and hero images if missing
CITY_METADATA = {
    "barcelona": {"lat": 41.3851, "lng": 2.1734, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/barcelona/hero.jpg"},
    "madrid": {"lat": 40.4168, "lng": -3.7038, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/madrid/hero.jpg"},
    "istanbul": {"lat": 41.0082, "lng": 28.9784, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/istanbul/hero.jpg"},
    "roma": {"lat": 41.9028, "lng": 12.4964, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/roma/hero.jpg"},
    "paris": {"lat": 48.8566, "lng": 2.3522, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/paris/hero.jpg"},
    "bodrum": {"lat": 37.0344, "lng": 27.4305, "hero": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bodrum/hero.jpg"},
}

for filepath in json_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ Parse error in {filepath.name}: {e}")
            continue
    
    # Ensure it's a dict
    if isinstance(data, list):
        print(f"📦 Converting {filepath.name} from LIST to DICT...")
        data = {
            "city": filepath.stem.capitalize(),
            "highlights": data
        }
    
    # 1. Ensure 'city' key exists
    if "city" not in data:
        if "name" in data:
            data["city"] = data["name"]
        else:
            data["city"] = filepath.stem.capitalize()
            
    # 2. Ensure 'coordinates' exists at top level
    if "coordinates" not in data and "centerCoords" not in data:
        city_id = filepath.stem.lower()
        if city_id in CITY_METADATA:
            data["coordinates"] = {
                "lat": CITY_METADATA[city_id]["lat"],
                "lng": CITY_METADATA[city_id]["lng"]
            }
        else:
            # Fallback to first highlight
            highlights = data.get("highlights", [])
            lat, lng = 0.0, 0.0
            if highlights and len(highlights) > 0:
                lat = highlights[0].get('lat', 0.0)
                lng = highlights[0].get('lng', 0.0)
            data["coordinates"] = {"lat": lat, "lng": lng}
            
    # 3. Ensure 'heroImage' exists
    if "heroImage" not in data:
        city_id = filepath.stem.lower()
        if city_id in CITY_METADATA:
            data["heroImage"] = CITY_METADATA[city_id]["hero"]
        else:
            # Fallback to first highlight's image
            highlights = data.get("highlights", [])
            if highlights and len(highlights) > 0:
                data["heroImage"] = highlights[0].get('imageUrl')

    # 4. Critical fix: Ensure Highlight objects use 'imageUrl' and have correct 'lat'/'lng'
    highlights = data.get("highlights", [])
    for h in highlights:
        # If 'image' exists but 'imageUrl' doesn't, sync them
        if "image" in h and "imageUrl" not in h:
            h["imageUrl"] = h["image"]
        # Ensure lat/lng are floats
        if "lat" in h and h["lat"] is not None:
            try: h["lat"] = float(h["lat"])
            except: h["lat"] = 0.0
        if "lng" in h and h["lng"] is not None:
            try: h["lng"] = float(h["lng"])
            except: h["lng"] = 0.0

    # Save back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ All city files processed and standardized.")

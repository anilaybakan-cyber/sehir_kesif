import json
import os
from pathlib import Path

cities_dir = Path("assets/cities")
json_files = list(cities_dir.glob("*.json"))

for filepath in json_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ Parse error in {filepath.name}: {e}")
            continue
    
    if isinstance(data, list):
        print(f"📦 Converting {filepath.name} to DICT format...")
        
        # Fallback coordinates from first highlight
        center_lat = 0.0
        center_lng = 0.0
        if len(data) > 0:
            center_lat = data[0].get('lat', 0.0)
            center_lng = data[0].get('lng', 0.0)
            
        new_data = {
            "city": filepath.stem.capitalize(),
            "country": "",
            "description": "",
            "coordinates": {
                "lat": center_lat,
                "lng": center_lng
            },
            "highlights": data
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
    else:
        # Check if it has 'coordinates' or 'centerCoords'
        if "coordinates" not in data and "centerCoords" not in data:
            print(f"📍 Adding missing coordinates to {filepath.name}...")
            highlights = data.get("highlights", [])
            lat = 0.0
            lng = 0.0
            if highlights and len(highlights) > 0:
                lat = highlights[0].get('lat', 0.0)
                lng = highlights[0].get('lng', 0.0)
            data["coordinates"] = {"lat": lat, "lng": lng}
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

import json
import os
from pathlib import Path

cities_dir = Path("assets/cities")
json_files = list(cities_dir.glob("*.json"))

print(f"{'City':<20} | {'Lat':<10} | {'Lng':<10} | {'Highlights':<10} | {'Images':<10}")
print("-" * 60)

for filepath in json_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ {filepath.name:<18} | Parse Error: {e}")
            continue
    
    if isinstance(data, list):
        print(f"📦 {filepath.name:<18} | LIST format (Bad)")
        continue
        
    city = data.get("city") or data.get("name") or "Unknown"
    coords = data.get("coordinates") or data.get("centerCoords")
    lat = coords.get("lat") if isinstance(coords, dict) else (coords[0] if isinstance(coords, list) else 0)
    lng = coords.get("lng") if isinstance(coords, dict) else (coords[1] if isinstance(coords, list) else 0)
    
    highlights = data.get("highlights", [])
    has_images = all("imageUrl" in h or "image" in h for h in highlights[:5]) if highlights else False
    
    print(f"{city:<20} | {lat:<10.4f} | {lng:<10.4f} | {len(highlights):<10} | {'✅' if has_images else '❌'}")

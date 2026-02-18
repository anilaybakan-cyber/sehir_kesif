import json
import math
import os

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
for filename in os.listdir(cities_dir):
    if filename.endswith(".json"):
        with open(os.path.join(cities_dir, filename), 'r') as f:
            try:
                data = json.load(f)
                coords = data.get("coordinates")
                if not coords: continue
                c_lat = coords['lat']
                c_lng = coords['lng']
                for h in data.get("highlights", []):
                    lat = h.get("lat", 0)
                    lng = h.get("lng", 0)
                    dist = haversine(c_lat, c_lng, lat, lng)
                    if 235 <= dist <= 237:
                        print(f"🎯 MATCH in {filename}: {h['name']} | Coords: {lat}, {lng} | Dist to center: {dist:.1f} km")
            except:
                pass

import json
import math
import os

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

target_lat = 41.3917
target_lng = 2.165

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
for filename in os.listdir(cities_dir):
    if filename.endswith(".json"):
        with open(os.path.join(cities_dir, filename), 'r') as f:
            data = json.load(f)
            coords = data.get("coordinates")
            if coords:
                lat = coords.get("lat")
                lng = coords.get("lng")
                dist = haversine(target_lat, target_lng, lat, lng)
                if 230 <= dist <= 242:
                    print(f"🎯 Found: {data.get('city')} ({filename}) | Dist: {dist:.1f} km")

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
centers = {}
for filename in os.listdir(cities_dir):
    if filename.endswith(".json"):
        with open(os.path.join(cities_dir, filename), 'r') as f:
            try:
                data = json.load(f)
                coords = data.get("coordinates")
                if coords:
                    centers[data['city']] = (coords['lat'], coords['lng'])
            except:
                pass

for city1, coord1 in centers.items():
    for city2, coord2 in centers.items():
        if city1 == city2: continue
        dist = haversine(coord1[0], coord1[1], coord2[0], coord2[1])
        if 235 <= dist <= 237:
            print(f"🎯 Pair: {city1} -> {city2} | Dist: {dist:.1f} km")

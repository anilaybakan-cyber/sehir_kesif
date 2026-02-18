import json
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

with open("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/barcelona.json", 'r') as f:
    data = json.load(f)

center = data["coordinates"]
c_lat = center["lat"]
c_lng = center["lng"]

print(f"Center: {c_lat}, {c_lng}")

for h in data["highlights"]:
    lat = h.get("lat", 0)
    lng = h.get("lng", 0)
    dist = haversine(c_lat, c_lng, lat, lng)
    if dist > 200:
        print(f"🚩 High Dist: {h['name']} | Coords: {lat}, {lng} | Calc Dist: {dist:.1f} km")
    if "Casa Batlló" in h['name']:
        print(f"✅ {h['name']} | Coords: {lat}, {lng} | Calc Dist: {dist:.1f} km")

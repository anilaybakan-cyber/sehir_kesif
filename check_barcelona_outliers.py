import json

def check_barcelona():
    path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/barcelona.json"
    with open(path, 'r') as f:
        data = json.load(f)
    
    highlights = data.get("highlights", [])
    for h in highlights:
        lat = h.get("lat", 0)
        lng = h.get("lng", 0)
        # Barcelona is around 41N, 2E
        # If any coord is wildly different, report it
        if lat < 35 or lat > 45 or lng < -5 or lng > 10:
            print(f"🚩 Wilder: {h.get('name')} | Lat: {lat} | Lng: {lng}")

if __name__ == "__main__":
    check_barcelona()

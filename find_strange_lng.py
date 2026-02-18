import json

def find_strange_lng():
    path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/barcelona.json"
    with open(path, 'r') as f:
        data = json.load(f)
    
    highlights = data.get("highlights", [])
    for h in highlights:
        lng = h.get("lng", 0)
        if lng > 3:
            print(f"🚩 High Lng: {h.get('name')} | Lng: {lng}")

if __name__ == "__main__":
    find_strange_lng()

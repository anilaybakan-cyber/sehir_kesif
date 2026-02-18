import json

def check_barcelona():
    path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/barcelona.json"
    with open(path, 'r') as f:
        data = json.load(f)
    
    highlights = data.get("highlights", [])
    for h in highlights:
        name = h.get("name")
        if "Casa Batlló" in name or "Sagrada" in name or "Nacional d'Art" in name or "Liceu" in name:
            print(f"📍 {name}: Lat {h.get('lat')}, Lng {h.get('lng')}")

if __name__ == "__main__":
    check_barcelona()

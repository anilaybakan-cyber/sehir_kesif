import json
import os
import re

curated_service_path = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/lib/services/curated_routes_service.dart"
cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/"

def get_city_highlights(city_key):
    # Mapping for city names in code to json filenames
    mapping = {
        "istanbul": "istanbul", "amsterdam": "amsterdam", "barcelona": "barcelona", 
        "london": "londra", "paris": "paris", "berlin": "berlin", "rome": "roma",
        "tokyo": "tokyo", "seville": "sevilya", "madrid": "madrid", "dubai": "dubai",
        "milan": "milano", "lucerne": "luzern", "stockholm": "stokholm", "lyon": "lyon",
        "dublin": "dublin", "antalya": "antalya", "gaziantep": "gaziantep", 
        "heidelberg": "heidelberg", "sintra": "sintra", "tromso": "tromso", "zermatt": "zermatt"
    }
    
    filename = mapping.get(city_key.lower())
    if not filename:
        # Fallback to direct name
        filename = city_key.lower()

    filepath = os.path.join(cities_dir, filename + ".json")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            highlights = data.get("highlights", [])
            names = set()
            for h in highlights:
                if h.get("name"): names.add(h["name"].lower().strip())
                if h.get("name_en"): names.add(h["name_en"].lower().strip())
                if h.get("nameEn"): names.add(h["nameEn"].lower().strip())
            return names
    return set()

with open(curated_service_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all route blocks in _get[City]Routes methods
# Using a more robust regex for the method blocks
methods = re.findall(r'static List<CuratedRoute> _get(\w+)Routes.*?return \[(.*?)\];', content, re.DOTALL)

for city_name, routes_block in methods:
    highlights = get_city_highlights(city_name)
    if not highlights:
        continue

    # Find placeNames in this block
    routes = re.findall(r'CuratedRoute\(.*?\)', routes_block, re.DOTALL)
    for route in routes:
        name_match = re.search(r'name:\s*isEnglish\s*\?\s*".*?"\s*:\s*"(.*?)"', route)
        name = name_match.group(1) if name_match else "Unknown"
        
        places_match = re.search(r'placeNames:\s*\[(.*?)\]', route, re.DOTALL)
        if places_match:
            places_str = places_match.group(1)
            places = [p.strip().strip('"').strip("'") for p in places_str.split(',') if p.strip()]
            
            missing = []
            for p in places:
                if p.lower().strip() not in highlights:
                    missing.append(p)
            
            if missing:
                print(f"City: {city_name} | Route: {name}")
                print(f"  Missing stops: {missing}")
                print("-" * 20)

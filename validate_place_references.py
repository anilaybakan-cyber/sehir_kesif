import re
import json
import os
import difflib

# Mapping special city function names to json filenames
CITY_MAPPING = {
    'NewYork': 'newyork.json',
    'HongKong': 'hongkong.json',
    'SanSebastian': 'san_sebastian.json',
    # Others usually follow pattern getCityRoutes -> city.json (lowercase)
}

def get_json_filename(city_func_name):
    if city_func_name in CITY_MAPPING:
        return CITY_MAPPING[city_func_name]
    return f"{city_func_name.lower()}.json"

def normalize(text):
    if not text: return ""
    return text.lower().strip().replace("'", "").replace("’", "")

def validate():
    dart_path = 'lib/services/curated_routes_service.dart'
    json_dir = 'assets/cities'
    
    with open(dart_path, 'r', encoding='utf-8') as f:
        dart_content = f.read()

    # Find all city blocks
    city_pattern = re.compile(r'static List<CuratedRoute> _get(\w+)Routes\(bool isEnglish\) \{(.*?)\}', re.DOTALL)
    
    report = {}
    
    for city_match in city_pattern.finditer(dart_content):
        city_func_name = city_match.group(1)
        city_block = city_match.group(2)
        
        json_filename = get_json_filename(city_func_name)
        json_path = os.path.join(json_dir, json_filename)
        
        if not os.path.exists(json_path):
            print(f"WARNING: JSON file not found: {json_path} for {city_func_name}")
            continue
            
        try:
            with open(json_path, 'r', encoding='utf-8') as jf:
                city_data = json.load(jf)
                highlights = city_data.get('highlights', [])
                
                # Create lookup map (Both name and name_en)
                available_places = {}
                for h in highlights:
                    if 'name' in h: available_places[normalize(h['name'])] = h['name']
                    if 'name_en' in h: available_places[normalize(h['name_en'])] = h['name_en']
                    
        except Exception as e:
            print(f"ERROR reading {json_path}: {e}")
            continue

        # Extract place names from Dart block
        # Look for placeNames: ["A", "B"]
        place_names_code = re.findall(r'placeNames:\s*\[(.*?)\]', city_block, re.DOTALL)
        
        referenced_places = []
        for p_code in place_names_code:
            # Extract strings
            literals = re.findall(r'"(.*?)"', p_code)
            referenced_places.extend(literals)
            
        missing = []
        for place in referenced_places:
            norm_place = normalize(place)
            if norm_place not in available_places:
                # Check for fuzzy match
                matches = difflib.get_close_matches(norm_place, available_places.keys(), n=1, cutoff=0.8)
                suggestion = available_places[matches[0]] if matches else None
                missing.append({'name': place, 'suggestion': suggestion})
        
        if missing:
            report[json_filename] = missing

    # Print Report
    if not report:
        print("ALL CLEAR! No missing places found.")
    else:
        print(f"FOUND ISSUES IN {len(report)} CITIES:\n")
        for city_file, misses in report.items():
            print(f"=== {city_file} ===")
            for m in misses:
                msg = f"  - MISSING: '{m['name']}'"
                if m['suggestion']:
                    msg += f" (Did you mean: '{m['suggestion']}'?)"
                print(msg)
            print("")

if __name__ == "__main__":
    validate()

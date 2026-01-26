import re
import json
import os
import difflib

# Mapping special city function names to json filenames
CITY_MAPPING = {
    'NewYork': 'newyork.json',
    'HongKong': 'hongkong.json',
    'SanSebastian': 'san_sebastian.json',
}

def get_json_filename(city_func_name):
    if city_func_name in CITY_MAPPING:
        return CITY_MAPPING[city_func_name]
    return f"{city_func_name.lower()}.json"

def normalize(text):
    if not text: return ""
    return text.lower().strip().replace("'", "").replace("’", "")

def fix_json_files():
    dart_path = 'lib/services/curated_routes_service.dart'
    json_dir = 'assets/cities'
    
    with open(dart_path, 'r', encoding='utf-8') as f:
        dart_content = f.read()

    # Find all city blocks
    city_pattern = re.compile(r'static List<CuratedRoute> _get(\w+)Routes\(bool isEnglish\) \{(.*?)\}', re.DOTALL)
    
    fixed_count = 0
    
    for city_match in city_pattern.finditer(dart_content):
        city_func_name = city_match.group(1)
        city_block = city_match.group(2)
        
        json_filename = get_json_filename(city_func_name)
        json_path = os.path.join(json_dir, json_filename)
        
        if not os.path.exists(json_path):
            continue
            
        with open(json_path, 'r', encoding='utf-8') as jf:
            city_data = json.load(jf)
            highlights = city_data.get('highlights', [])
        
        # Build map of available names
        available_names_map = {} # norm_name -> highlight_obj
        for h in highlights:
            if 'name' in h: available_names_map[normalize(h['name'])] = h
            if 'name_en' in h: available_names_map[normalize(h['name_en'])] = h
            
        # Extract place names from Dart block
        place_names_code = re.findall(r'placeNames:\s*\[(.*?)\]', city_block, re.DOTALL)
        referenced_places = []
        for p_code in place_names_code:
            literals = re.findall(r'"(.*?)"', p_code)
            referenced_places.extend(literals)
            
        modified = False
        
        for place in referenced_places:
            norm_place = normalize(place)
            
            # If already exists, skip
            if norm_place in available_names_map:
                continue
                
            # Try to find a match to fix
            # 1. Containment (e.g. "Kapellbrücke" in "Chapel Bridge (Kapellbrücke)")
            match_obj = None
            
            # Check if dart name is in json name
            for name_key, h_obj in available_names_map.items():
                if norm_place in name_key or name_key in norm_place:
                    match_obj = h_obj
                    break
            
            # 2. Fuzzy match
            if not match_obj:
                matches = difflib.get_close_matches(norm_place, available_names_map.keys(), n=1, cutoff=0.7)
                if matches:
                    match_obj = available_names_map[matches[0]]
            
            if match_obj:
                # We found a match in JSON, but the exact name was missing.
                # So we add 'name_en' = place (from Dart) to bridge the gap.
                # Only if name_en is not already set (or we overwrite it?)
                # To be safe, let's ONLY add if name_en is missing.
                # OR if name_en exists but is different, maybe we append or ignore?
                # User complaint was "Names don't match". 
                # If I set name_en to what Code expects, Code will find it.
                
                if 'name_en' not in match_obj:
                    match_obj['name_en'] = place
                    print(f"[{json_filename}] Added name_en: '{place}' to '{match_obj['name']}'")
                    modified = True
                    fixed_count += 1
                elif match_obj['name_en'] != place:
                    # If it exists but different, maybe just leave it? 
                    # But code expects 'place'. 
                    # Let's trust the code is "English" mode content.
                    pass 

        if modified:
            with open(json_path, 'w', encoding='utf-8') as jf:
                json.dump(city_data, jf, indent=2, ensure_ascii=False)

    print(f"Total fixes applied: {fixed_count}")

if __name__ == "__main__":
    fix_json_files()

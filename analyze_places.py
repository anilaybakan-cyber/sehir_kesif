import re
import json
import os

# Map Dart content variables to JSON filenames
# Based on common sense and file list.
CITY_MAPPING = {
    'amsterdam': 'amsterdam.json',
    'barcelona': 'barcelona.json',
    'berlin': 'berlin.json',
    'bologna': 'bologna.json',
    'londra': 'londra.json',
    'newyork': 'newyork.json',
    'nice': 'nice.json',
    'paris': 'paris.json',
    'prag': 'prag.json',
    'roma': 'roma.json',
    'milano': 'milano.json',
    'cenevre': 'cenevre.json'
}

DART_FILE = 'lib/services/city_blog_content.dart'
ASSETS_DIR = 'assets/cities'

def extract_blog_places():
    with open(DART_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    extracted_places = {}

    for city_key, json_file in CITY_MAPPING.items():
        # Find the TR block for this city
        # Pattern: static const _cityTR = '''...''';
        # We need to be careful about variable names.
        # e.g. _londraTR, _newyorkTR (might be _newYorkTR?), _cenevreTR
        
        # Construct expected variable name
        if city_key == 'newyork':
            var_name = '_newyorkTR'
        else:
            var_name = f'_{city_key}TR'

        pattern_block = r"static const " + var_name + r" = '''(.*?)''';"
        match = re.search(pattern_block, content, flags=re.DOTALL)
        
        if not match:
            print(f"Warning: Could not find block for {var_name}")
            continue

        block_content = match.group(1)
        
        # Find "Şehrin Hafızası" or "İkonik Duraklar" sections
        # Usually H2: ## 🏛️ Şehrin Hafızası: Görülmesi Gereken İkonik Duraklar
        
        section_match = re.search(r'## 🏛️.*?\n(.*?)(##|$)', block_content, flags=re.DOTALL)
        if not section_match:
            print(f"Warning: Could not find Iconic Stops section in {var_name}")
            continue
            
        section_text = section_match.group(1)
        
        # Extract bullet points: - **Place Name**: Description
        # Regex to capture the bold part
        bullet_matches = re.finditer(r'-\s*\*\*(.*?)\*\*.*?:', section_text)
        
        places = []
        for bm in bullet_matches:
            raw_name = bm.group(1).strip()
            # Clean up: "Kolezyum ve Roma Forumu (İmparatorluğun Kalbi)" -> "Kolezyum", "Roma Forumu"
            # It's better to just keep the raw bold text for analysis first, 
            # but we likely want to split by ' ve ' if it looks like two places, 
            # and remove parentheses.
            
            clean_name = re.sub(r'\(.*?\)', '', raw_name).strip() # Remove parens
            
            # Simple split by ' ve ' might be dangerous but let's try
            if ' ve ' in clean_name:
                parts = clean_name.split(' ve ')
                places.extend([p.strip() for p in parts])
            else:
                places.append(clean_name)
                
        extracted_places[city_key] = places
        
    return extracted_places

def load_json_places(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        return []
        
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        places = []
        if 'highlights' in data:
            for h in data['highlights']:
                places.append({
                    'name': h.get('name', ''),
                    'nameEn': h.get('nameEn', ''),
                    'category': h.get('category', '')
                })
        return places
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

def main():
    blog_places_map = extract_blog_places()
    
    report = {}
    
    for city_key, target_places in blog_places_map.items():
        json_file = CITY_MAPPING[city_key]
        existing_json_places = load_json_places(json_file)
        
        # Normalize for comparison
        json_names = []
        for p in existing_json_places:
            json_names.append(p['name'].lower())
            if p['nameEn']:
                json_names.append(p['nameEn'].lower())
        
        found = []
        missing = []
        
        for place in target_places:
            # Check if this place exists in JSON (fuzzy match or exact)
            search_term = place.lower()
            
            # Direct check
            is_found = False
            for jn in json_names:
                if search_term == jn or search_term in jn or jn in search_term:
                    is_found = True
                    break
            
            if is_found:
                found.append(place)
            else:
                missing.append(place)
                
        report[city_key] = {
            'found': found,
            'missing': missing,
            'json_count': len(existing_json_places)
        }
        
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

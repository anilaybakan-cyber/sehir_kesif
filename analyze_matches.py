import json
import difflib
import os

def normalize(s):
    return s.lower().strip()

def main():
    with open('blog_places_analysis.json', 'r') as f:
        blog_data = json.load(f)

    # Load JSON names mapping
    # Assuming current_json_names.txt format: "  Name | NameEn"
    json_places_map = {}
    
    current_city = None
    with open('current_json_names.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('---'):
                current_city = line.replace('---', '').strip().lower()
                json_places_map[current_city] = []
            elif '|' in line and current_city:
                parts = line.split('|')
                name = parts[0].strip()
                name_en = parts[1].strip()
                json_places_map[current_city].append({
                    'name': name,
                    'nameEn': name_en,
                    'search_key': name # Default to TR name for search, or EN if TR is empty
                })
    
    final_mapping = {}
    
    for city, data in blog_data.items():
        all_blog_places = data['found'] + data['missing']
        city_json_places = json_places_map.get(city, [])
        
        city_mapping = {}
        
        for blog_place in all_blog_places:
            best_match = None
            highest_ratio = 0.0
            
            # Special manual overrides or checks
            bp_norm = normalize(blog_place)
            
            for jp in city_json_places:
                jp_name = jp['name']
                jp_name_en = jp['nameEn']
                
                # Check match with TR name
                ratio_tr = difflib.SequenceMatcher(None, bp_norm, normalize(jp_name)).ratio()
                # Check match with EN name
                ratio_en = difflib.SequenceMatcher(None, bp_norm, normalize(jp_name_en)).ratio()
                
                max_ratio = max(ratio_tr, ratio_en)
                
                if max_ratio > highest_ratio:
                    highest_ratio = max_ratio
                    # If match with EN is better, maybe use EN? 
                    # But the search function searches all fields.
                    # We just need ONE valid name to put in [Name](search:ValidName)
                    best_match = jp['name'] 

            # Threshold for "Good Match"
            if highest_ratio > 0.6: # 60% similarity
                city_mapping[blog_place] = best_match
            else:
                city_mapping[blog_place] = None # Truly missing
                
        final_mapping[city] = city_mapping
        
    print(json.dumps(final_mapping, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

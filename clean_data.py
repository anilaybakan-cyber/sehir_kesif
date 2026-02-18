import json
import os
import re

cities_dir = 'assets/cities'

def clean_city_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'highlights' not in data:
        return
    
    original_count = len(data['highlights'])
    cleaned_highlights = []
    
    # Patterns for fake names: "City Gem X", "Berlin Highlight Y", "Place Z", "Point A"
    fake_name_patterns = [
        re.compile(r'.* Gem \d+', re.IGNORECASE),
        re.compile(r'.* Highlight \d+', re.IGNORECASE),
        re.compile(r'.* Place \d+', re.IGNORECASE),
        re.compile(r'.* Point \d+', re.IGNORECASE),
    ]
    
    for h in data['highlights']:
        name = h.get('name', '')
        desc = h.get('description', '')
        
        is_fake_name = any(pattern.match(name) for pattern in fake_name_patterns)
        
        # Condition to remove: Very generic description seen in Paris/Berlin/etc
        is_generic = "gizli kalmış, yerel halk tarafından sevilen" in desc
        
        # Condition to remove: "X. önerisi!" format
        is_numbered = ". önerisi!" in desc
        
        # Condition to remove: repetitive "Eşsiz özellikleri ve sunduğu deneyimle" from Sevilla/Berlin/etc
        # ONLY if accompanied by a generic-ish name or if it's very short. 
        # Actually, let's stick to the names for now to avoid false positives.
        
        if not (is_fake_name or is_generic or is_numbered):
            cleaned_highlights.append(h)
            
    if len(cleaned_highlights) < original_count:
        data['highlights'] = cleaned_highlights
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Cleaned {filepath}: {original_count} -> {len(cleaned_highlights)}")

for filename in os.listdir(cities_dir):
    if filename.endswith('.json'):
        clean_city_file(os.path.join(cities_dir, filename))

import json
import os
import re

CITIES_DIR = 'assets/cities'
PATTERN = re.compile(r'Spot \d+', re.IGNORECASE)

def sanitize_file(filename):
    path = os.path.join(CITIES_DIR, filename)
    if not os.path.exists(path): return False
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    venues = data.get('highlights', []) if isinstance(data, dict) else data
    original_count = len(venues)
    
    # Filter out venues matching "Spot [NUMBER]"
    cleaned_venues = [
        h for h in venues 
        if isinstance(h, dict) and not (PATTERN.search(h.get('name', '')) or PATTERN.search(h.get('id', '')))
    ]
    
    new_count = len(cleaned_venues)
    if original_count != new_count:
        if isinstance(data, dict):
            data['highlights'] = cleaned_venues
        else:
            data = cleaned_venues
            
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"🧹 {filename}: {original_count} -> {new_count} venues (Removed {original_count - new_count} fake cards)")
        return True
    return False

def main():
    cleaned_any = False
    for f in os.listdir(CITIES_DIR):
        if f.endswith('.json') and not f.endswith('.bak'):
            if sanitize_file(f):
                cleaned_any = True
    if not cleaned_any:
        print("✨ No fake cards found in any city file.")

if __name__ == "__main__":
    main()

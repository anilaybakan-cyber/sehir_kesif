import json
import os
import re

# Directory containing city JSON files
CITIES_DIR = "../assets/cities"

# Localization mappings (Regex -> Replacement)
# Using regex to capture dynamic parts like "Sintra (Günübirlik)" -> "Sintra (Day Trip)"
MAPPINGS = [
    (r"(.*) \(Günübirlik\)", r"\1 (Day Trip)"),
    (r"^Günübirlik$", "Day Trip"),
    (r"Yahudi Mahallesi", "Jewish Quarter"),
    (r"Mellah \(Yahudi Mahallesi\)", "Mellah (Jewish Quarter)"),
    (r"Eski Şehir", "Old Town"),
    (r"Merkez", "Center"),
    (r"İstasyon", "Station"),
    (r"Istasyon", "Station"),
    (r"Liman", "Harbor"),
    (r"Meydan", "Square"),
    (r"Tepe", "Hill"),
    (r"Sahil", "Coast"),
    (r"Kordon", "Promenade"),
]

def enrich_city_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        city_name = data.get("city", "Unknown")
        highlights = data.get("highlights", [])
        modified_count = 0
        
        for place in highlights:
            # We only touch if 'area' exists
            if "area" not in place:
                continue
                
            original_area = place["area"]
            
            # If area_en already exists and is not empty, skip (or maybe we should force update? Let's skip for safety unless it matches original area which implies it wasn't localized)
            # Actually, let's overwrite if we match our specific patterns, because user explicitly wants to fix these.
            
            new_area_en = original_area # Start with original
            matched = False
            
            for pattern, replacement in MAPPINGS:
                if re.search(pattern, new_area_en):
                    new_area_en = re.sub(pattern, replacement, new_area_en)
                    matched = True
            
            # If we made a change
            if matched and new_area_en != original_area:
                # Check if we should update/add area_en
                # If area_en doesn't exist, or if it equals the Turkish area (meaning it wasn't really translated), update it.
                current_area_en = place.get("area_en", "")
                
                if not current_area_en or current_area_en == original_area:
                    place["area_en"] = new_area_en
                    modified_count += 1
                    # print(f"[{city_name}] '{original_area}' -> '{new_area_en}' (in {place['name']})")

        if modified_count > 0:
            print(f"Updated {modified_count} places in {city_name} ({os.path.basename(filepath)})")
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            pass
            # print(f"No changes for {city_name}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cities_path = os.path.join(script_dir, CITIES_DIR)
    
    if not os.path.exists(cities_path):
        print(f"Directory not found: {cities_path}")
        return

    files = [f for f in os.listdir(cities_path) if f.endswith('.json')]
    print(f"Found {len(files)} city files.")
    
    for filename in files:
        enrich_city_json(os.path.join(cities_path, filename))

if __name__ == "__main__":
    main()

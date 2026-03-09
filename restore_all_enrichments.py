import json
import csv
import os
from pathlib import Path

GENERIC_TEMPLATES = [
    "popüler kafelerinden biri",
    "puan ile ödüllendirilen",
    "Akşam saatlerinde canlanan",
    "Aksiyon ve eğlence dolu bir gün",
    "güneşin ve denizin tadını çıkarmak",
    "One of the popular spots in",
    "Rated"
]

def is_generic(text):
    if not text:
        return True
    for template in GENERIC_TEMPLATES:
        if template.lower() in text.lower():
            return True
    return False

def format_city_key(city_name):
    """Normalize city name to match JSON filenames (lowercase, no spaces, standard english chars ideally, but we'll just lowercase and strip).
    Actually, JSON filenames are like 'barcelona.json', 'prag.json', 'amsterdam.json'.
    We need a robust mapping or just clean the name."""
    clean_name = city_name.lower().strip()
    return clean_name

def load_csv_data_all_cities(filepath):
    data = {} # { "city_name": { "place_name": { "tr": desc, "en": desc } } }
    if not os.path.exists(filepath):
        return data
        
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None) # skip header
        for row in reader:
            if len(row) >= 5:
                # Determine format based on structure
                # all_places_report_final.csv: Şehir;Yer Adı;Kategori;Açıklama (TR);Description (EN);Rating
                # all_places_report2.csv: 1: Yapılacak şey;Şehir;Yer Adı;Açıklama (TR);Description (EN);Rating
                
                # Check column 0 to see if it looks like an instruction ("İngilizceden çevirsin", "Türkçe'den çevirsin")
                if "çevir" in row[0].lower() or "araştırma yap" in row[0].lower() or "yapılacak" in row[0].lower():
                    # Format: all_places_report2.csv
                    city_raw = row[1].strip()
                    name = row[2].strip()
                    desc_tr = row[3].strip()
                    desc_en = row[4].strip()
                else:
                    # Format: all_places_report_final.csv
                    city_raw = row[0].strip()
                    name = row[1].strip()
                    desc_tr = row[3].strip()
                    desc_en = row[4].strip()
                
                if not city_raw or not name:
                    continue
                    
                city_key = format_city_key(city_raw)
                
                if not is_generic(desc_tr):
                    if city_key not in data:
                        data[city_key] = {}
                        
                    data[city_key][name.lower()] = {
                        "tr": desc_tr,
                        "en": desc_en if not is_generic(desc_en) else desc_tr
                    }
    return data

def get_json_city_key(filename):
    """Extracts base city name from filename, e.g., 'barcelona.json' -> 'barcelona'
    Some CSVs might have 'Barselona', JSON might have 'barcelona'. We'll handle basic mappings if needed."""
    base = filename.replace('.json', '')
    return base

CITY_MAPPINGS = {
    # CSV name (lowered) -> JSON filename base
    "barselona": "barcelona",
    "floransa": "florence", # or floransa depending on json
    "roma": "rome",
    "prag": "prague", # wait, earlier we saw prag.json
    "viyana": "vienna",
    "paris": "paris",
    "londra": "london",
    "amsterdam": "amsterdam",
    "new york": "newyork",
    "newyork": "newyork",
    "berlin": "berlin",
    "buda": "budapest",
    "budapeşte": "budapeste",
    "bruksel": "brussels", # wait, earlier we saw bruksel.json
}

def update_city_files(target_dir, enrichments_by_city):
    updated_files = 0
    total_places_updated = 0
    
    target_path = Path(target_dir)
    for json_file in target_path.glob("*.json"):
        json_city_key = json_file.stem.lower() # e.g., 'barcelona'
        
        # Gather all matching enrichments for this JSON file
        city_enrichments = {}
        
        # Check direct match
        if json_city_key in enrichments_by_city:
            city_enrichments.update(enrichments_by_city[json_city_key])
            
        # Check reverse mapping
        for csv_city, mapped_json in CITY_MAPPINGS.items():
            if mapped_json == json_city_key and csv_city in enrichments_by_city:
                city_enrichments.update(enrichments_by_city[csv_city])
                
        # Also check standard mappings (e.g. if csv has 'prague' but json is 'prag.json')
        # We'll just do a loose check. If the json filename translates to csv name
        for csv_city in enrichments_by_city.keys():
            # If they are very similar
            if csv_city == json_city_key or json_city_key in csv_city or csv_city in json_city_key:
                 # Don't overwrite if we already have exact matches, just merge cautiously
                 for k,v in enrichments_by_city[csv_city].items():
                     if k not in city_enrichments:
                         city_enrichments[k] = v
                         
        if not city_enrichments:
            continue
            
        # We have enrichments for this city. Let's try to apply them.
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                city_data = json.load(f)
        except Exception as e:
            continue
            
        file_updated = False
        places_updated = 0
        
        for place in city_data.get("highlights", []):
            name_lower = place.get("name", "").lower()
            if name_lower in city_enrichments:
                new_desc = city_enrichments[name_lower]["tr"]
                new_desc_en = city_enrichments[name_lower]["en"]
                
                current_tr = place.get("description", "")
                
                if current_tr != new_desc:
                    place["description"] = new_desc
                    place["description_en"] = new_desc_en
                    file_updated = True
                    places_updated += 1
                    
        if file_updated:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(city_data, f, ensure_ascii=False, indent=2)
            updated_files += 1
            total_places_updated += places_updated
            print(f"  [+] Updated {places_updated} places in {json_file.name}")
            
    return updated_files, total_places_updated


def main():
    print("Loading valid advanced descriptions for all cities from CSVs...")
    enrichments_by_city = {} # { city: { place: { tr, en } } }
    
    # Load from report2 (might have user's manual annotations)
    report2_data = load_csv_data_all_cities("all_places_report2.csv")
    for city, places in report2_data.items():
        if city not in enrichments_by_city:
            enrichments_by_city[city] = {}
        enrichments_by_city[city].update(places)
    
    # Load from final report
    final_report_data = load_csv_data_all_cities("all_places_report_final.csv")
    for city, places in final_report_data.items():
        if city not in enrichments_by_city:
            enrichments_by_city[city] = {}
        enrichments_by_city[city].update(places)
    
    total_advanced = sum(len(places) for places in enrichments_by_city.values())
    print(f"Found {total_advanced} advanced descriptions across {len(enrichments_by_city)} cities in CSVs.")
    
    # Apply to JSON
    print("\nApplying to assets/cities...")
    assets_files, assets_places = update_city_files("assets/cities", enrichments_by_city)
    
    print("\nApplying to ota_data_pack/cities...")
    ota_files, ota_places = update_city_files("ota_data_pack/cities", enrichments_by_city)
    
    print(f"\nSummary:")
    print(f"Updated {assets_files} files and {assets_places} places in assets/cities")
    print(f"Updated {ota_files} files and {ota_places} places in ota_data_pack/cities")

if __name__ == '__main__':
    main()

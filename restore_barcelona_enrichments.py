import json
import csv
import os

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

def load_csv_data(filepath, city_filter="barcelona"):
    data = {}
    if not os.path.exists(filepath):
        return data
        
    with open(filepath, 'r', encoding='utf-8') as f:
        # Assuming delimiter is ';' based on previous file views
        reader = csv.reader(f, delimiter=';')
        next(reader, None) # skip header
        for row in reader:
            if len(row) >= 5:
                # all_places_report2.csv: 1: Yapılacak şey;Şehir;Yer Adı;Açıklama (TR);Description (EN);Rating
                # all_places_report_final.csv: Şehir;Yer Adı;Kategori;Açıklama (TR);Description (EN);Rating
                # Let's detect which format it is based on row[1] vs row[0]
                if row[0].lower() == city_filter.lower():
                    # all_places_report_final.csv
                    city = row[0].strip()
                    name = row[1].strip()
                    desc_tr = row[3].strip()
                    desc_en = row[4].strip()
                elif row[1].lower() == city_filter.lower():
                    # all_places_report2.csv
                    city = row[1].strip()
                    name = row[2].strip()
                    desc_tr = row[3].strip()
                    desc_en = row[4].strip()
                else:
                    continue
                    
                
                if not is_generic(desc_tr):
                    data[name.lower()] = {
                        "tr": desc_tr,
                        "en": desc_en if not is_generic(desc_en) else desc_tr # Fallback to TR if EN is generic
                    }
    return data

def main():
    print("Loading valid advanced descriptions from CSVs...")
    enrichments = {}
    
    # Load from report2 (might have user's manual annotations)
    report2_data = load_csv_data("all_places_report2.csv", "barcelona")
    enrichments.update(report2_data)
    
    # Load from final report (might have even more refined ones)
    final_report_data = load_csv_data("all_places_report_final.csv", "barcelona")
    enrichments.update(final_report_data)
    
    print(f"Found {len(enrichments)} advanced descriptions for Barcelona.")
    
    # Apply to JSON
    json_paths = [
        "assets/cities/barcelona.json",
        "ota_data_pack/cities/barcelona.json"
    ]
    
    for path in json_paths:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            city_data = json.load(f)
            
        updated_count = 0
        for place in city_data.get("highlights", []):
            name_lower = place.get("name", "").lower()
            if name_lower in enrichments:
                new_desc = enrichments[name_lower]["tr"]
                new_desc_en = enrichments[name_lower]["en"]
                
                # Check if current JSON has the generic template
                current_tr = place.get("description", "")
                
                if current_tr != new_desc:
                    place["description"] = new_desc
                    place["description_en"] = new_desc_en
                    updated_count += 1
                    print(f"  [+] Updated: {place['name']}")
                    
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, ensure_ascii=False, indent=2)
            
        print(f"Applied {updated_count} advanced descriptions to {path}.")
        
if __name__ == '__main__':
    main()

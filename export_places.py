
import json
import csv
import os
import glob

# Mapping for categories from Turkish to English
CATEGORY_MAP = {
    "Müze": "Museum",
    "Park": "Park",
    "Restoran": "Restaurant",
    "Cafe": "Cafe",
    "Kafe": "Cafe",
    "Deneyim": "Experience",
    "Tarihi": "Historical",
    "Bar": "Bar",
    "Manzara": "Viewpoint",
    "Manzaralı": "Viewpoint",
    "Alışveriş": "Shopping",
    "Eğlence": "Entertainment",
    "Sanat": "Art",
    "Pazar": "Market",
    "Dini": "Religious",
    "Meydan": "Square",
    "Plaj": "Beach",
    "Doğa": "Nature",
    "Mimari": "Architecture",
    "Sokak Lezzeti": "Street Food",
    "Tatlı": "Dessert",
    "Yeme & İçme": "Food & Drink",
    "Görülmesi Gereken Yerler": "Must See Places"
}

def get_category_en(cat_tr):
    if not cat_tr:
        return ""
    # Try direct match
    if cat_tr in CATEGORY_MAP:
        return CATEGORY_MAP[cat_tr]
    # Try case insensitive
    for k, v in CATEGORY_MAP.items():
        if k.lower() == cat_tr.lower():
            return v
    # Default to TR if no match found
    return cat_tr

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    output_file = "/Users/anilebru/Desktop/application_places_export.csv"
    
    headers = [
        "City", 
        "Title (TR)", "Title (EN)", 
        "Description (TR)", "Description (EN)", 
        "Category (TR)", "Category (EN)", 
        "Location (Lat, Lng)"
    ]
    
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    print(f"Found {len(json_files)} city files.")
    
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for file_path in json_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                city_name = data.get('city', 'Unknown')
                highlights = data.get('highlights', [])
                
                print(f"Processing {city_name} - {len(highlights)} places")
                
                for place in highlights:
                    title_tr = place.get('name', '')
                    title_en = place.get('name_en', '')
                    
                    desc_tr = place.get('description', '')
                    desc_en = place.get('description_en', '')
                    
                    cat_tr = place.get('category', '')
                    cat_en = get_category_en(cat_tr)
                    
                    lat = place.get('lat', '')
                    lng = place.get('lng', '')
                    location = f"{lat}, {lng}" if lat and lng else ""
                    
                    writer.writerow([
                        city_name,
                        title_tr,
                        title_en,
                        desc_tr,
                        desc_en,
                        cat_tr,
                        cat_en,
                        location
                    ])
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    print(f"Export completed: {output_file}")

if __name__ == "__main__":
    main()


import os
import json
import csv
import glob

# Configuration
CITIES_DIR = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
OUTPUT_FILE = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/City_Content_Language_Comparison.csv'

# Translation Map from AppLocalizations.dart
CATEGORY_TRANSLATIONS = {
      'Tümü': 'All',
      'Restoran': 'Restaurant',
      'Kafe': 'Cafe',
      'Bar': 'Bar',
      'Müze': 'Museum',
      'Park': 'Park',
      'Tarihi': 'Historical',
      'Manzara': 'Viewpoint',
      'Deneyim': 'Experience',
      'Alışveriş': 'Shopping',
      'Mahalle': 'Neighborhood',
      'Semt': 'District',
      'Sakin': 'Calm',
      'Keşif': 'Discover',
      'Popüler': 'Popular',
      'Meydan': 'Square',
      'Fotoğraf': 'Photography',
      'Mimari': 'Architecture',
      'Spor': 'Sports',
      'Doğa': 'Nature',
      'Sanat': 'Art',
      'Gece Hayatı': 'Nightlife',
      'Yemek': 'Food',
      'Plaj': 'Beach',
      'Mistik': 'Mystic',
      'Yürüyüş': 'Walking',
      'Yeme-İçme': 'Food & Drink',
      'Gastronomi': 'Gastronomy',
      'Sokak Yemeği': 'Street Food',
      'Balık': 'Seafood',
      'Tatlı': 'Dessert',
      'Kokteyl Bar': 'Cocktail Bar',
      'Rooftop': 'Rooftop',
      'Kahve': 'Coffee',
      'Tapas': 'Tapas',
      # Common variations found in data
      'Cafe': 'Cafe',
      'Muzeler': 'Museums',
}

def get_displayed_text(primary, secondary, is_english_mode):
    """
    Simulates app logic: if English mode, prefer secondary (EN) if exists, else fallback to primary (TR).
    If Turkish mode, use primary.
    """
    if is_english_mode:
        if secondary and str(secondary).strip():
            return str(secondary).strip()
        return str(primary).strip() # Fallback
    else:
        return str(primary).strip()

def get_displayed_category(category_tr, is_english_mode):
    cat = str(category_tr).strip()
    
    # 1. NORMALIZE (Match AppLocalizations logic)
    corrections = {
        'Görülmesi Gereken Yerler': 'Deneyim',
        'Akvaryum': 'Deneyim',
        'Atıştırmalık': 'Yeme-İçme',
        'Atölye': 'Deneyim',
        'Eğitim': 'Tarihi',
        'Heyke': 'Tarihi',
        'Heykel': 'Tarihi',
        'Mağaza': 'Alışveriş',
        'Merkez': 'Deneyim',
        'Mimar': 'Tarihi',
        'Modern': 'Deneyim',
        'Neighborhood': 'Deneyim', 
        'Mahalle': 'Deneyim',
        'Pasaj': 'Deneyim',
        'Pazar': 'Deneyim',
        'Rahatlama': 'Deneyim',
        'Şarap': 'Yeme-İçme',
        'Saray': 'Tarihi',
        'Şehir': 'Deneyim',
        'Sokak': 'Deneyim',
        'Tarih': 'Tarihi',
    }
    
    if cat in corrections:
        cat = corrections[cat]
        
    # If Turkish mode, return normalized Turkish
    if not is_english_mode:
        return cat

    # If English mode, return translation
    return CATEGORY_TRANSLATIONS.get(cat, cat)

def main():
    print(f"Scanning directory: {CITIES_DIR}")
    json_files = glob.glob(os.path.join(CITIES_DIR, '*.json'))
    
    headers = [
        'CITY',
        'PLACE ID (Original Name)',
        
        '--- ENGLISH MODE: NAME ---',
        '--- ENGLISH MODE: CATEGORY ---',
        '--- ENGLISH MODE: DESCRIPTION ---',
        '--- ENGLISH MODE: TIPS ---',
        
        '--- TURKISH MODE: NAME ---',
        '--- TURKISH MODE: CATEGORY ---',
        '--- TURKISH MODE: DESCRIPTION ---',
        '--- TURKISH MODE: TIPS ---',
        
        'HAS EN DESCRIPTION?', # Helper check
        'IMAGE URL'
    ]

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        count = 0
        
        for file_path in sorted(json_files):
            if file_path.endswith('.tmp') or file_path.endswith('.DS_Store'):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                city_name = data.get('city', 'Unknown')
                highlights = data.get('highlights', [])
                
                print(f"Processing {city_name}...")
                
                for place in highlights:
                    count += 1
                    
                    # Raw Values
                    raw_name = place.get('name', '')
                    raw_name_en = place.get('name_en', '')
                    raw_cat = place.get('category', '')
                    raw_desc = place.get('description', '')
                    raw_desc_en = place.get('description_en', '')
                    raw_tips = place.get('tips', '')
                    raw_tips_en = place.get('tips_en', '')
                    
                    # ENGLISH MODE DISPLAY
                    disp_name_en = get_displayed_text(raw_name, raw_name_en, True)
                    disp_cat_en = get_displayed_category(raw_cat, True)
                    disp_desc_en = get_displayed_text(raw_desc, raw_desc_en, True)
                    # Tips logic: usually explicit check. If en missing, might show empty or fallback depending on UI impl.
                    # Based on standard fallback patterns:
                    disp_tips_en = get_displayed_text(raw_tips, raw_tips_en, True)

                    # TURKISH MODE DISPLAY
                    disp_name_tr = raw_name
                    disp_cat_tr = raw_cat
                    disp_desc_tr = raw_desc
                    disp_tips_tr = raw_tips
                    
                    has_en = 'YES' if (raw_desc_en and str(raw_desc_en).strip()) else 'NO (Fallback)'
                    
                    writer.writerow([
                        city_name,
                        raw_name,
                        
                        disp_name_en,
                        disp_cat_en,
                        disp_desc_en,
                        disp_tips_en,
                        
                        disp_name_tr,
                        disp_cat_tr,
                        disp_desc_tr,
                        disp_tips_tr,
                        
                        has_en,
                        place.get('imageUrl', '')
                    ])
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    print(f"\n✅ Export completed: {OUTPUT_FILE}")
    print(f"Total places: {count}")

if __name__ == "__main__":
    main()

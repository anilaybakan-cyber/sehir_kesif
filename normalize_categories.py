
import os
import json
import glob

# Configuration
CITIES_DIR = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'

# Corrections Map (Same as in AppLocalizations)
CORRECTIONS = {
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
    'Mimari': 'Historical', # If encountered as raw Turkish category
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
    'Must See': 'Deneyim', # Catch English pollution in TR field if any
}

def normalize_city_files():
    print(f"Scanning directory: {CITIES_DIR}")
    json_files = glob.glob(os.path.join(CITIES_DIR, '*.json'))
    
    total_corrections = 0
    files_changed = 0

    for file_path in sorted(json_files):
        if file_path.endswith('.tmp') or file_path.endswith('.DS_Store'):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            
            modified = False
            
            for place in highlights:
                # Check Category
                raw_cat = place.get('category', '').strip()
                
                # Check for direct match or substring (e.g. for "Mimar" matching inside "Mimar Sinan") - strict match preferable for categories
                if raw_cat in CORRECTIONS:
                    new_cat = CORRECTIONS[raw_cat]
                    print(f"[{city_name}] Fixed Category: '{raw_cat}' -> '{new_cat}' ({place.get('name')})")
                    place['category'] = new_cat
                    modified = True
                    total_corrections += 1
                
                # Special check for "Mimari" if mapped differently or "Mimar" typo
                if raw_cat == 'Mimar': 
                     place['category'] = 'Tarihi'
                     modified = True
                     total_corrections += 1

            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                files_changed += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\n✅ Normalization Completed")
    print(f"Files Changed: {files_changed}")
    print(f"Total Corrections: {total_corrections}")

if __name__ == "__main__":
    normalize_city_files()

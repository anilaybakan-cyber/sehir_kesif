import pandas as pd
import json
import os
import shutil

EXCEL_FILE = "/Users/anilebru/Desktop/Tum_Sehirler_V4_Final_Kategorili.xlsx"
ASSETS_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
OTA_DIR = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/cities"

def main():
    print(f"Loading data from {EXCEL_FILE}...")
    df = pd.read_excel(EXCEL_FILE)
    
    updated_files = 0
    updated_places = 0
    
    for filename in os.listdir(ASSETS_DIR):
        if not filename.endswith('.json'):
            continue
            
        file_path = os.path.join(ASSETS_DIR, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
                continue
                
        city_name_tr = data.get('city', '')
        if not city_name_tr:
            continue
            
        city_df = df[df['Şehir'] == city_name_tr]
        if city_df.empty:
            continue
            
        places_updated_in_city = 0
        
        for place in data.get('highlights', []):
            place_name_tr = place.get('name', '')
            
            row = city_df[city_df['Yer Adı (TR)'] == place_name_tr]
            if not row.empty:
                r = row.iloc[0]
                
                desc_tr = str(r.get('Açıklama (TR)', ''))
                desc_en = str(r.get('Açıklama (EN)', ''))
                if desc_tr and desc_tr != 'nan':
                    place['description'] = desc_tr
                if desc_en and desc_en != 'nan':
                    place['description_en'] = desc_en
                    
                tip_tr = str(r.get('Yerel İpucu (TR)', ''))
                tip_en = str(r.get('Yerel İpucu (EN)', ''))
                
                if tip_tr and tip_tr != 'nan':
                    place['tips'] = tip_tr
                if tip_en and tip_en != 'nan':
                    place['tips_en'] = tip_en
                    
                cat = str(r.get('Kategori', ''))
                if cat and cat != 'nan':
                    place['category'] = cat
                    
                places_updated_in_city += 1
                updated_places += 1
                
        if places_updated_in_city > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            ota_path = os.path.join(OTA_DIR, filename)
            shutil.copy2(file_path, ota_path)
            
            updated_files += 1
            print(f"Updated {filename} ({places_updated_in_city} places mapped.)")
            
    print(f"\nDone! Updated {updated_places} places across {updated_files} cities.")

if __name__ == '__main__':
    main()

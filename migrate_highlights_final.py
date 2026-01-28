import pandas as pd
import json
import os

def normalize_name(name):
    if not name: return ""
    return str(name).strip().lower()

def clean_en_name(name):
    if not name: return ""
    n = str(name).strip()
    # Fix specific common issues in the provided Excel data
    n = n.replace("Müze Island", "Museum Island")
    n = n.replace("Müzi", "Museum") # in case of other typos
    n = n.replace("Antalya Müze", "Antalya Museum")
    n = n.replace("Güray Müze", "Güray Museum")
    return n

def main():
    file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    
    df = pd.read_excel(file_path, header=0)
    df.columns = ['City', 'Name_TR', 'Name_EN', 'Category', 'Description_TR', 'Description_EN', 'Tips_TR', 'Tips_EN', 'Lat', 'Lng']
    df = df.iloc[1:].reset_index(drop=True)
    
    grouped = df.groupby('City')
    
    for city_name, group in grouped:
        # Standardize city filename mapping
        c_low = str(city_name).lower().strip()
        filename = c_low.replace('i̇', 'i').replace('ş', 's').replace('ç', 'c').replace('ö', 'o').replace('ü', 'u').replace('ğ', 'g')
        
        # Override common differences
        if filename == 'stokholm': filename = 'stockholm'
        elif filename == 'london': filename = 'londra'
        elif filename == 'rome': filename = 'roma'
        elif filename == 'lisbon': filename = 'lizbon'
        
        json_path = os.path.join(assets_dir, f"{filename}.json")
        if not os.path.exists(json_path):
            # Try alternate
            if filename == 'stockholm': json_path = os.path.join(assets_dir, "stokholm.json")
            
        if not os.path.exists(json_path):
            print(f"⚠️ Not found: {json_path}")
            continue
            
        with open(json_path, 'r', encoding='utf-8') as f:
            city_data = json.load(f)
            
        highlights = city_data.get('highlights', [])
        update_count = 0
        
        for _, row in group.iterrows():
            target_tr = normalize_name(row['Name_TR'])
            target_en = normalize_name(row['Name_EN'])
            
            for h in highlights:
                h_tr = normalize_name(h.get('name', ''))
                h_en = normalize_name(h.get('name_en', ''))
                
                # Broad match
                if (target_tr and h_tr == target_tr) or (target_en and h_en == target_en):
                    # Force update all requested fields
                    h['name'] = str(row['Name_TR']) # Turkish Name
                    h['name_en'] = clean_en_name(row['Name_EN']) # English Name
                    h['category'] = str(row['Category'])
                    h['description'] = str(row['Description_TR'])
                    
                    if pd.notna(row['Description_EN']):
                        h['description_en'] = str(row['Description_EN'])
                    
                    if pd.notna(row['Tips_TR']):
                        h['tips'] = str(row['Tips_TR'])
                    if pd.notna(row['Tips_EN']):
                        h['tips_en'] = str(row['Tips_EN'])
                        
                    if pd.notna(row['Lat']): h['lat'] = float(row['Lat'])
                    if pd.notna(row['Lng']): h['lng'] = float(row['Lng'])
                    
                    update_count += 1
                    break
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, ensure_ascii=False, indent=2)
            
        print(f"Done: {city_name} ({update_count} updates)")

if __name__ == '__main__':
    main()

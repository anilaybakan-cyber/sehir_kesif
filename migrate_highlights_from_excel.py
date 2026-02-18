import pandas as pd
import json
import os
import re

def normalize_name(name):
    if not name: return ""
    return str(name).strip().lower()

def main():
    file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    
    # Read Excel, skipping the first decorative row if needed, but our inspect showed data starts at row 1
    df = pd.read_excel(file_path, header=0)
    
    # Rename columns for easier access based on inspection
    df.columns = ['City', 'Name_TR', 'Name_EN', 'Category', 'Description_TR', 'Description_EN', 'Tips_TR', 'Tips_EN', 'Lat', 'Lng']
    
    # Skip the first row which is just original headers text
    df = df.iloc[1:].reset_index(drop=True)
    
    # Group by city
    grouped = df.groupby('City')
    
    for city_name, group in grouped:
        normalized_city = str(city_name).lower().strip().replace('i̇', 'i').replace('ş', 's').replace('ç', 'c').replace('ö', 'o').replace('ü', 'u').replace('ğ', 'g')
        # Specific mappings if needed
        if normalized_city == 'kopenhag': normalized_city = 'kopenhag'
        if normalized_city == 'stockholm': normalized_city = 'stockholm' # although our asset might be stokholm.json sometimes
        
        json_path = os.path.join(assets_dir, f"{normalized_city}.json")
        
        # Fallback for common Turkish/English name differences in filenames
        if not os.path.exists(json_path):
            if normalized_city == 'stokholm': json_path = os.path.join(assets_dir, "stockholm.json")
            elif normalized_city == 'stockholm': json_path = os.path.join(assets_dir, "stokholm.json")
            elif normalized_city == 'london': json_path = os.path.join(assets_dir, "londra.json")
            elif normalized_city == 'rome': json_path = os.path.join(assets_dir, "roma.json")
            elif normalized_city == 'lisbon': json_path = os.path.join(assets_dir, "lizbon.json")
        
        if not os.path.exists(json_path):
            print(f"⚠️ City file not found: {json_path} (City in Excel: {city_name})")
            continue
            
        print(f"Processing {city_name} -> {json_path}")
        
        with open(json_path, 'r', encoding='utf-8') as f:
            city_data = json.load(f)
            
        highlights = city_data.get('highlights', [])
        update_count = 0
        
        for _, row in group.iterrows():
            target_name_tr = normalize_name(row['Name_TR'])
            target_name_en = normalize_name(row['Name_EN'])
            
            found = False
            for h in highlights:
                h_name_tr = normalize_name(h.get('name', ''))
                h_name_en = normalize_name(h.get('name_en', ''))
                
                # Match by TR or EN name
                if (target_name_tr and h_name_tr == target_name_tr) or (target_name_en and h_name_en == target_name_en):
                    # Update fields
                    h['category'] = str(row['Category'])
                    h['description'] = str(row['Description_TR'])
                    
                    # Update Name EN if missing or changed
                    raw_name_en = str(row['Name_EN'])
                    if "Müze Island" in raw_name_en: raw_name_en = raw_name_en.replace("Müze Island", "Museum Island")
                    h['name_en'] = raw_name_en

                    if 'Description_EN' in row and pd.notna(row['Description_EN']):
                        h['description_en'] = str(row['Description_EN'])
                    
                    if 'Tips_TR' in row and pd.notna(row['Tips_TR']):
                        h['tips'] = str(row['Tips_TR'])
                    if 'Tips_EN' in row and pd.notna(row['Tips_EN']):
                        h['tips_en'] = str(row['Tips_EN'])
                        
                    if pd.notna(row['Lat']): h['lat'] = float(row['Lat'])
                    if pd.notna(row['Lng']): h['lng'] = float(row['Lng'])
                    
                    found = True
                    update_count += 1
                    break
            
            if not found:
                # Optional: Add as new if it's very important, but for now we just update
                # print(f"  Highlight not found in JSON: {row['Name_TR']}")
                pass
        
        # Save back
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, ensure_ascii=False, indent=2)
            
        print(f"  Updated {update_count} highlights in {city_name}")

if __name__ == '__main__':
    main()

import pandas as pd
import json
import os

def normalize_name(name):
    if not name: return ""
    return str(name).strip().lower()

def clean_en_name(name, tr_name):
    if not name or pd.isna(name) or str(name).strip() == "":
        return tr_name # Fallback
    n = str(name).strip()
    n = n.replace("Müze Island", "Museum Island")
    n = n.replace("Holokost Anıtı", "Holocaust Memorial")
    if "Müze" in n and "Museum" not in n:
        n = n.replace("Müze", "Museum")
    return n

def main():
    file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    
    df = pd.read_excel(file_path, header=0)
    df.columns = ['City', 'Name_TR', 'Name_EN', 'Category', 'Description_TR', 'Description_EN', 'Tips_TR', 'Tips_EN', 'Lat', 'Lng']
    # Filter out the first decorative row
    df = df[df['City'] != 'City'].reset_index(drop=True)
    
    grouped = df.groupby('City')
    
    for city_name, group in grouped:
        c_low = str(city_name).lower().strip()
        filename = c_low.replace('i̇', 'i').replace('ş', 's').replace('ç', 'c').replace('ö', 'o').replace('ü', 'u').replace('ğ', 'g')
        filename = filename.replace(' ', '') # remove spaces for new york, hong kong
        
        # Mapping overrides
        if filename == 'stokholm': filename = 'stockholm'
        elif filename == 'london': filename = 'londra'
        elif filename == 'rome': filename = 'roma'
        elif filename == 'lisbon': filename = 'lizbon'
        elif filename == 'sansebastian': filename = 'san_sebastian'
        
        json_path = os.path.join(assets_dir, f"{filename}.json")
        if not os.path.exists(json_path):
            # Try some common alternates
            if filename == 'stockholm': json_path = os.path.join(assets_dir, "stokholm.json")
            elif filename == 'kopenhag': json_path = os.path.join(assets_dir, "copenhagen.json")
            
        if not os.path.exists(json_path):
            print(f"❌ Missing: {city_name} -> {json_path}")
            continue
            
        with open(json_path, 'r', encoding='utf-8') as f:
            city_data = json.load(f)
            
        highlights = city_data.get('highlights', [])
        update_count = 0
        
        # Create a mapping for faster lookup
        excel_data_map = {}
        for _, row in group.iterrows():
            tr_key = normalize_name(row['Name_TR'])
            en_key = normalize_name(row['Name_EN'])
            excel_data_map[tr_key] = row
            if en_key:
                excel_data_map[en_key] = row
        
        for h in highlights:
            h_tr = normalize_name(h.get('name', ''))
            h_en = normalize_name(h.get('name_en', ''))
            
            match_row = None
            if h_tr in excel_data_map: match_row = excel_data_map[h_tr]
            elif h_en in excel_data_map: match_row = excel_data_map[h_en]
            
            if match_row is not None:
                # UPDATE ALL FIELDS
                h['name'] = str(match_row['Name_TR'])
                h['name_en'] = clean_en_name(match_row['Name_EN'], match_row['Name_TR'])
                h['category'] = str(match_row['Category'])
                h['description'] = str(match_row['Description_TR'])
                
                if pd.notna(match_row['Description_EN']):
                    h['description_en'] = str(match_row['Description_EN'])
                
                if pd.notna(match_row['Tips_TR']):
                    h['tips'] = str(match_row['Tips_TR'])
                if pd.notna(match_row['Tips_EN']):
                    h['tips_en'] = str(match_row['Tips_EN'])
                    
                if pd.notna(match_row['Lat']): h['lat'] = float(match_row['Lat'])
                if pd.notna(match_row['Lng']): h['lng'] = float(match_row['Lng'])
                
                update_count += 1
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, ensure_ascii=False, indent=2)
            
        print(f"✅ {city_name}: {update_count} updates")

if __name__ == '__main__':
    main()

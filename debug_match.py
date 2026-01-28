import pandas as pd
import json
import os

def normalize_name(name):
    if not name: return ""
    return str(name).strip().lower()

def main():
    file_path = '/Users/anilebru/Downloads/gpt_excel_processed_v6.xlsx'
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    
    df = pd.read_excel(file_path, header=0)
    df.columns = ['City', 'Name_TR', 'Name_EN', 'Category', 'Description_TR', 'Description_EN', 'Tips_TR', 'Tips_EN', 'Lat', 'Lng']
    df = df.iloc[1:].reset_index(drop=True)
    
    # Debug Berlin Museum Island
    berlin_excel = df[df['City'].str.contains('Berlin', na=False)]
    excel_row = berlin_excel[berlin_excel['Name_TR'].str.contains('Müze Adası', na=False)]
    
    if excel_row.empty:
        print("Excel row NOT found")
    else:
        print("Excel row FOUND")
        target_name_tr = normalize_name(excel_row.iloc[0]['Name_TR'])
        print(f"Target TR: '{target_name_tr}'")

    with open(os.path.join(assets_dir, 'berlin.json'), 'r') as f:
        data = json.load(f)
    
    for h in data['highlights']:
        if "Müze Adası" in h.get('name', ''):
            h_name_tr = normalize_name(h['name'])
            print(f"JSON Name: '{h_name_tr}'")
            if h_name_tr == target_name_tr:
                print("MATCH!")
            else:
                print("NO MATCH!")
                print("Chars JSON:", [ord(c) for c in h_name_tr])
                print("Chars Excel:", [ord(c) for c in target_name_tr])

if __name__ == '__main__':
    main()

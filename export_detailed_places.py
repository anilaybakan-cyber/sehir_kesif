import json
import pandas as pd
from pathlib import Path

def export_all_details():
    cities_dir = Path("assets/cities")
    records = []
    
    for json_file in cities_dir.glob("*.json"):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        city_name = data.get("city", json_file.stem.capitalize())
        
        for place in data.get("highlights", []):
            records.append({
                "Şehir": city_name,
                "Yer Adı": place.get("name", ""),
                "Kategori": place.get("category", ""),
                "Alt Kategori": place.get("subcategory", ""),
                "Enlem (Lat)": place.get("lat", ""),
                "Boylam (Lng)": place.get("lng", ""),
                "Açıklama (TR)": place.get("description", ""),
                "Açıklama (EN)": place.get("description_en", "")
            })
            
    df = pd.DataFrame(records)
    export_path = "/Users/anilebru/Desktop/Guncel_Tum_Mekanlar_Detayli.xlsx"
    df.to_excel(export_path, index=False)
    print(f"Exported {len(records)} records to {export_path}")

if __name__ == '__main__':
    export_all_details()

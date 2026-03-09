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
            tags = place.get("tags", [])
            if isinstance(tags, list):
                tags_str = ", ".join(tags)
            else:
                tags_str = str(tags)
                
            records.append({
                "Şehir": city_name,
                "Yer Adı (TR)": place.get("name", ""),
                "Yer Adı (EN)": place.get("name_en", place.get("name", "")),
                "Kategori": place.get("category", ""),
                "Alt Kategori": place.get("subcategory", ""),
                "Bölge (Area)": place.get("area", ""),
                "Enlem (Lat)": place.get("lat", ""),
                "Boylam (Lng)": place.get("lng", ""),
                "Fiyat Seviyesi": place.get("price", ""),
                "Puan (Rating)": place.get("rating", ""),
                "Açıklama (TR)": place.get("description", ""),
                "Açıklama (EN)": place.get("description_en", ""),
                "Yerel İpucu (TR)": place.get("localTip", ""),
                "Yerel İpucu (EN)": place.get("localTip_en", ""),
                "Etiketler (Tags)": tags_str,
                "En İyi Zaman (TR)": place.get("bestTime", ""),
                "En İyi Zaman (EN)": place.get("bestTime_en", ""),
                "Resim URL": place.get("imageUrl", "")
            })
            
    df = pd.DataFrame(records)
    export_path = "/Users/anilebru/Desktop/Tum_Sehirler_Cok_Detayli_Liste.xlsx"
    df.to_excel(export_path, index=False)
    print(f"Exported {len(records)} records to {export_path}")

if __name__ == '__main__':
    export_all_details()

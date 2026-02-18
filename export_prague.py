import json
import csv

input_file = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/prag.json'
output_file = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/MyWay_Prag_Data.csv'

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Mekan Adı (TR)', 'Mekan Adı (EN)', 'Kategori', 'Açıklama (TR)', 'Açıklama (EN)'])
        
        for place in data.get('highlights', []):
            name = place.get('name', '')
            name_en = place.get('name_en', name) # Fallback to name if name_en missing
            category = place.get('category', '')
            desc = place.get('description', '')
            desc_en = place.get('description_en', '')
            
            writer.writerow([name, name_en, category, desc, desc_en])
            
    print(f"Export successful: {output_file}")
except Exception as e:
    print(f"Error: {e}")

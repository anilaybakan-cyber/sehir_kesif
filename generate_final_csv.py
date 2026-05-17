import csv
import os
import json

cities_dir = 'assets/cities'
output_file = '/Users/anilebru/Desktop/revize_gerçek_içerikler.csv'

generic_patterns = [
    "kenti keşfinde dinamizmi ve",
    "kentin haritasına karakter katan en sevilen",
    "Yerel malzemelere ve mutfak sanatına olan bağlılığıyla",
    "en stil sahibi lezzet duraklarından biri olarak öne çıkan",
    "As a refined social and cultural point",
    "Renowned for its commitment to local ingredients",
    "A prestigious culinary destination in",
    "contemporary spirit and cultural identity"
]

def is_generic(text):
    if not text: return False
    for p in generic_patterns:
        if p in text:
            return True
    return False

rows = []
rows.append(["City", "Place Name", "Description (TR)", "Description (EN)", "Tips (TR)", "Tips (EN)", "Status"])

for filename in os.listdir(cities_dir):
    if filename.endswith('.json'):
        path = os.path.join(cities_dir, filename)
        with open(path, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            city_name = filename.replace('.json', '').capitalize()
            highlights = data
        else:
            city_name = data.get('city', filename.replace('.json', '').capitalize())
            highlights = data.get('highlights', [])
        
        for h in highlights:
            d_tr = h.get('description', '')
            d_en = h.get('description_en', '')
            
            status = "GÜNCELLENDİ (GERÇEK)" if not is_generic(d_tr) else "JENERİK (GÜNCELLENMELİ)"
            
            rows.append([
                city_name,
                h.get('name', ''),
                d_tr,
                d_en,
                h.get('tips', ''),
                h.get('tips_en', ''),
                status
            ])

with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Created {output_file} with {len(rows)-1} items.")

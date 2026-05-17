import os
import json

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

cities_dir = 'assets/cities'
generic_items = []

for filename in os.listdir(cities_dir):
    if filename.endswith('.json'):
        path = os.path.join(cities_dir, filename)
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            
            city_name = data.get('city', filename.replace('.json', ''))
            highlights = data.get('highlights', [])
            
            for h in highlights:
                desc_tr = h.get('description', '')
                desc_en = h.get('description_en', '')
                
                if is_generic(desc_tr) or is_generic(desc_en):
                    generic_items.append({
                        "city": city_name,
                        "name": h.get('name', ''),
                        "file": path
                    })
        except:
            continue

print(f"Total generic items found: {len(generic_items)}")
# Print first 20 to verify
for item in generic_items[:20]:
    print(f"{item['city']} | {item['name']}")

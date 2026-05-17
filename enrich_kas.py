#!/usr/bin/env python3
import json

updates = {
    "ChIJp-bnXADbwRQR_iGoNLD8grk": {
        "description": "Akdeniz'in en masmavi ve duru köşelerinden biri olan Kaş, antik Likya kalıntıları ile modern bohem yaşamı iç içe sunan eşsiz bir sahil kasabasıdır. Dünyaca ünlü dalış noktaları, begonvillerle süslü taş sokakları ve karşısındaki Meis adası manzarasıyla, her köşesinde huzuru ve macerayı bir arada bulacağınız bir cennettir.",
        "description_en": "One of the most azure and clear corners of the Mediterranean, Kas is a unique coastal town offering ancient Lycian ruins intertwined with modern bohemian life. With its world-famous diving spots, bougainvillaea-decorated stone streets, and the view of the opposite island of Kastellorizo, it is a paradise where you'll find peace and adventure together at every corner."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/kas.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    pid = place.get('id')
    if pid in updates:
        place['description'] = updates[pid]['description']
        place['description_en'] = updates[pid]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Kas enriched {count} items.")

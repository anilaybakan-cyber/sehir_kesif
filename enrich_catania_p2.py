#!/usr/bin/env python3
import json

updates = {
    "cat_trattoria_etnea_45": {
        "description": "Catania'nın karakteristik balıkçı limanı Ognina'da yer alan bu seçkin restoran, denize sıfır masalarında Akdeniz'in en taze mahsullerini sunuyor. Geleneksel Sicilya tariflerini modern bir şıklıkla buluşturan mekan, dalga sesleri eşliğinde huzurlu ve kaliteli bir akşam yemeği için kentin en iyi sahil duraklarından biridir.",
        "description_en": "Located in Catania's characteristic fishing harbor Ognina, this elite restaurant offers the freshest Mediterranean produce at its seafront tables. Bringing together traditional Sicilian recipes with modern elegance, it is one of the city's best coastal stops for a peaceful and high-quality dinner accompanied by the sound of waves."
    },
    "cat_trattoria_salvo_49": {
        "description": "San Giovanni Li Cuti'nin ikonik siyah volkanik taşlı kumsalında yer alan Cutilisci, doğallığı ve gurme mutfağıyla bilinir. Denize karşı ferah atmosferi, özenle hazırlanan mezeleri ve kentsel koşturmacadan uzak sakinliğiyle, Catania'nın sahil gastronomisini deneyimlemek için hem samimi hem de prestijli bir lezzet limanıdır.",
        "description_en": "Located on the iconic black volcanic stone beach of San Giovanni Li Cuti, Cutilisci is known for its naturalness and gourmet kitchen. With its fresh atmosphere facing the sea, carefully prepared mezes, and calmness away from urban hustle, it is both a sincere and prestigious flavor harbor to experience Catania's seaside gastronomy."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/catania.json.draft'
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

print(f"✅ Catania Part 2: Enriched {count} items.")

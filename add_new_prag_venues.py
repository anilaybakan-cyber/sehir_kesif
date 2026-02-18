#!/usr/bin/env python3
"""
Add 49 new Prague venues to prag.json from enriched CSV
"""
import json
import csv
import re

# Category to tags mapping
CATEGORY_TAGS = {
    "Tapas Bar": ["tapas", "ispanyol", "bar", "yeme-icme"],
    "Bistro": ["bistro", "restoran", "yeme-icme"],
    "Modern Çek": ["cek-mutfagi", "restoran", "modern", "yeme-icme"],
    "Slovak Restoran": ["slovak", "restoran", "yeme-icme"],
    "Ukrayna Restoran": ["ukrayna", "restoran", "yeme-icme"],
    "Amerikan Lokanta": ["amerikan", "lokanta", "yeme-icme"],
    "İtalyan": ["italyan", "restoran", "yeme-icme"],
    "İtalyan Fine Dining": ["italyan", "fine-dining", "restoran", "yeme-icme"],
    "Geleneksel Çek": ["cek-mutfagi", "geleneksel", "restoran", "yeme-icme"],
    "Fine Dining": ["fine-dining", "restoran", "yeme-icme"],
    "Steakhouse": ["steakhouse", "et", "restoran", "yeme-icme"],
    "Meksika": ["meksika", "restoran", "yeme-icme"],
    "Ukrayna Deniz Ürünleri": ["ukrayna", "deniz-urunleri", "restoran", "yeme-icme"],
    "Fast Casual": ["fast-food", "restoran", "yeme-icme"],
    "Japon-Peru": ["japon", "peru", "restoran", "yeme-icme"],
    "Çek Pub": ["cek-mutfagi", "pub", "bira", "yeme-icme"],
    "Bira Fabrikası": ["brewery", "bira", "pub", "yeme-icme"],
    "Bira Barı": ["bira", "bar", "craft-beer", "yeme-icme"],
    "Craft Bira": ["craft-beer", "bira", "bar", "yeme-icme"],
    "Bira Barı-Restoran": ["bira", "restoran", "bar", "yeme-icme"],
    "Brunch": ["brunch", "kahvalti", "kafe", "yeme-icme"],
    "Fransız Brunch": ["frans", "brunch", "kafe", "yeme-icme"],
    "İngiliz Brunch": ["ingiliz", "brunch", "kafe", "yeme-icme"],
    "Kahvaltı": ["kahvalti", "kafe", "yeme-icme"],
    "Şarap Barı": ["sarap", "bar", "vinoteka", "yeme-icme"],
    "Pub Restoran": ["pub", "restoran", "yeme-icme"],
    "Domuz Eti Restoranı": ["domuz", "et", "restoran", "yeme-icme"],
    "İspanyol": ["ispanyol", "tapas", "restoran", "yeme-icme"],
}

def create_id(name):
    """Create URL-friendly ID from name"""
    # Normalize characters
    id_str = name.lower()
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ý': 'y',
        'č': 'c', 'ď': 'd', 'ě': 'e', 'ň': 'n', 'ř': 'r', 'š': 's',
        'ť': 't', 'ů': 'u', 'ž': 'z', 'ô': 'o', 'ö': 'o', 'ü': 'u',
        'ğ': 'g', 'ş': 's', 'İ': 'i', 'ı': 'i',
        ' ': '-', "'": '', '"': '', '.': '', ',': ''
    }
    for old, new in replacements.items():
        id_str = id_str.replace(old, new)
    id_str = re.sub(r'[^a-z0-9-]', '', id_str)
    id_str = re.sub(r'-+', '-', id_str)
    return id_str.strip('-')

def get_best_time(category):
    """Determine best time based on category"""
    if category in ["Brunch", "Fransız Brunch", "İngiliz Brunch", "Kahvaltı"]:
        return ("Sabah/Öğle", "Morning/Afternoon")
    elif category in ["Şarap Barı", "Bira Barı", "Craft Bira"]:
        return ("Akşam", "Evening")
    else:
        return ("Öğle/Akşam", "Lunch/Dinner")

def main():
    # Read existing prag.json
    with open('assets/cities/prag.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_count = len(data['highlights'])
    print(f"Mevcut mekan sayısı: {existing_count}")
    
    # Read enriched CSV
    new_venues = []
    with open('prag_yeni_50_mekan_enriched.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row['category']
            tags = CATEGORY_TAGS.get(category, ["yeme-icme"])
            best_time = get_best_time(category)
            
            venue = {
                "name": row['name'],
                "name_en": row['name_en'],
                "area": row['area'],
                "category": category,
                "tags": tags,
                "distanceFromCenter": 1.0,  # Default
                "lat": float(row['lat']),
                "lng": float(row['lng']),
                "price": "$$",  # Default moderate
                "rating": 4.5,  # Default good rating
                "description": row['description'],
                "description_en": row['description_en'],
                "localTip": row.get('localTip', ''),
                "localTip_en": row.get('localTip_en', ''),
                "bestTime": best_time[0],
                "bestTime_en": best_time[1],
                "imageUrl": row.get('imageUrl', ''),
                "id": create_id(row['name'])
            }
            new_venues.append(venue)
    
    print(f"Eklenecek yeni mekan sayısı: {len(new_venues)}")
    
    # Add new venues
    data['highlights'].extend(new_venues)
    
    # Save to assets
    with open('assets/cities/prag.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ assets/cities/prag.json güncellendi ({len(data['highlights'])} mekan)")
    
    # Save to ota_data_pack
    with open('ota_data_pack/cities/prag.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ ota_data_pack/cities/prag.json güncellendi")
    
    print(f"\n✅ Toplam mekan sayısı: {len(data['highlights'])}")

if __name__ == "__main__":
    main()

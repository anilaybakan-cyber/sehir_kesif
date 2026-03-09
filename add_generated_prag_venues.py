#!/usr/bin/env python3
import json
import csv
import re

def main():
    with open('assets/cities/prag.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_count = len(data['highlights'])
    print(f"Mevcut mekan sayısı: {existing_count}")
    
    existing_names = {p['name'] for p in data['highlights']}
    
    new_venues = []
    with open('/Users/anilebru/Desktop/prag_yeni_mekan_onerileri_full.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['name'] in existing_names:
                continue
            
            venue = {
                "name": row['name'],
                "name_en": row['name_en'],
                "area": row['area'],
                "category": row['category'],
                "tags": [t.strip() for t in row['tags'].split(',')],
                "distanceFromCenter": 1.0,
                "lat": float(row['lat']),
                "lng": float(row['lng']),
                "price": row['price'],
                "rating": float(row['rating']),
                "description": row['description'],
                "description_en": row['description_en'],
                "localTip": row.get('tips', ''),
                "localTip_en": row.get('tips_en', ''),
                "bestTime": row['bestTime'],
                "bestTime_en": row['bestTime_en'],
                "imageUrl": row.get('imageUrl', ''),
                "id": row['id']
            }
            new_venues.append(venue)
            
    print(f"Eklenecek yeni mekan sayısı: {len(new_venues)}")
    data['highlights'].extend(new_venues)
    
    with open('assets/cities/prag.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    with open('ota_data_pack/cities/prag.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"✅ assets/cities/prag.json güncellendi (Toplam: {len(data['highlights'])} mekan)")

if __name__ == "__main__":
    main()

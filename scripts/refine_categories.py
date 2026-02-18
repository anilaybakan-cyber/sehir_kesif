import json
import os
import re

cities = [
    'amsterdam.json', 'stockholm.json', 'floransa.json', 'bangkok.json',
    'zurih.json', 'cenevre.json', 'milano.json', 'madrid.json',
    'nice.json', 'marsilya.json', 'lyon.json', 'kopenhag.json',
    'berlin.json', 'istanbul.json', 'paris.json', 'roma.json', 
    'londra.json', 'newyork.json', 'tokyo.json', 'sevilla.json'
]

# Kategori düzeltme kuralları
# "Deneyim", "Tarihi", "Bar" gibi kategorilerde olup aslında yeme-içme mekanı olanları bul
food_keywords = [
    'restoran', 'restaurant', 'kafe', 'cafe', 'kahve', 'coffee', 'döner', 
    'burger', 'pizza', 'tapas', 'yemek', 'mutfağı', 'gastronomi', 'pastane',
    'kebap', 'currywurst', 'lezzet', 'meyhane', 'bar', 'pub', 'bira', 'brewery'
]

def refine_categories():
    for city_file in cities:
        path = os.path.join('assets/cities', city_file)
        if not os.path.exists(path):
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified = False
        for h in data.get('highlights', []):
            name = h.get('name', '').lower()
            name_en = h.get('name_en', '').lower()
            desc = h.get('description', '').lower()
            tags = [t.lower() for t in h.get('tags', [])]
            current_cat = h.get('category', '')
            
            # Eğer kategori zaten Restoran veya Kafe ise dokunma
            if current_cat in ['Restoran', 'Kafe']:
                continue
                
            # Anahtar kelime kontrolü
            is_food = any(kw in name or kw in name_en or kw in desc or kw in tags for kw in food_keywords)
            
            if is_food:
                # Daha spesifik ayrım: kafe mi restoran mı?
                is_cafe = any(kw in name or kw in name_en or kw in desc or kw in tags for kw in ['kafe', 'cafe', 'kahve', 'coffee', 'pastane', 'bakery'])
                
                new_cat = 'Kafe' if is_cafe else 'Restoran'
                
                # Özel durum: Bar/Pub
                if any(kw in name or kw in name_en or kw in tags for kw in ['bar', 'pub', 'bira', 'brewery']):
                    new_cat = 'Bar'
                
                if new_cat != current_cat:
                    h['category'] = new_cat
                    modified = True
                    print(f"[{city_file}] {h['name']}: {current_cat} -> {new_cat}")
                    
        if modified:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    refine_categories()

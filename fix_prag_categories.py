#!/usr/bin/env python3
"""
Fix categories for new Prague venues - use only Yeme-İçme, Bar, Kafe
"""
import json

# Category mapping: old -> (new_tr, new_en)
CATEGORY_MAP = {
    # Restaurants -> Yeme-İçme
    "Tapas Bar": ("Yeme-İçme", "Food & Drink"),
    "Bistro": ("Yeme-İçme", "Food & Drink"),
    "Modern Çek": ("Yeme-İçme", "Food & Drink"),
    "Slovak Restoran": ("Yeme-İçme", "Food & Drink"),
    "Ukrayna Restoran": ("Yeme-İçme", "Food & Drink"),
    "Amerikan Lokanta": ("Yeme-İçme", "Food & Drink"),
    "İtalyan": ("Yeme-İçme", "Food & Drink"),
    "İtalyan Fine Dining": ("Yeme-İçme", "Food & Drink"),
    "Geleneksel Çek": ("Yeme-İçme", "Food & Drink"),
    "Fine Dining": ("Yeme-İçme", "Food & Drink"),
    "Steakhouse": ("Yeme-İçme", "Food & Drink"),
    "Meksika": ("Yeme-İçme", "Food & Drink"),
    "Ukrayna Deniz Ürünleri": ("Yeme-İçme", "Food & Drink"),
    "Fast Casual": ("Yeme-İçme", "Food & Drink"),
    "Japon-Peru": ("Yeme-İçme", "Food & Drink"),
    "Pub Restoran": ("Yeme-İçme", "Food & Drink"),
    "Domuz Eti Restoranı": ("Yeme-İçme", "Food & Drink"),
    "İspanyol": ("Yeme-İçme", "Food & Drink"),
    
    # Bars -> Bar
    "Çek Pub": ("Bar", "Bar"),
    "Bira Fabrikası": ("Bar", "Bar"),
    "Bira Barı": ("Bar", "Bar"),
    "Craft Bira": ("Bar", "Bar"),
    "Bira Barı-Restoran": ("Bar", "Bar"),
    "Şarap Barı": ("Bar", "Bar"),
    
    # Cafes/Brunch -> Kafe
    "Brunch": ("Kafe", "Cafe"),
    "Fransız Brunch": ("Kafe", "Cafe"),
    "İngiliz Brunch": ("Kafe", "Cafe"),
    "Kahvaltı": ("Kafe", "Cafe"),
}

def main():
    # Read prag.json
    with open('assets/cities/prag.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    fixed_count = 0
    
    # Fix categories for the last 49 entries (new venues)
    for highlight in data['highlights'][-49:]:
        old_cat = highlight.get('category', '')
        if old_cat in CATEGORY_MAP:
            new_cat_tr, new_cat_en = CATEGORY_MAP[old_cat]
            highlight['category'] = new_cat_tr
            highlight['category_en'] = new_cat_en
            fixed_count += 1
            print(f"  {highlight['name']}: {old_cat} -> {new_cat_tr}")
    
    print(f"\n✅ {fixed_count} mekan kategorisi düzeltildi")
    
    # Save to assets
    with open('assets/cities/prag.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✅ assets/cities/prag.json güncellendi")
    
    # Save to ota_data_pack
    with open('ota_data_pack/cities/prag.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✅ ota_data_pack/cities/prag.json güncellendi")

if __name__ == "__main__":
    main()

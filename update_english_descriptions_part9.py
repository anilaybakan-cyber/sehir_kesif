
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MADRID
    "Salty Dog Madrid": "Nautical-themed gastropub featuring a cozy atmosphere and global comfort food.",
    "Santana Choux": "Artisanal pastry shop specializing in sweet and savory choux with innovative fillings.",
    "Satán Cocktail Bar": "Gothic-themed cocktail bar serving unique drinks in an intimate, energetic setting.",
    "Shambala": "Tropical tiki bar near Gran Vía with sand floors and exotic cocktails.",
    "Shanghai Sheng Jian Bao": "Casual Chinese spot famous for its authentic pan-fried soup dumplings and sushi.",
    "Sinfonía Specialty Coffee": "Harmonious specialty coffee shop dedicated to perfect brews and a relaxing vibe.",
    "TastyCakes": "Authentic American bakery offering cakes and cookies made with local ingredients.",
    "ZAFYRO Cocktail Experience": "Magical cocktail bar inspired by Disney musicals offering theatrical drinks and decor.",
    "chök - Chueca | Pastelería sin gluten Madrid": "Gluten-free bakery paradise offering exquisite chocolate treats and matcha lattes.",

    # MARRAKESH
    "Anzar": "Vibrant restaurant celebrating Berber mythology with fresh, authentic Moroccan flavors.",
    "Arroz Bar Restaurant": "Specialist Spanish restaurant serving authentic paella and tapas in a lively setting.",
    "Azalai Şehir Çarşısı": "Unique urban souk concept blending Tuareg spirit with desert-inspired design.",
    "Bidaya Rooftop Restaurant Bar by Almaha": "Panoramic rooftop venue offering premium drinks and stunning views of the Medina.",
    "Café Carmel Marrakech": "Modern cafe with Moroccan touches serving specialty coffee and healthy breakfast options."
}

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    total_updated = 0
    print(f"Applying updates to {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_changed = False
            
            for place in highlights:
                name = place.get('name', '').strip()
                
                # Check exact name match
                if name in UPDATES:
                    place['description_en'] = UPDATES[name]
                    file_changed = True
                    total_updated += 1
            
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal English descriptions updated: {total_updated}")

if __name__ == "__main__":
    main()

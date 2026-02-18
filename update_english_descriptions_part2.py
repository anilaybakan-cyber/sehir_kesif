
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # FLORENCE
    "Wine Lab - vino sfuso": "Friendly wine bar with self-serve tastings, regional wines, and charming outdoor terrace.",

    # HONG KONG
    "Bakehouse": "Famous artisanal bakery known for sourdough egg tarts and flaky pastries in a cozy setting.",
    "Cloud Nine Specialty Coffee": "Unique Shaolin Temple-themed cafe serving specialty coffee, hearty breakfasts, and homemade desserts.",
    "FRANCIS west": "Vibrant spot serving modern Middle Eastern cuisine with North African influences and shared plates.",
    "Frenchie Toquee HK": "Authentic French bakery offering fresh traditional pastries and cakes by a certified chef.",
    "Islet Coffee Lab (Central)": "Tranquil coffee escape featuring micro-roasted beans and a relaxing open-air environment with greenery.",
    "MY KITCHEN (Tibetan Halal Homemade Food Restaurant)": "Halal-certified authentic Tibetan restaurant known for Momos and warm hospitality in a homely setting.",
    "Mayse Artisan Bakery": "Plant-based bakery specializing in traditional Latvian sourdough rye bread and vegan treats.",
    "Omnia Restaurant Hong Kong": "Elegant Lebanese restaurant blending traditional flavors with innovative twists and creative cocktails.",
    "Pakeeza Food Restaurant": "Casual dining spot serving authentic Pakistani curries, biryanis, and fresh naan in a spacious setting.",
    "Sheer Coffee": "Minimalist Japanese-inspired cafe with wabi-sabi decor, offering seasonal drinks and signature toast.",
    "Sugar Brothers hk": "Dessert shop renowned for signature Napoleon cakes, custom designs, and trendy sweet treats.",
    "The Savory Project": "Sophisticated bar revolutionizing cocktails with savory, umami-driven flavors in an intimate setting.",
    "Two-and-a-Half Sokağı": "Western coffee shop in Sai Ying Pun offering quality brews and heavy meals in a cozy space.",
    "Uncle Ben Coffee": "Popular specialty coffee shop famous for latte art, roll cakes, and a pet-friendly atmosphere."
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


import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # NAPOLI
    "WineCafè Da Mario": "Charming family-run wine cafe offering artisanal cheese platters and local Neapolitan vintages with a view.",
    "Zero - Healthy Bar & Specialty Coffee - Napoli": "Wellness-focused cafe serving fresh acai bowls, avocado toast, and protein-packed pancakes in an inviting setting.",
    "al Ruotino - Pizzeria Ristorante": "Authentic Neapolitan pizzeria specializing in traditional pan-baked 'ruotino' pizzas and classic Margherita since decades.",

    # NEW YORK
    "Blank Sokağı Coffee": "Trendy micro-cafe chain serving signature pistachio lattes and breakfast tacos in a minimalist setting.",
    "Blue Dove Coffee": "Visually appealing coffee truck serving artisanal lattes and fresh pastries with a friendly community vibe.",
    "Cellar 36": "Cozy natural wine bar in Manhattan offering candlelit ambiance, $1 oysters, and small plates.",
    "Cork Wine Bar": "Vibrant wine bar specializing in French cheeses, duck meats, and artisanal charcuterie boards.",
    "Cozymeal Cooking Classes NYC": "Hands-on culinary experiences led by professional chefs, covering diverse global cuisines from pasta to sushi.",
    "El Delicioso NY Food Truck": "Zestful food truck serving authentic Colombian Bandeja Paisa, BBQ ribs, and cheesy arepas on the go.",
    "MOE EATS NYC": "Authentic Middle Eastern halal dining in Midtown, featuring fresh shawarma bowls, kebabs, and aromatic biryani.",
    "Paper Sons Cafe": "Asian-inspired Chinatown cafe serving unique black sesame mooncakes and artisanal 'silk + smoke' lattes.",
    "Qahwah House W Village": "Authentic Yemeni coffee house famous for Adeni Chai and honey-filled 'Khaliat Alnahl' honeycomb bread.",
    "Somm Time": "Lively Lower East Side wine bar offering seasonal small plates and wines from small producers.",
    "Sote Coffee Roasters": "Independent Upper West Side roastery serving specialty lavender lattes and fresh house-baked cookies.",
    "Sweet Cats Union Meydanı": "Whimsical kawaii-themed cafe in Union Square famous for character-inspired ice creams and fruit slushes."
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

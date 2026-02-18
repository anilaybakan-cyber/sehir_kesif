
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # NEW YORK
    "Tiny Tapas and Bites": "Vibrant Latin-Asian fusion spot serving creative small plates and sushi in a cozy setting.",

    # NICE
    "\"Mary's sweeties\" gâteaux sur commande": "Artisanal patisserie specializing in bespoke custom cakes made with fresh, seasonal ingredients.",
    "Au Goût Thé D'antan": "Unique tea room and antique shop offering homemade pastries in a vintage atmosphere.",
    "Bella ciao - Bar": "Latin-inspired rooftop bar and restaurant with panoramic views over the Notre Dame Basilica.",
    "Big Boy Coffee": "Urban-style coffee shop featuring local art exhibitions, designer decor, and quality espresso.",
    "Café Marché": "Women-owned cafe serving fresh market-inspired brunch and homemade French cuisine near Cours Saleya.",
    "Cali Coffee Shop | Brunch Breakfast Lunch |": "Laid-back Californian-style coffee shop known for fresh bagels and a delightful brunch experience.",
    "French Coffee Shop": "Cozy French chain serving traditional espresso and viennoiserie in a friendly local ambiance.",
    "Full Bloom Café": "Peaceful vegan cafe and specialty coffee shop filled with lush greenery and natural light.",
    "La 36eme chambre": "Audacious Asian-fusion brunch spot blending Korean and Japanese flavors in a modern setting.",
    "Le comptoir des frères": "Refined wine bar and restaurant offering artisanal charcuterie and regional vintages in Nice.",
    "Les Agitateurs - restaurant gastronomique": "Michelin-starred restaurant serving contemporary Mediterranean cuisine with creative flair and seasonal ingredients.",
    "Pauline fait la cuisine, plat du jour, cuisine du marché, fait maison, sandwicherie, coffee shop, terrasse, Nice": "Serene micro-canteen offering homemade market dishes and delicious daily cakes in a convivial setting.",
    "The One - Coffee Shop, Bar Tapas & Lounge in Nice": "Modern multi-concept lounge offering shared tapas, cocktails, and coffee in a warm ambiance.",
    "V and B Nice Vauban": "Vibrant wine and beer bar featuring an extensive craft selection and warm indoor-outdoor atmosphere."
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

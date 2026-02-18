
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # NAPLES
    "Il rifugio Wine bar PEPPE MASIELLO. SPRITZ": "Vibrant Quartieri Spagnoli wine bar known for signature Spritz and lively local student scene.",
    "Jamme Caffé": "Authentic local cafe serving traditional Passalacqua espresso and fresh sfogliatella in a cozy setting.",
    "Joseph Restaurant": "Contemporary Neapolitan restaurant specializing in fresh Mediterranean seafood and creative house-made pasta dishes.",
    "La Fesseria - Sokağı Bar": "Trendy 'Wine Garage' cocktail bar offering balanced drinks and local charcuterie in a relaxed vibe.",
    "Lento Hi-Fi Bar": "Sophisticated listening bar featuring high-fidelity sound, disco-funk DJ sets, and refined evening cocktails.",
    "Mosto - Birra Artigianale & Distillati": "Popular craft beer haven offering a vast selection of IPAs, whiskies, and lively happy hours.",
    "Pasticceria \"SE.AN.\" di Serra Antonio": "Traditional family-run pastry shop serving artisanal Neapolitan sweets and classic breakfast treats with care.",
    "Pasticceria Tizzano® dal 1960 - Unica Sede": "Historic bakery celebrated for traditional babà and sfogliatella, reflecting decades of Neapolitan passion.",
    "Pasticceria, Caffetteria napoli Piterà": "Charming local pastry shop and cafe serving traditional sweets and espresso in a welcoming ambiance.",
    "SANTO cocktail bar": "Stylish cocktail bar in Chiaia known for expert mixology, cozy decor, and affordable evening drinks.",
    "San Caffè cappuccino factory": "Specialty cafe famous for artistic latte designs, personalized cappuccinos, and authentic Italian breakfast vibes.",
    "Sansone Coffee Artisan Microroastery & Specialty Coffee": "Dedicated artisan microroastery serving high-quality specialty coffee and house-roasted beans in a modern setting.",
    "Trattoria Pizzeria Bella Napoli Centro - Chef dal 1990": "Authentic trattoria serving perfectly crispy fried pizza and traditional seafood pasta since 1990.",
    "Trattoria canta napoli": "Traditional Italian trattoria offering classic home cooking and professional service in a pleasant atmosphere.",
    "Wine&ammor": "Relaxed and trendy wine bar offering local vintages and Limoncello Spritz in a cozy setting.",

    # NEW YORK
    "787 Coffee": "Vibrant farm-to-cup cafe serving whiskey-infused Puerto Rican coffee and freshly baked empanadas.",
    "Altair Restaurant NYC": "Elegant fine-dining destination featuring modern-American fare and celestial-inspired design for romantic evenings.",
    "BONSAII Tapas & Wine Bar": "Intimate botanical-themed bar blending Japanese and Spanish influences with creative international tapas."
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

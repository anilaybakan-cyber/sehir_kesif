
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MARSEILLE
    "Nabu et Jéro": "Vibrant restaurant blending traditional French cuisine with innovative Provençal flavors and exquisite seafood.",
    "PANAMA LATINO FOOD": "Authentic Latin American spot serving fresh ceviche, empanadas, and tropical cocktails in a lively atmosphere.",
    "Paloma Cocktail Bar": "Trendy bar known for creative seasonal cocktails, local DJ sets, and a cozy terrace.",
    "Papamousse": "Cheerful and vibrant bar with an inviting terrace, perfect for mojitos and festive nights.",
    "Propaganda - bar tapas Marseille": "Socio-political themed bar serving creative cocktails and diverse tapas with Vieux Port views.",
    "Restaurant-Epicerie fine. L'enseigne 117.": "Gourmet sandwich shop and grocery store serving artisanal products and global daily specials.",
    "Risette – Torréfacteur & Coffee Shop": "In-house roastery and cafe serving specialty coffee, homemade flans, and seasonal lunch bowls.",
    "Tigermilk Marseille": "South American street food haven serving pulled pork tacos, fresh ceviche, and truffle quesadillas.",
    "Verre a Cruise - Tapas & Cocktail Bar": "Nautical-themed bar serving Middle Eastern hidden gems like mezzes and octopus-infused tapas.",
    "Weeno - Vins, spiritueux, bières et sakés - Formation WSET - Marseille": "Convivial wine academy offering interactive tastings and professional WSET certification courses.",
    "White Rabbit": "Rock 'n' roll bar with a vintage 70s vibe, hosting DJ sets and live music.",
    "mamaco (Marseille Madame Coree) restaurant coreen marseille": "Authentic Korean gem serving homemade kimchi, bibimbap, and crispy fried chicken in a cozy setting.",

    # MILAN
    "Barlafus Cafè - Milano": "Welcoming Milanese cafe serving gourmet panini, seasonal salads, and home-baked pastries.",
    "Bottega dell'Arte del Vino": "Elegant enoteca overlooking Sempione Park, offering traditional Milanese dishes and premium wine pairings.",
    "Bricco Café": "Cozy and warm neighborhood cafe celebrated for its exceptional coffee and custard-filled croissants."
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

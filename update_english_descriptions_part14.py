
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MILAN
    "Cafezal Specialty Coffee - Magenta": "Specialty coffee roaster offering 1920s glamour, artisanal pastries, and sustainable Brazilian brews in a refined setting.",
    "Cortinovis Specialty Coffee roasters Milano": "Milan's first official Slow Food roaster serving exceptional single-origin espressos and gourmet pistachio croissants.",
    "Daimyo Restaurant Milano": "Refined Japanese fusion restaurant blending traditional techniques with Mediterranean ingredients in an intimate, dark-wood setting.",
    "Debbie's": "Welcoming cafe serving delicious focaccia sandwiches, artisanal pistachio croissants, and specialty coffee with joyful energy.",
    "EnotecaWine": "Historic wine shop and restaurant serving traditional Milanese risotto and ossobuco paired with barrel-poured wines.",
    "Il Cafetero Specialty Coffee Milan": "Cozy neighborhood gem serving 100% Arabica moka brews, brioche salata, and apricot cakes with passion.",
    "Insula Sardinia Experiences - Milano": "Authentic Sardinian cultural hub offering traditional island tapas, specialty sea-sourced dishes, and regional wines.",
    "LUCKY COCKTAIL BAR MILANO": "Contemporary lounge club serving expertly mixed cocktails and a refined apericena buffet in an elegant setting.",
    "Luma Cocktail Bar": "Modern bar serving original Latin-inspired cocktails and creative tapas with a popular Sunday brunch vibe.",
    "Sciuma Radical Wines - Enoteca Naturale": "Charming natural wine bar specializing in minimal-intervention wines paired with seasonal pumpkin soup and crostoni.",
    "Tin - Cocktail Pub Milano": "Trendy industrial-themed pub offering Italian spirits, Negronis, and live jazz or stand-up comedy nights.",
    "UNGARO 1956": "Historic pastry shop and cafeteria serving artisanal Italian desserts, all-you-can-eat pizza, and a vibrant Tuesday aperitivo.",
    "Venchi": "Iconic Italian chocolatier and gelateria serving premium Piedmontese hazelnut chocolates and artisanal gelato since 1878.",
    "Verso Ristorante, Capitaneo": "Two-Michelin-star fine dining establishment by the Capitaneo brothers, featuring a theatrical chef's table and modern Italian menus.",
    "Vino Vino dal 1921": "Historic enoteca focused on small, emerging producers, offering expert wine consulting and a century of heritage."
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


import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MILAN
    "Zizania via Celestino | Cocktail bar Milano": "Chic and vibrant botanical cocktail bar offering creative drinks and a fun, stylish atmosphere.",

    # NAPLES
    "AZZUPPA Restaurant": "Cozy Neapolitan restaurant featuring a retro 60s vibe and traditional dishes with modern twists.",
    "Alkymya Bellini": "Lively cocktail bar in Piazza Bellini serving tasty drinks paired with generous local tapas.",
    "Antica Pasticceria Lauri": "Historic family bakery famous for authentic Neapolitan sfogliatella and traditional recipes since generations.",
    "Apoteca Winebar": "Intimate and romantic wine bar in a shaded alley, serving local parmigiana and regional wines.",
    "Bar Materdei": "Authentic neighborhood bar known for its exceptional coffee, warm hospitality, and traditional Neapolitan cornetti.",
    "Bar and Bet's": "Vibrant sports bar and cafe perfect for watching football while enjoying refreshing frozen lemon drinks.",
    "Barrio Alto Caffe": "Charming hilltop cafe offering exceptional espresso and fresh pastries with a beautiful view of Naples.",
    "Botanical Bar": "Lush and magical garden bar serving plant-infused cocktails and Mediterranean fusion bites in Municipio.",
    "Cantina Central 92": "Lively and welcoming cantina known for affordable regional wines, Spritz, and authentic bruschetta.",
    "Decanter Wine and More": "Elegant yet cozy wine bar offering handcrafted cheese boards and expert local wine pairings.",
    "Esto Es Mezcaleria": "Energetic mezcaleria serving exceptional tequila cocktails and fresh tapas with live DJ sets.",
    "Gran Caffè Cimmino": "Historic and elegant cafe offering premium espresso and the famous Polacca pastry with sea views.",
    "Gran Caffè Valentino": "Refined cafe specializing in traditional Neapolitan sweets like cannoli and sfogliatelle in a stylish setting.",
    "Il Fiasco Bar&Restaurant": "Welcoming bar and restaurant with a pleasant outdoor area, serving Italian specialties and cocktails."
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

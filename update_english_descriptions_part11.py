
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MARRAKESH
    "Restaurant - Le 68 Bar à Vin Marrakech": "Sophisticated French wine bar offering tapas and coq au vin in a cozy, vibrant setting.",
    "Restaurant Granada Marrakech": "Charming spot blending traditional Moroccan dishes with Italian options in an elegant atmosphere.",
    "Rooftop Restaurant El Kennaria": "Modern Moroccan rooftop restaurant offering traditional flavors, live music, and stunning city views.",
    "Simple specialty coffee": "Serene coffee stall serving espresso, matcha, and homemade syrups with plant-based options.",
    "Sky Bar Wow": "Vibrant rooftop bar in the Medina offering panoramic sunset views and international dishes.",
    "Taberna12": "Convivial Spanish tapas bar in Gueliz serving authentic paella, sangria, and live DJ sets.",
    "Tanjia secrets": "Intimate restaurant specializing in the slow-cooked Marrakesh signature dish Tanjia.",
    "Wall Marrakech": "Historic city ramparts surrounding the Medina, an architectural landmark of Marrakesh.",

    # MARSEILLE
    "Absolem Marseille": "Lively festive bar with Latino vibes, salsa classes, and creative cocktails.",
    "Address Ateliers De Pâtisserie": "Creative pastry workshop offering hands-on baking classes with professional chefs.",
    "Aslan Kadaifs Pâtisserie": "Inviting pastry shop specializing in authentic Turkish kunefe, baklava, and warm hospitality.",
    "Bar Odéon": "Classic bar with a serene atmosphere, perfect for a quiet coffee or drink.",
    "Bar de L Est": "Bohemian neighborhood bar with a warm community spirit and affordable drinks.",
    "Café Barbotyne": "Cozy ceramic art cafe offering a calm space for painting and enjoying sweet treats.",
    "Café Lauca « La Boutchica »": "Charming artisan coffee shop roasting its own beans and serving exceptional flat whites."
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

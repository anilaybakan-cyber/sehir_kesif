
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # HONG KONG
    "Underpass Restaurant & Bar": "Cozy Tin Hau spot serving creative cocktails and diverse bar bites including Nepalese specialties.",
    "Yardleys Taproom": "Vibrant craft beer haven offering innovative brews and Western-Cantonese comfort food like smoked pork.",
    "ztoryhome": "Storytelling-themed cafe and gallery serving comforting udon and seasonal cakes in a peaceful setting.",

    # ISTANBUL
    "Cafe bianchi": "Highly-rated cafe in Fatih known for its excellent coffee and warm, welcoming service.",
    "Coffeebul": "Late-night cafe in Fatih offering a wide variety of coffee drinks and desserts in a warm atmosphere.",
    "D'amour Patisserie İstanbul": "Elegant patisserie offering a rich selection of cheesecakes, brownies, and freshly baked croissants.",
    "LUFFY PATISSERIE": "Creative dessert shop specializing in delicious profiteroles, eclairs, and colorful strawberry magnolia pudding.",
    "Marlen Bar": "Intimate bar serving unique cocktails and hearty bar food in a relaxed, music-filled atmosphere.",
    "Pal Coffee": "Historic atmosphere built on ancient ruins, serving authentic Turkish cuisine and clay pot dishes.",
    "Posa Coffee Roastery": "Minimalist third-wave coffee roastery focused on high-quality pour-overs and single-origin beans.",
    "Rivolta Caffé": "Classic coffeehouse offering quality espresso drinks and a relaxed vibe for a casual break.",
    "The Legacy Irish Pub": "Authentic Irish pub with a lively atmosphere, live music, and classic dishes like shepherd's pie.",

    # CAPPADOCIA
    "Yeşilöz Köyü": "Tranquil village featuring the historic T-shaped Tagar Church and authentic local cuisine at the inn.",

    # COPENHAGEN
    "Geranium": "World-renowned restaurant offering a nature-inspired tasting menu with panoramic park views and minimalist decor.",
    "The Coffee Collective": "Scandinavian specialty coffee pioneer roasting light, acidic beans in a warm, hygge-filled atmosphere."
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

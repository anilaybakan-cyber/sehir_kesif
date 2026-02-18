
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # LONDON
    "Colonna & Small's": "Minimalist sleek coffee shop serving exceptional curated specialty coffee and delicious pastries.",
    "Filo": "Vibrant Brazilian restaurant serving grilled picanha and authentic feijoada in a stylish setting.",
    "OMA": "Greek-inspired restaurant in Borough Market offering innovative dishes and a lively open-kitchen vibe.",
    "Osteria Fiorentina": "Authentic Tuscan spot in Chelsea serving classic Bistecca alla Fiorentina and handmade pasta.",
    "Scales Cocktail Bar": "Intimate, hidden Mayfair bar creating modernist, science-driven cocktails in a chic atmosphere.",
    "The Chocolate Cocktail Club": "Unique bar specializing in creative chocolate cocktails and sweet treats in a cozy setting.",
    "Tosi Gorgonzola": "Sophisticated bar in Mayfair dedicated to artisanal Gorgonzola cheese and fine wine pairings.",

    # LUCERNE
    "Babalas Bar": "Calm and relaxing bar near Alpineum known for spectacular service and comfort food.",
    "Bar León": "Cozy Spanish wine bar offering authentic tapas and a great selection of regional wines.",
    "Bäckerei Macchi": "Convenient and friendly bakery near the train station serving fresh Swiss pastries and quiche.",
    "Café Dahinden": "Historic lakeside cafe in Weggis offering homemade cakes and breathtaking mountain views.",
    "Kuchenhaus Annamelie": "Homey spot known for tasty homemade pies, fruitcakes, and friendly service.",
    "Macchi Bakery": "Popular central bakery offering a warm atmosphere and a variety of fresh artisan breads.",
    "Raedwulf Pub": "Cozy Scottish-style pub with a huge whiskey selection and regular live music.",
    "Restaurant Don Feri": "Pleasant restaurant serving Mediterranean cuisine with Spanish and Italian influences in a designed space."
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

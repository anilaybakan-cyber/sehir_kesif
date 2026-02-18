
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MADRID
    "Kon Kafé - Specialty Coffee": "Comfortable specialty coffee spot offering precision brews and light bites in a quaint setting.",
    "LICENSED specialty coffee": "Cozy, dog-friendly coffee shop serving exceptional brews in a calm, inviting atmosphere.",
    "La Cucharona - Comida casera para llevar": "Homestyle takeaway spot known for comforting dishes prepared with a mother's touch.",
    "La Dulcería Café |Tartas de Queso Artesanas|Specialty Cheesecakes. Desserts-Postres": "Cozy dessert cafe famous for its variety of artisanal cheesecakes and specialty coffee.",
    "Lito Pastelería": "Modern Spanish pastry shop offering traditional desserts with a contemporary presentation.",
    "Loca Obsesión | Brunch Madrid": "Central brunch spot near Plaza Mayor known for creative, fun dishes and lively vibes.",
    "Lovo Cocktail Bar Madrid": "Chic 1920s-themed cocktail bar serving inventive drinks and tapas in a stylish setting.",
    "Madremia Retiro": "Charming spot near Retiro Park offering homemade flavors in a relaxed atmosphere.",
    "Madrid & Darracott - Vinos y experiencias": "Friendly wine shop hosting informative tastings of Spanish wines, sherry, and vermouth.",
    "Minos Pastry & Specialty coffee": "Retiro district gem offering artisanal pastries, cinnamon rolls, and a wide range of specialty coffees.",
    "Momento Café": "Romantic and cozy cafe serving pies, empanadas, and specialty coffee in a quiet setting.",
    "MrWay - Specialty Coffee, Brunch & Cocktails": "Highly-rated spot offering a seamless blend of specialty coffee, hearty brunch, and cocktails.",
    "Nini’s Bakery": "Popular bakery delivery service known for creamy cheesecakes and freshly baked cookies.",
    "Norah Barrio Salamanca | Brunch Madrid": "Mediterranean-inspired brunch spot with charming decor, serving eggs benedict and specialty coffee.",
    "SAMBHAD the cocktail bar": "Artistic cocktail bar in Centro with a lively terrace and innovative mixology."
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

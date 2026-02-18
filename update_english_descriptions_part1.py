
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # AMSTERDAM
    "Morning Owl Coffee": "Cozy cafe serving locally roasted specialty coffee, matcha lattes, and fresh pastries in a warm atmosphere.",
    "La Dilettante Amsterdam - Natural Wine Bar": "Laid-back natural wine bar offering curated wines and small seasonal bites in a friendly setting.",
    "Madame Croissant Amsterdam": "Charming bakery specializing in buttery, crispy croissants with unique sweet and savory fillings.",
    "Rebel Wines": "Independent wine shop focusing on small-scale, low-intervention natural wines from overlooked regions.",
    "The Brokers Bar": "Refined yet energetic bar in a historic building, serving botanical cocktails and Nikkei cuisine.",
    "The Wine Spot": "Inviting wine shop offering a curated selection of Portuguese and natural wines with expert tastings.",
    "Vindict Wine": "Lively wine bar and shop with a vast selection of European wines and a lovely terrace.",

    # DUBLIN
    "The Wine Pair": "Casual neighborhood wine bar specializing in organic and biodynamic wines paired with cheese and charcuterie.",
    "Upside Coffee Roastery": "Passionate roastery offering extraordinary small-batch coffee blends and freshly baked goods in a friendly cafe.",

    # FLORENCE
    "FLUID - Specialty Coffee & Sharing": "Vibrant and modern coffee shop serving diverse specialty brews, creative pastries, and an all-day menu.",
    "Osteria Vecchio Cancello": "Authentic restaurant resembling an eclectic home, serving traditional Tuscan dishes and Florentine steak.",
    "Osteria dei Leoni Firenze": "Warm and lively osteria famous for its Bistecca alla Fiorentina and classic Tuscan specialties.",
    "Pasticceria Buonamici": "Family-owned historic bakery known for traditional Florentine pastries, artisanal croissants, and fresh cantucci.",
    "Ristorante La Gioia Toscana": "Welcoming restaurant offering authentic Tuscan flavors, homemade pasta, and excellent steak in a pleasant setting.",
    "Taverna Dei Servi Firenze": "Classy yet cozy tavern near the Duomo, serving modern takes on traditional Tuscan cuisine."
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

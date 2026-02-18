
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # LUCERNE
    "Restaurant Scala": "Elegant dining with panoramic Alpine views, serving fresh Mediterranean cuisine and fine wines.",
    "Salvatore Icilio La Bottega Del Buongustaio": "Authentic Italian deli and bistro offering fresh pasta, Sicilian specialties, and warm hospitality.",
    "Wirtshaus Taube Luzern": "Charming historic riverside inn serving traditional Swiss classics with a modern twist.",

    # LYON
    "Anahera": "Inviting urban oasis offering healthy superfood bowls, vegan pastries, and specialty coffee.",
    "Bonomia Boulangerie": "Charming bakery famous for organic sourdough, cinnamon buns, and creative baked goods.",
    "Boulangerie L'Artisan (Maison Dumollard)": "Local favorite for freshly baked organic breads, pastries, and delicious sandwiches.",
    "Boulangerie Les Frères Barioz": "Passionate artisan bakery renowned for exceptional croissants, seasonal tarts, and organic breads.",
    "Cigale": "Chic Art Deco bar specializing in creative gin cocktails in a relaxed setting.",
    "Duclef Café Pâtisserie": "Cozy vintage-style cafe serving modern pastries, specialty coffee, and homemade savory dishes.",
    "GRANIT Bar à Vins": "Lively neighborhood wine bar with a curated natural wine list and sharing plates.",
    "La Baignoire": "Intimate speakeasy with 1920s decor, creating unique cocktails and gourmet tapas.",
    "La Beer Fabrique - Atelier bière et microbrasserie": "Interactive microbrewery workshop offering brewing classes and craft beer tastings.",
    "Le Rancard : Coffee shop - Brunch - Laverie": "Unique concept combining a cozy cafe, brunch spot, and laundromat in one.",
    "Le Starck bar": "Festive spot for after-work drinks, burgers, and tapas with a lively terrace."
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


import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MARSEILLE
    "Carry Nation": "Authentic Prohibition-era speakeasy serving expert cocktails in a hidden, intimate setting.",
    "Chapati baille @ l'original": "Cozy spot serving Tunisian chapatis, pizzas, and grilled cheese in a friendly atmosphere.",
    "Coquetel Club - Bar à Manger et Cocktails - Marseille 6": "Trendy bar à manger serving cocktails, French charcuterie boards, and homemade tartines.",
    "Dionysos": "Vibrant bar with a festive atmosphere, known for signature cocktails and bruschettas.",
    "Fuella Nera": "Charming organic wine bar offering biodynamic wines and homemade focaccia in a relaxed setting.",
    "GRIGNE CAFÉ": "Inviting coffee shop serving specialty coffee, pastries, and light meals in a cozy space.",
    "Josie café": "Bright and cozy cafe in La Plaine serving specialty coffee, matcha, and homemade cakes.",
    "KRM café galerie": "Warm art cafe and gallery offering coffee, tea, and cultural events in Noailles.",
    "La Cosca": "Italian tapas bar with a warm atmosphere, specializing in natural wines and antipasti.",
    "La Movida": "Lively Spanish tapas restaurant with a festive vibe, serving croquetas and sangria.",
    "Le Balagan": "Friendly vegetarian bistro serving colorful, seasonal plant-based dishes with Scandinavian decor.",
    "Les Jardins de Tanin Natural Wine Club": "Natural wine club and bar dedicated to biodynamic wines and terroir-focused tastings.",
    "Mauvaise Herbe - Bistrot Café Végétal Marseille": "Plant-based bistro offering seasonal Provençal cuisine and sourdough tartines in a warm setting.",
    "Mercato X Winesucker": "Cozy vegetarian restaurant and wine bar serving natural wines and Mediterranean comfort food.",
    "Mostera Concept Store": "Charming concept store and cafe offering specialty coffee, plants, and curated lifestyle goods."
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

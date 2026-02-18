
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # MARRAKESH
    "FOLK MARRAKECH": "Vibrant restaurant blending traditional Moroccan cuisine with live Gnaoui music and art.",
    "Fish house Al Aachabe": "Warm and pleasant seafood spot specializing in fresh grilled fish and tagines.",
    "HESPERIS Coffee Factory": "Elegant specialty coffee house and artisanal restaurant fusing Moroccan heritage with modern luxury.",
    "HeiBai Speciality Coffee 黑白": "Cozy Japanese-style cafe offering exceptional specialty coffee and unique matcha drinks.",
    "Kesh cup Marrakech": "Charming Medina cafe serving spiced Moroccan coffee and plant-based options in a stylish setting.",
    "LE MECANO": "Automotive-themed bar with a lively atmosphere, motorcycles on walls, and great cocktails.",
    "La Cueva restaurant bar à tapas": "Festive tapas bar offering sangria, international cuisine, and nightly live music.",
    "La Pergola & Le bistro Arabe": "Rooftop garden spot serving Moroccan street food, jazz, and creative cocktails with Medina views.",
    "La Table Berbère": "Authentic restaurant within a Riad offering traditional Berber cuisine in a family-friendly setting.",
    "Le Slimana Restaurant & Rooftop": "Luxurious Riad dining with a panoramic rooftop, serving Moroccan fusion cuisine and sunsets.",
    "MK ROOFTOP Marrakech - FOOD & COCKTAILS": "Trendy rooftop bar offering 360-degree views, gourmet tapas, and premium cocktails.",
    "Manso Bar": "Cozy lounge at Mövenpick Hotel offering sunset views, live jazz, and refreshing cocktails.",
    "Moroccan Teahouse Restaurant - 1112 Marrakech": "Immersive teahouse in a beautiful courtyard serving traditional teas and Moroccan pastries.",
    "Oban": "Scottish whisky bar offering a selection of premium spirits in a refined setting.",
    "Petanque Social Club": "Nostalgic Art Deco venue with a garden, pétanque court, and French-Mediterranean menu."
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

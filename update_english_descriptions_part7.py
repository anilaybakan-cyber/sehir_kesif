
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # LYON
    "Magma Coffee shop": "Charming coffee shop serving Mediterranean-style breakfast and strong seasonal coffee.",
    "Puzzle Cafe": "Modern eco-friendly cafe serving specialty coffee from local roasters and healthy bites.",
    "Regain restaurant LYON": "Casual yet refined restaurant blending modern culinary techniques with traditional French flavors.",
    "Repère(s)": "Vibrant bar and tour venue offering local food boards and original cocktails.",
    "STEPPE BAR": "Trendy Asian-themed bar serving homemade gyoza, sushi, and innovative cocktails on a terrace.",
    "Skull Lyon - Bar à cocktails immersif": "Immersive steampunk cocktail bar serving creative drinks and snack platters in a whimsical setting.",
    "Soif !": "Retro-gaming wine bar offering sharing tapas, artisanal products, and a massive wine list.",
    "you cocktail bar": "Chic and lively bar famous for perfume-inspired cocktails and a warm, welcoming vibe.",

    # MADRID
    "Alchemist 1967": "High-end cocktail bar serving sophisticated drinks paired with innovative gastronomic creations.",
    "Botequim Brunch & Tapas Bar": "Lively spot popular for its Brazilian-inspired brunch and energetic tapas atmosphere.",
    "Cinco Hileras Café": "Quaint and comfortable cafe serving specialty coffee and a variety of light bites.",
    "Despacito Specialty Coffee - Café Especialidad": "Minimalist and tranquil cafe known for rich, nutty specialty coffee and baked goods.",
    "Devil’s Cut": "Moody, upscale cocktail bar combining sherry-based drinks with precise Izakaya-style bites.",
    "Dumpling House, Restaurante de empanadillas chinas": "Casual, warm spot specializing in handmade Chinese dumplings and empanadillas.",
    "Jack´s Club": "Intimate, seductive bar with a speakeasy vibe, live jazz, and storytelling cocktails."
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

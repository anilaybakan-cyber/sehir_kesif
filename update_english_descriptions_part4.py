
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # LISBON
    "Black Pavilion Restaurant": "Chic restaurant offering sophisticated, comforting dishes with Mediterranean touches and stunning city views.",
    "Casa de Dura": "Welcoming local favorite serving fabulous traditional Portuguese meals in an exotic setting.",
    "Fusion Grill": "Warm and cozy spot serving fresh Lebanese and Mediterranean specialties like falafel and kebabs.",
    "Gorgulho": "Exotic bakery known for fresh bread, focaccia, and cinnamon rolls served with patience.",
    "Kiosk Cafe": "Charming, book-filled sanctuary for coffee lovers, serving hearty brunches and homemade cakes.",
    "Listambul": "Unique Turkish-Portuguese fusion restaurant in a historic building offering authentic mezze and ribs.",
    "Mercearia do Século": "Intimate home-style bistro serving fresh, organic Portuguese dishes with refined presentation.",
    "O Tapas": "Authentic Portuguese tapas restaurant offering generous portions of sharing plates in a cozy setting.",
    "Orioli Coffee": "Cozy specialty coffee lab serving expert brews, fresh croissants, and banana bread.",
    "Tapa do BairroAlto": "Modern tapas spot in Bairro Alto serving diverse Spanish snacks in a friendly atmosphere.",
    "The Queen Ale": "Independent craft beer bar with a rustic-modern vibe, serving IPAs and tasty bar snacks.",
    "romana. specialty coffee": "Small, cozy espresso bar offering high-quality specialty coffee and light bites like toasts.",

    # LONDON
    "Bantof": "Vibrant Soho dining spot with 1920s glamour, serving creative Mediterranean sharing plates.",
    "Beverly Hills Bakery (Delivery only)": "Established American bakery famous for fresh muffins, cookies, and cakes, primarily for delivery.",
    "Cafe Parisienne": "Charming local cafe in Clapham Junction, popular for all-day brunch and Turkish sweets."
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


import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # NICE
    "l'Antidote - Restaurant - Bar à cocktails - Cuisine locale de saison": "Modern French restaurant offering creative Mediterranean-inspired world cuisine in a cozy, intimate setting.",
    "ÉBURNIE COFFEE CULTURE": "Artisanal coffee house celebrating African culture with premium beans and warm, inviting hospitality.",

    # OSLO
    "Kulturhuset": "Multi-level cultural hub and cafe serving fresh plant-based cuisine and artisan coffee since years.",
    "Paradisbukta Plajı": "Quiet and family-friendly sandy beach in a scenic bay, perfect for summer relaxation.",
    "Åpent Bakeri - Barcode": "Renowned bakery offering handmade organic breads, traditional cinnamon rolls, and specialty coffee in Barcode.",

    # STOCKHOLM
    "Abba The Müzesi": "Interactive museum celebrating ABBA, featuring a pop-themed cafe with traditional Swedish treats.",

    # STRASBOURG (Strazburg)
    "MAMCS (Modern Sanat Müzesi)": "Modern art museum with a glass-walled cafe offering stunning River Ill views.",

    # ZERMATT
    "Indoor Golf Zermatt": "Modern facility offering high-end golf simulators and a relaxed atmosphere for indoor sports practice.",
    "Kushion": "Stylish lounge offering a cozy setting for shisha, creative cocktails, and relaxed evening socializing.",
    "Madre Nostra": "Michelin-selected Italian restaurant serving refined classics and modern creations with spectacular Matterhorn views.",
    "Matterhorn Trail": "Iconic hiking path offering breathtaking Matterhorn views and access to rustic alpine mountain restaurants.",
    "Peak Performance": "Sophisticated restaurant offering winter truffles, mountain specialties, and upscale alpine dining in Zermatt.",
    "Restaurant Julen": "Traditional Swiss restaurant famous for Valaisan lamb specialties and cozy wood-fired grill ambiance.",
    "Sparky's Bar": "Informal Asian-international bar and restaurant known for a relaxed vibe and friendly social setting.",
    "Sunnegga": "Sunny mountain terrace offering traditional alpine specialties and premium Valais wines with iconic views.",
    "Swiss Chalet": "Authentic rustic chalet serving traditional cheese fondue and raclette in a historic wooden setting.",
    "Theodul Pass": "High-altitude mountain pass offering international specialties and panoramic glacier views at 3,300 meters.",
    "Vis-à-Vis": "Refined hotel restaurant at Gornergrat serving classic regional dishes with stunning alpine panoramas.",
    "Zermatt Unplugged": "Intimate acoustic music festival featuring a Taste Village with local gourmet delights and chalets.",
    "Zmutt Dam": "Hearty mountain eatery in a traditional hamlet serving traditional rösti amidst green meadows."
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


import json
import os
import glob
import re

# Dictionary of updates: Key = Place Name, Value = New English Description
UPDATES = {
    # OTTAWA / ISTANBUL
    "The Ottomans Kitchen Cafe Restaurant": "Authentic Ottoman Palace Cuisine with historical recipes near Hagia Sophia.",
    "The Rabbit Hole Coffee Sultanahmet": "Cozy escape in Sultanahmet serving Turkish breakfast and specialty coffee.",
    "Sector Cocktail Bar": "Vibrant cocktail bar with innovative mixology and delicious bar bites.",
    "Spresso Co Roastery Coffee": "Artisanal coffee roastery in a historic Balat building with Golden Horn views.",
    
    # AMSTERDAM
    "Morning Owl Coffee": "Specialty coffee sanctuary celebrating Dutch coffee culture with rotating roasters.",
    "Rebel Wines": "Natural wine shop featuring small-scale, low-intervention wines.",
    "The Brokers Bar": "Energetic bar serving Pisco cocktails and Nikkei cuisine like ceviche.",
    
    # BRUSSELS
    "Aux Merveilleux de Fred": "Artisan patisserie famous for cloud-light meringue 'Merveilleux' cakes.",
    
    # HONG KONG
    "ORKA Restaurant & Bar": "Wellness-focused restaurant offering sustainable, healthy, and organic dishes.",
    
    # COPENHAGEN
    "The Coffee Collective": "World-renowned roastery offering exceptional single-origin specialty coffee.",
    
    # LISBON
    "Cascavel": "Stylish cocktail bar with retro 80s aesthetics and creative drinks.",
    "Lisbonita Restaurante": "Cozy restaurant serving fresh Italian-inspired seafood and pasta dishes.",
    
    # LUCERNE
    "Glutenfreie Brotwerkstatt": "100% gluten-free bakery offering fresh artisan breads and pastries.",
    "Hinicht": "Modern bar and club, perfect for nightlife and social drinks.",
    "Melissa's Kitchen": "Swiss cuisine restaurant with extensive daily brunch and local products.",
    "tschuppi's wonderbar": "Vibrant sports and culture bar with live music and drinks.",
    "Äss-Bar": "Sustainable bakery fighting food waste with yesterday's fresh goods.",
    
    # LYON
    "Bacchanales, restaurant gastronomique.": "Creative gastronomic cuisine in a romantic 17th-century setting.",
    "Cuisiné Sensée et Inspirée": "Healthy, inspired cuisine using fresh ingredients and innovative cooking.",
    
    # MADRID
    "Santo Bakehouse": "Artisan bakery known for high-quality sourdough and delicious pastries.",
    "Vinoteca La Cristalería": "Historic wine bar offering curated wines and gourmet tapas.",
    
    # MARRAKESH
    "BAROMETRE MARRAKECH": "Speakeasy-style bar with creative mixology and Mediterranean fusion tapas.",
    "Cocktail La Poterne": "Relaxed spot for breakfast sandwiches, fresh juice, and coffee.",
    "SAVOR Coffee Shop": "Minimalist specialty coffee shop with great matcha and smoothies.",
    "So Lounge Marrakech": "Chic nightlife venue with Asian-Moroccan fusion dining and live music.",
    
    # MARSEILLE
    "Delices du port": "Sweet and savory crêpes and waffles in a casual setting.",
    "Mauvaise Herbe - Bistrot Café Végétal Marseille": "100% plant-based bistro with seasonal, Mediterranean-inspired dishes.",
    "Naima Cake": "Custom cake bakery creating exquisite desserts for special occasions.",
    "Succulentes Cafe": "Cozy, plant-filled cafe serving healthy food and specialty drinks.",
    
    # MILANO
    "Goccetto": "Intimate wine bar with rustic charm and authentic Italian small plates.",
    "Grappo Lambro": "Jovial enoteca offering wines, grappa, and cultural events.",
    "Marea Seafood & Beverage": "Elegant seafood restaurant with innovative dishes and fine wines.",
    "Raboucer": "Trendy bar with vinyl-record cocktails and a lively atmosphere.",
    "Remedy Wine & Spirits Milano": "Refined wine bar with an extensive selection and professional service.",
    "Vineria Cardenzia #diversamente buoni": "Rustic wine bar with unique jams, cheeses, and authentic vibes.",
    
    # NAPOLI
    "Bar Fantasy di Chierchia Antonio": "Welcoming cafe known for exceptional coffee and professional friendly staff.",
    "Bar del Chiostro": "Peaceful bar near San Francesco offering breakfast and aperitivo.",
    "Nineteen 19 Bar": "Charming cocktail bar with creative drinks and a warm vibe.",
    "Quesse cocktail bar": "Mixology-focused bar where every cocktail tells a flavor story.",
    
    # NEW YORK
    "Current Coffee": "Vibrant coffee shop with diverse roasts and honey oat lattes.",
    "Drinkology NYC": "Sophisticated cocktail bar with modern American cuisine and artful drinks.",
    "Everything's Jake NYC Bar & Lounge": "Speakeasy-style lounge with vintage vibes and craft cocktails.",
    "Noise NYC": "Cannabis-focused shop with a chill lounge atmosphere and music.",
    "The Townhouse Cafe": "Charming cafe with a skylit patio, perfect for work or relaxing.",
    
    # NICE
    "Coffee shop - La Brioche Chaude - CAFÉ": "Cozy cafe with Notre-Dame views, homemade pastries, and rich coffee.",
    "Original Pub Crawl Nice": "Lively guided tour through Nice's best bars and nightclubs.",
    
    # ZERMATT
    "Brown Cow Pub": "Casual pub serving Swiss burgers, beers, and all-day breakfast.",
    "Charles Kuonen Asma Köprüsü": "World's longest pedestrian suspension bridge offering thrilling Alpine views.",
    "Golf Club Matterhorn": "Scenic 9-hole golf course with panoramic views of the Breithorn.",
    "Grampi's Bar": "Cozy Italian restaurant and bar famous for wood-fired pizzas.",
    "Helicopter Tour": "Unforgettable flight experience with spectacular views of the Matterhorn.",
    "Hinterdorf (Eski Köy)": "Historic part of Zermatt featuring preserved 16th-century wooden buildings.",
    "Igloo Village Zermatt": "Unique ice hotel and bar with fondue and snow sculptures.",
    "Kayak & Snowboard": "Year-round winter sports paradise with extensive slopes for all levels.",
    "Migros Supermarket": "Large supermarket offering fresh groceries and daily essentials.",
    "Murmeli Brunnen": "Charming Marmot Fountain located in Zermatt's historic church square.",
    "Paragliding Zermatt": "Tandem paragliding flight offering breathtaking aerial views of the Alps.",
    "Rothorn Paradise": "Mountain restaurant with panoramic views and traditional Alpine cuisine.",
    "Wolli's Adventure Parkı": "Family-friendly adventure park at Sunnegga with playground and lake.",
    "Zermatt Spor Dükkanları": "Premium sports shop for ski rental and outdoor equipment.",
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
                
                if name in UPDATES:
                    # Update English description
                    place['description_en'] = UPDATES[name]
                    file_changed = True
                    total_updated += 1
                    # print(f"Updated {name} in {city_name}")
            
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal English descriptions updated: {total_updated}")

if __name__ == "__main__":
    main()


import json
import random

# --- CONFIGURATION ---
PRAG_JSON_PATH = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/prag.json'
ROUTE_OUTPUT_PATH = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/routes/prag.json'

def main():
    print("🚀 Generating Route for Prague OTA...")

    # 1. Load the FULL verified venue list
    try:
        with open(PRAG_JSON_PATH, 'r', encoding='utf-8') as f:
            city_data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading city data: {e}")
        return

    highlights = city_data.get('highlights', [])
    
    # Filter for the new venues (those with Firebase URLs are a good proxy, or just 'source': 'firebase_ota')
    # actually, why valid existing venues too?
    # Let's create a "New Discoveries" route with the BEST of the new ones.
    
    new_venues = [h for h in highlights if h.get('source') == 'firebase_ota']
    print(f"Found {len(new_venues)} new venues.")
    
    if not new_venues:
        print("⚠️ No new venues found to add to route. Check prag.json source fields.")
        # Fallback: take last 50
        new_venues = highlights[-54:]

    # Create a "Mega Route" or split into categories
    # Let's make one comprehensive "New Season Discoveries" route
    
    # We need to pick ~10-15 best ones or the route UI might lag? No, list view is fine.
    # Let's pick 20 distinctive ones.
    
    selected_venues = new_venues[:20] 
    
    place_names = [h['name'] for h in selected_venues]
    
    new_route = {
        "id": "prag_new_2026",
        "name": {
            "en": "New Season Discoveries",
            "tr": "Yeni Sezon Keşifleri"
        },
        "description": {
            "en": "Explore the freshest cafes, bars and hidden gems added for the new season.",
            "tr": "Yeni sezon için eklenen en taze kafeler, barlar ve gizli durakları keşfedin."
        },
        "duration": {
            "en": "2 Days",
            "tr": "2 Gün"
        },
        "distance": "15 km",
        "difficulty": {
            "en": "Easy",
            "tr": "Kolay"
        },
        "imageUrl": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/prag/bruxx.jpg", # Use a verified one
        "tags": {
            "en": ["New", "Foodie", "Hidden Gems"],
            "tr": ["Yeni", "Gurme", "Gizli Cevher"]
        },
        "placeNames": place_names, # This relies on names matching exactly
        "interests": {
            "en": ["Food", "Culture"],
            "tr": ["Yemek", "Kültür"]
        },
        "accentColor": "0xFFE91E63",
        "icon": "Icons.explore_rounded"
    }
    
    # output list of routes
    routes_list = [new_route]
    
    # Ensure dir exists
    import os
    os.makedirs(os.path.dirname(ROUTE_OUTPUT_PATH), exist_ok=True)
    
    with open(ROUTE_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(routes_list, f, indent=2, ensure_ascii=False)
        
    print(f"✅ Generated {ROUTE_OUTPUT_PATH} with 1 route containing {len(place_names)} stops.")

if __name__ == "__main__":
    main()

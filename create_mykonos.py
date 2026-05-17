from dotenv import load_dotenv
load_dotenv()
import json
import requests
import time
import os
from typing import List, Dict

# Config
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITY_NAME = "Mykonos"
CITY_ID = "mykonos"
OUTPUT_PATH = f"assets/cities/{CITY_ID}.json"

# Skeleton list of 50+ top places
MYKONOS_VENUE_NAMES = [
    "Little Venice Mykonos", "Kato Mili Windmills", "Panagia Paraportiani", 
    "Delos Island", "Armenistis Lighthouse", "Matoyianni Street", "Mykonos Town (Chora)",
    "Ano Mera", "Mykonos Old Port", "Mykonos New Port", "Vioma Organic Farm",
    "Psarou Beach", "Paradise Beach Mykonos", "Super Paradise Beach", "Nammos", 
    "Scorpios Mykonos", "Jackie O' Beach Club", "Principote Mykonos", "Alemagou", 
    "Kalafati Beach", "Elia Beach", "Ornos Beach", "Panormos Beach", "Agios Sostis Beach",
    "Lia Beach", "Ftelia Beach", "Kalo Livadi Beach", "Kiki's Tavern", "Spilia Restaurant", 
    "Sea Satin Market", "Mamalouka Mykonos", "Interni Restaurant", "Remezzo Mykonos", 
    "Uno Con Carne", "M-eating Mykonos", "Buddha-Bar Beach", "Beefbar Mykonos", "SantAnna",
    "Cavo Paradiso", "Toy Room Mykonos", "Nusr-Et Mykonos", "Zuma Mykonos", "Lio Mykonos",
    "Bonbonniere Mykonos", "180 Sunset Bar", "Boni's Windmill", "Archaeological Museum of Mykonos",
    "Lena's House", "Rarity Gallery", "Scandinavian Bar", "Breeze Cocktail Bar"
]

def search_place(name: str, city: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": f"{name} {city} Greece", "key": API_KEY, "language": "en"}
    try:
        r = requests.get(url, params=params)
        data = r.json()
        if data.get("results"): return data["results"][0]
    except Exception as e: print(f"Error searching {name}: {e}")
    return None

def nearby_search(lat, lng, radius, type_filter):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {"location": f"{lat},{lng}", "radius": radius, "type": type_filter, "key": API_KEY, "language": "en"}
    try:
        r = requests.get(url, params=params)
        return r.json().get("results", [])
    except Exception as e: print(f"Error nearby {type_filter}: {e}")
    return []

def get_details(place_id: str):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {"place_id": place_id, "key": API_KEY, "language": "en", "fields": "name,rating,user_ratings_total,geometry,photos,formatted_address,editorial_summary,types,price_level"}
    try:
        r = requests.get(url, params=params)
        return r.json().get("result")
    except Exception as e: print(f"Error details {place_id}: {e}")
    return None

def process_place(place_json, highlights, found_ids):
    pid = place_json.get("place_id")
    if not pid or pid in found_ids: return
    
    details = get_details(pid)
    if not details: return
    
    found_ids.add(pid)
    loc = details.get("geometry", {}).get("location", {})
    name = details.get("name", "Unknown")
    
    photo_url = ""
    if details.get("photos"):
        ref = details["photos"][0]["photo_reference"]
        photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={ref}&key={API_KEY}"
        
    desc_en = details.get("editorial_summary", {}).get("overview", "")
    if not desc_en: desc_en = f"{name} is a iconic spot in Mykonos. Perfect for exploration."
    
    # Mock Turkish for now, will enrich later
    desc_tr = f"{name}, Mikonos'un en sevilen yerlerinden biridir."
    
    category = "Deneyim"
    types = details.get("types", [])
    if "restaurant" in types or "food" in types: category = "Restoran"
    elif "museum" in types or "historical_landmark" in types: category = "Tarihi"
    elif "park" in types or "natural_feature" in types: category = "Park"
    
    h = {
        "id": pid, "name": name, "name_en": name, "category": category,
        "tags": ["mykonos", "greece", "luxury", "beach"], "lat": loc.get("lat"), "lng": loc.get("lng"),
        "rating": details.get("rating", 4.5), "reviewCount": details.get("user_ratings_total", 50),
        "price": "expensive", "imageUrl": photo_url, "description": desc_tr, "description_en": desc_en, "source": "google"
    }
    highlights.append(h)
    print(f"  ✅ Added: {name} ({category})")

def generate_mykonos_json():
    print(f"--- Generating {CITY_NAME} Data (Goal: 200) ---")
    found_ids = set()
    highlights = []
    
    for name in MYKONOS_VENUE_NAMES:
        print(f"Hardcoded: {name}...")
        search = search_place(name, CITY_NAME)
        if search: process_place(search, highlights, found_ids)
        if len(highlights) >= 200: break
        time.sleep(0.1)

    bases = [
        {"lat": 37.4467, "lng": 25.3289}, # Chora
        {"lat": 37.4150, "lng": 25.3430}, # Psarou
        {"lat": 37.4080, "lng": 25.3480}, # Paradise
        {"lat": 37.4480, "lng": 25.3950}  # Ano Mera
    ]
    categories = ["tourist_attraction", "restaurant", "cafe", "night_club", "museum"]
    
    if len(highlights) < 200:
        for base in bases:
            for cat in categories:
                print(f"Searching {cat} near {base}...")
                results = nearby_search(base["lat"], base["lng"], 5000, cat)
                for res in results:
                    process_place(res, highlights, found_ids)
                    if len(highlights) >= 200: break
                if len(highlights) >= 200: break
            if len(highlights) >= 200: break
            time.sleep(0.5)

    city_data = {
        "city": "Mikonos", "city_en": "Mykonos", "country": "Yunanistan", "country_en": "Greece",
        "description": "Ege denizinin en kozmopolit adası. Yel değirmenleri, labirent gibi sokakları olan Chora, dünya çapında ünlü plaj kulüpleri ve eşsiz gün batımlarıyla lüksün adresi.",
        "description_en": "The most cosmopolitan island of the Aegean. Chora with its windmills and labyrinthine streets, world-famous beach clubs, and unique sunsets—the address of luxury.",
        "heroImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/mykonos/hero.jpg",
        "coordinates": {"lat": 37.4467, "lng": 25.3289}, "highlights": highlights
    }
    
    os.makedirs("assets/cities", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Success: {len(highlights)} highlights.")

if __name__ == "__main__":
    generate_mykonos_json()

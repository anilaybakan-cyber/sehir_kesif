from dotenv import load_dotenv
load_dotenv()
import json
import requests
import time
import os
from typing import List, Dict

# Config
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITY_NAME = "Dubrovnik"
CITY_ID = "dubrovnik"
OUTPUT_PATH = f"assets/cities/{CITY_ID}.json"

# Skeleton list
DUBROVNIK_VENUE_NAMES = [
    "Dubrovnik City Walls", "Stradun", "Lovrijenac Fort", "Onofrio's Fountain",
    "Dubrovnik Cathedral", "Rector's Palace", "Sponza Palace", "Saint Blaise Church",
    "Dubrovnik Cable Car", "Mount Srd", "Lokrum Island", "Banje Beach", "Sveti Jakov Beach",
    "Lapad Beach", "Copacabana Beach Dubrovnik", "Cave Bar More", "Buža Bar", "Buža II",
    "Revelin Culture Club", "Dubrovnik Old Port", "Minčeta Tower", "Bokar Fortress",
    "St. John Fortress", "Maritime Museum Dubrovnik", "Ethnographic Museum Rupe",
    "Ancient Pharmacy", "Pile Gate", "Ploče Gate", "Gundulić Square", "Lazareti",
    "Trsteno Arboretum", "Pasjača Beach", "Elafiti Islands", "Šipan", "Koločep", "Lopud",
    "Panorama Restaurant & Bar", "Nautika Restaurant", "Restaurant Proto", "Kopun",
    "Lady Pi-Pi", "D'Vino Wine Bar", "Azur Dubrovnik", "PANTARUL", "Otto Taverna",
    "Gradska Kavana Arsenal", "Java Coffee Dubrovnik", "Cogito Coffee Dubrovnik"
]

def search_place(name: str, city: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": f"{name} {city} Croatia", "key": API_KEY, "language": "en"}
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
    if not desc_en: desc_en = f"{name} is a historic site in the heart of Dubrovnik. A jewel of the Adriatic."
    desc_tr = f"{name}, Dubrovnik'in Adriyatik kıyısındaki tarihi hazinelerinden biridir."
    
    category = "Tarihi"
    types = details.get("types", [])
    if "restaurant" in types or "food" in types: category = "Restoran"
    elif "park" in types or "natural_feature" in types: category = "Park"
    elif "museum" in types: category = "Müze"
    
    h = {
        "id": pid, "name": name, "name_en": name, "category": category,
        "tags": ["dubrovnik", "croatia", "adriatic", "historic"], "lat": loc.get("lat"), "lng": loc.get("lng"),
        "rating": details.get("rating", 4.5), "reviewCount": details.get("user_ratings_total", 50),
        "price": "medium", "imageUrl": photo_url, "description": desc_tr, "description_en": desc_en, "source": "google"
    }
    highlights.append(h)
    print(f"  ✅ Added: {name} ({category})")

def generate_dubrovnik_json():
    print(f"--- Generating {CITY_NAME} Data (Goal: 200) ---")
    found_ids = set()
    highlights = []
    
    for name in DUBROVNIK_VENUE_NAMES:
        print(f"Hardcoded: {name}...")
        search = search_place(name, CITY_NAME)
        if search: process_place(search, highlights, found_ids)
        if len(highlights) >= 200: break
        time.sleep(0.1)

    bases = [
        {"lat": 42.6403, "lng": 18.1083}, # Old Town
        {"lat": 42.6550, "lng": 18.0750}, # Lapad
        {"lat": 42.6620, "lng": 18.0720}  # Babin Kuk
    ]
    categories = ["tourist_attraction", "restaurant", "cafe", "night_club", "museum"]
    
    if len(highlights) < 200:
        for base in bases:
            for cat in categories:
                print(f"Searching {cat} near {base}...")
                results = nearby_search(base["lat"], base["lng"], 3000, cat)
                for res in results:
                    process_place(res, highlights, found_ids)
                    if len(highlights) >= 200: break
                if len(highlights) >= 200: break
            if len(highlights) >= 200: break
            time.sleep(0.5)

    city_data = {
        "city": "Dubrovnik", "city_en": "Dubrovnik", "country": "Hırvatistan", "country_en": "Croatia",
        "description": "Adriyatik'in incisi. UNESCO Dünya Mirası listesindeki surları, Game of Thrones sahnelerine ev sahipliği yapmış sokakları ve kristal berraklığındaki deniziyle büyüleyici bir Orta Çağ şehri.",
        "description_en": "The Pearl of the Adriatic. A mesmerizing medieval city with UNESCO World Heritage walls, streets that hosted Game of Thrones, and crystal-clear waters.",
        "heroImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubrovnik/hero.jpg",
        "coordinates": {"lat": 42.6403, "lng": 18.1083}, "highlights": highlights
    }
    
    os.makedirs("assets/cities", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Success: {len(highlights)} highlights.")

if __name__ == "__main__":
    generate_dubrovnik_json()

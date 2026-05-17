from dotenv import load_dotenv
load_dotenv()
import json
import requests
import time
import os
from typing import List, Dict

# Config
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITY_NAME = "Cesme"
CITY_ID = "cesme"
OUTPUT_PATH = f"assets/cities/{CITY_ID}.json"

# Skeleton list
CESME_VENUE_NAMES = [
    "Cesme Castle", "Alaçatı Çarşı", "Alaçatı Değirmenleri", "Cesme Marina", 
    "Ilıca Plajı", "Ayayorgi Koyu", "Altınkum Plajı", "Pırlanta Plajı", 
    "Dalyan Sahili", "Boyalık Plajı", "Paşalimanı", "Germiyan Köyü", "Ildır Antik Kenti (Erythrai)",
    "Delikli Koy", "Kleopatra Koyu", "Before Sunset Beach", "Fly-Inn Beach", 
    "Momo Beach Alacati", "Papazzo Beach", "Sole & Mare Beach Club", "Fun Beach Club",
    "Somera Beach", "Derya Beach", "Zio Beach", "Alaçatı Port", "Hacımemiş",
    "İmren Helva Tatlı", "Kumrucu Şevki", "Kumrucu Hüseyin", "Asma Yaprağı",
    "Babayanni", "Ferdi Baba Restaurant", "Kalamar Restaurant", "Horasan Balık pişiricisi",
    "Fava Alacati", "Agrilia", "Eflatun Alacati", "Kırmızı Ardıç Kuşu", "Dost Pide & Pizza",
    "Dondurmacı Veli Usta", "Köşe Kahve Alaçatı", "Sailors Coffee"
]

def search_place(name: str, city: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": f"{name} {city} Turkey", "key": API_KEY, "language": "tr"}
    try:
        r = requests.get(url, params=params)
        data = r.json()
        if data.get("results"): return data["results"][0]
    except Exception as e: print(f"Error searching {name}: {e}")
    return None

def nearby_search(lat, lng, radius, type_filter):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {"location": f"{lat},{lng}", "radius": radius, "type": type_filter, "key": API_KEY, "language": "tr"}
    try:
        r = requests.get(url, params=params)
        return r.json().get("results", [])
    except Exception as e: print(f"Error nearby {type_filter}: {e}")
    return []

def get_details(place_id: str):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {"place_id": place_id, "key": API_KEY, "language": "tr", "fields": "name,rating,user_ratings_total,geometry,photos,formatted_address,editorial_summary,types,price_level"}
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
        
    desc_tr = details.get("editorial_summary", {}).get("overview", "")
    if not desc_tr: desc_tr = f"{name}, Çeşme ve Alaçatı'nın en keyifli noktalarından biridir."
    desc_en = f"{name} is a top spot in Cesme and Alacati. Great for holidays."
    
    category = "Deneyim"
    types = details.get("types", [])
    if "restaurant" in types or "food" in types: category = "Restoran"
    elif "museum" in types or "historical_landmark" in types: category = "Tarihi"
    elif "park" in types or "natural_feature" in types: category = "Park"
    
    h = {
        "id": pid, "name": name, "name_en": name, "category": category,
        "tags": ["cesme", "alacati", "beach", "summer"], "lat": loc.get("lat"), "lng": loc.get("lng"),
        "rating": details.get("rating", 4.5), "reviewCount": details.get("user_ratings_total", 50),
        "price": "medium", "imageUrl": photo_url, "description": desc_tr, "description_en": desc_en, "source": "google"
    }
    highlights.append(h)
    print(f"  ✅ Added: {name} ({category})")

def generate_cesme_json():
    print(f"--- Generating {CITY_NAME} Data (Goal: 200) ---")
    found_ids = set()
    highlights = []
    
    for name in CESME_VENUE_NAMES:
        print(f"Hardcoded: {name}...")
        search = search_place(name, CITY_NAME)
        if search: process_place(search, highlights, found_ids)
        if len(highlights) >= 200: break
        time.sleep(0.1)

    bases = [
        {"lat": 38.3228, "lng": 26.3079}, # Cesme Center
        {"lat": 38.2817, "lng": 26.3742}, # Alacati
        {"lat": 38.3500, "lng": 26.3117}  # Dalyan
    ]
    categories = ["tourist_attraction", "restaurant", "cafe", "night_club"]
    
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
        "city": "Çeşme", "city_en": "Cesme", "country": "Türkiye", "country_en": "Turkey",
        "description": "Ege'nin sörf ve eğlence merkezi. Tarihi taş evleriyle Alaçatı, turkuaz sularıyla Ilıca, Ayayorgi'nin ünlü beach clubları ve sakız ağaçlarıyla bezeli eşsiz bir sahil kasabası.",
        "description_en": "The center of surfing and entertainment in the Aegean. A unique coastal town with Alacati's historic stone houses, Ilıca's turquoise waters, and Ayayorgi's famous beach clubs.",
        "heroImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cesme/hero.jpg",
        "coordinates": {"lat": 38.3228, "lng": 26.3079}, "highlights": highlights
    }
    
    os.makedirs("assets/cities", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Success: {len(highlights)} highlights.")

if __name__ == "__main__":
    generate_cesme_json()

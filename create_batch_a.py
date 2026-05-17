from dotenv import load_dotenv
load_dotenv()
import json
import requests
import time
import os
from typing import List, Dict

# Config
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

CITIES = [
    {"id": "ibiza", "name": "Ibiza", "country": "İspanya", "country_en": "Spain", "coords": (38.9067, 1.4206), "hardcoded": ["Dalt Vila", "Es Vedra", "Cafe del Mar", "Ushuaia Ibiza", "Pacha Ibiza", "Amnesia Ibiza", "Cala Salada", "Cala Jondal", "Las Salinas Ibiza", "Lio Ibiza"]},
    {"id": "mallorca", "name": "Mallorca", "country": "İspanya", "country_en": "Spain", "coords": (39.5696, 2.6502), "hardcoded": ["Catedral de Mallorca", "Castell de Bellver", "Valldemossa", "Coves del Drach", "Port d'Andratx", "Es Trenc", "Soller", "Deia", "Pollenca"]},
    {"id": "valencia", "name": "Valencia", "country": "İspanya", "country_en": "Spain", "coords": (39.4699, -0.3763), "hardcoded": ["Ciudad de las Artes y las Ciencias", "Oceanogràfic", "Mercado Central Valencia", "La Lonja de la Seda", "Bioparc Valencia", "Playa de la Malvarrosa", "Valencia Cathedral"]},
    {"id": "kas", "name": "Kaş", "country": "Türkiye", "country_en": "Turkey", "coords": (36.2023, 29.6322), "hardcoded": ["Kaputaş Plajı", "Patara Plajı", "Antiphellos Antik Tiyatrosu", "Kaş Uzun Çarşı", "Kekova", "Saklıkent Kanyonu", "Hidayet Koyu", "Küçük Çakıl Plajı", "Büyük Çakıl Plajı"]}
]

def search_place(query: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": query, "key": API_KEY, "language": "en"}
    try:
        r = requests.get(url, params=params)
        data = r.json()
        if data.get("results"): return data["results"][0]
    except Exception as e: print(f"Error searching {query}: {e}")
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

def process_place(place_json, highlights, found_ids, city_id):
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
    if not desc_en: desc_en = f"{name} is a top spot in {city_id.capitalize()}. Definitely worth visiting."
    desc_tr = f"{name}, {city_id.capitalize()} seyahatiniz için mutlaka görmeniz gereken harika bir yer."
    
    category = "Deneyim"
    types = details.get("types", [])
    if "restaurant" in types or "food" in types: category = "Restoran"
    elif "museum" in types or "historical_landmark" in types: category = "Tarihi"
    elif "park" in types or "natural_feature" in types: category = "Park"
    
    h = {
        "id": pid, "name": name, "name_en": name, "category": category,
        "tags": [city_id, "travel", "explore"], "lat": loc.get("lat"), "lng": loc.get("lng"),
        "rating": details.get("rating", 4.5), "reviewCount": details.get("user_ratings_total", 50),
        "price": "medium", "imageUrl": photo_url, "description": desc_tr, "description_en": desc_en, "source": "google"
    }
    highlights.append(h)
    print(f"  ✅ Added: {name} ({category})")

def generate_city(city_meta):
    city_id = city_meta["id"]
    print(f"\n--- Generating {city_id.upper()} (Goal: 200) ---")
    found_ids = set()
    highlights = []
    
    # 1. Hardcoded
    for name in city_meta["hardcoded"]:
        res = search_place(f"{name} {city_meta['name']}")
        if res: process_place(res, highlights, found_ids, city_id)
        time.sleep(0.1)

    # 2. Nearby
    types = ["tourist_attraction", "restaurant", "cafe", "night_club", "museum"]
    for t in types:
        if len(highlights) >= 200: break
        print(f"Searching {t}...")
        results = nearby_search(city_meta["coords"][0], city_meta["coords"][1], 10000, t)
        for res in results:
            process_place(res, highlights, found_ids, city_id)
            if len(highlights) >= 200: break
        time.sleep(0.2)

    city_data = {
        "city": city_meta["name"], "city_en": city_id.capitalize(), "country": city_meta["country"], "country_en": city_meta["country_en"],
        "description": f"{city_meta['name']}, muazzam manzaraları ve eşsiz atmosferiyle sizi bekliyor.",
        "description_en": f"{city_id.capitalize()} is waiting for you with its magnificent views and unique atmosphere.",
        "heroImage": f"https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/{city_id}/hero.jpg",
        "coordinates": {"lat": city_meta["coords"][0], "lng": city_meta["coords"][1]},
        "highlights": highlights
    }
    
    os.makedirs("assets/cities", exist_ok=True)
    with open(f"assets/cities/{city_id}.json", "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    for city in CITIES:
        generate_city(city)

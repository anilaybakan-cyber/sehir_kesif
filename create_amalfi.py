from dotenv import load_dotenv
load_dotenv()
import json
import requests
import time
import os
from typing import List, Dict

# Config
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITY_NAME = "Amalfi"
CITY_ID = "amalfi"
OUTPUT_PATH = f"assets/cities/{CITY_ID}.json"

# Skeleton list
AMALFI_VENUE_NAMES = [
    "Duomo di Amalfi", "Fontana di Sant'Andrea", "Chiostro del Paradiso", 
    "Museo della Carta", "Valle delle Ferriere", "Amalfi Coast Drive",
    "Positano (Spiaggia Grande)", "Spiaggia del Fornillo", "Chiesa di Santa Maria Assunta",
    "Ravello (Villa Cimbrone)", "Villa Rufolo", "Duomo di Ravello", "Auditorium Oscar Niemeyer",
    "Sentiero degli Dei (Path of the Gods)", "Atrani", "Minori", "Maiori", "Cetara", 
    "Vietri sul Mare", "Fiordo di Furore", "Grotta dello Smeraldo (Emerald Grotto)",
    "Praiano", "Marina di Praia", "One Fire Beach", "Conca dei Marini",
    "Da Gemma", "L'Antica Trattoria", "Marina Grande Restaurant", "Don Alfonso 1890",
    "Chez Black", "Le Sirenuse (Champagne Bar)", "Franco's Bar", "Terrazza Cele",
    "Pasticceria Andrea Pansa", "Gelateria Porto Salvo", "A' Sciuè Sciuè"
]

def search_place(name: str, city: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": f"{name} {city} Coast Italy", "key": API_KEY, "language": "it"}
    try:
        r = requests.get(url, params=params)
        data = r.json()
        if data.get("results"): return data["results"][0]
    except Exception as e: print(f"Error searching {name}: {e}")
    return None

def nearby_search(lat, lng, radius, type_filter):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {"location": f"{lat},{lng}", "radius": radius, "type": type_filter, "key": API_KEY, "language": "it"}
    try:
        r = requests.get(url, params=params)
        return r.json().get("results", [])
    except Exception as e: print(f"Error nearby {type_filter}: {e}")
    return []

def get_details(place_id: str):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {"place_id": place_id, "key": API_KEY, "language": "it", "fields": "name,rating,user_ratings_total,geometry,photos,formatted_address,editorial_summary,types,price_level"}
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
        
    desc_it = details.get("editorial_summary", {}).get("overview", "")
    if not desc_it: desc_it = f"{name} è un luogo incantevole sulla Costiera Amalfitana."
    desc_tr = f"{name}, Amalfi Kıyısı'nın masalsı atmosferinde yer alan benzersiz bir noktadır."
    desc_en = f"{name} is an enchanting place on the Amalfi Coast."
    
    category = "Deneyim"
    types = details.get("types", [])
    if "restaurant" in types or "food" in types: category = "Restoran"
    elif "museum" in types or "historical_landmark" in types: category = "Tarihi"
    elif "park" in types or "natural_feature" in types: category = "Park"
    
    h = {
        "id": pid, "name": name, "name_en": name, "category": category,
        "tags": ["amalfi", "italy", "coast", "luxury"], "lat": loc.get("lat"), "lng": loc.get("lng"),
        "rating": details.get("rating", 4.5), "reviewCount": details.get("user_ratings_total", 50),
        "price": "expensive", "imageUrl": photo_url, "description": desc_tr, "description_en": desc_en, "source": "google"
    }
    highlights.append(h)
    print(f"  ✅ Added: {name} ({category})")

def generate_amalfi_json():
    print(f"--- Generating {CITY_NAME} Data (Goal: 200) ---")
    found_ids = set()
    highlights = []
    
    for name in AMALFI_VENUE_NAMES:
        print(f"Hardcoded: {name}...")
        search = search_place(name, CITY_NAME)
        if search: process_place(search, highlights, found_ids)
        if len(highlights) >= 200: break
        time.sleep(0.1)

    bases = [
        {"lat": 40.6340, "lng": 14.6027}, # Amalfi
        {"lat": 40.6281, "lng": 14.4850}, # Positano
        {"lat": 40.6493, "lng": 14.6119}  # Ravello
    ]
    categories = ["tourist_attraction", "restaurant", "cafe", "museum"]
    
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
        "city": "Amalfi", "city_en": "Amalfi", "country": "İtalya", "country_en": "Italy",
        "description": "Limon kokulu masalsı kıyılar. Dik yamaçlara kurulu renkli evleri, turkuaz denizi ve UNESCO mirası tarihiyle dünyanın en romantik destinasyonu.",
        "description_en": "Lemon-scented fairytale shores. The world's most romantic destination with colorful houses perched on steep cliffs, turquoise waters, and UNESCO heritage history.",
        "heroImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/amalfi/hero.jpg",
        "coordinates": {"lat": 40.6340, "lng": 14.6027}, "highlights": highlights
    }
    
    os.makedirs("assets/cities", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Success: {len(highlights)} highlights.")

if __name__ == "__main__":
    generate_amalfi_json()

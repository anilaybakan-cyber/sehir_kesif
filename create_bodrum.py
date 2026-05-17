from dotenv import load_dotenv
load_dotenv()
import json
import requests
import time
import os
from typing import List, Dict

# Config
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITY_NAME = "Bodrum"
CITY_ID = "bodrum"
OUTPUT_PATH = f"assets/cities/{CITY_ID}.json"

# Skeleton list of 70+ top places
BODRUM_VENUE_NAMES = [
    "Bodrum Kalesi", "Halikarnas Mozolesi", "Bodrum Antik Tiyatrosu", "Myndos Kapısı", 
    "Bodrum Yel Değirmenleri", "Bodrum Deniz Müzesi", "Zeki Müren Sanat Müzesi", 
    "Pedasa Antik Kenti", "Karakaya Köyü", "Dibeklihan Kültür ve Sanat Köyü",
    "Türkbükü Sahili", "Yalıkavak Sahili", "Bitez Plajı", "Gümüşlük Sahili", "Ortakent Yahşi Plajı",
    "Karaincir Plajı", "Camel Beach", "Aspat Koyu", "Bağla Koyu", "Bardakçı Koyu", "Kumbahçe Sahili",
    "Torba Sahili", "Gündoğan Sahili", "Küçükbük Plajı", "Mazı Köyü", "Orak Adası", "Karaada", 
    "Cennet Koyu", "Akvaryum Koyu", "Yalıkavak Marina", "Milta Bodrum Marina", "Turgutreis D-Marin", 
    "Bodrum Çarşı", "Bodrum Barlar Sokağı", "Maçakızı Beach", "Nikki Beach Bodrum", "Lucca Beach", 
    "Blue Point Beach Club", "X Beach Yalıkavak", "Mandalin Bodrum", "Memedof Yalıkavak", 
    "Sait Restoran Yalıkavak", "Gemibaşı Restoran", "Orfos Restoran", "Ent Restaurant", "Miam Restoran", 
    "Zuma Bodrum", "Nusr-et Steakhouse Yalıkavak", "Limon Gümüşlük", "Melengeç Restoran", 
    "Dereköy Lokantası", "Brava Bodrum", "Malva Bodrum", "Kitchen by Osman Sezener", "Bagatelle Bodrum", 
    "Novikov Bodrum", "Paper Moon Bodrum", "Hakkasan Bodrum", "Lucca by the Sea", "Fenix Bodrum", 
    "Sunset Grill & Bar Bodrum", "Mett Bodrum", "Bitez Dondurmacısı", "Sünger Pizza", "Yunuslar Karadeniz Fırını",
    "Etrim Village", "Sandıma Köyü", "Kısmet Esnaf Lokantası"
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
    if not desc_tr: desc_tr = f"{name}, Bodrum'un harika bir noktası. Keşfedilmeyi bekliyor."
    desc_en = f"{name} is a beautiful spot in Bodrum. A must-visit place."
    
    category = "Deneyim"
    types = details.get("types", [])
    if "restaurant" in types or "food" in types: category = "Restoran"
    elif "museum" in types or "historical_landmark" in types: category = "Tarihi"
    elif "park" in types or "natural_feature" in types: category = "Park"
    
    h = {
        "id": pid, "name": name, "name_en": name, "category": category,
        "tags": ["bodrum", "tatil", "türkiye"], "lat": loc.get("lat"), "lng": loc.get("lng"),
        "rating": details.get("rating", 4.5), "reviewCount": details.get("user_ratings_total", 50),
        "price": "medium", "imageUrl": photo_url, "description": desc_tr, "description_en": desc_en, "source": "google"
    }
    highlights.append(h)
    print(f"  ✅ Added: {name} ({category})")

def generate_bodrum_json():
    print(f"--- Generating {CITY_NAME} Data (Goal: 200) ---")
    found_ids = set()
    highlights = []
    
    # 1. Hardcoded Must-See (70+)
    for name in BODRUM_VENUE_NAMES:
        print(f"Hardcoded: {name}...")
        search = search_place(name, CITY_NAME)
        if search: process_place(search, highlights, found_ids)
        if len(highlights) >= 200: break
        time.sleep(0.1)

    # 2. Nearby Discovery
    bases = [
        {"lat": 37.0344, "lng": 27.4305}, # Merkez
        {"lat": 37.1033, "lng": 27.2917}, # Yalıkavak
        {"lat": 37.0167, "lng": 27.3167}, # Gümüşlük
        {"lat": 37.0900, "lng": 27.3500}, # Türkbükü
        {"lat": 37.0289, "lng": 27.3736}  # Bitez
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
        "city": CITY_NAME, "city_en": "Bodrum", "country": "Türkiye", "country_en": "Turkey",
        "description": "Ege'nin parlayan yıldızı. Mavi pencereli beyaz evleri, Begonvilleri, antik dünyanın yedi harikasından biri olan Mozolesi ve lüks gece hayatıyla büyüleyici bir tatil beldesi.",
        "description_en": "The shining star of the Aegean. Charming white houses with blue windows, bougainvilleas, the Mausoleum, and a luxurious nightlife.",
        "heroImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bodrum/hero.jpg",
        "coordinates": {"lat": 37.0344, "lng": 27.4305}, "highlights": highlights
    }
    
    os.makedirs("assets/cities", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Success: {len(highlights)} highlights.")

if __name__ == "__main__":
    generate_bodrum_json()

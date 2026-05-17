from dotenv import load_dotenv
load_dotenv()
import requests
import json
import os

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

CITIES_LANDMARKS = {
    "mykonos": "Windmills of Mykonos",
    "dubrovnik": "Old Town Dubrovnik Walls",
    "cesme": "Cesme Castle",
    "amalfi": "Duomo di Amalfi",
    "ibiza": "Dalt Vila Ibiza",
    "mallorca": "Palma Cathedral Mallorca",
    "valencia": "City of Arts and Sciences Valencia",
    "kas": "Kaş Limanı",
    "palermo": "Palermo Cathedral",
    "catania": "Piazza del Duomo Catania",
    "bari": "Basilica San Nicola Bari",
    "sardinya": "Porto Cervo Sardinia",
    "budva": "Budva Old Town",
    "ksamil": "Ksamil Islands",
    "selanik": "White Tower of Thessaloniki",
    "rhodes": "Palace of the Grand Master Rhodes"
}

def get_hero_photo(query):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"
    try:
        r = requests.get(url).json()
        if r.get("results") and r["results"][0].get("photos"):
            ref = r["results"][0]["photos"][0]["photo_reference"]
            return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1600&photo_reference={ref}&key={API_KEY}"
    except Exception as e:
        print(f"Error fetching {query}: {e}")
    return None

def standardize_heros():
    results = {}
    for city_id, landmark in CITIES_LANDMARKS.items():
        photo_url = get_hero_photo(landmark)
        if photo_url:
            results[city_id] = photo_url
            print(f"✅ Found hero for {city_id}: {landmark}")
        else:
            print(f"❌ Failed for {city_id}")
    
    with open("hero_sync_list.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    standardize_heros()

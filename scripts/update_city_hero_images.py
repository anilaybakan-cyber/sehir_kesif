#!/usr/bin/env python3
"""
Script to update city hero images using Google Places API.
Fetches proper city photos for the city switcher screen.
"""

import requests
import json
import os

# Google Places API Key
API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Cities that need photo updates (those showing flags or wrong images)
CITIES_TO_UPDATE = [
    {"id": "cenevre", "search": "Geneva Switzerland city panorama"},
    {"id": "floransa", "search": "Florence Italy Duomo panorama"},
    {"id": "lucerne", "search": "Lucerne Switzerland Chapel Bridge"},
    {"id": "lyon", "search": "Lyon France old town Saone river"},
    {"id": "marakes", "search": "Marrakech Morocco Jemaa el-Fnaa"},
    {"id": "marsilya", "search": "Marseille France Notre Dame de la Garde"},
    {"id": "nice", "search": "Nice France Promenade des Anglais"},
    {"id": "atina", "search": "Athens Greece Acropolis"},
    {"id": "bangkok", "search": "Bangkok Thailand Grand Palace"},
    {"id": "budapeste", "search": "Budapest Hungary Parliament"},
    {"id": "dublin", "search": "Dublin Ireland Temple Bar"},
    {"id": "hongkong", "search": "Hong Kong Victoria Harbour skyline"},
    {"id": "tokyo", "search": "Tokyo Japan Tower skyline"},
]

def get_place_photo(search_query):
    """Get a photo reference from Google Places API"""
    # First, find the place
    find_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": search_query,
        "inputtype": "textquery",
        "fields": "photos,name,place_id",
        "key": API_KEY
    }
    
    response = requests.get(find_url, params=params)
    data = response.json()
    
    if data.get("candidates") and len(data["candidates"]) > 0:
        candidate = data["candidates"][0]
        if "photos" in candidate and len(candidate["photos"]) > 0:
            photo_ref = candidate["photos"][0]["photo_reference"]
            # Return the full photo URL
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
            return photo_url, candidate.get("name", search_query)
    
    return None, None

def main():
    print("Fetching city photos from Google Places API...")
    print("=" * 60)
    
    results = {}
    
    for city in CITIES_TO_UPDATE:
        city_id = city["id"]
        search_query = city["search"]
        
        photo_url, place_name = get_place_photo(search_query)
        
        if photo_url:
            print(f"✅ {city_id}: Found photo for '{place_name}'")
            results[city_id] = photo_url
        else:
            print(f"❌ {city_id}: No photo found")
    
    print("=" * 60)
    print("\n// Copy these to city_switcher_screen.dart and explore_screen.dart:\n")
    
    for city_id, url in results.items():
        print(f'    "{city_id}": "{url}",')
    
    # Save to file for reference
    with open("scripts/city_photos_output.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Results saved to scripts/city_photos_output.json")
    print(f"Total: {len(results)} city photos fetched")

if __name__ == "__main__":
    main()

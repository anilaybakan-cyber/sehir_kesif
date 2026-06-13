#!/usr/bin/env python3
import os
import re
import sys
import json
import time
import requests
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, storage

SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
STORAGE_BASE_URL = f"https://storage.googleapis.com/{BUCKET_NAME}"
TEMP_DOWNLOAD_DIR = Path("temp_hotels_photos")

FSQ_API_KEYS = [
    "WL5QWUMAFFEXJWRZIYCWYQV3AZXMPAOC3YHLRPFQSLY2C12O",
    "fsq3zPCpGPvKh94yzfpp7j3IcTdkQ9YPlfRpsxwwlEuU3Ak"
]

# Initialize Firebase
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {'storageBucket': BUCKET_NAME})
    except Exception as e:
        print(f"⚠️ Failed to initialize Firebase Admin SDK: {e}. Firebase uploads will fail.")


# Load Gemini API Key
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                os.environ["GEMINI_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
                break

GEMINI_KEY = os.environ.get("GEMINI_KEY", "")
# Use gemini-2.5-flash-lite (fast, cost-effective, no thinking tokens overhead)
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
CITIES_FILE = "lib/screens/city_switcher_screen.dart"
OUTPUT_DIR = "assets/hotels"

os.makedirs(OUTPUT_DIR, exist_ok=True)

PROMPT_TEMPLATE = """You are a global travel expert and local accommodation specialist.
For the city '{city_name}' (Country: {country_name}), generate a list of exactly {count} unique, high-quality hotels.
These must be '{category_focus}' hotels (category: '{category_focus}').

IMPORTANT: The hotel names must be completely unique. Never repeat any hotel name.
If this is a smaller destination and there are not enough well-known real-world hotels to meet the count of {count}, you MUST generate highly realistic, authentic-sounding, and locally-appropriate hotel names (e.g., using typical local words, neighborhood names, landmarks, or street names for '{city_name}'). Do NOT use generic placeholders like '{city_name} Hotel' or '{city_name} Grand Palace'. The names must sound 100% authentic, premium, and local.

You must output exactly a JSON array containing {count} hotel objects. Do not include markdown code block syntax (like ```json) - output ONLY the raw JSON string starting with '[' and ending with ']'.

{exclude_clause}

Each hotel object must have these exact JSON fields:
- "id": unique lowercase string format "{city_id}_hotel_[name_slug]", e.g. "{city_id}_hotel_sheraton"
- "name": name of the hotel (real hotel name, e.g. "Sheraton {city_name}" or authentic generated name)
- "category": string, exactly one of "luxury", "boutique", "budget" matching the focus
- "area": the neighborhood/area name in Turkish, e.g. "Şehir Merkezi"
- "areaEn": the neighborhood/area name in English, e.g. "City Center"
- "rating": double between 4.0 and 5.0 (realistic rating)
- "reviewCount": integer (e.g. between 100 and 15000)
- "priceRange": string, one of "€", "€€", "€€€", "€€€€" (based on luxury level)
- "imageUrl": string, a high-quality Unsplash image URL tailored for a hotel. Use one of these beautiful hotel image templates or similar:
  - https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80
  - https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80
  - https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80
  - https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=800&q=80
  - https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80
  - https://images.unsplash.com/photo-1546964124-0cce460f38ef?auto=format&fit=crop&w=800&q=80
- "features": list of 3-4 attractive tags in Turkish, e.g. ["Harika Konum", "Kahvaltı Dahil", "Çatı Barı"]
- "featuresEn": list of 3-4 attractive tags in English, e.g. ["Great Location", "Breakfast Included", "Rooftop Bar"]
- "description": a short description in Turkish (exactly 1-2 sentences), e.g. "Tarihi limana yakın, modern tasarımıyla öne çıkan şık bir otel."
- "descriptionEn": a short description in English (exactly 1-2 sentences).
- "affiliateUrl": string, Booking.com search URL for the hotel, e.g. "https://www.booking.com/searchresults.html?ss=Hotel+Name" (make sure ss parameter is URL-encoded name + city name)
- "stars": integer (3, 4, or 5 based on category)
- "facilities": list of 4-6 facility codes, selected from this list: ["wifi", "pool", "spa", "gym", "parking", "restaurant", "bar", "ac", "pet", "room_service"]

Remember: List exactly {count} hotels. Do not truncate the JSON. Do not stop midway. Return ONLY valid JSON array."""

def call_gemini(prompt: str) -> str:
    retries = 5
    backoff = 2
    for i in range(retries):
        try:
            r = requests.post(
                f"{GEMINI_URL}?key={GEMINI_KEY}",
                headers={"Content-Type": "application/json"},
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {
                        "temperature": 0.35,
                        "maxOutputTokens": 8192,
                        "responseMimeType": "application/json"
                    },
                },
                timeout=120,
            )
            if r.status_code == 200:
                data = r.json()
                if "candidates" not in data:
                    print("ERROR from Gemini (no candidates):", data)
                    return ""
                return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            
            if r.status_code in [429, 503, 500]:
                print(f"  Transient HTTP {r.status_code}. Retrying in {backoff}s...")
                time.sleep(backoff)
                backoff *= 2
                continue
            else:
                print(f"Error: HTTP {r.status_code} - {r.text}")
                return ""
        except Exception as e:
            print("EXCEPTION from Gemini:", e)
            time.sleep(backoff)
            backoff *= 2
    return ""

def parse_cities():
    with open(CITIES_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    cities = []
    matches = re.findall(r'\{"id":\s*"([^"]+)",\s*"name":\s*"([^"]+)",\s*"name_en":\s*"([^"]+)",\s*"country":\s*"([^"]+)",\s*"country_en":\s*"([^"]+)"', content)
    for m in matches:
        cities.append({
            "id": m[0],
            "name": m[1],
            "name_en": m[2],
            "country": m[3],
            "country_en": m[4]
        })
    return cities

PLACES_API_KEY = "AIzaSyBSZJmb9IIINxWbxXgCLTPiWC9SLcaDrMk"

def get_google_places_photo(hotel_name: str, city_name: str) -> str:
    query = f"{hotel_name} {city_name}"
    encoded_query = requests.utils.quote(query)
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={encoded_query}&key={PLACES_API_KEY}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data.get("status") == "OK" and data.get("results"):
                photos = data["results"][0].get("photos", [])
                if photos:
                    photo_ref = photos[0].get("photo_reference", "")
                    if photo_ref:
                        return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference={photo_ref}&key={PLACES_API_KEY}"
    except Exception as e:
        print(f"    Failed to fetch Google Places photo for {hotel_name}: {e}")
    return ""

def download_photo(url: str, filepath: Path) -> bool:
    """Download photo from URL and save locally"""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"    ❌ Download failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"    ❌ Download error: {e}")
        return False

def upload_to_firebase(local_path: Path, city_id: str, filename: str) -> str:
    """Upload photo to Firebase Storage and make it public"""
    try:
        bucket = storage.bucket()
        blob_path = f"hotels/{city_id}/{filename}"
        blob = bucket.blob(blob_path)
        
        # Check if already exists in storage
        if blob.exists():
            return f"{STORAGE_BASE_URL}/{blob_path}"
        
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"{STORAGE_BASE_URL}/{blob_path}"
    except Exception as e:
        print(f"    ❌ Firebase upload error: {e}")
        return ""

def fetch_foursquare_photo_url(hotel_name: str, city_name: str) -> str:
    """Query Foursquare API to search for a hotel and return its photo URL"""
    for api_key in FSQ_API_KEYS:
        try:
            # 1. Search place
            query = f"{hotel_name}"
            search_url = f"https://api.foursquare.com/v3/places/search?query={urllib.parse.quote(query)}&near={urllib.parse.quote(city_name)}&limit=1"
            headers = {
                "Authorization": api_key,
                "accept": "application/json"
            }
            
            r = requests.get(search_url, headers=headers, timeout=10)
            if r.status_code == 200:
                data = r.json()
                if data.get("results") and len(data["results"]) > 0:
                    fsq_id = data["results"][0].get("fsq_id")
                    if fsq_id:
                        # 2. Get photos
                        photo_url = f"https://api.foursquare.com/v3/places/{fsq_id}/photos?limit=1"
                        r_photo = requests.get(photo_url, headers=headers, timeout=10)
                        if r_photo.status_code == 200:
                            photos = r_photo.json()
                            if isinstance(photos, list) and len(photos) > 0:
                                prefix = photos[0].get("prefix", "")
                                suffix = photos[0].get("suffix", "")
                                if prefix and suffix:
                                    return f"{prefix}1000x800{suffix}"
            else:
                print(f"    ⚠️ Foursquare search HTTP {r.status_code} with key {api_key[:8]}...")
        except Exception as e:
            print(f"    ⚠️ Foursquare API error with key {api_key[:8]}: {e}")
    return ""

def normalize_hotel(hotel, city_id, city_name, category_focus):
    # Normalize ID
    hotel_id = str(hotel.get("id", "")).strip().lower()
    if not hotel_id or hotel_id == f"{city_id}_hotel_":
        name_slug = re.sub(r'[^a-z0-9_]', '', str(hotel.get("name", "")).strip().lower().replace(" ", "_"))
        hotel_id = f"{city_id}_hotel_{name_slug}"
    else:
        hotel_id = re.sub(r'[^a-z0-9_]', '', hotel_id.replace(" ", "_"))
    
    if not hotel_id.startswith(f"{city_id}_"):
        hotel_id = f"{city_id}_{hotel_id}"
    hotel["id"] = hotel_id

    # Normalize Name
    hotel["name"] = str(hotel.get("name", "")).strip()

    # Normalize Category
    category = str(hotel.get("category", "")).strip().lower()
    if category not in ["luxury", "boutique", "budget"]:
        category = category_focus if category_focus in ["luxury", "boutique", "budget"] else "boutique"
    hotel["category"] = category

    # Normalize Stars
    try:
        stars = int(hotel.get("stars", 4))
    except:
        stars = 4
    if category == "luxury":
        stars = max(4, min(5, stars))
    elif category == "budget":
        stars = max(2, min(4, stars))
    else:
        stars = max(3, min(5, stars))
    hotel["stars"] = stars

    # Normalize Rating
    try:
        rating = float(hotel.get("rating", 4.5))
    except:
        rating = 4.5
    hotel["rating"] = round(max(3.5, min(5.0, rating)), 1)

    # Normalize Review Count
    try:
        review_count = int(hotel.get("reviewCount", 500))
    except:
        review_count = 500
    hotel["reviewCount"] = max(50, review_count)

    # Normalize Price Range
    price_range = str(hotel.get("priceRange", "")).strip()
    if price_range not in ["€", "€€", "€€€", "€€€€"]:
        if category == "luxury":
            price_range = "€€€€"
        elif category == "budget":
            price_range = "€"
        else:
            price_range = "€€"
    hotel["priceRange"] = price_range

    # Normalize Facilities
    facilities = hotel.get("facilities", [])
    if not isinstance(facilities, list):
        facilities = []
    allowed_facilities = ["wifi", "pool", "spa", "gym", "parking", "restaurant", "bar", "ac", "pet", "room_service"]
    cleaned_facilities = [str(f).strip().lower() for f in facilities if str(f).strip().lower() in allowed_facilities]
    cleaned_facilities = list(dict.fromkeys(cleaned_facilities))
    if not cleaned_facilities:
        if category == "luxury":
            cleaned_facilities = ["wifi", "spa", "pool", "gym", "restaurant", "ac"]
        elif category == "budget":
            cleaned_facilities = ["wifi", "ac"]
        else:
            cleaned_facilities = ["wifi", "restaurant", "bar", "ac"]
    hotel["facilities"] = cleaned_facilities

    # Normalize Features
    features = hotel.get("features", [])
    if not isinstance(features, list) or not features:
        features = ["Merkezi Konum", "Şık Odalar", "Ücretsiz Wi-Fi"]
    hotel["features"] = [str(f).strip() for f in features][:4]

    featuresEn = hotel.get("featuresEn", [])
    if not isinstance(featuresEn, list) or not featuresEn:
        featuresEn = ["Central Location", "Chic Rooms", "Free Wi-Fi"]
    hotel["featuresEn"] = [str(f).strip() for f in featuresEn][:4]

    # Normalize Description
    desc = str(hotel.get("description", "")).strip()
    if not desc:
        desc = f"{hotel['name']}, {city_name} şehrinde konforlu ve keyifli bir konaklama sunar."
    hotel["description"] = desc

    desc_en = str(hotel.get("descriptionEn", "")).strip()
    if not desc_en:
        desc_en = f"{hotel['name']} offers a comfortable and pleasant stay in {city_name}."
    hotel["descriptionEn"] = desc_en

    # Normalize Image URL - just keep standard, places photo will be fetched concurrently
    image_url = str(hotel.get("imageUrl", "")).strip()
    if not image_url.startswith("http"):
        image_url = "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80"
    hotel["imageUrl"] = image_url

    # Normalize Affiliate URL
    hotel["affiliateUrl"] = f"https://www.booking.com/searchresults.html?ss={requests.utils.quote(hotel['name'] + ' ' + city_name)}"

    return hotel

def fetch_photos_concurrently(hotels, city_name, city_id):
    # Create temp download dir if not exists
    TEMP_DOWNLOAD_DIR.mkdir(exist_ok=True)

    def fetch_one(hotel):
        name = hotel.get("name", "").strip()
        hotel_id = hotel.get("id", "").strip()
        image_url = str(hotel.get("imageUrl", "")).strip()
        
        # Only fetch if it's an Unsplash fallback placeholder or empty
        if not image_url.startswith("http") or "unsplash.com" in image_url:
            filename = f"{hotel_id}.jpg"
            local_path = TEMP_DOWNLOAD_DIR / filename
            
            # 1. Try Foursquare first
            print(f"    [Photo] Searching Foursquare for {name} in {city_name}...")
            photo_url = fetch_foursquare_photo_url(name, city_name)
            method = "Foursquare"
            
            # 2. Fallback to Google Places
            if not photo_url:
                print(f"    [Photo] Foursquare failed. Searching Google Places for {name} in {city_name}...")
                photo_url = get_google_places_photo(name, city_name)
                method = "Google Places"
                
            if photo_url:
                print(f"    [Photo] Found {method} URL for {name}, downloading...")
                if download_photo(photo_url, local_path):
                    firebase_url = upload_to_firebase(local_path, city_id, filename)
                    if firebase_url:
                        hotel["imageUrl"] = firebase_url
                        print(f"    ✅ Uploaded {name} to Firebase: {firebase_url}")
                    try:
                        local_path.unlink()
                    except:
                        pass
                else:
                    print(f"    ⚠️ Failed to download photo for {name} from {method}")
            else:
                print(f"    ⚠️ No photo found for {name} on Foursquare or Google. Keeping Unsplash placeholder.")

    with ThreadPoolExecutor(max_workers=8) as executor:
        list(executor.map(fetch_one, hotels))

def generate_batch(city_name, country_name, city_id, category_focus, count=15, exclude_list=[]):
    exclude_clause = ""
    if exclude_list:
        names_str = ", ".join([f'"{name}"' for name in exclude_list])
        exclude_clause = f"Do NOT include any of these hotels that were generated in previous batches: {names_str}."

    prompt = PROMPT_TEMPLATE.format(
        city_id=city_id,
        city_name=city_name,
        country_name=country_name,
        category_focus=category_focus,
        count=count,
        exclude_clause=exclude_clause
    )

    retries = 3
    for attempt in range(retries):
        raw_response = call_gemini(prompt)
        if raw_response:
            try:
                clean_response = raw_response.strip()
                if clean_response.startswith("```"):
                    clean_response = re.sub(r"^```(?:json)?", "", clean_response)
                    clean_response = re.sub(r"```$", "", clean_response).strip()
                
                parsed = json.loads(clean_response)
                if isinstance(parsed, list):
                    normalized_list = []
                    for h in parsed:
                        if isinstance(h, dict):
                            normalized_list.append(normalize_hotel(h, city_id, city_name, category_focus))
                    fetch_photos_concurrently(normalized_list, city_name, city_id)
                    return normalized_list
                else:
                    print("  Received JSON is not a list.")
            except json.JSONDecodeError as je:
                print(f"  JSONDecodeError in batch ({category_focus}): {je}. Attempt {attempt + 1}/{retries}")
                os.makedirs("scratch", exist_ok=True)
                with open("scratch/raw_response.json", "w", encoding="utf-8") as rf:
                    rf.write(raw_response)
        
        time.sleep(3)
    return None

def generate_hotels_for_city(idx, city, total_cities):
    city_id = city["id"]
    city_name = city["name_en"]
    country_name = city["country_en"]
    output_file = os.path.join(OUTPUT_DIR, f"{city_id}.json")

    if os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if len(existing) >= 50:
                print(f"[{idx}/{total_cities}] Skipping {city_name} (JSON has {len(existing)} hotels)")
                return
            else:
                print(f"[{idx}/{total_cities}] Regenerating {city_name} (JSON has only {len(existing)} hotels)")
        except:
            pass

    print(f"[{idx}/{total_cities}] Starting hotel generation for {city_name}, {country_name}...")
    
    merged = []
    seen_names = set()
    
    # We target exactly 50: 17 luxury, 17 boutique, 16 budget
    cat_sizes = {"luxury": 17, "boutique": 17, "budget": 16}
    success_all = True

    for cat, size in cat_sizes.items():
        print(f"[{city_name}] Generating batch of {size} ({cat})...")
        batch = generate_batch(city_name, country_name, city_id, cat, count=size, exclude_list=list(seen_names))
        if not batch:
            print(f"[{city_name}] Failed batch ({cat}). Skipping city.")
            success_all = False
            break
        
        for hotel in batch:
            name = hotel.get("name", "").strip().lower()
            if name and name not in seen_names:
                seen_names.add(name)
                merged.append(hotel)
        
        time.sleep(1)

    if not success_all:
        return

    # Self-healing loop: keep requesting small batches of at most 8 hotels until we hit exactly 50
    max_attempts = 6
    loop_attempt = 0
    while len(merged) < 50 and loop_attempt < max_attempts:
        loop_attempt += 1
        diff = 50 - len(merged)
        batch_size = min(diff, 8)
        print(f"[{city_name}] Short of 50 hotels (currently {len(merged)}). Fetching batch of {batch_size} (mixed)...")
        
        batch = generate_batch(
            city_name, country_name, city_id, 
            "luxury or boutique or budget", 
            count=batch_size, 
            exclude_list=list(seen_names)
        )
        
        if batch:
            added_count = 0
            for hotel in batch:
                name = hotel.get("name", "").strip().lower()
                if name and name not in seen_names:
                    seen_names.add(name)
                    merged.append(hotel)
                    added_count += 1
            print(f"[{city_name}] Added {added_count} unique hotels in this iteration.")
        else:
            print(f"[{city_name}] Mixed batch request failed.")
            
        time.sleep(1)

    # Slice/pad to exactly 50 hotels
    final_hotels = merged[:50]
    
    if len(final_hotels) >= 45:
        print(f"[{city_name}] Successfully gathered {len(final_hotels)} unique hotels.")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(final_hotels, f, ensure_ascii=False, indent=2)
        print(f"[{city_name}] Successfully wrote {len(final_hotels)} hotels to {output_file}")
    else:
        print(f"[{city_name}] ERROR: Could only gather {len(final_hotels)} hotels (less than 45). Not saving to avoid incomplete dataset.")

def main():
    if not GEMINI_KEY:
        print("ERROR: GEMINI_API_KEY is required in .env or environment variables.")
        sys.exit(1)

    cities = parse_cities()
    total_cities = len(cities)
    print(f"Parsed {total_cities} cities from {CITIES_FILE}")

    # Use ThreadPoolExecutor to run 3 cities concurrently
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for idx, city in enumerate(cities, 1):
            futures.append(executor.submit(generate_hotels_for_city, idx, city, total_cities))
        
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error in city generation: {e}")

if __name__ == "__main__":
    main()

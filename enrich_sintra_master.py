import json
import requests
import time
import urllib.parse

API_KEY = 'AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g'

def get_google_photo_url(place_name):
    queries = [f"{place_name} Sintra Portugal", f"{place_name} Sintra", place_name]
    for query in queries:
        try:
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={urllib.parse.quote(query)}&inputtype=textquery&fields=place_id,photos&key={API_KEY}&locationbias=circle:10000@38.7992,-9.3911"
            r = requests.get(url)
            data = r.json()
            if data['status'] == 'OK' and data['candidates']:
                if 'photos' in data['candidates'][0]:
                    ref = data['candidates'][0]['photos'][0]['photo_reference']
                    print(f"  ✓ {place_name}")
                    return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={ref}&key={API_KEY}"
        except:
            continue
    print(f"  ✗ {place_name}")
    return None

# BATCH 1: Gizli Saraylar ve Bahçeler
batch_1 = [
    {"name": "Biester Palace", "name_en": "Biester Palace", "area": "Merkez", "category": "Tarihi", "tags": ["saray", "gizemli", "wednesday"], "lat": 38.7950, "lng": -9.3930, "price": "high", "rating": 4.6, "description": "Wednesday dizisinin çekildiği, gizli geçitleri ve gotik mimarisiyle büyüleyici saray.", "description_en": "Fascinating palace with secret passages and gothic architecture, where the Wednesday series was filmed.", "bestTime": "Gündüz", "tips": "Bahçesindeki çay evinde mola verin.", "tips_en": "Take a break at the tea house in its garden."},
    {"name": "Valley of Lakes", "name_en": "Valley of Lakes", "area": "Pena Park", "category": "Park", "tags": ["göl", "ördek", "huzur"], "lat": 38.7860, "lng": -9.3950, "price": "free", "rating": 4.8, "description": "Pena Parkı içinde, ördek evleri ve eğrelti otlarıyla dolu masalsı göller vadisi.", "description_en": "Fairytale valley of lakes in Pena Park filled with duck houses and ferns.", "bestTime": "Sabah", "tips": "Sisli havalarda atmosfer çok mistik olur.", "tips_en": "Atmosphere gets very mystical in foggy weather."},
    {"name": "Vila Sassetti", "name_en": "Vila Sassetti", "area": "Merkez", "category": "Tarihi", "tags": ["villa", "yürüyüş", "italyan"], "lat": 38.7960, "lng": -9.3940, "price": "free", "rating": 4.7, "description": "Merkezden kaleye giden yürüyüş rotasında, Toskana tarzı gizli bir villa.", "description_en": "A secret Tuscan-style villa on the walking route from center to the castle.", "bestTime": "Gündüz", "tips": "Ücretsiz bahçesi ve manzarası harikadır.", "tips_en": "Its free garden and view are wonderful."}
]

# BATCH 2: Vahşi Plajlar ve Manzaralar
batch_2 = [
    {"name": "Ursa Beach", "name_en": "Praia da Ursa", "area": "Cabo da Roca", "category": "Plaj", "tags": ["vahşi", "kaya", "bakir"], "lat": 38.7900, "lng": -9.4900, "price": "free", "rating": 4.9, "description": "Avrupa'nın en güzel vahşi plajlarından biri, devasa kayalıklarla çevrili.", "description_en": "One of Europe's most beautiful wild beaches, surrounded by massive cliffs.", "bestTime": "Gündüz", "tips": "İniş yolu zordur, spor ayakkabı şart.", "tips_en": "Descent path is difficult, sneakers are a must."},
    {"name": "Azenhas do Mar Viewpoint", "name_en": "Miradouro Azenhas", "area": "Azenhas", "category": "Manzara", "tags": ["panorama", "okyanus", "ikonik"], "lat": 38.8410, "lng": -9.4620, "price": "free", "rating": 4.9, "description": "Uçurumdaki beyaz köyün en ikonik fotoğrafının çekildiği nokta.", "description_en": "The spot where the most iconic photo of the white village on the cliff is taken.", "bestTime": "Gün batımı", "tips": "Gün batımında renkler büyüleyicidir.", "tips_en": "Colors are fascinating at sunset."},
    {"name": "Praia do Magoito", "name_en": "Magoito Beach", "area": "Magoito", "category": "Plaj", "tags": ["plaj", "fosil", "iyot"], "lat": 38.8600, "lng": -9.4500, "price": "free", "rating": 4.6, "description": "Fosil kumulları ve yüksek iyot oranıyla bilinen geniş plaj.", "description_en": "Wide beach known for fossil dunes and high iodine levels.", "bestTime": "Gündüz", "tips": "Turistlerden uzak, yerel halkın tercihidir.", "tips_en": "Away from tourists, preferred by locals."}
]

# BATCH 3: Restoranlar (Lezzet Durakları)
batch_3 = [
    {"name": "Curral dos Caprinos", "name_en": "Curral dos Caprinos", "area": "Várzea", "category": "Restoran", "tags": ["oğlak", "geleneksel", "rustik"], "lat": 38.8100, "lng": -9.3800, "price": "medium", "rating": 4.7, "description": "Sintra'nın geleneksel oğlak eti yemeği (Cabrito) için en iyi adres.", "description_en": "Best address for Sintra's traditional kid meat dish (Cabrito).", "bestTime": "Akşam", "tips": "Porsiyonlar büyüktür, paylaşabilirsiniz.", "tips_en": "Portions are large, you can share."},
    {"name": "Apeadeiro", "name_en": "Apeadeiro", "area": "İstasyon", "category": "Restoran", "tags": ["esnaf", "balık", "uygun"], "lat": 38.8000, "lng": -9.3850, "price": "low", "rating": 4.5, "description": "İstasyon yakınında, yerel halkın gittiği klasik Portekiz lokantası.", "description_en": "Classic Portuguese eatery near the station frequented by locals.", "bestTime": "Öğle", "tips": "Günün menüsü (Prato do Dia) çok ekonomiktir.", "tips_en": "Dish of the day (Prato do Dia) is very economical."},
    {"name": "Café Saudade", "name_en": "Café Saudade", "area": "İstasyon", "category": "Kafe", "tags": ["vintage", "queijada", "çay"], "lat": 38.7990, "lng": -9.3860, "price": "medium", "rating": 4.6, "description": "Tarihi binada, vintage dekorasyonlu ve harika tatlıları olan kafe.", "description_en": "Cafe with vintage decoration and great desserts in a historic building.", "bestTime": "Öğle", "tips": "Devasa 'Travesseiro'ları meşhurdur.", "tips_en": "Their giant 'Travesseiro's are famous."},
    {"name": "Bar do Fundo", "name_en": "Bar do Fundo", "area": "Praia Grande", "category": "Restoran", "tags": ["gün batımı", "deniz ürünleri", "plaj"], "lat": 38.8160, "lng": -9.4760, "price": "high", "rating": 4.6, "description": "Plajın sonunda, gün batımına karşı şık akşam yemeği.", "description_en": "Stylish dinner against sunset at the end of the beach.", "bestTime": "Akşam", "tips": "Romantik bir akşam yemeği için ideal.", "tips_en": "Ideal for a romantic dinner."}
]

def enrich():
    filepath = 'assets/cities/sintra.json'
    all_new = batch_1 + batch_2 + batch_3
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data['highlights'])} places.")
    
    existing_names = {p['name'].lower() for p in data['highlights']}
    places_to_add = []
    
    for place in all_new:
        if place['name'].lower() in existing_names:
            print(f"Skip: {place['name']}")
            continue
        print(f"Processing: {place['name']}")
        place['id'] = place['name'].lower().replace(' ', '-').replace("'", '').replace('ç', 'c').replace('ã', 'a')
        photo_url = get_google_photo_url(place['name'])
        place['imageUrl'] = photo_url or "https://images.unsplash.com/photo-1555990538-dca68da33989?q=80&w=800"
        place['source'] = 'google' if photo_url else 'unsplash_fallback'
        place['distanceFromCenter'] = place.get('distanceFromCenter', 1.0)
        places_to_add.append(place)
        time.sleep(0.3)
    
    data['highlights'].extend(places_to_add)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Added {len(places_to_add)} new places. Total: {len(data['highlights'])}")

if __name__ == "__main__":
    enrich()

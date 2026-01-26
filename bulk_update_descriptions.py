#!/usr/bin/env python3
"""
Bulk update script for researched places across multiple cities.
This script processes places that need research and generates
generic but category-specific descriptions.
"""

import json
import os
from pathlib import Path

CITIES_DIR = 'assets/cities'

# City name mapping
CITY_MAP = {
    'Venedik': 'venedik', 'Madrid': 'madrid', 'Napoli': 'napoli', 'Paris': 'paris',
    'İstanbul': 'istanbul', 'Hong Kong': 'hongkong', 'Gaziantep': 'gaziantep',
    'Zermatt': 'zermatt', 'Lucerne': 'lucerne', 'Sevilla': 'sevilla',
    'Marakeş': 'marakes', 'Santorini': 'santorini', 'Fes': 'fes',
    'Bangkok': 'bangkok', 'Amsterdam': 'amsterdam', 'Berlin': 'berlin',
    'Barcelona': 'barcelona', 'Londra': 'londra', 'Roma': 'roma',
    'Atina': 'atina', 'Budapeşte': 'budapeste', 'Prag': 'prag',
    'Viyana': 'viyana', 'Lizbon': 'lizbon', 'Porto': 'porto',
    'Floransa': 'floransa', 'Milano': 'milano', 'Dubai': 'dubai',
    'Singapur': 'singapur', 'Tokyo': 'tokyo', 'Seul': 'seul',
    'New York': 'newyork', 'Kopenhag': 'kopenhag', 'Stockholm': 'stockholm',
    'Dublin': 'dublin', 'Edinburgh': 'edinburgh', 'Cenevre': 'cenevre',
    'Zürih': 'zurih', 'Nice': 'nice', 'Lyon': 'lyon', 'Marsilya': 'marsilya',
    'Strazburg': 'strazburg', 'Colmar': 'colmar', 'Bologna': 'bologna',
    'Matera': 'matera', 'Heidelberg': 'heidelberg', 'Brugge': 'brugge',
    'Giethoorn': 'giethoorn', 'Sintra': 'sintra', 'San Sebastian': 'sansebastian',
    'Rovaniemi': 'rovaniemi', 'Tromsø': 'tromso', 'Kahire': 'kahire',
    'Oslo': 'oslo',
}

# Category-based description templates
CATEGORY_TEMPLATES = {
    'Bar': {
        'tr': lambda name, city: f"{city}'nin atmosferik barlarından biri. Özenle hazırlanmış kokteyller, samimi ortam ve yerel içki seçenekleriyle gece hayatının vazgeçilmez durağı.",
        'en': lambda name, city: f"One of {city}'s atmospheric bars. An essential nightlife stop with carefully crafted cocktails, intimate atmosphere and local drink options."
    },
    'Restoran': {
        'tr': lambda name, city: f"{city}'nin sevilen restoranlarından biri. Yerel lezzetler ve özenli sunum ile gurme bir deneyim sunuyor.",
        'en': lambda name, city: f"One of {city}'s beloved restaurants. Offering a gourmet experience with local flavors and careful presentation."
    },
    'Kafe': {
        'tr': lambda name, city: f"{city}'nin popüler kafelerinden biri. Kahve tutkunları için mükemmel bir mola noktası, samimi atmosfer ve lezzetli atıştırmalıklar.",
        'en': lambda name, city: f"One of {city}'s popular cafes. A perfect break spot for coffee lovers with intimate atmosphere and delicious snacks."
    },
    'Cafe': {
        'tr': lambda name, city: f"{city}'nin popüler kafelerinden biri. Kahve tutkunları için mükemmel bir mola noktası, samimi atmosfer ve lezzetli atıştırmalıklar.",
        'en': lambda name, city: f"One of {city}'s popular cafes. A perfect break spot for coffee lovers with intimate atmosphere and delicious snacks."
    },
    'Müze': {
        'tr': lambda name, city: f"{city}'nin önemli müzelerinden biri. Sanat ve tarih meraklıları için zengin koleksiyonlar ve etkileyici sergiler sunuyor.",
        'en': lambda name, city: f"One of {city}'s important museums. Offering rich collections and impressive exhibitions for art and history enthusiasts."
    },
    'Park': {
        'tr': lambda name, city: f"{city}'nin yeşil alanlarından biri. Doğa yürüyüşleri, piknik ve dinlenme için ideal bir kaçış noktası.",
        'en': lambda name, city: f"One of {city}'s green spaces. An ideal escape point for nature walks, picnics and relaxation."
    },
    'Tarihi': {
        'tr': lambda name, city: f"{city}'nin tarihi dokusunu yansıtan önemli bir yapı. Şehrin geçmişine açılan kapı niteliğinde.",
        'en': lambda name, city: f"An important structure reflecting {city}'s historic fabric. A gateway to the city's past."
    },
    'Manzara': {
        'tr': lambda name, city: f"{city}'nin en güzel manzara noktalarından biri. Şehir siluetini ve çevresini seyretmek için ideal bir durak.",
        'en': lambda name, city: f"One of {city}'s most beautiful viewpoints. An ideal stop to watch the city silhouette and surroundings."
    },
    'Deneyim': {
        'tr': lambda name, city: f"{city}'de benzersiz bir deneyim sunan mekan. Yerel kültürü yakından tanıma fırsatı.",
        'en': lambda name, city: f"A venue offering a unique experience in {city}. An opportunity to get to know the local culture up close."
    },
    'Alışveriş': {
        'tr': lambda name, city: f"{city}'nin alışveriş cenneti. Yerel ürünlerden hediyeliklere geniş bir yelpaze sunuyor.",
        'en': lambda name, city: f"A shopping paradise in {city}. Offering a wide range from local products to souvenirs."
    },
    'default': {
        'tr': lambda name, city: f"{city}'de mutlaka görülmesi gereken yerlerden biri. Şehrin ruhunu yansıtan atmosferiyle benzersiz bir keşif.",
        'en': lambda name, city: f"A must-see place in {city}. A unique discovery with an atmosphere reflecting the spirit of the city."
    }
}

def get_city_name(city_id):
    """Get display name for city"""
    for name, id in CITY_MAP.items():
        if id == city_id:
            return name
    return city_id.title()

def generate_description(name, city, category, lang='tr'):
    """Generate a description based on category"""
    template = CATEGORY_TEMPLATES.get(category, CATEGORY_TEMPLATES['default'])
    city_display = get_city_name(city)
    return template[lang](name, city_display)

def needs_update(desc):
    """Check if description needs updating (is generic)"""
    generic_patterns = [
        'popüler mekanlardan biri',
        'içindeki popüler',
        'puan ve',
        'yorum ile',
        'ziyaretçilerin beğenisini',
        'canlanan, kokteyl',
        'One of the popular places in',
        'rating and',
        'reviews',
    ]
    if not desc:
        return True
    for pattern in generic_patterns:
        if pattern.lower() in desc.lower():
            return True
    return False

def update_city(city_id):
    """Update a single city's JSON file"""
    city_file = os.path.join(CITIES_DIR, f"{city_id}.json")
    if not os.path.exists(city_file):
        print(f"Not found: {city_file}")
        return 0
    
    with open(city_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = 0
    for h in data.get('highlights', []):
        name = h.get('name', '')
        category = h.get('category', 'default')
        
        # Check TR description
        tr_desc = h.get('description', '')
        if needs_update(tr_desc):
            new_tr = generate_description(name, city_id, category, 'tr')
            h['description'] = new_tr
            updated += 1
        
        # Check EN description
        en_desc = h.get('description_en', '')
        if needs_update(en_desc):
            new_en = generate_description(name, city_id, category, 'en')
            h['description_en'] = new_en
    
    if updated > 0:
        with open(city_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {city_id}: {updated} descriptions")
    
    return updated

def main():
    # Load research_needed.json to find cities to process
    with open('research_needed.json', 'r', encoding='utf-8') as f:
        research_items = json.load(f)
    
    # Get unique cities
    cities = set()
    for city, place, tr, en in research_items:
        city_id = CITY_MAP.get(city, city.lower().replace(' ', ''))
        cities.add(city_id)
    
    print(f"Processing {len(cities)} cities...")
    total = 0
    for city_id in sorted(cities):
        count = update_city(city_id)
        total += count
    
    print(f"\n=== TOTAL UPDATES: {total} ===")

if __name__ == '__main__':
    main()

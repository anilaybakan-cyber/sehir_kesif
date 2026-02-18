#!/usr/bin/env python3
"""
Content Update Script - Translations
Reads CSV and updates JSON files based on task type
"""

import csv
import json
import os
from pathlib import Path

# City name mapping (CSV name -> JSON filename)
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
    'Safsavan': 'safsavan', 'Midilli': 'midilli', 'Antalya': 'antalya',
    'Kapadokya': 'kapadokya', 'Belgrad': 'belgrad', 'Kotor': 'kotor',
    'Tiran': 'tiran', 'Selanik': 'selanik', 'Saraybosna': 'saraybosna',
    'Mostar': 'mostar',
}

def normalize_city(city_name):
    """Convert CSV city name to JSON filename"""
    return CITY_MAP.get(city_name, city_name.lower().replace(' ', ''))

def translate_tr_to_en(text):
    """Simple TR to EN translation for common patterns"""
    # This is a placeholder - for real translation we'd use an API
    # For now, return the text as-is to be updated manually or via API
    return text

def translate_en_to_tr(text):
    """Simple EN to TR translation for common patterns"""
    # This is a placeholder - for real translation we'd use an API
    return text

def load_city_data(city_file):
    """Load JSON data for a city"""
    try:
        with open(city_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {city_file}: {e}")
        return None

def save_city_data(city_file, data):
    """Save JSON data for a city"""
    try:
        with open(city_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving {city_file}: {e}")
        return False

def find_place_in_city(data, place_name):
    """Find a place by name in city data"""
    for i, h in enumerate(data.get('highlights', [])):
        if h.get('name', '').strip() == place_name.strip():
            return i
    return -1

def main():
    csv_file = 'all_places_report2.csv'
    cities_dir = 'assets/cities'
    
    # Read CSV
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        rows = list(reader)
    
    # Skip header
    data_rows = rows[1:]
    
    # Group by task type
    translations_tr_to_en = []  # İngilizceden çevirsin
    translations_en_to_tr = []  # Türkçe'den çevirsin
    research_needed = []       # Araştırma gerekli
    
    for row in data_rows:
        if len(row) < 5:
            continue
        task = row[0].strip()
        city = row[1].strip()
        place = row[2].strip()
        tr_desc = row[3].strip()
        en_desc = row[4].strip()
        
        if 'İngilizceden çevirsin' in task:
            translations_tr_to_en.append((city, place, tr_desc, en_desc))
        elif 'Türkçe' in task and 'çevirsin' in task:
            translations_en_to_tr.append((city, place, tr_desc, en_desc))
        elif 'araştırma' in task.lower() or 'detaylı' in task.lower():
            research_needed.append((city, place, tr_desc, en_desc))
    
    print(f"TR→EN translations: {len(translations_tr_to_en)}")
    print(f"EN→TR translations: {len(translations_en_to_tr)}")
    print(f"Research needed: {len(research_needed)}")
    
    # Process translations
    city_changes = {}  # city_file -> [(index, field, value), ...]
    
    # TR→EN: Use TR description to update EN
    for city, place, tr_desc, en_desc in translations_tr_to_en:
        city_file = os.path.join(cities_dir, f"{normalize_city(city)}.json")
        if not os.path.exists(city_file):
            print(f"City file not found: {city_file}")
            continue
        
        if city_file not in city_changes:
            city_changes[city_file] = {'data': load_city_data(city_file), 'updates': []}
        
        if city_changes[city_file]['data'] is None:
            continue
        
        idx = find_place_in_city(city_changes[city_file]['data'], place)
        if idx >= 0:
            # Use existing TR description to create EN
            city_changes[city_file]['updates'].append((idx, 'description_en', tr_desc))
    
    # EN→TR: Use EN description to update TR
    for city, place, tr_desc, en_desc in translations_en_to_tr:
        city_file = os.path.join(cities_dir, f"{normalize_city(city)}.json")
        if not os.path.exists(city_file):
            print(f"City file not found: {city_file}")
            continue
        
        if city_file not in city_changes:
            city_changes[city_file] = {'data': load_city_data(city_file), 'updates': []}
        
        if city_changes[city_file]['data'] is None:
            continue
        
        idx = find_place_in_city(city_changes[city_file]['data'], place)
        if idx >= 0:
            # Use existing EN description to create TR
            city_changes[city_file]['updates'].append((idx, 'description', en_desc))
    
    # Apply changes and save
    total_updates = 0
    for city_file, info in city_changes.items():
        if info['data'] is None:
            continue
        
        for idx, field, value in info['updates']:
            info['data']['highlights'][idx][field] = value
            total_updates += 1
        
        if info['updates']:
            save_city_data(city_file, info['data'])
            print(f"Updated {city_file}: {len(info['updates'])} changes")
    
    print(f"\nTotal updates applied: {total_updates}")
    
    # Save research items to a separate file for web search
    with open('research_needed.json', 'w', encoding='utf-8') as f:
        json.dump(research_needed, f, ensure_ascii=False, indent=2)
    print(f"\nResearch items saved to research_needed.json: {len(research_needed)}")

if __name__ == '__main__':
    main()

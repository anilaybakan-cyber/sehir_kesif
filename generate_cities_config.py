import json
import os

CITIES_DIR = 'assets/cities'
OUTPUT_FILE = 'assets/cities_list.json'

FLAGS = {
    'Türkiye': '🇹🇷', 'Turkey': '🇹🇷',
    'İtalya': '🇮🇹', 'Italy': '🇮🇹',
    'İspanya': '🇪🇸', 'Spain': '🇪🇸',
    'Fransa': '🇫🇷', 'France': '🇫🇷',
    'Hollanda': '🇳🇱', 'Netherlands': '🇳🇱',
    'Almanya': '🇩🇪', 'Germany': '🇩🇪',
    'Yunanistan': '🇬🇷', 'Greece': '🇬🇷',
    'İsviçre': '🇨🇭', 'Switzerland': '🇨🇭',
    'İrlanda': '🇮🇪', 'Ireland': '🇮🇪',
    'Avusturya': '🇦🇹', 'Austria': '🇦🇹',
    'Belçika': '🇧🇪', 'Belgium': '🇧🇪',
    'Portekiz': '🇵🇹', 'Portugal': '🇵🇹',
    'Çekya': '🇨🇿', 'Czechia': '🇨🇿', 'Czech Republic': '🇨🇿', 'Czech': '🇨🇿',
    'Bosna Hersek': '🇧🇦', 'Bosnia': '🇧🇦',
    'Sırbistan': '🇷🇸', 'Serbia': '🇷🇸',
    'Norveç': '🇳🇴', 'Norway': '🇳🇴',
    'Finlandiya': '🇫🇮', 'Finland': '🇫🇮',
    'Karadağ': '🇲🇪', 'Montenegro': '🇲🇪',
    'Arnavutluk': '🇦🇱', 'Albania': '🇦🇱',
    'Macaristan': '🇭🇺', 'Hungary': '🇭🇺',
    'İngiltere': '🇬🇧', 'United Kingdom': '🇬🇧', 'England': '🇬🇧',
    'İskoçya': '🏴󠁧󠁢󠁳󠁣󠁴󠁿', 'Scotland': '🏴󠁧󠁢󠁳󠁣󠁴󠁿',
    'Danimarka': '🇩🇰', 'Denmark': '🇩🇰',
    'İsveç': '🇸🇪', 'Sweden': '🇸🇪',
    'ABD': '🇺🇸', 'USA': '🇺🇸',
    'Tayland': '🇹🇭', 'Thailand': '🇹🇭',
    'Japonya': '🇯🇵', 'Japan': '🇯🇵',
    'Güney Kore': '🇰🇷', 'South Korea': '🇰🇷',
    'Singapur': '🇸🇬', 'Singapore': '🇸🇬',
    'Fas': '🇲🇦', 'Morocco': '🇲🇦',
    'Mısır': '🇪🇬', 'Egypt': '🇪🇬',
    'BAE': '🇦🇪', 'UAE': '🇦🇪',
    'Çin (ÖİB)': '🇭🇰', 'China (SAR)': '🇭🇰',
    'Hırvatistan': '🇭🇷', 'Croatia': '🇭🇷'
}

def get_flag(country):
    return FLAGS.get(country, '🌍')

def generate():
    all_cities = []
    # Avoid backups and self
    files = sorted([f for f in os.listdir(CITIES_DIR) if f.endswith('.json') and not f.count('.bak') and f != 'cities_list.json'])
    
    for filename in files:
        city_id = filename.replace('.json', '')
        path = os.path.join(CITIES_DIR, filename)
        
        with open(path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except: continue
            
        if not isinstance(data, dict) or 'city' not in data:
            continue
            
        city_entry = {
            "id": city_id,
            "name": data.get('city', ''),
            "name_en": data.get('city_en', data.get('city', '')),
            "country": data.get('country', ''),
            "country_en": data.get('country_en', data.get('country', '')),
            "flag": get_flag(data.get('country', '')),
            "networkImage": data.get('heroImage', '')
        }
        all_cities.append(city_entry)
        
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_cities, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generated {len(all_cities)} cities in {OUTPUT_FILE}")

if __name__ == "__main__":
    generate()

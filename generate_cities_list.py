import json
import os

CITIES_DIR = 'assets/cities'
OUTPUT_FILE = 'assets/cities_list.json'

FLAGS = {
    "Türkiye": "🇹🇷", "Turkey": "🇹🇷",
    "İspanya": "🇪🇸", "Spain": "🇪🇸",
    "İtalya": "🇮🇹", "Italy": "🇮🇹",
    "Yunanistan": "🇬🇷", "Greece": "🇬🇷",
    "Arnavutluk": "🇦🇱", "Albania": "🇦🇱",
    "Karadağ": "🇲🇪", "Montenegro": "🇲🇪",
    "Hırvatistan": "🇭🇷", "Croatia": "🇭🇷",
    "Fransa": "🇫🇷", "France": "🇫🇷",
    "İsviçre": "🇨🇭", "Switzerland": "🇨🇭",
    "Almanya": "🇩🇪", "Germany": "🇩🇪",
    "Hollanda": "🇳🇱", "Netherlands": "🇳🇱",
    "Avusturya": "🇦🇹", "Austria": "🇦🇹",
    "Birleşik Krallık": "🇬🇧", "United Kingdom": "🇬🇧", "İngiltere": "🇬🇧",
    "Portekiz": "🇵🇹", "Portugal": "🇵🇹",
    "Çekya": "🇨🇿", "Czech Republic": "🇨🇿",
    "Norveç": "🇳🇴", "Norway": "🇳🇴",
    "Danimarka": "🇩🇰", "Denmark": "🇩🇰",
    "İsveç": "🇸🇪", "Sweden": "🇸🇪",
    "Finlandiya": "🇫🇮", "Finland": "🇫🇮",
    "Macaristan": "🇭🇺", "Hungary": "🇭🇺",
    "Sırbistan": "🇷🇸", "Serbia": "🇷🇸",
    "Bosna Hersek": "🇧🇦", "Bosnia": "🇧🇦",
    "BAE": "🇦🇪", "UAE": "🇦🇪",
    "Mısır": "🇪🇬", "Egypt": "🇪🇬",
    "Fas": "🇲🇦", "Morocco": "🇲🇦",
    "Tayland": "🇹🇭", "Thailand": "🇹🇭",
    "Japonya": "🇯🇵", "Japan": "🇯🇵",
    "Güney Kore": "🇰🇷", "South Korea": "🇰🇷",
    "Çin": "🇨🇳", "China": "🇨🇳", "Hong Kong": "🇭🇰",
    "ABD": "🇺🇸", "USA": "🇺🇸",
    "İrlanda": "🇮🇪", "Ireland": "🇮🇪",
    "İskoçya": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "Scotland": "🏴󠁧󠁢󠁳󠁣󠁴󠁿",
    "Belçika": "🇧🇪", "Belgium": "🇧🇪",
    "Singapur": "🇸🇬", "Singapore": "🇸🇬"
}

def get_flag(country):
    return FLAGS.get(country, "🌍")

def generate():
    cities_list = []
    for filename in sorted(os.listdir(CITIES_DIR)):
        # Sadece ana şehir JSON dosyalarını işle (batch, bak, tmp hariç)
        if (filename.endswith('.json') and
            not filename.endswith('.tmp') and
            not filename.endswith('.bak') and
            'batch' not in filename.lower() and
            'unique' not in filename.lower()):
            city_id = filename.replace('.json', '')
            path = os.path.join(CITIES_DIR, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    cities_list.append({
                        "id": city_id,
                        "name": data.get("city", city_id.capitalize()),
                        "name_en": data.get("city_en", city_id.capitalize()),
                        "country": data.get("country", ""),
                        "country_en": data.get("country_en", ""),
                        "flag": get_flag(data.get("country", "")),
                        "networkImage": data.get("heroImage", "")
                    })
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(cities_list, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated cities_list.json with {len(cities_list)} cities.")

if __name__ == "__main__":
    generate()

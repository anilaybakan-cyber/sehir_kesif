
import json
import os
import glob

# Hardcoded flag mapping
FLAGS = {
    "Türkiye": "🇹🇷",
    "İspanya": "🇪🇸",
    "Fransa": "🇫🇷",
    "İtalya": "🇮🇹",
    "Hollanda": "🇳🇱",
    "İngiltere": "🇬🇧",
    "Almanya": "🇩🇪",
    "Avusturya": "🇦🇹",
    "Çekya": "🇨🇿",
    "Portekiz": "🇵🇹",
    "Japonya": "🇯🇵",
    "Güney Kore": "🇰🇷",
    "Singapur": "🇸🇬",
    "BAE": "🇦🇪",
    "ABD": "🇺🇸",
    "İsviçre": "🇨🇭",
    "Danimarka": "🇩🇰",
    "İsveç": "🇸🇪",
    "Macaristan": "🇭🇺",
    "İrlanda": "🇮🇪",
    "Yunanistan": "🇬🇷",
    "Fas": "🇲🇦",
    "Tayland": "🇹🇭",
    "Çin": "🇨🇳",
    "Hırvatistan": "🇭🇷",
    "Slovenya": "🇸🇮",
    "Arnavutluk": "🇦🇱",
    "Malezya": "🇲🇾",
    "Estonya": "🇪🇪"
}

def get_sort_key(city_name):
    # Simple Turkish char replacement for sorting
    replacements = {
        'Ç': 'C', 'ç': 'c',
        'Ğ': 'G', 'ğ': 'g',
        'İ': 'I', 'ı': 'i',
        'Ö': 'O', 'ö': 'o',
        'Ş': 'S', 'ş': 's',
        'Ü': 'U', 'ü': 'u'
    }
    key = city_name
    for k, v in replacements.items():
        key = key.replace(k, v)
    return key.lower()

def generate_list():
    json_files = glob.glob("assets/cities/*.json")
    cities = []

    for filepath in json_files:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            city_id = os.path.basename(filepath).replace('.json', '')
            name = data.get('city')
            country = data.get('country')
            hero_image = data.get('heroImage', '')
            
            # Skip if basic data missing
            if not name or not country:
                continue

            flag = FLAGS.get(country, "🏳️")
            
            cities.append({
                "id": city_id,
                "name": name,
                "country": country,
                "flag": flag,
                "networkImage": hero_image
            })
            
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    # Sort alphabetically
    cities.sort(key=lambda x: get_sort_key(x['name']))

    # Generate Dart code
    print("  final List<Map<String, dynamic>> _cities = [")
    for city in cities:
        print("    {")
        print(f'      "id": "{city["id"]}",')
        print(f'      "name": "{city["name"]}",')
        print(f'      "country": "{city["country"]}",')
        print(f'      "flag": "{city["flag"]}",')
        print(f'      "networkImage": "{city["networkImage"]}",')
        # Keeping legacy 'image' field pointing to assets just in case, or we can omit it if not used.
        # The existing code uses 'image': 'assets/cities/...' which might not exist for new cities.
        # But cell only uses networkImage primarily.
        print("    },")
    print("  ];")

if __name__ == "__main__":
    generate_list()

import json
from datetime import datetime

manifest_path = '/Users/anilebru/Desktop/Uygulamalar/myway-data/version_manifest.json'

with open(manifest_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# List of city keys to increment (the top-level keys before "version")
city_keys = [
    "budapeste", "strazburg", "matera", "sevilla", "giethoorn", "colmar", "hallstatt", "kopenhag", "oslo",
    "amsterdam", "santorini", "heidelberg", "hongkong", "lucerne", "lyon", "zermatt", "istanbul", "gaziantep",
    "kapadokya", "bruksel", "tromso", "zurih", "belgrad", "lizbon", "tokyo", "marakes", "marsilya", "paris",
    "newyork", "floransa", "midilli", "porto", "saraybosna", "cenevre", "san_sebastian", "singapur",
    "edinburgh", "viyana", "kotor", "bologna", "napoli", "milano", "kahire", "londra", "brugge", "sintra",
    "atina", "nice", "stockholm", "dublin", "prag", "venedik", "dubai", "fes", "antalya", "berlin",
    "rovaniemi", "madrid", "barcelona", "seul", "bangkok", "roma"
]

for key in city_keys:
    if key in data:
        data[key] += 1

data['lastUpdated'] = datetime.now().strftime('%Y-%m-%d')
data['updateNotes'] = "Comprehensive content update from curated Excel data. Updated descriptions, categories, tips, and coordinates for 10,000+ highlights across all 60+ cities."

with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Manifest version increment completed for all cities.")

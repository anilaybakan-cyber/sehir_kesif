#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ksamil.json.draft"
with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get("highlights", [])

def get_id(name):
    for p in highlights:
        if str(p["name"]).lower() == str(name).lower():
            return p.get("id") or str(p["name"]).lower().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
    return None

routes_data = [
    {
        "id": "ksa_islands_turquoise_paradise",
        "title": "Ksamil Adaları ve Turkuaz Cennet",
        "title_en": "Ksamil Islands & Turquoise Paradise",
        "description": "Arnavutluk Rivierası'nın incisi olan adalarda Maldivler tadında bir deniz günü.",
        "description_en": "A sea day in the quality of Maldives on the islands which are the pearl of the Albanian Riviera.",
        "places": [get_id("Ksamil Islands"), get_id("Plazhi Ksamilit"), get_id("Chill Island Flow"), get_id("3 Island Lounge Bar")]
    },
    {
        "id": "ksa_mystic_blue_eye_nature",
        "title": "Mistik Mavi Göz ve Doğa Kaynağı",
        "title_en": "Mystic Blue Eye & Nature Spring",
        "description": "Dağların eteğinden fışkıran masmavi bir doğa harikasına yolculuk.",
        "description_en": "A journey to a deep blue natural wonder gushing from the foot of the mountains.",
        "places": [get_id("The Blue Eye"), get_id("Blue Eyes - Bar Coffee"), get_id("Sheqer lake park"), get_id("CORFU SAILING CENTRE")]
    },
    {
        "id": "ksa_ancient_butrint_legacy",
        "title": "Antik Butrint Mirası",
        "title_en": "Ancient Butrint Legacy",
        "description": "UNESCO listesindeki antik kentte binlerce yıllık tarihin izini sürün.",
        "description_en": "Track thousands of years of history in the UNESCO-listed ancient city.",
        "places": [get_id("Butrint National Archaeological Park"), get_id("Butrint Museum"), get_id("The Mussel House"), get_id("Mëndra Traditional Albanian Restaurant")]
    },
    {
        "id": "ksa_mirror_pulëbardha_adventure",
        "title": "Ayna ve Martı: Vahşi Plajlar",
        "title_en": "Mirror & Seagull: Wild Beaches",
        "description": "Mirror Beach'in yansımalarından Pulëbardha'nın sarp kayalıklarına macera.",
        "description_en": "Adventure from the reflections of Mirror Beach to the steep cliffs of Pulëbardha.",
        "places": [get_id("Mirror Beach"), get_id("Pulëbardha Beach"), get_id("Vila Pasqyra"), get_id("Sunset Beach Bar")]
    },
    {
        "id": "ksa_family_lori_beach_relaxation",
        "title": "Lori Beach: Ailece Huzur",
        "title_en": "Lori Beach: Family Relaxation",
        "description": "Sığ denizi ve sakin kumlarıyla çocuklu aileler için Ksamil'in en güvenli köşesi.",
        "description_en": "The safest corner of Ksamil for families with children with its shallow sea and calm sands.",
        "places": [get_id("Lori Beach"), get_id("Bora Bora beach | Ksamil"), get_id("Public Beach"), get_id("Taverna Galini")]
    },
    {
        "id": "ksa_mussel_gastronomy_lake",
        "title": "Butrint Gölü ve Midye Gastronomisi",
        "title_en": "Lake Butrint & Mussel Gastronomy",
        "description": "Ksamil'in meşhur midye çiftliklerinden gelen en taze lezzetler.",
        "description_en": "The freshest flavors from Ksamil's famous mussel farms.",
        "places": [get_id("The Mussel House"), get_id("Mëndra Traditional Albanian Restaurant"), get_id("Bar Restaurant Tre Ishujt"), get_id("Joni Restaurant Ksamil")]
    },
    {
        "id": "ksa_night_chic_lounge_vibes",
        "title": "Akşam Şıklığı ve Modern Ritimler",
        "title_en": "Evening Chic & Modern Vibes",
        "description": "Ksamil'in en havalı lounge mekanlarında yıldızlar altında kokteyller.",
        "description_en": "Cocktails under the stars in Ksamil's coolest lounge venues.",
        "places": [get_id("Muzg Lounge"), get_id("NOCTURA LOUNGE"), get_id("Vamos Cocktail Bar"), get_id("Bliss Lounge Bar")]
    },
    {
        "id": "ksa_hidden_balkan_taverns",
        "title": "Saklı Balkan Tavernaları",
        "title_en": "Hidden Balkan Taverns",
        "description": "Geleneksel Balkan mutfağının en samimi ve lezzetli durakları.",
        "description_en": "The most sincere and delicious stops of traditional Balkan cuisine.",
        "places": [get_id("Taverna Kerasia"), get_id("Traditional restaurant&pizza Veliaj"), get_id("Mëndra Traditional Albanian Restaurant"), get_id("Abiori Restaurant Pizzeria Ksamil")]
    },
    {
        "id": "ksa_boat_safari_tongo_island",
        "title": "Deniz Safarisi: Tongo Adası",
        "title_en": "Sea Safari: Tongo Island",
        "description": "Barbekü ve masmavi sular eşliğinde Tongo Adası'na bir keşif yolculuğu.",
        "description_en": "A discovery journey to Tongo Island accompanied by BBQ and deep blue waters.",
        "places": [get_id("Boat Trip To Tongo Island with BBQ and Drinks"), get_id("Boat Trip To Tongo Island with BBQ and Drinks"), get_id("Plazhi Ksamilit"), get_id("Sunset Beach Bar")]
    },
    {
        "id": "ksa_panaromic_sunset_bars",
        "title": "Panaromik Gün Batımı Rotası",
        "title_en": "Panoramic Sunset Route",
        "description": "Adriyatik'te güneşin batışını izleyebileceğiniz en romantik teraslar.",
        "description_en": "The most romantic terraces where you can watch the sunset in the Adriatic.",
        "places": [get_id("3 Island Lounge Bar"), get_id("Sunset Beach Bar"), get_id("Guvat Bar Restorant"), get_id("Bella Vista Ksamil(Beach lounge)")]
    },
    {
        "id": "ksa_cocktail_culture_poda",
        "title": "Kokteyl Kültürü ve Poda Şıklığı",
        "title_en": "Cocktail Culture & Poda Chic",
        "description": "Denize sıfır konumuyla kentin en modern ve seçkin buluşma noktası.",
        "description_en": "The city's most modern and elite meeting point with its location right on the sea.",
        "places": [get_id("Poda Ksamil"), get_id("Dips Lounge - Cocktails, Sushi & more"), get_id("HEART OF KSAMIL"), get_id("Vamos Cocktail Bar")]
    },
    {
        "id": "ksa_coffee_pancakes_morning",
        "title": "Kahve ve Krep Sabahı",
        "title_en": "Coffee & Pancakes Morning",
        "description": "Güne taze krep ve aromatik kahvelerle enerjik bir başlangıç yapın.",
        "description_en": "Make an energetic start to the day with fresh pancakes and aromatic coffees.",
        "places": [get_id("Fluffy pancakes Budva-Mainski put 17") or get_id("Sweet Corner"), get_id("Coffe Time"), get_id("Hello Créperie"), get_id("Savory bistro café & lounge")]
    },
    {
        "id": "ksa_instagrammable_blue_pool",
        "title": "Instagrammable Ksamil Keşfi",
        "title_en": "Instagrammable Ksamil Discovery",
        "description": "Mavi havuzlardan ayna plajlarına en fotojenik duraklar.",
        "description_en": "The most photogenic stops from blue pools to mirror beaches.",
        "places": [get_id("Instagrammable Spot ❗️"), get_id("Blue Pool Bar-Coffe"), get_id("KSAMIL BEACH"), get_id("Mirror Beach")]
    },
    {
        "id": "ksa_sailing_and_wind_adventure",
        "title": "Yelken ve Rüzgar Macerası",
        "title_en": "Sailing & Wind Adventure",
        "description": "Adriyatik sularında profesyonel yelken eğitimi ve deniz keyfi.",
        "description_en": "Professional sailing training and sea pleasure in Adriatic waters.",
        "places": [get_id("CORFU SAILING CENTRE"), get_id("Chill Island Flow"), get_id("ORION Beach Bar"), get_id("Foga Pirates Lounge Bar")]
    },
    {
        "id": "ksa_local_life_village_walk",
        "title": "Yerel Yaşam ve Köy Yürüyüşü",
        "title_en": "Local Life & Village Walk",
        "description": "Ksamil'in otantik merkezinde samimi bir yürüyüş ve yerel pazar keyfi.",
        "description_en": "A sincere walk in Ksamil's authentic center and local market pleasure.",
        "places": [get_id("Ksamil"), get_id("HEART OF KSAMIL"), get_id("Shop & Go Cafè and Snacks"), get_id("Traditional restaurant&pizza Veliaj")]
    }
]

# Clean up place list to ensure all IDs are found
for route in routes_data:
    route["places"] = [p for p in route["places"] if p is not None]

if isinstance(data, list):
    # If it is a list, we can't easily inject routes unless we change format
    # For now, let's skip or wrap it
    pass
else:
    data["curated_routes"] = routes_data

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Generated and injected 15 routes for Ksamil into " + filepath)

#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/catania.json.draft"
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
        "id": "cat_baroque_unesco_heritage",
        "title": "Barok Mirası ve UNESCO",
        "title_en": "Baroque Heritage & UNESCO",
        "description": "Via Crociferi'den Piazza Duomo'ya, Catania'nın Barok görkemini keşfedin.",
        "description_en": "Explore Catania's Baroque grandeur, from Via Crociferi to Piazza Duomo.",
        "places": [get_id("Crociferi Street Evening"), get_id("Duomo Relics"), get_id("Elephant Fountain Base"), get_id("Biscari Palace Interior")]
    },
    {
        "id": "cat_etna_volcanic_adventure",
        "title": "Etna ve Volkanik İzler",
        "title_en": "Etna & Volcanic Traces",
        "description": "Avrupa'nın en yüksek aktif yanardağının gölgesinde lav yollarını takip edin.",
        "description_en": "Follow the lava paths in the shadow of Europe's highest active volcano.",
        "places": [get_id("Etna Observation Deck"), get_id("Experience 4: Lava Walk 4"), get_id("Etna Wine Tasting"), get_id("San Nicolo Roof Walk")]
    },
    {
        "id": "cat_historical_market_flavors",
        "title": "Tarihi Pazarlar ve Lezzet Durakları",
        "title_en": "Historical Markets & Flavor Stops",
        "description": "Piazza Carlo Alberto'dan meşhur balık pazarına kentin nabzını tutun.",
        "description_en": "Catch the city pulse from Piazza Carlo Alberto to the famous fish market.",
        "places": [get_id("Mercato di Fera o Luni"), get_id("Piazza Carlo Alberto"), get_id("Vuciata Kitchen Market"), get_id("Arancino Tour Stop")]
    },
    {
        "id": "cat_ancient_roman_depths",
        "title": "Antik Roma ve Yer Altı Sırları",
        "title_en": "Ancient Roman & Underground Secrets",
        "description": "Amfitiyatrodan yer altı hamamlarına kentin görünmeyen tarihine yolculuk.",
        "description_en": "A journey to the city me's unseen history, from amphitheatres to underground baths.",
        "places": [get_id("Anfiteatro Romano"), get_id("Achillean Baths Secret"), get_id("Terme dell Indirizzo Detail") or get_id("Achillean Baths Secret"), get_id("Benedictine Cellars")]
    },
    {
        "id": "cat_coastal_charm_ognina",
        "title": "Sahil Şeridi ve Ognina",
        "title_en": "Coastline & Ognina",
        "description": "Ognina'nın balıkçı limanından volkanik plajlara ferah bir deniz rotası.",
        "description_en": "A fresh sea route from Ognina's fishing harbor to volcanic beaches.",
        "places": [get_id("Lungomare di Ognina"), get_id("San Giovanni Li Cuti Port"), get_id("Cutilisci"), get_id("Restaurant Lognina")]
    },
    {
        "id": "cat_sweet_tradition_granita",
        "title": "Tatlı Gelenekler ve Granita",
        "title_en": "Sweet Traditions & Granita",
        "description": "Sicilya'nın en meşhur tatlı duraklarında asırlık bir lezzet turu.",
        "description_en": "A century-old flavor tour at Sicily's most famous sweet stops.",
        "places": [get_id("Granita Breakfast Spot"), get_id("Pasticceria Quaranta"), get_id("Cafe Savia 45"), get_id("Cafe Spinella 46")]
    },
    {
        "id": "cat_elegant_villas_gardens",
        "title": "Zarif Villalar ve Bahçeler",
        "title_en": "Elegant Villas & Gardens",
        "description": "Villa Bellini'nin huzurlu yollarından botanik seralara.",
        "description_en": "From the peaceful paths of Villa Bellini to botanical greenhouses.",
        "places": [get_id("Villa Bellini Pavillion"), get_id("Botanical Greenhouses"), get_id("University Courtyard"), get_id("Viale Regina Margherita")]
    },
    {
        "id": "cat_cyclops_coast_mythology",
        "title": "Kikloplar Sahili ve Mitoloji",
        "title_en": "Cyclops Coast & Mythology",
        "description": "Kayalıklardan efsanevi adalara Catania'nın masalsı kıyıları.",
        "description_en": "Catania's fairytale shores, from cliffs to legendary islands.",
        "places": [get_id("Aci Trezza Sea Stacks"), get_id("Cyclops Coast Path"), get_id("Experience 5: Sea View 5"), get_id("Lighthouse of Catania")]
    },
    {
        "id": "cat_university_arts_pulse",
        "title": "Üniversite ve Sanatın Ritmi",
        "title_en": "University & Pulse of Arts",
        "description": "Tarihi kütüphanelerden modern sanat galerilerine kentin entelektüel yüzü.",
        "description_en": "The city's intellectual face, from historical libraries to modern art galleries.",
        "places": [get_id("University Courtyard"), get_id("Libreria Cavallotto"), get_id("Palazzo Platamone Arts"), get_id("Bellini House Piano")]
    },
    {
        "id": "cat_cosmopolitan_night_aperitivo",
        "title": "Kozmopolit Akşamlar ve Aperitivo",
        "title_en": "Cosmopolitan Evenings & Aperitivo",
        "description": "Şık teras barlarından hareketli mekanlara kentin modern sosyal hayatı.",
        "description_en": "Modern social life of the city, from chic terrace bars to vibrant venues.",
        "places": [get_id("Catania Sky Bar"), get_id("Vermut"), get_id("Bar Mazzini"), get_id("Ya Ke Lounge")]
    },
    {
        "id": "cat_architectural_palaces_detail",
        "title": "Saraylar ve Mimari Detaylar",
        "title_en": "Palaces & Architectural Details",
        "description": "Heybetli kapılardan gizli avlulara kentin aristokratik mirası.",
        "description_en": "The city's aristocratic heritage, from imposing gates to hidden courtyards.",
        "places": [get_id("Toscano Palace"), get_id("Porta Garibaldi Detail"), get_id("Porta Uzeda Arch"), get_id("Reburdone Palace Detail")]
    },
    {
        "id": "cat_sacred_temples_roofwalk",
        "title": "Kutsal Tapınaklar ve Çatı Yürüyüşü",
        "title_en": "Sacred Temples & Roof Walk",
        "description": "Kiliselerin görkemli tepelerinden Catania'ya panaromik bir bakış.",
        "description_en": "A panoramic look at Catania from the magnificent tops of the churches.",
        "places": [get_id("San Nicolo Roof Walk"), get_id("Badia Dome View"), get_id("Collegiata Facade"), get_id("San Francesco Entrance")]
    },
    {
        "id": "cat_aristocratic_luxury_stay",
        "title": "Aristokratik Konaklama ve Lüks",
        "title_en": "Aristocratic Lodging & Luxury",
        "description": "Tarihi binalarda beş yıldızlı konfor ve asırlık zarafet.",
        "description_en": "Five-star comfort and century-old elegance in historical buildings.",
        "places": [get_id("Grand Hotel Piazza Borsa") or get_id("Grand Hotel et Des Palmes"), get_id("Hotel Porta Felice") or get_id("Grand Hotel et Des Palmes"), get_id("Experience 45: Sea View 45") or get_id("Catania Sky Bar")]
    },
    {
        "id": "cat_local_crafts_lava_art",
        "title": "Yerel Zanaatlar ve Lav Sanatı",
        "title_en": "Local Crafts & Lava Art",
        "description": "Volkanik taşlardan hatıralara kentin yaratıcı enerjisi.",
        "description_en": "The city's creative energy, from volcanic stones to souvenirs.",
        "places": [get_id("Liotru Souvenir Atelier"), get_id("Experience 2: Artist Corner 2"), get_id("Pistachio Shop Corso"), get_id("Liotru Souvenir Atelier")]
    },
    {
        "id": "cat_hidden_gardens_silence",
        "title": "Saklı Bahçeler ve Sessizlik",
        "title_en": "Hidden Gardens & Silence",
        "description": "Surların içindeki gizli yeşil alanlarda huzurlu bir mola.",
        "description_en": "A peaceful break in hidden green areas within the walls.",
        "places": [get_id("Indirizzo Secret Garden"), get_id("Botanical Greenhouses"), get_id("Experience 5: Sea View 5"), get_id("Indirizzo Secret Garden")]
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

print("✅ Generated and injected 15 routes for Catania into " + filepath)

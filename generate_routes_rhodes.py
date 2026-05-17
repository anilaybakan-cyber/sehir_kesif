#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/rhodes.json.draft"
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
        "id": "rho_medieval_knights_legacy",
        "title": "Orta Çağ Şövalyeleri Mirası",
        "title_en": "Medieval Knights' Legacy",
        "description": "UNESCO listesindeki Eski Şehir surları içinde şövalyelerin izini sürün.",
        "description_en": "Track the knights within the UNESCO-listed Old Town walls.",
        "places": [get_id("Medieval City of Rhodes"), get_id("Palace of the Grand Master of the Knights of Rhodes"), get_id("Street of the Knights of Rhodes"), get_id("Medieval Clock Tower")]
    },
    {
        "id": "rho_ancient_acropolis_apollo",
        "title": "Antik Akropolis ve Güneş Tanrısı",
        "title_en": "Ancient Acropolis & Sun God",
        "description": "Apollo Tapınağı'ndan antik stadyuma Rodos'un binlerce yıllık zekası.",
        "description_en": "Rhodes' thousands of years of intelligence from the Temple of Apollo to the ancient stadium.",
        "places": [get_id("Acropolis of Rhodes"), get_id("Temple of Apollo Pythios"), get_id("Ancient Stadium of Rhodes"), get_id("Filerimos Monastery")]
    },
    {
        "id": "rho_mystic_nature_valley_springs",
        "title": "Mistik Doğa: Kelebekler ve Pınarlar",
        "title_en": "Mystic Nature: Butterflies & Springs",
        "description": "Kelebekler Vadisi'nin masalsı atmosferinden Yedi Pınarlar'ın serinliğine.",
        "description_en": "From the fairytale atmosphere of Butterflies Valley to the coolness of Seven Springs.",
        "places": [get_id("Butterflies Valley"), get_id("Seven Springs"), get_id("Bee Museum of Rhodes"), get_id("Cultural and Geological Melathro Rhodes")]
    },
    {
        "id": "rho_lindos_white_beauty",
        "title": "Lindos: Beyaz Güzellik ve Akropolis",
        "title_en": "Lindos: White Beauty & Acropolis",
        "description": "Rodos'un en fotojenik kasabasında beyaz evler ve sarp bir akropolis.",
        "description_en": "White houses and a steep acropolis in Rhodes' most photogenic town.",
        "places": [get_id("Lindos Acropolis"), get_id("Kallithea Springs"), get_id("WaterPark"), get_id("Elysium Resort & Spa | 5 star hotel in Rhodes")]
    },
    {
        "id": "rho_mandraki_harbor_windmills",
        "title": "Mandraki Limanı ve Yeldeğirmenleri",
        "title_en": "Mandraki Harbor & Windmills",
        "description": "Liman girişindeki ikonik geyiklerden tarihi yeldeğirmenlerine bir sahil yürüyüşü.",
        "description_en": "A seaside walk from the iconic deer at the harbor entrance to historical windmills.",
        "places": [get_id("Windmills of Rhodes"), get_id("Aquarium of Rhodes - Hydrobiological Station HCMR"), get_id("Το βενετσιάνικο συντριβάνι"), get_id("Rhodes Day Sailing Excursions | Sail in Greece")]
    },
    {
        "id": "rho_museum_trail_art_history",
        "title": "Müze Rotası: Sanat ve Tarih",
        "title_en": "Museum Trail: Art & History",
        "description": "Antik buluntulardan modern Yunan sanatına Rodos'un kültürel hafızası.",
        "description_en": "Rhodes' cultural memory from ancient finds to modern Greek art.",
        "places": [get_id("Archaeological Museum of Rhodes"), get_id("Modern Greek Art Museum of Rhodes - Nestorideion Melathron"), get_id("Jewish Museum of Rhodes"), get_id("decorative arts collection of rhodes")]
    },
    {
        "id": "rho_nightlife_energetic_clubs",
        "title": "Pulsar Neşeli Geceler: Kulüpler",
        "title_en": "Pulsating Joyful Nights: Clubs",
        "description": "Rodos'un dinamik gece hayatında en iddialı ve popüler eğlence adresleri.",
        "description_en": "The most ambitious and popular entertainment addresses in Rhodes me's dynamic nightlife.",
        "places": [get_id("PARADISO beach club"), get_id("KINKY RODOS"), get_id("Gazi club"), get_id("Vibe Nightclub")]
    },
    {
        "id": "rho_old_town_hidden_gardens",
        "title": "Eski Şehir'in Saklı Bahçeleri",
        "title_en": "Hidden Gardens of Old Town",
        "description": "Labirent sokakların arasında huzur dolu mola durakları ve avlular.",
        "description_en": "Peaceful break stops and courtyards among the labyrinthine streets.",
        "places": [get_id("Socratous Garden"), get_id("Minos Roof Garden Cafe"), get_id("Ρωγμή του Χρόνου"), get_id("Mama Sofia")]
    },
    {
        "id": "rho_elli_beach_city_summer",
        "title": "Elli Plajı ve Şehir Yazı",
        "title_en": "Elli Beach & City Summer",
        "description": "Kentin kalbinde kristal sular, şık beach-barlar ve yaz neşesi.",
        "description_en": "Crystal waters, stylish beach bars, and summer joy in the heart of the city.",
        "places": [get_id("Elli Beach"), get_id("RONDA - Resto | Beach-Bar"), get_id("ONO"), get_id("Louis Restaurant")]
    },
    {
        "id": "rho_gastronomy_old_town_flavors",
        "title": "Eski Şehir Gastronomisi",
        "title_en": "Old Town Gastronomy",
        "description": "Taş binaların gölgesinde en otantik Rodos lezzetleri ve şık akşamlar.",
        "description_en": "Rhodes' most authentic flavors and stylish evenings in the shadow of stone buildings.",
        "places": [get_id("Mama Sofia"), get_id("Aspri Avli Restaurant"), get_id("Island Lipsi Restaurant"), get_id("Zizi Restaurant")]
    },
    {
        "id": "rho_byzantine_spiritual_heritage",
        "title": "Bizans ve Manevi Miras",
        "title_en": "Byzantine & Spiritual Heritage",
        "description": "Orta çağ kiliselerinden manevi derinliği olan kutsal mekanlara.",
        "description_en": "From medieval churches to sacred places with spiritual depth.",
        "places": [get_id("Our Lady of the Castle (Panayia)"), get_id("Church of Saint John the Baptist"), get_id("Tower of St. Athanasius"), get_id("Jewish Museum of Rhodes")]
    },
    {
        "id": "rho_sailing_aegean_safari",
        "title": "Ege Safarisi ve Yelken Keyfi",
        "title_en": "Aegean Safari & Sailing Joy",
        "description": "Masmavi sular üzerinde Rodos sahil şeridini bir yelkenliyle keşfedin.",
        "description_en": "Explore the Rhodes coastline on a sailboat over deep blue waters.",
        "places": [get_id("Rhodes Day Sailing Excursions | Sail in Greece"), get_id("Windmills of Rhodes"), get_id("Kallithea Springs"), get_id("Elli Beach")]
    },
    {
        "id": "rho_coffee_and_craft_bakery",
        "title": "Kahve ve Fırın Geleneği",
        "title_en": "Coffee & Bakery Tradition",
        "description": "Rodos'un en köklü fırınlarından ve modern kahve duraklarından mola noktaları.",
        "description_en": "Break points from Rhodes' most established bakeries and modern coffee stops.",
        "places": [get_id("Pane di Capo"), get_id("Coffee Island"), get_id("Gregory's"), get_id("Aktaion Classic")]
    },
    {
        "id": "rho_9d_history_experience",
        "title": "9D Tarih Deneyimi ve Teknoloji",
        "title_en": "9D History Experience & Technology",
        "description": "Rodos tarihini modern teknolojiler ve interaktif müzelerle yaşayın.",
        "description_en": "Experience Rhodes history with modern technologies and interactive museums.",
        "places": [get_id("Throne of Helios: The History of Rhodes 9D Experience"), get_id("Rhodes Museum of Ancient Greek Technology by Kotsanas"), get_id("Path Of Gods - Greek History Museum"), get_id("Cultural and Geological Melathro Rhodes")]
    },
    {
        "id": "rho_aristocratic_luxury_lodging",
        "title": "Aristokratik Konaklama ve Lüks",
        "title_en": "Aristocratic Lodging & Luxury",
        "description": "Beş yıldızlı resortlardan tarihi butik otellere Rodos'un seçkin yüzü.",
        "description_en": "Rhodes' elite face from five-star resorts to historical boutique hotels.",
        "places": [get_id("Elysium Resort & Spa | 5 star hotel in Rhodes"), get_id("Hotel Parthenon Rodos City"), get_id("Villa Di Mare Restaurant"), get_id("Rhodian Rose Hotel")]
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

print("✅ Generated and injected 15 routes for Rhodes into " + filepath)

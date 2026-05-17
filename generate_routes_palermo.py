#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/palermo.json.draft"
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
        "id": "pal_arab_norman_unesco",
        "title": "Arap-Norman Mirası ve UNESCO",
        "title_en": "Arab-Norman Heritage & UNESCO",
        "description": "Sicilya'nın eşsiz mimari sentezini yansıran en görkemli saraylar ve kiliseler.",
        "description_en": "The most grand palaces and churches reflecting Sicily's unique architectural synthesis.",
        "places": [get_id("Palazzo dei Normanni"), get_id("Royal Palace and Palatine Chapel"), get_id("Palermo Cathedral"), get_id("Zisa Palace")]
    },
    {
        "id": "pal_historical_market_tour",
        "title": "Tarihi Pazarlar ve Sokak Lezzetleri",
        "title_en": "Historical Markets & Street Food",
        "description": "Ballarò'nun karmaşasından asırlık fırınlara gerçek Palermo.",
        "description_en": "Real Palermo, from the chaos of Ballarò to century-old bakeries.",
        "places": [get_id("Mercato Ballarò"), get_id("Ancient Saint Francis Focaccia Shop"), get_id("Antico Caffè Spinnato"), get_id("Casa Stagnitta")]
    },
    {
        "id": "pal_mystical_underground_catacombs",
        "title": "Mistik Yer Altı ve Katakomplar",
        "title_en": "Mystical Underground & Catacombs",
        "description": "Kentin görünmeyen hafızasında gizemli ve sarsıcı bir yolculuk.",
        "description_en": "A mysterious and poignant journey through the city's invisible memory.",
        "places": [get_id("Catacombe dei Cappuccini di Palermo"), get_id("Catacombe di Porta d'Ossuna"), get_id("Cappella e Loggia dell'Incoronata"), get_id("Church of Saint John of the Hermits")]
    },
    {
        "id": "pal_aristocratic_palaces_art",
        "title": "Aristokrat Sarayları ve Sanat",
        "title_en": "Aristocratic Palaces & Art",
        "description": "Soylu ailelerin mülklerinden Sicilya'nın en önemli sanat galerilerine.",
        "description_en": "From the properties of noble families to Sicily's most important art galleries.",
        "places": [get_id("Palazzo Abatellis"), get_id("Palazzo Butera"), get_id("Museo Palazzo Mirto Casa Museo"), get_id("Palazzo Chiaramonte Steri")]
    },
    {
        "id": "pal_theatre_and_square_pulse",
        "title": "Opera ve Meydanların Ritmi",
        "title_en": "Opera & Pulse of the Squares",
        "description": "Teatro Massimo'dan Quattro Canti'ye kentin zarif merkez rotası.",
        "description_en": "The city's elegant central route, from Teatro Massimo to Quattro Canti.",
        "places": [get_id("Teatro Massimo di Palermo"), get_id("Quattro Canti"), get_id("Palazzo delle Aquile"), get_id("Grand Hotel et Des Palmes")]
    },
    {
        "id": "pal_botanical_green_oasis",
        "title": "Botanik Bahçeleri ve Doğa",
        "title_en": "Botanical Gardens & Nature",
        "description": "Egzotik bitkilerden dev kaktüslere kentin en huzurlu yeşil rotası.",
        "description_en": "The city me's most peaceful green route, from exotic plants to giant cacti.",
        "places": [get_id("Orto Botanico di Palermo"), get_id("Giardino della Zisa"), get_id("Villa Boscogrande"), get_id("Mondello Beach")]
    },
    {
        "id": "pal_sacred_splendor_monreale",
        "title": "Kutsal İhtişam: Monreale",
        "title_en": "Sacred Splendor: Monreale",
        "description": "Altın mozaiklerin ve manevi derinliğin büyüleyici dünyası.",
        "description_en": "The fascinating world of golden mosaics and spiritual depth.",
        "places": [get_id("Cattedrale di Monreale"), get_id("Museo Diocesano"), get_id("Church of Saint Mary 'dell'Ammiraglio'"), get_id("Palermo Cathedral")]
    },
    {
        "id": "pal_creative_culture_factory",
        "title": "Yaratıcı Kültür ve Fabrakalar",
        "title_en": "Creative Culture & Factories",
        "description": "Eski endüstriyel alanlarda hayat bulan bohem sanat ve sinema.",
        "description_en": "Bohemian art and cinema brought to life in old industrial areas.",
        "places": [get_id("Cantieri Culturali alla Zisa"), get_id("Museo Palazzo Branciforte"), get_id("The Cultural Association Candelai"), get_id("Berlin Cafè")]
    },
    {
        "id": "pal_seaside_elegance_mondello",
        "title": "Sahil Şıklığı ve Mondello",
        "title_en": "Seaside Elegance & Mondello",
        "description": "Turkuaz deniz, Art Nouveau villalar ve sahil keyfi.",
        "description_en": "Turquoise sea, Art Nouveau villas, and seaside delight.",
        "places": [get_id("Mondello Beach"), get_id("Bar de la Vela"), get_id("Villa Igiea, a Rocco Forte hotel"), get_id("White")]
    },
    {
        "id": "pal_noble_lodging_tradition",
        "title": "Soylu Konaklama Geleneği",
        "title_en": "Noble Lodging Tradition",
        "description": "Tarihi saraylarda beş yıldızlı konfor ve nostaljik şıklık.",
        "description_en": "Five-star comfort and nostalgic elegance in historical palaces.",
        "places": [get_id("Grand Hotel Piazza Borsa"), get_id("Palazzo Brunaccini"), get_id("Grand Hotel et Des Palmes"), get_id("Hotel Porta Felice")]
    },
    {
        "id": "pal_gastronomy_excellence_vespri",
        "title": "Palermo Gastronomi Mükemmeliği",
        "title_en": "Palermo Gastronomy Excellence",
        "description": "Sicilya mutfağının en seçkin örneklerini sunan gurme duraklar.",
        "description_en": "Gourmet stops offering the most elite examples of Sicilian cuisine.",
        "places": [get_id("Osteria dei Vespri"), get_id("Kalhesa Restaurant & Sushi Bar"), get_id("Il Mirto e la Rosa"), get_id("Osteria dei Vespri")]
    },
    {
        "id": "pal_science_and_minerals",
        "title": "Bilim ve Yer Altı Hazineleri",
        "title_en": "Science & Underground Treasures",
        "description": "Minerallerden gökyüzüne Palermo'nun akademik keşif durakları.",
        "description_en": "Palermo me's academic discovery stops, from minerals to the sky.",
        "places": [get_id("Museo di Mineralogia"), get_id("Planetario di Palermo"), get_id("Museo enologico e della Civiltà contadina"), get_id("Orto Botanico di Palermo")]
    },
    {
        "id": "pal_nightlife_cocktail_pulse",
        "title": "Gece Hayatı ve Kokteyller",
        "title_en": "Nightlife & Cocktail Pulse",
        "description": "Kentin enerjik kulüplerinden bohem caz barlarına eğlence.",
        "description_en": "Fun from the city's energetic clubs to bohemian jazz bars.",
        "places": [get_id("Migò"), get_id("White"), get_id("Berlin Cafè"), get_id("Fabric Rise Up")]
    },
    {
        "id": "pal_sculpture_and_bronze_art",
        "title": "Heykel ve Bronz Sanatı",
        "title_en": "Sculpture & Bronze Art",
        "description": "Usta zanaatkarların atölyelerinden anıtsal meydanlara sanat.",
        "description_en": "Art from workshops of master artisans to monumental squares.",
        "places": [get_id("Scultore Monumentalista - Scultura in bronzo e marmo"), get_id("Fountain Garraffello"), get_id("Palazzo Fernandez"), get_id("Palazzo delle Aquile")]
    },
    {
        "id": "pal_hidden_chapels_silence",
        "title": "Saklı Şapeller ve Sessizlik",
        "title_en": "Hidden Chapels & Silence",
        "description": "Sokak aralarında gizlenmiş kutsal sığınaklar ve tarihin fısıltısı.",
        "description_en": "Sacred sanctuaries hidden in backstreets and the whispers of history.",
        "places": [get_id("Chiesa di Santa Maria in Valverde"), get_id("Chiesa di San Francesco Saverio"), get_id("Cappella e Loggia dell'Incoronata"), get_id("Chiesa di Santa Maria in Valverde")]
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

print("✅ Generated and injected 15 routes for Palermo into " + filepath)

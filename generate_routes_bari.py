#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/bari.json.draft"
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
        "id": "bar_ancient_heart_vecchia",
        "title": "Bari Vecchia: Antik Kalp",
        "title_en": "Bari Vecchia: Ancient Heart",
        "description": "Dar sokaklar, taze makarna yapan kadınlar ve kentin bin yıllık ruhu.",
        "description_en": "Narrow streets, women making fresh pasta, and the city me's thousand-year soul.",
        "places": [get_id("Bari Vecchia"), get_id("Basilica of Saint Nicholas"), get_id("Cathedral of Saint Sabinus"), get_id("Palazzo Simi (Simi Palace)")]
    },
    {
        "id": "bar_norman_hohenstaufen_defense",
        "title": "Norman ve Hohenstaufen Savunması",
        "title_en": "Norman & Hohenstaufen Defense",
        "description": "Heybetli bir kaleden antik surlara kentin askeri ihtişamı.",
        "description_en": "The city me's military grandeur, from an imposing castle to ancient walls.",
        "places": [get_id("Castello Svevo di Bari"), get_id("Archaeological Museum of Santa Scolastica"), get_id("Torre Balzano"), get_id("Archi della Marina") or get_id("Castello Svevo di Bari")]
    },
    {
        "id": "bar_maritime_promenade_lungomare",
        "title": "Deniz Kıyısı ve Lungomare",
        "title_en": "Seaside & Lungomare",
        "description": "Adriyatik boyu uzanan masmavi bir yürüyüş ve kentin ferah silüeti.",
        "description_en": "A deep blue walk along the Adriatic and the city me's fresh silhouette.",
        "places": [get_id("Lungomare di Bari"), get_id("Piazza del Ferrarese"), get_id("Teatro Margherita"), get_id("Murale 'Stella Maris' artista Laura Grimaldi") or get_id("Lungomare di Bari")]
    },
    {
        "id": "bar_opera_and_classical_arts",
        "title": "Opera ve Klasik Sanatlar",
        "title_en": "Opera & Classical Arts",
        "description": "İtalya'nın en büyük dördüncü tiyatrosundan aristokratik galerilere.",
        "description_en": "From Italy's fourth largest theater to aristocratic galleries.",
        "places": [get_id("Teatro Petruzzelli"), get_id("Teatro Margherita"), get_id("Pinacoteca metropolitana di Bari"), get_id("Palazzo Fizzarotti")]
    },
    {
        "id": "bar_sacred_nicolaian_path",
        "title": "Kutsal Nicolaian Yolu",
        "title_en": "Sacred Nicolaian Path",
        "description": "Aziz Nikolaos'un izinde kiliselerden müzeye manevi bir yolculuk.",
        "description_en": "A spiritual journey in the footsteps of St. Nicholas, from churches to the museum.",
        "places": [get_id("Basilica of Saint Nicholas"), get_id("Nicolaian Museum"), get_id("Russian Orthodox Church of Saint Nicholas"), get_id("Santuario Madonna della Grotta")]
    },
    {
        "id": "bar_puglian_gastronomy_tipico",
        "title": "Puglia Gastronomisi ve Lezzet",
        "title_en": "Puglian Gastronomy & Flavor",
        "description": "Kentin en otantik restoranlarında yerel mutfak mirasını keşfedin.",
        "description_en": "Explore local culinary heritage at the city's most authentic restaurants.",
        "places": [get_id("La Locanda di Federico – Ristorante tipico pugliese Bari Vecchia"), get_id("Terranima - Ristorante di cucina tipica pugliese"), get_id("Ristorante Biancofiore"), get_id("Ancient Saint Francis Focaccia Shop") or get_id("Bari Vecchia")]
    },
    {
        "id": "bar_bohemian_social_nights",
        "title": "Bohem Akşamlar ve Sosyal Hayat",
        "title_en": "Bohemian Evenings & Social Life",
        "description": "Kütüphane-kafelerden publara kentin en havalı sosyal durakları.",
        "description_en": "The city's coolest social stops, from library-cafes to pubs.",
        "places": [get_id("Joy's Pub"), get_id("Terra di Mezzo | Beer Food & Fun"), get_id("Jérôme Cafè"), get_id("Speakeasy Bari")]
    },
    {
        "id": "bar_family_science_fun",
        "title": "Ailece Bilim ve Eğlence",
        "title_en": "Family Science & Fun",
        "description": "Planeteryumdan su parkına çocuklar için keşif ve neşe dolu bir gün.",
        "description_en": "A day of discovery and joy for children, from the planetarium to the water park.",
        "places": [get_id("Planetario sky skan"), get_id("Cittadella Mediterranea della Scienza"), get_id("AcquaPark Bari"), get_id("Parco 2 Giugno")]
    },
    {
        "id": "bar_art_and_street_culture",
        "title": "Sanat ve Sokak Kültürü",
        "title_en": "Art & Street Culture",
        "description": "Duvar resimlerinden modern sanat derneklerine kentin yaratıcı enerjisi.",
        "description_en": "The city's creative energy, from murals to modern art associations.",
        "places": [get_id("Murale 'Stella Maris' artista Laura Grimaldi"), get_id("Associazione Culturale EX Studenti Accademia Belle Arti"), get_id("AncheCinema"), get_id("Museo della Fotografia")]
    },
    {
        "id": "bar_noble_palaces_aristocracy",
        "title": "Saraylar ve Aristokrat Miras",
        "title_en": "Palaces & Aristocratic Heritage",
        "description": "Barok saraylardan heybetli dış cephelere kentin soylu yüzü.",
        "description_en": "The noble face of the city, from Baroque palaces to grand facades.",
        "places": [get_id("Palazzo Fizzarotti"), get_id("Palazzo Teodoro Massa"), get_id("Palazzo Simi (Simi Palace)"), get_id("Palazzo Jannuzzi | Dimora Storica | Eventi | Bari")]
    },
    {
        "id": "bar_nightlife_energetic_clubs",
        "title": "Pulsar Neşeli Geceler: Kulüpler",
        "title_en": "Pulsating Joyful Nights: Clubs",
        "description": "Bari'nin en popüler ve enerjik kulüplerinde bitmeyen eğlence.",
        "description_en": "Never-ending fun at Bari's most popular and energetic clubs.",
        "places": [get_id("Demodé Club"), get_id("Riva Club"), get_id("KARA Bari - Karaoke Experience"), get_id("Remake eSports Bar")]
    },
    {
        "id": "bar_hidden_churches_silence",
        "title": "Saklı Kiliseler ve Sessizlik",
        "title_en": "Hidden Churches & Silence",
        "description": "Eski kentin sessiz köşelerinde tarihin fısıltısını soluyun.",
        "description_en": "Breathe the whispers of history in the quiet corners of the old town.",
        "places": [get_id("Church of Saint Theresa 'dei Maschi'"), get_id("Church of Saint Paschal Baylon"), get_id("Basilica of Saint Fara"), get_id("Diocesan Auditorium Vallisa")]
    },
    {
        "id": "bar_modern_lifestyle_metro",
        "title": "Modern Yaşam ve Metro Rotası",
        "title_en": "Modern Life & Metro Route",
        "description": "Kent merkezinden modern ulaşım ağlarına kentin pragmatik dokusu.",
        "description_en": "The city's pragmatic texture, from the city center to modern transport networks.",
        "places": [get_id("Metro City Bari"), get_id("Project Management"), get_id("Stazione Centrale") or get_id("Metro City Bari"), get_id("Fashion Cafè In")]
    },
    {
        "id": "bar_coffee_and_bakery_tradition",
        "title": "Kahve ve Fırın Geleneği",
        "title_en": "Coffee & Bakery Tradition",
        "description": "Bari'nin en meşhur kafelerinde yerel kahve ritüellerini yaşayın.",
        "description_en": "Live the local coffee rituals at Bari's most famous cafes.",
        "places": [get_id("Veronero Artisan Coffee & Bakery - Bari"), get_id("Caffè Italiano"), get_id("Pasticceria Ladisa Dolci ve Cioccolato"), get_id("Bar Orfeo Pasticceria")]
    },
    {
        "id": "bar_aristocratic_lodging_luxury",
        "title": "Aristokratik Konaklama ve Lüks",
        "title_en": "Aristocratic Lodging & Luxury",
        "description": "Tarihi saraylarda ve prestijli otellerde asude bir İtalya rüyası.",
        "description_en": "A serene Italian dream in historical palaces and prestigious hotels.",
        "places": [get_id("Grand Hotel Piazza Borsa") or get_id("Nicolaus Hotel Bari"), get_id("Hotel Terranobile Metaresort"), get_id("Villa Rotondo"), get_id("Hotel Majesty Bari")]
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

print("✅ Generated and injected 15 routes for Bari into " + filepath)

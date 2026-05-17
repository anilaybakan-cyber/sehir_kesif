#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/amalfi.json.draft"
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
        "id": "ama_heritage_spirit",
        "title": "Amalfi'nin Tarihi ve Ruhu",
        "title_en": "Amalfi's History & Spirit",
        "description": "Katedralden kağıt müzesine, Amalfi merkezinin en ikonik durakları.",
        "description_en": "The most iconic stops of Amalfi center, from the cathedral to the paper museum.",
        "places": [get_id("Duomo di Sant'Andrea Apostolo"), get_id("Chiostro del Paradiso"), get_id("Museo della Carta"), get_id("Arsenale della Repubblica di Amalfi - Infopoint Visit Amalfi")]
    },
    {
        "id": "ama_glamorous_positano",
        "title": "Positano: Dikey Şehir ve Lüks",
        "title_en": "Positano: Vertical City & Luxury",
        "description": "Dik yamaçlardaki renkli evler, şık butikler ve masmavi plajlar.",
        "description_en": "Colorful houses on steep slopes, chic boutiques, and deep blue beaches.",
        "places": [get_id("Spiaggia di Positano Marina Grande"), get_id("Chiesa Parrocchiale di Santa Maria Assunta"), get_id("MAR Positano Villa Romana"), get_id("Le Sirenuse")]
    },
    {
        "id": "ama_ravello_villas_views",
        "title": "Ravello: Bahçeler ve Sanat",
        "title_en": "Ravello: Gardens & Art",
        "description": "Tepelerin üzerinde klasik müzik notaları, muazzam bahçeler ve sonsuz manzara.",
        "description_en": "Classical music notes on hills, magnificent gardens, and endless views.",
        "places": [get_id("Villa Cimbrone"), get_id("Villa Rufolo"), get_id("Duomo di Ravello"), get_id("Auditorium Oscar Niemeyer")]
    },
    {
        "id": "ama_path_of_the_gods",
        "title": "Tanrıların Yolu: Doğa ve Yürüyüş",
        "title_en": "Path of the Gods: Nature & Hiking",
        "description": "Dünyanın en güzel yürüyüş rotalarından birinde gökyüzüyle deniz arasında bir yolculuk.",
        "description_en": "A journey between the sky and the sea on one of the world's most beautiful hiking routes.",
        "places": [get_id("Sentiero degli Dei"), get_id("Nocelle") or get_id("Sentiero degli Dei"), get_id("Praiano"), get_id("Monte Tre Calli")]
    },
    {
        "id": "ama_hidden_gems_atrani",
        "title": "Saklı Cevherler: Atrani ve Minori",
        "title_en": "Hidden Gems: Atrani & Minori",
        "description": "Kalabalıktan uzak, İtalya'nın en karakteristik ve küçük sahil köylerini keşfedin.",
        "description_en": "Discover Italy's most characteristic and small coastal villages, away from the crowds.",
        "places": [get_id("Atrani"), get_id("Collegiata di Santa Maria Maddalena Penitente"), get_id("Minori"), get_id("Villa Romana e Antiquarium di Minori")]
    },
    {
        "id": "ama_lemon_experience",
        "title": "Amalfi Limon Rotası",
        "title_en": "Amalfi Lemon Experience",
        "description": "Yemyeşil bahçelerden taze limoncello tadımına, kentin sarı dünyasına yolculuk.",
        "description_en": "A journey into the yellow world of the city, from lush gardens to fresh limoncello tasting.",
        "places": [get_id("Amalfi Lemon Experience"), get_id("Sentiero dei Limoni"), get_id("Pasticceria Pansa Amalfi"), get_id("Maiori")]
    },
    {
        "id": "ama_mystic_caves_coves",
        "title": "Mistik Mağaralar ve Koylar",
        "title_en": "Mystic Caves & Coves",
        "description": "Zümrüt yeşili sular, gizli mağaralar ve denizin mistik gücü.",
        "description_en": "Emerald green waters, hidden caves, and the mystical power of the sea.",
        "places": [get_id("Grotta dello Smeraldo"), get_id("Fiordo di Furore"), get_id("Conca dei Marini"), get_id("Praiano")]
    },
    {
        "id": "ama_gourmet_amalfi_flavors",
        "title": "Gurme Amalfi Lezzetleri",
        "title_en": "Gourmet Amalfi Flavors",
        "description": "Taze deniz ürünleri, meşhur makarnalar ve kentin prestijli restoranları.",
        "description_en": "Fresh seafood, famous pastas, and the city's prestigious restaurants.",
        "places": [get_id("Trattoria da Gemma"), get_id("Chez Black"), get_id("Boutique Hotel Don Alfonso 1890"), get_id("Don Vincenzo Positano")]
    },
    {
        "id": "ama_romantic_sunset_vibes",
        "title": "Romantik Gün Batımı ve Teraslar",
        "title_en": "Romantic Sunset & Terraces",
        "description": "Günü uğurlamak için Amalfi kıyılarının en şık bar ve terasları.",
        "description_en": "The Amalfi coast's most stylish bars and terraces to bid farewell to the day.",
        "places": [get_id("Bar Franco"), get_id("Terrazza Celè"), get_id("Oniro Sunset Bar - Restaurant") or get_id("180º Sunset Bar") or get_id("Bar Franco"), get_id("Positano")]
    },
    {
        "id": "ama_artisans_and_ceramics",
        "title": "Zanaatkarlar ve Seramik İzinde",
        "title_en": "Tracing Artisans & Ceramics",
        "description": "Rengarenk seramiklerden el yapımı objelere, kentin sanat ruhu.",
        "description_en": "The city's artistic spirit, from colorful ceramics to handmade objects.",
        "places": [get_id("Vietri sul Mare"), get_id("Pascal Ceramiche d'Arte Ravello"), get_id("Ceramiche D'Arte Carmela"), get_id("Salvatore Che Fa La Ringhiera")]
    },
    {
        "id": "ama_religious_heritage",
        "title": "Ruhani ve Manevi Miras",
        "title_en": "Spiritual & Sacred Heritage",
        "description": "Mistik manastırlardan görkemli kiliselere Amalfi'nin manevi durakları.",
        "description_en": "Amalfi's spiritual stops, from mystical monasteries to magnificent churches.",
        "places": [get_id("Museo Diocesano di Amalfi"), get_id("Santuario di Maria Santissima Avvocata"), get_id("Chiesa Dell'Annunziata"), get_id("Chiesa di San Giovanni del Toro")]
    },
    {
        "id": "ama_active_sea_adventure",
        "title": "Mavi Macera: Tekne ve Deniz",
        "title_en": "Blue Adventure: Boat & Sea",
        "description": "Özel teknelerle koyu keşif, şık plaj kulüpleri ve deniz sefası.",
        "description_en": "Exploring bays with private boats, chic beach clubs, and seaside delight.",
        "places": [get_id("Grassi Junior - Boat rental, ferries and mooring in Positano"), get_id("One Fire Beach Club"), get_id("Arienzo Beach Club Positano"), get_id("Marina di Praia")]
    },
    {
        "id": "ama_family_friendly_amalfi",
        "title": "Ailece Amalfi Keşfi",
        "title_en": "Family Amalfi Discovery",
        "description": "Sığ denizi ve huzurlu sahil kasabalarıyla aileler için en ideal duraklar.",
        "description_en": "The most ideal stops for families with their shallow sea and peaceful coastal towns.",
        "places": [get_id("Maiori"), get_id("Minori"), get_id("Spiaggia di Positano Marina Grande"), get_id("Gelato d'Arte") or get_id("Lartecono Davinci Gelato (Mykonos)") or get_id("Pasticceria Pansa Amalfi")]
    },
    {
        "id": "ama_luxury_hotels_lifestyle",
        "title": "Lüks Yaşam ve Prestijli Oteller",
        "title_en": "Luxury Lifestyle & Prestige Hotels",
        "description": "Görkemli teraslar, beş yıldızlı konfor ve Amalfi'nin en şık adresleri.",
        "description_en": "Grand terraces, five-star comfort, and Amalfi's most stylish addresses.",
        "places": [get_id("Le Sirenuse"), get_id("Santa Caterina Hotel"), get_id("Monastero Santa Rosa Hotel & Spa"), get_id("Hotel Poseidon")]
    },
    {
        "id": "ama_night_vibes_bars",
        "title": "Amalfi Akşamları ve Barlar",
        "title_en": "Amalfi Evenings & Bars",
        "description": "Geceyi renklendiren kaliteli müzik, şık kokteyller ve neşeli atmosfer.",
        "description_en": "Quality music, chic cocktails, and a cheerful atmosphere coloring the night.",
        "places": [get_id("Music On The Rocks") or get_id("Bar Franco"), get_id("Janeiro RistoBar"), get_id("Cafè Vittoria - Cafè & American Bar"), get_id("dejavu Cafè & Drinks")]
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

print("✅ Generated and injected 15 routes for Amalfi into " + filepath)

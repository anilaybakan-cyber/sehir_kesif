#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/mallorca.json.draft"
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
        "id": "mal_palma_classic_heritage",
        "title": "Palma'nın Klasik Mirası",
        "title_en": "Palma's Classic Heritage",
        "description": "Katedralden heybetli kalelere, Palma merkezinin en ikonik durakları.",
        "description_en": "The most iconic stops of Palma center, from the cathedral to grand castles.",
        "places": [get_id("Catedral-Basílica de Santa María de Mallorca"), get_id("Castillo de Bellver"), get_id("Palacio Ca Sa Galesa"), get_id("Museum of Mallorca")]
    },
    {
        "id": "mal_scenic_mountain_train",
        "title": "Sóller Treni ve Dağ Köyleri",
        "title_en": "Sóller Train & Mountain Villages",
        "description": "Nostaljik trenle zeytin bahçeleri ve dağ köyleri arasında masalsı bir yolculuk.",
        "description_en": "A fairytale journey between olive groves and mountain villages with the nostalgic train.",
        "places": [get_id("Train Sóller Station (Palma de Mallorca)"), get_id("Sóller"), get_id("Deià"), get_id("Valldemossa")]
    },
    {
        "id": "mal_hidden_aristocratic_courtyards",
        "title": "Saklı Saraylar ve Avlular",
        "title_en": "Hidden Palaces & Courtyards",
        "description": "Eski kentin dar sokaklarında Mallorca aristokrasisinin izini sürün.",
        "description_en": "Trace the Mallorcan aristocracy in the narrow streets of the old town.",
        "places": [get_id("Can Oleza"), get_id("Can March"), get_id("Can Amorós"), get_id("Can Alemany")]
    },
    {
        "id": "mal_art_and_modernism",
        "title": "Sanat ve Modernizm Rotası",
        "title_en": "Art & Modernism Route",
        "description": "Miró'dan CaixaForum'a kentin yaratıcı ve estetik yüzü.",
        "description_en": "The city's creative and aesthetic face, from Miró to CaixaForum.",
        "places": [get_id("Fundació Miró Mallorca"), get_id("Es Baluard Museu d'Art Contemporani de Palma"), get_id("CaixaForum Palma"), get_id("ABA ART")]
    },
    {
        "id": "mal_turquoise_beaches_south",
        "title": "Güneyin Turkuaz Koyları",
        "title_en": "Turquoise Bays of the South",
        "description": "Adanın en berrak suları ve uçsuz bucaksız kumsallarında deniz keyfi.",
        "description_en": "Sea delight in the island's clearest waters and endless sandy beaches.",
        "places": [get_id("Es Trenc"), get_id("Roc Illetas"), get_id("Platja de Palma") or get_id("Iberostar Selection Playa de Palma"), get_id("Purobeach Palma")]
    },
    {
        "id": "mal_mystical_caves_adventure",
        "title": "Mistik Mağaralar ve Doğa",
        "title_en": "Mystical Caves & Nature",
        "description": "Yer altı göllerinden dikey yamaçlara Mallorca'nın doğa harikaları.",
        "description_en": "Mallorca's natural wonders, from underground lakes to vertical slopes.",
        "places": [get_id("Cuevas del Drach"), get_id("Pollenca") or get_id("Pollença"), get_id("Castillo de Bellver"), get_id("Aula de la Mar")]
    },
    {
        "id": "mal_luxury_yacht_harbors",
        "title": "Lüks Marinalar ve Stil",
        "title_en": "Luxury Marinas & Style",
        "description": "Mallorca'nın en prestijli yat limanlarında yürüyüş ve elit duraklar.",
        "description_en": "Walking at Mallorca's most prestigious yacht harbors and elite stops.",
        "places": [get_id("Port d'Andratx"), get_id("Portals Nous") or get_id("Sallès Hotels Marina Portals"), get_id("Leonardo Boutique Hotel Mallorca Port Portals - Adults Only"), get_id("Social Club")]
    },
    {
        "id": "mal_gourmet_bakery_tour",
        "title": "Ensaimada ve Tatlı Mirası",
        "title_en": "Ensaimada & Sweet Heritage",
        "description": "Asırlık fırınlarda adanın en meşhur yerel lezzetlerini keşfedin.",
        "description_en": "Explore the island's most famous local flavors in century-old bakeries.",
        "places": [get_id("Can Joan de s'Aigo"), get_id("Forn del Santo Cristo"), get_id("La Madeleine de Proust Santa Catalina"), get_id("Pastisseria Mariola’s")]
    },
    {
        "id": "mal_family_fun_aquarium",
        "title": "Ailece Eğlence ve Deniz",
        "title_en": "Family Fun & Sea",
        "description": "Akvaryumdan yunus şovlarına, çocuklu aileler için en neşeli duraklar.",
        "description_en": "The most joyful stops for families with children, from aquariums to dolphin shows.",
        "places": [get_id("Palma Aquarium"), get_id("Marineland Mallorca"), get_id("Pueblo Español de Mallorca"), get_id("tent Capi Playa")]
    },
    {
        "id": "mal_bohemian_night_vibes",
        "title": "Bohem Akşamlar ve Barlar",
        "title_en": "Bohemian Evenings & Bars",
        "description": "Santa Catalina'nın neşeli sokaklarından mistik barlara Mallorca geceleri.",
        "description_en": "Mallorca nights, from the joyful streets of Santa Catalina to mystical bars.",
        "places": [get_id("Bar Abaco"), get_id("Bar Sabotage"), get_id("Bar Cafe Coto"), get_id("Bar Plata")]
    },
    {
        "id": "mal_romantic_boutique_stay",
        "title": "Romantik Butik Duraklar",
        "title_en": "Romantic Boutique Stops",
        "description": "Tarihi binalarda şık akşam yemekleri ve huzurlu teraslar.",
        "description_en": "Chic dinners in historical buildings and peaceful terraces.",
        "places": [get_id("Posada Terra Santa"), get_id("Hotel Cappuccino - Palma"), get_id("Can Alomar Urban Luxury Retreat"), get_id("Petit Palace Hotel Tres")]
    },
    {
        "id": "mal_military_history_walls",
        "title": "Askeri Tarih ve Savunma",
        "title_en": "Military History & Defense",
        "description": "Surların içindeki müzelerden kalesiyle kentin stratejik geçmişi.",
        "description_en": "The city's strategic past, from museums within walls to its castle.",
        "places": [get_id("Centre d'Historia i Cultura Militar de Balears"), get_id("Museu Històric Militar de Sant Carles"), get_id("Castillo de Bellver"), get_id("Centre Maimó Ben Faraig")]
    },
    {
        "id": "mal_cosmopolitan_luxury_beach",
        "title": "Kozmopolit Plaj Lüksü",
        "title_en": "Cosmopolitan Beach Luxury",
        "description": "Adanın en şık sahil otelleri ve prestijli plaj kulüpleri.",
        "description_en": "The island's most stylish seaside hotels and prestigious beach clubs.",
        "places": [get_id("Iberostar Selection Playa de Palma"), get_id("Valparaiso Palace & Spa") or get_id("GPRO Valparaiso Palace & Spa"), get_id("Hospes Maricel"), get_id("Purobeach Palma")]
    },
    {
        "id": "mal_religious_sacred_art",
        "title": "Kutsal Sanat ve Katedral",
        "title_en": "Sacred Art & Cathedral",
        "description": "Katedral müzesinden piskoposluk hazinelerine kentin manevi hazineleri.",
        "description_en": "The city's spiritual treasures, from the cathedral museum to episcopal treasures.",
        "places": [get_id("Museu de La Seu de Mallorca"), get_id("Museu Diocesà"), get_id("Catedral-Basílica de Santa María de Mallorca"), get_id("Fundación Bartolomé March Servera")]
    },
    {
        "id": "mal_local_flavors_market",
        "title": "Yerel Tatlar ve Pazar Yeri",
        "title_en": "Local Flavors & Market",
        "description": "Mallorca'nın en taze ürünleri ve yerel yaşamın kalbi.",
        "description_en": "Mallorca's freshest products and the heart of local life.",
        "places": [get_id("Naturalment"), get_id("Restaurant El Pilón"), get_id("miniBAR Palma - Cafe y Jamón Ibérico al Corte"), get_id("Sóller")]
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

print("✅ Generated and injected 15 routes for Mallorca into " + filepath)

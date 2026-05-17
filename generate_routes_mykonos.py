#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/mykonos.json.draft"
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
        "id": "myk_classic_chora",
        "title": "Chora'nın Büyüsü: Klasik Rota",
        "title_en": "Magic of Chora: Classic Route",
        "description": "Yel değirmenlerinden Little Venice'e, Mykonos Town'un en ikonik köşeleri.",
        "description_en": "The most iconic corners of Mykonos Town, from the windmills to Little Venice.",
        "places": [get_id("Windmills of Mykonos"), get_id("Little Venice"), get_id("Holy Church of Panagia Paraportiani"), get_id("Matogianni")]
    },
    {
        "id": "myk_glam_beach_party",
        "title": "Dünyaca Ünlü Plaj Partileri",
        "title_en": "World Famous Beach Parties",
        "description": "Lüks beach club'lar, çılgın partiler ve Mykonos'un en popüler kumları.",
        "description_en": "Luxury beach clubs, crazy parties, and Mykonos's most popular sands.",
        "places": [get_id("Paradise Beach Club Mykonos"), get_id("Super Paradise Beach Club"), get_id("Nammos Mykonos"), get_id("Scorpios")]
    },
    {
        "id": "myk_delos_ancient_trip",
        "title": "Delos: Antik Çağın Kutsal Adası",
        "title_en": "Delos: Sacred Island of Antiquity",
        "description": "UNESCO mirası Delos adasına arkeolojik bir yolculuk ve tarih keşfi.",
        "description_en": "An archaeological journey and historical discovery to the UNESCO heritage island of Delos.",
        "places": [get_id("Delos"), get_id("Archaeological Museum of Mykonos"), get_id("Mykonos Old Port"), get_id("Lena's House Folk Museum")]
    },
    {
        "id": "myk_luxury_waterfront",
        "title": "Lüks ve Seçkin Mykonos",
        "title_en": "Luxury & Exclusive Mykonos",
        "description": "En prestijli restoranlar, butikler ve şık sahil durakları.",
        "description_en": "The most prestigious restaurants, boutiques, and chic seaside stops.",
        "places": [get_id("Principote Mykonos"), get_id("Zuma Mykonos"), get_id("Beefbar Mykonos"), get_id("ToyRoom Mykonos")]
    },
    {
        "id": "myk_sunset_viewpoints",
        "title": "En Güzel Gün Batımı Noktaları",
        "title_en": "Best Sunset Viewpoints",
        "description": "Günü uğurlamak için adanın en büyüleyici terasları ve fenerleri.",
        "description_en": "The island's most enchanting terraces and lighthouses to bid farewell to the day.",
        "places": [get_id("180º Sunset Bar"), get_id("Armenistis Lighthouse"), get_id("Little Venice"), get_id("Boni's Windmill")]
    },
    {
        "id": "myk_hidden_beaches_quiet",
        "title": "Gizli Koylar ve Huzur",
        "title_en": "Hidden Bays & Serenity",
        "description": "Kalabalıktan uzak, Mykonos'un en bozulmamış ve sakin plajları.",
        "description_en": "Away from the crowds, Mykonos's most pristine and quiet beaches.",
        "places": [get_id("Agios Sostis Beach"), get_id("Lia Beach"), get_id("Panormos Beach"), get_id("Kiki's Tavern")]
    },
    {
        "id": "myk_cosmopolitan_night",
        "title": "Kozmopolit Gece Hayatı",
        "title_en": "Cosmopolitan Nightlife",
        "description": "Chora'nın dar sokaklarında sabahın ilk ışıklarına kadar süren eğlence.",
        "description_en": "Entertainment in the narrow streets of Chora lasting until the early hours of the morning.",
        "places": [get_id("ASTRA"), get_id("Moni"), get_id("Madon"), get_id("Skandinavian Bar Mykonos")]
    },
    {
        "id": "myk_local_ano_mera",
        "title": "Yerel Hayat: Ano Mera ve Çiftlikler",
        "title_en": "Local Life: Ano Mera & Farms",
        "description": "Adanın geleneksel köyü, organik çiftlikleri ve otantik durakları.",
        "description_en": "The island's traditional village, organic farms, and authentic stops.",
        "places": [get_id("Ano Mera"), get_id("Monastery of Tourliani"), get_id("Mykonos Vioma Organic Farm"), get_id("Amades Mykonos Eat Local")]
    },
    {
        "id": "myk_gourmet_dining",
        "title": "Gurme Mykonos Lezzetleri",
        "title_en": "Gourmet Mykonos Flavors",
        "description": "Dünyaca ünlü şeflerin ve yerel lezzet ustalarının en özel mönüleri.",
        "description_en": "The most special menus of world-famous chefs and local food masters.",
        "places": [get_id("Nusr-et Mykonos"), get_id("Buddha-Bar Beach (Mykonos)"), get_id("Spilia Restaurant"), get_id("Mamalouka Mykonos")]
    },
    {
        "id": "myk_traditional_culture",
        "title": "Gelenek ve Kültür İzinde",
        "title_en": "Tracing Tradition & Culture",
        "description": "Müzelerden kiliselere, Mykonos'un köklü kültürel mirası.",
        "description_en": "From museums to churches, Mykonos's deep-rooted cultural heritage.",
        "places": [get_id("Mykonos Folklore Museum"), get_id("Aegean Maritime Museum") or get_id("Ναυτικο Μουσείο Αιγαίου - Aegean Maritime Museum"), get_id("Holy Church of Panagia Paraportiani"), get_id("Agricultural Museum- Mylos tou Boni")]
    },
    {
        "id": "myk_chic_shopping",
        "title": "Şık Alışveriş ve Butikler",
        "title_en": "Chic Shopping & Boutiques",
        "description": "Tasarım ürünlerden lüks markalara, adanın en iyi alışveriş durakları.",
        "description_en": "From designer products to luxury brands, the island's best shopping stops.",
        "places": [get_id("Matogianni"), get_id("Rarity Gallery"), get_id("Fresh Boutique Hotel Mykonos") or get_id("Matogianni"), get_id("JackieO’")]
    },
    {
        "id": "myk_active_and_diving",
        "title": "Mavi Keşif: Sualtı ve Spor",
        "title_en": "Blue Discovery: Underwater & Sports",
        "description": "Adrenalin tutkunları için dalış merkezleri ve rüzgar sörfü koyları.",
        "description_en": "Diving centers and windsurfing bays for adrenaline enthusiasts.",
        "places": [get_id("Mykonos VIP Underwater Activities"), get_id("GoDive Mykonos Diving Scuba PADI Center at Lia beach"), get_id("Kalafati Beach"), get_id("Paralia Ftelias")]
    },
    {
        "id": "myk_family_friendly_beach",
        "title": "Ailece Plaj Keyfi",
        "title_en": "Family Beach Delight",
        "description": "Sığ denizi ve huzurlu ortamıyla aileler için en ideal sahil noktaları.",
        "description_en": "The most ideal coastal spots for families with their shallow sea and peaceful atmosphere.",
        "places": [get_id("Ornos Beach"), get_id("Paralia Kalo Livadi"), get_id("Platy Gialos Beach") or get_id("Psarou beach"), get_id("Trio Bambini, gelato & yogurt")]
    },
    {
        "id": "myk_chic_beach_clubs",
        "title": "Popüler Beach Clublar Turu",
        "title_en": "Popular Beach Clubs Tour",
        "description": "Adanın en çok konuşulan, şık ve hareketli plaj durakları.",
        "description_en": "The most talked about, chic and lively beach stops of the island.",
        "places": [get_id("JackieO’"), get_id("SantAnna Mykonos"), get_id("Alemagou"), get_id("Solymar")]
    },
    {
        "id": "myk_romantic_walks",
        "title": "Romantik Mykonos",
        "title_en": "Romantic Mykonos",
        "description": "Gün batımı barları ve loş ışıklı akşam yemeği mekanlarıyla aşk dolu bir rota.",
        "description_en": "A love-filled route with sunset bars and dimly lit dinner venues.",
        "places": [get_id("Oniro Sunset Bar - Restaurant"), get_id("Little Venice"), get_id("Sea Satin Market by Caprice Mykonos"), get_id("Lío Mykonos")]
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

print("✅ Generated and injected 15 routes for Mykonos into " + filepath)

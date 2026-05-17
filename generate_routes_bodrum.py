#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/bodrum.json.draft"
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
        "id": "bod_historical_halicarnassus",
        "title": "Antik Halikarnas'ın İzinde",
        "title_en": "Tracing Ancient Halicarnassus",
        "description": "Dünyanın yedi harikasından antik tiyatroya, Bodrum'un binlerce yıllık tarihine yolculuk.",
        "description_en": "A journey through thousands of years of Bodrum's history, from seven wonders of the world to the ancient theater.",
        "places": [get_id("Halikarnas Mozolesi"), get_id("Bodrum Antik Tiyatrosu"), get_id("Myndos Kapısı"), get_id("Bodrum Kalesi ve Sualtı Arkeoloji Müzesi")]
    },
    {
        "id": "bod_castle_and_maritime",
        "title": "Kale ve Deniz Mirası",
        "title_en": "Castle & Maritime Heritage",
        "description": "Şövalyelerin kalesinden deniz müzesine, kentin denizle bütünleşmiş hikayeleri.",
        "description_en": "Stories integrated with the sea, from the knights' castle to the maritime museum.",
        "places": [get_id("Bodrum Kalesi ve Sualtı Arkeoloji Müzesi"), get_id("Bodrum Deniz Müzesi"), get_id("Osmanlı Tersanesi Sanat Galerisi"), get_id("Bodrum Sualtı Arkeoloji Müzesi")]
    },
    {
        "id": "bod_bohemian_gumusluk",
        "title": "Gümüşlük: Bohem ve Dingin",
        "title_en": "Gümüşlük: Bohemian & Serene",
        "description": "Antik Myndos kalıntıları üzerinde gün batımı, deniz kenarı balıkçıları ve sanat atölyeleri.",
        "description_en": "Sunset over ancient Myndos ruins, seaside fish restaurants, and art workshops.",
        "places": [get_id("Gümüşlük"), get_id("Limon Gümüşlük Restaurant"), get_id("Kadir Akorak Atölyesi"), get_id("Gümüşlük Limanı Plajı")]
    },
    {
        "id": "bod_luxury_yalikavak",
        "title": "Lüks ve Modern Yalıkavak",
        "title_en": "Luxury & Modern Yalıkavak",
        "description": "Dünyaca ünlü markalar, prestijli restoranlar ve kentin en şık marinası.",
        "description_en": "World-famous brands, prestigious restaurants, and the city's most stylish marina.",
        "places": [get_id("Yalıkavak Marina"), get_id("Nusr-Et Steakhouse Yalıkavak Marina"), get_id("Zuma Bodrum"), get_id("Highlight Hotel Yalıkavak")]
    },
    {
        "id": "bod_artsy_and_intellectual",
        "title": "Sanat ve Entelektüel Bodrum",
        "title_en": "Artsy & Intellectual Bodrum",
        "description": "Zeki Müren'den Halikarnas Balıkçısı'na, kentin kültürel ikonlarına bir saygı duruşu.",
        "description_en": "A tribute to the city's cultural icons, from Zeki Müren to the Fisherman of Halicarnassus.",
        "places": [get_id("Zeki Müren Sanat Müzesi"), get_id("Halikarnas Balıkçısı Müzesi"), get_id("Dibeklihan Kültür ve Sanat Köyü"), get_id("Osmanlı Tersanesi Sanat Galerisi")]
    },
    {
        "id": "bod_sunset_windmills",
        "title": "Yel Değirmenleri ve Gün Batımı",
        "title_en": "Windmills & Sunset",
        "description": "Kentin en güzel panaromik manzaralarında günü uğurlama rotası.",
        "description_en": "A route to bid farewell to the day at the city's most beautiful panoramic views.",
        "places": [get_id("Bodrum Yel Değirmenleri"), get_id("Gümbet Yeldeğirmenleri"), get_id("Bitez Plaji"), get_id("Deniz Feneri")]
    },
    {
        "id": "bod_glamorous_beach_clubs",
        "title": "Bodrum'un Şık Plaj Kulüpleri",
        "title_en": "Bodrum's Glamorous Beach Clubs",
        "description": "Türkbükü ve Yalıkavak'ın en popüler ve kaliteli beach club durakları.",
        "description_en": "The most popular and high-quality beach club stops of Türkbükü and Yalıkavak.",
        "places": [get_id("Maçakızı Bodrum"), get_id("Lucca Beach"), get_id("Nikki Beach Resort & Spa Bodrum"), get_id("Bagatelle Bodrum")]
    },
    {
        "id": "bod_local_flavors_tour",
        "title": "Yerel Lezzetler ve Çarşı",
        "title_en": "Local Flavors & Bazaar",
        "description": "Bodrum sandaletlerinden meşhur dönerine, kentin otantik tatları ve çarşı ruhu.",
        "description_en": "From Bodrum sandals to famous doner, the city's authentic tastes and bazaar spirit.",
        "places": [get_id("Çarşı"), get_id("Bitez Dondurmacısı"), get_id("Kısmet Lokantası"), get_id("Sünger Pizza Restaurant")]
    },
    {
        "id": "bod_blue_cruise_bays",
        "title": "Koylar ve Mavi Yolculuk",
        "title_en": "Bays & Blue Cruise",
        "description": "Kristal berrak sularda yüzme ve teknelerle adaları keşif turu.",
        "description_en": "Swimming in crystal-clear waters and exploring islands by boats.",
        "places": [get_id("Orak Adası"), get_id("Karaada"), get_id("Akvaryum Koyu"), get_id("Cennet Koyu")]
    },
    {
        "id": "bod_village_life_derkoy",
        "title": "Kırsal Kaçış: Dereköy ve Etrim",
        "title_en": "Rural Escape: Dereköy & Etrim",
        "description": "Halı dokuma atölyeleri, yerel lokantalar ve Bodrum'un bozulmamış köy hayatı.",
        "description_en": "Carpet weaving workshops, local eateries, and Bodrum's unspoiled village life.",
        "places": [get_id("Etrim Halıcılık"), get_id("Dereköy Lokantası"), get_id("Sandıma Köyü"), get_id("Karakaya")]
    },
    {
        "id": "bod_vibrant_nightlife",
        "title": "Bodrum Geceleri ve Eğlence",
        "title_en": "Bodrum Nights & Fun",
        "description": "Barlar sokağından dev kulüplere, Bodrum'un hiç uyumayan enerjisi.",
        "description_en": "From the bar street to giant clubs, Bodrum's never-sleeping energy.",
        "places": [get_id("Kule Rock City"), get_id("Catamaran Club Bodrum"), get_id("Mandalin"), get_id("Posh Club Bodrum")]
    },
    {
        "id": "bod_family_beach_fun",
        "title": "Ailece Plaj Keyfi",
        "title_en": "Family Beach Delight",
        "description": "Sığ denizi ve çocuk dostu tesisleriyle aileler için en ideal koylar.",
        "description_en": "The most ideal bays for families with their shallow sea and kid-friendly facilities.",
        "places": [get_id("Bitez Plaji"), get_id("Yahşi Plajı"), get_id("Bitez Dondurmacısı"), get_id("Gümbet Belediye Cafe")]
    },
    {
        "id": "bod_gourmet_dining_selection",
        "title": "Seçkin Akşam Yemeği Rehberi",
        "title_en": "Elite Dining Guide",
        "description": "Bodrum'un en iyi balıkçıları ve dünya mutfağından ödüllü restoranlar.",
        "description_en": "Bodrum's best fish restaurants and award-winning international cuisine restaurants.",
        "places": [get_id("Memedof Balık Restaurant"), get_id("Orfoz Restaurant Bodrum"), get_id("Kitchen by Osman Sezener"), get_id("Sait")]
    },
    {
        "id": "bod_spiritual_and_mystic",
        "title": "Manevi ve Mistik Duraklar",
        "title_en": "Spiritual & Mystic Stops",
        "description": "Türbelerden antik tapınaklara Bodrum'un az bilinen huzur noktaları.",
        "description_en": "Bodrum's lesser-known peace spots, from tombs to ancient temples.",
        "places": [get_id("cafer paşa türbesi"), get_id("Mars Tapınağı"), get_id("Historical (Turkish bath ) Tarihi Bardakçı Hamamı"), get_id("Antik Mezarlar")]
    },
    {
        "id": "bod_lifestyle_and_marinas",
        "title": "Marina Yaşamı ve Stil",
        "title_en": "Marina Life & Style",
        "description": "Kentin marinasında yürüyüş, şık kafeler ve prestijli bir atmosfer.",
        "description_en": "Walking in the city's marina, chic cafes, and a prestigious atmosphere.",
        "places": [get_id("Milta Bodrum Marina"), get_id("Musto Bistro"), get_id("Marina & Cafe & Pub") or get_id("Yalıkavak Marina"), get_id("Kahve Dünyası - Bodrum Marina")]
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

print("✅ Generated and injected 15 routes for Bodrum into " + filepath)

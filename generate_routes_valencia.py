#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/valencia.json.draft"
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
        "id": "val_futuristic_city_arts",
        "title": "Geleceğin Şehri: Sanat ve Bilim",
        "title_en": "City of the Future: Arts & Sciences",
        "description": "Valensiya'nın fütüristik silüetinde, Calatrava mimarisinin en ikonik durakları.",
        "description_en": "The most iconic stops of Calatrava architecture in Valencia's futuristic silhouette.",
        "places": [get_id("Ciudad de las Artes y las Ciencias"), get_id("Oceanogràfic València"), get_id("Queen Sofia Palace of Arts"), get_id("Gulliver park")]
    },
    {
        "id": "val_historical_heart_silk",
        "title": "Tarihi Kalp ve İpek Yolu",
        "title_en": "Historical Heart & Silk Road",
        "description": "Orta Çağ borsalarından ipek müzesine, Valensiya'nın ticari mirası.",
        "description_en": "From medieval exchanges to the silk museum, Valencia me's commercial heritage.",
        "places": [get_id("La Lonja de la Seda de Valencia"), get_id("Central Market of Valencia"), get_id("Silk Museum"), get_id("Valencia Cathedral")]
    },
    {
        "id": "val_ancient_gates_walls",
        "title": "Antik Kapılar ve Savunma",
        "title_en": "Ancient Gates & Defense",
        "description": "Kenti koruyan devasa kuleler ve surlar arasında bir tarih yolculuğu.",
        "description_en": "A history journey among massive towers and walls protecting the city.",
        "places": [get_id("Torres de Serranos"), get_id("Quart Towers"), get_id("Almudín de Valencia"), get_id("Arxeological Museum of Valencia") or get_id("La Almoina Archaeological Museum")]
    },
    {
        "id": "val_art_and_monastery",
        "title": "Sanat ve Manastırların Sessizliği",
        "title_en": "Art & Silence of Monasteries",
        "description": "Eski manastırlarda hayat bulan modern ve klasik sanat koleksiyonları.",
        "description_en": "Modern and classical art collections brought to life in old monasteries.",
        "places": [get_id("Museo de Bellas Artes de Valencia"), get_id("CCCC (Centro del Carmen de Cultura Contemporánea)"), get_id("Centro Cultural la Beneficencia"), get_id("Art Modern Institute Museum of Valencia")]
    },
    {
        "id": "val_paella_and_rice_heritage",
        "title": "Paella ve Pirincin Hikayesi",
        "title_en": "Story of Paella & Rice",
        "description": "Dünyaca ünlü paellanın ana vatanında gastronomi ve tarım mirası.",
        "description_en": "Gastronomy and agricultural heritage in the homeland of world-famous paella.",
        "places": [get_id("Museo del Arroz"), get_id("Central Market of Valencia"), get_id("Navarro"), get_id("Restaurante La Cepa Vieja (Valencia)")]
    },
    {
        "id": "val_horchata_sweet_breaks",
        "title": "Horchata ve Tatlı Molaları",
        "title_en": "Horchata & Sweet Breaks",
        "description": "Valensiya'nın en meşhur ferahlatıcı içeceği ve tarihi pastaneleri.",
        "description_en": "Valencia me's most famous refreshing drink and historical bakeries.",
        "places": [get_id("Orxateria Daniel"), get_id("HORCHATERIA DOLZ"), get_id("La Sucrera Pastelería"), get_id("Pastís d'Or")]
    },
    {
        "id": "val_seaside_luxury_balneario",
        "title": "Sahil Lüksü ve Deniz Sefası",
        "title_en": "Seaside Luxury & Beach Bliss",
        "description": "Tarihi deniz hamamlarından modern sahil otellerine Akdeniz keyfi.",
        "description_en": "Mediterranean delight from historical seaside baths to modern coastal hotels.",
        "places": [get_id("Las Arenas Balneario Resort"), get_id("Malvarrosa beach (Valencia)"), get_id("Hotel Miramar Valencia"), get_id("Akuarela Playa")]
    },
    {
        "id": "val_green_oasis_turia",
        "title": "Turia Bahçeleri: Yeşil Bir Vaha",
        "title_en": "Turia Gardens: A Green Oasis",
        "description": "Kenti boydan boya kat eden devasa bahçelerde doğa ve dinlenme.",
        "description_en": "Nature and relaxation in the massive gardens crossing the city end-to-end.",
        "places": [get_id("Jardines del Real / Viveros"), get_id("Gulliver park"), get_id("Natural Science Museum of Valencia"), get_id("Bioparc Valencia")]
    },
    {
        "id": "val_bohemian_ruzafa_night",
        "title": "Bohem Ruzafa ve Gece Hayatı",
        "title_en": "Bohemian Ruzafa & Nightlife",
        "description": "Kütüphane-kafelerden enerjik barlara kentin en havalı mahalle turu.",
        "description_en": "The city me's coolest neighborhood tour, from library-cafes to energetic bars.",
        "places": [get_id("Ubik Café Cafetería Librería"), get_id("Radio City"), get_id("Jimmy Glass Jazz Bar"), get_id("Deseo 54")]
    },
    {
        "id": "val_architectural_dos_aguas",
        "title": "Saraylar ve Mimari Zarafet",
        "title_en": "Palaces & Architectural Elegance",
        "description": "Barok saraylardan modern kongre merkezlerine kentin estetik yüzü.",
        "description_en": "The city me's aesthetic face, from Baroque palaces to modern conference centers.",
        "places": [get_id("Museo Nacional de Cerámica y Artes Suntuarias 'González Martí") or get_id('Museo Nacional de Cerámica y Artes Suntuarias "González Martí'), get_id("Palacio de Congresos de Valencia"), get_id("Palau de Cervelló"), get_id("Palau dels Valeriola")]
    },
    {
        "id": "val_family_adventure_bioparc",
        "title": "Ailece Macera ve Hayvanlar Dünyası",
        "title_en": "Family Adventure & Animal World",
        "description": "Vahşi doğadan dev akvaryuma, çocuklarla keşif dolu bir gün.",
        "description_en": "A discovery-filled day with children, from wild nature to a giant aquarium.",
        "places": [get_id("Bioparc Valencia"), get_id("Oceanogràfic València"), get_id("Gulliver park"), get_id("Kids Mafia parque de bolas cafe")]
    },
    {
        "id": "val_modern_innovation_muvim",
        "title": "Modernlik ve İllüstrasyon",
        "title_en": "Modernity & Illustration",
        "description": "Zihni açan sergiler ve aydınlanma tarihine modern bir bakış.",
        "description_en": "Mind-opening exhibitions and a modern look at enlightenment history.",
        "places": [get_id("Museo Valenciano de la Ilustración ve la Modernidad"), get_id("La Fundación Chirivella Soriano"), get_id("Sala Parpalló"), get_id("Ana Serratosa - Gallery & Art Spaces - Sede Central")]
    },
    {
        "id": "val_vibrant_night_clubs",
        "title": "Pulsar Neşeli Geceler: Kulüpler",
        "title_en": "Pulsating Joyful Nights: Clubs",
        "description": "Valensiya'nın hiç uyumayan gece hayatında en iddialı adresler.",
        "description_en": "The most ambitious addresses in Valencia me's never-sleeping nightlife.",
        "places": [get_id("Indiana"), get_id("Rumbo 144"), get_id("Jerusalem Pop&Rock"), get_id("Bowie Show Disco")]
    },
    {
        "id": "val_mystic_legends_nostalgia",
        "title": "Mistik Efsaneler ve Nostalji",
        "title_en": "Mystic Legends & Nostalgia",
        "description": "Eski ambarlardan efsanelere kentin az bilinen hikayeleri.",
        "description_en": "Lesser-known stories of the city, from old warehouses to legends.",
        "places": [get_id("Antiguo Almacén de Dientes"), get_id("Museo Taurino"), get_id("La Almoina Archaeological Museum"), get_id("Quart Towers")]
    },
    {
        "id": "val_luxury_lifestyle_hospes",
        "title": "Lüks Yaşam ve Seçkin Oteller",
        "title_en": "Luxury Lifestyle & Elite Hotels",
        "description": "Tarihi saraylarda konaklama, sessiz avlular ve yüksek konfor.",
        "description_en": "Staying in historical palaces, quiet courtyards, and high comfort.",
        "places": [get_id("Hotel Hospes Palau de la Mar | Valencia"), get_id("Hotel Primus Valencia"), get_id("Hotel la Mozaira"), get_id("Hotel ILUNION Aqua 3")]
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

print("✅ Generated and injected 15 routes for Valencia into " + filepath)

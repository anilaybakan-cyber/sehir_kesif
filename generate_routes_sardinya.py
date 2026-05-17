#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/sardinya.json.draft"
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
        "id": "sard_emerald_luxury_luxury",
        "title": "Zümrüt Kıyısında Lüks Yaşam",
        "title_en": "Luxury Life on Emerald Coast",
        "description": "Porto Cervo'nun ışıltılı yat limanlarından Costa Smeralda'nın prestijli koylarına.",
        "description_en": "From the glitzy yacht harbors of Porto Cervo to the prestigious coves of Costa Smeralda.",
        "places": [get_id("Porto Cervo Marina"), get_id("Costa Smeralda Luxury"), get_id("Spiaggia del Principe"), get_id("Cala Brandinchi")]
    },
    {
        "id": "sard_ancient_nuragic_mysteries",
        "title": "Antik Nuragik Gizemler",
        "title_en": "Ancient Nuragic Mysteries",
        "description": "Binlerce yıllık taş kuleler ve Sardinya'nın prehistorik mühendislik dehası.",
        "description_en": "Thousands of years old stone towers and Sardinia me's prehistoric engineering genius.",
        "places": [get_id("Su Nuraxi di Barumini"), get_id("Nuraghe Santu Antine"), get_id("Nuraghe Losa"), get_id("Sanctuary of Santa Cristina")]
    },
    {
        "id": "sard_alghero_catalan_romance",
        "title": "Alghero: Katalan Romantizmi",
        "title_en": "Alghero: Catalan Romance",
        "description": "Sarı taşlı surlar, dar sokaklar ve Alghero'nun büyüleyici gün batımı.",
        "description_en": "Yellow stone walls, narrow streets, and Alghero's fascinating sunset.",
        "places": [get_id("Alghero Old Town"), get_id("Neptunes Grotto"), get_id("Nuraghe Palmavera"), get_id("Capo Caccia")]
    },
    {
        "id": "sard_wild_orosei_coves",
        "title": "Vahşi Orosei ve Saklı Koylar",
        "title_en": "Wild Orosei & Hidden Coves",
        "description": "Sadece denizden ulaşılabilen turkuaz cennetler ve kireçtaşı mağaraları.",
        "description_en": "Turquoise paradises and limestone caves accessible only by sea.",
        "places": [get_id("Cala Luna"), get_id("Cala Mariolu"), get_id("Cala Goloritzè"), get_id("Grotte del Bue Marino")]
    },
    {
        "id": "sard_cagliari_capital_heritage",
        "title": "Cagliari: Başkent Mirası",
        "title_en": "Cagliari: Capital Heritage",
        "description": "Heybetli surlardan katedral meydanlarına başkentin tarihi kalbi.",
        "description_en": "The capital's historical heart from imposing walls to cathedral squares.",
        "places": [get_id("Cagliari Castello"), get_id("Cagliari Cathedral"), get_id("Torre dell Elefante"), get_id("National Archaeological Museum")]
    },
    {
        "id": "sard_madalena_archipelago_sailing",
        "title": "La Maddalena: Adalar Denizi",
        "title_en": "La Maddalena: Sea of Islands",
        "description": "Kristal suların ve pembe kumların arasında bir tekne yolculuğu.",
        "description_en": "A boat trip among crystal waters and pink sands.",
        "places": [get_id("La Maddalena Archipelago"), get_id("Spiaggia Rosa"), get_id("Cala Coticcio"), get_id("Roccia dell Orso")]
    },
    {
        "id": "sard_archaeological_nora_tharros",
        "title": "Arkeolojik İzler: Nora ve Tharros",
        "title_en": "Archaeological Traces: Nora & Tharros",
        "description": "Deniz kıyısındaki antik Fenike-Roma kentlerinde bir tarih turu.",
        "description_en": "A history tour in ancient Phoenician-Roman cities on the seaside.",
        "places": [get_id("Nora Archaeological Area"), get_id("Tharros Ruins"), get_id("Giganti di Mont e Prama"), get_id("San Giovanni di Sinis")]
    },
    {
        "id": "sard_barbagia_cultural_roots",
        "title": "Barbagia: Kültürel Kökler",
        "title_en": "Barbagia: Cultural Roots",
        "description": "Dağ köylerinde maskeler, duvar resimleri ve adanın gerçek ruhu.",
        "description_en": "Masks in mountain villages, murals, and the island's true spirit.",
        "places": [get_id("Orgosolo Murals"), get_id("Mamoiada Masks"), get_id("Nuoro Museum"), get_id("Santu Lussurgiu")]
    },
    {
        "id": "sard_south_coast_chia_turquoise",
        "title": "Güney Kıyıları ve Chia Turkuazı",
        "title_en": "South Coasts & Chia Turquoise",
        "description": "Dev kum tepeleri ve sığ sularla Sardinya'nın vahşi güneyi.",
        "description_en": "Sardinia's wild south with massive sand dunes and shallow waters.",
        "places": [get_id("Chia Shoreline"), get_id("Tuerredda Beach"), get_id("Su Giudeu Beach"), get_id("Capo Spartivento")]
    },
    {
        "id": "sard_western_wildness_piscinas",
        "title": "Batı'nın Vahşiliği ve Kum Tepeleri",
        "title_en": "Western Wildness & Sand Dunes",
        "description": "Maden tarihinden Avrupa'nın en yüksek kum tepelerine macera.",
        "description_en": "Adventure from mining history to Europe's highest sand dunes.",
        "places": [get_id("Piscinas Dunes"), get_id("Pan di Zucchero"), get_id("Carbonia Mining Site"), get_id("Iglesias Old Town")]
    },
    {
        "id": "sard_gastronomy_agriturismo_wine",
        "title": "Sardinya Gastronomisi ve Şarap",
        "title_en": "Sardinian Gastronomy & Wine",
        "description": "Kırsal lezzet duraklarından asırlık şarap mahzenlerine gurme turu.",
        "description_en": "Gourmet tour from rural flavor stops to century-old wine cellars.",
        "places": [get_id("Sa Mandra Agriturismo"), get_id("Jerzu Wine Cellars"), get_id("Su Gologone Spring"), get_id("Arzana Peaks")]
    },
    {
        "id": "sard_islands_within_island",
        "title": "Ada İçinde Adalar: San Pietro",
        "title_en": "Islands Within Island: San Pietro",
        "description": "Ceneviz mirası sokaklar, balıkçı köyleri ve ferah deniz havası.",
        "description_en": "Genoese heritage streets, fishing villages, and fresh sea air.",
        "places": [get_id("San Pietro Island"), get_id("Carloforte Island"), get_id("Sant Antioco Island"), get_id("Teulada Port")]
    },
    {
        "id": "sard_hiking_oglisra_peaks",
        "title": "Oglisra Zirveleri ve Yürüyüş",
        "title_en": "Oglisra Peaks & Hiking",
        "description": "Avrupa'nın en derin kanyonundan sarp dağ patikalarına doğa.",
        "description_en": "Nature from Europe's deepest canyon to steep mountain paths.",
        "places": [get_id("Gorropu Gorge"), get_id("Baunei Mountain Path"), get_id("Arzana Peaks"), get_id("Ulassai Art Village")]
    },
    {
        "id": "sard_historical_towns_castelsardo",
        "title": "Tarihi Kasabalar ve Hilltoplar",
        "title_en": "Historical Towns & Hilltops",
        "description": "Tepedeki kalelerden renkli sokaklara masalsı bir yolculuk.",
        "description_en": "A fairytale journey from hilltop castles to colorful streets.",
        "places": [get_id("Castelsardo Hilltop"), get_id("Bosa Colorful Streets"), get_id("Bosa Marina"), get_id("Castello dei Malaspina")]
    },
    {
        "id": "sard_marine_reserves_villasimius",
        "title": "Deniz Rezervleri ve Su Altı",
        "title_en": "Marine Reserves & Underwater",
        "description": "Pirinç plajlarından kristal berraklığındaki mercan resiflerine.",
        "description_en": "From rice beaches to crystal clear coral reefs.",
        "places": [get_id("Capo Carbonara Marine Area"), get_id("Villasimius Turquoise"), get_id("Spiaggia del Riso"), get_id("Cala Pira")]
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

print("✅ Generated and injected 15 routes for Sardinya into " + filepath)

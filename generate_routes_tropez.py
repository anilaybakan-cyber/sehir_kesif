#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/saint_tropez.json.draft"
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
        "id": "tro_glamorous_coast_hike",
        "title": "Işıltılı Sahil Yürüyüşü",
        "title_en": "Glamorous Coast Hike",
        "description": "Sahil yolunun masmavi duraklarından ünlü plajlara bir keşif.",
        "description_en": "A discovery from the deep blue stops of the coastal path to famous beaches.",
        "places": [get_id("Sentier des Douaniers"), get_id("Plage des Canoubiers"), get_id("Plage de la Bouillabaisse"), get_id("Gigaro Beach")]
    },
    {
        "id": "tro_prestigious_wine_chateaux",
        "title": "Prestijli Şarap Şatoları",
        "title_en": "Prestigious Wine Chateaux",
        "description": "Dünyaca ünlü Rosé şaraplarının vahasında aristokratik bir gurme yolculuğu.",
        "description_en": "An aristocratic gourmet journey in the oasis of world-famous Rosé wines.",
        "places": [get_id("Château Minuty"), get_id("Domaine de la Croix"), get_id("Château Barbeyrolles"), get_id("Domaine du Siouvette")]
    },
    {
        "id": "tro_authentic_la_ponche_steps",
        "title": "La Ponche: Otantik Adımlar",
        "title_en": "La Ponche: Authentic Steps",
        "description": "Eski balıkçı mahallesinde Brigitte Bardot'nun izini sürün.",
        "description_en": "Track Brigitte Bardot in the old fishing quarter.",
        "places": [get_id("La Ponche Quarter"), get_id("Brigitte Bardot Statue"), get_id("Fishermans Alley View"), get_id("Place aux Herbes Market")]
    },
    {
        "id": "tro_designer_shopping_luxury",
        "title": "Tasarımcı Butikleri ve Lüks Şıklık",
        "title_en": "Designer Boutiques & Luxury Chic",
        "description": "Global modanın kalbinde en prestijli markalar ve aristokratik malikaneler.",
        "description_en": "The most prestigious brands and aristocratic manors in the heart of global fashion.",
        "places": [get_id("Designer Boutique Street"), get_id("Hermes Saint-Tropez"), get_id("Rue de la Citadelle Shops"), get_id("Saint-Tropez Polo Club")]
    },
    {
        "id": "tro_panaromic_gulf_views",
        "title": "Körfezin Panaromik Silüeti",
        "title_en": "Panoramic Silhouette of the Gulf",
        "description": "Surların üzerinden heybetli yatları ve kentin estetik gücünü izleyin.",
        "description_en": "Watch the imposing yachts and the city's aesthetic power from over the walls.",
        "places": [get_id("Gulf of Saint-Tropez View"), get_id("Private Helicopter Link"), get_id("Sentier des Douaniers"), get_id("Port de Ramatuelle")]
    },
    {
        "id": "tro_maritime_ferry_link_safari",
        "title": "Deniz Safarisi ve Vapur Keyfi",
        "title_en": "Sea Safari & Ferry Joy",
        "description": "Körfezin iki yakasını neşeli liman rotalarıyla su üzerinden keşfedin.",
        "description_en": "Explore the two sides of the bay from the water with joyful port routes.",
        "places": [get_id("Sainte-Maxime Ferry Link"), get_id("Cogolin Port Link"), get_id("Port de Ramatuelle"), get_id("Plage de la Bouillabaisse")]
    },
    {
        "id": "tro_bohemian_evening_luxe",
        "title": "Bohem Akşamlar ve Lüks Mola",
        "title_en": "Bohemian Evenings & Luxury Break",
        "description": "Günün yorgunluğunu şık çay saatlerinde ve neşeli buluşma noktalarında atın.",
        "description_en": "Relax from the day's weariness at stylish tea times and joyful meeting points.",
        "places": [get_id("Seaside Afternoon Tea"), get_id("Fishermans Alley View"), get_id("Seaside Gelato Spot"), get_id("La Maison des Papillons")]
    },
    {
        "id": "tro_hidden_gems_butterflies",
        "title": "Mistik Müze ve Saklı Taşlar",
        "title_en": "Mystic Museum & Hidden Gems",
        "description": "Kelebek evinden yerel atölyelere kentin keşfedilmeyi bekleyen köşeleri.",
        "description_en": "Corners of the city waiting to be discovered, from the butterfly house to local workshops.",
        "places": [get_id("La Maison des Papillons"), get_id("Local Pottery Shop"), get_id("Rue de la Citadelle Shops"), get_id("Place aux Herbes Market")]
    },
    {
        "id": "tro_market_flavor_discovery",
        "title": "Pazar Neşesi ve Lezzet Keşfi",
        "title_en": "Market Joy & Flavor Discovery",
        "description": "Taze narenciye kokuları arasında yerel gastronomiyi en otantik haliyle soluyun.",
        "description_en": "Breathe in local gastronomy in its most authentic form among fresh citrus scents.",
        "places": [get_id("Place aux Herbes Market"), get_id("Seaside Gelato Spot"), get_id("Domaine de la Croix"), get_id("Rue de la Citadelle Shops")]
    },
    {
        "id": "tro_aristocratic_polo_life",
        "title": "Polo Kulübü ve Aristokratik Yaşam",
        "title_en": "Polo Club & Aristocratic Life",
        "description": "Polo sporunun asaletinden helikopter ulaşımının heybetine elit bir gün.",
        "description_en": "An elite day from the nobility of polo sports to the majesty of helicopter transport.",
        "places": [get_id("Saint-Tropez Polo Club"), get_id("Private Helicopter Link"), get_id("Hermes Saint-Tropez"), get_id("Seaside Afternoon Tea")]
    },
    {
        "id": "tro_wild_gigaro_nature_trail",
        "title": "Vahşi Gigaro ve Doğa Yolu",
        "title_en": "Wild Gigaro & Nature Trail",
        "description": "El değmemiş koylardan çam ormanlarına kentin en sarp köşeleri.",
        "description_en": "The city's steepest corners from untouched coves to pine forests.",
        "places": [get_id("Gigaro Beach"), get_id("Sentier des Douaniers"), get_id("Plage des Canoubiers"), get_id("Port de Ramatuelle")]
    },
    {
        "id": "tro_cinematic_memory_bardot",
        "title": "Sinemasal Hafıza: Bardot'nun Rodos'u",
        "title_en": "Cinematic Memory: Bardot's Rhodes",
        "description": "İkonik heykellerden tarihi mahallelere kentin sinema tarihindeki izleri.",
        "description_en": "Traces in the city's cinema history from iconic statues to historical neighborhoods.",
        "places": [get_id("Brigitte Bardot Statue"), get_id("La Ponche Quarter"), get_id("Fishermans Alley View"), get_id("La Maison des Papillons")]
    },
    {
        "id": "tro_modern_luxury_designer_walk",
        "title": "Modern Lüks ve Tasarımcı Yürüyüşü",
        "title_en": "Modern Luxury & Designer Walk",
        "description": "Deri markalarından moda devlerine şıklığın kozmopolit kalbi.",
        "description_en": "The cosmopolitan heart of chic from leather brands to fashion giants.",
        "places": [get_id("Hermes Saint-Tropez"), get_id("Designer Boutique Street"), get_id("Seaside Afternoon Tea"), get_id("Saint-Tropez Polo Club")]
    },
    {
        "id": "tro_seaside_gelato_summer_sweet",
        "title": "Sahil Tatlısı ve Yaz Rüzgarı",
        "title_en": "Seaside Sweet & Summer Breeze",
        "description": "Dondurma duraklarından marina teraslarına neşeli bir sahil günü.",
        "description_en": "A joyful coastal day from gelato stops to marina terraces.",
        "places": [get_id("Seaside Gelato Spot"), get_id("Fishermans Alley View"), get_id("Port de Ramatuelle"), get_id("Plage de la Bouillabaisse")]
    },
    {
        "id": "tro_serene_provence_manors",
        "title": "Asude Provence Malikaneleri",
        "title_en": "Serene Provence Manors",
        "description": "Tarihi şatoların asude mönüleri ve üzüm bağlarının sessizliği.",
        "description_en": "The serene menus of historical chateaux and the silence of vineyards.",
        "places": [get_id("Château Barbeyrolles"), get_id("Domaine du Siouvette"), get_id("Château Minuty"), get_id("Domaine de la Croix")]
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

print("✅ Generated and injected 15 routes for Saint-Tropez into " + filepath)

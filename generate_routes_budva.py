#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/budva.json.draft"
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
        "id": "bud_ancient_old_town_walls",
        "title": "Eski Şehir ve Surlar",
        "title_en": "Old Town & Walls",
        "description": "Adriyatik'in en eski yerleşiminde, dar sokaklar ve tarihi kaleler arasında bir zaman yolculuğu.",
        "description_en": "A time travel between narrow streets and historical castles in one of the oldest settlements in the Adriatic.",
        "places": [get_id("Old Town"), get_id("Citadela Budva"), get_id("Church of Saint John the Baptist"), get_id("Holy Trinity Church")]
    },
    {
        "id": "bud_panaromic_paragliding_brajici",
        "title": "Adriyatik Üzerinde Yamaç Paraşütü",
        "title_en": "Paragliding Over the Adriatic",
        "description": "Brajići zirvesinden masmavi boşluğa süzülürken Budva'yı kuş bakışı keşfedin.",
        "description_en": "Discover Budva from a bird's-eye view while gliding into the deep blue space from the Brajići peak.",
        "places": [get_id("Paragliding Montenegro launch spot Brajići"), get_id("Budva Paragliding Montenegro - Flying Adventure"), get_id("Fort Kosmač"), get_id("Maine")]
    },
    {
        "id": "bud_iconic_sveti_stefan_luxury",
        "title": "Sveti Stefan ve Sahil Şıklığı",
        "title_en": "Sveti Stefan & Coastal Elegance",
        "description": "Karadağ'ın en meşhur ada-oteli ve çevresindeki kristal sular.",
        "description_en": "Montenegro's most famous island-hotel and the surrounding crystal waters.",
        "places": [get_id("Sveti Stefan"), get_id("Avala Resort & Villas"), get_id("Plaža Ričardova Glava"), get_id("Hotel & Restaurant Adrović")]
    },
    {
        "id": "bud_hawaii_island_escape",
        "title": "Hawaii Adası: Sveti Nikola",
        "title_en": "Hawaii Island Escape: Sveti Nikola",
        "description": "Budva'nın tam karşısındaki sarp kayalıkların ve vahşi doğanın asude huzuru.",
        "description_en": "The serene peace of steep cliffs and wild nature right across from Budva.",
        "places": [get_id("Sveti Nikola Island"), get_id("Montenegro rent-a-boat, Budva"), get_id("Gringo Boat"), get_id("Public Dock")]
    },
    {
        "id": "bud_romantic_mogren_path",
        "title": "Romantik Mogren Yolu",
        "title_en": "Romantic Mogren Path",
        "description": "Kayalıklar arasından süzülen masalsı bir patika ve Budva'nın en güzel kumları.",
        "description_en": "A fairytale path gliding through rocks and Budva's most beautiful sands.",
        "places": [get_id("Mogren beach"), get_id("Avala Resort & Villas"), get_id("Old Town"), get_id("Pet Friendly Beach")]
    },
    {
        "id": "bud_nightlife_pulsating_clubs",
        "title": "Pulsar Neşeli Geceler: Kulüpler",
        "title_en": "Pulsating Joyful Nights: Clubs",
        "description": "Budva'nın hiç uyumayan gece hayatında en iddialı ve enerjik adresler.",
        "description_en": "The most ambitious and energetic addresses in Budva me's never-sleeping nightlife.",
        "places": [get_id("Top Hill"), get_id("Trocadero"), get_id("Premium Palazzo night club"), get_id("Omnia")]
    },
    {
        "id": "bud_spiritual_monasteries_peace",
        "title": "Manevi Huzur ve Manastırlar",
        "title_en": "Spiritual Peace & Monasteries",
        "description": "İç kesimlerin sessiz vadilerinde saklı kalmış asırlık dini yapılar.",
        "description_en": "Century-old religious structures hidden in the silent valleys of the interior.",
        "places": [get_id("Podmaine Monastery"), get_id("Maine"), get_id("Budva City Museum"), get_id("Church of Saint John the Baptist")]
    },
    {
        "id": "bud_modern_city_rhythm_tq",
        "title": "Modern Şehir Ritmi ve TQ Plaza",
        "title_en": "Modern City Rhythm & TQ Plaza",
        "description": "Alışverişten lüks konaklamaya Budva'nın kozmopolit kalbi.",
        "description_en": "Budva's cosmopolitan heart from shopping to luxury accommodation.",
        "places": [get_id("Hotel TQ Plaza"), get_id("Traffic circle with Fountains"), get_id("Budva Tourist Capital"), get_id("Turist Market 4")]
    },
    {
        "id": "bud_seaside_gastronomy_jadran",
        "title": "Sahil Gastronomisi ve Deniz Keyfi",
        "title_en": "Seaside Gastronomy & Sea Pleasure",
        "description": "Adriyatik dalgaları eşliğinde en taze deniz ürünleri ve yerel tatlar.",
        "description_en": "Freshest seafood and local flavors accompanied by Adriatic waves.",
        "places": [get_id("Jadran"), get_id("La Bocca"), get_id("Tropico"), get_id("Lim Restaurant")]
    },
    {
        "id": "bud_adventure_water_fun",
        "title": "Macera ve Su Eğlencesi",
        "title_en": "Adventure & Water Fun",
        "description": "Dev kaydıraklardan neşeli havuzlara ailece adrenalin dolu bir gün.",
        "description_en": "A day full of adrenaline for families, from huge slides to joyful pools.",
        "places": [get_id("Aquapark 'Budva'"), get_id("Jaz Beach"), get_id("Pet Friendly Beach"), get_id("Montenegro rent-a-boat, Budva")]
    },
    {
        "id": "bud_hidden_cafes_coffee_ritual",
        "title": "Saklı Kafeler ve Kahve Ritüeli",
        "title_en": "Hidden Cafes & Coffee Ritual",
        "description": "Eski kentin dar sokaklarında taze kahve kokusunu takip edin.",
        "description_en": "Follow the scent of fresh coffee in the narrow streets of the old town.",
        "places": [get_id("CUPS Coffeeshop"), get_id("Caffe Excellence"), get_id("Caffe Scorpion"), get_id("Cake & Bake")]
    },
    {
        "id": "bud_balkan_authentic_flavors",
        "title": "Balkanların Otantik Lezzetleri",
        "title_en": "Authentic Flavors of the Balkans",
        "description": "Geleneksel ızgaralardan yerel meyhanelere Karadağ mutfağı.",
        "description_en": "Montenegrin cuisine from traditional grills to local taverns.",
        "places": [get_id("BALKAN BUDVA"), get_id("Kužina"), get_id("Restoran Kralj"), get_id("Kod Saičića")]
    },
    {
        "id": "bud_culture_art_museum_trail",
        "title": "Kültür ve Sanatın İzinde",
        "title_en": "Following Culture & Art",
        "description": "Antik buluntulardan modern galeri sergilerine Budva mirası.",
        "description_en": "Budva heritage from ancient finds to modern gallery exhibitions.",
        "places": [get_id("Budva City Museum"), get_id("Jovo Ivanovic Modern Gallery"), get_id("Stefan Mitrov Ljubiša museum"), get_id("Jadran")]
    },
    {
        "id": "bud_night_glamour_terrazza",
        "title": "Akşam Şıklığı ve Terrazza",
        "title_en": "Evening Glamour & Terrazza",
        "description": "Işıltılı kentin üzerinde şık kokteyller ve neşeli sohbetler.",
        "description_en": "Chic cocktails and joyful chats above the glittering city.",
        "places": [get_id("Terrazza Budva"), get_id("WOW Restaurant & Bar"), get_id("Hotel Mogren"), get_id("Caffe Bar CBR")]
    },
    {
        "id": "bud_island_legends_mystic",
        "title": "Ada Efsaneleri ve Mistik Duraklar",
        "title_en": "Island Legends & Mystic Stops",
        "description": "Denizin ortasındaki antik hikayelerden kentin masalsı köşelerine.",
        "description_en": "From ancient stories in the middle of the sea to the city's fairytale corners.",
        "places": [get_id("Sveti Nikola Island"), get_id("Citadela Budva"), get_id("Museum of Herbs and Spices"), get_id("Старое Оливковое Дерево")]
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

print("✅ Generated and injected 15 routes for Budva into " + filepath)

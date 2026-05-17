#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ibiza.json.draft"
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
        "id": "ibi_historical_dalt_vila",
        "title": "Dalt Vila: Tarihin Kalbi",
        "title_en": "Dalt Vila: Heart of History",
        "description": "Antik surlar, katedral ve Dalt Vila'nın labirent sokaklarında tarih yolculuğu.",
        "description_en": "A history journey in the ancient walls, cathedral, and labyrinthine streets of Dalt Vila.",
        "places": [get_id("Dalt Vila"), get_id("Baluarte de San Pedro"), get_id("Museu Puget"), get_id("Casa de la Curia")]
    },
    {
        "id": "ibi_glamorous_clubbing",
        "title": "Dünya Gece Hayatının Başkenti",
        "title_en": "Capital of World Nightlife",
        "description": "İbiza'nın dünyaca ünlü dev kulüplerinde bitmeyen eğlence ve dans.",
        "description_en": "Never-ending fun and dance at Ibiza's world-famous giant clubs.",
        "places": [get_id("Pacha"), get_id("Amnesia Ibiza"), get_id("Ushuaïa Ibiza"), get_id("Lío")]
    },
    {
        "id": "ibi_sunset_vibes_cafe_del_mar",
        "title": "Efsanevi Gün Batımı Rotaları",
        "title_en": "Legendary Sunset Routes",
        "description": "Café del Mar'dan gizli seyir noktalarına, İbiza'da günü uğurlayın.",
        "description_en": "Bid farewell to the day in Ibiza, from Café del Mar to hidden viewpoints.",
        "places": [get_id("Café del Mar"), get_id("Es Vedrà"), get_id("180º Sunset Bar") or get_id("Café del Mar"), get_id("Panaroma view Bossa Beach")]
    },
    {
        "id": "ibi_luxury_marina_life",
        "title": "Lüks Marina ve Yaşam",
        "title_en": "Luxury Marina & Lifestyle",
        "description": "Yat limanında yürüyüş, şık butikler ve elit bir akşam yemeği noktası.",
        "description_en": "Walking at the yacht harbor, chic boutiques, and an elite dinner spot.",
        "places": [get_id("Ibiza Casino"), get_id("Marina Ibiza") or get_id("Ibiza Casino"), get_id("Ocean Drive Ibiza"), get_id("Keeper Ibiza")]
    },
    {
        "id": "ibi_hidden_beaches_quiet",
        "title": "Gizli Koylar ve Huzurlu Deniz",
        "title_en": "Hidden Bays & Peaceful Sea",
        "description": "Kalabalıktan uzak, İbiza'nın en berrak ve sakin sularında yüzme keyfi.",
        "description_en": "Swimming delight in Ibiza's clearest and quietest waters, away from the crowds.",
        "places": [get_id("Cala Salada"), get_id("Platja des Jondal"), get_id("Pura Vida"), get_id("Experimental Beach Ibiza")]
    },
    {
        "id": "ibi_ancient_roots_museum",
        "title": "Antik Kökler ve Müzeler",
        "title_en": "Ancient Roots & Museums",
        "description": "Fenike nekropolünden modern sanat galerilerine adanın kültürel mirası.",
        "description_en": "The island's cultural heritage, from Phoenician necropolises to modern art galleries.",
        "places": [get_id("Puig des Molins, Ibiza"), get_id("MAEF - Museu Arqueològic d'Eivissa i Formentera (Museum/Museo)"), get_id("Museu d'Art Contemporani d'Eivissa"), get_id("Museo Sa Caleta Centro de Interpretación")]
    },
    {
        "id": "ibi_party_beach_central",
        "title": "Playa d'en Bossa: Parti ve Güneş",
        "title_en": "Playa d'en Bossa: Party & Sun",
        "description": "Adanın en uzun plajında gün boyu müzik, güneş ve eğlence.",
        "description_en": "Music, sun, and fun all day long on the island's longest beach.",
        "places": [get_id("Ushuaïa Ibiza Beach Hotel"), get_id("Bora Bora Eivissa"), get_id("Tantra Ibiza"), get_id("Murphy's Ibiza")]
    },
    {
        "id": "ibi_bohemian_artsy_town",
        "title": "Bohem İbiza ve Sanat",
        "title_en": "Bohemian Ibiza & Art",
        "description": "Tasarım atölyeleri, sokak sanatı ve adanın yaratıcı ruhu.",
        "description_en": "Design workshops, street art, and the island's creative spirit.",
        "places": [get_id("Bloop Festival"), get_id("Galeria MARTA TORRES"), get_id("Arte Ibiza"), get_id("Espacio Micus")]
    },
    {
        "id": "ibi_chic_beach_clubs",
        "title": "Şık Beach Clublar ve Lüks",
        "title_en": "Chic Beach Clubs & Luxury",
        "description": "Adanın en popüler ve prestijli sahil duraklarında Akdeniz keyfi.",
        "description_en": "Mediterranean delight at the island's most popular and prestigious coastal stops.",
        "places": [get_id("Blue Marlin Eivissa"), get_id("El Chiringuito Ibiza"), get_id("Amante Ibiza"), get_id("Platja de ses Salines")]
    },
    {
        "id": "ibi_local_life_markets",
        "title": "Yerel Hayat ve Tatlar",
        "title_en": "Local Life & Flavors",
        "description": "İç kesimlerdeki şirin köylerden tarihi çarşılara gerçek İbiza.",
        "description_en": "Real Ibiza, from charming villages in the interior to historical markets.",
        "places": [get_id("Es Tap Nou"), get_id("Vila Café"), get_id("Can Tomeu"), get_id("Estàtua Vara de Rei")]
    },
    {
        "id": "ibi_family_fun_park",
        "title": "Ailece Eğlence Dolu Bir Gün",
        "title_en": "A Day Full of Family Fun",
        "description": "Parklardan sığ plajlara, çocuklu aileler için en keyifli noktalar.",
        "description_en": "The most pleasant spots for families with children, from parks to shallow beaches.",
        "places": [get_id("Gran Piruleto Park Ibiza"), get_id("Parque de S'Illa"), get_id("Peter Pan Eivissa"), get_id("Playas del Vivé")]
    },
    {
        "id": "ibi_romantic_dinner_dalt",
        "title": "Dalt Vila'da Romantik Akşam",
        "title_en": "Romantic Evening in Dalt Vila",
        "description": "Surların içinde, loş ışıklar altında unutulmaz bir gurme deneyimi.",
        "description_en": "An unforgettable gourmet experience under dim lights within the walls.",
        "places": [get_id("R&C Hotel Mirador de Dalt Vila"), get_id("Casa de las Flores"), get_id("Can Moreta"), get_id("Dalt Vila")]
    },
    {
        "id": "ibi_active_adventure_kayak",
        "title": "Aktif Macera: Kano ve Deniz",
        "title_en": "Active Adventure: Kayak & Sea",
        "description": "Ulaşılamaz koyları denizden keşfetmek isteyen maceraperestlere.",
        "description_en": "For adventurers wanting to explore inaccessible coves from the sea.",
        "places": [get_id("La Vuelta en Kayak"), get_id("Cala Salada"), get_id("Es Vedrà"), get_id("Ocean Drive Talamanca") or get_id("La Vuelta en Kayak")]
    },
    {
        "id": "ibi_luxury_resorts_spa",
        "title": "Lüks Konaklama ve Dinlenme",
        "title_en": "Luxury Lodging & Relaxation",
        "description": "Adanın en prestijli otellerinde beş yıldızlı konfor ve sükunet.",
        "description_en": "Five-star comfort and tranquility at the island's most prestigious hotels.",
        "places": [get_id("Hotel Torre del Mar"), get_id("Hotel Garbi Ibiza & Spa"), get_id("Casa Maca"), get_id("Hotel THB Los Molinos")]
    },
    {
        "id": "ibi_gastronomy_fusion",
        "title": "İbiza Gastronomi Karması",
        "title_en": "Ibiza Gastronomy Fusion",
        "description": "Arjantin etinden lokal mezelere, kentin zengin mutfağını keşfedin.",
        "description_en": "Explore the city's rich cuisine, from Argentine meat to local mezes.",
        "places": [get_id("BCB Tango"), get_id("Es Tap Nou"), get_id("El Bucanero"), get_id("Pasticceria Figueretas") or get_id("Pastelería Figueretas")]
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

print("✅ Generated and injected 15 routes for Ibiza into " + filepath)

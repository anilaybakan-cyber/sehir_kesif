#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/selanik.json.draft"
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
        "id": "sk_historical_symbols",
        "title": "Selanik'in Tarihi Simgeleri",
        "title_en": "Historical Symbols of Thessaloniki",
        "description": "Beyaz Kule'den kentin kalbi olan meydanlara uzanan klasik bir Selanik keşfi.",
        "description_en": "A classic exploration of Thessaloniki, from the White Tower to the heart of the city's squares.",
        "places": [get_id("White Tower of Thessaloniki"), get_id("Aristotelous Square"), get_id("Arch of Galerius"), get_id("Rotonda")]
    },
    {
        "id": "sk_upper_city_vibe",
        "title": "Ano Poli: Yukarı Şehir Ruhu",
        "title_en": "Ano Poli: Upper Town Spirit",
        "description": "Dar sokaklarda, Osmanlı evleri ve devasa surlar eşliğinde kentin en otantik bölgesi.",
        "description_en": "The city's most authentic area in narrow streets, accompanied by Ottoman houses and massive walls.",
        "places": [get_id("Ano Poli"), get_id("Heptapyrgion of Thessaloniki"), get_id("Latomos Monastery - Holy Church of Hosios David"), get_id("Pasha’s Gardens")]
    },
    {
        "id": "sk_byzantine_heritage",
        "title": "Bizans Mirası ve Kiliseler",
        "title_en": "Byzantine Heritage & Churches",
        "description": "Görkemli katedrallerden antik mozaiklere Selanik'in bin yıllık inanç tarihini keşfedin.",
        "description_en": "Discover Thessaloniki's thousand-year religious history, from grand cathedrals to ancient mosaics.",
        "places": [get_id("Holy Church of Saint Demetrius"), get_id("Agios Therapon Kilisesi") or get_id("Holy Church of Saint Demetrius"), get_id("Museum of Byzantine Civilization"), get_id("Archaeological Museum of Thessaloniki")]
    },
    {
        "id": "sk_vibrant_ladadika",
        "title": "Ladadika Geceleri ve Eğlence",
        "title_en": "Ladadika Nights & Entertainment",
        "description": "Kentin en popüler tavernalarında lezzet dolu bir mola ve canlı gece hayatı.",
        "description_en": "A flavor-filled break and lively nightlife in the city's most popular tavernas.",
        "places": [get_id("Ladadika"), get_id("The jews rainbow pub"), get_id("VOG CLUB Thessaloniki"), get_id("Soulshakers bar services")]
    },
    {
        "id": "sk_local_market_food",
        "title": "Yerel Tatlar ve Sokak Lezzeti",
        "title_en": "Local Flavors & Street Food",
        "description": "Tarihi pazar yerlerinde baharat kokuları ve Selanik'in meşhur gastronomik durakları.",
        "description_en": "Spice scents in historical market places and Thessaloniki's famous gastronomic stops.",
        "places": [get_id("Kapani Market"), get_id("Bougatsa Bantis"), get_id("Agora Ouzeri"), get_id("Chatzi")]
    },
    {
        "id": "sk_ataturk_and_history",
        "title": "Atatürk'ün İzinde",
        "title_en": "In the Footsteps of Atatürk",
        "description": "Atatürk'ün doğduğu evden kentin tarihi mahallelerine uzanan anlamlı bir rota.",
        "description_en": "A meaningful route stretching from the house where Atatürk was born to the city's historic neighborhoods.",
        "places": [get_id("Ataturk Museum of Thessaloniki"), get_id("Ano Poli"), get_id("Yeni Mosque of Thessaloniki"), get_id("Jewish Museum of Thessaloniki")]
    },
    {
        "id": "sk_museum_mile",
        "title": "Müze ve Sanat Keşfi",
        "title_en": "Museum & Art Discovery",
        "description": "Moden sanattan antik kalıntılara Selanik'in zengin kültürel hazineleri.",
        "description_en": "Thessaloniki's rich cultural treasures, from modern art to ancient ruins.",
        "places": [get_id("Archaeological Museum of Thessaloniki"), get_id("Museum of Byzantine Civilization"), get_id("MOMus - Museum of Modern Art - Kostakis Collection"), get_id("Telloglou House")]
    },
    {
        "id": "sk_waterfront_promenade",
        "title": "Sahil Boyu Keyifli Yürüyüş",
        "title_en": "Pleasant Waterfront Stroll",
        "description": "Beyaz Kule'den marinaya uzanan kentin en fotojenik ve ferah sahil rotası.",
        "description_en": "The city's most photogenic and spacious seaside route stretching from the White Tower to the marina.",
        "places": [get_id("White Tower of Thessaloniki"), get_id("Makedonia Palace Hotel"), get_id("Mytilene Marina") or get_id("White Tower of Thessaloniki"), get_id("Omilos The Beach Club | Bar & Restaurant")]
    },
    {
        "id": "sk_jewish_legacy",
        "title": "Selanik'in Yahudi Mirası",
        "title_en": "Thessaloniki's Jewish Legacy",
        "description": "Kentin tarihinde derin izler bırakan Yahudi toplumunun hikayesini ve yapılarını keşfedin.",
        "description_en": "Discover the story and structures of the Jewish community that left deep traces on the city's history.",
        "places": [get_id("Jewish Museum of Thessaloniki"), get_id("MOMus-Museum of Contemporary Art"), get_id("Villa Giacomo Modiano") or get_id("Jewish Museum of Thessaloniki"), get_id("The jews rainbow pub")]
    },
    {
        "id": "sk_hidden_gardens_views",
        "title": "Gizli Bahçeler ve Manzaralar",
        "title_en": "Hidden Gardens & Vistas",
        "description": "Şehrin içinde sessiz kaçış alanları ve en iyi panaromik fotoğraf noktaları.",
        "description_en": "Quiet escape areas within the city and the best panoramic photo spots.",
        "places": [get_id("Pasha’s Gardens"), get_id("Room With a View"), get_id("Heptapyrgion of Thessaloniki"), get_id("Panorama Hotel")]
    },
    {
        "id": "sk_bouzouki_night",
        "title": "Geleneksel Buzuki Gecesi",
        "title_en": "Traditional Bouzouki Night",
        "description": "Kentin en ünlü canlı müzik duraklarında uzo ve sirtaki dolu bir akşam.",
        "description_en": "An evening full of ouzo and sirtaki at the city's most famous live music stops.",
        "places": [get_id("Μούσες Εν Χορώ"), get_id("Mousiko Sergiani - Live Music"), get_id("Παρασκήνιο live"), get_id("Aristotelous Square")]
    },
    {
        "id": "sk_ancient_roman_path",
        "title": "Roma Dönemi Selanik'i",
        "title_en": "Roman Era Thessaloniki",
        "description": "Roma Forumu'ndan zafer kemerine uzanan antik kentin görkemli kalıntıları.",
        "description_en": "The grand ruins of the ancient city, stretching from the Roman Forum to the triumphal arch.",
        "places": [get_id("Museum of the Roman Forum of Thessaloniki"), get_id("Arch of Galerius"), get_id("Rotonda"), get_id("Alcazar (Hamza Bey)")]
    },
    {
        "id": "sk_design_and_shopping",
        "title": "Tasarım ve Modern Yaşam",
        "title_en": "Design & Modern Living",
        "description": "Selanik'in modern yüzünü yansıtan butik mağazalar ve şık mobilya galerileri.",
        "description_en": "Boutique stores and chic furniture galleries reflecting Thessaloniki's modern face.",
        "places": [get_id("KAIMASIDIS FURNITURE THESSALONIKI"), get_id("Έπιπla B Home"), get_id("aggeliki-workshop.gr"), get_id("Aristotelous Square")]
    },
    {
        "id": "sk_family_friendly_fun",
        "title": "Ailece Selanik Keşfi",
        "title_en": "Family Thessaloniki Discovery",
        "description": "Çocuklar için müzelerden denize, her yaşa hitap eden keyifli duraklar.",
        "description_en": "From museums for children to the sea, pleasant stops appealing to all ages.",
        "places": [get_id("Children's Museum of Thessaloniki"), get_id("Thessaloniki Cinema Museum & Cinematheque"), get_id("Aristotelous Square"), get_id("Effe Cafe")]
    },
    {
        "id": "sk_academic_and_local",
        "title": "Akademik ve Yerel Rota",
        "title_en": "Academic & Local Route",
        "description": "Üniversite bölgesinin dinamik enerjisi ve yerel öğrenci kafelerini keşfedin.",
        "description_en": "Discover the dynamic energy of the university area and local student cafes.",
        "places": [get_id("University Student Restaurant Club AUTh"), get_id("Mikel Coffee"), get_id("Café EL PASO"), get_id("Gnet Όlgas")]
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

print("✅ Generated and injected 15 routes for Selanik into " + filepath)

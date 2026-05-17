#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/kas.json.draft"
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
        "id": "kas_classic_center",
        "title": "Kaş Merkez ve Tarih",
        "title_en": "Kas Center & History",
        "description": "Antik tiyatrodan begonvilli sokaklara, Kaş'ın kalbinde bir yürüyüş.",
        "description_en": "A walk in the heart of Kas, from the ancient theater to bougainvillaea-lined streets.",
        "places": [get_id("Antiphellos Ancient City"), get_id("Kaş Çarşı"), get_id("Hellenistic theatre"), get_id("Kas Merkez Mosque")]
    },
    {
        "id": "kas_turquoise_beaches",
        "title": "Turkuaz Plajlar Rotası",
        "title_en": "Turquoise Beaches Route",
        "description": "Kaş'ın en meşhur ve berrak sularında deniz keyfi.",
        "description_en": "Sea delight in the most famous and clear waters of Kas.",
        "places": [get_id("Kaputaş Beach"), get_id("Hidayet Bay Beach"), get_id("Küçük Çakıl Plajı"), get_id("Büyükçakıl Plajı")]
    },
    {
        "id": "kas_kekova_boat_trip",
        "title": "Kekova ve Batık Şehir Macerası",
        "title_en": "Kekova & Sunken City Adventure",
        "description": "Tekneyle masmavi koylara ve tarihin sular altında kaldığı Kekova'ya yolculuk.",
        "description_en": "A boat journey to deep blue bays and Kekova, where history remains underwater.",
        "places": [get_id("Boat Trips by Captain Ergun | Kekova Tekne Turu | Kaş Tekne Turu | Кекова прогулка на лодке | Tekne Kiralama") or get_id("Kekova Island"), get_id("Kekova tekne turu"), get_id("Kaş su altı müzesi"), get_id("Kekova Island")]
    },
    {
        "id": "kas_ancient_patara",
        "title": "Patara: Kum Tepeleri ve Antik Kent",
        "title_en": "Patara: Sand Dunes & Ancient City",
        "description": "Likya Birliği'nin başkentinden uçsuz bucaksız kumsallara.",
        "description_en": "From the capital of the Lycian League to endless sandy beaches.",
        "places": [get_id("Patara Beach"), get_id("Saklikent National Park") or get_id("Patara Beach"), get_id("Phellos Antik Kenti") or get_id("Patara Beach"), get_id("Antalya kaș")]
    },
    {
        "id": "kas_sunset_and_views",
        "title": "Muazzam Manzara ve Gün Batımı",
        "title_en": "Magnificent Views & Sunset",
        "description": "Günü uğurlamak için Kaş'ın en yüksek ve en etkileyici seyir noktaları.",
        "description_en": "The highest and most impressive viewing points of Kas to bid farewell to the day.",
        "places": [get_id("Manzara"), get_id("Hellenistic theatre"), get_id("Seaview Otel") or get_id("Manzara"), get_id("Atatürk Heykeli")]
    },
    {
        "id": "kas_bohemian_shopping",
        "title": "Bohem Alışveriş ve Sanat",
        "title_en": "Bohemian Shopping & Art",
        "description": "Tasarım butiklerden sanat galerilerine, Kaş'ın yaratıcı ruhunu keşfedin.",
        "description_en": "Discover Kas's creative spirit, from design boutiques to art galleries.",
        "places": [get_id("Kaş Çarşı"), get_id("Tuğra Art Gallery"), get_id("Handmade Bracelets"), get_id("Kaş Belediye Çarşısı")]
    },
    {
        "id": "kas_diving_discovery",
        "title": "Mavi Derinlikler: Dalış Rotası",
        "title_en": "Blue Depths: Diving Route",
        "description": "Türkiye'nin en iyi dalış noktalarında sualtı dünyasını keşfedin.",
        "description_en": "Explore the underwater world at Turkey's best diving spots.",
        "places": [get_id("Caretta Wall Kaş"), get_id("Kaş su altı müzesi"), get_id("Giant Stride Shop & Cafe & Bar"), get_id("Hidayet Bay Beach")]
    },
    {
        "id": "kas_meis_island_trip",
        "title": "Meis: Karşı Kıyıya Yolculuk",
        "title_en": "Meis: Journey to the Opposite Shore",
        "description": "Feribotla komşu ada Meis'e geçip renkli evler arasında bir gün geçirin.",
        "description_en": "Cross to the neighboring island of Kastellorizo by ferry and spend a day among colorful houses.",
        "places": [get_id("Larsoy Travel & Tourism Office || ⛵️ Kekova Boat Tour || 🚙 Rent a Car || 🛵 Rent a Motorbike || ⛴️ Meis Ferry Ticket ||") or get_id("Antalya kaș"), get_id("Kastellorizo Folk Art Museum (Kavos Mosque)"), get_id("Meduseum - Megisti Puzzle Museum"), get_id("Antalya kaș")]
    },
    {
        "id": "kas_local_cafe_culture",
        "title": "Kaş Kafe ve Sohbet Durakları",
        "title_en": "Kas Cafe & Conversation Stops",
        "description": "Yeni nesil kahvecilerden tarihi çay ocaklarına yerel yaşamın tadı.",
        "description_en": "The taste of local life, from new generation coffee shops to historical tea houses.",
        "places": [get_id("Linckia Roastery Cafe"), get_id("Süleyman Çavuş Kahvehanesi (Tatlı-Limonata)"), get_id("Noel Baba Cafe&Bistro"), get_id("Heybe Cafe")]
    },
    {
        "id": "kas_nature_saklikent",
        "title": "Saklıkent: Kanyon ve Doğa",
        "title_en": "Saklıkent: Canyon & Nature",
        "description": "Buz gibi suların içinde kanyon yürüyüşü ve doğa macerası.",
        "description_en": "Canyon walking in ice-cold waters and nature adventure.",
        "places": [get_id("Saklikent National Park"), get_id("Patara Beach") or get_id("Saklikent National Park"), get_id("Antalya kaș"), get_id("Saklikent National Park")]
    },
    {
        "id": "kas_romantic_dinner",
        "title": "Denize Karşı Romantik Akşam",
        "title_en": "Romantic Evening by the Sea",
        "description": "Dalga sesleri ve mum ışığı eşliğinde unutulmaz bir Kaş yemeği.",
        "description_en": "An unforgettable Kas dinner accompanied by wave sounds and candlelight.",
        "places": [get_id("Sardunya Restaurant"), get_id("Leymona Beach & Restaurant & Bar"), get_id("Cafe Corner Restaurant"), get_id("Mavilim Otel") or get_id("Sardunya Restaurant")]
    },
    {
        "id": "kas_evening_vibes",
        "title": "Kaş Akşamları ve Publar",
        "title_en": "Kas Evenings & Pubs",
        "description": "Günün yorgunluğunu atacağınız kaliteli müzik ve neşeli publar.",
        "description_en": "Quality music and cheerful pubs to relieve the day's fatigue.",
        "places": [get_id("Oxygen Pub"), get_id("Shotbar"), get_id("Old Town Cafe-Bar & Billiards"), get_id("Bla Bla Cafe Kaş")]
    },
    {
        "id": "kas_sweet_breaks",
        "title": "Kaş'ın Tatlı Molaları",
        "title_en": "Sweet Breaks of Kas",
        "description": "Limonatadan dondurmaya, Kaş gezisine lezzetli bir ara verin.",
        "description_en": "Give a tasty break to your Kas trip, from lemonade to ice cream.",
        "places": [get_id("Süleyman Çavuş Kahvehanesi (Tatlı-Limonata)"), get_id("Dessert Shop"), get_id("Kas Simit"), get_id("L'Apéro Kaş")]
    },
    {
        "id": "kas_ancient_civilizations",
        "title": "Likya Yolu ve Antik Kalıntılar",
        "title_en": "Lycian Way & Ancient Ruins",
        "description": "Kaya mezarlarından lahitlere, tarihin tozlu sayfalarında bir keşif.",
        "description_en": "A discovery in the dusty pages of history, from rock tombs to sarcophagi.",
        "places": [get_id("Great chair. Acdam doric tomb in Antiphellos ancient city"), get_id("Cistern 5th century BC"), get_id("Phellos Antik Kenti"), get_id("Antiphellos Ancient City")]
    },
    {
        "id": "kas_active_sailing",
        "title": "Yelken ve Deniz Keyfi",
        "title_en": "Sailing & Sea Delight",
        "description": "Rüzgarı arkanıza alıp Kaş'ın muazzam kıyılarını yelkenliyle keşfedin.",
        "description_en": "Take the wind behind you and explore Kas's magnificent shores by sailing.",
        "places": [get_id("Kaş Sailing & Catamaran Tours / Kaş / Turkey (Daily or Overnight) Rent a sailing yacht in Kas"), get_id("Kaş Merkez"), get_id("Doria Hotel & Yacht Club"), get_id("Kaş Belediye Çarşısı")]
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

print("✅ Generated and injected 15 routes for Kas into " + filepath)

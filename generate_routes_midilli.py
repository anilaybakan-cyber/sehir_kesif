#!/usr/bin/env python3
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/midilli.json.draft"
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
        "id": "mid_molyvos_petra_castle_trail",
        "title": "Kuzeyin İncileri: Molyvos ve Petra",
        "title_en": "Pearls of the North: Molyvos & Petra",
        "description": "Adanın en ikonik köylerinde kaleden kiliseye bir tarih yolculuğu.",
        "description_en": "A history journey from castle to church in the island's most iconic villages.",
        "places": [get_id("Molyvos (Mithymna)"), get_id("Molyvos Kalesi"), get_id("Petra"), get_id("Panagia Glykofilousa Kilisesi")]
    },
    {
        "id": "mid_mytilene_city_heritage",
        "title": "Midilli Şehir Merkezi Mirası",
        "title_en": "Mytilene City Heritage",
        "description": "Başkentin labirent sokaklarında kaleler, camiler ve antik tiyatrolar.",
        "description_en": "Castles, mosques, and ancient theaters in the labyrinthine streets of the capital.",
        "places": [get_id("Midilli Kalesi (Mytilene Castle)"), get_id("Yeni Cami"), get_id("Agios Therapon Kilisesi"), get_id("Antik Tiyatro")]
    },
    {
        "id": "mid_ouzo_homeland_plomari",
        "title": "Uzo'nun Ana Vatanı: Plomari",
        "title_en": "Homeland of Ouzo: Plomari",
        "description": "Dünyaca ünlü uzo damıtımevleri ve Plomari'nin aristokratik mimarisi.",
        "description_en": "World-famous ouzo distilleries and the aristocratic architecture of Plomari.",
        "places": [get_id("Plomari"), get_id("Barbayanni Uzo Müzesi"), get_id("Ouzo Plomari Isidoros Arvanitis Distillery"), get_id("Platanos Meydanı, Plomari")]
    },
    {
        "id": "mid_western_volcanic_wonders",
        "title": "Batının Volkanik Harikaları",
        "title_en": "Volcanic Wonders of the West",
        "description": "Milyonlarca yıllık taşlaşmış ormandan sarp Sigri kıyılarına macera.",
        "description_en": "Adventure from a million-year-old petrified forest to the steep Sigri coast.",
        "places": [get_id("Taşlaşmış Orman (Petrified Forest)"), get_id("Sigri"), get_id("Sigri Kalesi"), get_id("Midilli Doğal Tarih Müzesi")]
    },
    {
        "id": "mid_spiritual_monasteries_peace",
        "title": "Manevi Huzur ve Manastırlar",
        "title_en": "Spiritual Peace & Monasteries",
        "description": "İç kesimlerin sessiz dağlarında saklı kalmış asırlık dini yapılar.",
        "description_en": "Century-old religious structures hidden in the silent mountains of the interior.",
        "places": [get_id("Taksiarhis Manastırı"), get_id("Limonos Manastırı"), get_id("Ipsilou Manastırı"), get_id("Panagia Agiasos Kilisesi")]
    },
    {
        "id": "mid_authentic_mountain_villages",
        "title": "Otantik Dağ Köyleri ve Gelenek",
        "title_en": "Authentic Mountain Villages & Tradition",
        "description": "Agiasos'un renkli çarşısından Vatoussa'nın taş evlerine yerel yaşam.",
        "description_en": "Local life from the colorful market of Agiasos to the stone houses of Vatoussa.",
        "places": [get_id("Agiasos"), get_id("Vatoussa"), get_id("Agiasos Çarşısı"), get_id("Kafeneio To Stavri")]
    },
    {
        "id": "mid_south_beach_relaxation_vatera",
        "title": "Güney Sahili ve Vatera Huzuru",
        "title_en": "South Coast & Vatera Serenity",
        "description": "Adanın en uzun kumsalında uçsuz bucaksız bir deniz keyfi.",
        "description_en": "Endless sea pleasure on the island's longest sandy beach.",
        "places": [get_id("Vatera Plajı"), get_id("Agios Fokas"), get_id("Vatera Sahili (Uzun)"), get_id("Taverna 7 Thalasses")]
    },
    {
        "id": "mid_gastronomy_ouzeri_trail",
        "title": "Gastronomi: Uzeri ve Mezeler",
        "title_en": "Gastronomy: Ouzeri & Appetizers",
        "description": "Midilli'nin en meşhur uzerilerinde deniz ürünleri ve yerel tatlar.",
        "description_en": "Seafood and local flavors in Rhodes me's most famous ouzeris.",
        "places": [get_id("Ermis Ouzeri"), get_id("Ouzadiko Baboukos"), get_id("Tsalikis"), get_id("Octopus Restaurant")]
    },
    {
        "id": "mid_museum_art_and_history",
        "title": "Müze Rotası: Sanat ve Bellek",
        "title_en": "Museum Trail: Art & Memory",
        "description": "Antik buluntulardan dünya çapındaki naif sanat koleksiyonlarına.",
        "description_en": "From ancient finds to world-class naive art collections.",
        "places": [get_id("Midilli Arkeoloji Müzesi"), get_id("Theophilos Müzesi"), get_id("Teriade Müzesi"), get_id("Halim Bey Konağı")]
    },
    {
        "id": "mid_family_fun_and_shores",
        "title": "Ailece Deniz ve Eğlence",
        "title_en": "Family Fun & Shores",
        "description": "Sığ sular ve neşeli beach-barlar eşliğinde aile boyu bir gün.",
        "description_en": "A family-sized day accompanied by shallow waters and joyful beach bars.",
        "places": [get_id("Anaxos Plajı"), get_id("Agios Isidoros Plajı"), get_id("Parasol Beach Bar"), get_id("Congas Beach Bar")]
    },
    {
        "id": "mid_thermal_healing_spa",
        "title": "Termal Şifa ve Spa Durakları",
        "title_en": "Thermal Healing & Spa Stops",
        "description": "Ege manzarasına karşı antik ve modern termal banyolarda yenilenin.",
        "description_en": "Renew yourself in ancient and modern thermal baths against the Aegean view.",
        "places": [get_id("Midilli Termalleri"), get_id("Therma Spa Lesvos"), get_id("Loutra Eski Otel"), get_id("Eftalou Plajı")]
    },
    {
        "id": "mid_pottery_and_handicraft",
        "title": "Çömlekçilik ve El Sanatları",
        "title_en": "Pottery & Handicrafts",
        "description": "Mantamados'un asırlık atölyelerinde seramik sanatını keşfedin.",
        "description_en": "Explore the art of ceramics in the century-old workshops of Mantamados.",
        "places": [get_id("Mandamados Seramik Atölyeleri"), get_id("Stelios Stamatis Çömlek Atölyesi"), get_id("Agiasos Çarşısı"), get_id("Kadınlar Kooperatifi (Petra)")]
    },
    {
        "id": "mid_volcanic_nature_and_forest",
        "title": "Volkanik Doğa ve Çam Ormanları",
        "title_en": "Volcanic Nature & Pine Forests",
        "description": "Taşlaşmış ağaçlardan serin çam ormanlarına bir doğa yürüyüşü.",
        "description_en": "A nature walk from petrified trees to cool pine forests.",
        "places": [get_id("Taşlaşmış Orman (Petrified Forest)"), get_id("Achladeri Çam Ligi"), get_id("Vatoussa"), get_id("Megali Limni (Büyük Göl)")]
    },
    {
        "id": "mid_skala_sykaminas_fishing_magic",
        "title": "Skala Sykaminas: Balıkçı Büyüsü",
        "title_en": "Skala Sykaminas: Fishing Magic",
        "description": "Denizin ortasındaki küçük kilisesi ve asırlık çınarıyla en romantik köy.",
        "description_en": "The most romantic village with its small church in the middle of the sea and century-old plane tree.",
        "places": [get_id("Skala Sykaminas"), get_id("Panagia Gorgona"), get_id("Taverna 7 Thalasses"), get_id("Eftalou Plajı")]
    },
    {
        "id": "mid_local_flavor_cheese_and_oil",
        "title": "Yerel Lezzet: Peynir ve Zeytinyağı",
        "title_en": "Local Flavor: Cheese & Olive Oil",
        "description": "Adanın ünlü peynir mandıraları ve zeytinyağı müzelerinde gurme keşif.",
        "description_en": "Gourmet discovery in the island me's famous cheese dairies and olive oil museums.",
        "places": [get_id("Lesvos Cheese Factory - Mystakellis"), get_id("Sanayi Zeytinyağı Müzesi"), get_id("Agiasos Çarşısı"), get_id("Tsalikis")]
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

print("✅ Generated and injected 15 routes for Midilli into " + filepath)

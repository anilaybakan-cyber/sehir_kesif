
import json

filepath = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/cesme.json.draft"
with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get("highlights", [])

def get_id(name):
    for p in highlights:
        if p["name"] == name:
            return p.get("id") or str(p["name"]).lower().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
    return None

routes_data = [
    {
        "id": "cesme_classic_center",
        "title": "Çeşme Klasikleri",
        "title_en": "Cesme Classics",
        "description": "Kaleden marinaya, Çeşme merkezinin en ikonik noktalarını keşfedin.",
        "description_en": "Discover the most iconic spots of Cesme center, from the castle to the marina.",
        "places": [get_id("Çeşme Kalesi"), get_id("Çeşme Marina"), get_id("Cezayirli Gazi Hasan Paşa Anıtı"), get_id("Ayios Haralambos Kilisesi")]
    },
    {
        "id": "alacati_streets",
        "title": "Alaçatı Sokakları ve Yel Değirmenleri",
        "title_en": "Alacati Streets & Windmills",
        "description": "Arnavut kaldırımlı sokaklarda kaybolup tarihi yel değirmenlerinde gün batımını izleyin.",
        "description_en": "Get lost in the cobbled streets and watch the sunset at the historic windmills.",
        "places": [get_id("Alaçatı Çarşı"), get_id("Alaçatı Yel Değirmenleri"), get_id("Hacımemiş Mahallesi"), get_id("Köşe Kahve")]
    },
    {
        "id": "cesme_beach_luxury",
        "title": "Lüks Plaj Deneyimi",
        "title_en": "Luxury Beach Experience",
        "description": "Çeşme'nin en şık beach club'larında deniz, güneş ve eğlencenin tadını çıkarın.",
        "description_en": "Enjoy the sea, sun, and fun at Cesme's most stylish beach clubs.",
        "places": [get_id("Before Sunset Beach"), get_id("Fly-Inn Beach"), get_id("The Beach of Momo"), get_id("Sole & Mare Beach Club")]
    },
    {
        "id": "alacati_gourmet",
        "title": "Alaçatı Gastronomi Rotası",
        "title_en": "Alacati Gourmet Route",
        "description": "Ege mutfağının en seçkin lezzetlerini Alaçatı'nın tescilli restoranlarında tadın.",
        "description_en": "Taste the most distinguished flavors of Aegean cuisine in Alacati's registered restaurants.",
        "places": [get_id("Asma Yaprağı"), get_id("Fava Alaçatı"), get_id("Eflatun Alaçatı"), get_id("Dutlu Kahve") or get_id("Köşe Kahve")]
    },
    {
        "id": "cesme_family_fun",
        "title": "Ailece Eğlence",
        "title_en": "Family Fun",
        "description": "Aquapark'tan sığ plajlara, çocuklu aileler için en keyifli duraklar.",
        "description_en": "From aquaparks to shallow beaches, the most pleasant stops for families with children.",
        "places": [get_id("Oasis Aquapark"), get_id("Aqua Toy City"), get_id("Çeşme, Ilıca Yıldızburnu küçük halk plajı."), get_id("Yaz gülü cafe")]
    },
    {
        "id": "cesme_hidden_coves",
        "title": "Gizli Koylar ve Doğa",
        "title_en": "Hidden Bays & Nature",
        "description": "Kalabalıktan uzak, doğanın kalbinde turkuaz sularla buluşun.",
        "description_en": "Meet the turquoise waters in the heart of nature, away from the crowds.",
        "places": [get_id("Delikli Koy"), get_id("Kleopatra Koyu"), get_id("Bademlik Koy"), get_id("Tanay Tabiat Parkı")]
    },
    {
        "id": "alacati_nightlife",
        "title": "Alaçatı Gece Hayatı",
        "title_en": "Alacati Nightlife",
        "description": "Gece boyu süren eğlence, kaliteli müzik ve popüler buluşma noktaları.",
        "description_en": "All-night entertainment, quality music, and popular meeting points.",
        "places": [get_id("ZUM Alaçatı"), get_id("The Barra Alaçatı"), get_id("Cahide Alaçatı"), get_id("Wuu Club")]
    },
    {
        "id": "cesme_seafood_dinner",
        "title": "Denize Karşı Balık Keyfi",
        "title_en": "Seafood Dinner by the Sea",
        "description": "Dalyan ve Marina'nın en meşhur balıkçılarında unutulmaz bir akşam yemeği.",
        "description_en": "An unforgettable dinner at the most famous fish restaurants of Dalyan and Marina.",
        "places": [get_id("Ferdi Baba Restaurant - Çeşme Marina"), get_id("Horasan Balık"), get_id("Levent'in Yeri"), get_id("Dalyan Yelken Restoran Neco’nun Yeri")]
    },
    {
        "id": "cesme_breakfast_route",
        "title": "Ege Kahvaltısı Durakları",
        "title_en": "Aegean Breakfast Stops",
        "description": "Güne taze yerel ürünler ve eşsiz Ege manzarasıyla başlamak isteyenlere.",
        "description_en": "For those who want to start the day with fresh local products and unique Aegean views.",
        "places": [get_id("Tash Mekan Kahvaltı & Otel"), get_id("Çeşme Bahçelika Kahvaltı - Çeşme"), get_id("Tarçın Kahvaltı & Kafe"), get_id("Yaz gülü cafe")]
    },
    {
        "id": "cesme_castle_and_museums",
        "title": "Sanat ve Tarih İzinde",
        "title_en": "Tracing Art & History",
        "description": "Çeşme'nin tarihi dokusunu ve kültürel zenginliğini keşfedin.",
        "description_en": "Discover the historical texture and cultural richness of Cesme.",
        "places": [get_id("Çeşme Kalesi"), get_id("Çeşme Müzesi"), get_id("Uzo Müzesi"), get_id("Erythrai Tiyatrosu")]
    },
    {
        "id": "cesme_sunset_viewpoints",
        "title": "Efsanevi Gün Batımı Noktaları",
        "title_en": "Legendary Sunset Viewpoints",
        "description": "Günü uğurlamak için Çeşme'nin en güzel manzaralı terasları ve kuleleri.",
        "description_en": "Cesme's most beautiful terraces and towers to bid farewell to the day.",
        "places": [get_id("Point View"), get_id("Nezir's Tower"), get_id("Cava Roof"), get_id("Dinlenme Terasları")]
    },
    {
        "id": "cesme_shopping_and_souvenirs",
        "title": "Alışveriş ve Hediyelik",
        "title_en": "Shopping & Souvenirs",
        "description": "Yerel tatlardan tasarım butiklere Çeşme ve Alaçatı çarşıları.",
        "description_en": "From local tastes to design boutiques, Cesme and Alacati markets.",
        "places": [get_id("Alaçatı Pazaryeri Camii"), get_id("İmren Helva Ve Tatlı Evi"), get_id("Hasan Mersin Sakız Reçel Tatlı ve Dondurma Evi"), get_id("Alaçatı Çarşı")]
    },
    {
        "id": "cesme_thermal_wellness",
        "title": "Termal ve Huzur",
        "title_en": "Thermal & Wellness",
        "description": "Ilıca'nın şifalı sularında yenilenme ve huzur dolu bir gün.",
        "description_en": "A day of renewal and peace in the healing waters of Ilica.",
        "places": [get_id("Ilica Plaj"), get_id("Çeşme, Ilıca Yıldızburnu küçük halk plajı."), get_id("Altın Yunus Hotel & Spa - Çeşme"), get_id("paşalimanı")]
    },
    {
        "id": "cesme_boat_trips",
        "title": "Mavi Yolculuk ve Adalar",
        "title_en": "Blue Voyage & Islands",
        "description": "Marinadan kalkan teknelerle Ege'nin turkuaz sularına açılın.",
        "description_en": "Sail into the turquoise waters of the Aegean with boats departing from the marina.",
        "places": [get_id("Çeşme Marina"), get_id("Nirvana Cesme Tekne Turu"), get_id("Çeşme Tekne Turu / Grandstar Çeşme Tekne Turları"), get_id("Marin Alaçatı")]
    },
    {
        "id": "cesme_street_flavors",
        "title": "Çeşme Sokak Lezzetleri",
        "title_en": "Cesme Street Flavors",
        "description": "Kumru'dan boyoza, kentin en meşhur hızlı lezzet durakları.",
        "description_en": "From Kumru to boyoz, the city's most famous fast food spots.",
        "places": [get_id("Kumrucu Şevki Çeşme Merkez-Cafe-Cafeterya-Fast Food-Çeşme Kumrucu"), get_id("Kumrucu Hüseyin Gıda San. Tic. Ltd. Şti."), get_id("Dost Pide & Pizza"), get_id("Veli Usta")]
    }
]

# Cleanup None values in places (if any name was not found)
for r in routes_data:
    r["places"] = [p for p in r["places"] if p is not None]

if isinstance(data, list):
    # If it is a list, we can't easily inject routes unless we change format
    # For now, let's skip or wrap it
    pass
else:
    data["curated_routes"] = routes_data

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Generated and injected 15 routes for Cesme into " + filepath)

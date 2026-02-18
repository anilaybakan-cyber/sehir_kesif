import json

# Manual enrichment data (Rovaniemi Batch 3 FINAL: 12 items)
updates = {
    "Lampivaara Amethyst Mine": {
        "description": "Laponya'daki ametist madeni, kendi taşınızı kazabilme deneyimi. Doğal ametist, maden turu ve benzersiz hatıra.",
        "description_en": "Amethyst mine in Lapland with experience of digging your own stone. Natural amethyst, mine tour, and unique souvenir."
    },
    "Crystal Arctic Suites": {
        "description": "Cam tavanlı lüks suit konaklama, Kuzey Işıkları izleme. Aurora borealis, özel romantik deneyim ve nordik lüks.",
        "description_en": "Luxury suite accommodation with glass ceiling for Northern Lights viewing. Aurora borealis, private romantic experience, and Nordic luxury."
    },
    "Motelli Rovaniemi": {
        "description": "Bütçe dostu motel konaklama, yol gezginleri için pratik seçenek. Otopark, temiz odalar ve merkezi konum.",
        "description_en": "Budget-friendly motel accommodation, practical option for road travelers. Parking, clean rooms, and central location."
    },
    "Guesthouse Borealis": {
        "description": "Aile işletmesi konuk evi, samimi atmosfer ve yerel ipuçları. Ev yapımı kahvaltı, misafirperverlik ve bütçe dostu.",
        "description_en": "Family-run guesthouse with intimate atmosphere and local tips. Homemade breakfast, hospitality, and budget-friendly."
    },
    "Santasport Apartment Hotel": {
        "description": "Santasport kompleksinde apart otel, uzun konaklamalar ve aileler için. Mutfaklı odalar, spor tesislerine erişim.",
        "description_en": "Apartment hotel in Santasport complex for extended stays and families. Rooms with kitchen, access to sports facilities."
    },
    "Forenom Aparthotel Rovaniemi": {
        "description": "Şehir merkezinde self-catering daireler, iş ve tatil için. Modern tesisler, mutfak ve ev konforu.",
        "description_en": "Self-catering apartments in city center for business and vacation. Modern facilities, kitchen, and home comfort."
    },
    "Arctic Lifestyle": {
        "description": "Laponya yaşam tarzı ürünleri ve hediyelik dükkanı. Nordik tasarım, yerel el sanatları ve arktik temalı ürünler.",
        "description_en": "Lapland lifestyle products and gift shop. Nordic design, local handicrafts, and Arctic-themed products."
    },
    "Access Lapland": {
        "description": "Safari turları ve macera aktiviteleri organizatörü. Kar motoru, husky ve özelleştirilmiş Laponya deneyimleri.",
        "description_en": "Safari tours and adventure activities organizer. Snowmobile, husky, and customized Lapland experiences."
    },
    "Beyond Arctic": {
        "description": "Lüks ve butik Laponya turları, özel deneyimler ve VIP hizmet. Kuzey Işıkları avcılığı, helikopter turları ve premium macera.",
        "description_en": "Luxury and boutique Lapland tours with private experiences and VIP service. Northern Lights hunting, helicopter tours, and premium adventure."
    },
    "Auttiköngäs": {
        "description": "Rovaniemi yakınındaki şelaleli doğa alanı, yürüyüş rotaları ve fotoğrafçılık. Lapon doğası, nehir manzarası ve huzur.",
        "description_en": "Nature area with waterfalls near Rovaniemi with hiking trails and photography. Lappish nature, river views, and peace."
    },
    "Napapiirin Lahja": {
        "description": "Kuzey Kutup Dairesi'nde hediyelik eşya ve Lapon ürünleri dükkanı. Hatıralar, yerel el sanatları ve Finlandiya ürünleri.",
        "description_en": "Souvenir and Lappish products shop at Arctic Circle. Memorabilia, local handicrafts, and Finnish products."
    },
    "Snowman World Glass Resort": {
        "description": "Kardan adam temalı cam iglo konaklama, buz bar ve kış aktiviteleri. Kuzey Işıkları, aile eğlencesi ve büyülü atmosfer.",
        "description_en": "Snowman-themed glass igloo accommodation with ice bar and winter activities. Northern Lights, family fun, and magical atmosphere."
    }
}

filepath = 'assets/cities/rovaniemi.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Rovaniemi Batch 3 FINAL).")

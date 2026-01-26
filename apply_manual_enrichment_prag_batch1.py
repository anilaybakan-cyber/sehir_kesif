import json

# Manual enrichment data (Prague - ALL 18 items)
updates = {
    "Platýz Passage": {
        "description": "Prag'ın en eski pasajlarından biri, Národní Třída üzerinde. Sessiz iç avlu, sanat galerileri ve şık kafeler.",
        "description_en": "One of Prague's oldest passages, on Národní Třída. Quiet inner courtyard, art galleries, and chic cafes."
    },
    "Petřín Tower": {
        "description": "Prag'ın 'Küçük Eiffel'i, Petřín Tepesi'nde demir gözetleme kulesi. 299 basamakla çıkılan en iyi şehir manzarası.",
        "description_en": "Prague's 'Little Eiffel', iron observation tower on Petřín Hill. Best city view climbed by 299 steps."
    },
    "Petřín Hill Gardens": {
        "description": "Gül bahçeleri ve ağaçlarla kaplı romantik tepe. Füniküler ile ulaşım, Aynalar Labirenti ve Prag manzarası.",
        "description_en": "Romantic hill covered with rose gardens and trees. Funicular access, Mirror Maze, and Prague views."
    },
    "Strahov Monastery Library": {
        "description": "Dünyanın en güzel barok kütüphanelerinden biri. Felsefe ve Teoloji salonları, freskli tavanlar ve eski kitap kokusu.",
        "description_en": "One of the world's most beautiful Baroque libraries. Theological and Philosophical Halls, frescoed ceilings, and smell of old books."
    },
    "Strahov Monastery Brewery": {
        "description": "Manastırın yanında 17. yüzyıldan beri bira üreten tarihi mekan. Koyu renkli St. Norbert birası ve gulaş.",
        "description_en": "Historic venue next to monastery brewing beer since 17th century. Dark St. Norbert beer and goulash."
    },
    "Kafka Museum": {
        "description": "Franz Kafka'nın hayatı ve eserlerine adanmış karanlık ve etkileyici müze. 'Dava' ve 'Dönüşüm' atmosferi, el yazmaları.",
        "description_en": "Dark and impressive museum dedicated to life and works of Franz Kafka. Atmosphere of 'The Trial' and 'Metamorphosis', manuscripts."
    },
    "Kampa Island": {
        "description": "Vltava Nehri üzerindeki sakin ve yeşil ada, 'Prag'ın Venedik'i'. Modern sanat müzesi, sarı penguenler ve park.",
        "description_en": "Quiet green island on Vltava River, 'Venice of Prague'. Modern art museum, yellow penguins, and park."
    },
    "Municipal House": {
        "description": "Art Nouveau mimarinin şaheseri (Obecní dům). Smetana Salonu'nda konserler, lüks Fransız restoranı ve tarihi dekor.",
        "description_en": "Masterpiece of Art Nouveau architecture (Obecní dům). Concerts in Smetana Hall, luxury French restaurant, and historic decor."
    },
    "Powder Tower": {
        "description": "Eski Şehir'e giriş kapısı olan gotik kule. Eskiden barut deposu olarak kullanılmış, tepesinden şehir panoraması.",
        "description_en": "Gothic tower serving as gateway to Old Town. Formerly used as gunpowder store, city panorama from top."
    },
    "Havelská Market": {
        "description": "1232'den beri kurulan Prag'ın en eski açık pazarı. Taze meyve, sebze, ahşap oyuncaklar ve turistik hediyelikler.",
        "description_en": "Prague's oldest open market dating back to 1232. Fresh fruit, vegetables, wooden toys, and tourist souvenirs."
    },
    "Loreta Prague": {
        "description": "Barok hac yeri, Santa Casa kopyası ve hazine odası. 6.222 elmaslı 'Prag Güneşi' monstransı ve çan sesi.",
        "description_en": "Baroque pilgrimage site, replica of Santa Casa, and treasury. 'Prague Sun' monstrance with 6,222 diamonds and carillon."
    },
    "Klementinum Library": {
        "description": "Barok mimarinin incisi, dünyanın en estetik kütüphanelerinden. Astronomi kulesi, dev küreler ve tarihi atmosfer.",
        "description_en": "Pearl of Baroque architecture, one of world's most aesthetic libraries. Astronomy tower, giant globes, and historic atmosphere."
    },
    "Naplavka Farmers Market": {
        "description": "Vltava kıyısında Cumartesi günleri kurulan popüler pazar. Canlı müzik, kahve, sokak lezzetleri ve nehirde kuğular.",
        "description_en": "Popular market on Vltava embankment on Saturdays. Live music, coffee, street food, and swans on river."
    },
    "Vítkov Hill Monument": {
        "description": "Devasa Jan Žižka atlı heykeli ve Ulusal Anıt. Sovyet mimarisi etkisi, bilinmeyen asker mezarı ve en iyi gün batımı.",
        "description_en": "Massive equestrian statue of Jan Žižka and National Monument. Soviet architecture influence, tomb of unknown soldier, and best sunset."
    },
    "Letná Park": {
        "description": "Şehre tepeden bakan devasa park ve metronom. Kaykaycılar, bira bahçesi (Beer Garden) ve köprü manzaraları.",
        "description_en": "Huge park overlooking city with metronome. Skateboarders, Beer Garden, and bridge views."
    },
    "Žižkov TV Tower": {
        "description": "Üzerinde emekleyen bebek heykelleri (David Černý) olan fütüristik kule. 93 metrede gözlem güvertesi ve garip mimari.",
        "description_en": "Futuristic tower with crawling baby statues (David Černý). Observation deck at 93 meters and weird architecture."
    },
    "Trdelník Shops": {
        "description": "Sokaklarda köz ateşinde pişen tarçınlı ve şekerli rulo hamur tatlısı (baca keki). Dondurmalı veya çikolatalı.",
        "description_en": "Chatcoal-grilled cinnamon and sugar roll pastry (chimney cake) on streets. With ice cream or chocolate."
    },
    "Staropramen Brewery Tour": {
        "description": "Smíchov bölgesinde, Prag'ın ünlü birasının üretim tesisi turu. Bira yapımı tarihi ve barında tadım.",
        "description_en": "Tour of production facility of Prague's famous beer in Smíchov. Beer making history and tasting at bar."
    }
}

filepath = 'assets/cities/prag.json'
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

print(f"\n✅ Manually enriched {count} items (Prague - COMPLETE).")

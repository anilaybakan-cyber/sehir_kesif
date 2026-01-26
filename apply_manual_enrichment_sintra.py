import json

# Manual enrichment data (Batch 2: 15 items)
updates = {
    "Nortada": {
        "description": "Praia Grande'nin altın kumsallarına nazır, okyanus esintisiyle taze balık ve deniz ürünlerinin tadını çıkarabileceğiniz geniş ve ferah bir restoran. Gün batımında terasında oturup, dalgaların sesi eşliğinde lezzetli bir akşam yemeği yemek paha biçilemez.",
        "description_en": "A spacious restaurant overlooking the golden sands of Praia Grande where you can enjoy fresh fish and seafood with the ocean breeze. It is priceless to sit on its terrace at sunset and have a delicious dinner accompanied by the sound of the waves."
    },
    "Café da Natália": {
        "description": "São Pedro de Sintra'nın kalbinde, ev yapımı devasa kekleri ve samimi ortamıyla ün salmış, yerel halkın ve turistlerin uğrak noktası. Özellikle havuçlu keki ve yanında sunulan taze çayı, yorucu bir Sintra gezisinden sonra en tatlı ödül.",
        "description_en": "A destination for locals and tourists in the heart of São Pedro de Sintra, famous for its huge homemade cakes and friendly atmosphere. Its carrot cake and fresh tea served alongside are the sweetest reward after a tiring Sintra tour."
    },
    "Moinho de Vento": {
        "description": "Eski bir yel değirmeninin restore edilmesiyle restorana dönüştürülen bu mekan, hem tarihi dokusu hem de panoramik manzarasıyla büyülüyor. Geleneksel Portekiz yemeklerini, rustik ve romantik bir ortamda deneyimlemek isteyenler için eşsiz bir seçenek.",
        "description_en": "Converted into a restaurant by restoring an old windmill, this venue enchants with both its historical texture and panoramic view. A unique option for those wanting to experience traditional Portuguese dishes in a rustic and romantic setting."
    },
    "Tascantiga II": {
        "description": "Sintra'nın popüler tapas mekanı Tascantiga'nın bu ikinci şubesi, daha geniş oturma alanıyla kalabalık gruplar için ideal. Portekiz usulü 'petiscos' (tapas) çeşitlerini, rahat ve neşeli bir atmosferde paylaşmak için harika bir adres.",
        "description_en": "This second branch of Sintra's popular tapas venue Tascantiga is ideal for large groups with its wider seating area. A great address to share Portuguese style 'petiscos' (tapas) varieties in a relaxed and cheerful atmosphere."
    },
    "Garagem Café": {
        "description": "Otomobil tutkunları için bir cennet olan bu kafe, klasik araba parçaları ve motor sporları memorabilia'sı ile dekore edilmiş. Sadece ilginç dekorasyonuyla değil, kaliteli kahveleri ve lezzetli atıştırmanlıklarıyla da keyifli bir mola vadediyor.",
        "description_en": "A paradise for car enthusiasts, this cafe is decorated with classic car parts and motorsport memorabilia. It promises a pleasant break not only with its interesting decoration but also with its quality coffees and delicious snacks."
    },
    "Hop-Sin Brew": {
        "description": "Sintra'nın Colares bölgesinde, kendi üretimleri olan taze kraft biralarıyla bira severleri mutlu eden yerel bir mikro-bira fabrikası ve pub. Farklı aroma profillerine sahip biraları tadarken, samimi bahçesinde dostlarınızla sohbet edebilirsiniz.",
        "description_en": "A local micro-brewery and pub in the Colares region of Sintra that makes beer lovers happy with their own production fresh craft beers. You can chat with your friends in its friendly garden while tasting beers with different aroma profiles."
    },
    "Casa do Preto": {
        "description": "Sintra'nın geleneksel tatlısı 'Queijada' denince akla gelen ilk, efsaneleşmiş pastanelerden biri. Tarihi atmosferini koruyan bu mekanda, fırından yeni çıkmış taze queijada'ların kokusu sizi içeri davet ediyor.",
        "description_en": "One of the legendary patisseries that comes to mind first when mentioning Sintra's traditional dessert 'Queijada'. In this venue preserving its historic atmosphere, the smell of fresh queijadas right out of the oven invites you in."
    },
    "Restaurante Regional de Sintra": {
        "description": "Sintra Belediye Binası'nın tam karşısında yer alan, merkezi konumu ve hızlı servisiyle turistlerin güvenilir limanı. Geleneksel Portekiz mutfağının klasiklerini, temiz ve nezih bir ortamda, makul fiyatlarla sunuyor.",
        "description_en": "A reliable haven for tourists with its central location right across Sintra City Hall and fast service. It offers classics of traditional Portuguese cuisine in a clean and decent environment at reasonable prices."
    },
    "Hamburgueria do Maçãs": {
        "description": "Praia das Maçãs plajında geçirilen keyifli bir günün ardından, el yapımı, sulu ve lezzetli hamburgerleriyle açlığınızı yatıştırmak için en iyi durak. Rahat ortamı ve geniş menüsü, hem çocuklu aileleri hem de gençleri cezbediyor.",
        "description_en": "The best stop to satisfy your hunger with handmade, juicy, and delicious burgers after a pleasant day at Praia das Maçãs beach. Its relaxed atmosphere and extensive menu attract both families with children and young people."
    },
    "Bar Saloon": {
        "description": "Sintra'da Vahşi Batı rüzgarları estiren, yer fıstığı kabuklarını yere atmanın serbest olduğu, özgür ruhlu ve eğlenceli bir bar. Country müzik eşliğinde biranızı yudumlayıp, bilardo oynayabileceğiniz, şehrin en karakterli gece mekanlarından.",
        "description_en": "A free-spirited and fun bar blowing Wild West winds in Sintra, where throwing peanut shells on the floor is allowed. One of the city's most characteristic nightlife venues where you can sip your beer accompanied by country music and play billiards."
    },
    "Tasca do Xico": {
        "description": "Küçük, samimi ve gerçek bir Portekiz 'tasca'sı (meyhane) deneyimi arayanlar için gizli bir hazine. Günlük değişen menüsü, taze malzemelerle hazırlanan mezeleri ve sıcakkanlı işletmecileriyle kendinizi evinizde hissettirecek.",
        "description_en": "A hidden treasure for those looking for a small, friendly, and authentic Portuguese 'tasca' (tavern) experience. It will make you feel at home with its daily changing menu, appetizers prepared with fresh ingredients, and warm-hearted owners."
    },
    "Gelato Davvero": {
        "description": "Roma'daki ustalardan öğrenilen tekniklerle hazırlanan, katkısız ve doğal İtalyan dondurması sunan popüler dondurmacı. Mevsim meyveleriyle yapılan sorbeleri ve yoğun kıvamlı kremalı çeşitleri, sıcak bir yaz gününde serinlemenin en lezzetli yolu.",
        "description_en": "Popular ice cream shop offering pure and natural Italian ice cream prepared with techniques learned from masters in Rome. Sorries made with seasonal fruits and dense creamy varieties are the most delicious way to cool off on a hot summer day."
    },
    "Igreja de Santo André": {
        "description": "Mafra'nın tarihi mahallesinde, 13. yüzyılın gotik mimarisini günümüze taşıyan, şehrin en eski ve en önemli kiliselerinden biri. Sade dış cephesinin ardında, yüzyıllara meydan okuyan mistik bir atmosfer ve tarihi detaylar saklıyor.",
        "description_en": "One of the city's oldest and most important churches carrying 13th-century Gothic architecture to the present day in Mafra's historic neighborhood. Behind its simple facade, it hides a mystical atmosphere and historic details defying centuries."
    },
    "Jardim do Cerco": {
        "description": "Mafra Ulusal Sarayı'nın hemen arkasında uzanan, Versay Sarayı'nın bahçelerinden ilham alınarak tasarlanmış büyüleyici bir barok bahçe. Fıskiyeli havuzları, geometrik çalıları ve asırlık ağaçlarıyla, saray ihtişamını doğayla buluşturan bir kaçış noktası.",
        "description_en": "A fascinating baroque garden stretching right behind the Mafra National Palace, designed with inspiration from the gardens of the Palace of Versailles. An escape point meeting palace grandeur with nature with its fountain pools, geometric shrubs, and centuries-old trees."
    },
    "Cascais": {
        "description": "Bir zamanlar kralların yazlık tatil yeri olan, günümüzde ise Portekiz Rivierası'nın en popüler ve şık sahil kasabası. Zarif mimarisi, lüks butikleri, canlı marinası ve altın renkli plajlarıyla hem dinlenmek hem de eğlenmek isteyenler için mükemmel bir destinasyon.",
        "description_en": "Once the summer holiday resort of kings, now the most popular and stylish coastal town of the Portuguese Riviera. A perfect destination for those wanting both to relax and have fun with its elegant architecture, luxury boutiques, lively marina, and golden beaches."
    }
}

filepath = 'assets/cities/sintra.json'
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

print(f"\n✅ Manually enriched {count} items.")

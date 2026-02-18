import json

# Manual enrichment data (Batch 4: 20 items)
updates = {
    "Casa do Cipreste": {
        "description": "20. yüzyılın başlarında inşa edilen, Art Nouveau ve Manueline öğelerini harmanlayan bu mimari başyapıt, Sintra dağlarına hakim konumuyla dikkat çekiyor. Selvi ağaçlarıyla çevrili bahçesi ve karma mimari stiliyle bölgenin en fotoğrafik yapılarından biri.",
        "description_en": "This architectural masterpiece, blending Art Nouveau and Manueline elements built at the beginning of the 20th century, stands out with its position overlooking Sintra mountains. One of the most photogenic structures of the region with its cypress-surrounded garden and mixed architectural style."
    },
    "Fonte Mourisca": {
        "description": "Sintra'ya girişte ziyaretçileri karşılayan, Mağribi (Moorish) etkilerle süslenmiş görkemli bir tarihi çeşme. 19. yüzyılda romantik dönemin ruhunu yansıtacak şekilde tasarlanan yapı, renkli çinileri ve at nalı kemerleriyle şehrin masalsı atmosferinin ilk işareti.",
        "description_en": "A magnificent historic fountain decorated with Moorish influences welcoming visitors at the entrance to Sintra. Designed in the 19th century to reflect the spirit of the romantic period, the structure is the first sign of the city's fairytale atmosphere with its colorful tiles and horseshoe arches."
    },
    "Fonte da Pipa": {
        "description": "Pena Sarayı'na giden orman yolunun başlangıcında, efsanelere konu olmuş tarihi bir çeşme. Şarap fıçısı şeklindeki muslukları ve geleneksel azulejo çinileriyle süslü bu çeşmenin suyunu içenlerin tekrar Sintra'ya döneceğine inanılıyor.",
        "description_en": "A historic fountain at the beginning of the forest path to Pena Palace, subject to legends. It is believed that those who drink the water of this fountain, decorated with wine barrel-shaped taps and traditional azulejo tiles, will return to Sintra again."
    },
    "Cascata de Pisões": {
        "description": "Quinta dos Pisões mülkünün yakınında, yemyeşil ormanın içinde gizlenmiş küçük ama büyüleyici bir şelale. Yürüyüş rotalarının ödüllendirici bir molası olarak, serin sularda ayaklarınızı dinlendirip doğanın sesini dinleyebileceğiniz huzurlu bir köşe.",
        "description_en": "A small but charming waterfall hidden in the lush green forest near the Quinta dos Pisões estate. As a rewarding break on hiking routes, a peaceful corner where you can rest your feet in cool waters and listen to the sounds of nature."
    },
    "Cascata de Anços": {
        "description": "Sintra-Cascais Doğal Parkı'nın ormanlarında saklanan, az bilinen güzellerden biri olan bu şelale, keşfedilmeyi bekliyor. Yağmurlu mevsimde daha gür akan suları ve çevresindeki yosun kaplı kayalarıyla, doğa fotoğrafçıları için eşsiz kareler sunuyor.",
        "description_en": "One of the lesser-known beauties hidden in the forests of Sintra-Cascais Natural Park, this waterfall awaits to be discovered. With its waters flowing more abundantly in rainy season and moss-covered rocks around, it offers unique shots for nature photographers."
    },
    "Anta de Adrenunes": {
        "description": "Bronz Çağı'ndan (yaklaşık 5000 yıl öncesinden) kalma, devasa granit bloklardan oluşan megalitik bir anıt mezar. Portekiz'in dolmen (anta) mirasının önemli örneklerinden biri olan bu antik yapı, tarih öncesi dönemlere duyulan merakı uyandırıyor.",
        "description_en": "A megalithic monument tomb consisting of giant granite blocks from the Bronze Age (about 5000 years ago). One of the important examples of Portugal's dolmen (anta) heritage, this ancient structure arouses curiosity about prehistoric times."
    },
    "Pedra Amarela Field Camp": {
        "description": "Sintra dağlarının yükseklerinde, ormanla çevrili geniş açık alanda kurulu bir izci ve doğa aktivite kampı. Yürüyüşçüler, kampçılar ve macera grupları için piknik alanları, yürüyüş parkurları başlangıç noktaları ve panaoramik manzaralar sunan popüler bir buluşma noktası.",
        "description_en": "A scout and nature activity camp set up in a wide open area surrounded by forest high in Sintra mountains. A popular meeting point offering picnic areas, hiking trail starting points, and panoramic views for hikers, campers, and adventure groups."
    },
    "Convento da Trindade": {
        "description": "Sintra'nın merkezinde, modern yapıların arasında sessiz bir köşede bekleyen eski Trinitarian manastırı kalıntıları. Şehrin hareketli turistik dokusundan uzakta, geçmişin izlerini taşıyan bu arkeolojik alan, tarih meraklıları için sakin bir keşif noktası.",
        "description_en": "Ruins of the old Trinitarian monastery waiting in a quiet corner among modern buildings in the center of Sintra. Away from the city's bustling tourist texture, this archaeological site bearing traces of the past is a quiet discovery point for history enthusiasts."
    },
    "Igreja de São Pedro de Penaferrim": {
        "description": "São Pedro de Sintra mahallesinde, 18. yüzyıl Portekiz barok mimarisinin güzel bir örneği olan tarihi kilise. İç mekanını süsleyen geleneksel mavi-beyaz azulejo çini panelleri ve ahşap altın yaldızlı sunağıyla, dini sanat tutkunları için değerli bir durak.",
        "description_en": "A historic church in the São Pedro de Sintra neighborhood, a beautiful example of 18th century Portuguese baroque architecture. With traditional blue-white azulejo tile panels decorating its interior and wooden gilded altar, a valuable stop for religious art enthusiasts."
    },
    "Parque das Merendas": {
        "description": "Moorish Castle ve Pena Sarayı'na giden yol üzerinde, devasa ağaçların gölgesinde piknik yapmak için ideal bir dinlenme noktası. Masa ve banklarıyla donatılmış bu yeşil alan, zorlu kale tırmanışından önce veya sonra enerji toplamak için mükemmel bir ara mola yeri.",
        "description_en": "An ideal rest point for picnicking in the shade of giant trees on the way to Moorish Castle and Pena Palace. Equipped with tables and benches, this green area is a perfect stopover to gather energy before or after the challenging castle climb."
    },
    "Moinho do Penedo": {
        "description": "Penedo köyünün tepesinde, körfeze ve okyanusa bakan restore edilmiş geleneksel bir yel değirmeni. Sintra bölgesinin rüzgar enerjisindin nasıl yararlandığını gösteren bu tarihi yapı, günbatımında muhteşem fotoğraf kareleri sunan popüler bir manzara noktası.",
        "description_en": "A restored traditional windmill on top of Penedo village, overlooking the bay and ocean. This historic structure showing how the Sintra region benefited from wind energy is a popular viewpoint offering magnificent photo shots at sunset."
    },
    "Ciência Viva Center of Sintra": {
        "description": "Çocukların ve gençlerin bilimle eğlenceli bir şekilde tanışmasını sağlayan interaktif bilim merkezi. Deney stasyonları, heyecan verici sergiler ve atölyelerle, özellikle ailelerin yağmurlu bir günde vakit geçirmesi için harika bir alternatif sunan eğitici mekan.",
        "description_en": "An interactive science center enabling children and young people to meet science in a fun way. With experiment stations, exciting exhibitions, and workshops, an educational venue offering a great alternative especially for families to spend time on a rainy day."
    },
    "Quinta dos Pisões": {
        "description": "Sintra ormanlarının içinde, tarihi bir çiftlik evi ve antik su değirmeni kalıntılarını barındıran pitoresk bir mülk. Doğa yürüyüş rotalarının üzerinde bulunan bu eski quinta, geçmişin kırsal yaşamını hayal etmek ve mola vermek için atmosferik bir durak.",
        "description_en": "A picturesque estate in the Sintra forests, housing a historic farmhouse and ancient water mill ruins. This old quinta on nature hiking routes is an atmospheric stop to imagine past rural life and take a break."
    },
    "Miradouro de Santa Eufémia": {
        "description": "Sintra dağlarının en yüksek noktalarından birinde, 360 derecelik panoramik manzara sunan nefes kesici bir seyir noktası. Açık havalarda Lizbon'dan okyanusa kadar uzanan muhteşem görünüm, bu noktaya yapılan zorlu tırmanışın ödülüdür.",
        "description_en": "A breathtaking viewpoint offering 360-degree panoramic views from one of the highest points of Sintra mountains. The magnificent view extending from Lisbon to the ocean on clear days is the reward for the challenging climb to this point."
    },
    "Tapada das Necessidades": {
        "description": "Turistik rotalardan uzakta, yerel halkın yürüyüş ve bisiklet için tercih ettiği sakin bir ormanlık alan. Çam ve okaliptüs kokularıyla dolu patikalarında, şehrin kalabalığından uzaklaşarak doğayla baş başa kalabileceğiniz huzurlu bir sığınak.",
        "description_en": "A quiet wooded area away from tourist routes, preferred by locals for walking and cycling. A peaceful refuge on its paths filled with the scent of pine and eucalyptus where you can get away from the city crowds and be alone with nature."
    },
    "Quinta da Amizade": {
        "description": "Moorish Castle'ın eteklerinde, 19. yüzyıl romantik dönem mimarisinin güzel bir örneği olan tarihi malikane. Süslü kuleler, gotik pencereler ve yemyeşil bahçesiyle dikkat çeken bu yapı, Sintra'nın masalsı karakterini yansıtan gizli hazinelerden biri.",
        "description_en": "A historic manor at the foot of Moorish Castle, a beautiful example of 19th century romantic period architecture. Notable for its ornate towers, Gothic windows, and lush garden, this structure is one of the hidden treasures reflecting Sintra's fairytale character."
    },
    "Fojo dos Morcegos": {
        "description": "Sintra dağlarının kayalık arazisinde bulunan, 'yarasa çukuru' anlamına gelen derin ve dikey bir doğal mağara girişi. Macera severler ve spor tırmanıcılar için ilginç bir jeolojik oluşum olan bu nokta, çevresindeki sarp arazi nedeniyle dikkatli yaklaşım gerektiriyor.",
        "description_en": "A deep and vertical natural cave entrance in the rocky terrain of Sintra mountains, meaning 'bat pit'. An interesting geological formation for adventure lovers and sport climbers, this point requires careful approach due to the steep terrain around it."
    },
    "Moinho de Vento do Cabo da Roca": {
        "description": "Cabo da Roca burnunun yakınında, Atlantik Okyanusu manzarasına hakim konumda duran geleneksel yel değirmeni. Artık işlevsel olmasa da, harika okyanus manzarası ve nostaljik silueti ile fotoğraf çekmek için popüler bir durak noktasıdır.",
        "description_en": "A traditional windmill near Cabo da Roca cape, standing at a position dominating Atlantic Ocean views. Although no longer functional, it is a popular stop point for photography with its wonderful ocean view and nostalgic silhouette."
    },
    "Praia da Ursa Viewpoint": {
        "description": "Avrupa'nın en güzel vahşi plajlarından biri olan Praia da Ursa'ya inmeden, yukarıdan o muhteşem kayalık sahili ve devasa kaya formasyonlarını görebileceğiniz en iyi nokta. Zor inişi göze alamayanlar için bile, bu manzara noktası unutulmaz bir deneyim sunuyor.",
        "description_en": "The best point to see the magnificent rocky coast and giant rock formations of Praia da Ursa, one of Europe's most beautiful wild beaches, from above without going down. Even for those who can't risk the difficult descent, this viewpoint offers an unforgettable experience."
    },
    "Jardim da Comenda": {
        "description": "Roma dönemine ait arkeolojik kalıntıların bulunduğu, bakımlı çimenlik alanları piknik ve dinlenmeye uygun yeşil bir park. Tarihi atmosferi ve huzurlu ortamıyla, öğle yemeği molası vermek veya antik tarihi keşfetmek isteyenler için ideal bir mekan.",
        "description_en": "A green park with well-maintained lawn areas suitable for picnicking and relaxation, where archaeological remains from the Roman period are found. With its historic atmosphere and peaceful environment, an ideal venue for those wanting to take a lunch break or explore ancient history."
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

print(f"\n✅ Manually enriched {count} items (Batch 4).")

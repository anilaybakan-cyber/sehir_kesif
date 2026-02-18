import json

# Manual enrichment data (Batch 6 Final: Remaining Cascais & Estoril items - 20 items)
updates = {
    "Estoril": {
        "description": "Bir zamanlar II. Dünya Savaşı döneminde sürgündeki krallar ve casusların sığınağı olan, James Bond'a ilham veren efsanevi kumarhanesiyle ünlü prestijli tatil beldesi. Lüks otelleri, altın kumsalları ve canlı gece hayatıyla, Portekiz Rivierası'nın en göz alıcı destinasyonlarından biri.",
        "description_en": "A prestigious holiday resort once a refuge for exiled kings and spies during World War II, famous for its legendary casino that inspired James Bond. One of the most glamorous destinations of the Portuguese Riviera with its luxury hotels, golden beaches, and vibrant nightlife."
    },
    "Cabo Raso Lighthouse": {
        "description": "Cascais ile Guincho arasındaki kayalık burun üzerinde, canlı kırmızı rengiyle Atlantik manzarasına hakim olan ikonik deniz feneri. 17. yüzyıldan beri denizcilere yol gösteren bu yapı, okyanusun vahşi güzelliğini seyretmek için mükemmel bir fotoğraf noktası.",
        "description_en": "An iconic lighthouse dominating the Atlantic view with its vibrant red color on the rocky cape between Cascais and Guincho. Guiding sailors since the 17th century, this structure is a perfect photography spot to watch the wild beauty of the ocean."
    },
    "Sanctuary of Peninha Viewpoint": {
        "description": "Sintra dağlarının tepesinde, Cascais'ten Ericeira'ya kadar tüm kıyı şeridini görebileceğiniz en muhteşem panoramik seyir noktası. 16. yüzyılda inşa edilen kutsallık atfedilen şapelin yanında, sonsuz okyanus manzarasıyla ruhunuzu dinlendirecek bir yer.",
        "description_en": "The most magnificent panoramic viewpoint on top of Sintra mountains where you can see the entire coastline from Cascais to Ericeira. A place next to the 16th-century chapel attributed with sanctity that will rest your soul with endless ocean views."
    },
    "Praia de São Pedro do Estoril": {
        "description": "Tren istasyonunun hemen altında, kayalık falezlerle korunan, ailelere uygun popüler bir sahil plajı. Sakin suları, kolay erişimi, sahil kenarındaki restoranları ve cankurtaran hizmetleriyle, Estoril hattı boyunca en çok tercih edilen plajlardan biri.",
        "description_en": "A family-friendly popular beach right below the train station, protected by rocky cliffs. One of the most preferred beaches along the Estoril line with its calm waters, easy access, beachfront restaurants, and lifeguard service."
    },
    "Parque Marechal Carmona": {
        "description": "Cascais'in kalbinde, tavus kuşlarının özgürce dolaştığı, asırlık ağaçların gölgelendirdiği büyüleyici bir şehir parkı. Küçük bir göl, çocuk oyun alanları, kafe ve Condes de Castro Guimarães Müzesi'ne ev sahipliği yapan bu yeşil vaha, dinlenmek için mükemmel.",
        "description_en": "A charming city park in the heart of Cascais where peacocks roam freely, shaded by centuries-old trees. This green oasis hosting a small lake, children's playgrounds, cafes, and the Condes de Castro Guimarães Museum is perfect for relaxation."
    },
    "Santa Marta Lighthouse Museum": {
        "description": "Cascais'in simgesi haline gelmiş, mavi-beyaz çizgili sevimli deniz feneri, şimdi denizcilik tarihini anlatan küçük bir müzeye dönüştürüldü. Fenerin tepesine çıkarak körfezi ve limanı kuşbakışı görebilir, Portekiz'in denizcilik mirasını yakından keşfedebilirsiniz.",
        "description_en": "The cute blue-white striped lighthouse that has become a symbol of Cascais, now converted into a small museum telling maritime history. You can climb to the top of the lighthouse for a bird's-eye view of the bay and harbor, and explore Portugal's maritime heritage up close."
    },
    "Citadel of Cascais": {
        "description": "15. yüzyılda limanı korumak için inşa edilmiş tarihi kalenin içinde, günümüzde lüks bir otel, sanat galerileri ve restoranlar yer alıyor. Denize bakan burçlarından gün batımını izleyebilir, tarihi atmosferde modern konforun tadını çıkarabilirsiniz.",
        "description_en": "Inside the historic fortress built in the 15th century to protect the harbor, there are now a luxury hotel, art galleries, and restaurants. You can watch the sunset from its bastions overlooking the sea and enjoy modern comfort in a historic atmosphere."
    },
    "Praia dos Pescadores": {
        "description": "Ericeira'nın balıkçı geleneğini yaşatan, renkli balıkçı teknelerinin kıyıya çekildiği otantik merkezi plaj. Dalgakıranla korunan sakin suları, çocuklu aileler için güvenli yüzme olanağı sunarken, sahil kenarındaki restoranlarda taze deniz ürünlerinin tadına varabilirsiniz.",
        "description_en": "An authentic central beach in Ericeira keeping the fishing tradition alive, where colorful fishing boats are pulled ashore. Its calm waters protected by the breakwater offer safe swimming for families with children, while you can taste fresh seafood in beachfront restaurants."
    },
    "Centro de Interpretação da Natureza": {
        "description": "Sintra-Cascais Doğal Parkı'nın flora, faunası ve jeolojisi hakkında bilgi alabileceğiniz küçük ama bilgilendirici ziyaretçi merkezi. Yürüyüş rotaları, kuş gözlemi noktaları ve bölgedeki doğal yaşam hakkında haritalı rehberler sunan, park keşfine başlamadan önce ideal bir durak.",
        "description_en": "A small but informative visitor center where you can get information about the flora, fauna, and geology of Sintra-Cascais Natural Park. An ideal stop before starting park exploration, offering guides with maps about hiking routes, bird watching spots, and natural life in the region."
    },
    "Igreja de Nossa Senhora da Assunção": {
        "description": "Cascais'in ana meydanında yer alan, 16. yüzyıldan kalma şehrin en önemli kilisesi. İç mekanındaki muhteşem altın yaldızlı ahşap retablolar ve ünlü Portekizli ressam Josefa de Óbidos'un eserleri, dini sanat meraklılarını büyüleyecek.",
        "description_en": "The city's most important church from the 16th century located in Cascais' main square. The magnificent gilded wooden retables and works by famous Portuguese painter Josefa de Óbidos inside will enchant religious art enthusiasts."
    },
    "Parque Urbano de Rana": {
        "description": "Lizbon-Sintra tren hattının yanında, yerel halkın yürüyüş, koşu ve bisiklet için tercih ettiği geniş şehir parkı. Çocuk oyun alanları, spor sahaları, piknik alanları ve gölgeli patikalarıyla, hafta sonu ailece vakit geçirmek için mükemmel bir yeşil alan.",
        "description_en": "A large urban park next to the Lisbon-Sintra train line preferred by locals for walking, running, and cycling. A perfect green area for spending time with family on weekends with children's playgrounds, sports fields, picnic areas, and shaded trails."
    },
    "Jardim Visconde da Luz": {
        "description": "Cascais'in tarihi merkezinde, nostaljik atlı karıncası ve küçük çocuklara yönelik oyun alanlarıyla sevilen şirin bir bahçe. Gölgeli banklarında oturup geçen insanları izleyebilir, çocuklarınızı güvenle oynatırken bir nefes alabilirsiniz.",
        "description_en": "A cute garden in the historic center of Cascais, loved for its nostalgic carousel and playgrounds for small children. You can sit on its shaded benches watching passers-by and take a breath while your children play safely."
    },
    "Marina de Cascais": {
        "description": "Lüks yatların demirlediği, şık restoranlar ve kafelerle çevrili canlı Cascais marinası. Akşam saatlerinde deniz kenarında yürüyüş yapmak, bir bardak şarap eşliğinde gün batımını izlemek ve kozmopolit atmosferin keyfini çıkarmak için ideal bir buluşma noktası.",
        "description_en": "The lively Cascais marina where luxury yachts are moored, surrounded by stylish restaurants and cafes. An ideal meeting point for walking by the sea in the evening, watching the sunset accompanied by a glass of wine, and enjoying the cosmopolitan atmosphere."
    },
    "Praia da Rainha": {
        "description": "Bir zamanlar Kraliçe Amélia'nın özel plajı olan, yüksek kayalıkların arasında saklı küçük ve büyüleyici bir kum cenneti. Cascais merkezine sadece birkaç adım uzaklıkta olmasına rağmen, gizli konumuyla sanki başka bir dünyada gibi hissettirir.",
        "description_en": "A small and charming sand paradise hidden among high cliffs, once Queen Amélia's private beach. Despite being only a few steps from Cascais center, its hidden location makes you feel like you're in another world."
    },
    "Palácio dos Condes de Castro Guimarães": {
        "description": "Deniz kenarındaki Marechal Carmona Parkı içinde, masalsı kulesi ve gotik pencereleriyle dikkat çeken romantik dönem müze-sarayı. İç mekanında 18-19. yüzyıl mobilyaları, seramikleri ve değerli kitaplardan oluşan zengin bir koleksiyon barındırıyor.",
        "description_en": "A romantic period museum-palace in Marechal Carmona Park by the sea, notable for its fairytale tower and Gothic windows. Inside, it houses a rich collection of 18th-19th century furniture, ceramics, and valuable books."
    },
    "Casa de Santa Maria": {
        "description": "Santa Marta Deniz Feneri'nin yanında, 20. yüzyıl başlarında inşa edilmiş geleneksel Portekiz mimarisinin zarif bir örneği. Azulejo çinilerle süslü iç mekanı ve okyanusu gören bahçesiyle, Cascais'in aristokratik geçmişine göz atmak için mükemmel bir mekan.",
        "description_en": "An elegant example of traditional Portuguese architecture built in the early 20th century next to Santa Marta Lighthouse. With its interior decorated with azulejo tiles and garden overlooking the ocean, a perfect venue to glimpse Cascais' aristocratic past."
    },
    "Praia da Duquesa": {
        "description": "Cascais merkezinde, palmiye ağaçları ve tarihi Castro Guimarães sarayı manzarasıyla çerçevelenmiş şık sahil plajı. Şehrin kalabalık ana plajlarından biraz daha sakin olan bu kumsal, merkezi konumu ve zarif atmosferiyle günübirlik plaj keyfi için ideal.",
        "description_en": "A stylish beach in Cascais center framed by palm trees and views of the historic Castro Guimarães palace. Slightly calmer than the city's crowded main beaches, this beach is ideal for a day of beach fun with its central location and elegant atmosphere."
    },
    "Hipódromo Manuel Possolo": {
        "description": "Cascais'te at yarışlarının ve büyük konserlerin düzenlendiği çok amaçlı hipodrom ve park alanı. Heyecanlı yarış günlerinde tribune heyecanını yaşayabilir veya yıl boyunca düzenlenen çeşitli etkinliklere katılabilirsiniz.",
        "description_en": "A multipurpose hippodrome and park area in Cascais where horse races and major concerts are held. You can experience the grandstand excitement on exciting race days or attend various events held throughout the year."
    },
    "Forte de São Jorge de Oitavos": {
        "description": "Cascais kıyı yolunda, 17. yüzyıldan kalma orijinal bronz toplarıyla hâlâ yerlerinde duran atmosferik bir sahil kalesi. Surlarından Atlantik manzarası ve yakındaki golf sahasıyla, tarih ve doğanın buluştuğu fotoğrafik bir mekan.",
        "description_en": "An atmospheric coastal fort on the Cascais coastal road, with original bronze cannons from the 17th century still standing in their places. A photographic venue where history and nature meet with Atlantic views from its walls and a nearby golf course."
    },
    "Vila Sassetti": {
        "description": "Sintra'nın merkezinden Moorish Castle'a giden ücretsiz yürüyüş rotası üzerinde yer alan, Toskana villalarını andıran zarif 19. yüzyıl konağı. İtalyan etkilerini yansıtan mimarisi ve yemyeşil bahçeleri, turistik kalabalıklardan uzakta sakin bir keşif sunuyor.",
        "description_en": "An elegant 19th-century mansion reminiscent of Tuscan villas on the free walking route from Sintra center to Moorish Castle. Its architecture reflecting Italian influences and lush gardens offer a quiet discovery away from tourist crowds."
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

print(f"\n✅ Manually enriched {count} items (Batch 6 Final).")

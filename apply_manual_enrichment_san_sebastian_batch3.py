import json

# Manual enrichment data (San Sebastian Batch 3 FINAL: 33 items)
updates = {
    "Urdaibai Biosphere Reserve": {
        "description": "UNESCO tarafından korunan, Bask kıyısındaki en önemli sulak alan ve kuş cenneti. Flamingolar, balıkçıl kuşları ve göç eden türlerle, doğa fotoğrafçıları için cennet.",
        "description_en": "The most important wetland and bird paradise on Basque coast, protected by UNESCO. A paradise for nature photographers with flamingos, herons, and migratory species."
    },
    "Mundaka": {
        "description": "Dünyanın en iyi sol dalga (left-hand wave) sörfü için tanınan efsanevi surf spot. Profesyonel sörf yarışmalarına ev sahipliği yapan, sörfçülerin Mekke'si.",
        "description_en": "A legendary surf spot known for the world's best left-hand wave surfing. The Mecca of surfers hosting professional surf competitions."
    },
    "Santuario de Arantzazu": {
        "description": "Dağların arasında gizlenmiş, modern sanat eserleriyle dolu etkileyici Bask manastırı. Jorge Oteiza ve Eduardo Chillida'nın heykellerini barındıran, spiritüel ve sanatsal merkez.",
        "description_en": "An impressive Basque monastery hidden among mountains, full of modern artworks. A spiritual and artistic center housing sculptures by Jorge Oteiza and Eduardo Chillida."
    },
    "Butron Castle": {
        "description": "19. yüzyılda romantik tarzda yeniden inşa edilmiş, masalsı görünümlü ortaçağ kalesi. Kuleler, sivriler ve yeşillikler arasında, fotoğraf için mükemmel masal dekoru.",
        "description_en": "A fairy-tale-looking medieval castle rebuilt in romantic style in the 19th century. Perfect fairy-tale setting for photos among towers, spires, and greenery."
    },
    "Vizcaya Bridge (Puente Colgante)": {
        "description": "Dünyanın en eski taşıma köprüsü, UNESCO Dünya Mirası listesinde. 1893'ten beri çalışan bu mühendislik harikası, gondolla nehri geçme veya köprüde yürüyüş deneyimi sunuyor.",
        "description_en": "The world's oldest transporter bridge, on UNESCO World Heritage list. This engineering marvel operating since 1893 offers crossing the river by gondola or walking on the bridge."
    },
    "Olite Royal Palace": {
        "description": "Navarra'nın eski başkentinde, ortaçağ İspanyasının en görkemli saraylarından biri. Kuleler, bahçeler ve gotik mimarisiyle, Game of Thrones'vari atmosfer.",
        "description_en": "One of the most splendid palaces of medieval Spain in Navarra's former capital. Game of Thrones-like atmosphere with towers, gardens, and Gothic architecture."
    },
    "Urederra Nature Reserve": {
        "description": "Turkuaz rengiyle büyüleyen doğal havuzları ve şelaleleriyle Bask doğasının gizli cenneti. Yürüyüş parkuru boyunca masal ormanı ve kristal berraklığında sular.",
        "description_en": "The hidden paradise of Basque nature with natural pools and waterfalls enchanting with turquoise color. A fairy-tale forest and crystal-clear waters along the hiking trail."
    },
    "Bardenas Reales": {
        "description": "Navarra'da yarı-çöl manzarasıyla Mars'ı andıran UNESCO Biyosfer Rezervi. Oyulmuş kaya oluşumları, kurak vadiler ve Game of Thrones çekim mekanlarıyla, sıra dışı jeoloji.",
        "description_en": "A UNESCO Biosphere Reserve in Navarra resembling Mars with semi-desert landscape. Unusual geology with carved rock formations, arid valleys, and Game of Thrones filming locations."
    },
    "Salinas de Añana": {
        "description": "7000 yıllık tarihe sahip, hâlâ aktif olan dünyanın en eski tuz üretim tesislerinden biri. Teraslanmış tuz havuzları, rehberli turlar ve gurme tuz tadımıyla benzersiz deneyim.",
        "description_en": "One of the world's oldest still-active salt production facilities with 7000 years of history. A unique experience with terraced salt pans, guided tours, and gourmet salt tasting."
    },
    "Elantxobe": {
        "description": "Dik yamaçlara tutunmuş, sadece tek bir arabaya yol veren dar sokaklarıyla pitoresk balıkçı köyü. Renkli evleri, balıkçı limanı ve otantik Bask atmosferiyle keşfedilmeyi bekliyor.",
        "description_en": "A picturesque fishing village clinging to steep slopes with narrow streets allowing only one car. Waiting to be discovered with colorful houses, fishing harbor, and authentic Basque atmosphere."
    },
    "Aia": {
        "description": "Kırsal Bask yaşamını deneyimleyebileceğiniz, yeşil tepeler ve çiftliklerle çevrili sakin köy. Yöresel peynir üreticileri, sidreria'lar ve doğa yürüyüşleri için başlangıç noktası.",
        "description_en": "A peaceful village surrounded by green hills and farms where you can experience rural Basque life. Starting point for local cheese producers, cider houses, and nature walks."
    },
    "Leitza": {
        "description": "Bask dağlarında kaybolmuş, geleneksel yaşamın devam ettiği otantik köy. Euskara'nın (Bask dili) canlı tutulduğu, folklorik etkinlikler ve köy festivalleriyle kültürel miras.",
        "description_en": "An authentic village lost in Basque mountains where traditional life continues. Cultural heritage where Euskara (Basque language) is kept alive, with folkloric events and village festivals."
    },
    "Sare": {
        "description": "Fransa-İspanya sınırında, 'Fransa'nın en güzel köyleri' listesinde yer alan Bask köyü. Tarihi evleri, antik mağaraları ve geleneksel el sanatlarıyla günlük gezi için ideal.",
        "description_en": "A Basque village on France-Spain border, listed among 'Most Beautiful Villages of France'. Ideal for day trip with historic houses, ancient caves, and traditional handicrafts."
    },
    "Old Town Coffee": {
        "description": "Eski Şehir'de specialty coffee kültürünü yaşatan, kaliteli kahve ve rahat atmosferiyle dikkat çeken kafe. Yerel kavurucu ve özenli kahve hazırlama teknikleri.",
        "description_en": "A cafe in Old Town keeping specialty coffee culture alive, notable for quality coffee and comfortable atmosphere. Local roaster and careful coffee preparation techniques."
    },
    "Botanika": {
        "description": "Bitkisel bazlı menüsü ve sürdürülebilir yaklaşımıyla öne çıkan vegan/vejetaryen restoran. Bask mutfağının bitkisel yorumu, organik malzemeler ve yaratıcı tabaklar.",
        "description_en": "A vegan/vegetarian restaurant standing out with plant-based menu and sustainable approach. Plant-based interpretation of Basque cuisine, organic ingredients, and creative dishes."
    },
    "Gerald's Bar": {
        "description": "Avustralyalı şefinSan Sebastián'a taşıdığı, kaliteli şaraplar ve paylaşmalı tabaklarıyla ünlü bar-restoran. Rahat atmosfer, seçkin şarap listesi ve fusion lezzetler.",
        "description_en": "A bar-restaurant brought to San Sebastián by Australian chef, famous for quality wines and sharing plates. Relaxed atmosphere, select wine list, and fusion flavors."
    },
    "Txuleta": {
        "description": "Dev Bask bifteği 'Txuletón'un en iyi adreslerinden biri, et severler için cennet. Yüksek kalite et, basit pişirme tekniği ve büyük porsiyonlarla hardcore gurme deneyimi.",
        "description_en": "One of the best addresses for giant Basque steak 'Txuletón', a paradise for meat lovers. Hardcore gourmet experience with high-quality meat, simple cooking technique, and large portions."
    },
    "KATA4": {
        "description": "Modern Bask mutfağı ve yaratıcı kokteyllerle öne çıkan çağdaş restoran-bar. Akşam yemeği ve sonrasında içki için tek adreste sofistike deneyim.",
        "description_en": "A contemporary restaurant-bar standing out with modern Basque cuisine and creative cocktails. Sophisticated experience at one address for dinner and drinks afterward."
    },
    "Maiatza": {
        "description": "Geleneksel Bask tavernası konseptini sürdüren, samimi atmosferi ve klasik lezzetleriyle sevilen mekan. Yerel halkın tercih ettiği, otantik pintxos ve şarap.",
        "description_en": "A beloved venue continuing traditional Basque tavern concept with intimate atmosphere and classic flavors. Authentic pintxos and wine preferred by locals."
    },
    "SSua Arde Donostia": {
        "description": "Modern İspanyol mutfağını yaratıcı sunumlarla yorumlayan, genç şeflerin yönettiği restoran. Taze etkiler, cesur kombinasyonlar ve yenilikçi pişirme teknikleri.",
        "description_en": "A restaurant run by young chefs interpreting modern Spanish cuisine with creative presentations. Fresh influences, bold combinations, and innovative cooking techniques."
    },
    "Garrarte": {
        "description": "Bask el sanatlarını, seramikleri ve yerel sanatçıların eserlerini sergileyen ve satan galeri-dükkan. Orijinal hediyelikler ve Bask kültürüne ait özel parçalar.",
        "description_en": "A gallery-shop exhibiting and selling Basque handicrafts, ceramics, and works of local artists. Original souvenirs and special pieces of Basque culture."
    },
    "Libreria Donosti": {
        "description": "Bask edebiyatı, yerel tarih ve İspanyolca kitapların geniş koleksiyonunu sunan bağımsız kitapçı. Kültürel etkinlikler, imza günleri ve kitap severler için huzur köşesi.",
        "description_en": "An independent bookstore offering wide collection of Basque literature, local history, and Spanish books. Cultural events, book signings, and a peaceful corner for book lovers."
    },
    "Alboka Artesania": {
        "description": "Geleneksel Bask müzik aletleri, el yapımı deri ürünler ve folklorik hediyeliklerin satıldığı dükkan. Alboka (Bask nefesli çalgısı) ve txalaparta (tahta vurmalı) gibi özel parçalar.",
        "description_en": "A shop selling traditional Basque musical instruments, handmade leather products, and folkloric souvenirs. Special pieces like alboka (Basque wind instrument) and txalaparta (wooden percussion)."
    },
    "Casa Ponsol": {
        "description": "1838'den beri geleneksel Bask bereleri (txapela) ve başlıkları üreten tarihi dükkan. El yapımı, yüksek kaliteli yün bereleriyle otantik Bask aksesuarı.",
        "description_en": "A historic shop producing traditional Basque berets (txapela) and headwear since 1838. Authentic Basque accessory with handmade, high-quality wool berets."
    },
    "The End": {
        "description": "Surf kültürü ve sokak modasının buluştuğu vintage ve ikinci el giyim dükkanı. Benzersiz parçalar, yerel tasarımcı ürünleri ve sürdürülebilir moda seçenekleri.",
        "description_en": "A vintage and secondhand clothing shop where surf culture meets street fashion. Unique pieces, local designer products, and sustainable fashion options."
    },
    "Pukas Surf Shop": {
        "description": "Bask Bölgesi'nin en köklü sörf markası ve mağazası, her şey sörf için. Sörf tahtaları, wetsuit'ler, aksesuarlar ve sörf kültürü hakkında uzman tavsiyesi.",
        "description_en": "Basque Country's most established surf brand and store, everything for surfing. Surfboards, wetsuits, accessories, and expert advice about surf culture."
    },
    "Loreak Mendian": {
        "description": "San Sebastián çıkışlı, sokak modası ve sörf kültürünü harmanlayan yerel moda markası. Özgün tasarımlar, kaliteli malzemeler ve Bask kimliğinden ilham alan koleksiyonlar.",
        "description_en": "A local fashion brand from San Sebastián, blending street fashion and surf culture. Original designs, quality materials, and collections inspired by Basque identity."
    },
    "Aralar Mendi Elkartea": {
        "description": "Bask dağlarında rehberli yürüyüşler ve doğa aktiviteleri düzenleyen yerel dağcılık kulübü. Trekking, tırmanış ve açık hava maceraları için güvenilir organizatör.",
        "description_en": "A local mountaineering club organizing guided hikes and nature activities in Basque mountains. Reliable organizer for trekking, climbing, and outdoor adventures."
    },
    "Convent Garden": {
        "description": "Eski Şehir'in kalbinde gizli bir avlu bahçe, sakin atmosferiyle mola için ideal. Tarihi manastır yapısı, gölgelik banklar ve şehrin gürültüsünden kaçış.",
        "description_en": "A hidden courtyard garden in the heart of Old Town, ideal for a break with its calm atmosphere. Historic convent structure, shaded benches, and an escape from city noise."
    },
    "Egia Cultural Center": {
        "description": "Alternatif sanat, müzik ve kültürel etkinliklere ev sahipliği yapan bağımsız kültür merkezi. Sergiler, konserler ve atölyelerle, şehrin yaratıcı nabzı.",
        "description_en": "An independent cultural center hosting alternative art, music, and cultural events. The creative pulse of the city with exhibitions, concerts, and workshops."
    },
    "Hontza Museoa": {
        "description": "Baykuşlara ve gece kuşlarına adanmış küçük ama büyüleyici doğa müzesi. Tüylü ahbaplarla tanışma, ekolojik bilgi ve doğa koruma farkındalığı.",
        "description_en": "A small but fascinating nature museum dedicated to owls and nocturnal birds. Meeting feathered friends, ecological knowledge, and nature conservation awareness."
    },
    "Igeldo Amusement Park": {
        "description": "1912'den beri hizmet veren nostaljik lunapark, Monte Igueldo'nun tepesinde. Eski tarz dönme dolaplar, karanlık tren ve okyanus manzarasıyla, tüm yaşlar için eğlence.",
        "description_en": "A nostalgic amusement park serving since 1912, on top of Monte Igueldo. Fun for all ages with old-style ferris wheels, ghost train, and ocean views."
    },
    "Funicular de Igueldo": {
        "description": "1912'den beri işleyen tarihi füniküler, Monte Igueldo'nun tepesine nostaljik yolculuk. La Concha koyunu kuşbakışı gören muhteşem manzaraya açılan kapı.",
        "description_en": "A historic funicular operating since 1912, a nostalgic journey to the top of Monte Igueldo. A gateway to magnificent views overlooking La Concha bay from above."
    },
    "Motorboat to Santa Clara": {
        "description": "La Concha plajından Santa Clara adasına kısa tekne gezisi. Yaz aylarında çalışan motor, adada yüzme, güneşlenme ve piknik için kaçış fırsatı.",
        "description_en": "A short boat trip from La Concha beach to Santa Clara island. Motorboat running in summer months, an escape opportunity for swimming, sunbathing, and picnicking on the island."
    }
}

filepath = 'assets/cities/san_sebastian.json'
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

print(f"\n✅ Manually enriched {count} items (San Sebastian Batch 3 FINAL).")

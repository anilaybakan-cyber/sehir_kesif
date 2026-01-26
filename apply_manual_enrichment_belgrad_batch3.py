import json

# Manual enrichment data (Belgrad Batch 3 FINAL: 30 items)
updates = {
    "Terminal GastroBar": {
        "description": "Modern gastronomi konseptiyle çalışan, yaratıcı kokteyller ve paylaşmalı tabaklar sunan trendy bar-restoran. DJ geceleri, şık kalabalık ve çağdaş Belgrad yaşamı.",
        "description_en": "A trendy bar-restaurant working with modern gastronomy concept, serving creative cocktails and sharing plates. DJ nights, stylish crowd and contemporary Belgrade life."
    },
    "Ceger": {
        "description": "Sırbistan'ın en iyi craft bira barlarından biri, yerel ve uluslararası bira seçkisiyle. Rahat ortam, bira bilgisi ve topluluk atmosferi.",
        "description_en": "One of Serbia's best craft beer bars with local and international beer selection. Comfortable setting, beer knowledge and community atmosphere."
    },
    "Villa Maska": {
        "description": "Art Deco villada konumlanan lüks kokteyl barı ve restoran, zengin dekorasyon ve premium hizmet. Elit gece hayatı, özel etkinlikler ve sofistike atmosfer.",
        "description_en": "A luxury cocktail bar and restaurant located in Art Deco villa, rich decoration and premium service. Elite nightlife, special events and sophisticated atmosphere."
    },
    "Monk's Bar": {
        "description": "Manastır temalı dekorasyon ve gizemli atmosferiyle dikkat çeken kokteyl barı. Dimness, mumlar ve sıra dışı tasarımla münzevi bir gece deneyimi.",
        "description_en": "A cocktail bar notable for monastery-themed decoration and mysterious atmosphere. A reclusive night experience with dimness, candles and unusual design."
    },
    "Tezga Bar": {
        "description": "Rahat ve samimi atmosferiyle yerel halkın favorisi, arkadaş canlısı bar. Uygun fiyatlı içecekler, canlı sohbet ve tipik Belgrad gece hayatı.",
        "description_en": "A local favorite with comfortable and intimate atmosphere, friendly bar. Affordable drinks, lively conversation and typical Belgrade nightlife."
    },
    "Kafana Znak Pitanja": {
        "description": "1823'ten beri hizmet veren, Belgrad'ın en eski kafanası. Geleneksel Sırp yemekleri, canlı müzik ve yüzyılların tanığı tarihi atmosfer.",
        "description_en": "Belgrade's oldest kafana serving since 1823. Traditional Serbian dishes, live music and historic atmosphere witness to centuries."
    },
    "Endorfin": {
        "description": "Koşu, fitness ve sağlıklı yaşam tutkunlarının buluştuğu spor kafe konsepti. Protein smoothie'ler, sağlıklı atıştırmalıklar ve aktif yaşam topluluğu.",
        "description_en": "A sports cafe concept where running, fitness and healthy lifestyle enthusiasts meet. Protein smoothies, healthy snacks and active lifestyle community."
    },
    "D Bar": {
        "description": "Dorćol mahallesinde konumlanan, DJ setleri ve dans müziğiyle gece hayatının merkezi. Enerjik atmosfer, genç kalabalık ve parti ruhu.",
        "description_en": "Center of nightlife with DJ sets and dance music located in Dorćol neighborhood. Energetic atmosphere, young crowd and party spirit."
    },
    "Museum of Chocolate": {
        "description": "Çikolata yapımı, tarihi ve tadımlarını sunan interaktif müze-atölye. Çocuklar ve aileler için eğlenceli aktivite, kendi çikolatanızı yapma fırsatı.",
        "description_en": "An interactive museum-workshop offering chocolate making, history and tastings. Fun activity for children and families, opportunity to make your own chocolate."
    },
    "Selfie Museum": {
        "description": "Renkli arka planlar, optik illüzyonlar ve yaratıcı fotoğraf köşeleri sunan interaktif mekan. Instagram için ideal, eğlenceli anlar ve samimi paylaşımlar.",
        "description_en": "An interactive venue offering colorful backgrounds, optical illusions and creative photo corners. Ideal for Instagram, fun moments and genuine shares."
    },
    "Illusions Museum": {
        "description": "Göz yanılsamaları, optik hileler ve bilim eğlencesini birleştiren interaktif müze. Tüm yaşlar için şaşırtıcı deneyimler ve zihin bükücü sergiler.",
        "description_en": "An interactive museum combining optical illusions, tricks and science fun. Surprising experiences and mind-bending exhibitions for all ages."
    },
    "Drugstore": {
        "description": "Eski mezbahada konumlanan, elektronik müzik ve underground partilerin merkezi gece kulübü. Belgrad'ın tekno sahnesinin kalbi, uluslararası DJ'ler.",
        "description_en": "A nightclub located in old slaughterhouse, center of electronic music and underground parties. Heart of Belgrade's techno scene, international DJs."
    },
    "Ben Akiba": {
        "description": "Alternatif gece hayatı ve kültürel etkinliklere ev sahipliği yapan, canlı ve yaratıcı mekan. Konserler, sergiler ve bohemian ruh.",
        "description_en": "A lively and creative venue hosting alternative nightlife and cultural events. Concerts, exhibitions and bohemian spirit."
    },
    "Strogi Centar": {
        "description": "Şehir merkezinde konumlanan, kokteyller ve DJ müziğiyle ünlü şık bar. Zarif dekorasyon, gece geç saatlere kadar eğlence ve sosyal sahne.",
        "description_en": "A stylish bar located in city center, famous for cocktails and DJ music. Elegant decoration, entertainment until late at night and social scene."
    },
    "Ljutić": {
        "description": "Geleneksel Sırp mutfağının modern yorumlarını sunan, zamane şeflerin yönettiği restoran. Yerel malzemeler, yenilikçi teknikler ve Belgrad'ın yükselen gastronomisi.",
        "description_en": "A restaurant run by contemporary chefs serving modern interpretations of traditional Serbian cuisine. Local ingredients, innovative techniques and Belgrade's rising gastronomy."
    },
    "Tri Golubice": {
        "description": "Slaviya Meydanı yakınında, uzun yıllardır hizmet veren geleneksel Sırp restoranı. Ev yemekleri, uygun fiyat ve yerel halkın favori sofraları.",
        "description_en": "A traditional Serbian restaurant near Slavija Square, serving for many years. Home cooking, affordable prices and local favorites' tables."
    },
    "Zlatni Bokal": {
        "description": "Skadarlija'nın ikonik kafanalarından biri, canlı müzik ve geleneksel Balkan ziyafeti. Nostaljik akşamlar, türkü geceleri ve otantik atmosfer.",
        "description_en": "One of Skadarlija's iconic kafanas, live music and traditional Balkan feast. Nostalgic evenings, folk music nights and authentic atmosphere."
    },
    "Red Bar": {
        "description": "Kırmızı temalı dekorasyon ve canlı atmosferiyle dikkat çeken popüler kokteyl barı. Çeşitli içki menüsü, DJ müziği ve sosyalleşme için ideal.",
        "description_en": "A popular cocktail bar notable for red-themed decoration and lively atmosphere. Varied drink menu, DJ music and ideal for socializing."
    },
    "Muha Bar": {
        "description": "Küçük ama samimi atmosferiyle sevilen, yerel halkın buluşma noktası bar. Rahat ortam, güler yüzlü servis ve tipik Belgrad barı deneyimi.",
        "description_en": "A bar loved for small but intimate atmosphere, local meeting point. Comfortable setting, friendly service and typical Belgrade bar experience."
    },
    "Laboratorija Kafe": {
        "description": "Bilim ve kahve kültürünü birleştiren, özgün konseptiyle dikkat çeken kafe. Deney temalı dekorasyon, specialty coffee ve yaratıcı atmosfer.",
        "description_en": "A cafe notable for unique concept combining science and coffee culture. Experiment-themed decoration, specialty coffee and creative atmosphere."
    },
    "Burger House": {
        "description": "El yapımı hamburgerler ve American diner konseptiyle çalışan popüler burger restoranı. Büyük porsiyonlar, çeşitli seçenekler ve rahat ortam.",
        "description_en": "A popular burger restaurant working with handmade burgers and American diner concept. Large portions, various options and comfortable setting."
    },
    "Zaplet": {
        "description": "Genç şeflerin yaratıcı tabaklarını sunduğu, modern Sırp mutfağı restoranı. Dikkatli sunum, yerel malzemeler ve fine-dining yaklaşımı.",
        "description_en": "A modern Serbian cuisine restaurant serving creative dishes by young chefs. Careful presentation, local ingredients and fine-dining approach."
    },
    "Balkon": {
        "description": "Şehir manzaralı teras, kokteyller ve hafif yemekler sunan yüksekten konum. Gün batımı keyfi, romantik akşamlar ve fotoğraf için ideal.",
        "description_en": "A high location with city view terrace serving cocktails and light meals. Sunset enjoyment, romantic evenings and ideal for photography."
    },
    "Klub Književnika": {
        "description": "Yazarlar Kulübü, Sırp edebiyat çevrelerinin ve entelektüellerin buluştuğu tarihi mekan. Klasik dekorasyon, kitaplı köşeler ve kültürel sohbetler.",
        "description_en": "Writers' Club, a historic venue where Serbian literary circles and intellectuals meet. Classic decoration, book corners and cultural conversations."
    },
    "Senza": {
        "description": "Modern İtalyan mutfağını Belgrad'a taşıyan, pizza ve makarna çeşitleriyle ünlü restoran. Şık tasarım, kaliteli malzemeler ve Akdeniz lezzetleri.",
        "description_en": "A restaurant bringing modern Italian cuisine to Belgrade, famous for pizza and pasta varieties. Stylish design, quality ingredients and Mediterranean flavors."
    },
    "Bloom": {
        "description": "Çiçek konseptli dekorasyon, brunches ve afternoon tea sunan şık kafe. Instagram'a uygun sunum, özel günler ve feminen atmosfer.",
        "description_en": "A stylish cafe with flower concept decoration serving brunches and afternoon tea. Instagram-worthy presentation, special occasions and feminine atmosphere."
    },
    "Epigenia": {
        "description": "Taze malzemeler ve Akdeniz ilhamıyla hazırlanan yemeklerin sunulduğu sağlık odaklı restoran. Vejetaryen seçenekler, hafif tarifler ve wellness yaklaşımı.",
        "description_en": "A health-focused restaurant serving dishes prepared with fresh ingredients and Mediterranean inspiration. Vegetarian options, light recipes and wellness approach."
    },
    "Zla Zla": {
        "description": "Underground müzik ve alternatif kültür sahnesinin buluşma noktası, yaratıcı gece mekanı. Canlı konserler, DJ setleri ve indie atmosfer.",
        "description_en": "A creative night venue, meeting point of underground music and alternative culture scene. Live concerts, DJ sets and indie atmosphere."
    },
    "Dokolica": {
        "description": "Gevşek atmosfer ve 'hiçbir şey yapmama' konseptiyle dinlenmeye davet eden kafe. Kitaplar, masa oyunları ve sakin sohbetler için ideal.",
        "description_en": "A cafe inviting to relax with laid-back atmosphere and 'doing nothing' concept. Ideal for books, board games and calm conversations."
    },
    "Restoran 27": {
        "description": "Modern Balkan mutfağını yaratıcı bir şekilde sunan, genç şeflerin imza restoranı. Mevsimlik menü, özenli sunum ve fine-dining deneyimi.",
        "description_en": "A signature restaurant by young chefs creatively presenting modern Balkan cuisine. Seasonal menu, careful presentation and fine-dining experience."
    }
}

filepath = 'assets/cities/belgrad.json'
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

print(f"\n✅ Manually enriched {count} items (Belgrad Batch 3 FINAL).")

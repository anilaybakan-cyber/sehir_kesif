#!/usr/bin/env python3
import json

updates = {
    "Ano Poli": {
        "description": "Selanik'in 'Yukarı Şehir' bölgesi olan Ano Poli, Osmanlı dönemi evleri ve dar labirent sokaklarıyla kentin en otantik ve büyüleyici semtidir. Şehrin modern kaosundan uzaklaşarak tarihin içinde sessiz bir yürüyüş yapmak ve surların üzerinden körfez manzarasını seyretmek için mükemmel bir kaçış noktasıdır.",
        "description_en": "Ano Poli, the 'Upper Town' of Thessaloniki, is the city's most authentic and charming neighborhood with its Ottoman-era houses and narrow labyrinthine streets. It's a perfect escape point to take a quiet walk through history away from the modern chaos of the city and to watch the bay view from the walls."
    },
    "Rotonda": {
        "description": "Antik Çağ'dan günümüze uzanan görkemli yapısıyla Rotonda, hem bir tapınak hem bir kilise hem de bir cami olarak tarihin farklı katmanlarını bünyesinde barındırır. Olağanüstü kubbe yapısı ve Bizans dönemine ait nadide mozaikleriyle, Selanik'in çok kültürlü mirasının en çarpıcı anıtlarından biridir.",
        "description_en": "With its magnificent structure stretching from Antiquity to the present, the Rotunda embodies different layers of history as a temple, a church, and a mosque. With its extraordinary dome structure and rare Byzantine-era mosaics, it is one of the most striking monuments of Thessaloniki's multicultural heritage."
    },
    "Holy Church of Saint Demetrius": {
        "description": "Kentin koruyucu azizine adanan bu devasa bazilika, Selanik'in en önemli dini ve tarihi merkezidir. Erken Hıristiyanlık mimarisinin görkemli bir örneği olan kilise, mistik yer altı kriptası ve paha biçilemez duvar süslemeleriyle ziyaretçilerini bin yıllık bir inanç yolculuğuna çıkarır.",
        "description_en": "Dedicated to the city's patron saint, this massive basilica is the most important religious and historical center of Thessaloniki. A magnificent example of early Christian architecture, the church takes visitors on a thousand-year spiritual journey with its mystical underground crypt and priceless wall decorations."
    },
    "Ladadika": {
        "description": "Eskiden yağ depolarının bulunduğu Ladadika bölgesi, bugün Selanik'in en canlı ve renkli gastronomi-eğlence merkezidir. Restore edilmiş tarihi binaların arasında yer alan şık tavernaları, barları ve gece boyu süren enerjisiyle kentin sosyal yaşamının nabzının attığı yerdir.",
        "description_en": "Once an area of oil warehouses, Ladadika is today Thessaloniki's most vibrant and colorful gastronomy-entertainment hub. With its chic tavernas and bars located among restored historical buildings and an energy that lasts all night, it's where the pulse of the city's social life beats."
    },
    "Heptapyrgion of Thessaloniki": {
        "description": "Kentin Akropolis bölgesinde yükselen bu görkemli kale kompleksi, hem Bizans döneminin savunma ihtişamını hem de yakın geçmişin derin hikayelerini barındırır. Surların üzerinden körfeze düşen turuncu güneş ışıklarını izlemek, Selanik'in en dokunaklı ve unutulmaz anılarından biri olacaktır.",
        "description_en": "Rising in the Acropolis area of the city, this magnificent fortress complex embodies both the defensive grandeur of the Byzantine period and the deep stories of the recent past. Watching the orange sunset over the bay from the walls will be one of the most touching and unforgettable memories of Thessaloniki."
    },
    "Kapani Market": {
        "description": "Yüzyıllardır kentin en eski ve en hareketli pazarı olan Kapani, baharat kokuları, taze ürünler ve kalabalığın neşeli gürültüsüyle gerçek bir yerel deneyim sunar. Geleneksel ile modernin iç içe geçtiği bu pazar yerinde, Selanik'in gündelik yaşam ritmini en saf haliyle hissedebilirsiniz.",
        "description_en": "The oldest and most bustling market of the city for centuries, Kapani offers a true local experience with spice scents, fresh products, and the cheerful noise of the crowd. In this marketplace where tradition and modernity intertwine, you can feel Thessaloniki's daily life rhythm in its purest form."
    },
    "Latomos Monastery - Holy Church of Hosios David": {
        "description": "Ano Poli'nin gizli bir köşesinde saklanan bu küçük ama büyüleyici manastır, 5. yüzyıldan kalan nadide bir İsa mozaiğine ev sahipliği yapar. Sakin avlusu ve körfez manzarasıyla, Selanik'in en huzurlu ve mistik duraklarından biri olarak kabul edilen bir inanç noktasıdır.",
        "description_en": "Hidden in a secret corner of Ano Poli, this small but charming monastery houses a rare 5th-century mosaic of Christ. With its quiet courtyard and bay views, it's a place of faith considered one of Thessaloniki's most peaceful and mystical stops."
    },
    "Pasha’s Gardens": {
        "description": "Tarihi kulelerin hemen yanında gizemli bir vaha gibi uzanan Paşa Bahçeleri, Gaudí tarzını andıran ilginç taş mimarisi ve sessizliğiyle bilinir. Hem yerel halkın dinlenme noktası hem de tarih ve doğanın iç içe geçtiği fotojenik bir kaçış alanıdır.",
        "description_en": "Stretching like a mysterious oasis right next to historical towers, Pasha's Gardens is known for its interesting stone architecture reminiscent of the Gaudí style and its silence. It's both a rest point for locals and a photogenic escape area where history and nature intertwine."
    },
    "Arch of Galerius": {
        "description": "Kentin en meşhur antik anıtlarından biri olan Galerius Kemeri, Roma İmparatorluğu'nun zaferlerini simgeleyen detaylı taş oymalarıyla her yıl binlerce ziyaretçiyi ağırlar. Modern caddelerin tam ortasında yükselen bu tarihi dev, kentin zengin geçmişi ile bugünü arasındaki sarsılmaz köprünün bir parçasıdır.",
        "description_en": "One of the city's most famous ancient monuments, the Arch of Galerius welcomes thousands of visitors every year with its detailed stone carvings symbolizing the victories of the Roman Empire. Rising right in the middle of modern streets, this historical giant is a part of the unshakeable bridge between the city's rich past and today."
    },
    "MABÉL Bar Club Thessaloniki": {
        "description": "Selanik gece hayatına modern ve iddialı bir dokunuş katan MABÉL, şık tasarımı ve kaliteli ses sistemleriyle biliniyor. Hafta sonları kentin genç ve dinamik kitlesini ağırlayan mekan, yaratıcı kokteylleri ve etkileyici DJ performanslarıyla unutulmaz partilere ev sahipliği yapar.",
        "description_en": "Adding a modern and ambitious touch to Thessaloniki nightlife, MABÉL is known for its chic design and quality sound systems. Hosting the city's young and dynamic crowd on weekends, the venue hosts unforgettable parties with creative cocktails and impressive DJ performances."
    },
    "Soulshakers bar services": {
        "description": "Selanik'in en yaratıcı kokteyl duraklarından biri olan Soulshakers, miksoloji sanatını sokağın enerjisiyle birleştiriyor. Geniş içki mönüsü ve samimi atmosferiyle, kentin hareketli akşamlarına şık ve lezzetli bir başlangıç yapmak isteyenler için mükemmel bir buluşma noktasıdır.",
        "description_en": "One of Thessaloniki's most creative cocktail stops, Soulshakers combines the art of mixology with street energy. With its wide drink menu and intimate atmosphere, it is a perfect meeting point for those wanting a chic and flavorful start to the city's lively evenings."
    },
    "aggeliki-workshop.gr": {
        "description": "Geleneksel el sanatlarını modern tasarımlarla buluşturan bu butik atölye, Selanik yerel zanaatkarlığının en şık örneklerini sunuyor. El yapımı takılardan özgün ev aksesuarlarına kadar adanın kültürel izlerini taşıyan ürünleriyle, kendine has ve anlamlı bir hatıra arayanların uğrak yeridir.",
        "description_en": "This boutique workshop, which brings together traditional handicrafts with modern designs, offers the most elegant examples of Thessaloniki's local artisanship. From handmade jewelry to original home accessories, it's a frequent spot for those seeking a unique and meaningful souvenir reflecting cultural traces."
    },
    "Μούσες Εν Χορώ": {
        "description": "Selanik'in en popüler canlı müzik ve eğlence merkezlerinden biri olan bu mekan, geleneksel Yunan ezgilerini modern bir şov anlayışıyla sunuyor. Kaliteli servis ve neşeli ambiyansıyla, kentin ünlü buzuki gecelerini deneyimlemek ve sabahın ilk ışıklarına kadar eğlenmek için ideal bir adrestir.",
        "description_en": "One of Thessaloniki's most popular live music and entertainment centers, this venue presents traditional Greek melodies with a modern show concept. With quality service and a cheerful ambiance, it's an ideal address to experience the city's famous bouzouki nights and have fun until the first light of morning."
    },
    "Παρασκήνιο live": {
        "description": "Kentin ruhunu en iyi yansıtan canlı müzik duraklarından biri olan Parascnio, yerel sanatçıların performansları ve samimi taverna havasıyla bilinir. Dostlarınızla Ege mezeleri eşliğinde şarkılara eşlik etmek ve kentin gerçek gece kültürünü solumak için harika bir tercihtir.",
        "description_en": "One of the live music stops that best reflects the city's spirit, Parascnio is known for local artists' performances and a sincere taverna atmosphere. It's a great choice to sing along with friends accompanied by Aegean mezes and to breathe the city's real nocturnal culture."
    },
    "KAIMASIDIS FURNITURE THESSALONIKI": {
        "description": "Selanik'in tasarım dünyasında köklü bir geçmişe sahip olan bu galeri, mobilyayı bir sanat eserine dönüştüren özel koleksiyonlarıyla tanınıyor. Estetik ve konforun buluştuğu bu prestijli adres, kentin modern yaşam tarzını ve kaliteli işçiliğini yansıtan en şık mağazalardan biridir.",
        "description_en": "With a deep-rooted history in Thessaloniki's design world, this gallery is known for special collections that turn furniture into art. This prestigious address where aesthetics and comfort meet is one of the chicest stores reflecting the city's modern lifestyle and quality craftsmanship."
    },
    "Mousiko Sergiani - Live Music": {
        "description": "Geleneksel Yunan halk müziğinin en seçkin örneklerini sunan Mousiko Sergiani, samimi atmosferi ve kaliteli sahne performanslarıyla bilinir. Şehrin merkezinde tarihten gelen tınıları dinleyerek kentin otantik mirasını keşfetmek ve neşeli bir gece geçirmek için mükemmel bir duraktır.",
        "description_en": "Presenting the most distinguished examples of traditional Greek folk music, Mousiko Sergiani is known for its intimate atmosphere and quality stage performances. In the city center, it is a perfect stop to discover the city's authentic heritage and spend a cheerful night listening to tunes from history."
    },
    "VOG CLUB Thessaloniki": {
        "description": "Selanik gece hayatının en iddialı ve popüler kulüplerinden olan VOG, dünya standartlarındaki sahne şovları ve etkileyici atmosferiyle dikkat çekiyor. Işık gösterileri ve enerjik parçalarıyla, kentin kozmopolit gençliğini sabaha kadar dans ettiren en büyük eğlence sahnelerinden biridir.",
        "description_en": "One of the most ambitious and popular clubs of Thessaloniki's nightlife, VOG attracts attention with world-class stage shows and an impressive atmosphere. With its light shows and energetic tracks, it's one of the largest entertainment stages that keeps the city's cosmopolitan youth dancing until morning."
    },
    "Έπιπλα B Home": {
        "description": "Modern yaşam alanları tasarlayan B Home, şık minimalizm ve yüksek kaliteli ürünleriyle Selanik'in dekorasyon dünyasında kendine özgü bir yere sahiptir. Hem estetik hem de fonksiyonelliği bir araya getiren özgün tasarımlarıyla, kentin modern ev kültürüne yön veren yenilikçi bir adrestir.",
        "description_en": "Designing modern living spaces, B Home has a unique place in Thessaloniki's decoration world with its chic minimalism and high-quality products. With its original designs combining aesthetics and functionality, it is an innovative address shaping the city's modern home culture."
    },
    "The jews rainbow pub": {
        "description": "Ladadika'nın en eski binalarından birinde yer alan bu karakteristik pub, geniş bira mönüsü ve nostaljik iç mekanıyla kentin popüler duraklarındandır. Hafif rock ve blues tınıları eşliğinde geçmişin izlerini sürebileceğiniz, samimi ve kentin tarihi ruhunu yansıtan bir buluşma noktasıdır.",
        "description_en": "Located in one of Ladadika's oldest buildings, this characteristic pub is a popular city stop with its wide beer menu and nostalgic interior. It is a meeting point where you can trace the past accompanied by rock and blues tunes, reflecting the city's historical soul and sincerity."
    },
    "Symposium HNL": {
        "description": "Mytilene Limanı'nda yer alan 7 Thalasses, taze balık ve yaratıcı deniz ürünleri sunumlarıyla adanın en prestijli lokantalarından biridir. Dalgaların hemen yanında, kaliteli servis ve zengin şarap mönüsü eşliğinde seçkin bir akşam yemeği deneyimi sunar.",
        "description_en": "Located at Mytilene Harbor, 7 Thalasses is one of the island's most prestigious eateries with its fresh fish and creative seafood presentations. It offers an elite dinner experience by the waves, accompanied by quality service and a rich wine menu."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/selanik.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Selanik enriched {count} items.")

import json

# Manual enrichment data (Belgrad Batch 1: 40 items)
updates = {
    "Monument to the Unknown Hero": {
        "description": "Avala Dağı'nın zirvesinde, Birinci Dünya Savaşı'nda hayatını kaybeden bilinmeyen askerlere adanmış anıtsal yapı. Ivan Meštrović'in tasarladığı, Sırp ulusal kimliğinin önemli sembolü.",
        "description_en": "A monumental structure atop Mount Avala dedicated to unknown soldiers who lost their lives in World War I. An important symbol of Serbian national identity designed by Ivan Meštrović."
    },
    "Zemun Quay": {
        "description": "Tuna Nehri kıyısında balık restoranları, kafeler ve akşam yürüyüşleri için ideal sahil şeridi. Tarihi Zemun mahallesinin atmosferik rıhtımı, canlı gece hayatı ve manzaralı terraslar.",
        "description_en": "A waterfront ideal for fish restaurants, cafes, and evening walks along the Danube River. The atmospheric quay of historic Zemun neighborhood, lively nightlife and scenic terraces."
    },
    "New Palace (Novi Dvor)": {
        "description": "Sırbistan Cumhurbaşkanlığı Sarayı olarak hizmet veren, 20. yüzyıl başı Neo-Rönesans mimarisinin görkemli örneği. Tarihi bahçeler, muhafız değişimi ve resmi ziyaret programları.",
        "description_en": "A magnificent example of early 20th century Neo-Renaissance architecture serving as Serbia's Presidential Palace. Historic gardens, changing of the guard, and official visit programs."
    },
    "Botanical Garden Jevremovac": {
        "description": "Şehir merkezinde 5000'den fazla bitki türünü barındıran, 1874'ten beri hizmet veren tarihi botanik bahçe. Tropikal sera, nadir bitkiler ve huzurlu doğa kaçışı.",
        "description_en": "A historic botanical garden serving since 1874 housing over 5000 plant species in the city center. Tropical greenhouse, rare plants, and peaceful nature escape."
    },
    "Military Museum": {
        "description": "Kalemegdan Kalesi içinde konumlanan, Sırp askeri tarihini antik çağlardan günümüze anlatan kapsamlı müze. Silahlar, üniforma koleksiyonları ve savaş tarihi.",
        "description_en": "A comprehensive museum located within Kalemegdan Fortress telling Serbian military history from ancient times to present. Weapons, uniform collections, and war history."
    },
    "Bajrakli Mosque": {
        "description": "Osmanlı döneminden kalma, şehirdeki tek aktif camii. 16. yüzyıl mimarisi, tarihi önemi ve Belgrad'ın çok kültürlü geçmişine tanıklık eden yapı.",
        "description_en": "The only active mosque in the city from Ottoman period. A structure witnessing 16th-century architecture, historic significance, and Belgrade's multicultural past."
    },
    "Kralja Petra Street": {
        "description": "Şehrin en eski alışveriş caddesi, antikacılar, butikler ve kafelerle dolu. Tarihi binaları, kaldırım taşları ve bohemian atmosferiyle, keşfedilmeyi bekleyen sokak.",
        "description_en": "The city's oldest shopping street, full of antique shops, boutiques, and cafes. A street waiting to be discovered with historic buildings, cobblestones, and bohemian atmosphere."
    },
    "Zepter Museum": {
        "description": "Modern sanat ve çağdaş eserleri sergileyen özel müze, uluslararası sanatçıların eserlerini barındırıyor. Dönemsel sergiler, sanat etkinlikleri ve kültürel programlar.",
        "description_en": "A private museum exhibiting modern art and contemporary works, housing works of international artists. Periodic exhibitions, art events, and cultural programs."
    },
    "Belgrade Waterfront": {
        "description": "Sava Nehri kıyısında yükselen modern karma kullanım projesi: lüks rezidanslar, alışveriş merkezi ve yeme-içme alanları. Şehrin yeni silüeti ve çağdaş yaşam alanı.",
        "description_en": "A modern mixed-use project rising along Sava River: luxury residences, shopping mall, and dining areas. The city's new skyline and contemporary living space."
    },
    "Toplicin Venac": {
        "description": "Tarihi binaları, şık butikleri ve trendy kafelerle dolu, şehrin en zarif mahallelerinden biri. Art Nouveau mimarisi, sanat galerileri ve kozmopolit atmosfer.",
        "description_en": "One of the city's most elegant neighborhoods with historic buildings, stylish boutiques, and trendy cafes. Art Nouveau architecture, art galleries, and cosmopolitan atmosphere."
    },
    "Studentski Park": {
        "description": "Üniversite bölgesinde konumlanan, öğrencilerin ve yerel halkın gölgeli banklar altında dinlendiği kentsel park. Heykeller, çeşmeler ve canlı kampüs atmosferi.",
        "description_en": "An urban park located in the university area where students and locals rest under shaded benches. Sculptures, fountains, and lively campus atmosphere."
    },
    "Bajloni Market": {
        "description": "1920'lerden beri hizmet veren, yerel halkın günlük alışveriş için geldiği otantik açık pazar. Taze sebze, meyve, peynir ve Sırp ev yapımı ürünler.",
        "description_en": "An authentic open market serving since 1920s where locals come for daily shopping. Fresh vegetables, fruits, cheese, and Serbian homemade products."
    },
    "Zeleni Venac Market": {
        "description": "Şehrin en işlek pazarlarından biri, taze ürünler ve yerel lezzetlerin satıldığı kapalı ve açık bölümlerle. Sırp gastronomisini keşfetmek için ideal başlangıç noktası.",
        "description_en": "One of the city's busiest markets with covered and open sections selling fresh products and local flavors. An ideal starting point to discover Serbian gastronomy."
    },
    "Kosutnjak": {
        "description": "Şehrin en büyük orman parkı, yürüyüş yolları, spor tesisleri ve piknik alanlarıyla doğa kaçışı. Jogging, bisiklet ve hafta sonu piknikleri için yerel favori.",
        "description_en": "The city's largest forest park, a nature escape with walking trails, sports facilities, and picnic areas. A local favorite for jogging, cycling, and weekend picnics."
    },
    "Topcider Park": {
        "description": "19. yüzyıldan kalma İngiliz tarzı peyzajı ve görkemli ağaçlarıyla tarihi park. Prens Miloš'un yazlık sarayına komşu, Avrupa'nın en eski platan ağaçlarına ev sahipliği yapıyor.",
        "description_en": "A historic park with 19th-century English-style landscaping and magnificent trees. Adjacent to Prince Miloš's summer palace, hosting one of Europe's oldest plane trees."
    },
    "Residence of Prince Milos": {
        "description": "Sırbistan'ın bağımsızlık kahramanı Prens Miloš'un konforu için inşa edilen, Osmanlı-Balkan mimarisi karması tarihi köşk. Müze olarak ziyarete açık, tarihi eşyalar sergileniyor.",
        "description_en": "A historic mansion built for the comfort of Prince Miloš, Serbia's independence hero, a mix of Ottoman-Balkan architecture. Open as museum, displaying historical artifacts."
    },
    "White Palace": {
        "description": "Karađorđević Hanedanı'nın yazlık sarayı, Sırp kraliyet tarihini ve sanat koleksiyonlarını sergiliyor. Rehberli turlarla ziyaret edilebilen, muhteşem bahçeler ve iç dekorasyon.",
        "description_en": "The summer palace of Karađorđević Dynasty, exhibiting Serbian royal history and art collections. Visitable with guided tours, magnificent gardens and interior decoration."
    },
    "Nebojša Tower": {
        "description": "Kalemegdan Kalesi'nin en iyi korunmuş kulesi, Osmanlı döneminde zindan olarak kullanılmış. Tarihi işkence aletleri ve hapsedilenlerin hikayelerini anlatan küçük müze.",
        "description_en": "The best-preserved tower of Kalemegdan Fortress, used as dungeon during Ottoman period. A small museum telling stories of historic torture tools and prisoners."
    },
    "Victor Monument": {
        "description": "Kalemegdan Kalesi'nin en yüksek noktasında, Sava ve Tuna nehirlerinin birleştiği manzaraya bakan ikonik zafer heykeli. Birinci Dünya Savaşı zaferlerini simgeleyen, şehrin sembolü.",
        "description_en": "An iconic victory statue at Kalemegdan Fortress's highest point overlooking where Sava and Danube rivers meet. A city symbol commemorating World War I victories."
    },
    "Roman Well": {
        "description": "Kalemegdan Kalesi içindeki gizemli yeraltı kuyusu, Osmanlı veya daha önceki dönemlere ait su kaynağı. Efsaneler, labirent benzeri yapı ve keşfedilmeyi bekleyen karanlık derinlikler.",
        "description_en": "A mysterious underground well in Kalemegdan Fortress, water source from Ottoman or earlier periods. Legends, labyrinth-like structure, and dark depths waiting to be explored."
    },
    "Manak's House": {
        "description": "18. yüzyıldan kalma, Belgrad'ın en eski konut yapılarından biri. Sırp geleneksel yaşam tarzını sergileyen küçük müze, Balkan ev mimarisinin nadir örneği.",
        "description_en": "One of Belgrade's oldest residential structures from 18th century. A small museum exhibiting Serbian traditional lifestyle, a rare example of Balkan house architecture."
    },
    "Hyde Park Belgrade": {
        "description": "Vračar semtinde konumlanan, Londra'daki ünlü parktan ilham alan yeşil alan. Gölgeli ağaçlar, bank sıraları ve mahalle sakinlerinin favorisi dinlenme noktası.",
        "description_en": "A green area located in Vračar district, inspired by London's famous park. Shaded trees, bench rows, and a favorite rest spot for neighborhood residents."
    },
    "Red Star Stadium": {
        "description": "Kırmızı Yıldız Belgrad futbol takımının stadyumu, Sırp futbolunun en tutkulu atmosferlerinden birini sunan arena. Maç günleri çılgın tribün, stadyum turları mevcut.",
        "description_en": "The stadium of Red Star Belgrade football team, an arena offering one of the most passionate atmospheres in Serbian football. Crazy stands on match days, stadium tours available."
    },
    "Partizan Stadium": {
        "description": "Partizan Belgrad futbol takımının evi, şehrin büyük derbilerinin yarısını ağırlayan tarihi stadyum. Futbol tutkunları için maç ve tur deneyimi.",
        "description_en": "Home of Partizan Belgrade football team, a historic stadium hosting half of the city's big derbies. Match and tour experience for football enthusiasts."
    },
    "Belgrade City Museum": {
        "description": "Şehrin tarihini, kültürünü ve gündelik yaşamını antik çağlardan günümüze anlatan kapsamlı müze. Arkeolojik bulgular, eski fotoğraflar ve Belgrad hikayesi.",
        "description_en": "A comprehensive museum telling the city's history, culture, and daily life from ancient times to present. Archaeological finds, old photos, and Belgrade's story."
    },
    "Historical Museum of Serbia": {
        "description": "Sırp tarihinin en önemli belgelerini, eşyalarını ve eselerini sergileyen ulusal müze. Ortaçağ döneminden modern tarihe, Sırp kimliğinin kronolojisi.",
        "description_en": "A national museum exhibiting the most important documents, artifacts, and works of Serbian history. Chronology of Serbian identity from medieval period to modern history."
    },
    "Jewish Historical Museum": {
        "description": "Belgrad ve Sırbistan'daki Yahudi toplumunun tarihini, kültürünü ve Holokost anılarını sergileyen küçük ama anlamlı müze. Sinagogda konumlanmış, önemli koleksiyon.",
        "description_en": "A small but meaningful museum exhibiting the history, culture, and Holocaust memories of Jewish community in Belgrade and Serbia. Located in synagogue, important collection."
    },
    "Pajsijeva Street": {
        "description": "Dorćol mahallesinde, kafeler, butikler ve sokak sanatıyla dolu trendy sokak. Genç yaratıcıların, sanatçıların ve bohemian ruhun buluştuğu, keşfedilmeyi bekleyen köşe.",
        "description_en": "A trendy street in Dorćol neighborhood full of cafes, boutiques, and street art. A corner where young creatives, artists, and bohemian spirit meet, waiting to be discovered."
    },
    "Sajmiste Concentration Camp": {
        "description": "İkinci Dünya Savaşı sırasında Nazi işgali altında faaliyet gösteren toplama kampının kalıntıları. Holokost anıt alanı, tarihsel farkındalık ve anma ziyareti.",
        "description_en": "Remains of the concentration camp operating under Nazi occupation during World War II. Holocaust memorial site, historical awareness, and commemorative visit."
    },
    "Ada Bridge": {
        "description": "Sava Nehri'ni geçen, modern mühendisliğin şahikası asma köprü. Gece aydınlatması, minimalist tasarımı ve şehir silüetine katkısıyla, çağdaş Belgrad'ın sembolü.",
        "description_en": "A cable-stayed bridge crossing Sava River, a pinnacle of modern engineering. A symbol of contemporary Belgrade with night lighting, minimalist design, and contribution to city skyline."
    },
    "Branko's Bridge": {
        "description": "Eski Şehir'i Yeni Belgrad'a bağlayan tarihi köprü, yaya ve araç trafiğine açık. Köprü üzerinden Kalemegdan ve nehir manzarası, gün batımı için ideal konum.",
        "description_en": "A historic bridge connecting Old Town to New Belgrade, open to pedestrian and vehicle traffic. Kalemegdan and river views from the bridge, ideal location for sunset."
    },
    "Sava Promenade": {
        "description": "Sava Nehri kıyısında yeni düzenlenen yürüyüş ve bisiklet yolu, kafeler ve manzara noktalarıyla. Modern kent yaşamı, nehir kenarı dinlenmesi ve aktif ulaşım.",
        "description_en": "A newly arranged walking and cycling path along Sava River with cafes and viewpoints. Modern urban living, riverside relaxation, and active transportation."
    },
    "Karadjordje's Park": {
        "description": "Belgrad'ın en eski parklarından biri, tarihi heykeller ve anıtlarla dolu. Sırp tarihinin önemli figürlerine adanmış bu park, yeşil bir tarih dersi sunuyor.",
        "description_en": "One of Belgrade's oldest parks, full of historic statues and monuments. This park dedicated to important figures of Serbian history offers a green history lesson."
    },
    "Pioneer Park": {
        "description": "Cumhurbaşkanlığı Sarayı yakınında, şehir merkezinde çocuklar ve aileler için oyun alanları ve yeşil alan. Merkezi konumu ve gölgeli ağaçlarıyla mola noktası.",
        "description_en": "Playgrounds and green area for children and families in city center near Presidential Palace. A rest stop with central location and shaded trees."
    },
    "Cvetni Trg": {
        "description": "Şehrin merkezinde çiçekçiler, kafeler ve buluşma noktalarıyla ünlü küçük meydan. Canlı atmosferi, açık hava oturma alanları ve randevu için ideal konum.",
        "description_en": "A small square in city center famous for florists, cafes, and meeting points. Lively atmosphere, outdoor seating areas, and ideal location for appointments."
    },
    "Holy Trinity Church": {
        "description": "Rus Ortodoks tarzında inşa edilmiş, sürgündeki Rus göçmenlerin topluluğu tarafından kullanılan atmosferik kilise. İkonalar, freskler ve Rus dini mirasının Belgrad'daki izi.",
        "description_en": "An atmospheric church built in Russian Orthodox style, used by Russian emigrant community in exile. Icons, frescoes, and trace of Russian religious heritage in Belgrade."
    },
    "Belgrade Fortress Clock Tower": {
        "description": "Kalemegdan Kalesi'nin 18. yüzyıldan kalma ikonik saat kulesi, şehrin tarihi saatini gösteren landmark. Kale kompleksinin en fotoğraflanan noktalarından biri.",
        "description_en": "The iconic 18th-century clock tower of Kalemegdan Fortress, a landmark showing the city's historic time. One of the most photographed points of the fortress complex."
    },
    "Madlenianum Opera": {
        "description": "Zemun'da konumlanan özel opera ve tiyatro binası, kaliteli prodüksiyonları ve samimi atmosferiyle. Opera, bale ve tiyatro gösterileri, kültürel akşamlar için ideal.",
        "description_en": "A private opera and theater building located in Zemun with quality productions and intimate atmosphere. Opera, ballet, and theater performances, ideal for cultural evenings."
    },
    "Danube Quay": {
        "description": "Tuna Nehri kıyısında balık restoranları, barlar ve tekne turları sunan canlı sahil şeridi. Yaz akşamlarında nehir kenarı eğlencesi ve manzaralı yemek deneyimi.",
        "description_en": "A lively waterfront along Danube River offering fish restaurants, bars, and boat tours. Riverside entertainment on summer evenings and dining experience with views."
    },
    "Ivo Andric Museum": {
        "description": "Nobel Edebiyat Ödüllü Sırp yazar Ivo Andrić'in evine dönüştürülmüş anı müzesi. Kişisel eşyaları, el yazmaları ve edebiyat mirasıyla, yazarlar için ilham kaynağı.",
        "description_en": "A memorial museum converted from the home of Nobel Literature Prize-winning Serbian writer Ivo Andrić. A source of inspiration for writers with personal items, manuscripts, and literary legacy."
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

print(f"\n✅ Manually enriched {count} items (Belgrad Batch 1).")

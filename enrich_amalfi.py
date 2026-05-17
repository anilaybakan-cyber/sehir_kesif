#!/usr/bin/env python3
import json

updates = {
    "ChIJrSB4qrqVOxMR3io9z2JxH9Y": {
        "description": "Amalfi'nin bin yıllık kağıt yapım geleneğini yaşatan bu müze, eski bir kağıt değirmeninde yer alır. Orta Çağ'dan kalma makineleri, orijinal üretim tekniklerini ve elle yapılan özel kağıtların hikayesini keşfedebileceğiniz, kentin endüstriyel mirasına dair büyüleyici bir duraktır.",
        "description_en": "Preserving Amalfi's thousand-year-old papermaking tradition, this museum is located in an old paper mill. It is a fascinating stop on the city's industrial heritage where you can discover medieval machinery, original production techniques, and the story of special handmade papers."
    },
    "ChIJaZAh4qiVOxMRfqIdztVS_rY": {
        "description": "Amalfi'nin hemen yanı başında yer alan Atrani, İtalya'nın en küçük ve en karakteristik balıkçı köylerinden biridir. Labirent gibi dar sokakları, birbirine yaslanmış beyaz evleri ve denize açılan şirin meydanıyla, kitle turizminden uzak, gerçek bir Güney İtalya atmosferi sunar.",
        "description_en": "Located right next to Amalfi, Atrani is one of Italy's smallest and most characteristic fishing villages. With its labyrinthine narrow streets, leaning white houses, and charming square opening to the sea, it offers an authentic South Italian atmosphere away from mass tourism."
    },
    "ChIJUYB5vUSVOxMRiddknG1THH0": {
        "description": "Amalfi kıyılarının en geniş kumsalına ev sahipliği yapan Maiori, görkemli otelleri ve ferah sahil şeridiyle bilinir. Roma döneminden kalma antik villa kalıntıları ve huzurlu limanıyla, hem deniz keyfi hem de tarihi keşifler arayan aileler için kentin en konforlu ve keyifli noktalarından biridir.",
        "description_en": "Hosting the widest beach on the Amalfi coast, Maiori is known for its grand hotels and spacious coastline. With ancient Roman villa ruins and a peaceful harbor, it is one of the city's most comfortable and pleasant spots for families seeking both seaside fun and historical discoveries."
    },
    "ChIJQR1rY66VOxMRtlyZ3muuezw": {
        "description": "Amalfi Katedrali'nin hemen yanında yer alan bu müze, kentin dini tarihine ait paha biçilemez sanat eserlerini ve kutsal emanetleri sergiler. 9. yüzyıldan kalma bazilika kalıntıları ve göz alıcı Bizans dönemi objeleriyle, kentin manevi ve estetik derinliğini yansıtan sessiz bir hazinedir.",
        "description_en": "Located right next to Amalfi Cathedral, this museum exhibits priceless artworks and sacred relics from the city's religious history. With 9th-century basilica remains and stunning Byzantine-era objects, it is a quiet treasure reflecting the city's spiritual and aesthetic depth."
    },
    "ChIJob5w0K2VOxMRvCvlIHjVUDw": {
        "description": "Amalfi'nin güçlü denizcilik geçmişine tanıklık eden bu tarihi tersane, bugün kentin prestijli sergi alanı ve bilgi merkezi olarak hizmet veriyor. Taş kemerleri ve mistik atmosferiyle kentin eskiden tüm Akdeniz'e hükmeden kadırgalarının inşa edildiği bu alan, kentin en gurur duyulan tarihi miraslarından biridir.",
        "description_en": "Witnessing Amalfi's powerful maritime past, this historic shipyard today serves as the city's prestigious exhibition space and information center. With stone arches and a mystical atmosphere, this area where galleys that once ruled the Mediterranean were built is one of the city's proudest historical heritages."
    },
    "ChIJq9Ae3ciVOxMRNpg1ajlt_po": {
        "description": "Amalfi'nin sanatsal ve hobi dünyasına ışık tutan bu özel nokta, ünlü Amalfi kağıdından antika kartpostallara kadar kentin hatıralarını barındırır. Adanın nostaljik silüetini yansıtan özgün koleksiyonlarıyla, kentin ruhunu sevdiklerinize gönderebileceğiniz en samimi ve fotojenik alışveriş duraklarından biridir.",
        "description_en": "Lighting up Amalfi's artistic and hobby world, this special spot contains memories of the city ranging from famous Amalfi paper to antique postcards. With original collections reflecting the island's nostalgic silhouette, it's one of the most sincere and photogenic shopping stops where you can send the city's spirit to your loved ones."
    },
    "ChIJY1SKzNyVOxMRMYzOt-rrHNM": {
        "description": "Kentin dar sokakları arasına gizlenmiş bu karakteristik dini köşe, yerel halkın inanç ve geleneklerinin samimi bir yansımasıdır. Renkli süslemeleri ve her gün taze çiçeklerle bezenmiş sunaklarıyla, Amalfi'nin gündelik yaşamında dinin ne denli canlı ve önemli bir yer tuttuğunu gösteren etkileyici bir mahalle simgesidir.",
        "description_en": "This characteristic religious corner hidden among the narrow streets of the city is a sincere reflection of local beliefs and traditions. With colorful decorations and altars adorned with fresh flowers daily, it's an impressive neighborhood symbol showing how vibrant and important religion is in Amalfi's daily life."
    },
    "ChIJ1dqn3Z-VOxMROLCaZNzZXmw": {
        "description": "Ravello'nun tepelerinde yer alan bu tarihi kule, kentin antik savunma stratejilerini ve arkeolojik buluntularını sergileyen bir müzedir. Sarp kayalar üzerindeki konumu ve sunduğu uçsuz bucaksız deniz manzarasıyla, hem tarih meraklıları hem de fotoğraf tutkunları için eşsiz ve havadar bir keşif noktasıdır.",
        "description_en": "Located in the hills of Ravello, this historic tower is a museum exhibiting the city's ancient defensive strategies and archaeological finds. With its position on steep rocks and the endless sea views it offers, it is a unique and airy discovery point for both history buffs and photography enthusiasts."
    },
    "ChIJb8673Z-VOxMRaAqE3RFyebg": {
        "description": "Amalfi kıyılarının ünlü mercan işleme sanatını sergileyen bu müze, nadir bulunan mercan mücevherleri ve antik eserleriyle büyüleyicidir. Denizin derinliklerinden gelen bu şifalı olduğuna inanılan taşın hikayesini ve ustaların elinde nasıl birer sanat eserine dönüştüğünü görmek için büyüleyici bir duraktır.",
        "description_en": "Exhibiting the Amalfi coast's famous coral processing art, this museum is fascinating with rare coral jewelry and ancient artifacts. It's a mesmerizing stop to see the story of this stone believed to be healing, coming from the depths of the sea, and how it transforms into artworks in the hands of masters."
    },
    "ChIJEa6d0p-VOxMRdSTX4Cr4Xc0": {
        "description": "Ravello'nun en seçkin seramik atölyelerinden biri olan Pascal Ceramiche, el yapımı tabakları, vazoleri ve geleneksel motifleriyle ünlüdür. Her biri usta ellerden çıkan ve Amalfi'nin renklerini yansıtan bu eserler, kentin sanat ruhunu evinize taşımak için en zarif ve kaliteli hatıra duraklarından biridir.",
        "description_en": "One of Ravello's most exclusive ceramic workshops, Pascal Ceramiche is famous for its handmade plates, vases, and traditional motifs. Each of these works, emerging from master hands and reflecting Amalfi's colors, is one of the most elegant and high-quality souvenir stops to bring the city's artistic spirit to your home."
    },
    "ChIJOZQYLWyVOxMR7Y15y46QwAQ": {
        "description": "Minori'de yer alan bu antik Roma villası, 1. yüzyıldan kalma mozaikleri ve mimari detaylarıyla kentin aristokratik geçmişine ışık tutar. Deniz kenarındaki sakin konumu ve iyi korunmuş antik hamamlarıyla, Amalfi kıyılarının sadece bir doğa harikası değil, aynı zamanda köklü bir tarih havzası olduğunu kanıtlar.",
        "description_en": "Located in Minori, this ancient Roman villa sheds light on the city's aristocratic past with its 1st-century mosaics and architectural details. With its quiet seaside location and well-preserved ancient baths, it proves that the Amalfi coast is not just a natural wonder, but also a deep-rooted historical basin."
    },
    "ChIJif-my22VOxMRNCVpUubEL0o": {
        "description": "Salerno bölgesindeki arkeolojik zenginlikleri koruma ve sergileme görevini üstlenen bu kurum, kentin antik döneminden kalma en önemli eserlerin merkezidir. Bilimsel ve tarihi derinliğiyle, Amalfi kıyılarının binlerce yıllık katmanlarını merak eden gezginler için akademik düzeyde bir eğitim ve keşif noktasıdır.",
        "description_en": "Entrusted with the task of preserving and exhibiting archaeological riches in the Salerno region, this institution is the center for the most important artifacts from the city's ancient period. With its scientific and historical depth, it is an academic-level education and discovery point for travelers curious about the Amalfi coast's thousands of years of layers."
    },
    "ChIJEf7n3_6VOxMR9GwNWSTxdis": {
        "description": "Atrani'nin kalbinde yer alan bu dini müze, kentin yerel azizlerine ve kilise mirasına adanmış nadide bir koleksiyon sunar. Samimi atmosferi ve yüzyıllara meydan okuyan dini tablolarıyla, kentin sessiz ve inanç dolu ruhunu en saf haliyle deneyimleyebileceğiniz huzurlu bir kültürel duraktır.",
        "description_en": "Located in the heart of Atrani, this religious museum offers a rare collection dedicated to the city's local saints and church heritage. With its intimate atmosphere and religious paintings defying centuries, it is a peaceful cultural stop where you can experience the city's quiet and faith-filled spirit in its purest form."
    },
    "ChIJo5RTFACZOxMRWEZoyx_88bo": {
        "description": "Amalfi sahil şeridinin kristal berrak sularıyla buluştuğu bu ikonik plaj, kentin masmavi manzarasını ve güneşini deneyimlemek için en popüler adrestir. Dik kayalıkların altındaki şık tesisleri ve tazeleyici deniz havasıyla, İtalyan yazının tadını çıkarmak isteyen gezginlerin vazgeçilmez deniz sefası durağıdır.",
        "description_en": "This iconic beach where the Amalfi coastline meets crystal-clear waters is the most popular address to experience the city's deep blue views and sun. With chic facilities under steep cliffs and refreshing sea air, it is an indispensable seaside delight stop for travelers wanting to enjoy the Italian summer."
    },
    "ChIJm5orj3eXOxMRdbp-qtR0VNw": {
        "description": "Positano'nun merkezindeki bu etkileyici arkeoloji müzesi, bir kilisenin altında keşfedilen muazzam bir Roma villasının üzerine kurulmuştur. MS 79 yılındaki Vesuvius patlamasıyla korunan canlı freskleri ve antik objeleriyle, zamanın donduğu paha biçilemez bir tarihi hazine niteliğindedir.",
        "description_en": "This impressive archaeological museum in the center of Positano is built over a magnificent Roman villa discovered under a church. With its vivid frescoes and ancient objects preserved by the AD 79 Vesuvius eruption, it serves as a priceless historical treasure where time has frozen."
    },
    "ChIJw1WtrCSXOxMRAyokGzUaKUs": {
        "description": "Positano'nun karakterini tamamlayan yerel bir zanaatkar noktası olan bu alan, kentin dünden bugüne gelen geleneksel işçiliğini temsil eder. Sokak aralarında kaybolurken rastlayacağınız bu tipik duraklar, kentin sadece turistik bir tablo olmadığını, yaşayan ve üreten bir yerel halka sahip olduğunu gösteren samimi detaylardandır.",
        "description_en": "A local artisan spot completing Positano's character, this area represents the city's traditional craftsmanship passed down from yesterday to today. These typical stops you'll encounter while getting lost in alleys are sincere details showing that the city is not just a tourist painting, but has a living and producing local population."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/amalfi.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    pid = place.get('id')
    if pid in updates:
        place['description'] = updates[pid]['description']
        place['description_en'] = updates[pid]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Amalfi enriched {count} items.")

#!/usr/bin/env python3
import json

updates = {
    "ChIJ1SwHhqm_ohQRAUJ_qnteaB0": {
        "description": "Mykonos Town'un kalbi sayılan Matogianni, bembeyaz boyalı evleri, rengarenk begonvilleri ve dünyaca ünlü butikleriyle adanın en popüler alışveriş sokağıdır. Gece boyu canlılığını koruyan bu dar Arnavut kaldırımlı sokaklar, adanın kozmopolit enerjisini ve şık gece hayatını en iyi hissedeceğiniz yerdir.",
        "description_en": "Matogianni, considered the heart of Mykonos Town, is the island's most popular shopping street with its white-painted houses, colorful bougainvillaea, and world-famous boutiques. These narrow cobbled streets, which remain vibrant all night, are where you can best feel the island's cosmopolitan energy and chic nightlife."
    },
    "ChIJjRE-16m_ohQRZNVavPJdm1M": {
        "description": "Kentin üst kısımlarında yer alan Boni'nin Yel Değirmeni, adanın tarihi tarım geçmişini yansıtan en iyi korunmuş yapılardan biridir. Hem bir açık hava müzesi görevi gören bu bölge hem de batan güneşin Mykonos limanı ve Little Venice üzerindeki eşsiz manzarasını seyretmek için en ideal noktadır.",
        "description_en": "Located in the upper parts of the town, Boni's Windmill is one of the best-preserved structures reflecting the island's historical agricultural past. This area, which serves as an open-air museum, is also the most ideal spot to watch the unique view of the setting sun over Mykonos harbor and Little Venice."
    },
    "ChIJt2mz36e_ohQRmF1ws4-6Czs": {
        "description": "Adanın antik geçmişine ışık tutan bu müze, özellikle yakınlardaki Rhenia adasından getirilen eşsiz vazo koleksiyonları ve Helenistik dönem heykelleriyle bilinir. Mykonos'un sadece eğlence değil, aynı zamanda derin bir tarihi miras barındırdığını kanıtlayan, kültürel bir hazine niteliğindedir.",
        "description_en": "Shedding light on the island's ancient past, this museum is known for its unique pottery collections particularly brought from the nearby island of Rhenia and Hellenistic period statues. It operates as a cultural treasure proving that Mykonos hosts not just entertainment, but also a deep historical heritage."
    },
    "ChIJHVjEgKm_ohQRd2Aq2zQGfH0": {
        "description": "19. yüzyıldan kalma bir Mykonos orta sınıf evinin atmosferini yansıtan Lena'nın Evi, adanın yerel yaşam kültürüne ve geleneksel mobilyalarına dair samimi bir pencere açar. Dönemin estetik anlayışını ve günlük yaşam tarzını en doğal haliyle görebileceğiniz etkileyici bir folklor durağıdır.",
        "description_en": "Reflecting the atmosphere of a 19th-century Mykonos middle-class home, Lena's House opens an intimate window into the island's local life culture and traditional furniture. It is an impressive folklore stop where you can see the period's aesthetic understanding and daily lifestyle in its most natural form."
    },
    "ChIJGZBOn6m_ohQR-41vOdkSYTs": {
        "description": "Adanın tarım mirasını ve rüzgar enerjisiyle çalışan eski değirmen teknolojisini sergileyen bu müze, geleneksel bağ bozumu kutlamalarının da merkezidir. Değirmenin etrafındaki harman yerleri ve eski tarım aletleri, Mykonos'un kırsal hayatına dair nostaljik ve eğitici bir yolculuk sunar.",
        "description_en": "Showcasing the island's agricultural heritage and old windmill technology powered by wind energy, this museum is also the center of traditional harvest celebrations. The threshing floors around the mill and ancient farming tools offer a nostalgic and educational journey into Mykonos's rural life."
    },
    "ChIJi4r-MKm_ohQRZzqwIKDNKeM": {
        "description": "Kaptan evlerinden birinde yer alan Mykonos Folklör Müzesi, antik mobilyalar, yerel giysiler ve adanın denizcilik tarihine ait nadide parçalarla doludur. Adanın sadece turistik bir mekan olmaktan öte, ne denli köklü bir yerel kimliğe ve geleneğe sahip olduğunu ziyaretçilere fısıldar.",
        "description_en": "Located in one of the captain's houses, the Mykonos Folklore Museum is filled with ancient furniture, local costumes, and rare pieces of the island's maritime history. It whispers to visitors how deep-rooted a local identity and tradition the island possesses, beyond being just a tourist destination."
    },
    "ChIJ_f___y-_ohQRWXjQfo7HSAE": {
        "description": "Adanın en köklü ve ikonik kulüplerinden biri olan ASTRA, şık tasarımı ve elit atmosferiyle Mykonos gecelerinin vazgeçilmezidir. Gökyüzündeki yıldızları andıran tavan aydınlatması ve ünlü simaları ağırlayan ambiyansıyla, kentin kozmopolit ruhunu en iyi yansıtan eğlence merkezlerindendir.",
        "description_en": "One of the island's most established and iconic clubs, ASTRA is indispensable to Mykonos nights with its chic design and elite atmosphere. With its ceiling lighting reminiscent of stars in the sky and an ambiance hosting famous names, it's one of the entertainment hubs that best reflects the city's cosmopolitan spirit."
    },
    "ChIJ9d8ZBCm_ohQRibJF5II-KXQ": {
        "description": "Dar sokakların içine gizlenmiş şık ve modern bir eğlence noktası olan Madon, etkileyici ses sistemleri ve her gece değişen DJ performanslarıyla bilinir. Mykonos Town'un hareketli gecelerine enerjik ve kaliteli bir alternatif sunan mekan, dans ve eğlence tutkunlarının favori buluşma noktalarından biridir.",
        "description_en": "A chic and modern entertainment spot hidden within the narrow streets, Madon is known for its impressive sound systems and nightly rotating DJ performances. Offering an energetic and quality alternative to Mykonos Town's lively nights, the venue is a favorite meeting point for dance and fun enthusiasts."
    },
    "ChIJAaN7Pqm_ohQRYYW3kaZTMaQ": {
        "description": "Sadece bilenlerin uğradığı ve samimi atmosferiyle öne çıkan Moni, kaliteli müzik ve seçkin bir kitleyi buluşturan Mykonos'un saklı kulüplerindendir. Şık barı ve her gece kentin en iyi DJ'lerini ağırlayan sahnesiyle, gecenin ilerleyen saatlerinde adanın ritmine ayak uydurmak için mükemmeldir.",
        "description_en": "Moni, visited only by those in the know and standing out with its intimate atmosphere, is one of Mykonos's hidden clubs bringing together quality music and an elite crowd. With its chic bar and stage hosting the city's best DJs every night, it's perfect for keeping up with the island's rhythm in the late hours."
    },
    "ChIJr_CVadG_ohQRouZOQzBn4lo": {
        "description": "Ege denizinin zengin denizcilik tarihini maket gemiler, antik haritalar ve deniz araçlarıyla sergileyen bu müze, deniz severler için büyüleyici bir duraktır. Mykonos'un denizle olan derin bağını ve Ege'deki stratejik önemini anlamak için adanın en bilgilendirici kültürel duraklarından biridir.",
        "description_en": "Showcasing the Aegean Sea's rich maritime history with model ships, ancient maps, and nautical instruments, this museum is a fascinating stop for sea lovers. It is one of the island's most informative cultural stops for understanding Mykonos's deep bond with the sea and its strategic importance in the Aegean."
    },
    "ChIJvcCHNwC5ohQRXAiEu-1mWBw": {
        "description": "Kentin sahil şeridinde yer alan bu sembolik yapı, Mykonos'un kendine has beyaza boyalı mimarisi ve masmavi deniz manzarasıyla birleşen nostaljik bir anıttır. Şehir silüetine tarihi bir derinlik katan yapı, özellikle güneşin batışında altın rengine bürünerek harika fotoğraf karelerine eşlik eder.",
        "description_en": "Located along the city's coastline, this symbolic structure is a nostalgic monument combined with Mykonos's unique white-painted architecture and deep blue sea views. Adding a historical depth to the city silhouette, the structure turns golden especially at sunset, accompanying great photo shots."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/mykonos.json.draft'
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

print(f"✅ Mykonos enriched {count} items.")

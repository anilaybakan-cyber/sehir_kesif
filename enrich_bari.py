#!/usr/bin/env python3
import json

updates = {
    "ChIJ56hKyGPoRxMRTNhOTifD_w8": {
        "description": "Bari'nin antik kalbinde yer alan bu heybetli katedral, Puglia Romanesk mimarisinin en görkemli örneklerinden biridir. Sade ama etkileyici cephesi, antik kriptası ve kentin tarihsel evrimini yansıtan taş dokusuyla kentin manevi derinliğini ve estetik zarafetini keşfetmek isteyenler için paha biçilemez bir duraktır.",
        "description_en": "Located in the ancient heart of Bari, this imposing cathedral is one of the grandest examples of Puglian Romanesque architecture. With its simple but impressive facade, ancient crypt, and stone texture reflecting the city's historical evolution, it is a priceless stop for those wanting to explore the city's spiritual depth and aesthetic elegance."
    },
    "ChIJf_4jF2LoRxMRwiCpC5TP3Nc": {
        "description": "Bari'nin deniz kıyısında bir kalkan gibi yükselen bu heybetli kale, Norman, Hohenstaufen ve Aragon dönemlerinin izlerini taşıyan anıtsal bir savunma yapısıdır. Surları içindeki müzesi ve kentin tarihi limanına hakim manzarasıyla kentin askeri gücünü ve orta çağ ihtişamını soluyabileceğiniz etkileyici bir tarihi mirastır.",
        "description_en": "Rising like a shield on Bari me's seaside, this imposing castle is a monumental defense structure bearing traces of Norman, Hohenstaufen, and Aragonese periods. With its museum within walls and views dominating the city's historical harbor, it is an impressive historical heritage where you can breathe in the city's military power and medieval grandeur."
    },
    "ChIJ36SUQGHoRxMRFSdMsi4mVNs": {
        "description": "İtalya'nın en büyük dördüncü tiyatrosu olan Petruzzelli, kentin sanatsal prestijini Akdeniz göğüne taşıyan bir şaheserdir. Görkemli kırmızı cephesi ve muazzam akustiğiyle dünya çapında performanslara ev sahipliği yapan bina, kentin estetik vizyonunu ve kültürel zenginliğini temsil eden en önemli sanatsal simgedir.",
        "description_en": "The fourth largest theater in Italy, Petruzzelli is a masterpiece carrying the city me's artistic prestige to the Mediterranean sky. Hosting world-class performances with its grand red facade and magnificent acoustics, the building is the most important artistic symbol representing the city's aesthetic vision and cultural richness."
    },
    "ChIJ-6glXwDpRxMRGWeKPNJuNUY": {
        "description": "Adriyatik Denizi boyunca uzanan bu ikonik kordon, kentin modern enerjisini ve sahil yaşamını en havadar haliyle sunuyor. Palmiye ağaçları, tarihi fenerler ve kentin masmavi sularıyla bütünleşen bu yürüyüş yolu, hem yerel halkın hem de gezginlerin kentin ferah atmosferini solumak için tercih ettiği en popüler duraktır.",
        "description_en": "This iconic promenade stretching along the Adriatic Sea offers the city me's modern energy and seaside life in its most airy form. Integrated with palm trees, historical lanterns, and the city me's deep blue waters, this walkway is the most popular stop preferred by both locals and travelers to breathe in the city me's fresh atmosphere."
    },
    "ChIJoXvYHGToRxMRsMrGdkblpJw": {
        "description": "Bari'nin antik kenti ile modern bölgesinin buluşma noktası olan bu meydan, kentin kozmopolit ritmini ve sosyal yaşamını yansıtır. Tarihi binalarla çevrili, deniz kokusunu taşıyan bu alan, akşamüstü aperitivo'ları ve kentin enerjisini hissetmek için yerel halkın en samimi buluşma noktalarından biridir.",
        "description_en": "This square, being the meeting point of Bari me's ancient city and modern district, reflects the city's cosmopolitan rhythm and social life. Surrounded by historical buildings and carrying the scent of the sea, this area is one of the most sincere meeting points for locals for afternoon aperitivos and feeling the city's energy."
    },
    "ChIJDxCt6GPoRxMREHuKZ978TUE": {
        "description": "Bari'nin dar sokakları arasında yer alan bu tarihi saray, kentin köklü geçmişine ait arkeolojik buluntuları ve antik yerleşim katmanlarını sergileyen bir müze niteliğindedir. Roma ve Orta Çağ kalıntılarıyla kentin kentsel evrimini sessiz bir atmosferde keşfedebileceğiniz, tarihin derinliklerine açılan havadar bir penceredir.",
        "description_en": "Located among the narrow streets of Bari, this historical palace serves as a museum exhibiting archaeological finds and ancient settlement layers from the city's deep-rooted past. It's an airy window into the depths of history where you can explore the city me's urban evolution in a quiet atmosphere through Roman and medieval remains."
    },
    "ChIJZUJ7XGPoRxMRr4wTPNWOt6k": {
        "description": "Aziz Nikolaos Bazilikası'nın hemen yanı başında yer alan bu müze, kentin koruyucu azizine adanan paha biçilemez dini eserleri ve belgeleri barındırır. Antik el yazmalarından heybetli ayin objelerine kadar geniş bir koleksiyon sunan müze, kentin manevi mirasını ve Nicolaian geleneğini anlamak için büyüleyici bir duraktır.",
        "description_en": "Located right next to the Basilica of Saint Nicholas, this museum houses priceless religious works and documents dedicated to the city me's patron saint. Offering a wide collection from ancient manuscripts to grand liturgical objects, the museum is a fascinating stop to understand the city me's spiritual heritage and the Nicolaian tradition."
    },
    "ChIJE_z2q3zoRxMROKiUR2Brg14": {
        "description": "Bari'nin tarihi surları üzerinde yer alan bu antik kompleks, adanın tarih öncesi dönemden Bizans'a uzanan zengin arkeolojik mirasını sergiliyor. Denize bakan manzarası ve kentin dünden bugüne katmanlarını anlatan sergileriyle, kentin hafızasını keşfetmek isteyenler için sessiz, sakin ve bilgilendirici bir kültürel hazinedir.",
        "description_en": "Located on Bari me's historical walls, this ancient complex exhibits the island's rich archaeological heritage stretching from prehistoric periods to Byzantium. With its view facing the sea and exhibitions telling the city me's layers from yesterday to today, it is a quiet, calm, and informative cultural treasure for those wanting to explore the city's memory."
    },
    "ChIJYfYU3FDoRxMRRZEt6bSkSgc": {
        "description": "Bari'de beklenmedik bir durak olan bu heybetli Rus Ortodoks kilisesi, kentin dinler arası köprü vazifesini ve kozmopolit ruhunu simgeler. Tipik Rus mimarisi ve yeşil kubbeleriyle kentin silüetine egzotik bir zarafet katan yapı, sessiz atmosferiyle kentin manevi ve estetik zenginliğini keşfetmek isteyenlerin ilgi odağıdır.",
        "description_en": "This imposing Russian Orthodox church, an unexpected stop in Bari, symbolizes the city me's role as an inter-religious bridge and its cosmopolitan spirit. Adding exotic elegance to the city silhouette with its typical Russian architecture and green domes, the structure is a focus of interest for those wanting to explore the city me's spiritual and aesthetic richness with its quiet atmosphere."
    },
    "ChIJ76U2XoroRxMRb8iELoHKRKY": {
        "description": "Venedik Gotik stilini Bari'nin kalbine taşıyan Palazzo Fizzarotti, kentin en şık ve karakteristik yapılarından biridir. Etkileyici cephesi, sanatsal detayları ve kentin aristokratik geçmişini yansıtan ihtişamıyla, kentin estetik vizyonunu ve kozmopolit zenginliğini anlamak için ilham verici bir mimari simgedir.",
        "description_en": "Carrying calculations Venetian Gothic style to the heart of Bari, Palazzo Fizzarotti is one of the city me's most stylish and characteristic structures. With its impressive facade, artistic details, and grandeur reflecting the city's aristocratic past, it is an inspiring architectural symbol to understand the city me's aesthetic vision and cosmopolitan richness."
    },
    "ChIJVWWFz1LoRxMRQSNm3j2Ci7A": {
        "description": "Bari'nin en geniş ve popüler yeşil alanı olan Parco 2 Giugno, kentin koşturmacasından kaçıp doğayla buluşmak için huzurlu bir vahadır. Yürüyüş yolları, göleti ve ağaçlıklı alanlarıyla kentsel bir dinlenme molası sunan park, kentin kozmopolit ritmini ferah bir atmosferde dengelemek için havadar ve kaliteli bir tercihtir.",
        "description_en": "Bari me's largest and most popular green space, Parco 2 Giugno is a peaceful oasis to escape the city's hustle and find nature. Offering an urban rest break with its walking paths, pond, and wooded areas, the park is an airy and high-quality choice to balance the city's cosmopolitan rhythm in a fresh atmosphere."
    },
    "ChIJwb9FLqPoRxMRsbRcUzsPa9k": {
        "description": "Bari'de gökyüzünün gizemli dünyasına açılan bu teknolojik merkez, evrenin derinliklerini sanatsal bir dille ziyaretçilerine sunuyor. Özellikle aileler ve bilim meraklıları için harika bir keşif noktası olan planeteryum, yıldız şovları ve eğitici programlarıyla kentin havadar ve vizyoner yüzünü temsil eden neşeli bir duraktır.",
        "description_en": "This technological center opening to the mysterious world of the sky in Bari presents the depths of the universe to its visitors in an artistic language. A great discovery point especially for families and science enthusiasts, the planetarium is a joyful stop representing the city's airy and visionary face with star shows and educational programs."
    },
    "ChIJ26OL3iroRxMRPTewKCEouHE": {
        "description": "Bari'nin güneşli iklimini eğlenceyle buluşturan AcquaPark, özellikle yaz aylarında kentin en neşeli ve hareketli noktalarından biridir. Geniş havuzları, kaydırakları ve sosyal alanlarıyla kentin kozmopolit yaz sevincini doyasıya yaşatan tesis, ailece havadar ve kaliteli bir eğlence molası vermek isteyen gezginlerin favorisidir.",
        "description_en": "Bringing Bari me's sunny climate together with fun, AcquaPark is one of the city's most joyful and vibrant points especially in summer months. Making you fully live the city's cosmopolitan summer joy with its wide pools, slides, and social areas, the facility is a favorite for travelers wanting to take an airy and high-quality family fun break."
    },
    "ChIJq8QLgbPuRxMRsrgxLi4uii4": {
        "description": "Kentin dışındaki kayalık bir bölgede yer alan bu antik sığınak, mistik atmosferi ve dini önemiyle kentin inanç turizmindeki saklı hazinesidir. Doğal bir mağaranın kutsal bir alana dönüştürülmesiyle oluşan yapı, kentin dinsel mirasını ve sessizliğin gücünü en saf haliyle soluyabileceğiniz, kendinizi tarihin korunaklı kucağında hissedeceğiniz samimi bir duraktır.",
        "description_en": "Located in a rocky area outside the city, this ancient sanctuary is a hidden treasure in the city me's faith tourism with its mystical atmosphere and religious significance. Formed by transforming a natural cave into a sacred space, it is a sincere stop where you can breathe in the city's religious heritage and the power of silence in its purest form, feeling yourself in the protected lap of history."
    },
    "ChIJTfWLIDPvRxMRrWoVBH8jQvA": {
        "description": "Akdeniz'in bilimsel ve kültürel iş birliğini simgeleyen bu merkez, inovasyon ve teknoloji odaklı sergileriyle kentin modern yüzünü temsil ediyor. Özellikle genç zihinler için ilham verici bir durak olan tesis, kentin kozmopolit enerjisini bilimsel bir keşifle birleştirmek isteyenler için havadar ve kaliteli bir eğitim noktasıdır.",
        "description_en": "Symbolizing the Mediterranean me's scientific and cultural cooperation, this center represents the city me's modern face with innovation and technology-oriented exhibitions. Being an inspiring stop especially for young minds, the facility is an airy and high-quality educational point for those wanting to combine the city me's cosmopolitan energy with scientific discovery."
    },
    "ChIJzTOpABzpRxMRV0HmCyl-Brw": {
        "description": "Bari'nin modern semtlerinden birinde yükselen bu görkemli bazilika, kentin 20. yüzyıl dini mimarisinin ve ruhani bağlılığının önemli bir anıtıdır. Geniş iç mekanı, sanatsal pencereleri ve kentin sakin atmosferini yansıtan sessiz duruşuyla, kentin kozmopolit kalabalığından uzaklaşıp huzur bulabileceğiniz iddialı bir manevi duraktır.",
        "description_en": "Rising in one of Bari me's modern neighborhoods, this grand basilica is an important monument of the city me's 20th-century religious architecture and spiritual devotion. With its wide interior, artistic windows, and quiet posture reflecting the city me's calm atmosphere, it is an ambitious spiritual stop where you can move away from the cosmopolitan crowds and find peace."
    },
    "ChIJ0ZiAwWnoRxMRWav38xw11Pw": {
        "description": "Bari'nin en prestijli sanat galerisi olan Pinacoteca, 11. yüzyıldan günümüze Puglia sanatının gelişimini paha biçilemez bir koleksiyonla sergiliyor. Tarihi bir binanın çatı katında yer alan müze, kentin estetik gücünü ve sanatsal mirasını Akdeniz manzarası eşliğinde soluyabileceğiniz seçkin ve havadar bir sanat durağıdır.",
        "description_en": "Bari me's most prestigious art gallery, Pinacoteca, exhibits the development of Puglian art from the 11th century to today with a priceless collection. Located on the top floor of a historical building, the museum is an elite and airy art stop where you can breathe in the city me's aesthetic power and artistic heritage accompanied by Mediterranean views."
    },
    "ChIJmWuTK1voRxMRR1HtuZzmElk": {
        "description": "Kentin yerel dokusunda önemli bir yer tutan bu kilise, samimi atmosferi ve dini sanat eserleriyle kentin manevi hayatına ışık tutuyor. Geleneksel yapısı ve kentin sosyal tarihinde bıraktığı derin izlerle, hem yerel kültürü solumak hem de tarihin sessiz tanıklığını yapan köşeleri keşfetmek için ideal bir dini duraktır.",
        "description_en": "Holding an important place in the city me's local texture, this church sheds light on the city me's spiritual life with its intimate atmosphere and religious artworks. With its traditional structure and deep marks left in the city's social history, it is an ideal religious stop for both soaking in local culture and exploring corners that serve as silent witnesses to history."
    },
    "ChIJgw2ySq_pRxMRqlRQ7KULXAk": {
        "description": "Laura Grimaldi tarafından tasarlanan 'Stella Maris' duvar resmi, Bari'nin modern sokak sanatı kültürünün ve denizle olan romantik bağının en taze ifadesidir. Sanatsal derinliği ve kentin kozmopolit enerjisini yansıtan renkleriyle kentin kentsel silüetine sanatsal bir soluk getiren, dikkat çekici ve ilham verici bir duraktır.",
        "description_en": "The 'Stella Maris' mural designed by Laura Grimaldi is the freshest expression of Bari me's modern street art culture and its romantic connection with the sea. It is a remarkable and inspiring stop bringing an artistic breath to the city's urban silhouette with artistic depth and colors reflecting the city me's cosmopolitan energy."
    },
    "ChIJBwuO5lXpRxMRUbEtWy_jb_s": {
        "description": "Bari gece hayatının enerjik kalbi olan Demodé Club, alternatif müzik performansları ve neşeli atmosferiyle kentin en popüler eğlence adreslerinden biridir. Sanatsal etkinlikleri ve dünyanın her yerinden gelen müzisyenleri ağırlayan sosyal dokusuyla kentin yaratıcı ruhunu en yüksek seviyede hissedebileceğiniz dinamik bir duraktır.",
        "description_en": "The energetic heart of Bari nightlife, Demodé Club is one of the city me's most popular entertainment addresses with alternative music performances and a joyful atmosphere. It is a dynamic stop where you can feel the city me's creative spirit at its highest level with its social texture hosting artistic events and musicians from all over the world."
    },
    "ChIJx2A7y1foRxMR06E0uKGSEFY": {
        "description": "Kentin modern iş yaşamını ve organizasyon gücünü simgeleyen bu merkez, stratejik konumu ve profesyonel yaklaşımıyla kentin kozmopolit yüzünü temsil ediyor. Şık tasarımı ve kentsel dinamizme uyum sağlayan yapısıyla, kentin sadece bir tarih kenti değil, aynı zamanda modern bir vizyon merkezi olduğunu gösteren kaliteli bir duraktır.",
        "description_en": "Symbolizing the city's modern business life and organizational power, this center represents the city me's cosmopolitan face with its strategic location and professional approach. With its stylish design and structure harmonizing with urban dynamism, it is a high-quality stop showing that the city is not just a city of history but also a center of modern vision."
    },
    "ChIJB2HAvP_pRxMRJFPYp1nus4w": {
        "description": "Bari'nin genç ve dinamik kitlesini bir araya getiren Remake eSports Bar, modern eğlence kültürünü ve teknoloji tutkusunu samimi bir bar atmosferinde buluşturuyor. Neşeli sosyal yaşamın ve kaliteli sohbetlerin odağı olan mekan, kentin kozmopolit enerjisini dijital bir dünyayla keşfetmek isteyenler için havadar ve popüler bir tercihtir.",
        "description_en": "Bringing together Bari me's young and dynamic crowd, Remake eSports Bar meets modern entertainment culture and technology passion in a sincere bar atmosphere. Being a focal point of joyful social life and quality chats, the venue is an airy and popular choice for those wanting to explore the city me's cosmopolitan energy with a digital world."
    },
    "ChIJUxX469_pRxMRDNa1Y_UoaJM": {
        "description": "Kentin en neşeli ve Characteristic duraklarından olan KARA Bari, müzik ve sosyal bağların birleştiği enerjik bir eğlence noktasıdır. Kentin kozmopolit ritmini hissettiren atmosferi ve samimi servis anlayışıyla kentin gece hayatına havadar bir soluk getiren, arkadaş grupları için unutulmaz anılar vaat eden neşeli bir keşiştir.",
        "description_en": "One of the city's most joyful and characteristic stops, KARA Bari is an energetic entertainment point where music and social ties meet. It is a joyful discovery bringing an airy breath to the city's nightlife with an atmosphere making you feel the city's cosmopolitan rhythm and its sincere service concept, promising unforgettable memories for groups of friends."
    },
    "ChIJSVRYbgDpRxMRoLHada3ZYv0": {
        "description": "Bari'nin yerel bir efsanesi haline gelmiş bu sıra dışı ve esprili nokta, kentin neşeli sosyal dokusunu ve yerel mizah anlayışını yansıtır. Her köşesiyle kentin samimiyetini ve günlük yaşamın eğlenceli sürprizlerini barındıran bu bölge, kenti alışılmışın dışında bir bakış açısıyla keşfetmek isteyen gezginler için havadar ve merak uyandırıcı bir duraktır.",
        "description_en": "This unusual and humorous spot that has become a local legend in Bari reflects the city me's joyful social texture and local sense of humor. Containing the city's sincerity and daily life's fun surprises at every corner, this area is an airy and intriguing stop for travelers wanting to explore the city with an out-of-the-ordinary perspective."
    },
    "ChIJKb86E1_oRxMRYU9tWwZWrlc": {
        "description": "Uzak Doğu disiplinini Bari'nin kalbine taşıyan Kabuki, sanatsal tasarımı ve mistik atmosferiyle kentin en prestijli gurme duraklarından biridir. Modern ve sofistike tasarımının yanı sıra sunduğu yüksek kaliteli lezzet mönüsüyle kentin kozmopolit gastronomisini en şık haliyle yaşatan kaliteli ve havadar bir tecrübedir.",
        "description_en": "Carrying Far Eastern discipline to the heart of Bari, Kabuki is one of the city's most prestigious gourmet stops with its artistic design and mystical atmosphere. Beside its modern and sophisticated design, it's a high-quality and airy experience making you live the city's cosmopolitan gastronomy in its most stylish form with the high-quality flavor menu it offers."
    },
    "ChIJfScpcQDpRxMR8h9GF6fsz_Y": {
        "description": "Tiyatro, sinema ve sanatsal performansları tek bir çatı altında toplayan Anchecinema, Bari'nin yaratıcı zihinlerinin en aktif buluşma noktasıdır. Endüstriyel şıklığı ve kentin kozmopolit ruhuna derinlik katan etkinlikleriyle kentin modern sanat vizyonunu doyasıya soluyabileceğiniz iddialı ve ilham verici bir kültürel duraktır.",
        "description_en": "Gathering theater, cinema, and artistic performances under one roof, Anchecinema is the most active meeting point for Bari me's creative minds. It is an ambitious and inspiring cultural stop where you can fully breathe in the city's modern art vision with its industrial elegance and events adding depth to the city's cosmopolitan spirit."
    },
    "ChIJC9fZXVDoRxMRzFFJMNhEklM": {
        "description": "Bari Güzel Sanatlar Akademisi mezunlarını ve sanatseverleri bir araya getiren bu dernek, kentin köklü sanatsal mirasını geleceğe taşıyan önemli bir kültürel köprüdür. Sanat projeleri, sergiler ve yaratıcı atölyelerle kentin estetik gücünü hissedebileceğiniz, kendinizi kentin akademik ve sanatsal dokusunda bulabileceğiniz samimi bir merkezdir.",
        "description_en": "This association, bringing together Bari Academy of Fine Arts graduates and art lovers, is an important cultural bridge carrying the city me's deep-rooted artistic heritage to the future. It is a sincere center where you can feel the city's aesthetic power through art projects, exhibitions, and creative workshops, finding yourself in the city me's academic and artistic texture."
    },
    "ChIJFcl-8VDoRxMRaT7OBB4fUr0": {
        "description": "Eski kentin tarihi dokusu içerisinde yer alan bu şık saray, kentin kentsel gelişim sürecini ve aristokratik mimari tarzını yansıtan zarif dekoratif detaylarıyla bilinir. Taş duvarları ve nostaljik atmosferiyle kentin sosyal tarihini ve eski şehir yaşamının kalitesini hissetmek isteyenler için saklı ve havadar bir köşedir.",
        "description_en": "Located within the old town's historical texture, this stylish palace is known for its elegant decorative details reflecting the city me's urban development process and aristocratic architectural style. With stone walls and a nostalgic atmosphere, it is a hidden and airy corner for those wanting to feel the city's social history and the quality of old town life."
    },
    "ChIJN0o222noRxMRiSqXGrmUHVc": {
        "description": "Metro City, Bari'nin kentsel dinamizmini ve modern ulaşım ağının kozmopolit kalabalığını yansıtan havadar bir duraktır. Şık tasarımı ve kentin ana noktalarına hızlı erişim sağlayan yapısıyla Valensiya'nın pragmatik ve geleceğe dönük yüzünü temsil eden, kentin ritmini en yüksek seviyede hissedebileceğiniz kaliteli bir kesişim noktasıdır.",
        "description_en": "Metro City is an airy stop reflecting Bari me's urban dynamism and the cosmopolitan crowds of its modern transport network. With its stylish design and structure providing fast access to the city's main points, it is a high-quality intersection representing Valencia me's pragmatic and future-oriented face where you can feel the city me's rhythm at its highest level."
    },
    "ChIJrwJ6-mPoRxMR-uV7HX6IcY8": {
        "description": "Kentin tarihi merkezinde asude bir köşe olan bu kilise, Barok mimarisinin inceliklerini ve kentin manevi birikimini sade bir ihtişamla sunuyor. Mistik iç mekanı ve kenti sessiz bir tanık gibi izleyen yapısıyla kentin aristokratik köklerini ve ruhani derinliğini keşfetmek isteyenler için ideal ve havadar bir dini duraktır.",
        "description_en": "A serene corner in the city's historical center, this church offers the subtleties of Baroque architecture and binary's spiritual accumulation with simple grandeur. With its mystical interior and structure watching the city like a silent witness, it is an ideal and airy religious stop for those wanting to explore the city's aristocratic roots and spiritual depth."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/bari.json.draft'
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

print(f"✅ Bari enriched {count} items.")

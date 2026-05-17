#!/usr/bin/env python3
import json

updates = {
    "ChIJZeX1s9xIYA0Rdr_7evab_20": {
        "description": "Sanat ve Bilim Şehri yakınında yer alan A Tu Gusto, modern Akdeniz mutfağını yaratıcı bir dokunuşla sunan şık bir restorandır. Mevsimlik ürünlerle hazırlanan mönüsü, sanatsal sunumları ve minimalist dekorasyonuyla kentin fütüristik ruhuna gastronomi ile eşlik eden seçkin bir duraktır.",
        "description_en": "Located near the City of Arts and Sciences, A Tu Gusto is a stylish restaurant offering modern Mediterranean cuisine with a creative touch. With its menu prepared with seasonal products, artistic presentations, and minimalist decoration, it is an elite stop accompanying the city me's futuristic spirit with gastronomy."
    },
    "ChIJ99rmJEJIYA0RwtFOCEOGvaQ": {
        "description": "Valensiya'nın sahil şeridinde yer alan El Coso, denize sıfır konumu ve geleneksel İspanyol mimarisini yansıtan tasarımıyla kentin yaz ruhunu temsil eder. Taze deniz ürünleri ve meşhur Valensiya usulü pirinç yemekleriyle, Akdeniz güneşinin altında otantik bir ziyafet çekmek isteyenlerin yıllardır favori adresidir.",
        "description_en": "Located on Valencia's coastline, El Coso represents the city me's summer spirit with its seafront location and design reflecting traditional Spanish architecture. With fresh seafood and famous Valencian rice dishes, it has been the favorite address for years for those wanting an authentic feast under the Mediterranean sun."
    },
    "ChIJc_oc8VtPYA0RduISD8UlN_0": {
        "description": "Turia Bahçeleri'nin huzurlu manzarasını sunan bu otel, kentin ana ulaşım noktalarına yakın konumuyla pratik ve konforlu bir konaklama durağıdır. Sade ve işlevsel tasarımıyla öne çıkan tesis, Valensiya'nın hem tarihi merkezine hem de modern bölgelerine kolayca ulaşmak isteyen gezginler için havadar ve kaliteli bir tercihtir.",
        "description_en": "Offering peaceful views of the Turia Gardens, this hotel is a practical and comfortable accommodation stop with its location near the city's main transport points. Standing out with its simple and functional design, the facility is an airy and high-quality choice for travelers wanting to easily reach both Valencia's historical center and modern areas."
    },
    "ChIJQUA0BIxFYA0R_iiCZ10nOMM": {
        "description": "Valensiya'nın modern iş ve alışveriş bölgesinde yer alan bu tesis, şık ve enerjik tasarımıyla kozmopolit bir konaklama deneyimi sunuyor. Geniş pencereleri ve kentin fütüristik silüetini kucaklayan odalarıyla, Valensiya'nın dinamik ritmini hissetmek isteyen modern gezginler için kaliteli bir dinlenme noktasıdır.",
        "description_en": "Located in Valencia's modern business and shopping district, this facility offers a cosmopolitan accommodation experience with its stylish and energetic design. With large windows and rooms embracing the city's futuristic silhouette, it is a high-quality rest point for modern travelers wanting to feel Valencia me's dynamic rhythm."
    },
    "ChIJR6UGlEtPYA0RLO8qoS8OpZY": {
        "description": "Valensiya'nın gastronomi tarihinde bir klasik olan Restaurante Navarro, 1950'lerden beri kentin en iyi paella ve deniz ürünleri mönülerinden birini sunuyor. Geleneksel tariflerin modern bir zarafetle sunulduğu bu aile işletmesi, kentin yerel lezzet mirasını gerçek ve samimi bir atmosferde keşfetmek isteyenler için paha biçilemezdir.",
        "description_en": "A classic in Valencia me's gastronomic history, Restaurante Navarro has been offering one of the city's best paella and seafood menus since the 1950s. This family business, where traditional recipes are presented with modern elegance, is priceless for those wanting to explore the city me's local flavor heritage in a real and sincere atmosphere."
    },
    "ChIJx6gnh1lPYA0RdCV9WFcKS7M": {
        "description": "İspanya'nın en ikonik alışveriş merkezi olan El Corte Inglés, Valensiya'nın modern kalbinde, tüm ihtiyaçlarınızı bir arada sunan dev bir moda ve yaşam kompleksidir. En prestijli markalardan yerel delilere kadar geniş bir seçki sunan bu durak, kentin kozmopolit alışveriş kültürünü ve modern konforunu yansıtır.",
        "description_en": "Spain's most iconic shopping center, El Corte Inglés, is a giant fashion and lifestyle complex offering all your needs together in Valencia's modern heart. Offering a wide selection from the most prestigious brands to local delicacies, this stop reflects the city me's cosmopolitan shopping culture and modern comfort."
    },
    "ChIJIRgmmLdIYA0RZpX6MUMTVoE": {
        "description": "Valensiya usulü otantik mutfağın kentin merkezindeki en şık duraklarından biri olan Racó del Túria, sıcak taş duvarları ve geleneksel dekoruyla bilinir. Özellikle 'Pide a Banda' ve taze deniz ürünleriyle hazırlanan pirinç yemekleriyle gurme gezginlerin ve yerel halkın favorisi olan samimi bir gastronomi noktasıdır.",
        "description_en": "One of the most stylish stops for authentic Valencian cuisine in the city center, Racó del Túria is known for its warm stone walls and traditional decor. It is a sincere gastronomic spot that is a favorite of gourmet travelers and locals, especially with its 'Pide a Banda' and rice dishes prepared with fresh seafood."
    },
    "ChIJD0Op8jxGYA0R2p--3tSn9v0": {
        "description": "Valensiya'nın tatlı dünyasına modern ve yaratıcı bir soluk getiren La Sucrera, el yapımı pastaları ve sanatsal dokunuşları olan tatlılarıyla bir vaha niteliğindedir. Her biri taze malzemelerle hazırlanan ve adanın neşeli renklerini yansıtan bu eserler, kentin yerel pastane kültürünü modern bir estetikle birleştiren keyifli bir duraktır.",
        "description_en": "Bringing a modern and creative breath to Valencia's world of sweets, La Sucrera is like an oasis with its handmade cakes and sweets having artistic touches. These works, each prepared with fresh ingredients and reflecting the island's joyful colors, are a pleasant stop combining the city me's local bakery culture with a modern aesthetic."
    },
    "ChIJ_TB7W8tIYA0RehAJfTOFFVg": {
        "description": "Ruzafa bölgesinin bohem ruhunu temsil eden Ubik Café, binlerce kitabın arasında kahvenizi yudumlayabileceğiniz eşsiz bir kütüphane-kafedir. Sanatsal etkinlikleri, canlı müzik dinletileri ve entelektüel atmosferiyle kentin yaratıcı kitlesinin buluşma noktası olan bu mekan, samimiyet ve kültürün harika bir birleşimidir.",
        "description_en": "Representing the bohemian spirit of the Ruzafa area, Ubik Café is a unique library-cafe where you can sip your coffee among thousands of books. Being the meeting point for the city me's creative crowd with artistic events, live music performances, and an intellectual atmosphere, this venue is a wonderful combination of sincerity and culture."
    },
    "ChIJuUtWWv1FYA0RHda-Pfk23vg": {
        "description": "Malkebien, Akdeniz mutfağını modern ve minimalist bir yaklaşımla sunan, kentin gastronomi dünyasında kendine has bir yer edinmiş havadar bir restorandır. Yerel pazardan gelen taze ürünlerin usta ellerde sanata dönüştüğü mönüsüyle, kentin fütüristik ruhuna uyumlu kaliteli ve samimi bir yemek deneyimi vaat eder.",
        "description_en": "Malkebien is an airy restaurant that has carved out its own place in the city's gastronomic world, offering Mediterranean cuisine with a modern and minimalist approach. With its menu where fresh products from the local market are transformed into art in master hands, it promises a quality and sincere dining experience compatible with the city me's futuristic spirit."
    },
    "ChIJg89huyJGYA0RRsNidr8onlM": {
        "description": "Valensiya denilince akla gelen en meşhur içecek olan horchata'nın (yerli badem sütü alternatifi) efsanevi adresi Orxateria Daniel, asırlık tariflerini günümüze taşıyor. 'Fartons' adı verilen geleneksel çöreklerle ikram edilen bu eşsiz lezzet, kentin yerel damak tadını ve sosyal tarihini keşfetmek için paha biçilemez bir duraktır.",
        "description_en": "The legendary address of horchata (a local tiger nut milk alternative), Valencia's most famous drink, Orxateria Daniel brings century-old recipes to the present. Served with traditional buns called 'fartons', this unique flavor is a priceless stop for exploring the city me's local taste and social history."
    },
    "ChIJmeWytJBIYA0RFQLs_ogqaJM": {
        "description": "Geleneksel horchata kültürünü kentin modern yaşam tarzıyla birleştiren bu şık horchateria, taze malzemeleri ve samimi servis anlayışıyla bilinir. Valensiya güneşinin altında serinlemek ve adanın bu ferahlatıcı mirasını en doğal haliyle tatmak isteyenlerin, özellikle yaz akşamlarındaki vazgeçilmez yerel duraklarından biridir.",
        "description_en": "Combining traditional horchata culture with the city me's modern lifestyle, this stylish horchateria is known for its fresh ingredients and sincere service concept. It is one of the indispensable local stops, especially on summer evenings, for those wanting to cool off under the Valencia sun and taste this refreshing heritage of the island in its most natural form."
    },
    "ChIJZUFhME5PYA0RJ3UKxecoc9g": {
        "description": "Valensiya'nın kültürel gece hayatının ikonik adresi Radio City, sanatın, müziğin ve dansın her formunu tek bir çatı altında topluyor. Flamenko gecelerinden modern DJ performanslarına kadar geniş bir yelpaze sunan mekan, kentin kozmopolit ruhunu ve hiç bitmeyen sanatsal enerjisini en samimi haliyle yansıtan bir eğlence tapınağıdır.",
        "description_en": "Radio City, the iconic address of Valencia's cultural nightlife, gathers every form of art, music, and dance under one roof. Offering a wide range from flamenco nights to modern DJ performances, the venue is an entertainment temple reflecting the city's cosmopolitan spirit and never-ending artistic energy in its most sincere form."
    },
    "ChIJ8zYQAG9IYA0RHV6s79QZblU": {
        "description": "Malvarrosa plajının hemen yanında yer alan Akuarela, açık hava partileri ve Akdeniz meltemiyle kentin en enerjik gece hayatı duraklarından biridir. Palmiye ağaçları altındaki geniş terası ve sabahın ilk ışıklarına kadar süren neşeli atmosferiyle, Valensiya yazlarını dans ve müzikle taçlandırmak için en havalı ve popüler destinasyondur.",
        "description_en": "Located right next to Malvarrosa beach, Akuarela is one of the city's most energetic nightlife stops with open-air parties and the Mediterranean breeze. With its large terrace under palm trees and a cheerful atmosphere lasting until the first light of day, it's the coolest and most popular destination to crown Valencia summers with dance and music."
    },
    "ChIJwdPpA45IYA0R6T14rKRRPfQ": {
        "description": "Valensiya'nın modern ve sanatsal gece hayatına farklı bir soluk getiren Matisse Club, eklektik müzik seçkisi ve samimi tasarımıyla bilinir. Canlı cazdan elektronik tınılara uzanan zengin programıyla kentin yaratıcı kitlesini bir araya getiren mekan, kaliteli bir akşam geçirmek isteyenler için havadar ve ilham verici bir duraktır.",
        "description_en": "Bringing a different breath to Valencia's modern and artistic nightlife, Matisse Club is known for its eclectic music selection and sincere design. Bringing together the city me's creative crowd with its rich program ranging from live jazz to electronic tones, it is an airy and inspiring stop for those wanting to spend a high-quality evening."
    },
    "ChIJbYaFVo5IYA0RFKVxWvn-f-Y": {
        "description": "Kentin modern kitlelerinin favorisi olan Rumbo 144, enerjik dans pisti ve etkileyici DJ performanslarıyla İbiza atmosferini Valensiya'ya taşıyor. Çağdaş tasarımı ve sabahın ilk ışıklarına kadar süren neşeli atmosferiyle, kentin dinamik gece hayatını en yüksek seviyede hissedebileceğiniz iddialı ve popüler bir eğlence merkezidir.",
        "description_en": "A favorite of the city's modern crowds, Rumbo 144 brings the Ibiza atmosphere to Valencia with its energetic dance floor and impressive DJ performances. With contemporary design and a cheerful atmosphere lasting until the first light of morning, it is an ambitious and popular entertainment center where you can feel the city me's dynamic nightlife at its highest level."
    },
    "ChIJVR0NQ1VPYA0R89Km7ggQSUU": {
        "description": "Valensiya'nın kapsayıcı ve enerjik gece hayatının en önemli adreslerinden biri olan Deseo 54, görkemli şovları ve kaliteli pop-elektronik müzik seçkisiyle tanınır. Kentin kozmopolit ruhunu yansıtan kitleyi bir araya getiren kulüp, adanın hiç bitmeyen eğlence temposunu modern bir atmosferde yaşatan en havalı duraklardan biridir.",
        "description_en": "One of the most important addresses of Valencia me's inclusive and energetic nightlife, Deseo 54 is known for its grand shows and high-quality pop-electronic music selection. Bringing together a crowd that reflects the city's cosmopolitan spirit, the club is one of the coolest stops making the island's never-ending entertainment tempo live in a modern atmosphere."
    },
    "ChIJPa3pKFJPYA0R5ouaPtMgQ8k": {
        "description": "Eski kentin tarihi sokakları arasına gizlenmiş bu efsanevi caz barı, loş ışıkları ve antik taş duvarlarıyla gerçek bir 'New York' atmosferi sunuyor. Dünyaca ünlü caz sanatçılarının sahne aldığı Jimmy Glass, kentin entelektüel ve sanatsal ruhunu en rafine haliyle soluyabileceğiniz, her köşesi tarih dolu samimi bir mabettir.",
        "description_en": "Hidden among the narrow streets of the old town, this legendary jazz bar offers a real 'New York' atmosphere with its dim lights and ancient stone walls. Jimmy Glass, where world-famous jazz artists perform, is a sincere temple full of history at every corner where you can breathe in the city's intellectual and artistic spirit in its most refined form."
    },
    "ChIJY38uCkhPYA0RJ2ldssnNNE4": {
        "description": "Bohem şıklığı ve neşeli atmosferiyle kentin modern sosyal yaşamının kalbinde yer alan Apoquetanit, taze kokteylleri ve yerel lezzetleriyle bilinir. Samimi tasarımı ve havadar terasıyla kentin kozmopolit temposundan uzaklaşıp huzurlu ve kaliteli bir akşam geçirmek isteyenler için İbiza ruhunu kente taşıyan özel bir duraktır.",
        "description_en": "Located in the heart of the city me's modern social life with bohemian chic and a joyful atmosphere, Apoquetanit is known for its fresh cocktails and local flavors. With its sincere design and airy terrace, it's a special stop bringing the Ibiza spirit to the city for those wanting to move away from the city's cosmopolitan pace and spend a peaceful and high-quality evening."
    },
    "ChIJ4b_Bf0xPYA0R50CKSAiKWTk": {
        "description": "Valensiya'nın enerjik mahallelerinden birinde yer alan MClub, modern elektronik müzik tınılarını şık bir dekorasyonla birleştiriyor. Kaliteli ses sistemi ve seçkin DJ mönüsüyle kentin yaratıcı kitlesini bir araya getiren mekan, kentin kozmopolit gece hayatını daha samimi ve iddialı bir atmosferde yaşamak isteyenlerin favorisidir.",
        "description_en": "Located in one of Valencia's energetic neighborhoods, MClub combines modern electronic music tones with stylish decoration. Bringing together the city's creative crowd with its quality sound system and exclusive DJ menu, the venue is a favorite for those wanting to experience the city's cosmopolitan nightlife in a more intimate and ambitious atmosphere."
    },
    "ChIJdztGx0lPYA0Rs7Sl6sTeOrU": {
        "description": "Kentin iddialı gece kulüplerinden biri olan Indiana, üç farklı müzik tarzını tek bir çatı altında sunan devasa bir eğlence merkezidir. Modern tasarımı ve elit atmosferiyle Valensiya'nın dinamik gece hayatına yön veren mekan, etkileyici şovları ve kozmopolit kitlesiyle gecenin hiç bitmemesini isteyenlerin adresidir.",
        "description_en": "One of the city me's ambitious night clubs, Indiana is a massive entertainment center offering three different music styles under one roof. Guiding Valencia me's dynamic nightlife with modern design and an elite atmosphere, the venue is the address for those wanting the night never to end with its impressive shows and cosmopolitan crowd."
    },
    "ChIJu_jgGjZPYA0RDTOR9coQFng": {
        "description": "Tarihi bir sinema binasının muazzam bir eğlence merkezine dönüştürülmesiyle hayata geçen Jerusalem, yüksek tavanları ve nostaljik şıklığıyla büyüleyicidir. Pop, rock ve hit parçaların en kaliteli örneklerini enerjik bir atmosferde sunan kulüp, kentin nostalji ile modern eğlenceyi buluşturduğu en prestijli duraklardan biridir.",
        "description_en": "Brought to life by transforming a historical cinema building into a massive entertainment center, Jerusalem is fascinating with its high ceilings and nostalgic elegance. Offering high-quality examples of pop, rock, and hits in an energetic atmosphere, the club is one of the city's most prestigious stops where nostalgia meets modern entertainment."
    },
    "ChIJNVvh8LVIYA0RIuG6xW0RhN8": {
        "description": "İbiza tarzı açık hava kulüplerinin enerjisini Valensiya sahil şeridine taşıyan Bowie Show Disco, etkileyici sahne şovları ve enerjik DJ performanslarıyla tanınır. Deniz havası eşliğinde sabahın ilk ışıklarına kadar süren partileriyle kentin kozmopolit yaz neşesini en üst seviyede hissedebileceğiniz iddialı bir eğlence noktasıdır.",
        "description_en": "Carrying the energy of Ibiza-style open-air clubs to the Valencia coastline, Bowie Show Disco is known for its impressive stage shows and energetic DJ performances. It is an ambitious entertainment spot where you can feel the city me's cosmopolitan summer joy at its highest level with parties lasting until the first light of day accompanied by the sea breeze."
    },
    "ChIJQ0KiuFBPYA0RM6elkBxvxlI": {
        "description": "Valensiya Modern Sanat Enstitüsü (IVAM), İspanya'nın çağdaş sanat alanındaki en prestijli müzelerinden biridir. Julio González'in heykellerinden modern fotoğrafçılığa kadar geniş bir koleksiyon sunan müze, minimalist mimarisi ve avangart sergileriyle kentin sanatsal vizyonunu ve entelektüel gücünü temsil eden paha biçilemez bir duraktır.",
        "description_en": "The Valencia Institute of Modern Art (IVAM) is one of Spain's most prestigious museums in the field of contemporary art. Offering a wide collection from Julio González's sculptures to modern photography, the museum is a priceless stop representing the city's artistic vision and intellectual power with minimalist architecture and avant-garde exhibitions."
    },
    "ChIJafy3yE5PYA0RBMpDH8kVuG0": {
        "description": "Valensiya'nın 15. yüzyıldan kalma tarihi ipek borsası ve sanatına adanan bu müze, kentin tekstil tarihindeki devasa önemini gözler önüne seriyor. Restore edilmiş ipek tezgahları, paha biçilemez dokumalar ve kentin bir döneme damga vuran ipek loncası tarihiyle, kentin zengin ve elegan geçmişine tanıklık edebileceğiniz samimi bir miras durağıdır.",
        "description_en": "Dedicated to Valencia's historical silk exchange and art from the 15th century, this museum brings to light the city me's massive importance in textile history. With restored silk looms, priceless textiles, and the history of the silk guild that marked an era, it is a sincere heritage stop where you can witness the city's rich and elegant past."
    },
    "ChIJafy3yE5PYA0RrGPdp_-HASE": {
        "description": "İpek Müzesi (Silk Museum), Valensiya'nın İpek Yolu üzerindeki stratejik önemini ve kentin dünyaya ihraç ettiği sanatsal dokumaları anlatan paha biçilemez bir merkezdir. Sadece bir tekstil müzesi değil, aynı zamanda kentin mimari ve sosyal tarihini de içeren bu alan, kentin dününe dair zarif ve eğitici bir keşif noktasıdır.",
        "description_en": "The Silk Museum is a priceless center telling of Valencia me's strategic importance on the Silk Road and the artistic textiles the city exported to the world. Not just a textile museum, but also an area containing the city me's architectural and social history, it is an elegant and educational discovery point for the city me's past."
    },
    "ChIJv_3W7bJIYA0RZK4VewUjcA4": {
        "description": "Valensiya'nın en görkemli saraylarından biri olan Palau dels Valeriola, bugün kentin paha biçilemez sanat belgelerini ve sergilerini barındıran büyüleyici bir binadır. Barok mimarisinin asaletini ve kentin aristokratik köklerini yansıtan bu saray, sessiz avluları ve tarihi dokusuyla kentin en mistik ve keşfedilmeyi bekleyen köşe taşlarından biridir.",
        "description_en": "One of Valencia's most grand palaces, Palau dels Valeriola is a fascinating building today housing the city me's priceless art documents and exhibitions. Reflecting the nobility of Baroque architecture and the city's aristocratic roots, this palace is one of the city me's most mystical cornerstones waiting to be discovered with its quiet courtyards and historical texture."
    },
    "ChIJpajOEE5PYA0RGWvXonBklUs": {
        "description": "Gezgin ve sanatseverler için Valensiya'nın gizli hazinelerinden biri olan bu vakıf, kentin çağdaş sanat sahnesine derinlik katan önemli koleksiyonlara ev sahipliği yapıyor. Şık tasarımı ve modern sergileme teknikleriyle kentin hafızasını tazeleyen müze, Valensiya gezinize kalite ve entelektüel derinlik katan sessiz bir eğitim durağıdır.",
        "description_en": "One of Valencia's hidden treasures for travelers and art lovers, this foundation hosts important collections that add depth to the city me's contemporary art scene. Refreshing the city's memory with its stylish design and modern display techniques, the museum is a quiet educational stop that adds quality and intellectual depth to your Valencia trip."
    },
    "ChIJM6ZnOEVPYA0R3pQcCH3FeWc": {
        "description": "Valensiya'nın masalsı ve nostaljik dünyasına kapı aralayan bu ikonik yerleşke, kentin yerel efsanelerini ve dilden dile dolaşan hikayelerini koruyor. Adeta zamanın durduğu bu samimi köşe, kentin dünkü yüzünü merak eden gezginler için havadar, merak uyandırıcı ve kentin çocuk ruhunu yansıtan benzersiz bir keşif duraktır.",
        "description_en": "This iconic settlement opening a door to Valencia's fairytale and nostalgic world preserves the city's local legends and word-of-mouth stories. This sincere corner where time practically stands still is a unique discovery stop for travelers curious about the city me's past, reflecting the city's child spirit while being airy and intriguing."
    },
    "ChIJezaHTK5IYA0R7JgVQoLs2Gg": {
        "description": "Eski bir manastırın görkemli binasında yer alan Valensiya Güzel Sanatlar Müzesi, El Greco ve Velázquez gibi devlerin eserleriyle İspanya'nın en önemli müzelerinden biridir. Mavi kubbesi ve dingin avlularıyla kentin sanat zirvesini temsil eden bu müze, kentin estetik gücünü ve köklü kültürel birikimini keşfetmek için paha biçilemez bir duraktır.",
        "description_en": "Located in a grand former monastery building, the Museum of Fine Arts of Valencia is one of Spain's most significant museums with works by giants like El Greco and Velázquez. Representing the city's artistic peak with its blue dome and serene courtyards, this museum is a priceless stop for exploring the city's aesthetic power and deep-rooted cultural accumulation."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/valencia.json.draft'
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

print(f"✅ Valencia Part 2: Enriched {count} items.")

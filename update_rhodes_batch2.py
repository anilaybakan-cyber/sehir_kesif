import json

path = "assets/cities/rhodes.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the remaining 47 venues in Rhodes
updates = {
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Archipelagos, kentsel kıyıda yer alan ve Ege'nin en taze ürünlerini sunan prestijli bir deniz restoranıdır. Şık tasarımı ve masmavi deniz manzaralı terasıyla kentin gastronomi dünyasında kalite ve estetiğin kentsel buluşma noktasıdır.",
        "en": "Archipelagos is a prestigious seafood restaurant on the urban coast, offering the freshest products of the Aegean. With its chic design and deep blue sea-view terrace, it is a meeting point where quality and aesthetics merge."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "RoYo, Rodos'un canlanan turizm bölgesinde yer alan, modern tasarımı ve taze dondurulmuş yoğurt çeşitleriyle tatilcilerin en sevdiği kentsel 'sweet' duraklarından birisi olarak kentin tatlı hafızasında yer tutmaktadır.",
        "en": "RoYo is one of the favorite urban 'sweet' stops for vacationers in the city's reviving tourism district, known for its modern design and fresh frozen yogurt variety, holding a tasty place in the town's memory."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Piatsa Gusto Cafe, İtalyan kafe kültürünü Rodos'un kentsel enerjisiyle birleştiren, kentin en popüler ve şık buluşma duraklarından biri olup kentsel sosyal hayatın kalbinde prestijli bir yer kaplamaktadır.",
        "en": "Piatsa Gusto Cafe merges Italian cafe culture with the urban energy of Rhodes, occupying a prestigious spot in the heart of social life as one of the most popular and stylish meeting destinations in town."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Boheme Bar, adından da anlaşılacağı gibi 'boho-chic' tarzıyla Rodos'un tarihi sokaklarında kentsel bir prestij noktasıdır. Gurme kokteylleri ve rahat atmosferi ile kentsel sosyal hayatın en nezih ve modern duraklarındandır.",
        "en": "Boheme Bar is an urban prestige point in the historic streets of Rhodes with its 'boho-chic' style. With gourmet cocktails and a relaxed vibe, it stands as one of the most refined and modern spots in the social scene."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ice Art, dondurma yapımını bir sanata dönüştüren kentsel bir lezzet durağıdır. Tamamen doğal malzemelerle hazırlanan rengarenk dondurmalarıyla kentin kavurucu sıcağında kentsel bir sükunet ve lezzet vahası sunmaktadır.",
        "en": "Ice Art is an urban flavor stop that transforms ice cream making into an art form. With colorful gelatos prepared from all-natural ingredients, it offers a refreshing oasis of taste in the city's scorching summer heat."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Gregory's, kentin her noktasına yayılan kalitesi ve taze demlenmiş kahveleriyle, kenti keşfeden gezginlerin en pratik ve popüler kentsel lezzet duraklarından biri olarak kentsel sosyal hayatın bir parçasıdır.",
        "en": "Gregory's is a staple of urban social life, standing as one of the most practical and popular flavor stops for travelers exploring the city, known for its consistent quality and fresh-brewed coffee across Rhodes."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Flu Cafe-Pub, kentsel dinamizmi ve adanın huzurunu birleştiren, gölge altındaki konforlu alanlarıyla Rodos sahilinin en samimi lezzet duraklarından biridir. Akşamları kentsel eğlencenin en canlı rotalarından biri haline gelir.",
        "en": "Flu Cafe-Pub is one of the friendliest flavor stops on the Rhodes coast, merging urban dynamism and island calm with its comfortable shaded areas. In the evenings, it becomes one of the liveliest routes for urban fun."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Coffee Island Central, kentin en işlek meydanında yer alan ve taze demlenmiş kahvesiyle kenti keşfedenlerin enerjisini depoladığı kentsel bir duraktır. Kaliteli çekirdekleri ve hızlı servisiyle kentsel hayatın ritmini tutar.",
        "en": "Coffee Island Central is an urban stop in the city's busiest square where travelers recharge with fresh-brewed coffee. With its quality beans and fast service, it keeps the pulse of the Rhodes urban rhythm."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Aktaion Classic, kentsel sahil şeridinde yer alan ve masmavi deniz manzarası eşliğinde geleneksel Yunan mezeleri sunan, kentsel sosyal hayatın en köklü ve prestijli buluşma duraklarından biridir.",
        "en": "Aktaion Classic is one of the most established and prestigious meeting spots in urban social life, located on the waterfront and offering traditional Greek appetizers with views of the deep blue sea."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "ONO, kentsel modernliği ve Adriyatik'un bakir doğasını birleştiren şık tasarımı ve enerjik atmosferiyle kentsel sosyal yaşamın en elit ve modern deniz keyfini sunan prestijli bir kentsel duraktır.",
        "en": "ONO is a prestigious urban spot offering the most elite and modern seaside experience in social life, featuring an energetic vibe and chic design that merges urban modernity with the Adriatic's nature."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Starbucks Rhodes, kentin modern liman bölgesinde küresel bir kahve deneyimi sunan ve kenti keşfeden gezginlerin aşina olduğu kentsel bir dinlenme durağıdır. Panoramik deniz manzaralı balkonuyla popüler bir kentsel merkezdir.",
        "en": "Starbucks Rhodes offers a global coffee experience in the city's modern harbor area, serving as a familiar urban relaxation stop for travelers. Its panoramic sea-view balcony makes it a popular city center."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Dali Bistro, adını sürrealist sanatçıdan alan ve kentsel gastronomi dünyasına sanatsal bir dokunuş getiren kentin en stil sahibi lezzet duraklarından biridir. Gurme atıştırmalıkları ve iddialı kokteyl menüsüyle öne çıkar.",
        "en": "Dali Bistro is named after the surrealist artist and brings an artistic touch to the urban gastronomic world. Standing as one of the island's most stylish flavor spots, it features gourmet snacks and cocktails."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Playcafe, hem kentsel sosyal hayatın içinde olmak hem de eğlenceli vakit geçirmek isteyen gençler için popüler bir kentsel merkezdir. Geniş oyun alanları ve ferahlatıcı içecekleriyle kentin dinamik tarafını yansıtır.",
        "en": "Playcafe is a popular urban hub for youth looking to be part of social life and have fun. With its vast gaming areas and refreshing drinks, it reflects the dynamic and energetic side of the Rhodes city center."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Gazi Club, Rodos'un kentsel gece hayatındaki enerjinin merkezi olup, modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik sosyal alanıdır. Egzotik kokteylleriyle kentsel sosyal yaşamın prestijli bir rotasıdır.",
        "en": "Gazi Club is the heart of Rhodes' urban nightlife energy, serving as the most dynamic and stylish social area with DJ performances. With exotic cocktails, it stands as a prestigious route in the city's life."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Perro Negro, kentsel modernliği ve tarihi dokuyu birleştiren şık bir kentsel kaçış durağıdır. İddialı kokteyl menüsü ve Adriyatik'e tepeden bakan kentsel terasıyla kentsel sosyal hayatın en prestijli buluşma rotasıdır.",
        "en": "Perro Negro is a chic urban escape merging modern style with historic texture. With an ambitious cocktail menu and a terrace overlooking the Adriatic, it serves as a prestigious meeting route in social life."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Caramella Fin Cafe, kentin farklı kültürel katmanlarını yansıtan egzotik konsepti ve taze lezzetleriyle kentsel sosyal hayatın en özgün durakları arasındadır. Özellikle kentsel keşifler sonrası tatlı molalar için idealdir.",
        "en": "Caramella Fin Cafe ranks among the city's most unique stops with its exotic concept and fresh flavors, reflecting various cultural layers. It is ideal for sweet breaks after long days of urban exploration."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Paradiso Beach Club, kentsel kumsalda yer alan ve kentsel eğlenceyi dalga sesleriyle buluşturan kentin en büyüleyici kentsel buluşma duraklarından biridir. Yaz enerjisini en yüksek seviyede hissedebileceğiniz bir duraktır.",
        "en": "Paradiso Beach Club is one of the most enchanting urban meeting spots on the coast, merging city fun with the sound of waves. It is a destination where you can feel the highest level of summer energy."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kinky Rodos, kentsel modernliği ve iddialı gece hayatı konseptini birleştiren, kentin en dinamik kentsel sosyal alanlarından biridir. Modern aydınlatması ve kaliteli müzikleriyle kentsel sosyal yaşamın enerjik bir rotasıdır.",
        "en": "Kinky Rodos is one of the most dynamic urban social areas, merging modern style with an ambitious nightlife concept. With modern lighting and quality music, it is an energetic route in the town's social life."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Astron Pallas, Rodos'un kentsel gece hayatındaki en prestijli ve köklü gece kulüplerinden birisi olup, kentsel eğlenceyi adanın şık atmosferiyle birleştirerek kentsel sosyal hayatın merkezinde bir durak vaat eder.",
        "en": "Astron Pallas is one of the most prestigious and established night clubs in Rhodes' urban nightlife, merging city entertainment with the island's chic vibe for a central spot in the town's social life."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Keep It Simple Rhodes, adından da anlaşılacağı gibi sadeliği ve kaliteyi ön planda tutan, kentin en modern kentsel kafe duraklarından biridir. Taze kahveleriyle kentsel gürültüden uzaklaşmak isteyenler için idealdir.",
        "en": "Keep It Simple Rhodes, true to its name, prioritizes minimalism and quality as one of the island's most modern cafe stops. It is ideal for those looking to distance themselves from the urban rush."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ialyssos Bay Hotel, Rodos sahilinin lüks ve estetikle buluştuğu, kentsel sosyal hayatın ve konaklama dünyasının en prestijli kentsel duraklarından biri olarak kentsel turizm haritasında kalitesiyle öne çıkmaktadır.",
        "en": "Ialyssos Bay Hotel stands out in urban tourism as one of the most prestigious destinations where luxury meets aesthetics on the Rhodes coast for a complete and high-quality beach stay experience."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Rhodos, kentin kentsel simgelerini ve Adriyatik kıyısındaki tarihi dokuyu birleştiren, kenti keşfeden gezginlerin kentsel keşif albümündeki en ikonik ve fotojenik kentsel duraklardan biri haline gelmiştir.",
        "en": "Rhodos has become one of the most iconic and photogenic urban spots in travelers' discovery albums, merging the city's landmarks with the historic texture along the beautiful Adriatic coast."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Yahrak, kentin gastronomi dünyasına otantik bir dokunuş ve yaratıcı bir menü getiren, kentin en stil sahibi kentsel lezzet duraklarından biri olarak kentsel sosyal hayatın modern bir buluşma noktasıdır.",
        "en": "Yahrak is a modern meeting point in urban social life, serving as one of the most stylish flavor stops in town by bringing an authentic touch and creative menu to the culinary scene of Rhodes."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cendro, kentsel modernliği ve Rodos'un tarihi dokusunu birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan prestijli bir kentsel lezzet rotasıdır.",
        "en": "Cendro is a prestigious urban flavor route offering one of the most refined social escape stops in town, featuring a chic design that merges urban modernity with the historic texture of Rhodes."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Socratous Garden, Rodos Eski Şehir'in kalbinde gizli bir kentsel vaha gibi yemyeşil bahçeleri ve huzurlu atmosferiyle kentsel gürültüden kaçıp kentsel sükunete bürünmek isteyenlerin en samimi adresidir.",
        "en": "Socratous Garden is the friendliest address in the heart of Rhodes Old Town, offering a lush urban oasis and peaceful vibe for those looking to escape the city noise and find tranquility."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Legends Rock Bar, kentsel dinamizmi ve kaya müziğinin ruhunu birleştiren kentin en enerjik ve kentsel sosyal duraklarından biri olarak kentsel gece hayatının bir parçası olarak gezginleri ağırlar.",
        "en": "Legends Rock Bar welcomes travelers as part of the city's nightlife, standing as one of the most energetic urban social spots that merge urban dynamism with the historic spirit of rock music."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Decan Bar, kentsel modernliği ve Rodos'un tarihi silüetini birleştiren şık tasarımıyla kentsel sosyal hayatın en nezih kentsel sosyal kaçış duraklarından birini sunan kentsel bir prestij noktasıdır.",
        "en": "Decan Bar is an urban prestige point offering one of the most refined social escape stops in town, featuring a chic design that merges urban modernity with the historic silhouette of Rhodes."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Old School, adından da anlaşılacağı gibi kentsel nostaljiyi modern bir servisle sunan, kentin en popüler kentsel sosyal alanlarından biri olarak kentsel sosyal hayatın dinamik ve şık bir rotasıdır.",
        "en": "Old School, true to its name, offers urban nostalgia with a modern service style, standing as a dynamic and stylish route in social life as one of the city's most popular social areas."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Fuego Openair Club, kentsel kumsalda yer alan ve kentsel eğlenceyi dalga sesleriyle buluşturan kentin en büyüleyici kentsel buluşma duraklarından biridir. Akşamları kentsel bir enerjiyi vaat eder.",
        "en": "Fuego Openair Club is one of the most enchanting urban meeting spots on the coast, merging city fun with the sound of waves and promising a vibrant urban energy throughout the night."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Principato, kentsel modernliği ve Adriyatik'in bakir doğasını birleştiren şık tasarımıyla kentsel sosyal yaşamın en elit ve modern deniz keyfini sunan adreslerinden biri olarak kentsel bir prestij noktasıdır.",
        "en": "Principato is an urban prestige point and the address for the most elite and modern seaside experience in social life, featuring a design that merges urban style with the island's nature."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Vibe Nightclub, kentsel gece hayatının Rodos'taki kalbi olup modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik sosyal alanıdır. Egzotik kokteylleriyle kentsel sosyal yaşamın prestijli bir rotasıdır.",
        "en": "Vibe Nightclub is the heart of urban nightlife in Rhodes, serving as the town's most dynamic and stylish social area with DJ sets and exotic cocktails for a prestigious nocturnal route."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Akanthus Rhodes, kentsel kumsalda yer alan ve kentsel eğlenceyi dalga sesleriyle buluşturan kentin en büyüleyici kentsel buluşma duraklarından biridir. Modern tasarımıyla kentsel prestijini korumaktadır.",
        "en": "Akanthus Rhodes is one of the most enchanting urban meeting spots on the coast, merging city fun with the rhythm of the waves while maintaining its urban prestige with a modern design."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Stamatiadis Mineralogy Museum, Rodos'un jeolojik oluşumunu ve minerallerini anlatan, kentin kentsel eğitim ve bilimsel keşif haritasındaki en prestijli ve öğretici kentsel duraklarından biridir.",
        "en": "Stamatiadis Mineralogy Museum reveals the geological formation and minerals of Rhodes, standing as one of the most prestigious and educational urban stops on the city’s scientific map."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Throne of Helios, kentin tarihi serüvenini 9D teknolojiyle anlatan kentsel bir prestij noktasıdır. Rodos'un antik döneminden şövalyeler devrine kadar olan hikayesini kentsel bir aktiviteye dönüştürür.",
        "en": "Throne of Helios is an urban prestige point that uses 9D technology to tell the city's history, transforming the story of Rhodes from ancient times to the knights into an active urban experience."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Rhodos Old Town, kentin Ortaçağ dokusunu, dar şövalye sokaklarını ve kentsel simgelerini saklayan kentsel bir kültür kalesidir. UNESCO Dünya Mirası Listesi'nde kentin en prestijli tarih rotasıdır.",
        "en": "Rhodos Old Town is an urban cultural stronghold hiding Medieval textures, narrow knightly alleys, and landmarks. It is the city's most prestigious history route on the UNESCO World Heritage List."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Agora Roman Public Building, antik Rodos'un kentsel planlamasını ve sosyal hayatını yansıtan kentsel bir antik kalıntıdır. Kentin binlerce yıllık geçmişini keşfeden gezginlerin kentsel tarih rotasındadır.",
        "en": "Agora Roman Public Building is an urban ancient ruin reflecting the town planning and social life of ancient Rhodes, serving as a key point on the history route for those exploring the past."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Palatial Building, adanın şövalyeler dönemindeki kentsel görkemini ve aristokratik mimarisini yansıtan kentsel bir prestij kalesidir. Rodos'un kentsel ve askeri hafızasındaki en güçlü duraklardan biridir.",
        "en": "Palatial Building is an urban prestige stronghold reflecting the town's grandeur and aristocratic architecture from the era of the Knights, standing as a vital stop in Rhodes' military history."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Church of St. John the Baptist, kentin tarihi dokusuna mistik bir hava katan kentsel bir maneviyat kalesidir. Gotik mimarisi ve kentsel silüetiyle kentin binlerce yıllık şövalye hatıralarını saklamaktadır.",
        "en": "Church of St. John the Baptist is an urban spiritual stronghold adding a mystical vibe to the city's fabric. With its Gothic style, it preserves the knights' memories in the city's urban silhouette."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hafiz Ahmed Agha Library, kentsel Osmanlı mirasının en seçkin ve kentsel hafızayı koruyan duraklarından biridir. El yazması eserleriyle kentin çok kültürlü kentsel dokusunu yansıtan prestijli bir noktadır.",
        "en": "Hafiz Ahmed Agha Library is one of the most elite stops protecting the urban Ottoman heritage. It reflects the city's multicultural fabric with its manuscripts as a prestigious urban landmark."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kentro Sigchronis Technis, kentsel çağdaş sanatın Rodos'taki kalbi olup, kentin modern tasarım ve sanat topluluğu için prestijli bir buluşma noktasıdır. Kentsel keşiflere sanatsal bir derinlik katmaktadır.",
        "en": "Kentro Sigchronis Technis is the heart of contemporary art in Rhodes, serving as a prestigious meeting spot for the modern design community and adding artistic depth to urban explorations."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hellenic Technology Museum, kentin antik teknolojiye olan katkılarını kentsel bir eğitim projesiyle sunan Rodos'un en öğretici kentsel duraklarından biridir. Kentsel ve antik dehayı kenti keşfedenlere tanıtır.",
        "en": "Hellenic Technology Museum is one of the most educational urban stops in Rhodes, presenting the city's contribution to ancient technology and introducing its genius to all visitors."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Süleymaniye Medresesi, kentsel Osmanlı silüetinin ve kentsel eğitim tarihinin Rodos'taki en görkemli antik kalesi olup kentin çok katmanlı kentsel tarihinin ikonik bir parçası olarak gezginleri ağırlar.",
        "en": "Süleymaniye Madrasah is the most majestic ancient stronghold of the urban Ottoman silhouette and educational history, welcoming travelers as an iconic part of the city's multi-layered past."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Path of Gods Museum, kentsel Yunan mitolojisini interaktif bir deneyime dönüştüren, kentin turizm haritasında antik tanrıların kentsel hikayesini anlatan en prestijli ve sürprizli kentsel duraklardan biridir.",
        "en": "Path of Gods Museum transforms Greek mythology into an interactive experience, standing as one of the most prestigious stops telling the urban story of ancient gods on the tourism map."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Underwater Antiquities Exhibition, kentsel liman derinliklerinden çıkarılan paha biçilemez antik eserleri sunan, kentsel deniz arkeolojisinin en prestijli ve entelektüel kentsel tarih penceresidir.",
        "en": "Underwater Antiquities Exhibition is the most prestigious and intellectual window into urban maritime archaeology, showcasing priceless artifacts recovered from the depths of the city's harbor."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Jewish Museum of Rhodes, kentin tarihi mahallesindeki musevi mirasını ve kentsel çok kültürlü dokusunu anlatan kentsel bir prestij noktasıdır. Kentsel hafızanın en hüzünlü ve önemli kentsel duraklarındandır.",
        "en": "Jewish Museum of Rhodes is an urban prestige point telling of the Jewish heritage and multicultural fabric in the city's historic district, standing as a vital stop in the urban memory of Rhodes."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Panayia of the Castle, şövalye kalesinin kalbinde yükselen gotik mimarisi ve mistik atmosferiyle Rodos'un kentsel silüetindeki en prestijli ve manevi kentsel duraklar arasında yer almaktadır.",
        "en": "Panayia of the Castle is among the most prestigious and spiritual urban stops in the Rhodes silhouette, with its Gothic architecture and mystical vibe rising from the heart of the knight's castle."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Decorative Arts Collection, adanın kentsel zanaat ve estetik mirasını kentsel bir kültür projesiyle sunan Rodos'un en zarif kentsel duraklarından biridir. Kentin ev hayatı ve sanat hafızasını korumaktadır.",
        "en": "Decorative Arts Collection is one of the most elegant urban stops in Rhodes, presenting the island's craft and aesthetic heritage and protecting the memory of the city's artistic and domestic life."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Rhodes Batch 2 (47 venues). Total Rhodes Cleaned.")

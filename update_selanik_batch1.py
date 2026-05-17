import json

path = "assets/cities/selanik.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the first 42 venues in Selanik
updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Ano Poli (Eski Şehir), Selanik'in en yüksek noktasında yer alan ve kentin kentsel silüetini ve limanı panoramik olarak izleyebileceğiniz kentsel bir tarih kalesidir. Arnavut kaldırımlı sokakları ve Bizans surlarıyla kentin en otantik rotasıdır.",
        "en": "Ano Poli (Old Town) is Thessaloniki's highest point, offering panoramic views of the urban silhouette and harbor. With its cobblestone streets and Byzantine walls, it stands as the city's most authentic and historic route."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "Rotonda, Roma imparatoru Galerius tarafından yaptırılan ve kentin en eski kentsel yapılarından biri olan kentsel bir prestij noktasıdır. Hem cami hem de kilise olarak kullanılan bu anıt, kentin çok katmanlı kentsel hafızasını yansıtır.",
        "en": "The Rotunda is an urban prestige point commissioned by Emperor Galerius and stands as one of the city's oldest structures. Used as both a mosque and a church, this monument reflects Thessaloniki's multi-layered urban memory."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "Aziz Dimitrios Kilisesi, Selanik'in koruyucu azizine adanmış kentsel bir maneviyat kalesidir. UNESCO Dünya Mirası Listesi'ndeki bu bazilika, kentsel Bizans sanatının ve kentsel mozaik kültürünün en seçkin örneklerini saklamaktadır.",
        "en": "Church of Saint Demetrius is an urban spiritual stronghold dedicated to the patron saint of Thessaloniki. This UNESCO-listed basilica preserves elite examples of Byzantine art and urban mosaic culture."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Ladadika, kentsel liman bölgesindeki tarihi depoların restore edilmesiyle hayat bulan kentin en renkli ve popüler gastronomi ve eğlence mahallesidir. Kentsel sosyal hayatın ve lezzet duraklarının kalbi burada atar.",
        "en": "Ladadika is a vibrant neighborhood brought to life by restoring historic warehouses in the harbor area. It serves as the heart of the city's social life and culinary destinations for every urban explorer."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Selanik Arkeoloji Müzesi, merkezi kentsel konumuyla kentin antik Makedonya ve Roma dönemlerine ait paha biçilemez altın takılar ve heykellere ev sahipliği yapan en prestijli kentsel kültür merkezlerinden biridir.",
        "en": "Archaeological Museum of Thessaloniki is a prestigious urban center housing priceless gold jewelry and statues from the ancient Macedonian and Roman eras, centrally located for urban historical discovery."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Bizans Kültürü Müzesi, kentsel mimarisiyle ödül almış modern binasında, kentin bin yılı aşkın kentsel Bizans mirasını ikonalar ve günlük eşyalarla anlatan kentsel bir tarih ve sanat noktasıdır.",
        "en": "Museum of Byzantine Civilization stands in an award-winning modern building, detailing the city's millennia-old urban Byzantine heritage through icons and artifacts as a leading urban history and art spot."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Heptapyrgion (Yedi Kule), kentin Ano Poli bölgesindeki kentsel zirvesinde yer alan ve bir zamanlar hapishane olarak da kullanılan Rodos ve Bizans kentsel savunma mimarisinin en güçlü kentsel kalesidir.",
        "en": "Heptapyrgion (Seven Towers) is the strongest urban fortress in the Ano Poli district, once used as a prison and representing the peak of Byzantine and urban defensive architecture in Thessaloniki."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hamza Bey Camii (Alcazar), kentsel Osmanlı silüetinin ve kentsel ticaret tarihinin en önemli duraklarından biridir. Kentin farklı inançların kentsel bir arada yaşama kültürünü yansıtan sembolik bir kentsel duraktır.",
        "en": "Hamza Bey Mosque (Alcazar) is a key landmark of the city's Ottoman silhouette and commercial history, reflecting the symbolic urban coexistence of different faiths throughout the centuries."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Atatürk Evi Müzesi, Türkiye Cumhuriyeti'nin kurucusu kentsel lider Mustafa Kemal Atatürk'ün doğduğu yer olup, kentin en çok ziyaret edilen kentsel tarihi ve diplomatik kentsel duraklarından biridir.",
        "en": "Atatürk Museum is the birthplace of Mustafa Kemal Atatürk, the founder of modern Turkey, standing as one of the city's most visited and significant urban historical and diplomatic landmarks."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kapani Pazarı, kentsel hayatın ritmini en doğal haliyle hissedeceğiniz, taze yerel ürünlerin ve kentsel seslerin iç içe geçtiği Selanik'in en köklü ve kentsel gastronomik pazar alanıdır.",
        "en": "Kapani Market is Thessaloniki's oldest urban gastronomic market area, where you can feel the natural pulse of city life amidst fresh local produce and vibrant urban sounds and colors."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "MOMus Modern Sanat Müzesi (Kostakis Koleksiyonu), kentsel Rus avangart sanatının dünyadaki en önemli seçkilerine ev sahipliği yapan kentin en prestijli kentsel ve çağdaş sanat kalesidir.",
        "en": "MOMus Museum of Modern Art holds one of the world's most significant selections of Russian avant-garde art, standing as a prestigious urban and contemporary art stronghold in the city center."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Lazaristes Manastırı, kentsel sanat topluluklarının ve tiyatro festivallerinin buluşma noktası olan, tarihi kentsel dokusuyla kentin kuzeyindeki en önemli kentsel kültür ve dinlenme merkezidir.",
        "en": "Lazaristes Monastery is a hub for urban art communities and theater festivals, serving as a key culture and relaxation center in the city's north with its unique historic urban fabric."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hosios David Kilisesi, kentsel Ano Poli sokaklarında gizlenmiş ve 5. yüzyıldan kalan paha biçilemez kentsel mozaikleriyle kentin en mistik ve kentsel Bizans mirası kentsel kalesidir.",
        "en": "Holy Church of Hosios David is a mystical urban Byzantine heritage site hidden in the streets of Ano Poli, featuring priceless 5th-century urban mosaics and a tranquil historic vibe."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Selanik Sinema Müzesi, liman bölgesindeki tarihi bir depoda yer alan ve kentsel film tarihini interaktif bir deneyime dönüştüren, kentin kentsel kültürel hafızasındaki en popüler kentsel duraklardır.",
        "en": "Thessaloniki Cinema Museum is located in a historic harbor warehouse, transforming urban film history into an interactive experience as a popular landmark in the city's cultural memory."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Yeni Camii, kentin dönme (Donmeh) cemaati için inşa edilmiş ve kentsel mimarisiyle eklektik bir tarz sunan, kentin kentsel silüetindeki en estetik ve prestijli kentsel tarih duraklarından biridir.",
        "en": "Yeni Mosque was built for the city's Donmeh community, featuring an eclectic urban architectural style that stands as an aesthetic and prestigious historic landmark in the city silhouette."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Alaca İmaret, kentsel Osmanlı eğitim ve sosyal yardım tarihini anlatan, mimarisindeki kentsel bezemeleriyle kentin çok kültürlü kentsel hafızasındaki en sanatsal kentsel duraklardan biridir.",
        "en": "Aladja Imaret tells the story of urban Ottoman education and social welfare history, standing as an artistic landmark representing the city's multicultural urban memory with its decorations."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Telloglou Sanat Vakfı, kentin kentsel sanat topluluğu için modern sergi alanları sunan, kentin çağdaş kentsel gelişimi ve kültürel prestijini yansıtan en önemli kentsel sanat merkezlerinden biridir.",
        "en": "Telliglou House is a key urban art center offering modern exhibition spaces for the city's creative community, reflecting Thessaloniki's contemporary growth and cultural prestige today."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Paşa Bahçeleri, Ano Poli'nin eteklerinde yer alan mistik taş yapıları ve panoramik deniz manzaralı kentsel teraslarıyla kentin gizli kalmış bir kentsel vaha ve dinlenme duraklarından biridir.",
        "en": "Pasha’s Gardens is a hidden urban oasis at the edge of Ano Poli, with mystical stone structures and terraces offering panoramic sea views for a peaceful break from the city rush."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Radyo Müzesi, kentsel iletişim tarihini ve teknolojinin kentsel gelişime olan etkisini anlatan, kenti keşfeden gezginlerin kentsel keşif haritasındaki en sürprizli kentsel duraklardan biridir.",
        "en": "Radio Museum details the history of urban communication and technology's role in the city's growth, standing as a surprising and educational landmark on the urban discovery map of Rhodes."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Stefanos Dragoumis Amfitiyatrosu, Bizans Kültürü Müzesi'nin kalbinde yer alan ve kentsel konserlerin ve kentsel festivallerin ruhunu yaşatan kentin en entelektüel kentsel performans alanıdır.",
        "en": "Stefanos Dragoumis Amphitheater is an intellectual urban performance space at the heart of the Byzantine Museum, keeping the spirit of city concerts and festivals alive for every visitor."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Selanik Olimpiyat Müzesi, kentsel spor tarihini ve sporun kentsel gelişime katkısını anlatan, kentin hem kentsel hem de atletik hafızasındaki en prestijli kentsel eğitim duraklarından biridir.",
        "en": "Olympic Museum is a prestigious urban educational landmark in the city center, telling the story of sports history and its vital contribution to Thessaloniki's growth and athletic identity."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Makedonya-Trakya Halk Bilimi Müzesi, kentsel mimarinin incisi Villa Modiano binasında kentsel yerel mirası ve gelenekleri anlatan kentin en prestijli kentsel kültür rotalarından biridir.",
        "en": "Folklife & Ethnological Museum, set in the urban architectural jewel Villa Modiano, details local heritage and traditions as one of the city's most prestigious urban cultural routes today."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Selanik Çocuk Müzesi, kentsel eğitim ve eğlenceyi birleştiren kentin en dinamik kentsel sosyal alanlarından biridir. Çocuklar için yaratıcı kentsel atölyeleriyle kentin kentsel aile hayatının kalbidir.",
        "en": "Children's Museum of Thessaloniki merges urban education and play, standing as a dynamic social area that serves as a creative hub for children in the heart of the city's family life."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Galerius Kemeri (Kamara), kentin antik Roma döneminden kalan en ikonik kentsel sembolü olup kenti keşfedenlerin kentsel keşif albümündeki en popüler kentsel buluşma ve tarih kalesidir.",
        "en": "Arch of Galerius (Kamara) is the most iconic urban symbol of the Roman era in Thessaloniki, serving as a popular history stronghold and a favorite meeting spot for travelers exploring the city."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Makedonia Palace Hotel, kentsel liman şeridinin en prestijli ve lüks konaklama durağıdır. Adriyatik'in mavisine bakan konumuyla kentsel sosyal hayatın ve lüks kentsel turizmin en önemli rotasıdır.",
        "en": "Makedonia Palace Hotel is a prestigious luxury stay on the city waterfront. With views of the deep sea, it stands as the most vital route for high-end urban tourism and social life in the city."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "The Met Hotel, endüstriyel kentsel tasarımla modern sanatı birleştiren kentin en stil sahibi kentsel dinlenme duraklarından biridir. Panoramik deniz manzaralı kentsel terasıyla kentsel lüksü yaşatır.",
        "en": "The Met Hotel merges industrial urban design with modern art, standing as one of the city's most stylish relaxation spots. Its panoramic urban terrace brings high-end luxury to the waterfront."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Panorama Hotel, Selanik'in kentsel zirvesindeki stratejik konumu ve kentsel ve panoramik manzarasıyla tanınan kentsel bir prestij durağı olup kenti keşfedenlere kentsel bir sükunet vaat eder.",
        "en": "Panorama Hotel is a prestigious urban destination on the city's peak, known for its strategic location and panoramic vistas, promising travelers a sense of calm high above the city rush."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "University Club Restaurant, kentin dinamik öğrenci hayatını ve kentsel gastronomi dünyasını birleştiren, kentsel sosyal hayatın en enerjik ve kentsel öğrenci rotası olan bir kentsel merkezdir.",
        "en": "University Club Restaurant merges the city's dynamic student life and urban culinary world, serving as an energetic social hub and a central point for Thessaloniki's university community life."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Effe Cafe, kentsel kahve kültürünü kentin kentsel keşif haritasına taşıyan, taze kahveleriyle kentsel sosyal hayatın en sevilen ve tatlı kentsel duraklarından birisi olarak kentin kalbinde yer alır.",
        "en": "Effe Cafe is a beloved sweet stop in the heart of Thessaloniki, bringing urban coffee culture to the map as a favorite social landmark for travelers seeking a refreshing coffee break in the city."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "El Burrito, kentsel gastronomi dünyasına Meksika mutfağının kentsel ve enerjik dokunuşlarını getiren, kentin en popüler kentsel lezzet duraklarından biri olup turizm haritasında öne çıkan duraktır.",
        "en": "El Burrito brings an energetic urban twist of Mexican cuisine to the city's food world, standing out on the tourism map as one of Thessaloniki's most popular and vibrant flavor destinations."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "The Heavy Melon (To vari peponi), adından da anlaşılacağı gibi kentsel sakinliği ve yerel meyveleri esas alan, kentin en 'relaxed' ve samimi kentsel lezzet duraklarından birisi olarak gezginleri ağırlar.",
        "en": "The Heavy Melon is one of the city's most 'relaxed' and friendly food spots, centering on urban calm and fresh local produce as a unique and welcoming destination for every urban traveler."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Agora Ouzeri, geleneksel Yunan mutfak geleneklerini modern bir servisle birleştiren kentin en köklü ve kentsel lezzet durakları arasındadır. Kentsel sosyal hayatın en samimi gastronomik merkezidir.",
        "en": "Agora Ouzeri ranks among the city's most established flavor destinations, merging traditional Greek culinary habits with modern service for the friendliest social dining experience in town."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ouzeri to Yenti, Ano Poli'nin tarihi gölgesinde otantik bir mezeci deneyimi sunan kentsel bir prestij kalesidir. Kentsel manzara eşliğinde taze lezzetleri kenti keşfeden gezginlerle buluşturur.",
        "en": "Ouzeri to Yenti is a prestige stronghold in the historic shadow of Ano Poli, presenting an authentic meze experience with fresh flavors and urban vistas for every traveler exploring the city."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Wall by Wall, kentsel dinamizmi ve kentsel sanat topluluğunu birleştiren kentin en enerjik ve kentsel sosyal alanlarından birisi olup kentsel sosyal hayatın yaratıcı bir kentsel durak kalesidir.",
        "en": "Wall by Wall is a creative urban stronghold and energetic social area merging city dynamism with the art community, standing as a vital landmark for social interaction in modern Thessaloniki."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Camel's Pizza, kentsel gastronomi dünyasına kentsel bir lezzet ve taze malzeme anlayışı katan kentin en sevilen ve popüler kentsel pizzacı duraklarından biri olup turizm haritasında yer alır.",
        "en": "Camel's Pizza is a popular urban pizzeria stop recognized for its fresh ingredients and great taste, occupying a beloved spot on the city's food map for travelers seeking a quality urban dinner."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ristretto Wine Bar, kentsel sosyal hayata kaliteli şaraplar ve gurme atıştırmalıklarla modern bir soluk getiren kentin en stil sahibi ve prestijli kentsel dinlenme duraklarından bir tanesidir.",
        "en": "Ristretto is one of the most stylish and prestigious urban relaxation spots, bringing a modern breath to social life with quality wines and gourmet snacks in the heart of Thessaloniki."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Giok Balik, kentsel desenler ve balıkçılık kültürünü birleştiren kentin en özgün kentsel deniz ürünleri duraklarından biri olup kentsel sosyal hayata taze ve kentsel bir lezzet hafızası katar.",
        "en": "Giok Balik is a unique urban seafood spot merging city design with maritime culture, adding a fresh and memorable urban flavor memory to the town's vibrant social and culinary life."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mikel Coffee Thessaloniki, kentin her noktasına yayılan kalitesi ve taze demlenmiş kahveleriyle kenti keşfeden gezginlerin en pratik ve popüler kentsel duraklarından birisi olarak öne çıkar.",
        "en": "Mikel Coffee is a prominent and popular urban stop for travelers exploring the city, known for its consistent quality and fresh-brewed coffee that serves the busy rhythm of Thessaloniki life."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Sibēría, kentsel dinamizmi ve kentsel sosyal hayatı birleştiren şık tasarımıyla kentin en nezih kentsel sosyal kaçış duraklarından birini sunan modern ve kentsel bir prestijli rotadır.",
        "en": "Sibēría is a modern and prestigious urban route and a refined social escape spot in town, featuring a chic design that merges city dynamism with a sophisticated social atmosphere for all."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Omilos Beach Club, kentsel kumsalda yer alan ve kentsel eğlenceyi dalga sesleriyle buluşturan kentin en büyüleyici kentsel buluşma duraklarından biridir. Modern tasarımıyla prestijli bir yerdir.",
        "en": "Omilos Beach Club is one of the most enchanting urban meeting spots on the waterfront, merging city fun with the rhythm of the waves while maintaining its status as a prestigious destination."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Ladokolla Restaurant, kentsel gastronomi haritasında taze ürünleri ve iddialı sunumlarıyla tanınan prestijli bir kentsel lezzet durağıdır. Isminden de anlaşılacağı gibi kentsel lezzet kalesidir.",
        "en": "Ladokolla is a prestigious urban flavor destination recognized for its fresh products and ambitious service on the food map, standing as a culinary stronghold in the heart of Thessaloniki."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pizza Romana, geleneksel İtalyan taş fırın sanatını Selanik'e taşıyan kentin en popüler ve samimi pizzacı duraklarından biri olup kentsel gastronomi dünyasında prestijli yer kaplamaktadır.",
        "en": "Pizza Romana moves the Italian stone-fired oven art to Thessaloniki, standing as one of the city's most popular and friendly pizzeria stops with a prestigious spot in the urban food scene."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Selanik Batch 1 (42 venues).")

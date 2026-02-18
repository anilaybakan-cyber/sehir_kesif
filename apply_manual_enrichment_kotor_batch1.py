import json

# Manual enrichment data (Kotor Batch 1: 20 items)
updates = {
    "St. George Island": {
        "description": "Perast açıklarında, 12. yüzyıldan kalma Benediktin manastırıyla taçlanmış doğal bir ada. Ziyaretçilere kapalı olsa da, kardeş adası Our Lady of the Rocks'a tekne turları sırasında eşsiz fotoğraf kareleri sunan mistik bir manzara oluşturuyor.",
        "description_en": "A natural island offshore from Perast, crowned with a 12th-century Benedictine monastery. Although closed to visitors, it creates a mystical landscape offering unique photo opportunities during boat tours to its sister island Our Lady of the Rocks."
    },
    "Perast Müzesi": {
        "description": "Bujovic Sarayı'nın zarif barok mimarisi içinde kurulu, Perast'ın görkemli denizcilik tarihini anlatan kapsamlı müze. Venedik döneminin haritaları, gemicilik aletleri, silah koleksiyonu ve tarihi portrelerle, kasabanın altın çağına ışık tutuyor.",
        "description_en": "A comprehensive museum housed in the elegant baroque architecture of Bujovic Palace, telling the story of Perast's glorious maritime history. With maps from the Venetian period, navigational instruments, weapon collection, and historic portraits, it sheds light on the town's golden age."
    },
    "Lovcen Milli Parkı": {
        "description": "Karadağ'ın kutsal dağı ve ulusal kimliğinin sembolü olan Lovcen, 1.749 metre yüksekliği ve muhteşem manzaralarıyla ziyaretçileri büyülüyor. Çam ormanları, alpin çayırları ve kayalık zirveleriyle hem doğa yürüyüşleri hem de tarihi geziler için eşsiz bir destinasyon.",
        "description_en": "Montenegro's sacred mountain and symbol of national identity, Lovćen enchants visitors with its 1,749-meter height and magnificent views. With pine forests, alpine meadows, and rocky peaks, a unique destination for both nature hikes and historic tours."
    },
    "Njegos Mozolesi": {
        "description": "Karadağ'ın en büyük şairi ve hükümdarı Petar II Petrović Njegoš'un, Lovcen dağının zirvesinde yer alan anıtsal mezarı. 461 basamaklı zorlu tırmanışın ödülü: Adriyatik'ten İtalya'ya uzanan muhteşem 360 derece panorama ve ulusal bir kültür sembolü.",
        "description_en": "The monumental tomb of Montenegro's greatest poet and ruler Petar II Petrović Njegoš, located on the summit of Mount Lovćen. The reward for the challenging 461-step climb: a magnificent 360-degree panorama extending from the Adriatic to Italy and a national cultural symbol."
    },
    "Ivanova Korita": {
        "description": "Lovcen Milli Parkı'nın kalbinde, yemyeşil çam ormanlarıyla çevrili geleneksel piknik ve rekreasyon alanı. Taş ocakta pişen kuzu eti ve yerel peynirler sunan rustik restoranları, temiz dağ havası ve aile dostu atmosferiyle, yerel halkın hafta sonu kaçamağı.",
        "description_en": "A traditional picnic and recreation area in the heart of Lovćen National Park, surrounded by lush pine forests. A weekend getaway for locals with its rustic restaurants serving lamb cooked in stone ovens and local cheeses, clean mountain air, and family-friendly atmosphere."
    },
    "Budva Old Town": {
        "description": "Adriyatik kıyısında 2.500 yıllık geçmişiyle Balkanların en eski yerleşimlerinden biri olan bu surlarla çevrili şehir, gündüz tarihi sokaklarıyla, gece ise canlı barları ve kulüpleriyle büyülüyor. Karadağ'ın 'Rivierası'nın kalbi, hem kültür hem eğlence arayanlar için mükemmel.",
        "description_en": "One of the oldest settlements in the Balkans with 2,500 years of history on the Adriatic coast, this walled city enchants with its historic streets by day and lively bars and clubs by night. The heart of Montenegro's 'Riviera', perfect for those seeking both culture and entertainment."
    },
    "Sveti Stefan": {
        "description": "Bir zamanlar basit bir balıkçı köyüyken, şimdi dünyanın en lüks ve fotoğrafik ada-otellerinden biri olan Karadağ'ın ikonik simgesi. Denize uzanan taş köprüsü ve kırmızı çatılı evleriyle, uzaktan bile nefes kesici, cennetten bir köşe.",
        "description_en": "Once a simple fishing village, now one of the world's most luxurious and photogenic island-hotels, this is Montenegro's iconic symbol. With its stone bridge extending into the sea and red-roofed houses, a breathtaking piece of paradise even from afar."
    },
    "Jaz Beach": {
        "description": "1.2 kilometre uzunluğuyla Karadağ'ın en popüler plajlarından biri, hem sakin deniz keyfi hem de dünyaca ünlü yaz festivalleriyle tanınıyor. Açık hava konserlerine sahne olan kumsalı, su sporları imkanları ve canlı plaj barlarıyla, hem dinlenme hem de eğlence arayanların favorisi.",
        "description_en": "One of Montenegro's most popular beaches at 1.2 kilometers long, known for both calm sea enjoyment and world-famous summer festivals. A favorite for those seeking both relaxation and entertainment with its sandy shores hosting outdoor concerts, water sports, and lively beach bars."
    },
    "Mogren Beach": {
        "description": "Budva Kalesi'nin hemen batısında, kayalık geçitlerle birbirine bağlanan iki koydan oluşan cennet plaj. Berrak turkuaz suları, dramatik kaya oluşumları ve sahil boyunca keşfedilen mağaralarıyla, Budva'nın kalabalık merkezinden bir kaçış noktası.",
        "description_en": "A paradise beach consisting of two coves connected by rocky passages just west of Budva Fortress. An escape point from Budva's crowded center with its crystal-clear turquoise waters, dramatic rock formations, and caves discovered along the shore."
    },
    "Saat Kulesi (Clock Tower)": {
        "description": "17. yüzyılda Venedikliler tarafından inşa edilen, Kotor'un ana meydanı Silah Meydanı'nın simgesi tarihi saat kulesi. Hafifçe eğik yapısı ve yüzyıllık geçmişiyle, eski şehrin kalbinin attığı yeri işaret eden fotoğrafik bir ikon.",
        "description_en": "A historic clock tower built by the Venetians in the 17th century, the symbol of Kotor's main square, the Square of Arms. A photographic icon marking the beating heart of the old city with its slightly tilted structure and centuries-old history."
    },
    "Pima Sarayı": {
        "description": "Kotor'un soylu Pima ailesine ait, Venedik döneminden kalma görkemli barok saray. Cephesindeki muhteşem taş kabartmalar, aslan başları ve dekoratif süslemelerle, şehrin en etkileyici sivil mimari örneklerinden biri olarak dikkat çekiyor.",
        "description_en": "A magnificent baroque palace from the Venetian period belonging to Kotor's noble Pima family. Standing out as one of the city's most impressive examples of civil architecture with its magnificent stone reliefs, lion heads, and decorative ornaments on its facade."
    },
    "Karampana Meydanı": {
        "description": "Kotor'un ana turistik güzergahlarından saklı, yerel halkın ve bilenler için gizli bir mücevher olan küçük ve sakin meydan. Kalabalıklardan uzak, taş duvarlarla çevrili bu atmosferik köşede, bir kahve içerek şehrin gerçek ruhunu hissedebilirsiniz.",
        "description_en": "A small and quiet square hidden from Kotor's main tourist routes, a hidden gem for locals and those in the know. In this atmospheric corner surrounded by stone walls away from crowds, you can feel the city's true spirit while having a coffee."
    },
    "Napolyon Tiyatrosu": {
        "description": "Fransız işgali döneminden (1807-1813) kalma, Kotor'un dar sokaklarında gizlenmiş tarihi küçük tiyatro. Napolyon ordusunun askerleri için inşa edilmiş bu yapı, şehrin çok katmanlı tarihine ve Fransız etkisine tanıklık ediyor.",
        "description_en": "A historic small theater from the French occupation period (1807-1813), hidden in Kotor's narrow streets. This structure built for Napoleon's army soldiers witnesses the city's multi-layered history and French influence."
    },
    "Restoran Stari Mlini": {
        "description": "Ljuta nehri kıyısında, asırlık su değirmenlerinin restore edilmesiyle oluşturulmuş büyüleyici bir restoran. Nehrin şırıltısı eşliğinde taze alabalık, kuzu çevirme ve geleneksel Karadağ mezelerini tadabileceğiniz, romantik ve nostaljik bir yemek deneyimi.",
        "description_en": "A charming restaurant on the Ljuta river banks, created by restoring centuries-old watermills. A romantic and nostalgic dining experience where you can taste fresh trout, lamb on the spit, and traditional Montenegrin appetizers accompanied by the babbling of the river."
    },
    "Conte Nautilus": {
        "description": "Perast'ın körfeze bakan en iyi restoranlarından biri, taze deniz ürünleri ve şaraplarıyla tanınıyor. Our Lady of the Rocks adasına karşı masanızda, güneşin suya yansımasını izlerken unutulmaz bir Adriyatik mutfağı deneyimi sunuyor.",
        "description_en": "One of Perast's best restaurants overlooking the bay, known for its fresh seafood and wines. At your table facing Our Lady of the Rocks island, it offers an unforgettable Adriatic cuisine experience while watching the sun reflect on the water."
    },
    "Restoran Catovica Mlini": {
        "description": "Kotor Körfezi'nin en romantik restoranlarından biri: 300 yıllık antik değirmenlerin içinde, küçük bir şelalenin hemen yanında konumlanan masalsı mekan. Işıl ışıl aydınlatılmış bahçesinde, su sesi eşliğinde Karadağ'ın en iyi mutfağını deneyimleyin.",
        "description_en": "One of the most romantic restaurants in the Bay of Kotor: a fairytale venue located next to a small waterfall inside 300-year-old ancient mills. Experience Montenegro's best cuisine accompanied by the sound of water in its illuminated garden."
    },
    "Ladovina": {
        "description": "Kotor'un tarihi sokaklarında, Karadağ'ın yerel şaraplarını ve geleneksel mezelerini keşfetmek için mükemmel bir şarap evi ve tapas barı. Vranac şarabı, pršut jambonu ve Njeguški peyniri eşliğinde, şehrin otantik lezzetlerine dalın.",
        "description_en": "A perfect wine house and tapas bar in Kotor's historic streets to discover Montenegro's local wines and traditional appetizers. Dive into the city's authentic flavors accompanied by Vranac wine, pršut ham, and Njeguški cheese."
    },
    "City Pub": {
        "description": "Yerel halkın ve turistlerin kaynaştığı, Kotor'un gece hayatının merkezi olan samimi ve enerjik bar. Canlı müzik geceleri, yerel bira çeşitleri ve sıcak atmosferiyle, şehrin nabzını tutmak ve yeni arkadaşlar edinmek için ideal bir buluşma noktası.",
        "description_en": "An intimate and energetic bar at the center of Kotor's nightlife where locals and tourists mingle. An ideal meeting point to feel the city's pulse and make new friends with its live music nights, local beer selection, and warm atmosphere."
    },
    "Maximus": {
        "description": "Kotor'un ortaçağ surlarına ve limanına bakan konumuyla, gün batımında kokteyl içmek için şehrin en şık barlarından biri. Profesyonelce hazırlanan karışımları, zarif dekorasyonu ve muhteşem manzarasıyla, romantik bir akşam için mükemmel bir tercih.",
        "description_en": "One of the city's most stylish bars with its position overlooking Kotor's medieval walls and harbor, perfect for cocktails at sunset. An excellent choice for a romantic evening with its professionally prepared mixes, elegant decoration, and magnificent view."
    },
    "Kayak Turu": {
        "description": "Kotor Körfezi'nin sakin sularında kayakla keşfe çıkın: Mavi Mağara, gizli koylar ve durgun sulara yansıyan antik köyler. Hem yeni başlayanlar hem de deneyimli kayakçılar için rehberli turlar, Adriyatik'i suyun seviyesinden deneyimlemenin en büyüleyici yolu.",
        "description_en": "Set out to explore the calm waters of the Bay of Kotor by kayak: the Blue Cave, hidden coves, and ancient villages reflected in still waters. Guided tours for both beginners and experienced kayakers, the most enchanting way to experience the Adriatic from water level."
    }
}

filepath = 'assets/cities/kotor.json'
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

print(f"\n✅ Manually enriched {count} items (Kotor Batch 1).")

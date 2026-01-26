import json

# Manual enrichment data (Batch 5: 25 items)
updates = {
    "Bazaar do Povo": {
        "description": "Sintra'nın merkezinde, geleneksel Portekiz el sanatları, seramikler, dokumalar ve özgün hediyelik eşyaların satıldığı renkli bir butik. Usta zanaatkarların elinden çıkmış yerel ürünler ve Portekiz'in kültürel mirasını yansıtan objelerle dolu.",
        "description_en": "A colorful boutique in the center of Sintra selling traditional Portuguese handicrafts, ceramics, textiles, and unique souvenirs. Full of local products handmade by master craftspeople and objects reflecting Portugal's cultural heritage."
    },
    "Sintra Bazaar": {
        "description": "Antika meraklıları ve vintage koleksiyoncuları için hazine dolu bir keşif noktası. Eski mobilyalar, azulejo çini parçaları, nostaljik objeler ve nadir bulunan koleksiyon parçalarının satıldığı bu küçük pazar, geçmişe açılan bir kapı gibi.",
        "description_en": "A discovery point full of treasures for antique enthusiasts and vintage collectors. This small market selling old furniture, azulejo tile pieces, nostalgic objects, and rare collectibles is like a door opening to the past."
    },
    "Azenhas do Mar Ocean Pool": {
        "description": "Kayalıkların içine oyulmuş, her gel-gitte okyanus suyuyla yenilenen eşsiz bir doğal yüzme havuzu. Azenhas do Mar köyünün hemen altında, Atlantik'in tuzlu sularında serinlerken muhteşem kıyı manzarasının tadını çıkarabileceğiniz büyüleyici bir nokta.",
        "description_en": "A unique natural swimming pool carved into the rocks, renewed with ocean water at each tide. A fascinating spot just below the village of Azenhas do Mar where you can enjoy the magnificent coastal scenery while cooling off in the salty waters of the Atlantic."
    },
    "Praia Pequena do Rodízio": {
        "description": "Praia Grande'nin hemen yanında, daha küçük ve genellikle daha sakin olan bu şirin plaj, kalabalıktan kaçmak isteyenler için ideal bir alternatif. Aileler ve sakin bir yüzme deneyimi arayanlar için, ana plajın gölgesinde kalmış gizli bir cennet.",
        "description_en": "This cute beach right next to Praia Grande, smaller and usually calmer, is an ideal alternative for those wanting to escape crowds. A hidden paradise in the shadow of the main beach for families and those seeking a quiet swimming experience."
    },
    "Miradouro da Praia das Maçãs": {
        "description": "Praia das Maçãs plajının tamamını ve tarihi tramvay hattının kıvrılan raylarını kuşbakışı görebileceğiniz panoramik seyir noktası. Gün batımında, güneşin okyanusa batışını izlerken şehrin nostaljik tramvayının geçişini de yakalayabilirsiniz.",
        "description_en": "A panoramic viewpoint offering a bird's-eye view of the entire Praia das Maçãs beach and the winding rails of the historic tramway. At sunset, you can also catch the passage of the city's nostalgic tram while watching the sun sink into the ocean."
    },
    "Praia do Abano": {
        "description": "Guincho plajının kuzeyinde, dik patikalarla inilen, güçlü rüzgarları ve vahşi dalgalarıyla tanınan gözlerden uzak bir kumsal. Sörfçüler ve macera arayanlar için çekici, ancak yüzme için dikkatli olunması gereken bir doğa harikası.",
        "description_en": "A secluded beach north of Guincho beach, accessed by steep paths, known for its strong winds and wild waves. Attractive for surfers and adventure seekers, but a natural wonder where caution is needed for swimming."
    },
    "Praia de Samarra": {
        "description": "Dik falezlerin arasına sıkışmış, dar ve az bilinen bu plaj, macera dolu bir iniş yoluyla ulaşılabiliyor. El değmemiş doğası, turkuaz suları ve kalabalıktan uzak konumuyla, keşfedilmeyi bekleyen bir sır gibi duruyor.",
        "description_en": "This narrow and little-known beach squeezed between steep cliffs is accessible via an adventurous descent path. With its untouched nature, turquoise waters, and location away from crowds, it stands like a secret waiting to be discovered."
    },
    "Loba (Wolf) Rock": {
        "description": "Cabo da Roca bölgesinde, rüzgar ve dalgaların yüzyıllar içinde şekillendirdiği, uluyan bir kurdu andıran dramatik kaya oluşumu. Doğanın mükemmel bir heykeli olan bu ilginç jeolojik yapı, fotoğrafçıların favorilerinden biri.",
        "description_en": "A dramatic rock formation in the Cabo da Roca area resembling a howling wolf, shaped by wind and waves over centuries. This interesting geological structure, a perfect sculpture of nature, is one of the favorites of photographers."
    },
    "Praia de São Julião": {
        "description": "Sintra ve Ericeira sınırında uzanan, altın renkli geniş kumsalıyla hem yerel balıkçıların hem de sörfçülerin buluştuğu popüler bir plaj. Açık denize bakan konumu, güçlü dalgaları ve otantik atmosferiyle Portekiz kıyı kültürünü yansıtıyor.",
        "description_en": "A popular beach extending on the border of Sintra and Ericeira, with its golden wide sand where both local fishermen and surfers meet. Its position facing the open sea, strong waves, and authentic atmosphere reflect Portuguese coastal culture."
    },
    "Praia do Sul": {
        "description": "Ericeira'nın en popüler plajlarından biri olan Praia do Sul, mükemmel sörf koşulları ve canlı plaj atmosferiyle hem sporcuları hem de güneşlenenleri kendine çekiyor. Sahil kenarındaki kafe ve restoranlarla desteklenen keyifli bir gün geçirmek için ideal.",
        "description_en": "One of Ericeira's most popular beaches, Praia do Sul attracts both athletes and sunbathers with its excellent surfing conditions and lively beach atmosphere. Ideal for a pleasant day supported by cafes and restaurants along the shore."
    },
    "Miradouro de Ribeira d'Ilhas": {
        "description": "Dünya Sörf Rezervi kapsamındaki ünlü Ribeira d'Ilhas plajına tepeden hakim olan manzara noktası. Profesyonel sörf yarışmalarının izlendiği bu nokta, dalgaların ve sörfçülerin dansını yukarıdan seyretmek için en iyi yer.",
        "description_en": "A viewpoint overlooking the famous Ribeira d'Ilhas beach from above, within the World Surfing Reserve. This point where professional surfing competitions are watched is the best place to watch the dance of waves and surfers from above."
    },
    "Buraco do Fojo": {
        "description": "Kıyı kayalıklarında oluşmuş, yükselen dalgaların yarattığı basınçla deniz suyunun fışkırdığı doğal bir kuyu (blowhole). Güçlü fırtınalarda okyanusun gücünü gözler önüne seren bu jeolojik harika, çevresindeki dikkatli yürüyüşle keşfedilebilir.",
        "description_en": "A natural blowhole in the coastal rocks where seawater spurts with the pressure created by rising waves. This geological wonder showcasing the power of the ocean during strong storms can be explored with careful walking around."
    },
    "Pedra da Agulha": {
        "description": "Kıyıdan birkaç metre açıkta denizden yükselen, iğne şeklindeki sivri ve dramatik bir kaya. Dalga erozyonunun yüzyıllarca süren etkisiyle oluşan bu doğal anıt, özellikle gün doğumunda ve batımında etkileyici siluetler oluşturuyor.",
        "description_en": "A sharp and dramatic needle-shaped rock rising from the sea a few meters off the shore. This natural monument formed by centuries of wave erosion creates impressive silhouettes especially at sunrise and sunset."
    },
    "Praia das Azenhas do Mar": {
        "description": "Ünlü beyaz yamaç köyünün hemen altında, kayalıkların arasında gizlenmiş küçük ve samimi bir kumsal. Köyün Instagram'da ünlü manzarasını tamamlayan bu plaj, kayık barınağı atmosferi ve doğal havuzlarıyla dinlendirici bir mola sunuyor.",
        "description_en": "A small and intimate beach hidden among the rocks just below the famous white hillside village. Complementing the village's Instagram-famous view, this beach offers a relaxing break with its boathouse atmosphere and natural pools."
    },
    "Vigia da Urca": {
        "description": "Sintra kıyısında, eski bir sahil gözetleme kulesinin atmosferik kalıntıları. Bir zamanlar denizdeki gemileri ve olası tehlikeleri gözetlemek için kullanılan bu tarihi yapının kalıntıları, okyanus manzarası eşliğinde geçmişe bir pencere açıyor.",
        "description_en": "Atmospheric remains of an old coastal watchtower on the Sintra coast. The ruins of this historic structure once used to watch ships and potential dangers at sea open a window to the past accompanied by ocean views."
    },
    "Praia da Grota": {
        "description": "Sadece alçak gel-git zamanlarında güvenle ulaşılabilen, gizli bir mağaranın içine açılan küçük ve maceraperest bir plaj. Deniz seviyesinin yükseldiği saatlerde su altında kalabilen bu gizemli koy, zamanlama ve dikkat gerektiren özel bir keşif.",
        "description_en": "A small and adventurous beach opening into a hidden cave, accessible safely only at low tide. This mysterious cove that can become submerged when sea levels rise is a special discovery requiring timing and attention."
    },
    "Arribas de Sintra": {
        "description": "Sintra-Cascais kıyı şeridi boyunca uzanan, dramatik falezlerin tepesinden geçen nefes kesici yürüyüş parkuru. Okyanus manzaraları, kayalık sahiller ve yabani flora eşliğinde milerce devam eden bu rota, doğa yürüyüşü tutkunları için cennet.",
        "description_en": "A breathtaking hiking trail passing over the tops of dramatic cliffs along the Sintra-Cascais coastline. This route continuing for miles accompanied by ocean views, rocky beaches, and wild flora is a paradise for nature hiking enthusiasts."
    },
    "Forte da Roca": {
        "description": "Cabo da Roca burnunu koruması için 17. yüzyılda inşa edilmiş, bugün kalıntıları bile etkileyici olan tarihi kale. Atlantik'e egemen konumu, antik surları ve Avrupa'nın en batı ucundaki stratejik önemiyle tarih ve manzara meraklılarını cezbediyor.",
        "description_en": "A historic fortress built in the 17th century to protect Cabo da Roca cape, whose ruins are impressive even today. It attracts history and scenery enthusiasts with its position dominating the Atlantic, ancient walls, and strategic importance at the westernmost tip of Europe."
    },
    "Praia do Magoito Viewpoint": {
        "description": "Portekiz'in benzersiz jeolojik oluşumu olan sertleşmiş fosil kumullarını (duna consolidada) en iyi görebileceğiniz panoramik seyir noktası. Binlerce yıl öncesinden kalma bu taşlaşmış kumsallar, jeoloji meraklıları için büyüleyici bir zaman kapsülü.",
        "description_en": "A panoramic viewpoint where you can best see the consolidated fossil dunes (duna consolidada), Portugal's unique geological formation. These petrified beaches from thousands of years ago are a fascinating time capsule for geology enthusiasts."
    },
    "Sítio Arqueológico de São Miguel de Odrinhas": {
        "description": "Müzenin dışında, açık havada sergilenen Roma dönemine ait arkeolojik kalıntılar alanı. Lahitler, sütunlar ve taş yazıtların bulunduğu bu mekan, antik Roma'nın bu bölgedeki varlığına ışık tutan canlı bir tarih dersi sunuyor.",
        "description_en": "An area of archaeological remains from the Roman period exhibited outdoors outside the museum. This venue with sarcophagi, columns, and stone inscriptions offers a living history lesson shedding light on ancient Rome's presence in this region."
    },
    "Aldeia da Praia": {
        "description": "Eski bir yazlık koloni yerleşkesinden dönüştürülmüş, restoran, dükkan ve glamping tesisleri barındıran modern bir sahil yaşam konsepti. Deniz kenarında şık bir yemek yemek, yerel ürünler keşfetmek veya yıldızların altında uyumak isteyenler için çekici bir destinasyon.",
        "description_en": "A modern coastal living concept converted from an old summer colony settlement, hosting restaurants, shops, and glamping facilities. An attractive destination for those wanting to have stylish food by the sea, discover local products, or sleep under the stars."
    },
    "Pinhal da Nazaré": {
        "description": "Kıyı boyunca uzanan kumulları tutmak ve toprak erozyonunu önlemek amacıyla dikilen geniş sahil çam ormanı. Bisiklet yolları, yürüyüş parkurları ve gölgeli piknik alanlarıyla, sıcak yaz günlerinde serinlik arayan aileler için ideal bir kaçış noktası.",
        "description_en": "A wide coastal pine forest planted to hold dunes along the coast and prevent soil erosion. An ideal escape point for families seeking coolness on hot summer days with bicycle paths, walking trails, and shaded picnic areas."
    },
    "Moinho de Don Quixote": {
        "description": "Peninha tepesinin yakınında, muhteşem vadi ve okyanus manzarasına sahip eksantrik bir bar ve restoran. Don Kişot temasıyla dekore edilmiş bu ilginç mekan, gün batımında bir içki eşliğinde manzaranın tadını çıkarmak için mükemmel bir durak.",
        "description_en": "An eccentric bar and restaurant near Peninha hill with magnificent valley and ocean views. This interesting venue decorated with the Don Quixote theme is a perfect stop to enjoy the view accompanied by a drink at sunset."
    },
    "Azenhas do Mar Beach Bar": {
        "description": "Azenhas do Mar köyünün ünlü plaj havuzunun hemen üstünde, okyanus dalgalarının patladığı kayalıklara karşı içki içebileceğiniz atmosferik bar. Tuzlu esinti ve dalga sesleri eşliğinde geçen, unutulmaz bir Portekiz sahil deneyimi sunuyor.",
        "description_en": "An atmospheric bar right above the famous beach pool of Azenhas do Mar village where you can drink against the rocks where ocean waves crash. Offers an unforgettable Portuguese coastal experience accompanied by salty breeze and wave sounds."
    },
    "Praia da Viúva": {
        "description": "Azenhas do Mar'a komşu, neredeyse hiç bilinmeyen ve ulaşımı biraz macera gerektiren minik bir koy. Az ziyaretçi çektiği için neredeyse özel plaj hissi veren bu yer, keşfedilmemiş köşeler arayanlar için gizli bir mücevher.",
        "description_en": "A tiny cove neighboring Azenhas do Mar, almost unknown and requiring a bit of adventure to reach. This place, which feels almost like a private beach due to few visitors, is a hidden gem for those seeking undiscovered corners."
    }
}

filepath = 'assets/cities/sintra.json'
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

print(f"\n✅ Manually enriched {count} items (Batch 5).")

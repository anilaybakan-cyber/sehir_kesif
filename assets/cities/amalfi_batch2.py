import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
26: {'d': "Positano'nun dar sokaklarında gizlenen bu geleneksel trattoria, taze yakalanmış deniz ürünleri ve ev yapımı limoncello ile 1970'lerden bu yana ziyaretçilerin kalbini kazanıyor. Ahşap masalar, asılı sarımsak örgüleri ve Napoli aksanlı güler yüzlü servis, burayı bir restoran değil ev gibi hissettiriyor.",
    'de': "Hidden in Positano's narrow lanes, this traditional trattoria has been winning hearts since the 1970s with freshly caught seafood and homemade limoncello. Wooden tables, hanging garlic braids, and warm Neapolitan service make it feel more like someone's home than a restaurant."},

27: {'d': "Positano'nun meşhur kum plajının hemen kenarında konumlanan bu mekan, tekne turlarının gelip gittiği rıhtımdan adım mesafesinde taze deniz mahsulü sunar. Martı seslerinin eşliğinde yediğiniz deniz ürünleri makarnası ve bir kadeh yerel Falanghina şarabı, Positano deneyimini mükemmel şekilde tamamlar.",
    'de': "Situated right on the edge of Positano's famous sandy beach, this spot serves fresh seafood just steps from the boat-tour jetty. A plate of seafood pasta with a glass of local Falanghina wine, with gulls calling overhead, perfectly completes the Positano experience."},

28: {'d': "İki Michelin yıldızına sahip Don Alfonso 1890, Kampanya'nın en prestijli restoranlarından biridir. Sant'Agata sui Due Golfi'de şef Alfonso Iaccarino'nun kendi organik bahçesinden toplanan malzemelerle hazırladığı imza yemekler, her tabağı bir sanat eserine dönüştürür.",
    'de': "Holding two Michelin stars, Don Alfonso 1890 is one of Campania's most prestigious restaurants. In Sant'Agata sui Due Golfi, chef Alfonso Iaccarino transforms each plate into a work of art using produce grown in his own organic garden."},

29: {'d': "Positano plajının simgesi olan Chez Black, 1949'dan bu yana hem sahil barı hem de gurme balık restoranı olarak hizmet verir. Flamboyanın gölgesinde, denize inen taşlı merdivenlerin yanında deniz ürünlü linguine yemek, Positano'nun en ikonik anlarından birini oluşturur.",
    'de': "An icon of Positano beach since 1949, Chez Black serves as both a beachside bar and gourmet fish restaurant. Dining on seafood linguine in the shade of a flamboyant tree beside stone steps leading to the sea is one of Positano's most iconic moments."},

30: {'d': "Positano'nun en prestijli butik oteli olan Le Sirenuse, 1951'den bu yana dünya turizm rehberlerinde yerini koruyan çatı terası, panoramik havuzu ve ödüllü La Sponda restoranıyla sahil şeridinin tamamına hükmeder. Orijinal aile mülkü olan bu 18. yüzyıl villası, zarafet ve özgünlüğü bir arada yaşatır.",
    'de': "Positano's most prestigious boutique hotel, Le Sirenuse has graced world travel guides since 1951 with its rooftop terrace, panoramic pool, and award-winning La Sponda restaurant overlooking the entire coastline. This original 18th-century family villa blends elegance with genuine authenticity."},

31: {'d': "Amalfi merkezi ile Atrani arasındaki yolda bulunan Bar Franco, limon kokusu sinmiş sahil havasında yerel halkın sabah kahvesi durağıdır. Taş fırından yeni çıkmış cornetto ve taze sıkılmış portakal suyu eşliğinde gerçek bir Güney İtalya sabahını burada yaşarsınız.",
    'de': "Located on the road between central Amalfi and Atrani, Bar Franco is the morning coffee stop for locals breathing the lemon-scented coastal air. A stone-oven cornetto and freshly squeezed orange juice here deliver the authentic Southern Italian morning experience.",
    't': "Sabah 7-9 arası en canlı zamandır; taze malzemeler tükenmeden erken gidin.",
    'te': "It is liveliest between 7 and 9am; go early before fresh pastries sell out."},

32: {'d': "Ravello'nun üst mahallelerinde saklanan Terrazza Celè, kıyının 300 metre üzerinden uzanan panoramik terasıyla olağanüstü bir deneyim sunar. Akşam menüsündeki el yapımı limon makarnası ve ızgara karides, manzaranın büyüsüne eşlik eden gerçek Kampanya lezzetleridir.",
    'de': "Tucked in Ravello's upper quarters, Terrazza Celè offers an extraordinary experience from its panoramic terrace perched 300 metres above the coast. The evening menu's handmade lemon pasta and grilled prawns are authentic Campanian flavors that perfectly match the magic of the view."},

34: {'d': "1984'ten bu yana aile işletmesi olarak devam eden Porto Salvo, Positano'nun plaj seviyesindeki sade ama samimi deniz ürünleri mekânlarındandır. Sabah avından gelen palamut, sarıkuyruk ve ahtapotu çorba ya da ızgara olarak sunan bu mekan, yerel lezzet tutkunlarının vazgeçilmez adresidir.",
    'de': "Family-run since 1984, Porto Salvo is one of Positano's humble yet sincere seafood spots at beach level. Serving morning-catch bonito, amberjack, and octopus as soup or grilled dishes, it is the go-to address for local food enthusiasts."},

36: {'d': "UNESCO Dünya Mirası listesindeki Amalfi Kıyısı, Tyrrhen'in berrak sularına bakan limon bahçeleri, renkli kule evler ve antik köprülerle örülü 50 km'lik eşsiz bir şerit oluşturur. Her virajda açılan manzara, dünyanın az sayıda sahilinin yaratabileceği türden bir görsel şölen sunar.",
    'de': "Listed as a UNESCO World Heritage Site, the Amalfi Coast forms a unique 50 km ribbon of lemon groves facing the crystal Tyrrhenian Sea, colorful tower houses, and ancient bridges. Every bend reveals a visual feast few coastlines in the world can match.",
    't': "SS163'te en iyi manzaralar için belveder noktalarını kullanın; büyük otobüsler geçerken kenarına çekilin.",
    'te': "Use the belvedere lay-bys on SS163 for the best views; pull aside when large buses pass on the narrow bends."},

37: {'d': "Ravello'nun kültürel kimliğini taşıyan Fondazione Ravello, her yaz düzenlenen Wagner Festivali dahil dünya standartlarında müzik etkinliklerine ev sahipliği yapar. Villa Rufolo bahçesindeki açık hava sahnesi, 300 metre yüksekten denize bakan dramatik arka planıyla konserlere eşsiz bir atmosfer katar.",
    'de': "The cultural heart of Ravello, Fondazione Ravello hosts world-class music events including its annual summer Wagner Festival. Its open-air stage in the gardens of Villa Rufolo, with a dramatic 300-metre drop to the sea as a backdrop, adds an unmatched atmosphere to every concert.",
    't': "Festival biletleri aylarca önceden tükeniyor; erken rezervasyon şart. Konser öncesi Villa Rufolo bahçelerini de gezip içeride yemek yiyin.",
    'te': "Festival tickets sell out months in advance — early booking is essential. Explore Villa Rufolo's gardens and dine there before the concert."},

38: {'d': "Amalfi ile Ravello arasındaki sarp yamaçlarda yükselen Torre dello Ziro, Bourbon döneminden kalma bir gözetleme kulesidir. Zirveye 45 dakikalık yürüyüşün ödülü; Amalfi kentinin tamamını, limanı ve sahili kuşbakışı görmektir.",
    'de': "Rising on the steep slopes between Amalfi and Ravello, Torre dello Ziro is a Bourbon-era watchtower. The reward for a 45-minute climb is a bird's-eye view of the entire town of Amalfi, its harbor, and the coastline stretching to the horizon.",
    't': "Patikanın başlangıç noktasını Amalfi merkezinden bulmak için yerel haritalara başvurun; tabelalar yetersiz olabilir.",
    'te': "Consult local maps to find the trailhead from central Amalfi as signposting can be inconsistent along the way."},

39: {'d': "Atrani meydanında yükselen bu 10. yüzyıl katedrali, Güney İtalya'nın en iyi korunmuş Normann mozaiklerine ev sahipliği yapar. Konstantinopolis'te dökülen bronz kapıları ve mavi-altın renkli iç mekanı, sabah ışığında büyülü bir görünüm sunar.",
    'de': "Rising in Atrani's main square, this 10th-century collegiate church houses some of Southern Italy's best-preserved Norman mosaics. Its bronze doors cast in Constantinople and blue-and-gold interior offer a mesmerizing sight in the morning light.",
    't': "Atrani, Amalfi'den 10 dakika yürüme mesafesinde ve neredeyse hiç kalabalık değil; tamamen farklı bir atmosfer taşır.",
    'te': "Atrani is 10 minutes on foot from Amalfi and almost never crowded, carrying a completely different atmosphere."},

41: {'d': "Ravello'nun üst bölümünde kayalara yaslanmış bu Bizans dönemine ait küçük kilise, yüzyıllarca süregelen taş mimarisi ve içindeki eski fresk kalıntılarıyla şehrin en sakin ruhani köşelerinden birini oluşturur. Ravello'nun turistik alanlarının gölgesinde kalan bu mekan, huzur arayanlar için tam bir buluş.",
    'de': "Nestled against the rocks in Ravello's upper quarter, this small Byzantine-era church with its centuries-old stone architecture and ancient fresco remnants forms one of the town's most tranquil spiritual corners, a true find for those seeking peace away from the busier attractions.",
    't': "Kapı her zaman açık olmayabilir; sabah ayini saatinde (genellikle 08:00) içeri girme şansı daha yüksek.",
    'te': "The door may not always be open; your best chance to enter is during morning mass, usually around 08:00."},

43: {'d': "1080 yılına tarihlenen San Giovanni del Toro, Ravello'nun en güzel Normann kiliselerinden biridir. Süslü ambon üzerindeki inci mavisi mozaikler ve gemi biçimindeki taş vaftiz teknesi, Orta Çağ ustalarının ustalığını tüm görkemiyle sergiler.",
    'de': "Dating to 1080, San Giovanni del Toro is among Ravello's finest Norman churches. Its ornate ambo with pearl-blue mosaics and ship-shaped stone baptismal font display medieval craftsmanship in all its splendor.",
    't': "Restorasyon nedeniyle kısmen kapalı olabilir; ziyaretten önce kilise yönetimiyle iletişime geçin.",
    'te': "It may be partially closed for restoration; check with the church administration before visiting."},

47: {'d': "Amalfi limanının hemen üstünde, sarmaşıklarla örtülü bu Fransisken kilisesi ve manastır kompleksi 1280 yılında kurulmuştur. İç avlusundaki turunç ve limon ağaçları arasında oturmak, dışarıdaki kalabalıktan uzaklaşmanın en huzurlu yoludur.",
    'de': "Founded in 1280, this ivy-draped Franciscan church and monastery complex just above Amalfi's harbor has a tranquil inner courtyard of orange and lemon trees. Sitting among them offers the most peaceful escape from the tourist bustle just outside its walls.",
    't': "Manastır bahçesi genellikle ziyaretçilere açıktır; Amalfi'nin en sakin fotoğrafik anlarını burada yaşayabilirsiniz.",
    'te': "The monastery garden is generally open to visitors, offering some of Amalfi's most peaceful and photogenic moments."},

48: {'d': "Piazza Flavio Gioia'daki bu anıt, pusulayı icat ettiği söylenen 13. yüzyıl denizcisi Flavio Gioia'yı onurlandırmak için dikilmiştir. Bir denizci cumhuriyetinin gururu olan bu heykel, Amalfi'nin dünya denizcilik tarihindeki köklü yerine dair önemli bir hatırlatıcıdır.",
    'de': "This monument in Piazza Flavio Gioia honors 13th-century mariner Flavio Gioia, credited with inventing the magnetic compass. A symbol of pride for a seafaring republic, the statue is a powerful reminder of Amalfi's deep place in world maritime history.",
    't': "Heykel günbatımında altın ışıkla aydınlandığında en güzel görünümünü alır; kısa bir duruş bile değer.",
    'te': "The statue looks its best when bathed in golden sunset light — even a brief stop is worthwhile."},
}

apply_batch('amalfi.json', U)

import json

# Manual enrichment data (Gaziantep Batch 2: 42 items)
updates = {
    "Mercimek Köftecisi": {
        "description": "Antep'in ünlü acılı mercimek köftelerini, kıvır kıvır ve bol baharatlı halinde sunan geleneksel lokanta. Yanında marul, limon ve nar ekşisi ile servis edilen bu vegan lezzet, şehrin sokak mutfağının simgesi.",
        "description_en": "A traditional restaurant serving Antep's famous spicy lentil patties in their curly and heavily spiced form. This vegan flavor served with lettuce, lemon, and pomegranate syrup is a symbol of the city's street food."
    },
    "Şehir Parkı": {
        "description": "Şehir merkezinde geniş yeşil alanları, göletleri ve yürüyüş yollarıyla yerel halkın favori dinlenme noktası. Çocuk oyun alanları, kafeler ve mevsimlik etkinliklerle, her yaştan ziyaretçi için ideal.",
        "description_en": "A favorite resting point for locals in the city center with wide green areas, ponds, and walking paths. Ideal for visitors of all ages with children's playgrounds, cafes, and seasonal events."
    },
    "Teleferik Tesisleri": {
        "description": "Şehrin tepesine panoramik manzara eşliğinde çıkaran modern teleferik hattı. Yukarıda kafeler, manzara noktaları ve piknik alanlarıyla, Gaziantep'i kuşbakışı görme fırsatı.",
        "description_en": "A modern cable car line taking you to the city's hilltop with panoramic views. An opportunity to see Gaziantep from bird's eye with cafes, viewpoints, and picnic areas above."
    },
    "Film Platosu": {
        "description": "Gaziantep'in geleneksel yaşamını yansıtan, tarihi film setleri ve kostüm koleksiyonuyla ilginç açık hava müzesi. Nostaljik fotoğraflar çektirmek ve Antep tarihini canlandırılmış olarak görmek için ideal.",
        "description_en": "An interesting open-air museum with historic film sets and costume collection reflecting Gaziantep's traditional life. Ideal for taking nostalgic photos and seeing Antep history brought to life."
    },
    "Dağ Evi Restaurant": {
        "description": "Şehrin yükseklerinde, manzara eşliğinde geleneksel Antep yemekleri sunan atmosferik restoran. Özellikle gece şehir ışıkları manzarasıyla, romantik yemek için mükemmel tercih.",
        "description_en": "An atmospheric restaurant high above the city serving traditional Antep dishes with views. A perfect choice for romantic dining, especially with city lights view at night."
    },
    "Antika Pazarı": {
        "description": "Tarihi eşyalar, eski kitaplar, vintage objeler ve koleksiyonluk parçaların satıldığı nostaljik pazar. Hazine avcıları ve antika meraklıları için keşfedilecek sürprizlerle dolu köşe.",
        "description_en": "A nostalgic market selling historical items, old books, vintage objects, and collectible pieces. A corner full of surprises to discover for treasure hunters and antique enthusiasts."
    },
    "Etnografya Sergisi": {
        "description": "Gaziantep ve çevresinin geleneksel yaşam tarzını, kıyafetlerini ve günlük objelerini sergileyen kültürel alan. El sanatları, dokumacılık ve ev kültürüne dair zengin koleksiyon.",
        "description_en": "A cultural area exhibiting traditional lifestyle, clothing, and daily objects of Gaziantep and surroundings. Rich collection on handicrafts, weaving, and home culture."
    },
    "Sanat Galerisi": {
        "description": "Yerel ve ulusal sanatçıların eserlerinin sergilendiği, dönemsel sergiler ve satışların yapıldığı sanat mekanı. Çağdaş Türk sanatını keşfetmek ve orijinal eserler edinmek için adres.",
        "description_en": "An art venue where works of local and national artists are exhibited, with periodic exhibitions and sales. An address to discover contemporary Turkish art and acquire original works."
    },
    "Kültür Merkezi": {
        "description": "Konserler, tiyatro gösterileri, konferanslar ve kültürel etkinliklere ev sahipliği yapan şehrin ana kültür mekanı. Gaziantep'in sanat ve kültür programlarını takip etmek için kilit nokta.",
        "description_en": "The city's main cultural venue hosting concerts, theater performances, conferences, and cultural events. A key point to follow Gaziantep's art and culture programs."
    },
    "Antep Mutfağı Kursu": {
        "description": "Profesyonel eğitmenler eşliğinde geleneksel Antep yemekleri ve tatlıları yapmayı öğrenebileceğiniz uygulamalı atölye. Kebaptan baklavaya, şeflerden birebir eğitim.",
        "description_en": "A hands-on workshop where you can learn to make traditional Antep dishes and desserts with professional instructors. One-on-one training from chefs, from kebab to baklava."
    },
    "Fıstık Hasadı Turu": {
        "description": "Sezonunda (Eylül-Ekim) Antep fıstığı bahçelerine giderek hasat deneyimi yaşayabileceğiniz tarım turu. Taze fıstık toplama, kavrulmuş fıstık tadımı ve çiftlik yaşamını keşif.",
        "description_en": "An agricultural tour where you can experience harvest in Antep pistachio orchards in season (September-October). Fresh nut picking, roasted pistachio tasting, and farm life discovery."
    },
    "Geleneksel Oyun Gecesi": {
        "description": "Tavla, okey ve diğer geleneksel Türk oyunlarını yerel halkla oynayabileceğiniz kültürel etkinlik. Çay eşliğinde sosyal etkileşim ve Antep günlük yaşamına katılım fırsatı.",
        "description_en": "A cultural event where you can play backgammon, okey, and other traditional Turkish games with locals. An opportunity for social interaction over tea and participation in Antep daily life."
    },
    "Hammam Deneyimi": {
        "description": "Tarihi Antep hamamlarından birinde geleneksel Türk hamamı ritüelini yaşayabileceğiniz wellness deneyimi. Kese, köpük masajı ve sıcak mermer taşları üzerinde dinlenme.",
        "description_en": "A wellness experience where you can live traditional Turkish bath ritual in one of historic Antep hammams. Exfoliation, foam massage, and relaxation on hot marble stones."
    },
    "Bakır Atölyesi Workshop": {
        "description": "Gaziantep'in ünlü bakır işçiliğini ustalardan öğrenip kendi bakır eserinizi yapabileceğiniz interaktif atölye. Zanaatın inceliklerini keşfedin ve benzersiz bir hatıra götürün.",
        "description_en": "An interactive workshop where you can learn Gaziantep's famous copperwork from masters and make your own copper piece. Discover the subtleties of craftsmanship and take a unique souvenir."
    },
    "Gece Şehir Turu": {
        "description": "Aydınlatılmış tarihi yapıları, gece pazarlarını ve şehrin gece yaşamını keşfedebileceğiniz rehberli tur. Farklı bir perspektiften Gaziantep, ışıltılı anıtlar ve atmosferik sokaklar.",
        "description_en": "A guided tour to discover illuminated historic buildings, night markets, and city nightlife. Gaziantep from a different perspective, glittering monuments, and atmospheric streets."
    },
    "Bisiklet Turu": {
        "description": "Şehrin tarihi ve modern bölgelerini bisikletle keşfedebileceğiniz organize tur. Sağlıklı ve çevre dostu ulaşım, yerel rehber eşliğinde gizli köşeleri keşif.",
        "description_en": "An organized tour to discover the city's historic and modern areas by bicycle. Healthy and eco-friendly transportation, discovering hidden corners with local guide."
    },
    "Yürüyüş Parkuru": {
        "description": "Şehir çevresinde doğa yürüyüşleri için işaretlenmiş patikalar ve manzaralı rotalar. Sabah koşusu, hafif yürüyüş veya aktif bir gün için ideal yeşil koridor.",
        "description_en": "Marked trails and scenic routes for nature walks around the city. An ideal green corridor for morning jogging, light walking, or an active day."
    },
    "Fotoğraf Müzesi": {
        "description": "Gaziantep'in tarihini ve dönüşümünü eski fotoğraflar aracılığıyla anlatan nostaljik koleksiyon. 19. ve 20. yüzyıldan görüntüler, şehrin geçmişine görsel bir yolculuk.",
        "description_en": "A nostalgic collection telling Gaziantep's history and transformation through old photographs. Images from 19th and 20th centuries, a visual journey into the city's past."
    },
    "Minyatür Müzesi": {
        "description": "Gaziantep'in tarihi yapılarının detaylı minyatür modellerini sergileyen küçük ama büyüleyici müze. Şehrin mimari mirasını küçük ölçekte keşfedin.",
        "description_en": "A small but fascinating museum exhibiting detailed miniature models of Gaziantep's historic buildings. Discover the city's architectural heritage in small scale."
    },
    "Seramik Atölyesi": {
        "description": "Geleneksel Antep motiflerini kullanarak seramik yapımı öğrenebileceğiniz yaratıcı atölye. Kendi tabak veya vazınızı yapın ve otantik bir hatıra götürün.",
        "description_en": "A creative workshop where you can learn ceramic making using traditional Antep motifs. Make your own plate or vase and take an authentic souvenir."
    },
    "Ahşap Oymacılık": {
        "description": "Geleneksel Antep ahşap oymacılığını ustalardan öğrenebileceğiniz ve deneyebileceğiniz zanaat atölyesi. El işçiliğinin inceliklerini keşfedin ve kendi parçanızı yaratın.",
        "description_en": "A craft workshop where you can learn and try traditional Antep wood carving from masters. Discover the subtleties of handwork and create your own piece."
    },
    "Çarşı Rehberli Tur": {
        "description": "Tarihi çarşıları, hanları ve kapalı pazarları uzman rehber eşliğinde keşfedebileceğiniz organize tur. Gizli hikayeler, yerel sırlar ve en iyi dükkanları öğrenin.",
        "description_en": "An organized tour to discover historic bazaars, hans, and covered markets with expert guide. Learn hidden stories, local secrets, and best shops."
    },
    "Gastronomi Turu": {
        "description": "Antep mutfağının en iyi örneklerini tadarak şehri keşfedeceğiniz lezzet odaklı tur. Kebapçılardan tatlıcılara, yerel uzman eşliğinde gurme macera.",
        "description_en": "A flavor-focused tour to discover the city by tasting the best examples of Antep cuisine. A gourmet adventure from kebab houses to dessert shops with local expert."
    },
    "Güneş Battı Bar": {
        "description": "Şehrin tepesinde gün batımını izleyerek kokteyl ve içki keyfi yapabileceğiniz manzaralı bar. Romantik atmosfer, panoramik görünüm ve kaliteli içeceklerle özel akşam.",
        "description_en": "A scenic bar on the city's hilltop where you can watch sunset while enjoying cocktails and drinks. A special evening with romantic atmosphere, panoramic view, and quality drinks."
    },
    "Gece Pazarı": {
        "description": "Akşam saatlerinde açılan, sokak yemekleri, hediyelikler ve yerel ürünlerin satıldığı canlı pazar. Gece yemeği, alışveriş ve şehrin gece enerjisini hissetmek için ideal.",
        "description_en": "A lively market opening in evening hours selling street food, souvenirs, and local products. Ideal for night dining, shopping, and feeling the city's night energy."
    },
    "Yesemek Heykel Atölyesi": {
        "description": "Hitit döneminden kalma dünyanın en büyük açık hava heykel atölyesi kalıntıları. Binlerce yarım kalmış heykel ve antik taş işçiliğini görebileceğiniz arkeolojik hazine.",
        "description_en": "Remains of the world's largest open-air sculpture workshop from Hittite period. An archaeological treasure where you can see thousands of unfinished sculptures and ancient stone work."
    },
    "Bayazhan Gaziantep Kent Müzesi": {
        "description": "Tarihi bir handa kurulan, şehrin tarihini, ekonomisini ve kültürünü interaktif sergilerle anlatan modern müze. Fıstık kültüründen savunma sanayine, Gaziantep hikayesi.",
        "description_en": "A modern museum established in a historic han telling the city's history, economy, and culture with interactive exhibitions. Gaziantep's story from pistachio culture to defense industry."
    },
    "Mevlevi Hamamı": {
        "description": "Mevlevi dervişleri tarafından kullanılan tarihi hamam, şimdi restore edilmiş kültürel mekan. Osmanlı hamam mimarisinin güzel bir örneği ve tarihi atmosfer.",
        "description_en": "A historic hammam used by Mevlevi dervishes, now a restored cultural venue. A beautiful example of Ottoman bath architecture and historic atmosphere."
    },
    "Tarihi Baklavatçılar Çarşısı": {
        "description": "Onlarca baklava ve tatlı ustasının yan yana sıralandığı, Antep baklavasının anavatanı tarihi çarşı. Tadım yaparak en beğendiğinizi seçin ve taze paketletin.",
        "description_en": "A historic bazaar, homeland of Antep baklava, where dozens of baklava and dessert masters are lined up side by side. Taste, choose your favorite, and have it freshly packed."
    },
    "Küçükbayram Kebap Salonu": {
        "description": "Turistik olmayan bir mahallede, yerel halkın favori kebapçısı. Sade ortamı, lezzetli etleri ve uygun fiyatlarıyla, gerçek Antep kebap deneyimi.",
        "description_en": "A local favorite kebab house in a non-touristy neighborhood. A real Antep kebab experience with simple setting, delicious meats, and affordable prices."
    },
    "Katmer Dünyası": {
        "description": "Antep'e özgü ince yufkalı, fıstıklı ve kaymaklı tatlı katmerin en güzel örneklerini sunan özel mekan. Sabah kahvaltısı olarak da tüketilen bu lezzeti denemeyi unutmayın.",
        "description_en": "A special venue offering the finest examples of katmer, a thin pastry dessert with pistachio and cream unique to Antep. Don't forget to try this delicacy also consumed as morning breakfast."
    },
    "Tarihi Menengiç Kahvesi": {
        "description": "Antep'e özgü menengiç kahvesinin en otantik halini sunan tarihi mekan. Kafeinsiz, fıstık aromalı bu benzersiz içeceği, geleneksel ortamda deneyimleyin.",
        "description_en": "A historic venue offering the most authentic version of menengiç coffee unique to Antep. Experience this unique caffeine-free, pistachio-flavored drink in traditional setting."
    },
    "Lahmacun Durağı": {
        "description": "İnce açılmış, bol baharatlı ve kıymalı Antep usulü lahmacunların yapıldığı popüler lokanta. Hızlı, lezzetli ve uygun fiyatlı öğle yemeği seçeneği.",
        "description_en": "A popular restaurant making thin-rolled, heavily spiced Antep-style lahmacun with minced meat. A quick, delicious, and affordable lunch option."
    },
    "Kültür Yolu": {
        "description": "Şehrin tarihi bölgelerini birbirine bağlayan, yaya dostu sokaklar ve kültürel noktalardan oluşan turizm rotası. Müzeler, hanlar ve anıtları yürüyerek keşfedin.",
        "description_en": "A tourism route connecting the city's historic areas, consisting of pedestrian-friendly streets and cultural points. Discover museums, hans, and monuments on foot."
    },
    "Alaüddevle Camii": {
        "description": "16. yüzyıldan kalma Memluk mimarisinin etkileyici örneği tarihi cami. Taş işçiliği, minaresi ve tarihi atmosferiyle, Gaziantep'in dini mirasının önemli parçası.",
        "description_en": "A historic mosque from the 16th century, impressive example of Mamluk architecture. An important part of Gaziantep's religious heritage with stone work, minaret, and historic atmosphere."
    },
    "Şahinbey Anıt Mezarı": {
        "description": "Kurtuluş Savaşı kahramanı Şahinbey'in anısına yapılan, şehrin tarihinde önemli yeri olan anıt mezar. Milli mücadele tarihine saygı duruşu ve şehitlik ziyareti.",
        "description_en": "A memorial tomb built in memory of War of Independence hero Şahinbey, with important place in city's history. A tribute to national struggle history and martyrdom visit."
    },
    "Olgun Pide Salonu": {
        "description": "Antep usulü pide ve lahmacunun en lezzetli örneklerini sunan, yerel halk arasında popüler aile lokantası. Odun fırınında pişirme ve geleneksel tariflerle otantik lezzet.",
        "description_en": "A family restaurant popular among locals, serving the most delicious examples of Antep-style pide and lahmacun. Authentic flavor with wood-fired baking and traditional recipes."
    },
    "Çardak Kahvesi": {
        "description": "Gölgelik avluda çardaklar altında çay ve menengiç kahvesi içebileceğiniz geleneksel kahvehane. Tavla, okey ve sohbet için yerel halkın buluşma noktası.",
        "description_en": "A traditional coffeehouse where you can drink tea and menengiç coffee under pergolas in a shaded courtyard. A meeting point for locals for backgammon, okey, and conversation."
    },
    "Hamdi Usta Ciğer Salonu": {
        "description": "Antep usulü baharatlı ciğer kebabının en usta yapıldığı yer. Taze kuzu ciğeri, özel baharat karışımı ve mangal ateşi ile hazırlanan, cesur damaklar için lezzet.",
        "description_en": "The place where Antep-style spicy liver kebab is made most masterfully. A flavor for brave palates prepared with fresh lamb liver, special spice mix, and charcoal fire."
    },
    "Ahşap Oyuncak Müzesi": {
        "description": "Geleneksel ahşap oyuncakların sergilendiği ve satıldığı, çocukluk nostaljisi yaşatan küçük müze-dükkan. El yapımı, doğal malzemeli oyuncaklar ve oyun atölyesi.",
        "description_en": "A small museum-shop where traditional wooden toys are exhibited and sold, evoking childhood nostalgia. Handmade toys with natural materials and play workshop."
    },
    "Şire Pazarı": {
        "description": "Üzüm şırası, pekmez ve geleneksel içeceklerin satıldığı, sonbaharda özellikle canlanan mevsimlik pazar. Taze üzüm ürünleri ve Antep'in hasat kültürünü deneyimleyin.",
        "description_en": "A seasonal market selling grape must, molasses, and traditional drinks, especially lively in autumn. Experience fresh grape products and Antep's harvest culture."
    },
    "Antep Sofrası": {
        "description": "Geleneksel Antep yemeklerinin geniş çeşitliliğini sunan, zengin menüsüyle dikkat çeken büyük aile restoranı. Beyran, yuvalama, kebap ve tatlılar bir arada.",
        "description_en": "A large family restaurant offering wide variety of traditional Antep dishes, notable for rich menu. Beyran, yuvalama, kebab, and desserts all together."
    }
}

filepath = 'assets/cities/gaziantep.json'
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

print(f"\n✅ Manually enriched {count} items (Gaziantep Batch 2).")

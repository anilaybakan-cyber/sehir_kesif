import json

# Manual enrichment data (Brugge Batch 3 FINAL: 52 items)
updates = {
    "Graaf Visartpark": {
        "description": "Şehrin kuzeybatısında geniş yeşil alanları, göletleri ve spor tesisleriyle dikkat çeken popüler halk parkı. Koşu yolları, çocuk oyun alanları ve piknik noktalarıyla, yerel halkın hafta sonu favorisi.",
        "description_en": "A popular public park in the city's northwest notable for wide green areas, ponds, and sports facilities. A local weekend favorite with jogging paths, children's playgrounds, and picnic spots."
    },
    "Arentshuis": {
        "description": "Gruuthuse kompleksinin bir parçası olarak, İngiliz ressam Frank Brangwyn'in eserlerini ve güzel bahçesini ziyaretçilere sunan küçük ama nitelikli müze. Kanal manzaralı terasıyla, sakin bir sanat molası için ideal.",
        "description_en": "A small but quality museum offering English painter Frank Brangwyn's works and beautiful garden as part of the Gruuthuse complex. Ideal for a quiet art break with its canal-view terrace."
    },
    "Bruges Beer Experience": {
        "description": "Belçika bira kültürünü interaktif sergiler, tadım oturumları ve multimedya araçlarıyla anlatan modern müze. 16 farklı bira tadımı dahil, eğlenceli ve eğitici bir Belçika bira deneyimi.",
        "description_en": "A modern museum explaining Belgian beer culture with interactive exhibitions, tasting sessions, and multimedia tools. An entertaining and educational Belgian beer experience including 16 different beer tastings."
    },
    "Kantcentrum": {
        "description": "Brugge'ün dünyaca ünlü dantel üretim geleneğini yaşatan, kurslar ve gösteriler sunan dantel merkezi. Zanaatkarların çalışmasını izleyebilir, el yapımı orijinal danteller satın alabilirsiniz.",
        "description_en": "A lace center keeping Bruges' world-famous lace production tradition alive, offering courses and demonstrations. You can watch artisans work and purchase handmade original laces."
    },
    "Gezellehuis": {
        "description": "Ünlü Flaman şair Guido Gezelle'nin doğduğu ve büyüdüğü tarihi ev, şimdi hayatını ve eserlerini sergileyen müze. Romantik bahçesi ve 19. yüzyıl atmosferiyle, edebiyat meraklıları için özel durak.",
        "description_en": "The historic house where famous Flemish poet Guido Gezelle was born and raised, now a museum exhibiting his life and works. A special stop for literature enthusiasts with romantic garden and 19th-century atmosphere."
    },
    "Sint-Janshuis Mill": {
        "description": "1770'lerden kalma, hala aktif olarak un öğüten ve ziyarete açık tarihi yel değirmeni. Değirmenin çalışma mekanizmasını öğrenebilir, tepedeki konumundan şehir manzarasını seyredebilirsiniz.",
        "description_en": "A historic windmill from the 1770s, still actively grinding flour and open for visits. You can learn the mill's working mechanism and watch city views from its hilltop location."
    },
    "Poortersloge": {
        "description": "Ortaçağda zengin tüccarların buluşma yeri olan, gotik mimarisinin en güzel örneklerinden tarihi lonca binası. Cephesindeki heykeller ve işlemelerle, Brugge ticaret tarihinin simgesi.",
        "description_en": "A historic guild building, one of the finest examples of Gothic architecture, where wealthy merchants met in medieval times. A symbol of Bruges' trade history with sculptures and carvings on its facade."
    },
    "Hof Arents": {
        "description": "Gruuthuse müzesinin yakınında, huzurlu atmosferi ve Bonifacius köprüsü manzarasıyla gizli bahçe. Şehrin en romantik ve sakin köşelerinden biri, fotoğraf çekimi için mükemmel.",
        "description_en": "A hidden garden near Gruuthuse museum with peaceful atmosphere and Bonifacius bridge views. One of the city's most romantic and quiet corners, perfect for photography."
    },
    "Provinciaal Hof": {
        "description": "Grote Markt meydanının kuzey tarafını kaplayan, Neo-Gotik tarzda görkemli idari bina. Cephesindeki detaylı işlemeler ve aydınlatılmış gece silueti ile şehrin en etkileyici yapılarından biri.",
        "description_en": "A magnificent administrative building in Neo-Gothic style covering the north side of Grote Markt square. One of the city's most impressive structures with detailed carvings on its facade and illuminated night silhouette."
    },
    "Huis 't Schaep": {
        "description": "17. yüzyıldan kalma tarihi ev, şimdi küçük bir müze ve kültürel etkinliklere ev sahipliği yapan mekan. Geleneksel Flaman mimarisi ve iç dekorasyonuyla, dönem yaşamına göz atma fırsatı.",
        "description_en": "A 17th-century historic house, now a small museum and venue hosting cultural events. An opportunity to glimpse period life with traditional Flemish architecture and interior decoration."
    },
    "Hof van Watervliet": {
        "description": "16. yüzyıldan kalma tarihi avlu ve evler topluluğu, şehrin az bilinen mimari hazinelerinden. Gotik ve Rönesans öğelerinin karışımı ile, tarihi keşif meraklıları için gizli bir köşe.",
        "description_en": "A 16th-century historic courtyard and house complex, one of the city's lesser-known architectural treasures. A hidden corner for historic discovery enthusiasts with a mix of Gothic and Renaissance elements."
    },
    "Huis de Crombrugghe": {
        "description": "Rokoko tarzı cephesiyle dikkat çeken, şehrin en güzel örneklerinden tarihi konak. Özel mülk olmasına rağmen, dışarıdan mimari zarafetini hayranlıkla izleyebilirsiniz.",
        "description_en": "A historic mansion notable for its Rococo-style facade, one of the city's finest examples. Although private property, you can admiringly watch its architectural elegance from outside."
    },
    "Loge van de Vrijmetselarij": {
        "description": "Tarihi Mason Locası binası, Brugge'ün 18. yüzyıldaki sivil toplum hayatına ışık tutan ilginç yapı. Gizemli sembolizmi ve ayarı mimari stili ile meraklı gezginlerin durağı.",
        "description_en": "The historic Masonic Lodge building, an interesting structure shedding light on Bruges' 18th-century civil society life. A stop for curious travelers with mysterious symbolism and ornate architectural style."
    },
    "Bisschoppelijk Paleis": {
        "description": "Brugge piskoposunun resmi ikametgahı olan görkemli barok saray. Genellikle ziyarete kapalı olsa da, dış mimarisi ve bahçesi gözlemlenebilir.",
        "description_en": "The magnificent baroque palace serving as the official residence of the Bishop of Bruges. Although usually closed to visits, its exterior architecture and garden can be observed."
    },
    "Grootseminarie": {
        "description": "Rahip yetiştirmek için kurulan büyük dini eğitim kompleksi, Brugge'ün dini tarihinin önemli bir parçası. Kütüphanesi ve binası nadiren ziyarete açılsa da, mimari önemi büyük.",
        "description_en": "A large religious education complex established for training priests, an important part of Bruges' religious history. Though its library and building rarely open for visits, its architectural significance is great."
    },
    "English Seminary": {
        "description": "17. yüzyılda İngilizce konuşan Katolikler için kurulan, tarihi bir teoloji okulu ve ruhani merkez. İngiliz-Belçika dini bağlarına tanıklık eden özel atmosferli yapı.",
        "description_en": "A historic theology school and spiritual center established for English-speaking Catholics in the 17th century. A structure with special atmosphere witnessing English-Belgian religious ties."
    },
    "Godshuis De Moor": {
        "description": "17. yüzyıldan kalma, yaşlılar için inşa edilmiş hayır evi. Beyaz badanalı cephesi, düzgün avlusu ve çiçekleriyle, Brugge'ün sosyal tarihinin güzel bir örneği.",
        "description_en": "A 17th-century almshouse built for the elderly. A beautiful example of Bruges' social history with its whitewashed facade, tidy courtyard, and flowers."
    },
    "Godshuis Van Campen": {
        "description": "1636'da kurulan tarihi almshouse, Brugge'ün hayırseverlik geleneğinin canlı temsilcisi. Huzurlu iç avlusu ve geleneksel mimarisiyle, turistlerden uzak sakin bir köşe.",
        "description_en": "A historic almshouse founded in 1636, a living representative of Bruges' charity tradition. A quiet corner away from tourists with its peaceful inner courtyard and traditional architecture."
    },
    "Godshuis Rooms Convent": {
        "description": "Eski Roomse rahibe yurdundan dönüştürülmüş, şimdi sosyal konut olarak kullanılan tarihi yapı kompleksi. Ortaçağ atmosferi ve huzurlu avlusuyla, şehrin korunan tarihsel mirasından.",
        "description_en": "A historic building complex converted from an old Roman nuns' residence, now used as social housing. Part of the city's preserved historical heritage with medieval atmosphere and peaceful courtyard."
    },
    "Godshuis Vette Vispoort": {
        "description": "Balık tüccarları loncası tarafından finanse edilen, nadir bulunan özel amaçlı almshouse. Brugge balıkçılık tarihine ve lonca sistemine ışık tutan benzersiz sosyal kurum.",
        "description_en": "A rarely found special-purpose almshouse financed by the fish traders' guild. A unique social institution shedding light on Bruges' fishing history and guild system."
    },
    "Ribs 'n Beer": {
        "description": "Adından da anlaşılacağı gibi, kaburga ve bira kombinasyonu uzmanı Amerikan tarzı restoran. Doyurucu porsiyonlar, geniş bira seçkisi ve samimi atmosferiyle et severler için ideal.",
        "description_en": "As the name suggests, an American-style restaurant specializing in ribs and beer combination. Ideal for meat lovers with satisfying portions, wide beer selection, and friendly atmosphere."
    },
    "Tête Pressée": {
        "description": "Geleneksel Belçika ve Fransız mutfağını modern yorumlarla sunan şık bistro. Mevsimlik menüsü, kaliteli şarapları ve zarif sunumuyla, özel bir yemek deneyimi.",
        "description_en": "An elegant bistro offering traditional Belgian and French cuisine with modern interpretations. A special dining experience with seasonal menu, quality wines, and elegant presentation."
    },
    "Park Restaurant": {
        "description": "Minnewater parkına bakan, romantik konumu ve yaratıcı mutfağıyla dikkat çeken restoran. Gün batımında terasta yemek, şehrin en romantik deneyimlerinden biri.",
        "description_en": "A restaurant overlooking Minnewater park, notable for romantic location and creative cuisine. Dining on the terrace at sunset is one of the city's most romantic experiences."
    },
    "Den Amand": {
        "description": "Yerel malzemelerle hazırlanan modern Belçika mutfağı sunan samimi restoran. Şefin günlük menüsü, dikkatli servis ve dostane atmosferiyle, yerel halkın favorisi.",
        "description_en": "An intimate restaurant offering modern Belgian cuisine prepared with local ingredients. A local favorite with chef's daily menu, attentive service, and friendly atmosphere."
    },
    "Bistro Bruut": {
        "description": "Ham ve pişmemiş lezzetlere odaklanan, minimalist tasarımıyla dikkat çeken yenilikçi restoran. Beklenmedik tat kombinasyonları ve cesur sunumlarıyla, gastronomi maceracıları için.",
        "description_en": "An innovative restaurant focusing on raw and uncooked flavors with minimalist design. For gastronomy adventurers with unexpected taste combinations and bold presentations."
    },
    "Pro Deo": {
        "description": "Yerel ve mevsimlik malzemelere odaklanan, küçük ama nitelikli Michelin tavsiyeli restoran. Yaratıcı tabaklar, özenli servis ve samimi ortamıyla, gurmelerin durağı.",
        "description_en": "A small but quality Michelin-recommended restaurant focusing on local and seasonal ingredients. A stop for gourmets with creative dishes, careful service, and intimate setting."
    },
    "'t Bagientje": {
        "description": "Kanal kenarında romantik konumuyla öne çıkan, sıcak atmosferi ve geleneksel Belçika yemekleriyle ünlü restoran. Işıltılı kanallar eşliğinde akşam yemeği için ideal bir tercih.",
        "description_en": "A restaurant standing out with romantic canalside location, famous for warm atmosphere and traditional Belgian food. An ideal choice for dinner accompanied by glistening canals."
    },
    "One Restaurant": {
        "description": "Modern fine-dining konseptiyle, şık sunumlar ve yaratıcı lezzetler sunan üst düzey restoran. Özenli şarap eşleştirmeleri ve profesyonel servisiyle, özel kutlamalar için mükemmel.",
        "description_en": "An upscale restaurant offering stylish presentations and creative flavors with modern fine-dining concept. Perfect for special celebrations with careful wine pairings and professional service."
    },
    "Pomperlut": {
        "description": "Tradisyonel Flaman yemeklerini ev yapımı atmosferde sunan, samimi aile restoranı. Anne eli lezzetleri, doyurucu porsiyonlar ve uygun fiyatlarıyla, yerel deneyim arayanlar için.",
        "description_en": "An intimate family restaurant serving traditional Flemish dishes in homemade atmosphere. For those seeking local experience with homestyle flavors, satisfying portions, and affordable prices."
    },
    "Reliva": {
        "description": "Sağlıklı ve hafif öğünler sunan, vejetaryen ve vegan dostu modern kafe-restoran. Taze malzemeler, yaratıcı salatalar ve smoothie'lerle, bilinçli beslenenlerin durağı.",
        "description_en": "A modern cafe-restaurant serving healthy and light meals, vegetarian and vegan friendly. A stop for conscious eaters with fresh ingredients, creative salads, and smoothies."
    },
    "The Olive Tree": {
        "description": "Yunan ve Akdeniz lezzetlerini Belçika'ya taşıyan, sıcak atmosferli restoran. Mezeler, zeytinyağlı yemekler ve Yunan şaraplarıyla, farklı bir mutfak deneyimi.",
        "description_en": "A restaurant bringing Greek and Mediterranean flavors to Belgium with warm atmosphere. A different cuisine experience with appetizers, olive oil dishes, and Greek wines."
    },
    "Rock Fort": {
        "description": "İtalyan etkili, yaratıcı sunum ve yerel malzemelerle çalışan modern mutfak restoranı. Açık mutfağı, samimi ortamı ve lezzet odaklı yaklaşımıyla, şehrin sevilen adresleri arasında.",
        "description_en": "A modern cuisine restaurant with Italian influence, working with creative presentation and local ingredients. Among the city's beloved addresses with open kitchen, intimate setting, and flavor-focused approach."
    },
    "Kok au Vin": {
        "description": "Adından da anlaşılacağı gibi, klasik Fransız mutfağı şaheseri Coq au Vin'in en iyi yapıldığı restoran. Geleneksel tarifler, iyi şaraplar ve nostaljik atmosfer.",
        "description_en": "As the name suggests, the restaurant where the classic French cuisine masterpiece Coq au Vin is made best. Traditional recipes, good wines, and nostalgic atmosphere."
    },
    "De Vlaamsche Pot": {
        "description": "Geleneksel Flaman güveç yemeklerinin en otantik halini sunan rustik restoran. Stoofvlees, waterzooi ve diğer klasik tariflerle, gerçek Belçika mutfağı deneyimi.",
        "description_en": "A rustic restaurant offering the most authentic version of traditional Flemish stew dishes. A real Belgian cuisine experience with stoofvlees, waterzooi, and other classic recipes."
    },
    "Lebowski Bar": {
        "description": "Kült film 'The Big Lebowski'den ilham alan, geniş kokteyl menüsü ve rahat atmosferiyle eğlenceli bar. Film severler ve kokteyl tutkunları için benzersiz bir deneyim.",
        "description_en": "A fun bar inspired by the cult film 'The Big Lebowski' with extensive cocktail menu and relaxed atmosphere. A unique experience for film lovers and cocktail enthusiasts."
    },
    "Chocolatier Van Oost": {
        "description": "El yapımı pralinler ve trüfleriyle ünlü, üç nesil deneyime sahip geleneksel çikolata ustası. Taze üretim, kaliteli hammadde ve zarif sunumla, çikolata tutkunlarının durağı.",
        "description_en": "A traditional chocolatier famous for handmade pralines and truffles with three generations of experience. A stop for chocolate lovers with fresh production, quality raw materials, and elegant presentation."
    },
    "Spegelaere Chocolatier": {
        "description": "1963'ten beri aile işletmesi olarak çalışan, otantik Belçika çikolataları üreten butik atölye. Klasik tatlar, geleneksel teknikler ve sıcak servisyle, çikolata deneyimi.",
        "description_en": "A boutique workshop producing authentic Belgian chocolates as a family business since 1963. A chocolate experience with classic flavors, traditional techniques, and warm service."
    },
    "Oyya Waffles": {
        "description": "Brüksel ve Liège waffle'larının en kaliteli versiyonlarını sunan butik waffle dükkanı. Çıtır dışı, yumuşak içi ve taze malzemeleriyle, gerçek Belçika waffle deneyimi.",
        "description_en": "A boutique waffle shop offering the best quality versions of Brussels and Liège waffles. A real Belgian waffle experience with crispy exterior, soft interior, and fresh ingredients."
    },
    "Chez Albert": {
        "description": "Grote Markt'ta konumlanan, onlarca yıllık deneyimle waffle ve krep sunan klasik mekan. Turistik konuma rağmen, kalite ve lezzetten ödün vermeyen güvenilir adres.",
        "description_en": "A classic venue located in Grote Markt serving waffles and crepes with decades of experience. A reliable address not compromising on quality and taste despite tourist location."
    },
    "Fred's Waffles": {
        "description": "Küçük ama sevilen waffle dükkanı, organik malzemeler ve yaratıcı toppinglerle fark yaratan. Yerel halk arasında popüler, turistik tuzaklardan uzak özgün bir alternatif.",
        "description_en": "A small but beloved waffle shop making a difference with organic ingredients and creative toppings. An original alternative away from tourist traps, popular among locals."
    },
    "Tudor Castle": {
        "description": "Loppem yakınlarında, İngiliz Tudor stilini taklit eden ilginç şato. Mimari merakı, labirent bahçesi ve doğa yürüyüşleriyle, günübirlik kaçamak için romantik bir seçenek.",
        "description_en": "An interesting castle near Loppem imitating English Tudor style. A romantic option for day getaway with architectural curiosity, maze garden, and nature walks."
    },
    "Beisbroek": {
        "description": "Gözlemevi, planetaryum ve geniş ormanlık alanıyla bilim ve doğayı buluşturan park. Astronomi gösterileri, yürüyüş parkurları ve çocuk aktiviteleriyle, aileler için eğitici gezi.",
        "description_en": "A park uniting science and nature with observatory, planetarium, and extensive woodland area. An educational trip for families with astronomy shows, hiking trails, and children's activities."
    },
    "Chartreuse Nature Reserve": {
        "description": "Brugge yakınında, çeşitli kuş türleri ve yaban hayatını barındıran korunan doğa alanı. Kuş gözlemi, fotoğrafçılık ve doğa yürüyüşleri için ideal, şehir gürültüsünden kaçış.",
        "description_en": "A protected nature area near Bruges housing various bird species and wildlife. Ideal for bird watching, photography, and nature walks, an escape from city noise."
    },
    "Oostkerke": {
        "description": "Damme yakınlarında sakin ve pittoresk köy, tarihi kilisesi ve yeşil manzaralarıyla dikkat çekiyor. Bisiklet rotaları üzerinde mola noktası, otantik Flaman kırsal yaşamının örneği.",
        "description_en": "A quiet and picturesque village near Damme, notable for historic church and green landscapes. A rest point on bicycle routes, an example of authentic Flemish rural life."
    },
    "Hoeke Windmill": {
        "description": "Hollanda sınırına yakın pitoresk köyün simgesi tarihi yel değirmeni. Düz Flaman arazisi üzerinde etkileyici siluet, bisiklet turları ve fotoğraf için popüler durak.",
        "description_en": "A historic windmill, the symbol of the picturesque village near the Dutch border. An impressive silhouette over flat Flemish terrain, popular stop for cycling tours and photography."
    },
    "Sluis": {
        "description": "Hollanda sınırının hemen ötesinde, güzel evleri ve zengin alışveriş olanaklarıyla ünlü kasaba. Sınır ötesi günübirlik gezi, pazarcılar ve turist dostu mağazalarla dolu.",
        "description_en": "A town just across the Dutch border, famous for beautiful houses and rich shopping opportunities. A cross-border day trip, full of market vendors and tourist-friendly stores."
    },
    "Cadzand": {
        "description": "Hollanda'nın Belçika sınırına yakın sahil kasabası, geniş kumsalı ve köpek dostu plajlarıyla popüler. Deniz havası, yürüyüş ve günübirlik plaj gezisi için ideal.",
        "description_en": "A Dutch coastal town near Belgian border, popular for wide beach and dog-friendly shores. Ideal for sea air, walking, and day beach trips."
    },
    "Blankenberge Pier": {
        "description": "350 metre uzunluğundaki etkileyici iskele, Kuzey Denizi manzarası ve sahil eğlencesinin merkezi. Restoranlar, dükkanlar ve gece aydınlatmasıyla, Belçika kıyı tatilinin simgelerinden.",
        "description_en": "An impressive 350-meter pier, center of North Sea views and coastal entertainment. One of the symbols of Belgian coastal vacation with restaurants, shops, and night lighting."
    },
    "Sea Life Blankenberge": {
        "description": "Çeşitli deniz canlılarını barındıran akvaryum, köpekbalıkları ve denizanaları ile ailelere yönelik merkez. Eğitici sergiler, dokunma havuzları ve çocuk aktiviteleriyle, yağmurlu gün planı.",
        "description_en": "An aquarium housing various marine creatures, a family-oriented center with sharks and jellyfish. A rainy day plan with educational exhibitions, touch pools, and children's activities."
    },
    "Serpentarium": {
        "description": "Blankenberge'de egzotik sürüngenler ve yılanların sergilendiği küçük ama ilgi çekici hayvanat bahçesi. Eğitici turlar ve canlı gösterilerle, doğa meraklıları için benzersiz deneyim.",
        "description_en": "A small but interesting zoo in Blankenberge exhibiting exotic reptiles and snakes. A unique experience for nature enthusiasts with educational tours and live shows."
    },
    "Permeke Museum": {
        "description": "Belçikalı ekspresyonist ressam Constant Permeke'nin eski stüdyosu ve evinde kurulan sanat müzesi. Sanatçının eserleri, kişisel eşyaları ve yaratıcı atmosferiyle, sanat tarihi ziyareti.",
        "description_en": "An art museum established in the former studio and home of Belgian expressionist painter Constant Permeke. An art history visit with artist's works, personal belongings, and creative atmosphere."
    },
    "Uitkerkese Polder": {
        "description": "Belçika'nın en önemli kuş gözlem alanlarından biri olan geniş tarım arazisi ve sulak alan. Göçmen kuşlar, dramatik gökyüzü ve düz manzarasıyla, doğa fotoğrafçılarının cennet.",
        "description_en": "An extensive agricultural land and wetland, one of Belgium's most important bird watching areas. A paradise for nature photographers with migratory birds, dramatic skies, and flat landscapes."
    }
}

filepath = 'assets/cities/brugge.json'
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

print(f"\n✅ Manually enriched {count} items (Brugge Batch 3 FINAL).")

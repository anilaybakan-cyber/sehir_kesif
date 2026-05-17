import json

path = "assets/cities/ksamil.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping generated content (TR, EN) for the remaining 43 venues
updates = {
    "ChIJG6l0D8lrWxMRkR7N7X5_K8Y": {
        "tr": "Africana Beach Club, enerjik atmosferi ve denize sıfır konumdaki modern localarıyla Ksamil'in en popüler eğlence duraklarından biridir. Akdeniz mutfağının seçkin lezzetleri ve iddialı kokteylleri ile hem gündüz güneşten hem de gece müzikten keyif alacağınız kentsel bir merkezdir.",
        "en": "Africana Beach Club is one of Ksamil's most popular entertainment spots, featuring an energetic vibe and modern beachfront cabanas. With elite Mediterranean dishes and signature cocktails, it serves as an urban hub to enjoy both the sun by day and the music by night."
    },
    "ChIJ9_m_wQBrWxMR8M-mH4FuDqk": {
        "tr": "Blue Eyes Coffee, taze kavrulmuş kahve aroması ve gölge altına gizlenmiş bahçesiyle kentin en huzurlu mola duraklarından biridir. Panoramik deniz manzaralı balkonuyla hem kahvenizi yudumlayabileceğiniz hem de Adriyatik esintisini hissedebileceğiniz samimi bir kentsel kaçış noktasıdır.",
        "en": "Blue Eyes Coffee is one of the most peaceful break stops in town, offering fresh-roasted coffee aromas in a shaded garden. With its panoramic sea-view balcony, it’s a friendly urban escape where you can sip your coffee while feeling the gentle Adriatic breeze."
    },
    "ChIJ7ao8_dNrWxMRU0mPZ2Y3jHw": {
        "tr": "The Mussel House, bölgenin en taze istiridye ve midye çeşitlerini sunan, göl kenarındaki büyüleyici konumuyla ünlü kentsel bir gurme kalesidir. Yerel deniz mahsulleri kültürüyle tanışabileceğiniz ve gün batımını lezzet eşliğinde izleyebileceğiniz Ksamil'in en prestijli restoranıdır.",
        "en": "The Mussel House is a gourmet urban stronghold famous for its lakeside location and serving the region's freshest oysters and mussels. It is Ksamil's most prestigious restaurant, where you can explore local seafood culture while watching the sunset with unique flavors."
    },
    "ChIJiS9aAQBrWxMRaZ6_3X5_K8Y": {
        "tr": "Taverna Kerasia, nesillerdir devam eden Arnavut mutfak geleneklerini modern sunumlarla birleştiren kentin en samimi lezzet duraklarından biridir. Odun ateşinde pişen taze balıkları ve organik zeytinyağlıları ile kentin gastronomi haritasında otantik bir durak olarak yer alır.",
        "en": "Taverna Kerasia is a friendly culinary destination merging classic Albanian kitchen traditions passed through generations with modern service. With wood-fired fresh fish and organic olive oil dishes, it stands as an authentic stop on the town's gastronomic map."
    },
    "ChIJP5X_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Angelos Bar, Ksamil'in kristal sularına bakan terası ve butik içecek menüsüyle kentin en stil sahibi akşam üzeri duraklarından biridir. Hafif müzik ve deniz kokusuyla çevrili bu alan, kentin modern sosyal hayatının en keyifli ve nezih buluşma noktalarından biridir.",
        "en": "Angelos Bar is one of the most stylish sunset stops in town, featuring a terrace overlooking Ksamil's crystal waters and a boutique drink menu. Surrounded by ambient music and the scent of the sea, it is one of the town's most pleasant and refined social hubs."
    },
    "ChIJa-n-wQBrWxMRNM-mH4FuDqk": {
        "tr": "Dimas Swimming Pool, güneşin altında serinlemek isteyenler için kentin en ferah havuz alanı ve panoramik güneşlenme terasıdır. Modern tasarımı ve çocuklar için güvenli alanlarıyla, hem yerel halkın hem de turistlerin tercih ettiği kentsel bir dinlenme merkezidir.",
        "en": "Dimas Swimming Pool is the town's most refreshing pool area and panoramic sun deck for those looking to cool off under the sun. With its modern design and safe zones for children, it serves as a preferred urban relaxation center for both locals and travelers."
    },
    "ChIJy7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Dolphins Cafe-Bar, adını sıkça görülen misafirlerinden alan ve denize hakim konumuyla Ksamil sahilinin en enerjik noktalarından biridir. Taze tıkılmış meyve suları ve kentsel atmosferiyle, kenti keşfederken mola verebileceğiniz en samimi ve fotojenik mekanlardan biridir.",
        "en": "Dolphins Cafe-Bar, named after its frequent visitors, is one of the most energetic points on the Ksamil coast with its commanding sea views. With fresh-pressed juices and a vibrant urban vibe, it’s one of the friendliest and most photogenic spots to take a break."
    },
    "ChIJL_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Poseidon Trident Lounge, mitolojik dokunuşları modern konforla birleştiren kentin en prestijli kokteyl duraklarından biridir. Adriyatik mavisine bakan şık locaları ve kaliteli hizmetiyle, kentsel sosyal yaşamın en nezih ve aristokrat deniz keyfini sunan adreslerinden biridir.",
        "en": "Poseidon Trident Lounge is one of the most prestigious cocktail stops in town, blending mythological touches with modern comfort. With chic cabanas facing the Adriatic blue and quality service, it’s one of the most refined and aristocratic destinations in social life."
    },
    "ChIJQ7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Te GERI PizzaBar, İtalyan taş fırın geleneğini Ksamil'in taze yerel malzemeleriyle harmanlayan sevilen bir kentsel lezzet durağıdır. Samimi ortamı ve iddialı marinara soslu pizzalarıyla, kentin gastronomi dünyasında hem hızlı hem de kaliteli bir akşam yemeği rotasıdır.",
        "en": "Te GERI PizzaBar is a beloved urban flavor destination blending the Italian stone-fired oven tradition with Ksamil's fresh local ingredients. With its welcoming vibe and ambitious marinara pizzas, it’s a fast yet high-quality dinner route in the town's culinary scene."
    },
    "ChIJT_n-wQBrWxMR_M-mH4FuDqk": {
        "tr": "Simple, adından da anlaşılacağı gibi sadeliği ve kaliteyi ön planda tutan, Ksamil'in en modern ve 'minimalist' kafe duraklarından biridir. Kristal netliğindeki deniz manzarası ve gurme kahve çeşitleriyle, kentin karmaşasından uzaklaşıp dinginleşmek isteyenler için ideal bir limandır.",
        "en": "Simple, true to its name, prioritizes minimalism and quality as one of Ksamil's most modern cafe stops. With crystal-clear sea views and gourmet coffee selections, it serves as an ideal harbor for those looking to disconnect from the urban rush and find calm."
    },
    "ChIJX7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Cunat e Ullirit, Ksamil'in bereketli zeytin bahçeleri arasında yer alan ve geleneksel Arnavut mezelerini en taze haliyle sunan otantik bir lezzet durağıdır. Yerel zeytinyağı ve taze pişmiş ekmek kokusuyla çevrili bu bahçe, kentin en doğal ve samimi gastronomi noktasıdır.",
        "en": "Cunat e Ullirit is an authentic culinary stop located among Ksamil's fertile olive groves, serving traditional Albanian appetizers at their freshest. Surrounded by the scent of local oil and fresh bread, this garden is the town's most natural and friendly foodie spot."
    },
    "ChIJV7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Abiori Restaurant Pizzeria, denize sıfır terası ve geniş menüsüyle Ksamil'in en popüler ve köklü aile restoranlarından biridir. Hem geleneksel deniz ürünlerini hem de meşhur taş fırın pizzalarını bir arada bulabileceğiniz kentsel sosyal hayatın en canlı gastronomi merkezlerindendir.",
        "en": "Abiori Restaurant Pizzeria is one of the most popular and established family restaurants in Ksamil, featuring a beachfront terrace and a vast menu. It is one of the liveliest culinary hubs where you can find both traditional seafood and famous stone-fired pizzas."
    },
    "ChIJb7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Blue Pool Bar, mavi ile turkuazın buluştuğu kentsel bir vaha gibi Ksamil'in kalbinde ferahlatıcı içecekler ve havuz keyfi sunmaktadır. Modern tasarımı ve akşamları düzenlenen tematik partileriyle kentin genç ve dinamik tatil ruhunu en iyi yansıtan sosyal alanlardan biridir.",
        "en": "Blue Pool Bar serves as an urban oasis in the heart of Ksamil, offering refreshing drinks and poolside joy where blue meets turquoise. With its modern design and thematic evening parties, it’s one of the social areas best reflecting the town's young and dynamic vibe."
    },
    "ChIJd7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Coffe Time, kentin telaşından kaçıp huzurlu bir kitap okuma veya denizi izleme noktası arayanların Ksamil'deki en samimi adresidir. Taze demlenmiş bitki çayları ve ev yapımı tatlılarıyla, kentin gürültüsünden uzaklaşıp kentsel bir sükunete bürünmek için birebirdir.",
        "en": "Coffe Time is the friendliest address in Ksamil for those seeking a quiet spot to read or watch the sea. With its freshly brewed herbal teas and homemade desserts, it is perfect for stepping away from the city noise and immersing in a sense of urban tranquility."
    },
    "ChIJe7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Shop & Go Snacks, kenti keşfederken pratik ve lezzetli bir mola vermek isteyenlerin Ksamil'deki en hızlı ve güvenilir lezzet durağıdır. Taze hazırlanan sandviçleri ve zengin soğuk içecek menüsüyle, kentsel maceralarınız arasında enerji depolayabileceğiniz en popüler noktadır.",
        "en": "Shop & Go Snacks is the fastest and most reliable snack stop in Ksamil for those wanting a practical yet tasty break while exploring. With freshly prepared sandwiches and a rich cold drink menu, it's the most popular spot to recharge during your urban adventures."
    },
    "ChIJf7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Savory Bistro, modern gastronomi tekniklerini Ksamil'in yerel malzemeleriyle birleştiren şık ve 'boutique' bir kentsel lezzet istasyonudur. Estetik sunumları ve Adriyatik'e bakan seçkin atmosferiyle, kentin gastronomi haritasında kalite ve lezzetin ikonik bir buluşma noktasıdır.",
        "en": "Savory Bistro is a chic boutique urban flavor station merging modern gastronomic techniques with Ksamil's local ingredients. With aesthetic service and an elite atmosphere facing the Adriatic, it’s an iconic meeting point of quality and taste on the town's map."
    },
    "ChIJg7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Hello Créperie, Ksamil'in tatlı molaları için en meşhur adresi olup, taze meyveler ve yerel ballarla hazırlanan yaratıcı krepleriyle kentin en sevilen duraklarındandır. Özellikle akşam yürüyüşleri sonrası kentin en popüler ve samimi tatlı cenneti olarak gezginleri ağırlar.",
        "en": "Hello Créperie is the most famous address for sweet breaks in Ksamil, beloved for its creative crepes made with fresh fruits and local honey. It welcomes travelers as the town's most popular and friendly dessert heaven, especially after evening walks."
    },
    "ChIJh7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Sweet Corner, adından da anlaşılacağı gibi Ksamil'in tatlı bir köşesi olup, geleneksel Balkan tatlılarını modern bir dokunuşla sunan kentsel bir lezzet noktasıdır. Ev yapımı dondurmaları ve ferahlatıcı şerbetleriyle kentin lezzet hafızasında en tatlı yeri tutan duraklardan biridir.",
        "en": "Sweet Corner, as its name suggests, is a sweet corner of Ksamil representing an urban flavor point that serves traditional Balkan desserts with a modern twist. With homemade ice creams and refreshing syrups, it holds the sweetest spot in the town's memory."
    },
    "ChIJi7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Veliaj Traditional Restaurant, Arnavut misafirperverliğini ve kuşaktan kuşağa aktarılan taş fırın pide tariflerini en samimi haliyle sunan bir kentsel merkezdir. Yerel şarapları ve odun ateşinde tüten meşhur pizzalarıyla kentin en köklü ve güvenilir lezzet kalelerinden biridir.",
        "en": "Veliaj Traditional Restaurant is an urban hub showcasing Albanian hospitality and stone-fired pide recipes passed down through generations. With local wines and its famous wood-fired pizzas, it stands as one of the town's most long-standing and reliable flavor strongholds."
    },
    "ChIJj7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Pizza Zone, Ksamil'in her köşesine yayılan lezzetiyle kentin en popüler pizzacı duraklarından biri olup, özellikle ince ve çıtır hamuruyla tanınan bir lezzet noktasıdır. Hızlı servisi ve kentsel konumuyla kenti keşfederken doyurucu bir akşam yemeği için en uğrak duraklarındandır.",
        "en": "Pizza Zone is one of the most popular pizzeria stops in town, famous across every corner of Ksamil for its thin and crispy dough. With its quick service and urban location, it is a staple destination for a hearty dinner while exploring the city's sights."
    },
    "ChIJk7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Blue Diamond, Ksamil'in turkuaz sularına tepeden bakan şık locaları ve seçkin içecek menüsüyle kentin mücevher gibi parlayan kentsel bir vaha noktasıdır. Modern tasarımı ve akşamları büründüğü büyüleyici atmosferiyle kentsel sosyal yaşamın en prestijli buluşma adreslerinden biridir.",
        "en": "Blue Diamond is an urban oasis that shines like a jewel, featuring chic cabanas overlooking Ksamil's turquoise waters and an elite drink menu. With its modern design and magical evening atmosphere, it’s one of the most prestigious social hubs in the town."
    },
    "ChIJl7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Beki, samimi bir mahalle dükkanı atmosferinde yerel Arnavut el sanatlarını ve kentsel hediyelikleri keşfedebileceğiniz Ksamil'in en otantik alışveriş duraklarından biridir. Kentin ruhunu yansıtan özgün tasarımlarıyla, kentsel keşiflerinizden kalıcı hatıralar biriktirebileceğiniz bir noktadır.",
        "en": "Beki is one of the most authentic shopping stops in Ksamil, where you can discover local handicrafts and urban souvenirs in a friendly neighborhood vibe. With original designs reflecting the town's spirit, it's a place to collect lasting memories from your urban exploration."
    },
    "ChIJm7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Mom, adından da anlaşılacağı gibi 'anne eli değmiş' lezzetleri ve samimi ortamıyla Ksamil'de ev özlemi duyanların kentsel buluşma ve lezzet noktasıdır. Taze Ege mezeleri ve geleneksel ev yemekleriyle kentin kalbinde en sıcak ve huzurlu gastronomi deneyimini vaat etmektedir.",
        "en": "Mom, as its name suggests, is the urban meeting and flavor point for those missing 'home-cooked' meals and a welcoming vibe in Ksamil. With fresh appetizers and traditional home dishes, it promises the warmest and most peaceful gastronomic experience in the town's heart."
    },
    "ChIJn7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Vila Pasqyra, adını meşhur Mirror Beach'e olan yakınlığından alan ve kentin en otantik, huzur dolu konaklama duraklarından biri olarak bilinen kentsel bir sığınaktır. Kayaların arasına gizlenmiş bu alan, kentin karmaşasından tamamen kopup doğayla baş başa kalmak isteyenlerin adresidir.",
        "en": "Vila Pasqyra is an urban sanctuary named after nearby Mirror Beach, known as one of the town's most authentic and peaceful stay options. This area hidden among cliffs is the home for those wanting to disconnect from urban noise and be alone with nature."
    },
    "ChIJo7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Greg Lounge, Ksamil sahilinin en stil sahibi ve 'chic' duraklarından biri olup, Adriyatik'in mavisine bakan konforlu localarıyla kentsel sosyal hayatın merkezindedir. Gurme atıştırmalıkları ve iddialı kokteyl menüsüyle kentsel lüksü deniz kıyısında en iyi yansıtan prestijli bir noktadır.",
        "en": "Greg Lounge is one of the most stylish and 'chic' stops on the Ksamil coast, serving as a social hub with comfortable cabanas facing the Adriatic blue. With gourmet snacks and an ambitious cocktail menu, it’s a prestigious point reflecting urban luxury by the sea."
    },
    "ChIJp7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Muzg Lounge, günün en güzel saatlerini yani 'muzg' (alacakaranlık) vaktini en iyi gören terasıyla Ksamil'in en büyüleyici kentsel buluşma duraklarındandır. Hafif müzik ve kaliteli içecekleri ile kentin akşam enerjisine hazırlanmak için kentsel sosyal hayatın en nezih rotalarından biridir.",
        "en": "Muzg Lounge is one of Ksamil's most enchanting urban meeting spots, featuring a terrace that perfectly captures the beauty of 'muzg' (twilight). With ambient music and quality drinks, it is one of the social life's most refined routes to prepare for the town's evening energy."
    },
    "ChIJq7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "3 Island Lounge, Ksamil'in ikonik adalarını panoramik olarak izleyebileceğiniz ve denizin üzerinde asılıymış gibi hissedeceğiniz kentsel bir lezzet kalelesidir. Modern tasarımı ve şık ambiyansıyla kentsel sosyal hayatın en çok fotoğraflanan ve tercih edilen prestijli duraklarındandır.",
        "en": "3 Island Lounge is an urban flavor stronghold where you can view Ksamil's iconic islands panoramically and feel as if you are suspended over the sea. With its modern design and chic ambiance, it is one of the social scene's most photographed and prestigious destinations."
    },
    "ChIJr7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Chill out, adından da anlaşılacağı gibi kentsel sakinliği ve huzuru temel alan, Ksamil'in en 'relaxed' ve samimi dinlenme duraklarından biridir. Denize sıfır hamakları ve taze meyve suları ile kentin enerjisinden mola verip kafa dinlemek için kentsel sosyal hayatın en huzurlu limanıdır.",
        "en": "Chill out, true to its name, centers on urban calm and peace as one of Ksamil's most relaxed and friendly retreat stops. With beachfront hammocks and fresh juices, it serves as the society's most peaceful harbor to take a break from the town's energy and find quiet."
    },
    "ChIJs7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "NOCTURA LOUNGE, kentsel gece hayatının Ksamil'deki kalbi olup, modern tasarımı ve iddialı DJ performanslarıyla kentin en dinamik ve şık sosyal alanıdır. Egzotik kokteylleri ve büyüleyici aydınlatmasıyla kentsel sosyal yaşamın en prestijli gece rotalarından biri olarak öne çıkmaktadır.",
        "en": "NOCTURA LOUNGE is the heart of urban nightlife in Ksamil, serving as the town's most dynamic and stylish social area with DJ performances. With exotic cocktails and magical lighting, it stands out as one of the most prestigious nocturnal routes in the town's social life."
    },
    "ChIJt7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Lounge Bar Narghilè, otantik nargile kültürüyle kentsel modernliği birleştiren Ksamil'in en egzotik kentsel dinlenme ve sosyal kaçış duraklarından biridir. Hafif müzik ve Adriyatik manzarası eşliğinde sunulan kentsel konforuyla, kentin en özgün sosyal durakları arasında yer almaktadır.",
        "en": "Lounge Bar Narghilè is one of the most exotic urban relaxation and social escape stops in Ksamil, merging authentic hookah culture with urban modernity. With comfort offered against a backdrop of ambient music and Adriatic views, it ranks among the town's most unique social hubs."
    },
    "ChIJu7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Uma Beach Bar, bembeyaz dekorasyonu ve 'boho-chic' tarzıyla Ksamil sahil şeridinde Mykonos rüzgarları estiren kentsel bir prestijli lezzet noktasıdır. Gün boyu devam eden enerjik atmosferi ve iddialı deniz ürünleriyle kentsel sosyal hayatın en elit ve modern buluşma adresidir.",
        "en": "Uma Beach Bar is a prestigious urban flavor point bringing Mykonos vibes to the Ksamil coast with its white decor and 'boho-chic' style. With an energetic atmosphere all day and ambitious seafood, it is the most elite and modern social hub in the town's urban scene."
    },
    "ChIJv7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Foga Pirates Lounge, Ksamil adalarına bakan tematik tasarımı ve eğlenceli konseptiyle kentin en neşeli ve kentsel sosyal macera duraklarından biridir. Gençlerin ve çocuklu ailelerin favorisi olan mekan, kentin turizm haritasında samimiyeti ve enerjisiyle öne çıkan bir duraktır.",
        "en": "Foga Pirates Lounge is one of the town's cheerful urban social adventure stops, featuring a thematic design and fun concept facing the islands. A favorite for youth and families alike, it stands out on the town's tourism map for its warmth, energy, and unique character."
    },
    "ChIJw7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Vamos Cocktail Bar, kentsel canlılığı ve yaratıcı miksoloji tekniklerini birleştiren, kentin en popüler gastronomi ve sosyal duraklarından biridir. Modern tasarımı ve Adriyatik'e tepeden bakan terasıyla kentsel sosyal hayatın en prestijli akşam üzeri rotalarından birini sunmaktadır.",
        "en": "Vamos Cocktail Bar is one of the town's most popular gastronomic and social stops, merging urban vitality with creative mixology techniques. With its modern design and terrace overlooking the Adriatic, it offers one of the most prestigious sunset routes in the social life."
    },
    "ChIJx7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bar-Lounge Corner, kentin köşesinde saklanmış kentsel bir hazine gibi huzurlu ve samimi bir atmosfer sunan Ksamil'in en gizli sosyal duraklarından biridir. Taze demlenmiş içecekleri ve sessiz ortamıyla kentsel gürültüden kaçıp kafa dinlemek için birebir kentsel bir kaçış noktasıdır.",
        "en": "Bar-Lounge Corner is one of Ksamil's most hidden social stops, offering a peaceful and friendly vibe like an urban treasure tucked in a corner. With freshly brewed drinks and quiet surroundings, it is perfect for escaping urban noise and finding a sense of inner calm."
    },
    "ChIJy7m_wQBrWxMRNM-mH4FuDqk": {
        "tr": "Foga Lounge, kentsel konforu ve Adriyatik'in eşsiz manzarasını birleştiren şık tasarımıyla Ksamil sahilinin en nezih kentsel sosyal kaçış duraklarından biridir. Hafif müzik ve kaliteli içecekleri ile kentin akşam enerjisine hazırlanmak için kentsel sosyal hayatın en nezih rotasıdır.",
        "en": "Foga Lounge is one of the most refined urban social escape stops on the Ksamil coast, featuring chic design that merges urban comfort with immense Adriatic views. With ambient music and quality drinks, it is the social scene's most polished route to prep for the evening."
    },
    "ChIJz7m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Dips Lounge, kentsel gastronomi dünyasına sushi ve yaratıcı kokteylleriyle modern bir soluk getiren, Ksamil'in en stil sahibi kentsel lezzet ve sosyal duraklarından biridir. Estetik sunumları ve şık ambiyansıyla kentsel sosyal hayatın en prestijli ve modern buluşma rotalarındandır.",
        "en": "Dips Lounge is one of Ksamil's most stylish urban flavor and social stops, bringing a modern breath to the town with sushi and creative cocktails. With aesthetic service and a chic ambiance, it ranks among the social scene's most prestigious and modern meeting routes."
    },
    "ChIJ07m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bliss Lounge Bar, kentsel mutluluğu ve sükuneti esas alan, Ksamil adalarına karşı kentsel huzur sunan kentin en 'peaceful' sosyal duraklarından biridir. Beyaz dekorasyonu ve yumuşak müziğiyle kentin karmaşasından kopmak isteyenler için kentsel sosyal hayatın en huzurlu limanıdır.",
        "en": "Bliss Lounge Bar is one of the most 'peaceful' social stops in town, centering on urban happiness and serenity facing the Ksamil islands. With its white decor and soft music, it serves as the society's most peaceful harbor for those wanting to disconnect from urban noise."
    },
    "ChIJ17m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Azora Beach, kristal suları ve şık localarıyla Ksamil sahil şeridinde kentsel bir 'chic' atmosfere sahip en prestijli deniz kulübü duraklarından biridir. Gurme akşam yemekleri ve gün batımı partileriyle kentsel sosyal hayatın en elit ve modern deniz keyfini sunan buluşma adresidir.",
        "en": "Azora Beach is one of the most prestigious beach club stops on the Ksamil coast, featuring crystal waters and a chic urban atmosphere. With gourmet dinners and sunset parties, it is the most elite and modern social hub for enjoying the Adriatic seaside in style."
    },
    "ChIJ27m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Bella Vista Lounge, adından da anlaşılacağı gibi Ksamil'in 'en güzel manzarasını' panoramik olarak sunan kentsel bir prestijli sosyal kaçış durağıdır. Şık tasarımı ve iddialı içecek menüsüyle kentsel sosyal hayatın en çok fotoğraflanan ve tercih edilen prestijli rotaları arasındadır.",
        "en": "Bella Vista Lounge, as its name suggests, is a prestigious urban social escape stop offering 'the most beautiful view' of Ksamil panoramically. With its chic design and ambitious drink menu, it ranks among the most photographed and preferred prestige routes in social life."
    },
    "ChIJ37m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Sunset Beach Bar, her akşam Adriyatik üzerinde gerçekleşen renk cümbüşünü izlemek için Ksamil'deki en ideal ve samimi kentsel sosyal duraktır. Hafif müzik ve taze meyve kokteylleri eşliğinde sunulan kentsel konforuyla, kentin en sevilen kentsel sosyal kaçış noktalarından biridir.",
        "en": "Sunset Beach Bar is the ideal and friendly urban social stop in Ksamil to watch the explosion of colors over the Adriatic every evening. With comfort offered against a backdrop of ambient music and fresh fruit cocktails, it is one of the town's most beloved social escapes."
    },
    "ChIJ47m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "Kuga Beach Bar, kentsel dinamizmi ve denizin huzurunu birleştiren, gölge altındaki konforlu alanlarıyla Ksamil sahilinin en samimi lezzet duraklarından biridir. Gün boyu devam eden ferahlatıcı içecek sunumlarıyla kentsel sosyal hayatın sahil kentsel ruhunu en iyi yansıtan adresidir.",
        "en": "Kuga Beach Bar is one of the friendliest flavor stops on the Ksamil coast, merging urban dynamism and seaside calm with its comfortable shaded areas. With refreshing drink services throughout the day, it is the address best reflecting the town's coastal urban spirit."
    },
    "ChIJ57m_wQBrWxMR_M-mH4FuDqk": {
        "tr": "ORION Beach Bar, kentsel modernliği ve Adriyatik'in bakir doğasını birleştiren şık tasarımıyla Ksamil'in en prestijli kentsel sosyal kaçış duraklarından biridir. Modern locaları ve seçkin hizmet anlayışıyla kentsel sosyal yaşamın en elit ve aristokrat deniz keyfini sunan adresidir.",
        "en": "ORION Beach Bar is one of Ksamil's most prestigious urban social escape stops, featuring chic design that merges urban modernity with the Adriatic's wild nature. With modern cabanas and elite service, it offers the most aristocratic seaside experience in social life."
    },
    "ChIJZVB_lfFrWxMRQbjnMr97kUs": {
        "tr": "Butrint Müzesi, UNESCO Dünya Mirası Listesi'ndeki antik kentin tarihini anlatan kentsel bir kültür kalesidir. Roma, Bizans ve Venedik dönemlerine ait eserlerin sergilendiği bu alan, kentin binlerce yıllık geçmişine açılan en prestijli ve entelektüel kentsel tarih penceresidir.",
        "en": "Butrint Museum is an urban cultural stronghold showcasing the history of the UNESCO-listed ancient city. With artifacts from Roman, Byzantine, and Venetian eras, it serves as the most prestigious and intellectual urban history window opening up to the town's millennia-old past."
    }
}

for h in data["highlights"]:
    if h["id"] in updates:
        h["description"] = updates[h["id"]]["tr"]
        h["description_en"] = updates[h["id"]]["en"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Ksamil Batch 2 (43 venues). Total Ksamil Cleaned.")

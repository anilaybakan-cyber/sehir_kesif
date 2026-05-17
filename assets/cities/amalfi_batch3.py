import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
52: {'d': "Amalfi katedrali yakınında tarihi bir binada yer alan bu butik konak, köy misafirperverliğini modern konforla harmanlıyor. Taş merdivenleri ve küçük terasıyla Orta Çağ sokaklarına açılan Locanda, şehrin tarihi dokusunun tam ortasında geçirilecek bir gece için biçilmiş kaftandır.",
    'de': "Located in a historic building near Amalfi's cathedral, this boutique guesthouse blends village hospitality with modern comfort. With stone stairways and a small terrace opening onto medieval streets, the Locanda is tailor-made for a night at the very heart of the town's historic fabric."},

57: {'d': "Amalfi'nin yüksek yamaçlarında konumlanan Hotel Panorama, adının hakkını veren koyun tamamını kaplayan deniz manzarası sunar. Aile işletmesi olan butik otelin kahvaltı terasında ev yapımı limonata ile sabaha başlamak, ziyaretçilerin vazgeçemediği anlardan birini oluşturur.",
    'de': "Perched on Amalfi's high slopes, Hotel Panorama lives up to its name with a sea view spanning the entire bay. Starting the morning with homemade lemonade on the breakfast terrace of this family-run boutique hotel is one of the moments guests never forget."},

58: {'d': "Amalfi merkezine yürüyüş mesafesindeki sakin bir konumda yer alan Hotel Santa Lucia, beyaz badanalı taş duvarlı odaları ve gül bahçeli terasıyla şehrin gürültüsünden uzaklaşmak isteyenler için huzurlu bir sığınak sunar.",
    'de': "Set in a quiet location within walking distance of central Amalfi, Hotel Santa Lucia offers whitewashed stone-walled rooms and a terrace with a rose garden, providing a peaceful refuge for those wishing to step away from the town's noise."},

60: {'d': "Ravello'nun tarihi merkezinde aile tarafından işletilen Hotel Giordano, Tyrrhen denizine uzanan manzarası ve limoncellosu ünlü bahçesiyle birleşiyor. Sakin terası ve yerel kahvaltı seçenekleriyle güne güzel bir başlangıç yapmak için mükemmel bir yerdir.",
    'de': "Family-run in the historic center of Ravello, Hotel Giordano combines its Tyrrhenian Sea views with a garden famous for its homemade limoncello. Its peaceful terrace and local breakfast options make it a perfect place to start the day beautifully."},

62: {'d': "Vettica di Amalfi tepesindeki bu küçük restoran, 1959'dan bu yana taze balık ve ahtapot risottosuyla Amalfi Sahili'nde söz sahibidir. Terastan görülen sahil panoraması, deniz ürünlü makarna tabağına eşlik eden bedelsiz manzara hediyesidir.",
    'de': "Perched in Vettica di Amalfi since 1959, this small restaurant has built its reputation on the Amalfi Coast with fresh fish and octopus risotto. The coastal panorama from its terrace is a priceless scenic companion to your seafood pasta plate."},

63: {'d': "Ravello'nun en huzurlu köşelerinden birine yerleşmiş bu lüks villa, özel havuzu ve panoramik terasıyla çiftler ile aileler için unutulmaz bir konaklama sağlar. Kahvaltıda sunulan ev yapımı limon reçeli ve taze meyve suları, Kampanya'nın bolluğuyla güne başlatır.",
    'de': "Set in one of Ravello's most serene corners, this luxury villa with its private pool and panoramic terrace provides an unforgettable stay for couples and families. Homemade lemon marmalade and fresh juices at breakfast start the day with the full abundance of Campania."},

67: {'d': "Positano'nun üst mahallelerindeki bu aile restoranı, elde yapılmış gnocchi, yöresel keklik otu soslu tavuk ve ev yapımı tatlılarıyla Güney İtalya ev mutfağının sıcaklığını aktarır. Küçük ve sakin ortamı, samimi bir öğle yemeği için mükemmel bir seçimdir.",
    'de': "This family restaurant in Positano's upper quarters conveys the warmth of Southern Italian home cooking through its handmade gnocchi, local thyme-sauced chicken, and homemade desserts. Its small and quiet setting makes it a perfect choice for an intimate lunch."},

69: {'d': "Amalfi merkezi yakınında tarihi bir binada konumlanan Hotel Bonadies, modern çizgilerle tarihi dokuyu harmanlayan odaları ve geniş pencereleriyle şehir merkezine yürüme mesafesinde konforlu bir konaklama sunar. Kahvaltı büfesindeki taze portakal suyu ve yerel pastacılık ürünleri güne güzel başlamanın yoludur.",
    'de': "Located in a historic building near central Amalfi, Hotel Bonadies offers comfortable accommodation within walking distance of the town center, combining modern furnishings with historic fabric through its spacious windows. Fresh orange juice and local pastries at the breakfast buffet provide a lovely start to the day."},

71: {'d': "Ravello'nun tarihi meydanındaki bu pastane-kafeterya, desfasato keki, limonlu krem tart ve el yapımı granita ile köyün tatlı durakları arasında birinci sıradadır. Yerel halkın çay saatlerinde dolup taşan bu küçük mekan, gerçek Ravello ruhunu yansıtır.",
    'de': "This pastry café on Ravello's historic square ranks first among the village's sweet stops with its desfasato cake, lemon cream tart, and handmade granita. Filled with locals during afternoon tea hours, this small spot reflects the true spirit of Ravello."},

73: {'d': "Valle delle Ferriere yürüyüş rotasının başlangıç noktasına yakın konumlanan Bar Della Valle, hiking öncesi espresso ve bricoche ile güne başlamak ya da zorlu parkurdan sonra buz gibi limonata içmek için biçilmiş kaftandır. Doğa severler arasında bilinen bir buluşma noktasıdır.",
    'de': "Conveniently positioned near the Valle delle Ferriere trailhead, Bar Della Valle is tailor-made for a pre-hike espresso and brioche or an ice-cold lemonade after the demanding trail. It is a well-known meeting point among nature enthusiasts."},

76: {'d': "Amalfi'nin tarihi dokusu içinde saklanan bu butik restoran, taze kremalı deniz ürünlü bruschetta, ızgara kalamari ve yerel peynir tabağıyla öne çıkar. Taş kemer duvarları ve sarı limon motifli dekorasyonuyla Güney İtalya kıyı mutfağını özgün bir atmosferde sunar.",
    'de': "Hidden within Amalfi's historic fabric, this boutique restaurant stands out with its freshly prepared creamy seafood bruschetta, grilled calamari, and local cheese board. Stone-arched walls and yellow lemon-motif décor serve Southern Italian coastal cuisine in a genuinely authentic setting."},

77: {'d': "1939'dan bu yana Minori'de faaliyet gösteren De Riso, Amalfi Sahili'nin limon tatlıları söz konusu olduğunda başvurulan isimdir. Maestro pasticciere Salvatore De Riso'nun imzalı Delizia al Limone pastası, rafine bir İtalyan tatlı ustasının erişebildiği zirvelerden birini temsil eder.",
    'de': "Operating in Minori since 1939, De Riso is the definitive name for Amalfi Coast lemon pastries. Master pastry chef Salvatore De Riso's signature Delizia al Limone represents one of the peaks achievable only by the finest Italian pastry masters."},

78: {'d': "Amalfi kıyısında beklenmedik bir yerde karşınıza çıkan bu Brezilya bistrosu, passionfruit caipirinha ve churrasco tostlarıyla görsel güzelliğin ötesinde damak çıkartan bir deneyim sunar. İtalyan ve Latin Amerika mutfağı karışımından doğan yaratıcı menüsü, uzun bir sahil gününün ardından farklı tat arayanlar için idealdir.",
    'de': "An unexpected find on the Amalfi coast, this Brazilian bistro delivers a palate-surprising experience with passion-fruit caipirinhas and churrasco toasts. Its creative menu born from Italian-Latin American fusion is ideal for those seeking something different after a long day on the coast."},

79: {'d': "Basit görünümüne aldanmayın; bu küçük liman büfesi, sabahın erken saatlerinde yerel balıkçıların taze yakaladığı ürünleri uygun fiyatlarla sunar. Ahtapot salatasından istiridyeye kadar sahilde ayakta yenen deniz ürünleriyle gerçek bir Güney İtalya liman deneyimi yaşarsınız.",
    'de': "Don't be fooled by its simple appearance; this small harbor counter offers freshly caught produce from local early-morning fishermen at honest prices. From octopus salad to oysters eaten standing at the waterfront, it delivers a truly authentic Southern Italian harbor experience."},

81: {'d': "Minori kasabasının bakımlı ara sokaklarında bulunan bu küçük pastane, limon kremalı sfogliatella ve kakao dolgulu cornetto ile bölgede ün kazanmıştır. Her sabah taş fırından yeni çıkan hamur işleri ve el çekimi espresso için yerel halkın tercihidir.",
    'de': "Found in Minori's well-kept side streets, this small pastry shop has gained a local reputation with its lemon cream sfogliatella and cocoa-filled cornetto. It is the daily preference of locals for stone-oven fresh pastries and hand-pulled espresso every morning."},

83: {'d': "Amalfi Sahili'nin bazen kavurucu öğle güneşinden sığınmak için ideal olan bu bar, taze limonluk, nane granita ve yöresel meyve smoothieleriyle sizi serinletiyor. Açık cephesi ve taze çiçeklerle dekore edilmiş iç mekan, kısacık bir mola için bile hoş bir duraktır.",
    'de': "An ideal refuge from the Amalfi Coast's sometimes scorching midday sun, this bar cools you with fresh lemonade, mint granita, and local fruit smoothies. Its open facade and fresh flower décor make it a pleasant stop even for the briefest of breaks."},

86: {'d': "Amalfi Sahili'nin eski Caffè Vittoria'sı, 19. yüzyıldan kalma art deco mobilyası ve ahşap tavanlı iç mekanıyla zaman içinde donakalmış gibi bir atmosfer taşır. Öğleden sonra burada bir espresso içmek ya da tarihi tezgahın önünde granita beklemek, başlı başına bir deneyimdir.",
    'de': "The historic Caffè Vittoria of the Amalfi Coast carries an atmosphere frozen in time with 19th-century art deco furnishings and a wooden-ceilinged interior. Sitting here for an afternoon espresso or waiting for a granita at the historic counter is an experience in itself."},

87: {'d': "Amalfi ile dağ köyleri arasındaki yol ayrımında yer alan bu küçük bakkal-bar, yerel halkın ekmek, zeytin ve peynir alışverişi yaptığı otantik bir duraktır. Sabah gazetesiyle espresso içmek ya da piknik malzemesi temin etmek için ideal olan bu mekan, turizmin dışında kalan gerçek Amalfi yaşamını gözlemleme fırsatı sunar.",
    'de': "Located at the junction between Amalfi and the mountain villages, this small grocer-bar is an authentic stop where locals pick up bread, olives, and cheese. Ideal for a morning coffee with the local paper or stocking up on picnic supplies, it offers a window into real Amalfi life outside the tourism bubble."},
}

apply_batch('amalfi.json', U)

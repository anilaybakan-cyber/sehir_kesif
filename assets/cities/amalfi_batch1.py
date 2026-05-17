import sys; sys.path.insert(0, '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
from fix_generic import apply_batch

U = {
1: {'d': "Amalfi'nin kalbi Piazza Duomo'da yükselen bu çeşme, şehrin hamisi Aziz Andreas'a adanmıştır. 14. yüzyıldan kalma mermer kabartmaları ve limon ağaçlarının gölgesinde katedral basamaklarına yaslanmış şekilde duran bu yapı, kentin en ikonik buluşma noktasıdır.",
    'de': "Standing in Piazza Duomo at the heart of Amalfi, this fountain is dedicated to Saint Andrew, the city's patron saint. Its 14th-century marble reliefs framed by lemon trees beside the cathedral steps make it the town's most iconic meeting point.",
    't': "Sabah erken saatlerde meydana gelin; turistler gelmeden çeşmeyi ve katedrali sakin bir şekilde fotoğraflayabilirsiniz.",
    'te': "Arrive early morning to photograph the fountain and cathedral steps before the crowds arrive."},

4: {'d': "Amalfi'nin hemen arkasındaki bu doğa koruma alanı, 5 km boyunca şelaleler, antik papirüs tarlaları ve Orta Çağ'dan kalma değirmen kalıntılarının arasından geçen nefes kesen bir yürüyüş güzergahı sunar. Boğan deresinin serin sularını takip eden patika, bölgenin en büyüleyici tropikal vadisine kapı aralar.",
    'de': "This nature reserve behind Amalfi offers a breathtaking 5 km hike past waterfalls, ancient papyrus groves, and medieval mill ruins. The trail follows the cool Boğan stream into the region's most mesmerizing tropical-feeling valley.",
    't': "Kaymaz tabanlı yürüyüş ayakkabısı şart; bazı bölümler kayalık ve ıslak. Öğleden önce çıkın, öğleden sonra sis basabilir.",
    'te': "Non-slip hiking shoes are essential as some sections are rocky and wet. Set out before noon as afternoon fog can roll in."},

11: {'d': "Ravello meydanında 1086 yılında inşa edilen bu katedral, Güney İtalya'nın en etkileyici Normann-Bizans eserlerinden biridir. İki süslü ambon üzerindeki renk cümbüşü mozaikler ve Aziz Pantaleone'nin kanını saklayan relik, her ziyaretçide derin bir etki bırakır.",
     'de': "Built in Ravello's main square in 1086, this cathedral is one of Southern Italy's finest Norman-Byzantine masterpieces. Its two ornate ambos with vivid mosaics and the relic of Saint Pantaleone's blood leave a lasting impression on every visitor.",
     't': "İçindeki müzeye de girin; 12. yüzyıldan kalma fildiş eserleri ve antik sikkeler mutlaka görülmeli.",
     'te': "Don't skip the museum inside — 12th-century ivory artifacts and ancient coins are well worth seeing."},

13: {'d': "Agerola'dan Nocelle'ye uzanan 7.8 km'lik bu efsanevi patika, Amalfi Sahili'nin en ünlü yürüyüş güzergahıdır. Uçurum kenarındaki teras tarlaları ve yüzyıllık zeytinlikler arasında ilerlerken Positano ile Capri'ye uzanan sonsuz mavi eşlik eder.",
     'de': "This legendary 7.8 km trail from Agerola to Nocelle is the most celebrated hike on the Amalfi Coast. Cliff-edge terraced orchards and centuries-old olive groves line the path while endless blue vistas to Positano and Capri accompany every step.",
     't': "Sabah 8'den önce yola çıkın; öğleden sonra kalabalık ve sıcak olur. Nocelle'de küçük bir kafede oturun.",
     'te': "Start before 8am as it gets crowded and hot in the afternoon. Sit at a small café in Nocelle at the trail's end."},

15: {'d': "Amalfi Sahili'nin en sakin kasabalarından biri olan Minori, deniz kıyısındaki antik Roma villa kalıntıları, taze limon reçeli satan bakkallar ve gürültüsüz plajıyla özgün bir kıyı deneyimi yaşatır. Büyük kasabalara kıyasla kalabalıktan uzak bu köy, sahilin gerçek yüzünü görmek isteyenler için idealdir.",
     'de': "One of the Amalfi Coast's most tranquil towns, Minori offers an authentic coastal experience through its seafront Roman villa ruins, family shops selling fresh lemon preserves, and an uncrowded beach. Compared to the larger towns, it shows the coast's real face to those who seek it.",
     't': "Sahildeki Roma villasının girişi ücretsizdir; mozaik zeminler ve antik havuz özellikle görülmeye değer.",
     'te': "Entry to the Roman villa ruins on the seafront is free — the mosaic floors and ancient pool are particularly worth seeing."},

17: {'d': "Asırlık 'colatura di alici' ançuez sosuyla dünya mutfağında kendine özgü bir yer edinen Cetara, renkli evlerin sıralandığı limanı ve taze balık restoranlarıyla Amalfi Sahili'nin en otantik balıkçı köyüdür. Her Aralık düzenlenen Colatura Festivali kasabayı mutfak tutkunlarıyla doldurur.",
     'de': "World-renowned for its centuries-old 'colatura di alici' anchovy sauce, Cetara is the Amalfi Coast's most authentic fishing village, with a colorful harbor and fresh-catch restaurants. Each December the Colatura Festival fills the town with food lovers from across the globe.",
     't': "Limandaki küçük dükkanlardan cam şişelerde colatura di alici satın alın; ev yemeklerinde kullanmak için mükemmel bir hediye.",
     'te': "Pick up glass-bottled colatura di alici from small harbor shops — a perfect culinary souvenir to use at home."},

18: {'d': "Amalfi Sahili'nin giriş kapısı Vietri sul Mare, el yapımı majolika çinileriyle ünlü bir seramik kentidir. Renk renk çiçek ve deniz motifleriyle bezeli çiniler camii kubbelerinden kaldırım taşlarına kadar her yüzeyi süsler; atölyeler ziyaretçileri üretim sürecine ortak eder.",
     'de': "The gateway to the Amalfi Coast, Vietri sul Mare is a celebrated ceramics town famous for its hand-painted majolica tiles. Colorful floral and marine motifs adorn every surface from church domes to cobblestones, while workshops invite visitors to witness the craft firsthand.",
     't': "Bir seramik atölyesi turu önceden rezervasyon yapın; usta seramikçilerin yanında kendiniz de deneme yapabilirsiniz.",
     'te': "Book a ceramics workshop tour in advance — you can try painting alongside master craftspeople."},

20: {'d': "Deniz seviyesinin altında saklanan bu doğal mağara, dışarıdan sızan güneş ışığının su yüzeyinde kırılmasıyla oluşan eşsiz zümrüt-yeşili ışıltısıyla büyüler. Düşük bir kapıdan tekneyle sürüklenerek girilen mağaranın içinde balıkların gölgeleri duvarlarda dans eder.",
     'de': "Hidden below sea level, this natural cave mesmerizes with a unique emerald-green luminescence created by sunlight refracting through the water below. Reached by ducking through a low entrance by boat, the dancing shadows of fish play across its glowing walls.",
     't': "Sabah 10-12 arası ışık en güçlüdür; fotoğraf için ideal zaman. Tekne ve asansör olmak üzere iki giriş seçeneği var.",
     'te': "Light is most intense between 10am and noon — ideal for photography. Both boat access and an elevator are available."},

21: {'d': "Amalfi ile Positano arasına sıkışmış Praiano, dar taş merdivenlerden aşağıya inen küçük Marina di Praia koyu ve uçurumdan izlenen nefes kesen gündoğumuyla kalabalıktan kaçanlar için mükemmel bir sığınaktır. Geceleri liman ışıkları denizde yansır, büyülü bir atmosfer oluşur.",
     'de': "Tucked between Amalfi and Positano, Praiano is a perfect refuge for those escaping crowds, with its tiny Marina di Praia cove at the foot of narrow stone steps and breathtaking cliff-top sunrises. At night, harbor lights reflected in the sea create a magical atmosphere.",
     't': "Merdivenler çok dik; rahat spor ayakkabı giyin. Marina di Praia'da sabah erken saatler kalabalıksız ve yüzmek için ideal.",
     'te': "The steps are very steep — wear comfortable shoes. Early mornings at Marina di Praia are crowd-free and ideal for swimming."},

24: {'d': "Amalfi Sahili'nin en küçük ve en gizli köyü olan Conca dei Marini, falezin üstündeki Saracen Kulesi ve altındaki Grotta dello Smeraldo ile hem tarihe hem doğaya aynı anda dokunma fırsatı sunar. Turistlerin neredeyse uğramadığı bu köy, huzur arayanların gizli cenneti.",
     'de': "The smallest and most hidden village on the Amalfi Coast, Conca dei Marini offers simultaneous contact with history and nature through its cliff-top Saracen Tower and the Grotta dello Smeraldo below. Barely touched by tourists, it is a hidden paradise for those seeking peace.",
     't': "SS163 üzerindeki durak işaretini takip edin; park yeri çok sınırlı, dolmuş ya da tekneyle gitmek daha pratikdir.",
     'te': "Follow the stop signs on SS163; parking is very limited, so taking a local bus or boat is far more practical."},
}

apply_batch('amalfi.json', U)

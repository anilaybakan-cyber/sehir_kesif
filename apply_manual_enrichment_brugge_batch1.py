import json

# Manual enrichment data (Brugge Batch 1: 40 items)
updates = {
    "Jan van Eyckplein": {
        "description": "Flaman resim sanatının babası kabul edilen ünlü ressam Jan van Eyck'in heykelinin bulunduğu, ortaçağda ticaret limanı olarak kullanılan tarihi meydan. Kanalların kesiştiği bu pittoresk köşe, kafeleri ve antik binaları ile şehrin en fotoğrafik noktalarından.",
        "description_en": "A historic square where the statue of famous painter Jan van Eyck, considered the father of Flemish painting, stands, once used as a trading port in medieval times. This picturesque corner where canals intersect is one of the city's most photogenic spots with its cafes and antique buildings."
    },
    "Sint-Janshospitaal": {
        "description": "800 yılı aşkın tarihiyle Avrupa'nın en eski hastanelerinden biri, şimdi ortaçağ tıbbı ve ünlü ressam Hans Memling'in şaheserlerini sergileyen müze. Gotik mimarisi, antik eczanesi ve dini sanat eserleriyle benzersiz bir kültürel deneyim.",
        "description_en": "One of Europe's oldest hospitals with over 800 years of history, now a museum exhibiting medieval medicine and masterpieces by famous painter Hans Memling. A unique cultural experience with Gothic architecture, antique pharmacy, and religious art."
    },
    "Bonifacius Bridge": {
        "description": "Brugge'ün en romantik ve fotojenik köprüsü, kırmızı tuğla evler ve gotik kuleler arasından süzülen dar bir kanal üzerinde yer alıyor. 19. yüzyılda inşa edilmesine rağmen, ortaçağ masallarından fırlamış gibi görünümüyle efsane olmuş bir aşk köprüsü.",
        "description_en": "Bruges' most romantic and photogenic bridge, located over a narrow canal flowing between red brick houses and Gothic towers. Despite being built in the 19th century, a legendary love bridge with an appearance as if stepped out of medieval fairy tales."
    },
    "Jeruzalemkerk": {
        "description": "Adornes ailesi tarafından 15. yüzyılda Kudüs Kutsal Kabir Kilisesi'ne benzetilerek yaptırılan özel mülk kilise. Orijinal ortaçağ vitrayları, korkunç çarmıh sahneleri ve yeraltı mezarı ile şehrin en gizemli dini yapısı.",
        "description_en": "A private chapel built by the Adornes family in the 15th century to resemble the Church of the Holy Sepulchre in Jerusalem. The city's most mysterious religious structure with original medieval stained glass, terrifying crucifixion scenes, and underground tomb."
    },
    "Gentpoort": {
        "description": "Brugge'ün günümüze ulaşan dört ortaçağ şehir kapısından biri, 15. yüzyıldan kalma etkileyici savunma yapısı. Gent şehrine giden yol üzerindeki bu anıtsal kapı, şehrin bir zamanlar surlarla çevrili olduğunun canlı kanıtı.",
        "description_en": "One of Bruges' four surviving medieval city gates, an impressive defensive structure from the 15th century. This monumental gate on the road to Ghent is living proof that the city was once surrounded by walls."
    },
    "Torture Museum Oude Steen": {
        "description": "Eski bir hapishanede kurulan, ortaçağ Avrupa'sının karanlık yargı ve ceza sistemini gözler önüne seren müze. Gerçek işkence aletleri, idam yöntemleri ve korkutucu hikayelerle, tarihin karanlık yüzüyle yüzleşme.",
        "description_en": "A museum established in an old prison revealing the dark judicial and punishment system of medieval Europe. Confronting history's dark face with real torture instruments, execution methods, and frightening stories."
    },
    "Lumina Domestica": {
        "description": "Dünyanın en büyük lamba koleksiyonlarından birine ev sahipliği yapan, 6.000 antik lamba ve aydınlatma cihazı sergileyen ilginç müze. Meşale çağından elektriğe uzanan aydınlatma tarihinin büyüleyici yolculuğu.",
        "description_en": "An interesting museum housing one of the world's largest lamp collections, exhibiting 6,000 antique lamps and lighting devices. A fascinating journey through lighting history from the torch era to electricity."
    },
    "Gruuthusemuseum": {
        "description": "15. yüzyılda Brugge'ün en güçlü ailelerinden birinin sarayında kurulan, şehrin zengin tarihini ve aristokrat yaşamını sergileyen kapsamlı müze. Goblenler, dantel, silahlar ve dönem mobilyalarıyla, Flaman lüksüne dalış.",
        "description_en": "A comprehensive museum established in the 15th-century palace of one of Bruges' most powerful families, exhibiting the city's rich history and aristocratic life. A dive into Flemish luxury with tapestries, lace, weapons, and period furniture."
    },
    "Godshuizen": {
        "description": "Ortaçağda yaşlılar ve yoksullar için hayır kurumları tarafından inşa edilen, beyaz badanalı tarihi almshouse evleri. Iç avluları çiçeklerle dolu bu huzurlu köşeler, Brugge'ün sosyal tarihine açılan pencereler.",
        "description_en": "Historic whitewashed almshouse homes built by charities for the elderly and poor in medieval times. These peaceful corners with courtyards full of flowers are windows into Bruges' social history."
    },
    "De Garre": {
        "description": "Şehrin en dar sokağında gizlenmiş, kendi özel birası 'Tripel de Garre'yi üreten efsanevi bira evi. Masalara yalnızca üç kadeh sınırı koyan %11 alkollü güçlü birasıyla, gerçek bira tutkunlarının hac yeri.",
        "description_en": "A legendary beer house hidden in the city's narrowest alley, producing its own special beer 'Tripel de Garre'. A pilgrimage site for real beer enthusiasts with its 11% alcohol strong beer limited to only three glasses per table."
    },
    "'t Brugs Beertje": {
        "description": "300'den fazla farklı Belçika birası sunan, bira tutkunlarının kutsal mekanı sayılan kült bar. Vintage posterleri, ahşap dekorasyonu ve bilgili personeli ile otantik bir Belçika bira deneyiminin adresi.",
        "description_en": "A cult bar considered the sacred place of beer enthusiasts, offering over 300 different Belgian beers. The address for an authentic Belgian beer experience with vintage posters, wooden decor, and knowledgeable staff."
    },
    "Otto Waffle Atelier": {
        "description": "Dantel desenlerini yansıtan özel yulaf waffle'ları ve yaratıcı tatlı sunumlarıyla öne çıkan butik waffle dükkanı. Geleneksel Belçika waffle'ından farklı, hafif ve artistik bir alternatif arayanların durağı.",
        "description_en": "A boutique waffle shop standing out with special oat waffles reflecting lace patterns and creative dessert presentations. A stop for those seeking a light and artistic alternative different from traditional Belgian waffles."
    },
    "The Chocolate Line": {
        "description": "Belçika çikolata ustası Dominique Persoone'un çılgın ve ödüllü çikolata kreasyonlarını sunan dünyaca ünlü atölye. Wasabi, bira ve acı biber gibi sıra dışı tatlarla, çikolata dünyasının sınırlarını zorlayan yaratıcı bir deneyim.",
        "description_en": "A world-famous workshop offering crazy and award-winning chocolate creations by Belgian chocolate master Dominique Persoone. A creative experience pushing the limits of the chocolate world with extraordinary flavors like wasabi, beer, and hot pepper."
    },
    "Frituur De Halve Maan": {
        "description": "Ünlü De Halve Maan bira fabrikasının hemen yanında, Belçika'nın efsanevi patates kızartmasını en otantik haliyle sunan friture dükkanı. Taze kesilmiş patatesler, çeşitli soslar ve soğuk bira eşliğinde mükemmel bir lezzet deneyimi.",
        "description_en": "A friture shop right next to the famous De Halve Maan brewery, offering Belgium's legendary fries in their most authentic form. A perfect taste experience with freshly cut potatoes, various sauces, and cold beer."
    },
    "Koningin Astridpark": {
        "description": "Turistik merkezden biraz uzakta, göletlerin, kuğuların ve yemyeşil ağaçların bulunduğu huzurlu şehir parkı. Koşu yolları, bank sıraları ve çocuk oyun alanlarıyla, yerel halkın günlük yaşamını deneyimlemek için ideal.",
        "description_en": "A peaceful city park slightly away from the tourist center with ponds, swans, and lush green trees. Ideal for experiencing local daily life with jogging paths, bench rows, and children's playgrounds."
    },
    "Sint-Janshuismolen": {
        "description": "Hala aktif olarak un öğüten ve içine girilebilen tarihi yel değirmeni. 1770'lerden kalma bu çalışan değirmen, Brugge'ün tarım geçmişine açılan canlı bir pencere ve kanalların panoramik manzarasını sunuyor.",
        "description_en": "A historic windmill still actively grinding flour that you can enter. This working mill from the 1770s offers a living window into Bruges' agricultural past and panoramic views of the canals."
    },
    "Concertgebouw": {
        "description": "21. yüzyılın başında inşa edilen, 30.000'den fazla terra cotta kiremitle kaplı çarpıcı çağdaş konser salonu ve kültür merkezi. Klasik müzikten çağdaş dansa geniş programıyla, Brugge'ün modern kültür yüzü.",
        "description_en": "A striking contemporary concert hall and cultural center built at the beginning of the 21st century, covered with over 30,000 terracotta tiles. The modern cultural face of Bruges with its wide program from classical music to contemporary dance."
    },
    "'t Zand": {
        "description": "Şehrin en büyük meydanı, altında büyük bir otoparkı barındıran ve haftalık pazarların kurulduğu canlı alan. Konser, festival ve etkinliklere ev sahipliği yapan bu geniş açıklık, yerel yaşamın nabzını tutmak için ideal.",
        "description_en": "The city's largest square, a lively area housing a large parking garage underneath and hosting weekly markets. This wide open space hosting concerts, festivals, and events is ideal for feeling the pulse of local life."
    },
    "Bourgogne des Flandres Brewery": {
        "description": "Kanal kenarında romantik konumuyla öne çıkan, geleneksel Flaman kırmızı birası üretilen butik bira fabrikası. Tur ve tadım seanslarıyla, şehrin su kenarında en atmosferik bira deneyimini sunan mekan.",
        "description_en": "A boutique brewery producing traditional Flemish red beer, standing out with its romantic canalside location. The venue offering the city's most atmospheric beer experience by the water with tours and tasting sessions."
    },
    "Ezelpoort": {
        "description": "Su ile çevrili hendekler arasında, kuğuların yüzdüğü masalsı ortamda yükselen 14. yüzyıldan kalma şehir kapısı. Gentpoort'tan sonra en iyi korunmuş kapı olarak, ortaçağ atmosferini hissetmek için mükemmel.",
        "description_en": "A 14th-century city gate rising in a fairytale setting among moats surrounded by water where swans swim. The second best-preserved gate after Gentpoort, perfect for feeling the medieval atmosphere."
    },
    "Concertgebouw Brugge": {
        "description": "Binlerce kırmızı pişmiş toprak kiremitle kaplı cephesiyle dikkat çeken modern mimari şaheseri. Akustik mükemmelliği, çağdaş tasarımı ve kaliteli kültürel programlarıyla, Brugge'ün sanat ve müzik merkezi.",
        "description_en": "A modern architectural masterpiece notable for its facade covered with thousands of red fired clay tiles. Bruges' art and music center with acoustic excellence, contemporary design, and quality cultural programming."
    },
    "Simon Stevinplein": {
        "description": "Ondalık kesir sisteminin mucidi matematikçi Simon Stevin'in heykelinin bulunduğu, kafeleri ve restoranlarıyla canlı meydan. Büyük Pazar'a yakın konumuyla, turistik keşif arasında mola vermek için ideal.",
        "description_en": "A lively square where the statue of mathematician Simon Stevin, inventor of the decimal system, stands, with cafes and restaurants. Ideal for taking a break during tourist exploration with its location near the Grote Markt."
    },
    "Walplein": {
        "description": "De Halve Maan bira fabrikasının önündeki şirin meydan, kestane ağaçlarının gölgesinde bira içmek için mükemmel. Küçük butikler, kafeler ve otantik Brugge atmosferiyle, sakin bir mola noktası.",
        "description_en": "A charming square in front of De Halve Maan brewery, perfect for drinking beer in the shade of chestnut trees. A quiet rest point with small boutiques, cafes, and authentic Bruges atmosphere."
    },
    "Wijngaardplein": {
        "description": "Begijnhof'un ana girişini oluşturan, kuğuların beslendiği nostaljik ve huzurlu küçük meydan. Minnewater parkına açılan bu romantik köşe, Brugge'ün en büyüleyici fotoğraf noktalarından biri.",
        "description_en": "A nostalgic and peaceful small square forming the main entrance to Begijnhof, where swans are fed. This romantic corner opening to Minnewater park is one of Bruges' most enchanting photo spots."
    },
    "Meebrug": {
        "description": "Brugge'ün en eski taş köprülerinden biri, dar kanalda ahşap evler ve tarihi binalar arasında konumlanan pittoresk yapı. Kalabalıktan uzak, otantik fotoğraf kareleri için mükemmel bir köşe.",
        "description_en": "One of Bruges' oldest stone bridges, a picturesque structure located among wooden houses and historic buildings on a narrow canal. A perfect corner for authentic photo frames, away from crowds."
    },
    "Peerdenbrug": {
        "description": "Meebrug'un hemen yanında, at heykelleriyle süslü zarif köprü. Yeşil sakinlikler ve tarihi binalarla çevrili bu nokta, kanal manzarası fotoğrafları için gizli bir mücevher.",
        "description_en": "An elegant bridge decorated with horse statues right next to Meebrug. This spot surrounded by green calm and historic buildings is a hidden gem for canal view photos."
    },
    "Groenerei": {
        "description": "Brugge'ün en yeşil ve huzurlu kanallarından biri, söğüt ağaçlarının suya değdiği romantik manzarasıyla ünlü. Tekne turlarının geçtiği bu kanal, şehrin doğayla iç içe geçmiş güzelliğini yansıtıyor.",
        "description_en": "One of Bruges' greenest and most peaceful canals, famous for its romantic scenery where willow trees touch the water. This canal where boat tours pass reflects the city's beauty intertwined with nature."
    },
    "Spiegelrei": {
        "description": "Jan van Eyck meydanından uzanan, suya yansıyan tarihi binaların görsel şöleni sunan kanal. Gece aydınlatmasıyla büyüleyici, gündüz ise canlı renkleriyle dikkat çeken fotojenik güzergah.",
        "description_en": "A canal extending from Jan van Eyck square offering a visual feast of historic buildings reflected in the water. A photogenic route enchanting with night lighting and notable for vibrant colors by day."
    },
    "Langerei": {
        "description": "Turistik merkezden biraz uzak, yerel yaşamı ve günlük Brugge'ü deneyimleyebileceğiniz sakin kanal. Balıkçılar, bisikletliler ve şehir halkının ritmiyle, otantik atmosferin tadını çıkarın.",
        "description_en": "A quiet canal slightly away from the tourist center where you can experience local life and daily Bruges. Enjoy the authentic atmosphere with fishermen, cyclists, and the rhythm of city folk."
    },
    "Potterierei": {
        "description": "Eski çömlekçilerin yerleşim yeri olan tarihi mahalle, taş evleri ve dar sokakları ile ortaçağ atmosferini yaşatan bölge. Onze-Lieve-Vrouw ter Potterie kilisesi ve müzesiyle, keşfedilmeyi bekleyen bir hazine.",
        "description_en": "A historic neighborhood that was the settlement of old potters, an area keeping medieval atmosphere alive with stone houses and narrow streets. A treasure waiting to be discovered with Onze-Lieve-Vrouw ter Potterie church and museum."
    },
    "St. Walburga Church": {
        "description": "Brugge'deki en etkileyici Barok kilisesi, muhteşem mermer sunağı ve ahşap heykelleriyle göz kamaştırıyor. Yaz akşamları organ konserlerine ev sahipliği yapan bu yapı, dini sanat ve müziğin buluşma noktası.",
        "description_en": "The most impressive Baroque church in Bruges, dazzling with its magnificent marble altar and wooden sculptures. This structure hosting organ concerts on summer evenings is where religious art and music meet."
    },
    "St. Giles Church": {
        "description": "13. yüzyıldan kalma, ünlü Flaman ressamların (Memling, Van Eyck) ibadet ettiği ve bazılarının gömüldüğü tarihi kilise. Sanat tarihine tutkulu olanlar için özel bir hac noktası.",
        "description_en": "A 13th-century historic church where famous Flemish painters (Memling, Van Eyck) worshipped and some were buried. A special pilgrimage point for those passionate about art history."
    },
    "English Convent": {
        "description": "17. yüzyılda İngiliz Katolik rahibeler tarafından kurulan, nadir bulunan kubbeli kilisesiyle dikkat çeken manastır. Huzurlu atmosferi ve tarihi önemi ile rehberli turlar eşliğinde ziyaret edilebilir.",
        "description_en": "A convent established by English Catholic nuns in the 17th century, notable for its rare domed church. Can be visited with guided tours for its peaceful atmosphere and historical significance."
    },
    "Karmelietenklooster": {
        "description": "Huzurlu bahçesi, ortaçağ kütüphanesi ve sessiz atmosferiyle bilinen aktif Carmelite manastırı. Şehrin kalabalığından kaçış arayan ziyaretçiler için meditasyon ve düşünce mekanı.",
        "description_en": "An active Carmelite monastery known for its peaceful garden, medieval library, and quiet atmosphere. A place of meditation and reflection for visitors seeking escape from the city's crowds."
    },
    "Godshuis De Vos": {
        "description": "1713 yılında kurulan, iç avlusu çiçeklerle bezeli tarihi almshouse. Brugge'ün sosyal tarihine ışık tutan bu huzurlu köşe, fotoğraf çekimi ve sakin bir mola için mükemmel.",
        "description_en": "A historic almshouse established in 1713 with its inner courtyard decorated with flowers. This peaceful corner shedding light on Bruges' social history is perfect for photography and a quiet break."
    },
    "Godshuis St Jozef": {
        "description": "Geleneksel Flaman mimarisini en iyi yansıtan tarihi hayır evi, beyaz badanalı cepheleri ve düzenli bahçesiyle dikkat çekiyor. Yaşlılar için inşa edilen bu sakin ortam, ortaçağ sosyal sisteminin canlı örneği.",
        "description_en": "A historic charitable house best reflecting traditional Flemish architecture, notable for whitewashed facades and tidy garden. This quiet environment built for the elderly is a living example of the medieval social system."
    },
    "Godshuis De Meulenaere": {
        "description": "17. yüzyıldan kalma, küçük bir şapeli ve iç avlusu olan tarihi almshouse. Brugge'ün hayırseverlik geleneğini yaşatan, huzurlu ve fotojenik bir köşe.",
        "description_en": "A 17th-century historic almshouse with a small chapel and inner courtyard. A peaceful and photogenic corner keeping Bruges' charity tradition alive."
    },
    "Park Sebrechts": {
        "description": "Eski bir özel bahçeden kamusal parka dönüştürülmüş, merkeze yakın gizli yeşil vaha. Romantik havuzları, gölgeli patikları ve sakin atmosferiyle, kalabalık sokaklardan kaçış noktası.",
        "description_en": "A hidden green oasis near the center, converted from an old private garden to public park. An escape point from crowded streets with romantic pools, shaded paths, and quiet atmosphere."
    },
    "Smedenvest": {
        "description": "Eski şehir surları boyunca uzanan, kanal manzaralı yeşil ve sakin yürüyüş güzergahı. Bisikletliler ve yürüyüşçüler için ideal, turistik kalabalıktan uzak bir rota.",
        "description_en": "A green and quiet walking route with canal views extending along old city walls. An ideal route for cyclists and walkers, away from tourist crowds."
    },
    "Baron Ruzettepark": {
        "description": "Kanal kenarında, modern düzenlemeleriyle dikkat çeken şehir parkı. Çocuk oyun alanları, bank sıraları ve güzel bitki örtüsüyle, yerel ailelerin tercih ettiği huzurlu bir yeşil alan.",
        "description_en": "A city park by the canal notable for modern landscaping. A peaceful green area preferred by local families with children's playgrounds, bench rows, and beautiful vegetation."
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

print(f"\n✅ Manually enriched {count} items (Brugge Batch 1).")

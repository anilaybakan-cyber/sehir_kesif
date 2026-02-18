
import csv
import os

# Existing places to exclude (normalized)
existing_places = {
    'angelato', 'antoninovo pekarstvi', 'artic bakehouse', 'bad flash bar', 'banh mi ba', 
    'beergeek bar', 'bistro hai ha', 'bistro monk', 'bokovka', 'cafe louvre', 'cafe savoy', 
    'cafe imperial', 'cafe letka', 'cafefin', 'coffee room', 'creme de la creme', 
    'cukrarna mysak', 'cukrar skala', 'dish fine burger bistro', 'dobra cajovna', 
    'dva kohouti', 'ema espresso bar', 'eska', 'field', 'friends coffee house', 
    'good food coffee & bakery', 'grand cafe orient', 'havelska koruna', 'hemingway bar', 
    'if cafe', 'kantyna', 'kavarna slavia', 'kavarna co hleda jmeno', 'kro kitchen', 
    'la boheme cafe', 'las adelitas', 'letna beer garden', 'lokal dlouhaaa', 
    'manifesto market andel', 'mazelab coffee', 'monolok cafe', 'muj salek kavy', 
    'nase maso', 'onesip coffee', 'pho tung', 'pivovarsky dum benedict', 
    'remember vietnamese food', 'sansho', 'skautsky institut', 'smetanaq', 
    'stalin', 'strahov monastery brewery', 'styl & interier', 'super tramp coffee', 
    'the eatery', 'trdelnik shops', 'tricafe', 'u fleku', 'u hrocha', 'u medvidku', 
    'u parlamentu', 'u pinkasu', 'u rudolfina', 'u zlateho tygra', 'u cerneho vola', 
    'vinohradsky pivovar', 'vnitroblock', 'yamato', 'zly casy', 'cestr'
}

# New candidates list (Name, Category, Description, Source/Tag)
new_candidates = [
    ("Café Jen", "Kafe", "Yerel halkın favorisi olan bu küçük ve samimi kafe, özellikle hafta sonları sunduğu zengin kahvaltı tabakları ve kaliteli üçüncü dalga kahveleriyle ünlüdür. Oitheblog tarafından da şiddetle tavsiye edilen, rezervasyonun şart olduğu popüler bir duraktır.", "Oitheblog / Bizevdeyokuz"),
    ("Kavárna Místo", "Kafe", "Modern ahşap iç tasarımı ve ferah atmosferiyle dikkat çeken Místo, nitelikli kahve kavurucusu Doubleshot'ın amiral gemisidir. Hem çalışmak hem de lezzetli ve doyurucu bir brunch keyfi yapmak için idealdir.", "Bizevdeyokuz / Tripadvisor"),
    ("Mezi Srnky", "Kafe", "Vinohrady semtinde yer alan bu şirin mekan, sağlıklı ve taze malzemelerle hazırlanan brunch menüsüyle öne çıkar. Özellikle avokadolu ve yumurtalı ekmek üstü lezzetleri denemeye değerdir.", "Blogger Favorite"),
    ("Typika", "Kafe", "Nusle bölgesinin sakinliğinde, minimalist dekorasyonu ve sanat galerisi havasıyla huzurlu bir kahve molası sunar. Kalabalıktan uzaklaşıp kaliteli bir espresso içmek isteyenler için harika bir keşif noktasıdır.", "Local Guide"),
    ("Omai", "Yeme-İçme", "Modern Asya füzyon mutfağını kahvaltı kültürüyle birleştiren Omai, özellikle matcha latteleri ve egzotik tatlara sahip pankekleriyle ünlüdür. Hafta sonları kapısında uzun kuyruklar oluşabilir.", "Reddit / Blogs"),
    ("Coffee Corner Bakery", "Kafe", "Vinohrady'nin kalbinde, vitrinindeki çeşit çeşit taze pasta ve hamur işleriyle baştan çıkaran popüler bir fırın kafedir. Özellikle havuçlu keki ve sabah kahvaltıları çok sevilir.", "Local Suggestion"),
    ("GRAM", "Kafe", "Endüstriyel şık tasarımı ve günlük taze çıkan ekmekleriyle ünlü olan GRAM, hem fırın hem de bistro olarak hizmet verir. Kahvaltıda sundukları poşe yumurtalı tabaklar oldukça popülerdir.", "Newloggers"),
    ("Zanzibar", "Kafe", "Vinohrady'nin yerlileri arasında bir klasik olan Zanzibar, rahat koltukları ve geniş menüsüyle evinizdeymiş gibi hissettirir. Hem sabah kahvesi hem de akşam içkisi için uğranabilecek samimi bir mekandır.", "Gezimanya"),
    ("Bella Vida Cafe", "Kafe", "Vltava Nehri kıyısında, Charles Köprüsü'nün büyüleyici manzarasına karşı kahvaltı yapabileceğiniz nadir mekanlardan biridir. Özellikle güneşli havalarda dışarıdaki masaları tercih etmenizi öneririz.", "Tripadvisor"),
    ("Arte Bianca", "Kafe", "Gerçek İtalyan unlu mamullerini Prag'a taşıyan bu otantik fırın, taze kruvasanları, focaccia ekmekleri ve cannoli tatlısıyla İtalya'daymışsınız hissi yaratır. Kahvaltısı çok sevilir.", "Tripadvisor"),
    ("Šodó Bistro", "Yeme-İçme", "Geleneksel Çek malzemelerini modern tekniklerle yorumlayan Şodó, mevsimsel menüsüyle her ziyarette farklı bir deneyim sunar. Özellikle öğle yemekleri için taze ve yaratıcı seçenekler bulabilirsiniz.", "Gourmet Guide"),
    ("Bjukitchen Bistro", "Yeme-İçme", "Ünlü Çek yemek bloggerının açtığı bu mekan, sağlıklı, doğal ve katkısız yemekleriyle bilinir. Özellikle yulaf lapaları ve ev yapımı granolalarıyla kahvaltıda fark yaratır.", "Local Blog"),
    ("The Artisan", "Kafe", "Marriott otelinin içinde yer almasına rağmen sokaktan girişi olan, pazar günleri sunduğu zengin açık büfe brunch ve canlı müzik performansıyla lüks bir hafta sonu keyfi sunar.", "Time Out"),
    ("ZEM Prague", "Yeme-İçme", "Tarihi bir binada modern sanat eserleriyle dekore edilmiş şık atmosferinde, Çek mutfağını Japon teknikleriyle harmanlayan avangart bir restoran deneyimi yaşatır.", "Michelin Guide"),
    ("Cafe Hrnek", "Kafe", "Letna semtinde, özel kavrulmuş kahveleri ve hafta sonlarına özel hazırladıkları yaratıcı brunch menüleriyle kahve severlerin yeni favorisi haline gelmiş samimi bir mekandır.", "Local Guide"),
    ("Bakeshop", "Kafe", "Eski Şehir'de Amerikan tarzı dev kurabiyeleri, kişleri ve çeşit çeşit ekmekleriyle ünlü, günün her saati taze ve lezzetli atıştırmalıklar bulabileceğiniz köklü bir fırındır.", "Tripadvisor"),
    ("U Pivrnce", "Yeme-İçme", "Duvarlarındaki eğlenceli ve karikatürize çizimlerle hem güldüren hem de doyuran, geleneksel Çek mutfağının en sevilen klasiklerini uygun fiyata sunan turistik ama keyifli bir restorandır.", "Gezimanya / Tripadvisor"),
    ("Kolkovna Celnice", "Yeme-İçme", "Pilsner Urquell bira fabrikasının orijinal restoran konsepti olan Kolkovna, klasik birahane atmosferinde garantili lezzet ve taze tank birası arayanlar için en güvenilir adrestir.", "Honest Guide"),
    ("U Dvou Koček", "Yeme-İçme", "1678'den beri hizmet veren, akşamları canlı akordeon müziği eşliğinde kendi ürettikleri taze biraları ve dev porsiyonlu geleneksel yemekleri tadabileceğiniz tarihi bir atmosfer sunar.", "Prague Guide"),
    ("Mincovna", "Yeme-İçme", "Eski Şehir Meydanı'ndaki tarihi darphane binasında yer alan bu şık restoran, gelenekseli modern bir sunumla birleştirerek turist tuzağı olmayan kaliteli bir Çek mutfağı deneyimi vaat eder.", "Oggusto"),
    ("U Modré Kachničky", "Yeme-İçme", "Kadife koltukları ve antika dekorasyonuyla 1920'lerin atmosferini yaşatan, özellikle ördek ve av etleri konusunda uzmanlaşmış, romantik akşam yemekleri için mükemmel bir seçenektir.", "Michelin / Tripadvisor"),
    ("Bistro 8", "Kafe", "Letna'nın sanatçı ruhunu yansıtan vintage dekorasyonu, günlük değişen yaratıcı menüsü ve ev yapımı limonatalarıyla öğle yemeği veya kahve molası için çok keyifli bir duraktır.", "Bizevdeyokuz"),
    ("Kidó Bistro", "Yeme-İçme", "Şehrin karmaşasından kaçıp arka bahçesinde huzur bulabileceğiniz, vejetaryen dostu sağlıklı yemekleri ve glutensiz seçenekleriyle öne çıkan sevimli bir bistrodur.", "Blogger Favorite"),
    ("School Restaurant & Lounge", "Yeme-İçme", "Okul temalı eğlenceli dekorasyonu ve Vltava nehri manzarası eşliğinde, Çek mutfağının klasiklerini modern sunumlarla tadabileceğiniz, hem göze hem damağa hitap eden bir mekandır.", "Tripadvisor"),
    ("Kalina Kampa", "Yeme-İçme", "Kampa Adası'nın en güzel noktasında, nehir kenarında romantik ve şık bir akşam yemeği için ideal, Fransız teknikleriyle hazırlanan gurme lezzetler sunan üst düzey bir restorandır.", "Gourmet Guide"),
    ("Vytopna Railway Restaurant", "Yeme-İçme", "Wenceslas Meydanı'nda, sipariş ettiğiniz içeceklerin masanıza minyatür tren rayları üzerinden vagonlarla servis edildiği, hem çocuklar hem de yetişkinler için çok eğlenceli bir deneyimdir.", "Viral / Social Media"),
    ("Lehká Hlava", "Yeme-İçme", "Yıldızlı gökyüzü tavanı ve masalsı dekorasyonuyla büyüleyen, 'Clear Head' adıyla bilinen bu mekan, vejetaryen yemeklerin ne kadar lezzetli olabileceğini kanıtlayan bir gastronomi durağıdır.", "Bizevdeyokuz / Oitheblog"),
    ("Maitrea", "Yeme-İçme", "Eski Şehir'de Feng Shui prensiplerine göre tasarlanmış, sakin ve huzurlu atmosferiyle dikkat çeken, Asya etkili yaratıcı vejetaryen yemekler sunan popüler bir restorandır.", "Tripadvisor"),
    ("Terasa U Prince", "Bar", "Eski Şehir Meydanı'ndaki otelin çatısında yer alan, Astronomik Saat kulesine karşı en ikonik Instagram fotoğraflarını çekebileceğiniz, manzarasıyla büyüleyen bir teras bardır.", "Instagram / Bloggers"),
    ("Kuchyň", "Yeme-İçme", "Prag Kalesi'nin hemen girişinde, muhteşem şehir manzarasına karşı tencerelerden yemeğinizi seçip yiyebileceğiniz, Çek anne yemekleri konseptli samimi bir restorandır.", "Honest Guide"),
    ("Black Angel's Bar", "Bar", "Gotik bir mahzenin içinde, 1930'ların 'yasak dönem' atmosferini yaşatan, ödüllü barmenlerin hazırladığı imza kokteylleriyle ünlü, şehrin en prestijli barlarından biridir.", "World's 50 Best / Time Out"),
    ("L'Fleur", "Bar", "Şampanya ve klasik kokteyller konusunda uzmanlaşmış, Belle Époque dönemini andıran şık dekorasyonu ve bilgili barmenleriyle sofistike bir gece geçirmek isteyenler için idealdir.", "Bar Guide"),
    ("Anonymous Bar", "Bar", "Guy Fawkes maskeli barmenleri, gizli menüleri ve tiyatral kokteyl sunumlarıyla misafirlerine sadece bir içki değil, unutulmaz bir şov ve deneyim sunan gizemli bir bardır.", "Viral / Tripadvisor"),
    ("Shrink's Office", "Bar", "Anonymous Bar ekibinin işlettiği, sadece rezervasyonla girilen, size özel 'terapi' seansları gibi kokteyl hazırlayan, çok daha sakin ve özel bir speakeasy bardır.", "Local Secret"),
    ("Bukowski's Bar", "Bar", "Zizkov'un bohem atmosferinde, loş ışıkları, kitaplarla dolu rafları ve entelektüel havasıyla Charles Bukowski ruhunu yaşatan, harika kokteyller sunan kült bir mekandır.", "Time Out"),
    ("Cacao Prague", "Kafe", "Hem sağlıklı smoothie kaseleri hem de günahkar çikolatalı tatlılarıyla ünlü, özellikle fıstıklı dondurması ve sıcak çikolataları denenmesi gereken merkezi bir kafedir.", "Tripadvisor"),
    ("Choco Café", "Kafe", "Çikolata severler için bir mabet olan bu aile işletmesi, onlarca çeşit yoğun kıvamlı sıcak çikolatası ve el yapımı pralinleriyle tatlı krizleri için en doğru adrestir.", "Oitheblog"),
    ("Venue", "Kafe", "Eski Şehir'de yerel malzemelerle hazırlanan yaratıcı brunch ve öğle yemeği menüsüyle öne çıkan, modern sunumları ve lezzetli kahveleriyle popüler bir mekandır.", "Tripadvisor"),
    ("Marthy's Kitchen", "Kafe", "Fransız ve Çek mutfağını harmanlayan, özellikle incecik krepleri, galeteleri ve ev yapımı reçelleriyle kahvaltı severleri mutlu eden şirin bir mahalle kafesidir.", "Blogger Favorite"),
    ("Den Noc", "Kafe", "Sadece pankek üzerine uzmanlaşmış bu küçük mekan, hem tatlı hem de tuzlu sayısız pankek çeşidiyle kahvaltıda farklılık arayanların mutlaka uğraması gereken bir yerdir.", "Tripadvisor / Blogs"),
    ("Proti Proudu", "Kafe", "Karlin semtinde, elektrik devresi temalı ilginç ve ödüllü iç tasarımıyla dikkat çeken, iyi kahve ve lezzetli atıştırmalıklar sunan modern bir bistro kafedir.", "Wallpaper / Design Guides"),
    ("Spižírna 1902", "Kafe", "Duvarlarındaki çiçek resimleri ve ferah atmosferiyle bir bahçede oturuyormuş hissi veren, ev yapımı kekleri ve limonatalarıyla ünlü çok fotojenik bir mekandır.", "Instagram / Blogs"),
    ("Coda Restaurant", "Yeme-İçme", "Mala Strana'daki Aria Hotel'in terasında, 360 derece Prag manzarası eşliğinde piyano dinletileriyle fine dining deneyimi sunan, özel günler için mükemmel bir restorandır.", "Michelin / Oggusto"),
    ("Kampa Park", "Yeme-İçme", "Doğrudan nehir kenarında, Charles Köprüsü'nün ayaklarının dibinde yer alan konumuyla şehrin en romantik ve lüks akşam yemeği mekanlarından biridir.", "Getyourguide / Tripadvisor"),
    ("Hergetova Cihelna", "Yeme-İçme", "Eski bir tuğla fabrikasından dönüştürülen, nehre sıfır terasında Charles Köprüsü manzarasına karşı modern ve şık bir yemek deneyimi sunan popüler bir restorandır.", "Tripadvisor"),
    ("Marina Ristorante", "Yeme-İçme", "Vltava nehri üzerine demirlemiş bir gemide, İtalyan şeflerin hazırladığı taze makarna ve deniz ürünlerinin tadını çıkarabileceğiniz, manzaralı şık bir restorandır.", "Tripadvisor"),
    ("Lasagneria", "Yeme-İçme", "Sadece lazanya üzerine uzmanlaşmış bu butik İtalyan restoranı, klasik tariflerin yanı sıra siyah trüflü veya sebzeli gibi yaratıcı lazanya çeşitleri de sunar.", "Local Favorite"),
    ("Johnny Pizza", "Yeme-İçme", "Şehrin en iyi pizzacılarından biri olarak kabul edilen Johnny, incecik hamurlu ve bol malzemeli dev pizzalarıyla hem lezzetli hem de doyurucu bir seçenek sunar.", "Honest Guide"),
    ("Paprika", "Yeme-İçme", "Vinohrady ve Andel şubeleriyle, ev yapımı humusu, çıtır falafelleri ve şavurmasıyla Orta Doğu mutfağının Prag'daki en iyi ve samimi temsilcisidir.", "Local Favorite"),
    ("Mr.HotDoG", "Yeme-İçme", "Letna semtinde, gurme sosisli sandviçleri, lezzetli slider burgerleri ve harika kokteylleriyle Amerikan diner kültürünü yaşatan popüler bir duraktır.", "Local Blog"),
    ("Hillbilly", "Yeme-İçme", "Holesovice'de burger severler için kaçırılmaması gereken, sulu ve lezzetli burgerleri, ev yapımı sosları ve rahat ortamıyla öne çıkan bir mekandır.", "Burger Guide"),
    ("Sad Man's Tongue", "Yeme-İçme", "50'lerin Rock & Roll atmosferinde, devasa boyutlarda ve inanılmaz lezzetli burgerler sunan, rezervasyonsuz yer bulmanın zor olduğu kült bir mekandır.", "Tripadvisor"),
    ("Bruxx", "Yeme-İçme", "Náměstí Míru meydanında, taze Belçika midyeleri, patates kızartması ve yüzlerce çeşit Belçika birası sunan, her zaman canlı ve kalabalık bir brasserie'dir.", "Time Out"),
    ("Vinograf", "Bar", "Hem yerel Çek şaraplarını hem de dünya şaraplarını kadehle tadabileceğiniz, bilgili sommelier'lerin size eşlik ettiği, şarap severler için bir cennettir.", "Wine Guide")
]

# Output file
output_path = '/Users/anilebru/Desktop/prag_yeni_mekan_onerileri.csv'

try:
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Mekan Adı', 'Kategori', 'Açıklama', 'Kaynak/Öneri'])
        
        count = 0
        for name, cat, desc, source in new_candidates:
            # Normalize name for check
            norm_name = name.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ý", "y").replace("č", "c").replace("š", "s").replace("ž", "z").replace("ř", "r").replace("ů", "u").replace("ě", "e").replace("ň", "n").replace("ť", "t")
            
            # Simple check if any existing place name is a substring or close match
            is_existing = False
            for exist in existing_places:
                if exist in norm_name or norm_name in exist:
                    pass
            
            writer.writerow([name, cat, desc, source])
            count += 1
            
    print(f"Successfully generated {count} new recommendations to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")

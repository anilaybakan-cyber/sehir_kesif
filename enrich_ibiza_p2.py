#!/usr/bin/env python3
import json

updates = {
    "ChIJrxf1VyxEmRIRplqUErzS56Y": {
        "description": "Playa d'en Bossa'nın kalbinde yer alan Murphy's, İrlanda barı konseptini İbiza'nın enerjik gece hayatıyla birleştiriyor. Canlı spor yayınları, geniş bira seçkisi ve sabahın erken saatlerine kadar süren neşeli atmosferiyle, hem yerel mola vermek hem de partiye ısınmak için adanın en samimi duraklarından biridir.",
        "description_en": "Located in the heart of Playa d'en Bossa, Murphy's combines the Irish bar concept with Ibiza's energetic nightlife. With live sports broadcasts, a wide beer selection, and a cheerful atmosphere lasting until the early hours, it's one of the island's most sincere stops to take a local break or warm up for the party."
    },
    "ChIJ8WopDktBmRIRM3IYSSPa4XM": {
        "description": "Marina Botafoch'un şık atmosferinde yer alan Bubbles, kaliteli müzik ve seçkin bir kitleyi buluşturan sofistike bir gece kulübüdür. Modern tasarımı ve etkileyici ses sistemleriyle İbiza'nın marinadaki kozmopolit lüksünü yansıtan mekan, gecenin ilerleyen saatlerinde dans ve eğlence için adanın favori adreslerindendir.",
        "description_en": "Located in the chic atmosphere of Marina Botafoch, Bubbles is a sophisticated night club bringing together quality music and an elite crowd. Reflecting Ibiza's cosmopolitan luxury in the marina with modern design and impressive sound systems, the venue is a favorite for late-night dance and fun on the island."
    },
    "ChIJH7c0o5hHmRIRE59isATlHEo": {
        "description": "Sadece bilenlerin uğradığı bir saklı bahçe gibi olan Underground, ticari müzikten uzak, gerçek 'Ibiza vibe'ını hissetmek isteyenlerin buluşma noktasıdır. Minimalist dekoru ve yerel halkla kaynaşan kozmopolit kitlesiyle, adanın en özgün ve samimi gece hayatı deneyimlerinden birini sunar.",
        "description_en": "Like a hidden garden visited only by those in the know, Underground is the meeting point for those wanting to feel the real 'Ibiza vibe' away from commercial music. With minimalist decor and a cosmopolitan crowd mingling with locals, it offers one of the island's most authentic and sincere nightlife experiences."
    },
    "ChIJ6_sc8clGmRIRX9mkd_g109M": {
        "description": "Marina Ibiza'da onlarca yıllık geçmişiyle bir klasik olan Keeper, hem yerel denizcilerin hem de elit gezginlerin favori barlarından biridir. Marinaya hakim konumu ve nostaljik şıklığıyla, akşamüstü kokteylinizi içerken İbiza'nın en havalı yatlarını ve Dalt Vila manzarasını izleyebileceğiniz ikonik bir duraktır.",
        "description_en": "A classic with decades of history in Marina Ibiza, Keeper is one of the favorite bars for both local sailors and elite travelers. With its position overlooking the marina and nostalgic elegance, it's an iconic stop where you can watch Ibiza's coolest yachts and the Dalt Vila view while sipping your late afternoon cocktail."
    },
    "ChIJt9rbr7NGmRIRb6e0IXxOdmQ": {
        "description": "İbiza kenti sakinlerinin ve tatilcilerin buluşma noktası olan bu samimi yerleşke, adanın modern ve yerel yaşamını bir arada sunuyor. Şık butikler, küçük kafeler ve kentin çarşısına yürüme mesafesindeki konumuyla, İbiza'nın gündelik ritmini en doğal haliyle soluyabileceğiniz keyifli bir mahalle dokusuna sahiptir.",
        "description_en": "This sincere settlement, a meeting point for Ibiza residents and vacationers, offers the island's modern and local life together. With its chic boutiques, small cafes, and location within walking distance of the city's bazaar, it has a pleasant neighborhood texture where you can breathe Ibiza's daily rhythm in its most natural form."
    },
    "ChIJ77Hk25dGmRIRl1AUbNxvztg": {
        "description": "Egzotik atmosferi ve geniş ürün seçkisiyle dikkat çeken bu alışveriş durağı, adanın renkli ve bohem tarzını yansıtan modern bir tasarım merkezidir. Şehrin kalbinde kendine has stiliyle öne çıkan mekan, tatilinize renk katacak özgün aksesuarlar ve adanın ruhunu taşıyan tasarımlar arayanların uğrak yeridir.",
        "description_en": "Attracting attention with its exotic atmosphere and wide product selection, this shopping stop is a modern design center reflecting the island's colorful and bohemian style. Standing out with its unique style in the heart of the city, the venue is a frequent spot for those seeking original accessories and designs carrying the island's spirit to color their holiday."
    },
    "ChIJI3bvGC1EmRIRJ6_GFrIjtuM": {
        "description": "Playa d'en Bossa'nın enerjik ruhunu temsil eden Tantra, adanın en hit parçalarını ve dünyaca ünlü DJ performanslarını sokağın nabzıyla birleştiriyor. Geniş terası ve sabahın ilk ışıklarına kadar süren neşeli atmosferiyle, büyük kulüplere gitmeden önce ısınmak veya geceyi burada noktalamak için İbiza'nın favorisidir.",
        "description_en": "Representing the energetic spirit of Playa d'en Bossa, Tantra combines the island's biggest hits and world-famous DJ performances with street energy. With its wide terrace and cheerful atmosphere lasting until the first light of morning, it is an Ibiza favorite to warm up before big clubs or end the night there."
    },
    "ChIJa3jSebtGmRIRsj_750w95sE": {
        "description": "Cala Jondal'da yer alan Blue Marlin, dünyanın en ünlü ve şık beach club'larından biri kabul edilir. Turkuaz sulara karşı konforlu locaları, gurme mutfağı ve gün boyu süren sofistike partileriyle, İbiza'nın jet-set yaşam tarzını ve Akdeniz lüksünü en rafine haliyle deneyimleyebileceğiniz prestijli bir adrestir.",
        "description_en": "Located in Cala Jondal, Blue Marlin is considered one of the world's most famous and chic beach clubs. With its comfortable booths against turquoise waters, gourmet cuisine, and sophisticated parties throughout the day, it is a prestigious address where you can experience Ibiza's jet-set lifestyle and Mediterranean luxury in its most refined form."
    },
    "ChIJBVwbj6OplxIRhOf4-duR1yM": {
        "description": "Cap des Falcó'nun vahşi doğasında, tuz göllerinin hemen kıyısında yer alan bu mekan, adanın en iyi korunan sırlarından biridir. Minimalist tasarımı ve denize düşen turuncu gün batımı manzarasıyla, doğayla iç içe, huzurlu ve kaliteli bir gastronomi-eğlence deneyimi arayanların vazgeçilmez sığınağıdır.",
        "description_en": "In the wild nature of Cap des Falcó, right on the edge of the salt pans, this venue is one of the island's best-kept secrets. With its minimalist design and orange sunset views falling into the sea, it is an indispensable sanctuary for those seeking a peaceful and high-quality gastronomy-entertainment experience intertwined with nature."
    },
    "ChIJSZhc3rpGmRIRz8qp7LwjCTc": {
        "description": "Antik Çağ'dan kalma Pön (Fenike) nekropolünün bir parçası olan bu sergi alanı, adanın derin arkolojik köklerine ışık tutuyor. Şehrin antik surlarının hemen altında yer alan bu alan, tarihin farklı dönemlerine ait mezarlar ve buluntularla İbiza'nın dünden bugüne uzanan mistik hikayesini sessizce anlatıyor.",
        "description_en": "Part of the ancient Punic (Phoenician) necropolis, this exhibition space sheds light on the island's deep archaeological roots. Located right under the city's ancient walls, this area silently tells Ibiza's mystical story stretching from yesterday to today with tombs and finds belonging to different historical periods."
    },
    "ChIJ_afXv7FGmRIRRlX8TkEAWTI": {
        "description": "İbiza'nın görsel ve işitsel hafızasını koruyan bu tarihi arşiv, adanın sanat ve kültür tarihine dair paha biçilemez dökümanlara ev sahipliği yapıyor. Eski kentin tarihi dokusu içindeki konumuyla, adanın müzik, sinema ve görsel sanatlar alanındaki gelişimini merak edenler için akademik bir duraktır.",
        "description_en": "Preserving Ibiza's visual and auditory memory, this historical archive hosts priceless documents related to the island's art and cultural history. With its location within the old town's historical texture, it is an academic stop for those curious about the island's development in music, cinema, and visual arts."
    },
    "ChIJ1yyQ7PpHmRIRepQV0iiBdgw": {
        "description": "Modern İbiza'nın sosyal sorumluluk ve dayanışma ruhunu temsil eden bu merkez, şehrin kalbinde kültürel etkinliklere ve toplumsal projelere ev sahipliği yapıyor. Kentin yaşayan ve gelişen dokusunu yakından tanımak isteyen gezginler için yerel yaşamın nabzını tutan, anlamlı bir toplumsal merkez duraktır.",
        "description_en": "Representing the social responsibility and solidarity spirit of modern Ibiza, this center hosts cultural events and social projects in the heart of the city. For travelers wanting to closely know the city's living and developing texture, it's a meaningful community center stop that keeps the pulse of local life."
    },
    "ChIJmZIyNbBGmRIRJTKMb3s73U8": {
        "description": "İbiza kenti Dalt Vila surları içerisinde, antik Madina Yabisa (Müslüman İbiza) tarihine dair etkileyici bir sergi sunan bu merkez, kentin Orta Çağ dönemini dijital ve interaktif yöntemlerle canlandırıyor. Surların içindeki konumuyla ziyaretçileri tarihin derinliklerinde büyüleyici bir yolculuğa çıkarıyor.",
        "description_en": "Located within the Dalt Vila walls of Ibiza city, this center presents an impressive exhibition about the history of ancient Madina Yabisa (Muslim Ibiza), bringing the city's Medieval era to life with digital and interactive methods. Its position within the walls takes visitors on a fascinating journey deep into history."
    },
    "ChIJ43sMNbBGmRIRVQbTz_tAg0Q": {
        "description": "Dalt Vila'nın en yüksek noktasında yer alan bu tarihi bina, yüzyıllarca kentin idari merkezi olarak kullanılmış, bugün ise adanın paha biçilemez arşivlerini ve mirasını koruyor. Heybetli kapısı ve taş mimarisiyle kentin güç ve tarih dengesini temsil eden en önemli anıtsal yapılardan biridir.",
        "description_en": "Located at the highest point of Dalt Vila, this historical building was used as the city's administrative center for centuries and today preserves the island's priceless archives and heritage. With its imposing gate and stone architecture, it is one of the most important monumental structures representing the city's balance of power and history."
    },
    "ChIJ8wOmtKxHmRIRtjIZJuH8AbY": {
        "description": "Dalt Vila surlarına gömülü etkileyici mimarisiyle İbiza Çağdaş Sanat Müzesi (MACE), 1960'lardan günümüze adadan ilham alan yerel ve uluslararası sanatçıların eserlerine ev sahipliği yapıyor. Modern sanatın adanın antik dokusuyla yarattığı kontrast, ziyaretçilere eşsiz bir estetik deneyim sunuyor.",
        "description_en": "With its impressive architecture embedded in the Dalt Vila walls, the Museum of Contemporary Art of Ibiza (MACE) hosts works by local and international artists inspired by the island from the 1960s to the present. The contrast that modern art creates with the island's ancient texture offers visitors a unique aesthetic experience."
    },
    "ChIJLR7yzSBHmRIRTARbBRHVz04": {
        "description": "Eski kentin en prestijli müzesi olan MAEF, Fenike, Kartaca ve Roma dönemlerinden kalma paha biçilemez buluntularla Akdeniz arkeolojisine ışık tutuyor. Özellikle kentin antik geçmişini ve Dalt Vila'nın nasıl inşa edildiğini anlamak isteyen tarih meraklıları için adadaki en kapsamlı ve bilgilendirici kültürel duraktır.",
        "description_en": "MAEF, the old town's most prestigious museum, sheds light on Mediterranean archaeology with priceless finds from Phoenician, Carthaginian, and Roman periods. Especially for history buffs wanting to understand the city's ancient past and how Dalt Vila was built, it is the most comprehensive and informative cultural stop on the island."
    },
    "ChIJh8wuLwBHmRIRzX59un-IG-s": {
        "description": "Dalt Vila'nın antik surları içerisinde yer alan bu tarihi baruthane, bugün kentin kültürel etkinliklerine ve geçici sergilerine ev sahipliği yapan mistik bir sanat galerisi olarak kullanılıyor. Taş oda yapısı ve akustik atmosferiyle, modern sanatın kentin tarihi derinliğiyle buluştuğu sessiz ve etkileyici bir keşif noktasıdır.",
        "description_en": "Located within the ancient walls of Dalt Vila, this historical powder magazine is today used as a mystical art gallery hosting the city's cultural events and temporary exhibitions. With its stone room structure and acoustic atmosphere, it's a quiet and impressive discovery point where modern art meets the city's historical depth."
    },
    "ChIJ_79IzsZHmRIRX-CdtK7GPRc": {
        "description": "İbiza kenti sokaklarını bir açık hava müzesine dönüştüren bu uluslararası sanat festivali, kentin silüetine devasa murallar ve dijital enstalasyonlarla modern bir ruh katıyor. Sanatın demokratikleşmesi ve sokağa taşması hedeflenen bu projeyle, kenti gezerken her köşede dünya çapında sanatçıların izlerine rastlayabilirsiniz.",
        "description_en": "Transforming the streets of Ibiza city into an open-air museum, this international art festival adds a modern spirit to the city's silhouette with giant murals and digital installations. With this project aiming for the democratization and street expansion of art, you can encounter traces of world-wide artists at every corner while wandering the city."
    },
    "ChIJG0aV3j9FmRIROFjqRGN-sSc": {
        "description": "Ses Salines Doğal Parkı'nın kalbinde yer alan bu merkez, adanın tuz üretim tarihine ve eşsiz biyolojik çeşitliliğine dair eğitici bir yolculuk sunuyor. Flamingo gözlem alanlarına yakınlığı ve doğayla iç içe konumuyla İbiza'nın ekolojik mirasını keşfetmek isteyenler için havadar ve huzurlu bir öğrenme durağıdır.",
        "description_en": "Located in the heart of the Ses Salines Natural Park, this center offers an educational journey about the island's salt production history and unique biodiversity. With its proximity to flamingo observation areas and location intertwined with nature, it is an airy and peaceful learning stop for those wanting to explore Ibiza's ecological heritage."
    },
    "ChIJtzOJ6yFAmRIRnhvMvNbvAEk": {
        "description": "Jesús köyü yakınlarında saklı bir sanat vahası olan Espacio Micus, ressam Eduard Micus'un mimarisiyle bütünleşen eserlerini sergiliyor. Minimalist beyaz yapısı ve adanın huzurlu kırsal doğası arasındaki bu galeri, kentin kozmopolit havasından uzaklaşıp saf sanatın ve sükunetin tadını çıkarmak isteyenlerin favorisidir.",
        "description_en": "A hidden art oasis near the village of Jesús, Espacio Micus exhibits painter Eduard Micus's works integrated with his architecture. This gallery between its minimalist white structure and the island's peaceful rural nature is a favorite for those wanting to escape the city's cosmopolitan air and enjoy pure art and tranquility."
    },
    "ChIJz9QiL1RPmRIRYnlYYf-O1Y4": {
        "description": "İbiza'nın en eski insan yerleşimi kalıntılarına (Sa Caleta) komşu olan bu merkez, adanın kadim Fenike köklerini ve Akdeniz'deki stratejik önemini anlatıyor. Kıyıdaki sarp kayalıklar üzerindeki konumu ve arkeolojik derinliğiyle İbiza'nın yaklaşık 3000 yıllık bir yerleşim tarihine sahip olduğunun sessiz ve vakur bir tanığıdır.",
        "description_en": "Neighboring the remains of Ibiza's oldest human settlement (Sa Caleta), this center tells of the island's ancient Phoenician roots and its strategic importance in the Mediterranean. With its position on steep coastal cliffs and its archaeological depth, it is a silent and dignified witness that Ibiza has a settlement history of approximately 3000 years."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/ibiza.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data.get('highlights', []):
    pid = place.get('id')
    if pid in updates:
        place['description'] = updates[pid]['description']
        place['description_en'] = updates[pid]['description_en']
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Ibiza Part 2: Enriched {count} items.")

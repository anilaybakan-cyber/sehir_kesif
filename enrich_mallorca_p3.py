#!/usr/bin/env python3
import json

updates = {
    "ChIJ1V0bimiSlxIRqkaGn4fmbrU": {
        "description": "Palma Marina'da yer alan Social Club, kentin en şık ve modern gece kulüplerinden biridir. Panaromik liman manzarasına hakim terası, etkileyici ses sistemi ve dünyaca ünlü DJ'lerin performanslarıyla İbiza atmosferini Mallorca'ya taşıyan bu mekan, adanın elit eğlence yaşamının kalbinde yer alır.",
        "description_en": "Located in Palma Marina, Social Club is one of the city's most stylish and modern night clubs. With its terrace dominating panoramic harbor views, impressive sound system, and world-famous DJ performances, this venue bringing the Ibiza atmosphere to Mallorca sits at the heart of the island's elite entertainment life."
    },
    "ChIJfQmM-XKSlxIRGgq3QksFMBY": {
        "description": "Mallorca gece hayatının nabzını tutan Level, iddialı tasarımı ve enerjik atmosferiyle kentin en popüler dans duraklarından biridir. Marina kıyısındaki konumu ve sabahın ilk ışıklarına kadar süren kaliteli müzik performanslarıyla, kentin kozmopolit enerjisini en yüksek seviyede hissedebileceğiniz bir eğlence merkezidir.",
        "description_en": "Catching the pulse of Mallorca's nightlife, Level is one of the city's most popular dance spots with its ambitious design and energetic atmosphere. With its location on the marina shore and high-quality music performances lasting until the first light of day, it's an entertainment center where you can feel the city me's cosmopolitan energy at its highest level."
    },
    "ChIJhzG2jBeTlxIRB2eQ_BzxCYU": {
        "description": "Playa de Palma'da yer alan bu neşeli ve tropikal esintili plaj kulübü, taze kokteylleri ve rahat atmosferiyle bilinir. Gündüz güneşin ve Akdeniz melteminin tadını çıkarırken akşamüstü başlayan hafif partilerle İbiza ruhunu yaşatan, kentin en havadar ve keyifli sahil duraklarından biridir.",
        "description_en": "Located in Playa de Palma, this cheerful and tropical-inspired beach club is known for its fresh cocktails and relaxed atmosphere. It is one of the city's most airy and pleasant coastal stops, keeping the Ibiza spirit alive with light parties starting in the afternoon while enjoying the sun and Mediterranean breeze by day."
    },
    "ChIJ4fvLfgySlxIR9bcWwOTRiaE": {
        "description": "Can Pastilla bölgesinde elektronik müzik ve kaliteyi buluşturan Lunita, adanın yeraltı (underground) eğlence kültürünün önemli temsilcilerinden biridir. Samimi tasarımı ve seçkin DJ performanslarıyla bildiğimiz mekan, kentin ticari kulüplerinden uzaklaşıp gerçek müzik tutkusuyla dans etmek isteyenlerin favorisidir.",
        "description_en": "Bringing together electronic music and quality in the Can Pastilla area, Lunita is one of the important representatives of the island's underground entertainment culture. Known for its sincere design and exclusive DJ performances, the venue is a favorite for those wanting to move away from commercial clubs and dance with real music passion."
    },
    "ChIJQTDCDE-SlxIRL1nCPY35RQE": {
        "description": "Eski kentin tarihi surları üzerinde görkemli bir sarayda yer alan Palacio Ca Sa Galesa, lüks ve tarihin en rafine birleşimidir. Katedralin hemen yanı başındaki konumu, şık antik dekorasyonu ve muazzam körfez manzaralı terasıyla, kendinizi bir Mallorcan asilzadesi gibi hissedeceğiniz paha biçilemez bir konaklama durağıdır.",
        "description_en": "Located in a grand palace on the ancient walls of the old town, Palacio Ca Sa Galesa is the most refined combination of luxury and history. With its position right next to the cathedral, chic antique decoration, and terrace featuring magnificent bay views, it is a priceless accommodation stop where you will feel like a Mallorcan nobleman."
    },
    "ChIJJfJCzlySlxIRQU9XFkDIKC4": {
        "description": "Kentin tarihi burçlarından birinin içine modern bir mimariyle inşa edilen Es Baluard, Mallorca'nın en önemli çağdaş sanat müzesidir. Miró'dan Picasso'ya kadar birçok sanatçının eserlerine ev sahipliği yapan müze, surların üzerinden sunduğu panaromik liman manzarasıyla hem sanatı hem de kentin güzelliğini harmanlar.",
        "description_en": "Built with modern architecture inside one of the city's historical bastions, Es Baluard is Mallorca's most important contemporary art museum. Hosting works by many artists from Miró to Picasso, the museum blends both art and the city me's beauty with the panoramic harbor views it offers from the walls."
    },
    "ChIJnc0_gU-SlxIRrJYz4R7JujE": {
        "description": "Mallorca Katedrali'nin (La Seu) içinde yer alan bu müze, kentin dini ve sanatsal mirasına ait paha biçilemez hazineleri barındırır. Gotik mimarinin ihtişamı altında sergilenen kutsal emanetler, antik dini objeler ve katedralin inşa sürecine dair detaylarla kentin manevi derinliğini keşfetmek için büyüleyici bir duraktır.",
        "description_en": "Located inside the Mallorca Cathedral (La Seu), this museum houses priceless treasures from the city's religious and artistic heritage. Exhibiting sacred relics, ancient religious objects under the grandeur of Gothic architecture, and details about the cathedral's construction, it is a fascinating stop to explore the city me's spiritual depth."
    },
    "ChIJNzS2ZE-SlxIRvTJjq7W5MPM": {
        "description": "Palma Piskoposluk Sarayı içinde yer alan bu müze, Mallorca'nın bin yıllık dini sanat tarihini gözler önüne seriyor. Orta Çağ tablolarından heybetli ayin kıyafetlerine kadar geniş bir koleksiyon sunan müze, kentin estetik ve ruhani geçmişine dair sessiz ve havadar bir keşif noktasıdır.",
        "description_en": "Located within the Episcopal Palace of Palma, this museum brings Mallorca's thousand-year religious art history to light. Offering a wide collection from medieval paintings to grand liturgical garments, the museum is a quiet and airy discovery point for the city me's aesthetic and spiritual past."
    },
    "ChIJKc7suFySlxIR4hlqFVNKaz0": {
        "description": "ABA ART, Mallorca'nın modern sanat dünyasına taze ve yaratıcı bir bakış sunan en şık galerilerinden biridir. Yerel ve uluslararası sanatçıların özgün eserlerine ev sahipliği yapan galeri, minimalist tasarımıyla sanatın ön plana çıktığı, kentin kültürel dokusuna derinlik katan modern bir mekandır.",
        "description_en": "ABA ART is one of Mallorca's most stylish galleries offering a fresh and creative look into the modern art world. Hosting original works by local and international artists, the gallery is a modern space where art takes center stage with its minimalist design, adding depth to the city's cultural texture."
    },
    "ChIJNVcyyVaSlxIRMXTpZUcUxD4": {
        "description": "Mallorca'nın askeri tarihini ve stratejik önemini sergileyen bu merkez, antik bir kışla binasında yer alıyor. Akdeniz'in savunma tarihine dair eski haritalar, üniformalar ve silah koleksiyonlarıyla kentin geçmişindeki kahramanlık hikayelerini ve jeopolitik gücünü anlamak için etkileyici bir duraktır.",
        "description_en": "Exhibiting Mallorca's military history and strategic importance, this center is located in an ancient barrack building. With old maps, uniforms, and weapon collections related to Mediterranean defense history, it's an impressive stop to understand the heroic stories and geopolitical power in the city me's past."
    },
    "ChIJo60sAl2SlxIR3jE0Z_iNgxg": {
        "description": "Palma'nın dar sokaklarında gizlenmiş bu karakteristik mekan, bir kafe atmosferini mistik ve gotik bir müze konseptiyle buluşturuyor. Sıra dışı dekorasyonu ve kentin efsanelerine atıfta bulunan objeleriyle, alışılmışın dışında havadar ve merak uyandırıcı bir mola vermek isteyen gezginler için keşfedilmesi gereken bir noktadır.",
        "description_en": "Hidden in Palma's narrow streets, this characteristic venue brings a cafe atmosphere together with a mystical and gothic museum concept. With unusual decoration and objects referring to city legends, it's a point to be discovered for travelers wanting to take an airy and intriguing break out of the ordinary."
    },
    "ChIJb2_W-nqSlxIRk1z6qeT3Mqk": {
        "description": "İspanya'nın farklı bölgelerine ait mimari şaheserlerin birer örneğinin sergilendiği Pueblo Español, kentin içinde adeta bir İspanya turu yapmanızı sağlar. El Hamra Sarayı'ndan Sevilla'nın avlularına kadar birçok ikonik yapının minyatür veya modelleriyle kentin kültürel çeşitliliğini ve birleştirici gücünü sergileyen havadar bir açık hava müzesidir.",
        "description_en": "Pueblo Español, exhibiting examples of architectural masterpieces from different regions of Spain, allows you to practically take a tour of Spain within the city. It's an airy open-air museum showcasing the city me's cultural diversity and unifying power with miniatures or models of many iconic structures from the Alhambra Palace to Seville's courtyards."
    },
    "ChIJFWdhrLmTlxIRDKdvs0AJ8Rg": {
        "description": "Denizin ekolojik mirasını ve Akdeniz'in biyolojik çeşitliliğini anlatan Aula de la Mar, kentin kıyı koruma bilincini yansıtan eğitici bir merkezdir. Deniz canlıları ve ekosistem üzerine interaktif sergileriyle çocuklar için harika bir öğrenme durağı olan mekan, Mallorca'nın masmavi doğasına duyulan saygıyı temsil eder.",
        "description_en": "Teaching the sea's ecological heritage and Mediterranean biodiversity, Aula de la Mar is an educational center reflecting the city me's coastal preservation awareness. A great learning stop for children with interactive exhibitions on marine life and ecosystems, the venue represents respect for Mallorca's deep-blue nature."
    },
    "ChIJ6RFzlAaSlxIRkYn8fwt7gLQ": {
        "description": "Palma Körfezi'ni koruyan tarihi bir kalede (Castell de Sant Carles) yer alan bu müze, kentin deniz savunma tarihine ışık tutuyor. Surların üzerinden sunduğu muazzam körfez manzarası ve antik toplardan savaş gemisi modellerine kadar zengin koleksiyonuyla hem tarih hem de manzara tutkunları için benzersizdir.",
        "description_en": "Located in a historical castle (Castell de Sant Carles) protecting Palma Bay, this museum sheds light on the city me's maritime defense history. It is unique for both history and view enthusiasts with the magnificent bay views it offers from walls and its rich collection ranging from ancient cannons to warship models."
    },
    "ChIJ18E5B_KNlxIRRnYzOJYHB_A": {
        "description": "Dünyaca ünlü sanatçı Joan Miró'nun Mallorca'daki çalışma alanı ve evi üzerine kurulu bu vakıf, modern sanatın dahi ruhunu yakından tanıma fırsatı sunuyor. Sanatçının atölyeleri, orijinal tuvalleri ve heybetli bahçesindeki heykelleriyle, kentin yaratıcı enerjisini sanatsal bir zirvede deneyimlemek için paha biçilemez bir duraktır.",
        "description_en": "Built on world-famous artist Joan Miró's workspace and home in Mallorca, this foundation offers a chance to closely know the genius spirit of modern art. With the artist's workshops, original canvases, and sculptures in its grand garden, it is a priceless stop to experience the city me's creative energy at an artistic peak."
    },
    "ChIJqafoD1SSlxIRICizVrt8rZQ": {
        "description": "Demiryolu tutkunları için bir cennet olan bu merkez, Mallorca'nın nostaljik tren ve istasyon kültürünü yaşatıyor. Eski lokomotifler, maket demiryolları ve tarihi dökümanlarla adanın ulaşım mirasına dair keyifli bir yolculuk sunan mekan, kentin endüstriyel geçmişini merak edenler için samimi bir keşif durağıdır.",
        "description_en": "A paradise for railway enthusiasts, this center keeps Mallorca's nostalgic train and station culture alive. Offering a pleasant journey through the island's transport heritage with old locomotives, model railways, and historical documents, the venue is a sincere discovery stop for those curious about the city me's industrial past."
    },
    "ChIJawpLFUWSlxIRhw66JjWD0sE": {
        "description": "Almudaina Sarayı yakınlarındaki tarihi bir konakta yer alan bu vakıf, nadir kitap koleksiyonu ve görkemli kütüphanesiyle kentin entelektüel hazinesidir. Mallorcan aristokrasisinin sanata ve bilime olan ilgisini yansıtan kütüphane ve heykel bahçesiyle, sessiz ve kaliteli bir kültürel derinlik arayanların adresidir.",
        "description_en": "Located in a historical mansion near the Almudaina Palace, this foundation is the city me's intellectual treasure with its rare book collection and grand library. With its library and sculpture garden reflecting the Mallorcan aristocracy's interest in art and science, it's the address for those seeking quiet and quality cultural depth."
    },
    "ChIJd9OzrbGTlxIRoZQY4t91wKM": {
        "description": "Adını Hırvat-Mallorcan ressam Kristian Krekovic'ten alan bu müze, kentin kozmopolit sanat bağlarını temsil ediyor. Sanatçının adanın ışığından ilham alarak yarattığı devasa tabloları ve karakteristik fırça darbeleriyle kentin sanatsal kimliğine özgün bir renk katan, keşfedilmesi gereken sessiz bir sanat durağıdır.",
        "description_en": "Named after the Croatian-Mallorcan painter Kristian Krekovic, this museum represents the city me's cosmopolitan art ties. It's a quiet art stop to be discovered, adding a unique color to the city me's artistic identity with the artist's giant paintings and characteristic brushstrokes inspired by the island's light."
    },
    "ChIJFTGVvk-SlxIRVSFZUObuq28": {
        "description": "Palma'nın tarihi Yahudi mahallesinin kalbinde yer alan bu merkez, kentin Orta Çağ'daki Yahudi toplumunun yaşamına ve kültürel mirasına ışık tutuyor. Dar sokakların arasındaki mistik atmosferi ve bilgilendirici sergileriyle kentin çok kültürlü geçmişini anlamak için paha biçilemez ve kutsal bir keşif duraktır.",
        "description_en": "Located in the heart of Palma's historical Jewish quarter, this center sheds light on the life and cultural heritage of the city me's Medieval Jewish community. With its mystical atmosphere among narrow streets and informative exhibitions, it is a priceless and sacred discovery stop to understand the city me's multicultural past."
    }
}

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/mallorca.json.draft'
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

print(f"✅ Mallorca Part 3: Enriched {count} items.")

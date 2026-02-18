
import json
import os
import glob

UPDATES = {
    ("Lyon", "A NOTRE TABLE"): {
        "tr": "Sıcak bir mahalle bistrosunda, mevsimlik malzemelerle hazırlanan klasik Fransız lezzetleri. Ördek konfit ve balık yemekleriyle ünlü.",
        "en": "Classic French flavors prepared with seasonal ingredients in a warm neighborhood bistro. Famous for duck confit and fish dishes."
    },
    ("Lyon", "Comptoir B"): {
        "tr": "Yaratıcı ve samimi bir neo-bistro deneyimi. Taze, mevsimsel ürünlerle hazırlanan özgün tabaklar ve sıcak bir atmosfer.",
        "en": "A creative and intimate neo-bistro experience. Original dishes prepared with fresh, seasonal products in a warm atmosphere."
    },
    ("Lyon", "Contrast."): {
        "tr": "Sofistike bir ortamda şaşırtıcı kokteyller ve tapaslar. Modern funk müzikleri eşliğinde yaratıcı bir akşam için ideal.",
        "en": "Surprising cocktails and tapas in a sophisticated setting. Ideal for a creative evening accompanied by modern funk music."
    },
    ("Lyon", "Le Bar à Vin Bio"): {
        "tr": "200'den fazla organik şarap seçeneği ve kömür ateşinde pişen lezzetler. Canlı ve samimi bir ortam.",
        "en": "Over 200 organic wine options and charcoal-grilled delights. A lively and friendly atmosphere."
    },
    ("Lyon", "Le PoliGone"): {
        "tr": "Lyon'da modern ve hareketli bir alışveriş ve yaşam merkezi. Mağazalar, restoranlar ve açık hava alanlarıyla keyifli bir durak.",
        "en": "A modern and bustling shopping and lifestyle center in Lyon. A pleasant stop with shops, restaurants, and outdoor areas."
    },
    ("Lyon", "MOFUSAN"): {
        "tr": "Fransız teknikleriyle Asya lezzetlerini buluşturan füzyon mutfak. Çay ve miso ile harmanlanmış yenilikçi tadım menüleri.",
        "en": "Fusion cuisine blending French techniques with Asian flavors. Innovative tasting menus blended with tea and miso."
    },
    ("Lyon", "The Coffee"): {
        "tr": "Minimalist Japon tasarımı ve Brezilya kahve kültürünün buluşması. Şehirde huzurlu bir kahve molası.",
        "en": "The meeting of minimalist Japanese design and Brazilian coffee culture. A peaceful coffee break in the city."
    },
    ("Lyon", "Vivants"): {
        "tr": "Doğal şaraplar, butik biralar ve harika pizzalar sunan rock ruhlu bir bar. Rahat ve samimi bir ortam.",
        "en": "A rock-spirited bar offering natural wines, craft beers, and great pizzas. A relaxed and friendly environment."
    },
    ("Marsilya", "Bucado"): {
        "tr": "Brezilya'nın canlı lezzetlerini Fransız teknikleriyle sunan şık bir mekan. Amazon ve Bahia esintili renkli tabaklar.",
        "en": "A stylish venue offering lively Brazilian flavors with French techniques. Colorful dishes inspired by the Amazon and Bahia."
    },
    ("Marsilya", "Ginger Phoenix"): {
        "tr": "Vietnam mutfağından ilham alan modern Asya lezzetleri. 80'ler stili renkli dekorasyonda tatlı ve baharatlı tatlar.",
        "en": "Modern Asian flavors inspired by Vietnamese cuisine. Sweet and spicy tastes in colorful 80s-style decor."
    },
    ("Marsilya", "Kin"): {
        "tr": "Orta Afrika köklerini Fransız bistro kültürüyle birleştiren yaratıcı mutfak. Şef Hugues Mbenda'dan mevsimsel ve neşeli tabaklar.",
        "en": "Creative cuisine combining Central African roots with French bistro culture. Seasonal and joyful dishes from Chef Hugues Mbenda."
    },
    ("Marsilya", "L'Imprévu"): {
        "tr": "İtalyan lezzetleri ve tapaslar sunan şenlikli bir mekan. Canlı müzik ve DJ performanslarıyla hareketlenen akşamlar.",
        "en": "A festive venue offering Italian flavors and tapas. Evenings that come alive with live music and DJ performances."
    },
    ("Marsilya", "La Gaudina"): {
        "tr": "Samimi bir ortamda sunulan Akdeniz ve Provençal lezzetler. Yerel malzemelerle hazırlanan burgerler ve tapaslar.",
        "en": "Mediterranean and Provençal flavors served in an intimate setting. Burgers and tapas prepared with local ingredients."
    },
    ("Marsilya", "La Mağarası de Baille"): {
        "tr": "Geniş şarap kavı ve şarküteri seçenekleriyle ünlü bir mahzen. Caz müzik eşliğinde keyifli tadım akşamları.",
        "en": "Cellar famous for its extensive wine cellar and charcuterie options. Delightful tasting evenings accompanied by jazz music."
    },
    ("Marsilya", "Le Comptoir de Becca"): {
        "tr": "Taze ve mevsimsel ürünlerle hazırlanan modern Fransız mutfağı. Şık sunumlar ve sıcak bir karşılama.",
        "en": "Modern French cuisine prepared with fresh and seasonal products. Stylish presentations and a warm welcome."
    },
    ("Marsilya", "Les Caves de l'Abbaye - Marseille 7ème"): {
        "tr": "Tarihi Saint-Victor Manastırı yakınında geniş bir şarap seçeneği ve şarküteri tabakları sunan otantik şarap barı.",
        "en": "Authentic wine bar offering a wide selection of wines and charcuterie platters near the historic Saint-Victor Abbey."
    },
    ("Marsilya", "Maison Jouglas"): {
        "tr": "Marsilya'nın geleneksel lezzetlerini sunan tarihi bir şarküteri ve fırın. Özellikle yerel spesiyaliteleriyle meşhur.",
        "en": "Historical deli and bakery offering traditional flavors of Marseille. Especially famous for local specialties."
    },
    ("Marsilya", "O'Bidul"): {
        "tr": "Küçük, samimi ve sadece öğle yemeklerinde açık olan popüler bir bistro. Şefin günlük değişen yaratıcı menüsü.",
        "en": "Small, intimate, and popular bistro open only for lunch. The chef's daily changing creative menu."
    },
    ("Marsilya", "Restaurant Chez Tamar"): {
        "tr": "Ermeni, Lübnan ve Gürcü mutfağının en iyi örneklerini sunan aile işletmesi. Zengin mezeler ve ızgaralar.",
        "en": "Family business offering the best examples of Armenian, Lebanese, and Georgian cuisine. Rich appetizers and grills."
    },
    ("Marsilya", "Rive Sud Vins"): {
        "tr": "Limanın hemen yanında, rahat bir atmosferde geniş şarap kavı ve atıştırmalıklar sunan keyifli bir durak.",
        "en": "A delightful stop right next to the port offering a wide wine cellar and snacks in a relaxed atmosphere."
    },
    ("Marsilya", "chez moe"): {
        "tr": "Deniz ürünleri ve taze balıklarla öne çıkan, liman manzaralı rahat bir restoran. Marsilya ruhunu yansıtan lezzetler.",
        "en": "Relaxed restaurant overlooking the harbor, standing out with seafood and fresh fish. Flavors reflecting the spirit of Marseille."
    },
    ("Marsilya", "The Coffee"): {
        "tr": "Özenle seçilmiş kahve çekirdekleri ve minimalist bir ortam. Şehir turuna kısa ve lezzetli bir mola vermek için ideal.",
        "en": "Carefully selected coffee beans and a minimalist setting. Ideal for taking a short and delicious break from the city tour."
    },
    ("Milano", "Andalous"): {
        "tr": "Milano'da Fas rüzgarları estiren otantik bir köşe. Geleneksel tajin, kuskus ve nane çayı servisi.",
        "en": "An authentic corner bringing Moroccan winds to Milan. Traditional tagine, couscous, and mint tea service."
    },
    ("Milano", "Autem Milano"): {
        "tr": "Şık ve minimalist bir ortamda sunulan yenilikçi İtalyan mutfağı. Mevsimsel malzemelere getirilen modern yorumlar.",
        "en": "Innovative Italian cuisine served in a stylish and minimalist setting. Modern interpretations of seasonal ingredients."
    },
    ("Milano", "Focaccerie Genovesi Milano"): {
        "tr": "Cenova usulü gerçek focaccia deneyimi. Peynirli, zeytinli ve sade çeşitleriyle hızlı ve lezzetli bir durak.",
        "en": "Authentic Genoese style focaccia experience. A quick and delicious stop with cheese, olive, and plain varieties."
    },
    ("Milano", "KUSINA ni LODI"): {
        "tr": "Filipin mutfağının en sevilen lezzetlerini sunan sıcak ve samimi bir aile restoranı. Adobo ve çıtır domuz eti favorilerden.",
        "en": "Warm and friendly family restaurant offering the most beloved flavors of Filipino cuisine. Adobo and crispy pork are among the favorites."
    },
    ("Milano", "La Medina"): {
        "tr": "Fas kültürünü yansıtan dekorasyonuyla otantik bir deneyim. Canlı renkler arasında lezzetli Kuzey Afrika yemekleri.",
        "en": "An authentic experience reflecting Moroccan culture with its decoration. Delicious North African dishes amidst vibrant colors."
    },
    ("Milano", "Nàpiz' Milano"): {
        "tr": "Milano'nun kalbinde gerçek Napoli pizzası. Odun fırınından çıkan kabarık kenarlı, taze malzemeli pizzalar.",
        "en": "Real Neapolitan pizza in the heart of Milan. Puffy-crusted pizzas with fresh ingredients straight from the wood oven."
    },
    ("Milano", "Ristorante Spore"): {
        "tr": "Fermentasyon tekniklerine odaklanan yenilikçi ve sürdürülebilir bir mutfak. Asya esintili modern tadım menüleri.",
        "en": "Innovative and sustainable cuisine focusing on fermentation techniques. Asian-inspired modern tasting menus."
    },
    ("Milano", "The Rabbit"): {
        "tr": "Rahat atmosferi ve geniş içki menüsüyle popüler bir buluşma noktası. Kokteyller ve aperitif atıştırmalıklar.",
        "en": "Popular meeting point with a relaxed atmosphere and extensive drink menu. Cocktails and aperitif snacks."
    },
    ("Milano", "drinc.different"): {
        "tr": "Gizli bir speakeasy havasında, yaratıcı ve sanat eseri gibi sunulan kokteyller. Miksoloji tutkunları için özel bir deneyim.",
        "en": "Creative and art-like cocktails offered in a secret speakeasy vibe. A special experience for mixology enthusiasts."
    },
    ("Napoli", "Bar Pasticceria La Veneziana"): {
        "tr": "Güne taze sfogliatella ve mis gibi bir kahve ile başlamak için klasik bir Napoli pastanesi.",
        "en": "A classic Neapolitan pastry shop to start the day with fresh sfogliatella and fragrant coffee."
    },
    ("Napoli", "Caffe Aragonese/Drinkspoint"): {
        "tr": "Tarihi dokusuyla dikkat çeken, klasik bir İtalyan kafesi. Lezzetli kahveler ve hamur işleri sunar.",
        "en": "Classic Italian cafe attracting attention with its historical texture. Offers delicious coffees and pastries."
    },
    ("Napoli", "Corno Gelato - Gelateria Artigianale"): {
        "tr": "Napoli'nin simgesi boynuz şeklindeki külahlarda sunulan artizan dondurmalar. Eğlenceli ve lezzetli.",
        "en": "Artisan ice creams served in horn-shaped cones, the symbol of Napoli. Fun and delicious."
    },
    ("Napoli", "HYPEBAR"): {
        "tr": "Napoli gecelerinin nabzını tutan, şık ve modern bir bar. Geniş kokteyl menüsü ve enerjik atmosfer.",
        "en": "Stylish and modern bar keeping the pulse of Napoli nights. Extensive cocktail menu and energetic atmosphere."
    },
    ("Napoli", "I Servino"): {
        "tr": "Geleneksel pizza ve kızartmaların modern bir ortamda sunumu. Aile sıcaklığında lezzetli bir akşam yemeği.",
        "en": "Presentation of traditional pizza and fried foods in a modern setting. A delicious dinner in family warmth."
    },
    ("Napoli", "LA TUPAIA VINERIA"): {
        "tr": "Zengin şarap kavı ve şarküteri tabaklarıyla keyifli bir akşam. Rahat, samimi ve sohbet dolu bir ortam.",
        "en": "Delightful evening with a rich wine cellar and charcuterie platters. Comfortable, friendly, and chatty environment."
    },
    ("Napoli", "Mozzelato"): {
        "tr": "Mozzarella ve gelato aşkı! Taze peynirler ve serinleten dondurmalarla dolu lezzetli bir mola.",
        "en": "Love for mozzarella and gelato! A delicious break full of fresh cheeses and refreshing ice creams."
    },
    ("Napoli", "Pasticceria Liccardo"): {
        "tr": "Geleneksel Napoli tatlılarının adresi. Babà, zeppole ve daha fazlası için yerel halkın favorisi.",
        "en": "Address for traditional Neapolitan sweets. Local favorite for Babà, zeppole, and more."
    },
    ("Napoli", "Pasticceria Pascal"): {
        "tr": "Sanat eseri görünümlü pastaları ve tatlılarıyla ünlü. Özel günler ve tatlı krizleri için şık bir tercih.",
        "en": "Famous for its art-like cakes and sweets. A stylish choice for special occasions and sweet cravings."
    },
    ("Napoli", "Tappò Tapas Bar"): {
        "tr": "İspanyol tapas kültürünü Napoli'ye taşıyan, canlı ve hareketli bir bar. Paylaşımlı tabaklar ve sangria.",
        "en": "Lively and bustling bar bringing Spanish tapas culture to Napoli. Shared plates and sangria."
    },
    ("Napoli", "Vino Franco"): {
        "tr": "Doğal şaraplar ve yerel atıştırmalıklar sunan samimi bir şarap evi. Napoli'nin ara sokaklarında gizli bir hazine.",
        "en": "Intimate wine house offering natural wines and local snacks. A hidden treasure in the backstreets of Napoli."
    },
    ("Napoli", "restaQmme"): {
        "tr": "Napoli mutfağına modern dokunuşlar. Şık sunumlar ve taze deniz ürünleriyle gurme bir deneyim.",
        "en": "Modern touches to Neapolitan cuisine. A gourmet experience with stylish presentations and fresh seafood."
    },
    ("Nice", "Aperitiv"): {
        "tr": "Şarap, peynir ve şarküteri severler için cennet. Dostane bir ortamda en iyi yerel ürünleri tadın.",
        "en": "Paradise for wine, cheese, and charcuterie lovers. Taste the best local products in a friendly environment."
    },
    ("Nice", "Au Sud De Nulle Part"): {
        "tr": "Kitaplarla çevrili, huzurlu bir edebiyat kafesi. Lezzetli brunchlar, ev yapımı tatlılar ve sakin bir avlu.",
        "en": "Peaceful literary cafe surrounded by books. Delicious brunches, homemade sweets, and a quiet courtyard."
    },
    ("Nice", "Bio Brod"): {
        "tr": "Organik ve glütensiz ürünleriyle ünlü artizan fırın. Antik tahıllarla yapılan ekşi mayalı ekmekler ve sağlıklı atıştırmalıklar.",
        "en": "Artisan bakery famous for its organic and gluten-free products. Sourdough breads made with ancient grains and healthy snacks."
    },
    ("Nice", "Bocca Mar"): {
        "tr": "Promenade des Anglais üzerinde, deniz manzaralı şık bir restoran. Akdeniz mutfağı, taze deniz ürünleri ve tatil havası.",
        "en": "Stylish restaurant with sea view on Promenade des Anglais. Mediterranean cuisine, fresh seafood, and holiday vibe."
    },
    ("Nice", "Brume Coffee Nice"): {
        "tr": "Ahşap dekorasyonu ve bitkilerle süslü rahat bir kahve dükkanı. Nitelikli kahveler, sağlıklı brunchlar ve vegan seçenekler.",
        "en": "Cozy coffee shop decorated with wood and plants. Specialty coffees, healthy brunches, and vegan options."
    },
    ("Nice", "Gelato D'Amore Nice"): {
        "tr": "Gerçek İtalyan gelatosu arayanlar için doğru adres. Güler yüzlü hizmet ve doğal malzemelerle hazırlanan dondurmalar.",
        "en": "The right address for those looking for real Italian gelato. Friendly service and ice creams prepared with natural ingredients."
    },
    ("Nice", "Glacier du Pin"): {
        "tr": "Place du Pin meydanında popüler bir dondurmacı. Geniş dondurma çeşitleri, krepler ve wafıllar.",
        "en": "Popular ice cream shop in Place du Pin square. Wide variety of ice creams, crepes, and waffles."
    },
    ("Nice", "IBERICA comptoir"): {
        "tr": "Nice limanında İspanya rüzgarı. Jambon, peynir ve tapas çeşitleriyle dolu, keyifli ve hareketli bir mekan.",
        "en": "Spanish breeze at Nice port. Delightful and bustling venue full of ham, cheese, and tapas varieties."
    },
    ("Nice", "L'Alchimie restaurant Nice"): {
        "tr": "Uygun fiyatlı ve dürüst yemekleriyle sevilen modern bir bistro. Mevsimsel malzemelerle hazırlanan yaratıcı öğle yemekleri.",
        "en": "Modern bistro loved for its affordable and honest food. Creative lunches prepared with seasonal ingredients."
    },
    ("Nice", "La Bonne étoile Nice - Afro fusion"): {
        "tr": "Afro-füzyon mutfağıyla farklı kültürleri birleştiren renkli bir mekan. Egzotik tatlar ve sıcak bir ortam.",
        "en": "Colorful venue combining different cultures with Afro-fusion cuisine. Exotic tastes and a warm environment."
    },
    ("Nice", "La Saudade"): {
        "tr": "Portekiz kültürünü Nice'e taşıyan şirin bir çay salonu. Meşhur 'Pastéis de Nata' ve diğer geleneksel tatlılar.",
        "en": "Cute tea room bringing Portuguese culture to Nice. Famous 'Pastéis de Nata' and other traditional sweets."
    },
    ("Nice", "Le Bistrot du Fromager"): {
        "tr": "Peynir tutkunları için eşsiz bir mahzen restoran. Fondü, raclette ve şarap eşleşmeleriyle kış gecelerinin vazgeçilmezi.",
        "en": "Unique cellar restaurant for cheese lovers. Indispensable for winter nights with fondue, raclette, and wine pairings."
    },
    ("Nice", "Le Glouphile"): {
        "tr": "Şarap ve iyi yemek tutkunlarının buluşma noktası. Özenle seçilmiş şarap listesi ve onlara eşlik eden lezzetli tabaklar.",
        "en": "Meeting point for wine and good food lovers. Carefully selected wine list and delicious plates accompanying them."
    },
    ("Nice", "Le bistrot poète"): {
        "tr": "Şiirsel bir atmosferde sunulan Fransız mutfağı klasikleri. Romantik akşam yemekleri ve sakin sohbetler için ideal.",
        "en": "French cuisine classics served in a poetic atmosphere. Ideal for romantic dinners and quiet conversations."
    },
    ("Nice", "MARMAR Restaurant"): {
        "tr": "Orta Doğu ve Akdeniz mutfağının sıcak lezzetleri. Zengin mezeler ve ızgara çeşitleriyle doyurucu bir deneyim.",
        "en": "Warm flavors of Middle Eastern and Mediterranean cuisine. A satisfying experience with rich appetizers and grill varieties."
    },
    ("Nice", "Meryenda Sokağı Food"): {
        "tr": "Eski Nice sokaklarında Asya sokak lezzetleri turu. Kore, Japon ve Filipin mutfaklarından füzyon tatlar.",
        "en": "Asian street food tour in Old Nice streets. Fusion flavors from Korean, Japanese, and Filipino cuisines."
    },
    ("Nice", "Vino Margaux"): {
        "tr": "Samimi ve rahat bir şarap barı. Yerel şarapları keşfetmek ve yanında lezzetli atıştırmalıklar denemek için harika.",
        "en": "Intimate and comfortable wine bar. Great for discovering local wines and trying delicious snacks alongside."
    },
    ("Nice", "Restaurant & Lounge La Bonne étoile Nice - Afro fusion"): {
        "tr": "Afro-füzyon mutfağıyla farklı kültürleri birleştiren renkli bir mekan. Egzotik tatlar ve sıcak bir ortam.",
        "en": "Colorful venue combining different cultures with Afro-fusion cuisine. Exotic tastes and a warm environment."
    },
    ("Madrid", "AMIS"): {
        "tr": "Doğal şaraplar ve dürüst yemekler sunan samimi bir bar. Gösterişten uzak, lezzete odaklanan bir deneyim.",
        "en": "Intimate bar offering natural wines and honest food. An experience focusing on flavor, far from pretension."
    },
    ("Madrid", "Bloved Restaurante"): {
        "tr": "Gran Vía üzerinde, şık ve zarif bir Akdeniz restoranı. Trüflü ördek ve deniz ürünlü risotto gibi gurme lezzetler.",
        "en": "Stylish and elegant Mediterranean restaurant on Gran Vía. Gourmet flavors like truffled duck and seafood risotto."
    },
    ("Madrid", "EL LOCO"): {
        "tr": "Chueca'nın kalbinde, bilardo ve langırtla dolu eğlenceli bir bar. Madrid gece hayatının enerjisini hissetmek için ideal.",
        "en": "Fun bar full of pool and foosball in the heart of Chueca. Ideal for feeling the energy of Madrid nightlife."
    },
    ("Marakeş", "Epicurien"): {
        "tr": "Casino de Marrakech içinde yer alan, canlı müzik ve DJ performanslarıyla ünlü şık gece kulübü ve restoran.",
        "en": "Stylish nightclub and restaurant located inside Casino de Marrakech, famous for live music and DJ performances."
    },
    ("Marakeş", "Foundouk Gargaa"): {
        "tr": "Medina'nın kalbinde gizli bir vaha. Ceviz ağacı gölgesindeki terası ve organik malzemelerle hazırlanan Fas yemekleri.",
        "en": "Hidden oasis in the heart of Medina. Moroccan dishes prepared with organic ingredients on a terrace shaded by a walnut tree."
    },
    ("Marakeş", "Gazélia pâtisserie"): {
        "tr": "Fas'ın meşhur 'ceylan boynuzu' tatlısı ve diğer geleneksel hamur işleri için en iyi adreslerden biri.",
        "en": "One of the best addresses for Morocco's famous 'gazelle horn' dessert and other traditional pastries."
    },
    ("Marakeş", "la Joie"): {
        "tr": "Güzel bir teras manzarasına sahip, huzurlu bir geleneksel kafe. Nane çayı ve Fas hamur işleri eşliğinde dinlenmek için mükemmel.",
        "en": "Peaceful traditional cafe with a beautiful terrace view. Perfect for relaxing with mint tea and Moroccan pastries."
    },
    ("New York", "Al-Andalus"): {
        "tr": "Endülüs ve Kuzey Afrika esintili, canlı bir tapas bar. Paylaşımlı tabaklar ve renkli çini dekorasyonuyla enerjik bir ortam.",
        "en": "Lively tapas bar inspired by Andalusia and North Africa. Energetic vibe with shared plates and colorful tile decor."
    },
    ("New York", "BARBOUNIA"): {
        "tr": "Akdeniz'in modern lezzetlerini New York'a taşıyan şık mekan. Açık mutfağı ve yüksek enerjili atmosferiyle popüler.",
        "en": "Stylish venue bringing modern Mediterranean flavors to New York. Popular with its open kitchen and high-energy atmosphere."
    },
    ("Oslo", "Norwegian Maritime Müzesi"): {
        "tr": "Norveç'in denizcilik tarihini ve kıyı kültürünü keşfedin. Viking gemileri ve interaktif sergilerle dolu bir müze.",
        "en": "Explore Norway's maritime history and coastal culture. A museum full of Viking ships and interactive exhibitions."
    },
    ("Oslo", "Technical Müzesi Oslo"): {
        "tr": "Bilim, teknoloji ve tıp dünyasına eğlenceli bir yolculuk. Her yaştan ziyaretçi için 100'den fazla interaktif deneyim.",
        "en": "Fun journey into the world of science, technology, and medicine. Over 100 interactive experiences for visitors of all ages."
    },
    ("Oslo", "University of Oslo"): {
        "tr": "Şehir merkezine yakın, doğayla iç içe tarihi bir kampüs. Öğrenci enerjisini ve akademik atmosferi hissetmek için keyifli bir durak.",
        "en": "Historic campus integrated with nature, close to the city center. A pleasant stop to feel the student energy and academic atmosphere."
    }
}

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    updated_files = 0
    total_updated_places = 0
    
    print("Starting updates...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', '')
            highlights = data.get('highlights', [])
            file_changed = False
            
            for place in highlights:
                name = place.get('name', '')
                key = (city_name, name)
                
                if key in UPDATES:
                    update_data = UPDATES[key]
                    place['description'] = update_data['tr']
                    place['description_en'] = update_data['en']
                    file_changed = True
                    total_updated_places += 1
                    print(f"Updated {city_name} - {name}")
            
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                updated_files += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nDone. Updated {total_updated_places} places across {updated_files} files.")

if __name__ == "__main__":
    main()

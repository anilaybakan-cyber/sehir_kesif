import re

dart_file = "lib/services/city_blog_content.dart"

with open(dart_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "_hiddenGemsTR": """  static const _hiddenGemsTR = '''# Avrupa'nın Gizli Hazineleri

Herkes Paris ve Roma'ya akın ederken, siz rotanızı kalabalıktan uzak, kendine has dokusunu korumuş bu büyüleyici kasabalara çevirin. Saklı kalmış sokaklarda kaybolmaya hazır mısınız?

## 1. Matera, İtalya
Taş devrinden kalma mağara evlerin oluşturduğu bu antik şehir, adeta zamanın durduğu bambaşka bir gezegen gibi. Labirenti andıran mistik sokakları ve sarı taşlı evleriyle James Bond filmlerine set olmuş, büyüleyici bir atmosfere sahip.
> **İpucu:** [Sassi di Matera](search:Sassi di Matera) bölgesindeki otantik bir mağara otelde konaklayarak bu eşsiz tarihi dokuyu bizzat yaşayın.

## 2. Giethoorn, Hollanda
"Kuzeyin Venedik'i" olarak anılan bu masalsı köyde motor sesi yok, yollar yok. Ulaşım tamamen kanallar üzerinden sessiz elektrikli teknelerle sağlanıyor. Saz çatılı şirin evleri, ahşap köprüleri ve yemyeşil doğasıyla tam bir huzur cenneti.
> **İpucu:** Sabahın erken saatlerinde kanal turuna çıkarak köyün uyanışına sessizce tanıklık edin.

## 3. Kotor, Karadağ
Balkanlar'ın fiyortları arasına gizlenmiş bu ortaçağ şehri, dramatik dağ manzaraları ve sevimli sokak kedileriyle meşhur. Labirent gibi dar sokaklarında kaybolmak ve Venedik mimarisinin en güzel örneklerini incelemek oldukça keyifli.
> **İpucu:** [Kale surlarına](search:Kotor Fortress) tırmanıp, Kotor Körfezi'nin o nefes kesici kuşbakışı manzarasını izlemeyi unutmayın.

## 4. Colmar, Fransa
Alsace şarap yolunun kalbinde yer alan bu şehir, rengarenk yarı ahşap evleri ve sardunyalarla süslü balkonlarıyla ünlü. "Küçük Venedik" (Petite Venise) bölgesi, adeta Güzel ve Çirkin gibi klasik Disney filmlerinin setinden fırlamış, büyüleyici bir estetiğe sahip.
> **İpucu:** Şehrin kanallarında kısa bir kayık turu yapıp çevredeki yerel şarap evlerini ziyaret edin.

## 5. Sintra, Portekiz
Lizbon'un sadece 40 dakika uzağında yer alan Sintra, sisli ormanları, gotik şatoları ve sarı-kırmızı renkleriyle göz kamaştıran Pena Sarayı ile mistik bir dünya sunuyor. Eskiden Portekiz kraliyet ailesinin yazlık mekanı olan bu kasaba, eşsiz bir romantizme sahip.
> **İpucu:** Pena Sarayı'nın yanı sıra, gizemli tünelleri olan [Quinta da Regaleira](search:Quinta da Regaleira)'yı da mutlaka gezin.
''';""",

    "_hiddenGemsEN": """  static const _hiddenGemsEN = '''# Europe's Hidden Gems

While everyone flocks to Paris and Rome, distinct yourself by exploring these enchanting towns that remain wonderfully untouched and away from the dense tourist crowds.

## 1. Matera, Italy
A breathtaking city carved into limestone cliffs, featuring cave dwellings dating back to the Stone Age. Wandering its mystical, labyrinthine streets feels like stepping onto another planet—a landscape so dramatic it became a set for James Bond.
> **Tip:** Enhance your experience by staying in an authentic cave hotel in the [Sassi di Matera](search:Sassi di Matera) district.

## 2. Giethoorn, Netherlands
Known as the "Venice of the North," this fairytale village has no roads and zero engine noise. Transportation relies entirely on silent electric boats gliding through peaceful canals, surrounded by idyllic thatched-roof houses and wooden bridges.
> **Tip:** Rent a whisper boat early in the morning to enjoy the village's pristine tranquility.

## 3. Kotor, Montenegro
A perfectly preserved medieval city hidden deep within stunning Balkan fjords. Famous for its dramatic mountain backdrop and charming street cats, its narrow alleys offer exquisite examples of Venetian architecture and history.
> **Tip:** Climbing the [fortress walls](search:Kotor Fortress) to witness the magnificent panoramic view of the bay is priceless.

## 4. Colmar, France
The undisputed capital of the Alsace wine route. With its half-timbered colorful houses and flower-lined canals in "Petite Venise," it looks straight out of a classic Disney fairytale like Beauty and the Beast.
> **Tip:** Take a traditional flat-bottomed boat ride on the Lauch River and enjoy the local Riesling wine.

## 5. Sintra, Portugal
Only 40 minutes from Lisbon, yet a completely mystical world of its own. Defined by the vibrant yellow-red hues of the Pena Palace, foggy pine forests, and gothic estates, it served as a summer sanctuary for Portuguese royals.
> **Tip:** Don't miss the initiation wells and secret tunnels of [Quinta da Regaleira](search:Quinta da Regaleira).
''';""",

    "_gastronomyTR": """  static const _gastronomyTR = '''# Gastronomi Tutkunları İçin

Sadece yeni yerler görmekle yetinmeyip, seyahatini lezzet odaklı planlayanlar için midenizin bayram edeceği, diyeti unutturacak 5 muazzam lezzet başkenti.

## 1. San Sebastian, İspanya
Dünyada metrekareye en çok Michelin yıldızı düşen, deniz kıyısındaki bu şık Bask şehri gastronominin zirvesidir. Asıl olay lüks restoranlar kadar, barlarda sunulan "Pintxos" isimli minyatür lezzet şölenleridir. 
> **İpucu:** Eski Şehir (Parte Vieja) bölgesindeki barları dolaşıp tezgahtaki her Pintxo'dan tatmaya çalışın.

## 2. Lyon, Fransa
Paris gösterişlidir ama Fransa'nın gerçek, otantik yemek başkenti tartışmasız Lyon'dur. "Bouchon" adı verilen geleneksel ve sıcak atmosferli lokantalarda zengin et yemekleri ve efsanevi soğan çorbasını denemelisiniz.
> **İpucu:** Dünyaca ünlü şef Paul Bocuse'nin adını taşıyan [Les Halles de Lyon](search:Les Halles de Lyon) kapalı pazarını kesinlikle gezin.

## 3. Bologna, İtalya
İtalyanlar bile bu şehre "La Grassa" (Şişman) lakabını takmıştır çünkü burada yemek yemek bir ibadet gibidir. Parmigiano-Reggiano, Prosciutto ve gerçek Bolonez sosunun (Ragù) doğduğu yer burasıdır.
> **İpucu:** Gerçek Ragù sosunu asla spagettiyle değil, geniş şeritli ev yapımı Tagliatelle ile sipariş edin.

## 4. Gaziantep, Türkiye
UNESCO Yaratıcı Şehirler Ağı'na Gastronomi dalında giren, baharatın, etin ve fıstığın başkenti. Sabah erken saatlerde içilen şifalı beyran, öğle vakti lokum gibi küşleme ve kapanışta sıcak katmer ile eşsiz bir mutfak.
> **İpucu:** [Bakırcılar Çarşısı](search:Bakırcılar Çarşısı) civarındaki tarihi hanlarda fıstıklı kahvenizi içmeyi unutmayın.

## 5. Kopenhag, Danimarka
Yerel malzemeleri minimalist tekniklerle buluşturan "Yeni İskandinav Mutfağı"nın doğduğu yer. Dünyanın en iyi restoranlarından sayılan Noma'nın ev sahibi olmasının yanı sıra, "Smørrebrød" (açık sandviç) kültürüyle de muhteşem sokak lezzetleri sunar.
> **İpucu:** Şehrin ikonik sokak yemeği pazarı [Reffen](search:Reffen Copenhagen)'de dünya mutfaklarının İskandinav yorumunu tadın.
''';""",

    "_gastronomyEN": """  static const _gastronomyEN = '''# For Gastronomy Lovers

For travelers who plan their itineraries around meals, here are 5 delicious culinary capitals where your taste buds will celebrate and diets will gladly be forgotten.

## 1. San Sebastian, Spain
This elegant Basque coastal city boasts the highest number of Michelin stars per square meter globally. Yet, its true culinary soul lies in "Pintxos"—exquisite, bite-sized creations served atop fresh bread in bustling local bars.
> **Tip:** Go on a Pintxo crawl in the Old Town (Parte Vieja), grabbing different bites from various tavern counters.

## 2. Lyon, France
While Paris has the glamour, Lyon is unequivocally recognized as the true gastronomic capital of France. Experience rich duck confits, quenelles, and iconic onion soups in traditional, convivial bistros known locally as "Bouchons".
> **Tip:** Wander through the famed indoor food market, [Les Halles de Lyon Paul Bocuse](search:Les Halles de Lyon), to sample premium regional produce.

## 3. Bologna, Italy
Italians affectionately nickname this city "La Grassa" (The Fat One) for a very good reason. It is the birthplace of Parmigiano-Reggiano, Prosciutto, and the authentic, slow-cooked Bolognese sauce (Ragù).
> **Tip:** Remember that authentic Ragù is always served with wide, fresh Tagliatelle pasta, never with spaghetti.

## 4. Gaziantep, Turkey
A UNESCO City of Gastronomy, renowned as the capital of spices, pistachios, and legendary kebabs. Start your day with hearty Beyran soup, enjoy tender Küşleme for lunch, and indulge in hot, crispy Katmer for dessert.
> **Tip:** Visit the historic caravanserais near the [Coppersmith Bazaar](search:Bakırcılar Çarşısı) for a traditional pistachio coffee.

## 5. Copenhagen, Denmark
The undisputed birthplace of "New Nordic Cuisine," blending hyper-local foraging with minimalist culinary art. Beyond housing legendary restaurants like Noma, the city offers phenomenal street food, especially the artful "Smørrebrød" open sandwiches.
> **Tip:** Explore [Reffen](search:Reffen Copenhagen), the vibrant street food market offering innovative dishes by the waterfront.
''';""",

    "_romanticTR": """  static const _romanticTR = '''# Romantik Haftasonu Kaçamakları

Koşturmacadan uzaklaşıp, sadece anı yaşamak isteyen çiftler için tarihle, güzel manzaralarla ve eşsiz bir atmosferle harmanlanmış mükemmel rotalar.

## 1. Venedik, İtalya
Kanallar şehri her ne kadar turistik olsa da, gece çöktüğünde labirent gibi sokaklarında el ele kaybolmanın yerini hiçbir şey tutamaz. Gondol gezileri, zarif köprüler ve maskelerin arkasına saklanmış gizemli bir romantizm.
> **İpucu:** Kalabalıktan uzaklaşmak için San Marco yerine daha sakin, lokal ve sanatsal olan Dorsoduro bölgesini tercih edin.

## 2. Brugge, Belçika
Adeta bir çikolata kutusundan fırlamış gibi duran bu Orta Çağ şehri. Arnavut kaldırımlı sokakları, kanallarda süzülen kuğuları ve tüm şehri saran tatlı waffle kokusuyla masalsı bir hafta sonu vadediyor.
> **İpucu:** Şehri yürüyerek keşfettikten sonra bisiklet kiralayıp etraftaki tarihi yel değirmenlerine doğru keyifli bir sürüş yapın.

## 3. Santorini, Yunanistan
Volkanik kayalıkların üzerine kurulmuş mavi kubbeli beyaz evleri ve sonsuz Ege Denizi manzarasıyla dünyanın tartışmasız en romantik adalarından biri. Kalderaya karşı şarabınızı yudumlamak unutulmaz bir deneyim.
> **İpucu:** Daha iyi manzara ve daha az turistik yoğunluk için Oia yerine [Imerovigli](search:Imerovigli) bölgesinde konaklamayı seçin.

## 4. Heidelberg, Almanya
Almanya'nın romantizm başkenti. Tepeden şehre bakan görkemli kalesi, altından usulca akan Neckar nehri ve tarihi köprüleriyle tam bir tablo gibi. Özellikle sonbaharda şehrin büründüğü renkler büyüleyicidir.
> **İpucu:** Eskiden düşünürlerin yürüdüğü filozoflar yolunda ([Philosophenweg](search:Philosophenweg)) yürüyüş yaparak nehrin karşısından şehri izleyin.

## 5. Sevilla, İspanya
Endülüs ruhunun merkezi. Flamenko dansının tutkusu, sokaklara yayılan portakal çiçeği kokuları ve görkemli Arap-Gotik mimarisiyle sıcacık bir atmosfere sahip. Akşamları dar sokaklarda gitar sesleri yankılanır.
> **İpucu:** Muazzam çinileriyle süslü [Plaza de España](search:Plaza de España)'da kanal etrafında romantik bir fayton turu yapın.
''';""",

    "_romanticEN": """  static const _romanticEN = '''# Romantic Weekend Getaways

Step away from the daily rush and savor the moment. These perfectly curated routes offer couples an unforgettable blend of history, breathtaking scenery, and intimate atmospheres.

## 1. Venice, Italy
While often bustling, nothing compares to the magic of getting lost hand-in-hand in its labyrinthine alleys after sunset. Elegant bridges, gliding gondolas, and a mysterious, timeless romance await at every corner.
> **Tip:** Escape the dense tourist crowds around San Marco and explore the tranquil, art-filled Dorsoduro district instead.

## 2. Bruges, Belgium
A beautifully preserved medieval town that looks exactly like a vintage chocolate box. Cobblestone streets, swans drifting through serene canals, and the warm scent of fresh waffles create an absolute fairytale setting.
> **Tip:** After walking the center, rent a tandem bike and cycle out to the iconic windmills on the city outskirts.

## 3. Santorini, Greece
One of the most indisputably romantic islands on earth, featuring iconic white houses with blue domes perched on dramatic volcanic cliffs. Sipping local wine while gazing over the vast Aegean caldera is a true bucket list experience.
> **Tip:** For superior panoramic views and significantly fewer crowds, book your stay in [Imerovigli](search:Imerovigli) rather than Oia.

## 4. Heidelberg, Germany
The heart of German romanticism. Dominated by a majestic ruined castle on the hill and beautifully mirrored in the Neckar River below, this historic university town feels like a living painting, especially in autumn.
> **Tip:** Walk the famous [Philosophenweg](search:Philosophenweg) (Philosophers' Walk) across the river for the most spectacular views of the castle.

## 5. Seville, Spain
The beating heart of Andalusia. Defined by the intense passion of flamenco, the sweet scent of orange blossoms, and breathtaking Moorish-Gothic architecture. Evening strolls here are always accompanied by distant Spanish guitar melodies.
> **Tip:** Take a romantic horse-drawn carriage ride through the magnificent, tile-covered [Plaza de España](search:Plaza de España).
''';"""
}

def replace_block(text, var_name, new_val):
    pattern = re.compile(rf"(static const {var_name} = ''')(.*?)(''';)", re.DOTALL)
    return pattern.sub(new_val.replace('\\', '\\\\'), text)

for var_name, new_val in replacements.items():
    content = replace_block(content, var_name, new_val)

with open(dart_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated 3 collections successfully.")

import json
import os

all_updates = {
    "Amalfi": {
        "Buco di Montepertuso": {
            "description": "Positano'nun yukarısındaki Montepertuso köyünde yer alan bu devasa doğal kaya deliği, efsaneye göre Meryem Ana ile Şeytan arasındaki bir düello sonucu oluşmuştur. Dağın kalbindeki bu etkileyici açıklık, fiyortlara ve denize bakan eşsiz bir manzara sunan gizli bir doğa harikasıdır.",
            "description_en": "This massive natural hole in the rock in the village of Montepertuso above Positano is said to have been formed by a duel between the Virgin Mary and the Devil. This impressive opening in the heart of the mountain is a hidden natural wonder offering unique views of the fjords and the sea.",
            "tips": "Köyden deliğe çıkan patika biraz diktir; gün batımında deliğin içinden süzülen ışığı yakalamak için akşamüstü gidin.",
            "tips_en": "The path from the village to the hole is a bit steep; go in the late afternoon to catch the light streaming through the hole at sunset.",
            "category": "Doğa"
        },
        "Ceramiche D'Arte Carmela": {
            "description": "Ravello'nun en prestijli seramik atölyelerinden biri olan Ceramiche D'Arte Carmela, canlı renkleri ve el yapımı geleneksel Amalfi motifleriyle ünlü bir sanat merkezidir. Her bir parçanın bir hikaye anlattığı bu dükkan, bölgenin asırlık zanaat mirasını modern estetikle birleştirir.",
            "description_en": "One of Ravello's most prestigious ceramic workshops, Ceramiche D'Arte Carmela is an art center famous for its vibrant colors and handmade traditional Amalfi motifs. This shop, where each piece tells a story, combines the region's centuries-old craft heritage with modern aesthetics.",
            "tips": "Atölye kısmını ziyaret edip sanatçıları iş başında izleyebilirsiniz; kargo ile gönderim seçeneği mevcuttur.",
            "tips_en": "You can visit the workshop area to watch the artists at work; worldwide shipping options are available.",
            "category": "Alışveriş"
        },
        "Chiesa Parrocchiale di Santa Maria Assunta": {
            "description": "Positano'nun ikonik sahil silüetinin en belirgin parçası olan bu kilise, muazzam majolika çini kubbesiyle ünlüdür. 10. yüzyıla kadar uzanan tarihi ve içerisinde barındırdığı 12. yüzyıldan kalma Bizans usulü 'Kara Meryem' ikonuyla kentin manevi kalbidir.",
            "description_en": "The most prominent part of Positano's iconic coastal skyline, this church is famous for its magnificent majolica tile dome. Dating back to the 10th century, it is the city's spiritual heart, housing a 12th-century Byzantine-style 'Black Madonna' icon.",
            "tips": "Kilisenin önündeki meydan fotoğraf için en popüler noktadır; içeriyi gezmek için omuzların kapalı olması gerektiğini unutmayın.",
            "tips_en": "The square in front of the church is the most popular photo spot; remember that shoulders must be covered to tour the interior.",
            "category": "Tarihi"
        },
        "Chiostro del Paradiso": {
            "description": "Amalfi Katedrali'nin yanında yer alan bu 13. yüzyıl yapımı 'Cennet Avlusu', Mağrip tarzı zarif sütunları ve huzurlu atmosferiyle kentin en güzel köşelerinden biridir. Eski Amalfi soylularının mezarlığı olarak kullanılan bu alan, şimdi kentin tarihini fısıldayan bir açık hava müzesidir.",
            "description_en": "Located next to Amalfi Cathedral, this 13th-century 'Cloister of Paradise' is one of the city's most beautiful corners with its elegant Moorish-style columns and peaceful atmosphere. Once used as a cemetery for Amalfi nobles, it is now an open-air museum whispering the city's history.",
            "tips": "Avlunun ortasındaki egzotik bahçede biraz zaman geçirin; Katedral giriş bileti ile burayı da gezebilirsiniz.",
            "tips_en": "Spend some time in the exotic garden in the center of the cloister; you can visit here with your Cathedral entry ticket.",
            "category": "Tarihi"
        },
        "Fontana di Sant'Andrea": {
            "description": "Amalfi'nin ana meydanında, katedralin hemen dibinde yer alan bu Barok çeşme, kentin koruyucu azizi Aziz Andreas'a adanmıştır. 1760 yılında inşa edilen ve mermerden yontulan bu sanat eseri, kentin sosyal yaşamının merkezinde yer alan tarihi bir buluşma noktasıdır.",
            "description_en": "Located in Amalfi's main square right at the foot of the cathedral, this Baroque fountain is dedicated to the city's patron saint, Saint Andrew. Built in 1760 and sculpted from marble, this masterpiece is a historical meeting point at the center of the city's social life.",
            "tips": "Çeşmeden akan su içilebilirdir; mataranızı kentin bu tarihi kaynağından doldurabilirsiniz.",
            "tips_en": "The water flowing from the fountain is potable; you can fill your water bottle from this historical source of the city.",
            "category": "Tarihi"
        },
        "Grotta dello Smeraldo": {
            "description": "Conca dei Marini fiyordunda yer alan 'Zümrüt Mağara', ismini suyun içerideki ışık kırılmalarıyla büründüğü büyüleyici yeşil tondan alır. Mağaranın içindeki su altı seramik doğum sahnesi ve devasa sarkıtları, Amalfi kıyılarının en gizemli ve mistik doğa deneyimlerinden birini sunar.",
            "description_en": "Located in the Conca dei Marini fjord, the 'Emerald Grotto' takes its name from the mesmerizing green hue the water acquires through light refraction inside. The underwater ceramic nativity scene and massive stalactites offer one of the Amalfi Coast's most mysterious and mystical nature experiences.",
            "tips": "Öğle saatlerinde güneş dik geldiğinde suyun rengi en canlı halini alır; mağaraya asansörle veya denizden tekneyle ulaşabilirsiniz.",
            "tips_en": "The water color is most vibrant at noon when the sun is direct; you can reach the cave by elevator or by boat from the sea.",
            "category": "Doğa"
        },
        "MAR - Museo Archeologico Romano": {
            "description": "Positano'nun kalbinde, Santa Maria Assunta kilisesinin hemen altında keşfedilen bu Roma arkeoloji müzesi, MS 79 yılında Vezüv patlamasıyla küller altında kalan lüks bir Roma villasının kalıntılarını sergiler. Muazzam freskleri ve kentin derinliklerindeki antik yaşam izleriyle büyüleyici bir tarih yolculuğudur.",
            "description_en": "Discovered in the heart of Positano right under the Santa Maria Assunta church, this Roman archeological museum exhibits the remains of a luxury Roman villa buried under ash by the Vesuvius eruption in 79 AD. It is a fascinating journey through time with its magnificent frescoes and traces of ancient life deep within the city.",
            "tips": "Rehberli turlar kısıtlı kapasitededir, önceden rezervasyon yapılması önerilir; fresklerin renklerini yakından görmek büyüleyicidir.",
            "tips_en": "Guided tours have limited capacity, so pre-booking is recommended; seeing the colors of the frescoes up close is mesmerizing.",
            "category": "Müze"
        },
        "Museo del Corallo": {
            "description": "Ravello'da yer alan bu butik müze, Amalfi kıyılarının en değerli hazinelerinden biri olan mercan işlemeciliği sanatına adanmıştır. 19. yüzyıldan kalma nadide mercan koleksiyonları ve kentin zanaat geçmişine ışık tutan eserleriyle, ince bir estetiğin ve kültürel mirasın merkezidir.",
            "description_en": "This boutique museum in Ravello is dedicated to the art of coral crafting, one of the Amalfi Coast's most precious treasures. With its rare 19th-century coral collections and artifacts shedding light on the city's craft history, it is a center of fine aesthetics and cultural heritage.",
            "tips": "Mercan takıların nasıl işlendiğini anlatan videoları izleyin; müze küçük ama içeriği çok yoğundur.",
            "tips_en": "Watch the videos explaining how coral jewelry is crafted; the museum is small but its content is very rich.",
            "category": "Müze"
        },
        "Path of the Gods": {
            "description": "Bomerano'dan Nocelle'e uzanan 'Tanrıların Yolu', Amalfi kıyılarının en efsanevi yürüyüş rotasıdır. Denizden yüzlerce metre yüksekte, sarp kayalıkların üzerinden kentin ve kıyı şeridinin nefes kesen panaromik manzarasını sunan bu patika, ismini gerçekten de tanrılara layık manzaralarından alır.",
            "description_en": "The 'Path of the Gods', stretching from Bomerano to Nocelle, is the most legendary hiking route on the Amalfi Coast. Hundreds of meters above the sea, this path offering breathtaking panoramic views of the city and coastline from over steep cliffs truly earns its name from its divine vistas.",
            "tips": "Yürüyüşe Bomerano'dan (yukarıdan aşağıya) başlamak çok daha kolaydır; yanınıza mutlaka 1.5 litre su ve kaymaz tabanlı ayakkabı alın.",
            "tips_en": "It's much easier to start the hike from Bomerano (downwards); be sure to bring at least 1.5 liters of water and wear shoes with non-slip soles.",
            "category": "Doğa"
        },
        "Valle delle Ferriere": {
            "description": "Amalfi'nin hemen arkasındaki derin vadide yer alan Valle delle Ferriere, kentin antik kağıt değirmenlerinin ve demirhanelerinin kalıntıları arasında uzanan yemyeşil bir doğa rezervidir. Şelaleleri, nadir bitki türleri ve serin mikro-klimasıyla kıyı sıcağından kaçmak için kentin en huzurlu sığınağıdır.",
            "description_en": "Located in the deep valley right behind Amalfi, Valle delle Ferriere is a lush green nature reserve stretching among the remains of the city's ancient paper mills and ironworks. With its waterfalls, rare plant species, and cool micro-climate, it is the city's most peaceful sanctuary to escape the coastal heat.",
            "tips": "Vadi içindeki ana şelaleye ulaşmak için yürüyüşe Pontone köyünden başlamayı deneyin; fotoğrafçılar için yosun tutmuş antik duvarlar eşsiz kareler sunar.",
            "tips_en": "Try starting the hike from Pontone village to reach the main waterfall inside the valley; the ancient mossy walls offer unique shots for photographers.",
            "category": "Doğa"
        }
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    
    # Handle both list and object structures
    highlights = []
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get('highlights', [])
        
    for h in highlights:
        name = h.get('name')
        if name in city_updates:
            upd = city_updates[name]
            h['description'] = upd['description']
            h['description_en'] = upd['description_en']
            h['tips'] = upd['tips']
            h['tips_en'] = upd['tips_en']
            h['category'] = upd['category']
            changed = True
            
    if changed:
        with open(city_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {city_file}")

# Apply Amalfi update
apply_updates('assets/cities/amalfi.json', all_updates['Amalfi'])

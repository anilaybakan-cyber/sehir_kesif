import json
import os

all_updates = {
    "Bari": {
        "KGB - Katzuti Garage Bari": {"description": "Bari'nin endüstriyel ve modern yüzünü yansıtan KGB, kentin en alternatif ve enerjik sosyal kulüplerinden biridir. Garaj konseptiyle kentsel eğlenceye farklı bir soluk getiren mekan, yerel gençliğin ve kenti keşfedenlerin uğrak noktasıdır.", "description_en": "Reflecting Bari's industrial and modern side, KGB is one of the city's most alternative and energetic social clubs. Bringing a different breath to urban entertainment with its garage concept, it's a frequent spot for local youth and city explorers.", "tips": "Özellikle tematik parti gecelerini takip edin; giriş için bazen üyelik veya ön rezervasyon gerekebilir.", "tips_en": "Follow the thematic party nights in particular; membership or pre-reservation may sometimes be required for entry.", "category": "Sosyal"},
        "Speakeasy Bari": {"description": "Bari'nin gizli ve sofistike akşam hayatını simgeleyen Speakeasy, kentin en özel kokteyl duraklarından biridir. 1920'lerin yasaklı dönem ruhunu kentsel bir zarafetle sunan mekan, her içeceğin bir hikaye anlattığı büyüleyici bir atmosfere sahiptir.", "description_en": "Symbolizing Bari's secret and sophisticated evening life, Speakeasy is one of the city's most exclusive cocktail stops. Presenting the spirit of the 1920s Prohibition era with urban elegance, it has a captivating atmosphere where every drink tells a story.", "tips": "Kapıdaki şifreyi veya rezervasyon durumunu önceden öğrenin; kentin en iyi hazırlanan klasik kokteyllerini burada tadabilirsiniz.", "tips_en": "Learn the password at the door or the reservation status in advance; you can taste the city's best-prepared classic cocktails here.", "category": "Sosyal"},
        "Museo della Cattedrale": {"description": "Bari Katedrali'nin altında keşfedilen bu müze, kentin Roma ve Bizans dönemlerine uzanan derin tarihini sergiler. Antik mozaikleri ve kentin dini mimari evrimini anlatan nadide eserleriyle kentsel hafızanın en paha biçilemez duraklarından biridir.", "description_en": "Discovered beneath the Bari Cathedral, this museum exhibits the city's deep history dating back to the Roman and Byzantine periods. With its ancient mosaics and rare artifacts telling the story of the city's religious architectural evolution, it's one of the city's most priceless stops.", "tips": "Katedral girişinden ayrı bir bileti vardır; alt kattaki antik mozaiklerin renklerini korumak için loş ışıklandırıldığını unutmayın.", "tips_en": "It has a separate ticket from the Cathedral entrance; remember that it's dimly lit to preserve the colors of the ancient mosaics downstairs.", "category": "Kültür"},
        "Diocesan Auditorium Vallisa": {"description": "Bari'nin tarihi dokusunda önemli bir yer tutan bu eski kilise alanı, şimdi kentin en prestijli kültürel etkinliklerine ve klasik müzik konserlerine ev sahipliği yapar. Akustik zarafeti ve tarihi atmosferiyle kentsel sanatın en mistik duraklarından biridir.", "description_en": "An important place in Bari's historical texture, this former church area now hosts the city's most prestigious cultural events and classical music concerts. With its acoustic elegance and historical atmosphere, it's one of the most mystical stops of urban art.", "tips": "Konser programlarını önceden takip edin; binanın dış cephesindeki ortaçağ mimarisi fotoğrafçılar için eşsizdir.", "tips_en": "Follow the concert schedules in advance; the medieval architecture on the building's exterior is unique for photographers.", "category": "Kültür"},
        "State Archives": {"description": "Bari'nin binlerce yıllık belgesel hafızasını koruyan bu devlet arşivi, kentin en entelektüel ve tarihi derinliğe sahip merkezlerinden biridir. Puglia bölgesinin sosyal ve siyasi tarihine ışık tutan paha biçilemez belgeleriyle bir kültür kalesidir.", "description_en": "Preserving Bari's millennia-old documentary memory, this state archive is one of the city's most intellectual and historically deep centers. It is a cultural fortress with priceless documents shedding light on the social and political history of the Puglia region.", "tips": "Ziyaret için önceden izin gerekebilir; dönemsel olarak açılan tarihi harita sergilerini kaçırmayın.", "tips_en": "Prior permission may be required for a visit; don't miss the historical map exhibitions opened periodically.", "category": "Kültür"}
    },
    "Budva": {
        "Akacia Coffee Budva": {"description": "Budva'nın modern yüzünü yansıtan Akacia Coffee, kentin en iyi kavrulmuş çekirdeklerini ve taze pastane ürünlerini sunar. Kentsel koşturmacadan uzaklaşmak isteyenler için şık tasarımıyla huzurlu bir mola noktasıdır.", "description_en": "Reflecting Budva's modern side, Akacia Coffee offers the city's best roasted beans and fresh pastry products. With its stylish design, it's a peaceful break point for those wanting to escape urban hustle.", "tips": "Filtre kahve seçenekleri oldukça geniştir; yanına taze meyveli tartlarını denemeyi unutmayın.", "tips_en": "The filter coffee options are quite extensive; don't forget to try their fresh fruit tarts along with it.", "category": "Sosyal"},
        "Fluffy pancakes Budva": {"description": "Budva'nın en tatlı duraklarından biri olan bu mekan, puf puf Japon usulü pankekleriyle kentin gastronomi dünyasına neşeli bir soluk getiriyor. Hem çocuklar hem de tatlı severler için kentsel bir lezzet şölenidir.", "description_en": "One of Budva's sweetest stops, this place brings a cheerful breath to the city's gastronomic world with its fluffy Japanese-style pancakes. It's an urban flavor feast for both children and sweet lovers.", "tips": "Pankeklerin hazırlanması 15-20 dakika sürebilir, beklemeye değer; üzerine yerel bal dökülmüş versiyonu favoridir.", "tips_en": "Preparation of pancakes can take 15-20 minutes, well worth the wait; the version drizzled with local honey is a favorite.", "category": "Sosyal"},
        "Modern Gallery": {"description": "Budva Eski Şehir'in kalbinde yer alan Jovo Ivanovic Modern Galerisi, Karadağlı ve uluslararası sanatçıların modern eserlerini sergiler. Kentin tarihi dokusuyla modern sanatın buluştuğu en prestijli kültürel duraktır.", "description_en": "Located in the heart of Budva Old Town, the Jovo Ivanovic Modern Gallery exhibits modern works by Montenegrin and international artists. It is the most prestigious cultural stop where the city's historical texture meets modern art.", "tips": "Giriş ücretsizdir; galerinin üst katındaki pencerelerden Eski Şehir sokaklarını izlemek büyüleyicidir.", "tips_en": "Entry is free; watching the Old Town streets from the windows on the gallery's upper floor is magical.", "category": "Kültür"},
        "Dva Vesla": {"description": "Budva sahilinde yer alan Dva Vesla, taze deniz ürünleri ve geleneksel Adriyatik mutfağıyla kentin en köklü restoranlarından biridir. Denize sıfır konumu ve samimi servisiyle kentsel yaz akşamlarının vazgeçilmez adresidir.", "description_en": "Located on the Budva coast, Dva Vesla is one of the city's most established restaurants with fresh seafood and traditional Adriatic cuisine. With its beachfront location and sincere service, it's an indispensable address for urban summer evenings.", "tips": "Kalamar tava ve yerel beyaz şarapları çok başarılıdır; akşam yemeği için liman manzarasını tercih edin.", "tips_en": "Their fried calamari and local white wines are very successful; prefer the harbor view for dinner.", "category": "Restoran"}
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    highlights = data if isinstance(data, list) else data.get('highlights', [])
        
    for h in highlights:
        name = h.get('name')
        # Check if name is in updates, or name_en (sometimes they vary)
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

# Apply updates
apply_updates('assets/cities/bari.json', all_updates['Bari'])
apply_updates('assets/cities/budva.json', all_updates['Budva'])

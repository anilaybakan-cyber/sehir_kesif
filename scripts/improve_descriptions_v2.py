#!/usr/bin/env python3
"""
Enhanced script to improve ALL short/generic POI descriptions.
Targets descriptions under 100 characters and generates rich, detailed content.
"""

import json
import os
import glob
import random

def generate_description(poi, city_name):
    """Generate a rich, detailed Turkish description based on POI attributes"""
    name = poi.get('name', '')
    area = poi.get('area', '')
    category = poi.get('category', '')
    tags = poi.get('tags', [])
    rating = poi.get('rating', 0)
    price = poi.get('price', 'medium')
    subcategory = poi.get('subcategory', '')
    
    # Joined tags for context
    tag_context = ', '.join(tags[:3]) if tags else ''
    
    # Very detailed category-based descriptions
    descriptions = {
        'Müze': [
            f"{name}, {city_name}'nin kültürel zenginliğinin en güzel örneklerinden birini sergiliyor. {area} bölgesinde konumlanan bu müze, dünya çapında tanınan eserleri, interaktif sergileri ve eğitici programlarıyla her yaş grubundan ziyaretçiye hitap ediyor. Rehberli turlar sayesinde eserlerin hikayelerini derinlemesine keşfetme imkanı bulabilirsiniz.",
            f"Sanat ve tarih meraklılarının uğrak noktası {name}, {area}'nın en prestijli müzelerinden biri olarak öne çıkıyor. Özenle düzenlenmiş koleksiyonu, dönemsel sergiler ve son teknoloji sunum yöntemleriyle ziyaretçilerine unutulmaz bir deneyim vaat ediyor.",
            f"{name}, {city_name}'nin sanat sahnesinin nabzını tutan önemli bir kültür merkezi. {area} bölgesindeki modern binası, kalıcı ve geçici sergiler, atölye çalışmaları ve özel etkinlikleriyle yıl boyunca ziyaret edilmeye değer.",
        ],
        'Tarihi': [
            f"{name}, {city_name}'nin zengin tarihine tanıklık eden muhteşem bir yapı. {area} bölgesindeki bu anıtsal mekan, yüzyılların izlerini taşıyan mimarisi, özgün detayları ve kültürel önemiyle hem tarih tutkunlarını hem mimari severlerini büyülüyor.",
            f"Geçmişin görkemini günümüze taşıyan {name}, {area}'nın en önemli tarihi yapılarından biri. Restorasyonlarla korunan özgün dokusu, dönemin yaşam tarzını yansıtan eserleri ve muhteşem mimarisiyle keşfedilmeyi bekliyor.",
            f"{name}, {city_name} tarihinin en parlak dönemlerinden kalma nadide bir miras. {area} bölgesindeki konumuyla şehrin geçmişine açılan bir pencere olan bu yapı, rehberli turlar ve sesli rehber seçenekleriyle zenginleştirilmiş bir ziyaret deneyimi sunuyor.",
        ],
        'Park': [
            f"{name}, {city_name}'nin yeşil ciğerlerinden biri olarak {area} bölgesinde huzur arayanları bekliyor. Geniş çim alanları, gölgelik yürüyüş yolları, çocuk oyun alanları ve piknik noktalarıyla ailelerin ve doğa severlerin favorisi.",
            f"Şehrin kalabalığından kaçış arayanlar için {name} mükemmel bir sığınak. {area}'daki bu yeşil vaha, botanik çeşitliliği, kuş gözlem noktaları ve mevsimlik çiçek bahçeleriyle her ziyarette farklı bir güzellik sunuyor.",
            f"{name}, {area} bölgesinin en sevilen buluşma noktalarından. Sabah koşucuları, öğleden sonra kitap okuyanlar ve akşam piknik yapan ailelerle dolu olan bu park, {city_name}'nin sosyal yaşamının önemli bir parçası.",
        ],
        'Yeme-İçme': [
            f"{name}, {city_name} mutfağının en iyi temsilcilerinden biri olarak {area}'da gurmeleri ağırlıyor. Yerel çiftçilerden temin edilen taze malzemeler, kuşaktan kuşağa aktarılan tarifler ve ustaca hazırlanan sunumlarla damak tadınıza hitap ediyor.",
            f"Otantik lezzetlerin adresi {name}, {area} bölgesinin en çok tercih edilen mekanlarından. Sıcak ambiyansı, özenli servisi ve zengin menüsüyle hem yerel halkın hem turistlerin vazgeçilmezi haline gelmiş.",
            f"{name}, {city_name}'nin gastronomi sahnesinde önemli bir yere sahip. {area}'daki bu mekan, geleneksel tariflere modern dokunuşlar ekleyen yaratıcı mutfağı ve seçkin içecek menüsüyle özel bir deneyim vaat ediyor.",
        ],
        'Mahalle': [
            f"{name}, {city_name}'nin karakterini en iyi yansıtan semtlerden biri. Tarihi binaları, dar sokakları, yerel dükkanları ve sokak sanatıyla dolu duvarlarıyla gezginin kaybolmak isteyeceği türden bir mahalle. Her köşede yeni bir keşif sizi bekliyor.",
            f"Yerel yaşamın en canlı hali {name}'de karşınıza çıkıyor. {area} bölgesindeki bu semt, sabah pazarları, aile işletmesi kafeler, vintage dükkanlar ve gece hayatıyla 24 saat yaşayan bir atmosfer sunuyor.",
            f"{name}, {city_name}'nin ruhunu en iyi hissedebileceğiniz yerlerden. Tarihi dokusu korunmuş sokakları, komşuluk kültürü ve özgün atmosferiyle şehrin turistik olmayan yüzünü keşfetmek isteyenler için ideal.",
        ],
        'Manzara': [
            f"{name}, {city_name}'nin nefes kesen panoramasını sunan en iyi bakış noktalarından biri. {area} bölgesindeki bu nokta, özellikle gün batımında altın ve mor tonlarının gökyüzünü kapladığı anlarda fotoğrafçılar için cennet.",
            f"Şehri kuş bakışı görmek isteyenler için {name} kaçırılmamalı. {area}'daki bu manzara noktası, gündüz şehrin siluetini, gece ise ışıl ışıl bir halı gibi yayılan şehir ışıklarını izleme imkanı sunuyor.",
            f"{name}, {city_name}'nin en romantik köşelerinden. {area} bölgesindeki bu nokta, özel günlerde, evlilik teklifleri için veya sadece şehrin güzelliğine hayran kalmak için tercih edilen büyüleyici bir mekan.",
        ],
        'Kültür': [
            f"{name}, {city_name}'nin kültürel yaşamının merkezi konumunda. {area}'daki bu mekan, dünya çapında sanatçıların performansları, çağdaş sanat sergileri ve interaktif etkinlikleriyle şehrin yaratıcı enerjisini yansıtıyor.",
            f"Sanat ve kültür tutkunlarının buluşma noktası {name}. {area} bölgesindeki zengin programı, atölye çalışmaları ve özel etkinlikleriyle her ziyarette farklı bir deneyim vaat ediyor.",
        ],
        'Kafe': [
            f"{name}, {city_name}'nin kahve kültürünün en güzel örneklerinden birini sunuyor. {area}'daki bu samimi mekan, özenle hazırlanan içecekleri, ev yapımı tatlıları ve huzurlu atmosferiyle mola vermek için ideal.",
            f"Şehrin en sevilen buluşma noktalarından {name}, {area} bölgesinde kahve tutkunlarını ağırlıyor. Kaliteli çekirdekler, vintage dekor ve dostane servis anlayışıyla her gün yeni müdavimler kazanıyor.",
        ],
        'Restoran': [
            f"{name}, {city_name}'nin en prestijli restoranlarından biri olarak {area}'da gastronomi tutkunlarını ağırlıyor. Şefin imza yemekleri, mevsimlik menüler ve özenli şarap seçkisiyle özel akşamlar için mükemmel bir tercih.",
            f"Gurmelerin vazgeçilmez adresi {name}, {area} bölgesinin en çok konuşulan restoranlarından. Yerel tatları uluslararası tekniklerle buluşturan yaratıcı mutfağı ve zarif ambiyansıyla fark yaratıyor.",
        ],
        'Bar': [
            f"{name}, {city_name}'nin gece hayatının en heyecan verici duraklarından biri. {area}'daki bu mekan, özel kokteylleri, canlı müziği ve enerjik atmosferiyle geceye renk katıyor.",
            f"Şehrin en cool barlarından {name}, {area} bölgesinde gece kuşlarını ağırlıyor. Yaratıcı içecek menüsü, DJ performansları ve şık iç mekanıyla unutulmaz geceler vaat ediyor.",
        ],
        'Sokak': [
            f"{name}, {city_name}'nin en ikonik ve canlı caddelerinden biri. {area} bölgesindeki bu cadde, tarihi yapıları, sokak sanatçıları, butik dükkanları ve çeşitli restoranlarıyla gündüzden geceye kadar keşfedilmeye değer.",
            f"Şehrin nabzının attığı yer {name}. {area}'daki bu ünlü cadde, yerel kültürün, ticaretin ve sosyal hayatın buluştuğu canlı bir arter olarak hem turistlerin hem yerel halkın favorisi.",
        ],
        'Plaj': [
            f"{name}, {city_name}'nin en güzel sahil deneyimlerinden birini sunuyor. {area} bölgesindeki bu plaj, berrak suları, temiz kumsalı ve çevresindeki plaj barlarıyla yaz günlerinin vazgeçilmezi.",
            f"Güneş, deniz ve eğlencenin bir arada olduğu {name}, {area}'nın en popüler plajlarından. Su sporları, sahil voleybolu ve gün batımı partileriyle her yaştan ziyaretçiye hitap ediyor.",
        ],
        'Spor': [
            f"{name}, {city_name}'nin spor tarihinin en önemli sahnelerinden biri. {area}'daki bu tesiste unutulmaz maçlar izleyebilir, stadyum turuna katılabilir veya müzesinde efsanevi anları yeniden yaşayabilirsiniz.",
            f"Tutku ve rekabetin buluştuğu {name}, taraftar kültürünün en yoğun yaşandığı yerlerden. Maç günlerinin elektrikli atmosferi veya sakin günlerde yapılan turlar, sporseverler için benzersiz deneyimler sunuyor.",
        ],
        'Aktivite': [
            f"{name}, {city_name}'de eğlence ve macera arayanlar için harika bir seçenek. {area} bölgesindeki bu mekan, adrenalin dolu aktiviteleri, eğitici deneyimleri ve aile dostu etkinlikleriyle keyifli saatler vaat ediyor.",
            f"Aksiyon dolu bir gün geçirmek isteyenler için {name} ideal bir tercih. {area}'daki bu mekanda hem fiziksel aktiviteler hem de interaktif deneyimlerle enerjinizi yükseltebilirsiniz.",
        ],
        'Meydan': [
            f"{name}, {city_name}'nin sosyal hayatının kalbi. {area} bölgesindeki bu tarihi meydan, çevresindeki kafeler, tarihi binalar ve sokak sanatçılarıyla şehrin atmosferini en yoğun hissedeceğiniz yerlerden.",
            f"Şehrin buluşma noktası {name}, yüzyıllardır {area}'nın merkezi olma özelliğini koruyor. Önemli etkinliklere ev sahipliği yapan, yerel halkın ve turistlerin kaynaştığı canlı bir meydan.",
        ],
        'Kilise': [
            f"{name}, {city_name}'nin dini mirasının en etkileyici örneklerinden. {area}'daki bu kutsal mekan, görkemli mimarisi, tarihi freskleri ve huzurlu atmosferiyle hem inanç sahiplerini hem mimari tutkunlarını cezbediyor.",
        ],
        'Cami': [
            f"{name}, İslam mimarisinin {city_name}'deki en güzel örneklerinden. {area} bölgesindeki bu cami, zarif minareleri, el işi çinileri ve manevi atmosferiyle hem ibadet hem de kültürel keşif için değerli bir mekan.",
        ],
    }
    
    # Get appropriate description
    if category in descriptions:
        desc_list = descriptions[category]
        return random.choice(desc_list)
    
    # Default for unknown categories
    return f"{name}, {city_name}'nin {area} bölgesinde bulunan dikkat çekici bir nokta. Eşsiz özellikleri ve sunduğu deneyimle ziyaretçilerine unutulmaz anlar yaşatıyor. Bölgenin en çok ziyaret edilen yerlerinden biri olarak her gezginin listesinde yer almalı."

def generate_description_en(poi, city_name):
    """Generate a rich, detailed English description based on POI attributes"""
    name = poi.get('name', '')
    area = poi.get('area', '')
    category = poi.get('category', '')
    
    descriptions_en = {
        'Müze': [
            f"{name} showcases one of the finest examples of {city_name}'s cultural richness. Located in {area}, this museum appeals to visitors of all ages with its world-renowned works, interactive exhibits, and educational programs.",
            f"A must-visit for art and history enthusiasts, {name} stands out as one of {area}'s most prestigious museums. With its carefully curated collection, seasonal exhibitions, and state-of-the-art presentation methods, it promises an unforgettable experience.",
        ],
        'Tarihi': [
            f"{name} is a magnificent structure witnessing {city_name}'s rich history. This monumental venue in {area} enchants both history buffs and architecture lovers with its centuries-old architecture and cultural significance.",
            f"Carrying the glory of the past to the present, {name} is one of {area}'s most important historical structures. Its preserved original texture and magnificent architecture await discovery.",
        ],
        'Park': [
            f"{name} awaits those seeking peace in {area} as one of {city_name}'s green lungs. With its wide lawns, shaded walking paths, children's playgrounds and picnic spots, it's a favorite among families and nature lovers.",
            f"For those seeking escape from the city's crowds, {name} is a perfect sanctuary. This green oasis in {area} offers different beauty each visit with its botanical diversity and seasonal flower gardens.",
        ],
        'Yeme-İçme': [
            f"{name} hosts gourmets in {area} as one of the best representatives of {city_name}'s cuisine. Fresh ingredients from local farmers, recipes passed down through generations, and masterful presentations satisfy every palate.",
            f"The address of authentic flavors, {name} is one of {area}'s most preferred venues. With its warm ambiance, attentive service and rich menu, it has become indispensable for both locals and tourists.",
        ],
        'Mahalle': [
            f"{name} is one of the neighborhoods that best reflects {city_name}'s character. With its historic buildings, narrow streets, local shops and walls full of street art, it's the kind of neighborhood where travelers want to get lost.",
            f"Local life at its most vibrant can be found in {name}. This neighborhood in {area} offers a 24-hour living atmosphere with its morning markets, family-run cafes, vintage shops and nightlife.",
        ],
        'Manzara': [
            f"{name} is one of the best viewpoints offering a breathtaking panorama of {city_name}. This spot in {area} is paradise for photographers, especially at sunset when gold and purple tones fill the sky.",
            f"For those wanting a bird's eye view of the city, {name} is unmissable. This viewpoint in {area} offers the chance to watch the city's silhouette by day and the sparkling city lights spreading like a carpet by night.",
        ],
        'Kültür': [
            f"{name} is at the center of {city_name}'s cultural life. This venue in {area} reflects the city's creative energy with performances by world-class artists, contemporary art exhibitions and interactive events.",
        ],
        'Kafe': [
            f"{name} offers one of the finest examples of {city_name}'s coffee culture. This cozy venue in {area} is ideal for a break with its carefully crafted drinks, homemade desserts and peaceful atmosphere.",
        ],
        'Restoran': [
            f"{name} hosts gastronomy enthusiasts in {area} as one of {city_name}'s most prestigious restaurants. With the chef's signature dishes, seasonal menus and careful wine selection, it's a perfect choice for special evenings.",
        ],
        'Bar': [
            f"{name} is one of the most exciting stops in {city_name}'s nightlife. This venue in {area} adds color to the night with its special cocktails, live music and energetic atmosphere.",
        ],
        'Sokak': [
            f"{name} is one of {city_name}'s most iconic and vibrant streets. This avenue in {area} is worth exploring from day to night with its historic buildings, street performers, boutique shops and various restaurants.",
        ],
        'Plaj': [
            f"{name} offers one of the best beach experiences in {city_name}. This beach in {area} is essential for summer days with its crystal clear waters, clean sand and surrounding beach bars.",
        ],
        'Spor': [
            f"{name} is one of the most important stages in {city_name}'s sports history. At this facility in {area}, you can watch unforgettable matches, join stadium tours or relive legendary moments in its museum.",
        ],
        'Aktivite': [
            f"{name} is a great choice for those seeking fun and adventure in {city_name}. This venue in {area} promises enjoyable hours with its adrenaline-filled activities, educational experiences and family-friendly events.",
        ],
        'Meydan': [
            f"{name} is the heart of {city_name}'s social life. This historic square in {area} is one of the places where you can most intensely feel the city's atmosphere with its surrounding cafes, historic buildings and street artists.",
        ],
        'Mahalle': [
            f"{name} is one of the neighborhoods that best captures the essence of {city_name}. With its historic architecture, local markets, artisan shops, and authentic atmosphere, this neighborhood offers a genuine glimpse into daily life in {area}.",
        ],
    }
    
    if category in descriptions_en:
        desc_list = descriptions_en[category]
        return random.choice(desc_list)
    
    return f"{name} is a noteworthy destination in {city_name}'s {area} district. With its unique features and experiences, it offers unforgettable moments to visitors. As one of the most visited places in the area, it deserves a spot on every traveler's list."

def process_city(filepath):
    """Process a single city JSON file and improve short descriptions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    city_name = data.get('city', 'Unknown')
    highlights = data.get('highlights', [])
    
    improved_count = 0
    
    for poi in highlights:
        desc = poi.get('description', '')
        desc_en = poi.get('description_en', '')
        
        # Check and improve Turkish description if too short
        if len(desc) < 100:
            new_desc = generate_description(poi, city_name)
            poi['description'] = new_desc
            improved_count += 1
        
        # Check and improve English description if too short
        if len(desc_en) < 80:
            new_desc_en = generate_description_en(poi, city_name)
            poi['description_en'] = new_desc_en
    
    # Save updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return city_name, improved_count

def main():
    city_files = sorted(glob.glob('assets/cities/*.json'))
    
    print(f"Found {len(city_files)} city files")
    print("=" * 50)
    
    total_improved = 0
    
    for filepath in city_files:
        city_name, count = process_city(filepath)
        if count > 0:
            print(f"✅ {city_name}: {count} descriptions improved")
            total_improved += count
        else:
            print(f"⚪ {city_name}: All descriptions OK")
    
    print("=" * 50)
    print(f"Total: {total_improved} descriptions improved across all cities")

if __name__ == "__main__":
    main()

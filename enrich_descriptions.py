import json
import os
import glob

# Cities directory
cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

# 1. SPECIFIC RICH DESCRIPTIONS (Hand-crafted)
# -----------------------------------------------------------------------------
rich_descriptions = {
    # BARCELONA
    "Sagrada Familia": "Antoni Gaudí'nin 1882'de devraldığı ve hala yapımı süren dünyaca ünlü bazilika. Gotik ve Art Nouveau tarzlarını birleştiren bu mimari şaheser, her cephesinde İncil'den farklı hikayeleri betimleyen, doğadan esinlenmiş sütunları ve ışık oyunlarıyla büyüleyen bir atmosfere sahip.",
    "Park Güell": "Gaudí'nin en renkli ve hayal gücünü zorlayan eserlerinden biri. Başlangıçta lüks bir konut sitesi olarak planlanan ancak daha sonra halka açık bir parka dönüşen bu alan, organik formları, ünlü mozaik kertenkelesi ve şehri kuş bakışı gören terasıyla masalsı bir deneyim sunuyor.",
    "Casa Batlló": "Passeig de Gràcia üzerinde yer alan, 'Kemikler Evi' olarak da bilinen modernizm harikası. Dalgalı cephesi, renkli seramikleri ve ejderha sırtını andıran çatısı, Gaudí'nin doğaya olan tutkusunun en sanatsal dışavurumlarından biridir.",
    "Casa Milà": "Halk arasında 'La Pedrera' (Taş Ocağı) olarak bilinen Casa Milà, Gaudí'nin tamamladığı son sivil yapıdır. Dalgalı taş cephesi ve sürrealist bacalarıyla ünlü terası, mimarlık tarihinin en ikonik yapılarından biri olarak kabul edilir.",
    "La Rambla": "Şehrin kalbinin attığı, Placa de Catalunya'dan limana kadar uzanan canlı bulvar. Sokak sanatçıları, çiçekçiler, kafeler ve ünlü La Boqueria pazarıyla dolu bu cadde, Barcelona'nın enerjisini hissetmek için en doğru adres.",
    "Mercado de La Boqueria": "Avrupa'nın en iyi gıda pazarlarından biri. Taze meyvelerden deniz ürünlerine, jamón tezgahlarından tapas barlarına kadar uzanan renkli ve lezzetli bir dünya. Yerel gastronomiyi keşfetmek için bir cennet.",
    "Barri Gòtic": "Şehrin en eski yerleşimi olan Gotik Mahalle, dar ve labirent gibi sokaklarıyla Roma döneminden günümüze uzanan bir tarih yolculuğu sunuyor. Katedraller, gizli meydanlar ve antik duvarlar arasında kaybolmak büyüleyici.",
    "Camp Nou": "Futbol tutkunlarının mabedi ve FC Barcelona'nın evi. Avrupa'nın en büyük stadyumu olmasının yanı sıra, kulübün tarihini anlatan müzesiyle sporseverler için unutulmaz bir deneyim sunuyor.",
    "Picasso Müzesi": "Ünlü ressam Pablo Picasso'nun erken dönem eserlerine ev sahipliği yapan müze, sanatçının Barcelona ile olan derin bağını gözler önüne seriyor. Beş adet gotik sarayın birleşimiyle oluşan bina, başlı başına bir sanat eseri.",
    "Barceloneta Plajı": "Şehir merkezine yürüme mesafesinde, Akdeniz'in keyfini çıkarabileceğiniz canlı bir sahil şeridi. Altın sarısı kumları, sahil boyu uzanan restoranları (chiringuitos) ve modern mimarisiyle hem dinlenmek hem eğlenmek için ideal.",

    # ISTANBUL
    "Ayasofya": "Yaklaşık 1500 yıllık tarihiyle dünya mimarlık tarihinin en önemli anıtlarından biri. Bizans ve Osmanlı imparatorluklarına tanıklık etmiş, devasa kubbesi ve eşsiz mozaikleriyle büyüleyen bu yapı, İstanbul'un en ikonik simgesi.",
    "Topkapı Sarayı": "Osmanlı padişahlarına 400 yıl boyunca ev sahipliği yapmış, imparatorluğun yönetim merkezi. Harem dairesi, Kutsal Emanetler bölümü, ihtişamlı avluları ve eşsiz Boğaz manzarasıyla tarihin kalbinde bir yolculuk.",
    "Sultanahmet Camii": "İç mekanını süsleyen 20.000'den fazla mavi İznik çinisi nedeniyle 'Blue Mosque' olarak da bilinir. 6 minaresi ve zarif kubbe yapısıyla Osmanlı mimarisinin zirve noktalarından biri.",
    "Kapalıçarşı": "Dünyanın en eski ve en büyük kapalı çarşılarından biri. Labirent gibi sokaklarında kuyumculardan halıcılara, baharatçılardan antikacılara kadar binlerce dükkanın yer aldığı, ticaretin ve tarihin yaşayan merkezi.",
    "Galata Kulesi": "Cenevizlilerden kalma tarihi kule, İstanbul'un en güzel panoramik manzaralarından birini sunuyor. Tarih boyunca gözetleme kulesi, hapishane ve rasathane olarak kullanılan yapı, günümüzde şehrin en popüler seyir terası.",
    "Yerebatan Sarnıcı": "Bizans döneminden kalma bu büyüleyici yeraltı sarnıcı, suyun içinden yükselen yüzlerce mermer sütunu ve gizemli Medusa başlarıyla ziyaretçilerini mistik bir atmosfere davet ediyor.",
    "Dolmabahçe Sarayı": "Osmanlı'nın son dönem ihtişamını yansıtan, Avrupa barok tarzında inşa edilmiş saray. Atatürk'ün hayata gözlerini yumduğu yer olmasıyla da Türk milleti için ayrı bir manevi değere sahip.",
    "Mısır Çarşısı": "Tarihi İpek Yolu'nun son duraklarından biri. Rengarenk baharatlar, lokumlar, kuruyemişler ve şifalı otlarla dolu tezgahlarıyla hem göze hem damağa hitap eden, kokusuyla baş döndüren bir çarşı.",
    "Taksim Meydanı": "Modern İstanbul'un kalbi ve buluşma noktası. Cumhuriyet Anıtı'na ev sahipliği yapan meydan, ünlü İstiklal Caddesi'nin başlangıcı olup, şehrin en canlı, kozmopolit ve hareketli noktasıdır.",
    "Kız Kulesi": "İstanbul Boğazı'nın ortasında süzülen, hakkında sayısız efsane anlatılan zarif yapı. 2500 yıllık tarihiyle şehrin romantik simgesi ve Asya ile Avrupa arasındaki eşsiz bir nöbetçi.",
}

# 2. TEMPLATES (For places without specific descriptions)
# -----------------------------------------------------------------------------
templates = {
    "Tarihi": "{name}, {area} bölgesinin tarihine ışık tutan önemli bir yapı. Geçmişin izlerini günümüze taşıyan mimarisi ve kültürel mirasıyla, tarih meraklıları için keşfedilmeyi bekleyen bir hazine.",
    "Manzara": "{name}, şehrin en etkileyici manzaralarından birine ev sahipliği yapıyor. Özellikle gün batımında sunduğu görsel şölen ve {area} bölgesine hakim konumuyla fotoğraf tutkunları için vazgeçilmez bir nokta.",
    "Park": "{name}, şehir hayatının karmaşasından uzaklaşıp nefes almak isteyenler için {area} bölgesinde yeşil bir vaha. Yürüyüş yolları, dinlenme alanları ve huzurlu atmosferiyle doğayla baş başa kalmak için ideal.",
    "Müze": "{name}, zengin koleksiyonu ve etkileyici sergileriyle kültür sanat severlerin uğrak noktası. {area} bölgesinde yer alan mekan, ziyaretçilerine ilham verici ve öğretici bir deneyim sunuyor.",
    "Restoran": "{name}, {area} bölgesinin en popüler lezzet duraklarından biri. Özenle hazırlanan menüsü, kaliteli hizmeti ve {subcategory} mutfağının seçkin örnekleriyle hem göze hem damağa hitap ediyor.",
    "Kafe": "{name}, {area} sokaklarında keyifli bir mola vermek için harika bir seçenek. Samimi atmosferi, lezzetli kahveleri ve tatlılarıyla gününüze enerji katacak sıcak bir mekan.",
    "Bar": "{name}, {area} gece hayatının nabzını tutan, enerjisi yüksek bir mekan. Özel kokteylleri, müziği ve canlı atmosferiyle arkadaşlarınızla keyifli vakit geçirebileceğiniz popüler bir adres.",
    "Alışveriş": "{name}, {area} bölgesinde alışveriş tutkunları için çeşitli seçenekler sunuyor. Yerel tasarımlardan popüler markalara kadar aradığınız pek çok şeyi bulabileceğiniz canlı bir nokta.",
    "Plaj": "{name}, güneşin ve denizin tadını çıkarmak isteyenler için mükemmel bir kaçış noktası. Temiz kumsalı ve ferah atmosferiyle yaz günlerinin vazgeçilmez adresi.",
    "Semt": "{name}, şehrin en karakteristik bölgelerinden biri. Renkli sokakları, yerel dükkanları ve kendine has dokusuyla {area} ruhunu en iyi yansıtan, keşfetmeye doyamayacağınız bir semt.",
    "Semt": "{name}, şehrin en karakteristik bölgelerinden biri. Renkli sokakları, yerel dükkanları ve kendine has dokusuyla {area} ruhunu en iyi yansıtan, keşfetmeye doyamayacağınız bir semt.",
    "Meydan": "{name}, şehrin ritminin hissedildiği canlı bir buluşma noktası. Tarihi dokusu ve çevresindeki mekanlarla {area} bölgesinin sosyal hayatının kalbi konumunda.",
    "Eğlence": "{name}, {area} bölgesinde keyifli vakit geçirmek isteyenler için ideal bir durak. Sunduğu aktiviteler ve atmosferiyle ziyaretçilerine unutulmaz anlar yaşatıyor.",
    "Sanat": "{name}, sanatseverler için ilham verici bir merkez. {area} bölgesinde yer alan mekan, özgün eserleri ve kültürel atmosferiyle ziyaretçilerini büyüleyici bir yolculuğa çıkarıyor."
}

def generate_description(place, city_name=""):
    name = place.get("name", "")
    category = place.get("category", "")
    area = place.get("area", "Şehir Merkezi")
    subcategory = place.get("subcategory", "yerel")
    
    # 1. Check specific descriptions first
    for key, desc in rich_descriptions.items():
        if key == name: 
            return desc
        if key in name and len(key) > 5:
            return desc

    # 2. Check current description length
    # EXCEPTION: For Barcelona, we overwrite EVERYTHING (unless it matches the specific description we just returned)
    current_desc = place.get("description", "")
    if len(current_desc) > 120 and city_name != "Barcelona":
        return current_desc

    # 3. Use template
    if category in templates:
        return templates[category].format(
            name=name, 
            area=area, 
            subcategory=subcategory.lower() if subcategory else "yerel"
        )
    
    # 4. Fallback (Force update for Barcelona)
    fallback_desc = f"{name}, {area} bölgesinde yer alan ve ziyaretçilerine {subcategory if subcategory else 'keyifli'} bir deneyim sunan popüler bir {category.lower()} noktası. Şehrin dokusunu hissetmek için harika bir durak."
    
    if city_name == "Barcelona":
        return fallback_desc
        
    return current_desc if current_desc else fallback_desc

def process_files():
    json_files = glob.glob(os.path.join(cities_dir, "*.json"))
    print(f"Found {len(json_files)} JSON files.")
    
    total_updated = 0
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get("city", "Unknown")
            highlights = data.get("highlights", [])
            updated_count = 0
            
            for place in highlights:
                new_desc = generate_description(place, city_name)
                # Only update if description changed
                if new_desc != place.get("description", ""):
                    place["description"] = new_desc
                    updated_count += 1
            
            if updated_count > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"Updated {city_name}: Enriched {updated_count} descriptions.")
                total_updated += updated_count
            else:
                print(f"Skipped {city_name}: No updates needed.")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    print(f"Finished! Total {total_updated} descriptions enriched.")

if __name__ == "__main__":
    process_files()

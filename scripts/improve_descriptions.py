#!/usr/bin/env python3
"""
Script to improve generic/template POI descriptions across all city JSON files.
Identifies template patterns and generates richer, more descriptive content.
"""

import json
import os
import glob
import re

# Template patterns to detect (Turkish)
TEMPLATE_PATTERNS = [
    r"bölgesinde yer alan ve ziyaretçilerine .+ bir deneyim sunan popüler bir",
    r"Şehrin dokusunu hissetmek için harika bir durak",
    r"popüler bir .+ noktası\. Şehrin dokusunu",
    r"zengin koleksiyonu ve etkileyici sergileriyle kültür sanat severlerin uğrak noktası",
    r"Yerel halkın favori noktalarından biri, keyfini çıkarın!",
]

# English template patterns
TEMPLATE_PATTERNS_EN = [
    r"is a popular .+ in the .+ district offering visitors",
    r"A great stop to feel the city's texture",
    r"One of the locals' favorite spots, enjoy!",
    r"is a destination for art and culture enthusiasts with its rich collection",
]

def is_template_description(desc):
    """Check if description matches template patterns"""
    if not desc:
        return False
    for pattern in TEMPLATE_PATTERNS:
        if re.search(pattern, desc, re.IGNORECASE):
            return True
    return False

def is_template_description_en(desc):
    """Check if English description matches template patterns"""
    if not desc:
        return False
    for pattern in TEMPLATE_PATTERNS_EN:
        if re.search(pattern, desc, re.IGNORECASE):
            return True
    return False

def generate_description(poi, city_name):
    """Generate a richer description based on POI attributes"""
    name = poi.get('name', '')
    area = poi.get('area', '')
    category = poi.get('category', '')
    tags = poi.get('tags', [])
    rating = poi.get('rating', 0)
    price = poi.get('price', 'medium')
    
    # Category-based description templates (much more varied and specific)
    descriptions = {
        'Müze': [
            f"{name}, {city_name}'nin en değerli kültürel hazinelerinden birini barındırıyor. {area} bölgesindeki bu mekan, zengin koleksiyonu ve özenle hazırlanmış sergileriyle ziyaretçilerine benzersiz bir sanat yolculuğu vaat ediyor.",
            f"Sanat ve tarih tutkunlarının vazgeçilmez durağı {name}. {area}'da konumlanan müze, nadir eserleri ve interaktif sergileriyle hem öğretici hem ilham verici bir deneyim sunuyor.",
        ],
        'Tarihi': [
            f"{name}, yüzyılların izlerini taşıyan görkemli yapısıyla {city_name}'nin tarihine açılan bir pencere. {area} bölgesindeki bu anıt, mimari ihtişamı ve kültürel önemiyle mutlaka görülmeli.",
            f"Tarihin derinliklerinden günümüze uzanan {name}, {area}'nın en etkileyici yapılarından biri. Geçmişin izlerini taşıyan duvarları, ziyaretçileri zamanda yolculuğa çıkarıyor.",
        ],
        'Park': [
            f"{name}, şehrin kalabalığından uzaklaşmak isteyenler için {area}'da saklı bir cennet. Yeşil alanları, yürüyüş parkurları ve huzurlu atmosferiyle hem yerel halk hem turistler için mükemmel bir kaçış noktası.",
            f"Doğanın ve şehir hayatının kusursuz birleşimi olan {name}. {area} bölgesindeki bu park, piknik alanları ve botanik zenginliğiyle her mevsim ziyaret edilebilir.",
        ],
        'Yeme-İçme': [
            f"{name}, {city_name} mutfağının en otantik lezzetlerini sunan eşsiz bir mekan. {area}'daki bu adres, yerel malzemeler ve geleneksel tariflerle damak zevkinize unutulmaz bir şölen vaat ediyor.",
            f"Gurmelerin gözdesi {name}, {area} bölgesinin en sevilen yeme-içme adreslerinden. Şefin özel tarifleri ve samimi atmosferiyle yemek deneyimini bir üst seviyeye taşıyor.",
        ],
        'Mahalle': [
            f"{name}, {city_name}'nin en karakteristik semtlerinden biri. Tarihi dokusu, butik dükkanları ve sokak kültürüyle şehrin ruhunu en iyi yansıtan yerlerden. Kaybolmaktan korkmadan keşfe çıkın.",
            f"Yerel yaşamın nabzını tutmak isteyenler için {name} ideal bir başlangıç noktası. {area}'nın dar sokakları, renkli cepheleri ve canlı atmosferi sizi bekliyor.",
        ],
        'Manzara': [
            f"{name}, {city_name}'nin nefes kesen panoramasını sunan büyüleyici bir nokta. Özellikle gün batımında altın ışıkların şehri sardığı anlarda, fotoğrafçılar ve romantikler için cennet.",
            f"Şehrin siluetini kuş bakışı görmek isteyenler için {name} mutlaka listede olmalı. {area}'daki bu nokta, gece ışıkları ve gündüz manzarasıyla eşit derecede etkileyici.",
        ],
        'Kültür': [
            f"{name}, {city_name}'nin kültürel kalbinin attığı yerlerden. {area}'daki bu mekan, sanat performansları, sergiler ve etkinlikleriyle şehrin yaratıcı ruhunu yansıtıyor.",
            f"Kültür ve sanat tutkunlarının buluşma noktası {name}. Düzenli etkinlikleri ve zengin programıyla {area} bölgesinin en canlı kültür merkezlerinden.",
        ],
        'Sokak': [
            f"{name}, {city_name}'nin en ikonik caddelerinden biri. Tarihi binalar, sokak sanatçıları ve canlı atmosferiyle hem gündüz hem gece büyülü bir yürüyüş deneyimi sunuyor.",
            f"Şehrin nabzını en iyi hissedebileceğiniz yerlerden biri olan {name}. Kafeler, dükkanlar ve sokak kültürüyle {area}'nın kalbi burada atıyor.",
        ],
        'Plaj': [
            f"{name}, Akdeniz'in berrak sularında serinlemek ve güneşin tadını çıkarmak isteyenler için mükemmel bir kaçamak. Altın kumsalı ve canlı sahil atmosferiyle yaz günlerinin vazgeçilmezi.",
            f"Deniz, kum ve güneş üçlüsünün en güzel hali {name}'de. {area}'nın en popüler plajlarından biri olan bu sahil, su sporları ve sahil barlarıyla tam bir Akdeniz deneyimi sunuyor.",
        ],
        'Spor': [
            f"{name}, spor tutkunları ve takım taraftarları için adeta kutsal bir mekan. Tarihi başarıları, atmosferi ve modern tesisleriyle {city_name}'nin spor mirasının en önemli parçalarından.",
            f"Tutku ve rekabetin buluştuğu {name}. {area}'daki bu ikonik tesis, canlı maç günleri ve müze turuyla sporseverler için unutulmaz anlar vaat ediyor.",
        ],
        'Aktivite': [
            f"{name}, {city_name}'de eğlence ve macera arayanlar için harika bir seçenek. {area} bölgesindeki bu mekan, hem aileler hem bireysel gezginler için keyifli saatler vaat ediyor.",
            f"Aksiyon ve eğlence dolu bir gün geçirmek isteyenler için {name} ideal. Çeşitli aktiviteleri ve enerjik atmosferiyle {area}'nın en popüler noktalarından.",
        ],
        'Meydan': [
            f"{name}, {city_name}'nin sosyal hayatının merkezi. Tarihi yapıları, çevresindeki kafeler ve canlı atmosferiyle hem yerel halkın hem turistlerin buluşma noktası.",
            f"Şehrin kalbinin attığı yer {name}. {area} bölgesindeki bu tarihi meydan, sokak sanatçıları, terası olan kafeler ve çevresindeki mimari yapılarla keşfedilmeyi bekliyor.",
        ],
    }
    
    # Get appropriate description
    if category in descriptions:
        import random
        desc_list = descriptions[category]
        return desc_list[hash(name) % len(desc_list)]
    
    # Default for unknown categories
    return f"{name}, {city_name}'nin {area} bölgesinde bulunan ve {category.lower()} kategorisindeki en dikkat çekici noktalardan biri. Eşsiz atmosferi ve sunduğu deneyimle ziyaretçilerine unutulmaz anlar vaat ediyor."

def generate_description_en(poi, city_name):
    """Generate a richer English description based on POI attributes"""
    name = poi.get('name', '')
    area = poi.get('area', '')
    category = poi.get('category', '')
    
    descriptions_en = {
        'Müze': [
            f"{name} houses one of {city_name}'s most valuable cultural treasures. Located in {area}, this venue promises a unique artistic journey with its rich collection and carefully curated exhibitions.",
            f"An essential stop for art and history enthusiasts, {name} is located in {area}. The museum offers both educational and inspiring experiences with its rare artifacts and interactive exhibits.",
        ],
        'Tarihi': [
            f"{name} is a window into {city_name}'s history with its magnificent structure bearing traces of centuries. This monument in {area} is a must-see for its architectural grandeur and cultural significance.",
            f"Stretching from the depths of history to the present, {name} is one of the most impressive structures in {area}. Its walls carrying traces of the past take visitors on a journey through time.",
        ],
        'Park': [
            f"{name} is a hidden paradise in {area} for those who want to escape the city's crowds. With its green spaces, walking trails and peaceful atmosphere, it's a perfect escape for both locals and tourists.",
            f"A perfect blend of nature and city life, {name} in {area} can be visited in any season with its picnic areas and botanical richness.",
        ],
        'Yeme-İçme': [
            f"{name} offers the most authentic flavors of {city_name}'s cuisine. This address in {area} promises an unforgettable feast with local ingredients and traditional recipes.",
            f"A favorite among foodies, {name} is one of {area}'s most beloved dining destinations. The chef's special recipes and intimate atmosphere elevate the dining experience.",
        ],
        'Mahalle': [
            f"{name} is one of {city_name}'s most characteristic neighborhoods. With its historic texture, boutique shops and street culture, it best reflects the city's soul. Don't be afraid to get lost and explore.",
            f"For those who want to feel the pulse of local life, {name} is an ideal starting point. The narrow streets, colorful facades and vibrant atmosphere of {area} await you.",
        ],
        'Manzara': [
            f"{name} offers a breathtaking panorama of {city_name}. Especially at sunset when golden light envelops the city, it's paradise for photographers and romantics.",
            f"For those who want a bird's eye view of the city skyline, {name} is a must. This spot in {area} is equally impressive with its night lights and daytime views.",
        ],
        'Kültür': [
            f"{name} is where {city_name}'s cultural heart beats. This venue in {area} reflects the city's creative spirit with art performances, exhibitions and events.",
            f"A meeting point for culture and art enthusiasts, {name} is one of {area}'s liveliest cultural centers with regular events and rich programming.",
        ],
        'Sokak': [
            f"{name} is one of {city_name}'s most iconic streets. With historic buildings, street artists and vibrant atmosphere, it offers a magical walking experience both day and night.",
            f"One of the best places to feel the city's pulse, {name}. With cafés, shops and street culture, the heart of {area} beats here.",
        ],
        'Plaj': [
            f"{name} is a perfect getaway for those who want to cool off in the Mediterranean's crystal waters and enjoy the sun. With its golden sand and lively beach atmosphere, it's essential for summer days.",
            f"The best combination of sea, sand and sun is found at {name}. One of {area}'s most popular beaches, it offers a complete Mediterranean experience with water sports and beach bars.",
        ],
        'Spor': [
            f"{name} is practically a sacred place for sports fans and team supporters. With its historic achievements, atmosphere and modern facilities, it's one of the most important parts of {city_name}'s sports heritage.",
            f"Where passion and competition meet, {name}. This iconic facility in {area} promises unforgettable moments for sports fans with exciting match days and museum tours.",
        ],
        'Aktivite': [
            f"{name} is a great choice for those seeking fun and adventure in {city_name}. This venue in {area} promises enjoyable hours for both families and solo travelers.",
            f"Ideal for those who want a day full of action and fun, {name}. With various activities and energetic atmosphere, it's one of {area}'s most popular spots.",
        ],
        'Meydan': [
            f"{name} is the center of {city_name}'s social life. With its historic buildings, surrounding cafés and lively atmosphere, it's a meeting point for both locals and tourists.",
            f"Where the city's heart beats, {name}. This historic square in {area} awaits discovery with street artists, terrace cafés and surrounding architectural structures.",
        ],
    }
    
    if category in descriptions_en:
        desc_list = descriptions_en[category]
        return desc_list[hash(name) % len(desc_list)]
    
    return f"{name} is one of the most noteworthy spots in the {category.lower()} category in {city_name}'s {area} district. With its unique atmosphere and experience, it promises unforgettable moments for visitors."

def process_city(filepath):
    """Process a single city JSON file and improve template descriptions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    city_name = data.get('city', 'Unknown')
    highlights = data.get('highlights', [])
    
    improved_count = 0
    
    for poi in highlights:
        desc = poi.get('description', '')
        desc_en = poi.get('description_en', '')
        
        # Check and improve Turkish description
        if is_template_description(desc):
            new_desc = generate_description(poi, city_name)
            poi['description'] = new_desc
            improved_count += 1
        
        # Check and improve English description
        if is_template_description_en(desc_en):
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
            print(f"⚪ {city_name}: No template descriptions found")
    
    print("=" * 50)
    print(f"Total: {total_improved} descriptions improved across all cities")

if __name__ == "__main__":
    main()

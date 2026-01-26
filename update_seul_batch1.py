#!/usr/bin/env python3
"""
Update Seul bars with researched descriptions
"""

import json
import os

SEUL_FILE = 'assets/cities/seul.json'

# Researched descriptions
UPDATES = {
    "BOUND BAR": {
        "description": "Myeongdong'un popüler barı, bira pong ve dart gibi aktivitelerle enerjik ama samimi bir atmosfer sunuyor. Honey Makgeolli ve Peach Crush kokteyliyle ünlü.",
        "description_en": "Popular bar in Myeongdong offering an energetic yet friendly atmosphere with activities like beer pong and darts. Famous for Honey Makgeolli and Peach Crush cocktail."
    },
    "Bar Cham": {
        "description": "Asia's 50 Best Bars listesinde yer alan, geleneksel Kore hanok'unda bulunan speakeasy. Soju ve makgeolli bazlı yaratıcı kokteyller, Chungju Gimbap kokteyliyle meşhur.",
        "description_en": "Award-winning speakeasy in a traditional Korean hanok, ranked in Asia's 50 Best Bars. Famous for creative cocktails using soju and makgeolli, especially the Chungju Gimbap cocktail."
    },
    "Antidote": {
        "description": "Reçete konseptli bar, her kokteyl bir malzeme adı taşıyor: Basil, Rice, Tomato gibi. Taze mevsimlik malzemelerle hazırlanan benzersiz kokteylleriyle dikkat çekiyor.",
        "description_en": "Prescription-concept bar where each cocktail is named after ingredients like Basil, Rice, Tomato. Known for unique cocktails made with fresh seasonal ingredients."
    },
    "Bar Pomme": {
        "description": "Jongno bölgesinin gizli cevheri, elma likörü bazlı yaratıcı kokteyller sunuyor. SOUR YOO ve Healing kokteyliyle ünlü, sıcak ve samimi atmosfer.",
        "description_en": "Hidden gem in Jongno district, known for creative apple liquor-based cocktails. Famous for SOUR YOO and Healing cocktails, warm and intimate atmosphere."
    },
    "Coley": {
        "description": "Bir çiftin işlettiği samimi bar, Kore'nin en iyi kokteylerinden bazılarını sunuyor. Özel yapım kokteyller, viski seçenekleri ve lezzetli pizza ile tanınıyor.",
        "description_en": "Cozy bar run by a married couple, serving some of Korea's best cocktails. Known for custom-made drinks, whisky selection, and delicious pizza."
    },
    "Cinderella Bar": {
        "description": "Seongsu-dong'un ayakkabı yapım mirasından ilham alan peri masalı konseptli speakeasy. Kokteyller 3D baskılı ayakkabı tutucularında servis ediliyor, Instagram'lık bir deneyim.",
        "description_en": "Fairy tale-themed speakeasy inspired by Seongsu-dong's shoemaking heritage. Cocktails served in 3D-printed shoe holders, offering an Instagram-worthy experience."
    },
    "AnotherLv.": {
        "description": "Seul'un yükselen kokteyl sahnesinin dinamik mekanı, yerel malzemelerle hazırlanmış yaratıcı içkiler sunuyor. Samimi atmosfer ve usta bartenderlar.",
        "description_en": "Dynamic venue of Seoul's rising cocktail scene, offering creative drinks made with local ingredients. Intimate atmosphere and skilled bartenders."
    },
    "Bar Jangsaeng": {
        "description": "Geleneksel Kore içkilerini modern miksoloji ile birleştiren bar. Soju ve makgeolli bazlı kokteylleriyle bilinir, samimi ve otantik bir ortam.",
        "description_en": "Bar blending traditional Korean drinks with modern mixology. Known for soju and makgeolli-based cocktails in an intimate and authentic setting."
    },
    "Bar Tea Scent": {
        "description": "Çay bazlı kokteyllerin uzmanı, aromatik içecekleriyle öne çıkan benzersiz bir mekan. Huzurlu bir atmosferde çay ve alkol arasındaki mükemmel dengeyi sunuyor.",
        "description_en": "Specialist in tea-based cocktails, standing out with aromatic drinks. Offers the perfect balance between tea and alcohol in a peaceful atmosphere."
    },
    "Bar ZEYA(제야)": {
        "description": "Kore gelenekleri ve modern kokteyl sanatını harmanlayan şık bir bar. Mevsimsel malzemeler ve yaratıcı sunumlarla dikkat çekiyor.",
        "description_en": "Stylish bar blending Korean traditions with modern cocktail artistry. Notable for seasonal ingredients and creative presentations."
    },
    "Birdman bar": {
        "description": "Seul'un craft kokteyl sahnesinin gözde mekanlarından biri. Samimi ortam, usta bartenderlar ve özenle hazırlanmış içecekler.",
        "description_en": "One of the favorites in Seoul's craft cocktail scene. Intimate setting, skilled bartenders, and carefully crafted drinks."
    },
    "BoomBox Beer & Music": {
        "description": "Bira ve müzik tutkunları için mükemmel buluşma noktası. Geniş craft bira seçeneği, canlı müzik atmosferi ve enerjik gece hayatı.",
        "description_en": "Perfect meeting point for beer and music lovers. Wide craft beer selection, live music atmosphere, and energetic nightlife."
    },
    "Cobbler Yeonhee 코블러 연희": {
        "description": "Yeonhee'nin sakin sokağında bulunan zarif kokteyl barı. Klasik ve modern kokteyller, samimi atmosfer ve kişiselleştirilmiş servis.",
        "description_en": "Elegant cocktail bar on Yeonhee's quiet street. Classic and modern cocktails, intimate atmosphere, and personalized service."
    },
    "Ghiwon22": {
        "description": "Seul'un en iyi speakeasy'lerinden biri, gizli girişi ve özel atmosferiyle tanınıyor. Yaratıcı kokteyller ve kusursuz servis.",
        "description_en": "One of Seoul's best speakeasies, known for its hidden entrance and special atmosphere. Creative cocktails and impeccable service."
    },
    "Gong-Gan": {
        "description": "Minimalist tasarımlı kokteyl barı, sakin bir ortamda kaliteli içecekler sunuyor. Kişiye özel hazırlanan kokteyller ve samimi servis.",
        "description_en": "Minimalist cocktail bar offering quality drinks in a calm environment. Personalized cocktails and friendly service."
    },
    "Grand Ole Opry": {
        "description": "Amerikan country müziği temalı canlı performans barı. Whiskey seçenekleri, canlı müzik ve nostaljik atmosfer.",
        "description_en": "American country music-themed live performance bar. Whiskey selections, live music, and nostalgic atmosphere."
    },
    "Haroo Music Bar": {
        "description": "Müzik ve kokteyllerin buluştuğu canlı eğlence mekanı. DJ setleri, dans pistleri ve yaratıcı içecek menüsü.",
        "description_en": "Lively entertainment venue where music meets cocktails. DJ sets, dance floors, and creative drink menu."
    },
    "Kyoto match good": {
        "description": "Japon estetiğinden ilham alan matcha temalı kokteyl barı. Matcha bazlı içecekler ve huzurlu Zen atmosferi.",
        "description_en": "Matcha-themed cocktail bar inspired by Japanese aesthetics. Matcha-based drinks and peaceful Zen atmosphere."
    },
    "Lit Lounge Itaewon 릿라운지 이태원": {
        "description": "Itaewon'un popüler lounge barı, geniş kokteyl menüsü ve rahat atmosferiyle tanınıyor. Uluslararası müşteri kitlesi ve canlı gece hayatı.",
        "description_en": "Popular lounge bar in Itaewon, known for extensive cocktail menu and relaxed atmosphere. International clientele and vibrant nightlife."
    },
    "MAHALO": {
        "description": "Hawaii temalı tropikal kokteyl barı, Tiki kültüründen ilham alan içecekler sunuyor. Egzotik meyveler, renkli sunumlar ve yaz havası.",
        "description_en": "Hawaiian-themed tropical cocktail bar serving Tiki culture-inspired drinks. Exotic fruits, colorful presentations, and summer vibes."
    }
}

def main():
    # Load city data
    with open(SEUL_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = 0
    for h in data.get('highlights', []):
        name = h.get('name', '')
        if name in UPDATES:
            h['description'] = UPDATES[name]['description']
            h['description_en'] = UPDATES[name]['description_en']
            updated += 1
            print(f"✓ Updated: {name}")
    
    # Save
    with open(SEUL_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal updated: {updated}")

if __name__ == '__main__':
    main()

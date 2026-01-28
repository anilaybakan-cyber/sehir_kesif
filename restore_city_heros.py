#!/usr/bin/env python3
"""
Restore City Hero Images
Reverts the heroImage fields in city JSON files back to their original Unsplash URLs.
"""

import json
import os
from pathlib import Path

# Original city images from AIService.dart
CITY_IMAGES = {
    'amsterdam': 'https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800',
    'atina': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg',
    'bangkok': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/grand_palace.jpg',
    'barcelona': 'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800',
    'berlin': 'https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800',
    'budapeste': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltfde92aef92ecf073/6787eae0bf32fe28813c50fe/BCC-2024-EXPLORER-BUDAPEST-LANDMARKS-HEADER-_MOBILE.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'cenevre': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/jet_deau.jpg',
    'dubai': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800',
    'dublin': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/temple_bar.jpg',
    'floransa': 'https://italien.expert/wp-content/uploads/2021/05/Florenz-Toskana-Italien0.jpg',
    'hongkong': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/victoria_peak.jpg',
    'istanbul': 'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800',
    'kopenhag': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800',
    'lizbon': 'https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800',
    'londra': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800',
    'lucerne': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/chapel_bridge_kapellbrucke.jpg',
    'lyon': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/basilica_of_notre_dame_de_fourviere.jpg',
    'madrid': 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800',
    'marakes': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/jemaa_el_fna.jpg',
    'marsilya': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt0feb4d48a3fc134c/67c5fafa304ea9666082ff3e/iStock-956215674-2-Header_Mobile.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'milano': 'https://images.unsplash.com/photo-1520440229-6469a149ac59?w=800',
    'napoli': 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=800',
    'newyork': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800',
    'nice': 'https://www.flypgs.com/blog/wp-content/uploads/2024/05/nice-sahilleri.jpeg',
    'paris': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800',
    'porto': 'https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=800',
    'prag': 'https://images.unsplash.com/photo-1541849546-216549ae216d?w=800',
    'roma': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800',
    'seul': 'https://www.agoda.com/wp-content/uploads/2019/03/Seoul-attractions-Gyeongbokgung-palace.jpg',
    'sevilla': 'https://images.unsplash.com/photo-1558370781-d6196949e317?w=800',
    'singapur': 'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800',
    'stockholm': 'https://images.unsplash.com/photo-1509356843151-3e7d96241e11?w=800',
    'tokyo': 'https://img.piri.net/mnresize/900/-/resim/imagecrop/2023/01/17/11/54/resized_d9b02-8b17feafkapak2.jpg',
    'venedik': 'https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=800',
    'viyana': 'https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800',
    'zurih': 'https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800',
    'fes': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=800',
    'safsavan': 'https://images.unsplash.com/photo-1558258695-0e4284b3975d?w=800',
    'kahire': 'https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2019-11/image-explore-ancient-egypt-merl.jpg',
    'saraybosna': 'https://images.unsplash.com/photo-1596715694269-80838637ba76?w=800',
    'mostar': 'https://images.unsplash.com/photo-1605198089408-0138977114b0?w=800',
    'strazburg': 'https://www.avruparuyasi.com.tr/uploads/tour-gallery/36c44666-5e5a-4c2d-a341-2fa8285c3fb6.webp',
    'antalya': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/antalya/kaleici.jpg',
    'edinburgh': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt9d8daa2acc7bb33c/6797dc563b4101992b03092a/iStock-1153650218-MOBILE-HEADER.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'belgrad': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/belgrad/belgrad_kalesi_kalemegdan.jpg',
    'kotor': 'https://www.etstur.com/letsgo/wp-content/uploads/2025/12/montenegro-kotorda-gezilecek-yerler-en-populer-rotalar-guncel-liste-1024x576.png',
    'tiran': 'https://images.unsplash.com/photo-1599593442654-e1b088b7538c?w=800',
    'selanik': 'https://images.unsplash.com/photo-1562608460-f97577579893?w=800',
    'kapadokya': 'https://images.unsplash.com/photo-1641128324972-af3212f0f6bd?w=800',
    'rovaniemi': 'https://www.visitfinland.com/dam/jcr:70734834-7ba2-4bf1-9f6e-bf185e014367/central-plaza-santa-claus-village-rovaniemi-lapland-finland%20(1).jpg',
    'tromso': 'https://www.flightgift.com/media/wp/FG/2024/02/tromso.webp',
    'zermatt': 'https://holidaystoswitzerland.com/wp-content/uploads/2020/07/Zermatt-and-the-Matterhorn-at-dawn.jpg',
    'matera': 'https://ita.travel/user/blogimg/ostatni/aerial-view_matera_sunset.jpg',
    'giethoorn': 'https://www.onedayinacity.com/wp-content/uploads/2021/03/Giethoorn-Village.png',
    'colmar': 'https://images.goway.com/production/hero/iStock-1423136049.jpg',
    'sintra': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt75a384a61f2efa5b/68848225e7cb649650cc2d81/BCC-2024-EXPLORER-SINTRA-BEST_PLACES_TO_VISIT-HEADER-MOBILE.jpg?format=webp&auto=avif&quality=60&crop=16%3A9&width=1440',
    'sansebastian': 'https://cdn.bunniktours.com.au/public/posts/images/Europe/Blog%20Header%20-%20Spain%20-%20San%20Sebastian%20-%20credit%20Raul%20Cacho%20Oses%20%28Unsplash%29-feature.jpg',
    'bologna': 'https://www.datocms-assets.com/57243/1661342703-6245af628d40974c9ab5a7fd_petr-slovacek-sxk8bwkvoxe-unsplash-20-1.jpg?auto=compress%2Cformat',
    'gaziantep': 'https://www.brandlifemag.com/wp-content/uploads/2021/04/acilis-gaziantep-december-06gaziantep-coppersmith-bazaar-600w-549044518.jpg',
    'brugge': 'https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2021-08/brugge-hakkinda-bilinmesi-gerekenler.jpg',
    'santorini': 'https://www.kucukoteller.com.tr/storage/images/2024/07/14/5e7eaf11eb5ec2dda2f7a602232faa8961347f29.webp',
    'heidelberg': 'https://image.hurimg.com/i/hurriyet/90/1110x740/56b3325818c7730e3cdb6757.jpg',
    'bruksel': 'https://images.unsplash.com/photo-1559113513-d5e09c18b9e8?w=800',
    'oslo': 'https://www.journavel.com/wp-content/uploads/2024/10/IMG_1851-scaled.webp',
    'hallstatt': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hallstatt/hallstatt-postcard-viewpoint.jpg',
}

CITIES_DIR = Path("assets/cities")

def normalize_key(key):
    return key.lower().strip().replace('ü', 'u').replace('ş', 's').replace('ç', 'c').replace('ö', 'o').replace('ğ', 'g').replace('ı', 'i').replace(' ', '')

def main():
    print("🔄 Restoring original city hero images...")
    
    restored = 0
    
    # Normalize mapping keys for easier lookup
    normalized_mapping = {normalize_key(k): v for k, v in CITY_IMAGES.items()}
    
    for json_file in CITIES_DIR.glob("*.json"):
        city_id = json_file.stem
        norm_city_id = normalize_key(city_id)
        
        if norm_city_id in normalized_mapping:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            old_hero = data.get('heroImage')
            target_hero = normalized_mapping[norm_city_id]
            
            if old_hero != target_hero:
                data['heroImage'] = target_hero
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"   ✅ Restored hero for: {city_id}")
                restored += 1
        else:
            print(f"   ⚠️ No original hero found for: {city_id}")
            
    print(f"\n🎉 Done! Restored {restored} hero images.")

if __name__ == "__main__":
    main()

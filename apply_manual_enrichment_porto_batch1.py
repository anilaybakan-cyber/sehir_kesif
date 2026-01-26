import json

# Manual enrichment data (Porto Batch 1: 52 items - ALL)
updates = {
    "Livraria Lello": {
        "description": "Dünyanın en güzel kitapçılarından biri, neo-gotik cephesi ve kırmızı merdivenlerle. Harry Potter ilham kaynağı, 1906'dan beri hizmet veriyor.",
        "description_en": "One of world's most beautiful bookstores with neo-Gothic facade and red staircase. Harry Potter inspiration, serving since 1906."
    },
    "Dom Luis I Bridge": {
        "description": "Porto ve Vila Nova de Gaia'yı birleştiren ikonik çelik köprü, Gustave Eiffel'in öğrencisi tarafından tasarlanmış. Üst ve alt kat yürüyüşü.",
        "description_en": "Iconic steel bridge connecting Porto and Vila Nova de Gaia, designed by student of Gustave Eiffel. Upper and lower deck walks."
    },
    "Sao Bento Station": {
        "description": "20.000 mavi-beyaz azulejo çinili duvarlarıyla dünyanın en güzel tren istasyonlarından biri. Portekiz tarihi sahneleri ve mimari zarafet.",
        "description_en": "One of world's most beautiful train stations with 20,000 blue-white azulejo tiles. Portuguese historical scenes and architectural elegance."
    },
    "Ribeira District": {
        "description": "UNESCO korumasındaki tarihi nehir kenarı mahallesi, renkli binalar ve canlı atmosfer. Restoranlar, kafeler ve Douro manzarası.",
        "description_en": "UNESCO-protected historic riverside district with colorful buildings and lively atmosphere. Restaurants, cafes, and Douro views."
    },
    "Clerigos Tower": {
        "description": "Porto'nun simgesi 76 metre yüksekliğindeki barok çan kulesi. 225 basamak sonunda 360 derece şehir panoraması.",
        "description_en": "Porto's symbol 76-meter high Baroque bell tower. 360-degree city panorama after 225 steps."
    },
    "Porto Cathedral": {
        "description": "12. yüzyıldan kalma romanesk katedral, azulejos kaplı iç avlu ve gotik detaylar. Şehrin en eski ve görkemli dini yapısı.",
        "description_en": "12th-century Romanesque cathedral with azulejos-covered inner courtyard and Gothic details. City's oldest and most magnificent religious building."
    },
    "Palacio da Bolsa": {
        "description": "19. yüzyıldan kalma neo-klasik borsa sarayı, Arap Salonu ve süslemeli iç mekanlar. Porto ticaret tarihinin muhteşem örneği.",
        "description_en": "19th-century neo-classical stock exchange palace with Arabian Hall and ornate interiors. Magnificent example of Porto's trading history."
    },
    "Bolhao Market": {
        "description": "1914'ten beri hizmet veren tarihi pazar, taze ürünler ve yerel lezzetler. Restorasyondan sonra yeniden açılmış, Porto'nun gastronomi kalbi.",
        "description_en": "Historic market serving since 1914 with fresh produce and local flavors. Reopened after restoration, Porto's gastronomic heart."
    },
    "Casa da Musica": {
        "description": "Rem Koolhaas tasarımı modern konser salonu, çağdaş mimarinin ikonik yapısı. Klasik müzik, caz ve dünya müziği konserleri.",
        "description_en": "Rem Koolhaas-designed modern concert hall, iconic structure of contemporary architecture. Classical music, jazz, and world music concerts."
    },
    "Serralves Museum": {
        "description": "Çağdaş sanat müzesi, art deco villa ve geniş park kompleksi. Uluslararası sergiler, bahçe yürüyüşü ve kültürel etkinlikler.",
        "description_en": "Contemporary art museum, art deco villa, and large park complex. International exhibitions, garden walks, and cultural events."
    },
    "Crystal Palace Gardens": {
        "description": "19. yüzyıldan kalma botanik bahçeleri, Douro nehri manzarası ve tavus kuşları. Romantik yürüyüş, piknik ve açık hava etkinlikleri.",
        "description_en": "19th-century botanical gardens with Douro river views and peacocks. Romantic walks, picnics, and outdoor events."
    },
    "Majestic Cafe": {
        "description": "1921'den beri hizmet veren Belle Époque tarzı ikonik kafe. J.K. Rowling'in yazdığı efsanevi mekan, taze pastalar ve kahve.",
        "description_en": "Iconic Belle Époque style cafe serving since 1921. Legendary venue where J.K. Rowling wrote, fresh pastries, and coffee."
    },
    "Capela das Almas": {
        "description": "15.947 mavi-beyaz azulejo çinisiyle kaplı 18. yüzyıl şapeli. Aziz Katarina ve Aziz Francis'in yaşamını anlatan duvarlar.",
        "description_en": "18th-century chapel covered with 15,947 blue-white azulejo tiles. Walls depicting lives of Saint Catherine and Saint Francis."
    },
    "Igreja do Carmo": {
        "description": "Portekiz'in en etkileyici azulejo cepheli kiliselerinden biri. Karmelite rahiplerin tarihi, rokoko iç mekan ve dış mozaikler.",
        "description_en": "One of Portugal's most impressive azulejo-facade churches. Carmelite friars' history, Rococo interior, and exterior mosaics."
    },
    "Foz do Douro": {
        "description": "Douro Nehri'nin Atlantik'le buluştuğu şık sahil mahallesi. Deniz esintisi, plajlar, restoranlar ve gün batımı yürüyüşleri.",
        "description_en": "Elegant seaside neighborhood where Douro River meets Atlantic. Sea breeze, beaches, restaurants, and sunset walks."
    },
    "Matosinhos Beach": {
        "description": "Porto'nun en popüler plajı, sörfçüler ve deniz ürünleri restoranlarıyla ünlü. Taze ızgara balık, yaz eğlencesi ve okyanus.",
        "description_en": "Porto's most popular beach famous for surfers and seafood restaurants. Fresh grilled fish, summer fun, and ocean."
    },
    "Graham's Port Lodge": {
        "description": "1820'den beri Porto şarabı üreten tarihi mahzen, tadım turları ve nehir manzarası. Premium vintage Porto şarapları.",
        "description_en": "Historic cellar producing Port wine since 1820 with tasting tours and river views. Premium vintage Port wines."
    },
    "Taylors Port": {
        "description": "1692'den beri Porto şarabı üreten köklü İngiliz evi. Mahzen turları, tadım bahçesi ve şarap mirası.",
        "description_en": "Established English house producing Port wine since 1692. Cellar tours, tasting garden, and wine heritage."
    },
    "Sandeman": {
        "description": "İkonik siyah pelerinli logo ile tanınan Porto şarabı evi. Üç yüzyıllık gelenek, mahzenler ve interaktif turlar.",
        "description_en": "Port wine house known for iconic black-caped logo. Three centuries of tradition, cellars, and interactive tours."
    },
    "WOW World of Wine": {
        "description": "Gaia'daki şarap ve kültür kompleksi, müzeler, restoranlar ve panoramik terraslar. Porto şarabı deneyimi için tek adres.",
        "description_en": "Wine and culture complex in Gaia with museums, restaurants, and panoramic terraces. One address for Port wine experience."
    },
    "Teleferico de Gaia": {
        "description": "Vila Nova de Gaia'yı Douro kıyısından yukarı bağlayan teleferik. Nehir manzarası, fotoğrafçılık ve pratik ulaşım.",
        "description_en": "Cable car connecting Vila Nova de Gaia from Douro shore to upper level. River views, photography, and practical transport."
    },
    "Jardim do Morro": {
        "description": "Gaia'da Dom Luis köprüsü başındaki park, Porto skyline manzarası. Gün batımı izleme, piknik ve fotoğrafçılık.",
        "description_en": "Park at Dom Luis bridge start in Gaia with Porto skyline views. Sunset watching, picnic, and photography."
    },
    "Maus Habitos": {
        "description": "Alternatif kültür merkezi, bar, galeri ve canlı müzik sahnesı. Underground Porto, sanat ve gece hayatı.",
        "description_en": "Alternative culture center with bar, gallery, and live music stage. Underground Porto, art, and nightlife."
    },
    "Cafe Santiago": {
        "description": "Efsanevi Francesinha'nın en iyi adreslerinden biri. Porto'nun ikonik sandviçi, bira ve yerel deneyim.",
        "description_en": "One of best addresses for legendary Francesinha. Porto's iconic sandwich, beer, and local experience."
    },
    "Brasao Cervejaria": {
        "description": "Geleneksel Portekiz yemekleri ve Francesinha sunan popüler birahane. Soğuk bira, deniz ürünleri ve yerel atmosfer.",
        "description_en": "Popular beer hall serving traditional Portuguese food and Francesinha. Cold beer, seafood, and local atmosphere."
    },
    "Gazela": {
        "description": "Porto'nun ünlü hot dog (cachorro) ve bifanasının adresi. Yerel fast-food, otantik lezzet ve hızlı mola.",
        "description_en": "Address of Porto's famous hot dog (cachorro) and bifana. Local fast-food, authentic flavor, and quick break."
    },
    "Pedro dos Frangos": {
        "description": "Piri-piri soslu kızarmış tavuğun en iyi adresi. Portekiz tavuğu, uygun fiyat ve doyurucu öğle yemeği.",
        "description_en": "Best address for roasted chicken with piri-piri sauce. Portuguese chicken, affordable, and satisfying lunch."
    },
    "Taberna dos Mercadores": {
        "description": "Ribeira'da geleneksel Porto mutfağı sunan küçük taverna. Balık güveç, petiscos ve samimi ortam.",
        "description_en": "Small tavern serving traditional Porto cuisine in Ribeira. Fish stew, petiscos, and intimate setting."
    },
    "Cantina 32": {
        "description": "Endüstriyel dekoryasyonlu modern Portekiz restoranı. Yaratıcı menü, paylaşımlı tabaklar ve şık atmosfer.",
        "description_en": "Modern Portuguese restaurant with industrial decor. Creative menu, sharing plates, and stylish atmosphere."
    },
    "Zenith": {
        "description": "Vejetaryen ve vegan seçenekler sunan sağlıklı kafe. Organik kahvaltı, smoothie ve hafif öğle yemeği.",
        "description_en": "Healthy cafe serving vegetarian and vegan options. Organic breakfast, smoothies, and light lunch."
    },
    "Fabrica Coffee Roasters": {
        "description": "Porto'nun specialty coffee sahnesinin öncülerinden. El kavruması kahve, latte art ve kahve kültürü.",
        "description_en": "One of pioneers of Porto's specialty coffee scene. Hand-roasted coffee, latte art, and coffee culture."
    },
    "7g Roaster": {
        "description": "Third wave kahve hareketi ile ünlü butik kahve dükkanı. Single origin, pour-over ve kahve eğitimi.",
        "description_en": "Boutique coffee shop famous for third wave coffee movement. Single origin, pour-over, and coffee education."
    },
    "Manteigaria": {
        "description": "Taze çıkan pastel de nata'nın en iyi adreslerinden biri. Portekiz tatlısı, tarçın ve kahve eşliği.",
        "description_en": "One of best addresses for freshly baked pastel de nata. Portuguese pastry, cinnamon, and coffee pairing."
    },
    "A Perola do Bolhao": {
        "description": "1917'den beri hizmet veren art nouveau delicatessen. Jambon, peynir ve Portekiz gurme ürünleri.",
        "description_en": "Art nouveau delicatessen serving since 1917. Ham, cheese, and Portuguese gourmet products."
    },
    "Armazem": {
        "description": "Tarihi depoda kurulan çok katlı vintage mağaza. Antika, retro moda ve Porto tasarımı.",
        "description_en": "Multi-story vintage shop in historic warehouse. Antiques, retro fashion, and Porto design."
    },
    "Soares dos Reis Museum": {
        "description": "Portekiz'in en eski sanat müzesi, 19. yüzyıl Portekiz resim ve heykelden koleksiyon. Ulusal romantizm ve modern sanat.",
        "description_en": "Portugal's oldest art museum with collection of 19th-century Portuguese painting and sculpture. National romanticism and modern art."
    },
    "Portuguese Centre of Photography": {
        "description": "Tarihi hapishane binasında fotoğrafçılık müzesi ve sergi mekanı. Dönemsel sergiler, arşiv ve görsel sanat.",
        "description_en": "Photography museum and exhibition venue in historic prison building. Periodic exhibitions, archive, and visual art."
    },
    "Virtudes Garden": {
        "description": "Şehrin gizli bahçesi, teraslı parkta nehir manzarası ve huzur. Gün batımı, okuma ve romantik mola.",
        "description_en": "City's hidden garden with river views and peace in terraced park. Sunset, reading, and romantic break."
    },
    "Parque da Cidade": {
        "description": "Avrupa'nın en büyük kentsel parkı, okyanus kıyısına kadar uzanan yeşil alan. Bisiklet, koşu ve aile pikniği.",
        "description_en": "Europe's largest urban park, green area extending to ocean shore. Cycling, running, and family picnics."
    },
    "Base Porto": {
        "description": "Sokak yemekleri, craft bira ve açık hava atmosferi sunan food court. Farklı mutfaklar, sosyal mekan ve gece eğlencesi.",
        "description_en": "Food court serving street food, craft beer, and outdoor atmosphere. Different cuisines, social venue, and night entertainment."
    },
    "Bonaparte Downtown": {
        "description": "Porto'nun popüler gece kulübü, DJ geceleri ve dans. Elektronik müzik, kokteyller ve gece hayatı.",
        "description_en": "Porto's popular nightclub with DJ nights and dancing. Electronic music, cocktails, and nightlife."
    },
    "Capela Incomum": {
        "description": "Eski şapelde kurulan benzersiz şarap barı ve restoran. Gotik atmosfer, Porto şarapları ve romantik yemekler.",
        "description_en": "Unique wine bar and restaurant in old chapel. Gothic atmosphere, Port wines, and romantic dining."
    },
    "Letraria": {
        "description": "Craft bira ve Portekiz biracılık kültürüne adanmış bar. Yerel üreticiler, tadım uçuşları ve sosyal ortam.",
        "description_en": "Bar dedicated to craft beer and Portuguese brewing culture. Local producers, tasting flights, and social setting."
    },
    "O Buraco": {
        "description": "Yerel halkın favori bara, canlı fado geceleri ve Portekiz şarapları. Samimi atmosfer, müzik ve kültür.",
        "description_en": "Locals' favorite bar with live fado nights and Portuguese wines. Intimate atmosphere, music, and culture."
    },
    "Conga": {
        "description": "1976'dan beri bifana sandviçi sunan efsane lokanta. Porto'nun en ünlü bifanası, bira ve nostalji.",
        "description_en": "Legendary restaurant serving bifana sandwich since 1976. Porto's most famous bifana, beer, and nostalgia."
    },
    "Euskalduna Studio": {
        "description": "Yaratıcı Bask-Portekiz fusion mutfağı sunan yenilikçi restoran. Fine-dining, tadım menüleri ve gastronomi sanatı.",
        "description_en": "Innovative restaurant serving creative Basque-Portuguese fusion cuisine. Fine-dining, tasting menus, and gastronomy art."
    },
    "Flow": {
        "description": "Nehir manzaralı kokteyl barı ve lounge, DJ setleri ve gece eğlencesi. Douro kenarı, sofistike atmosfer ve içecekler.",
        "description_en": "Cocktail bar and lounge with river views, DJ sets, and night entertainment. Douro side, sophisticated atmosphere, and drinks."
    },
    "Mistica": {
        "description": "Alternatif bar ve kültür mekanı, canlı müzik ve sanat etkinlikleri. Underground Porto, yaratıcı sahne ve sosyal hayat.",
        "description_en": "Alternative bar and culture venue with live music and art events. Underground Porto, creative scene, and social life."
    },
    "Cervejaria Gazela": {
        "description": "Porto'nun ikonik cachorro (hot dog) papatya tabir lokanta. 1962'den beri, bira ve nostaljik atmosfer.",
        "description_en": "Porto's iconic cachorro (hot dog) legendary restaurant. Since 1962, beer, and nostalgic atmosphere."
    },
    "World of Discoveries": {
        "description": "Portekiz keşiflerini ve denizcilik tarihini anlatan interaktif müze. Aileler için eğitici, haritalar ve macera.",
        "description_en": "Interactive museum telling Portuguese discoveries and maritime history. Educational for families, maps, and adventure."
    },
    "Lada Lift": {
        "description": "Douro nehri kıyısından yukarı şehre bağlayan tarihi asansör. Ribeira erişimi, manzara ve pratik ulaşım.",
        "description_en": "Historic elevator connecting Douro riverside to upper city. Ribeira access, views, and practical transport."
    },
    "Sigilo Craft Beer Bar Wine & Garden": {
        "description": "Gizli bahçede craft bira ve şarap barı, rahat ortam ve sosyal atmosfer. Yerel üreticiler, açık hava ve arkadaşlar.",
        "description_en": "Craft beer and wine bar in hidden garden with relaxed setting and social atmosphere. Local producers, outdoors, and friends."
    }
}

filepath = 'assets/cities/porto.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Porto Batch 1 - COMPLETE).")

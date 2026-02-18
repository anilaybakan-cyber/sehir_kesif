import json

# Manual enrichment data (Dublin - ALL 50 items)
updates = {
    "Kilmainham Gaol": {
        "description": "İrlanda bağımsızlık tarihinin kalbi, 1916 Paskalya Ayaklanması liderlerin idam edildiği tarihi hapishane. Rehberli turlar ve duygusal deneyim.",
        "description_en": "Heart of Irish independence history, historic prison where 1916 Easter Rising leaders were executed. Guided tours and emotional experience."
    },
    "Phoenix Park": {
        "description": "Avrupa'nın en büyük şehir parklarından biri, serbest gezen geyikler ve Dublin Hayvanat Bahçesi. 707 hektar yeşil alan, bisiklet ve piknik.",
        "description_en": "One of Europe's largest urban parks with free-roaming deer and Dublin Zoo. 707 hectares of green space, cycling, and picnics."
    },
    "Jameson Distillery": {
        "description": "İkonik İrlanda viskisinin hikayesini anlatan interaktif müze, tadım turları. 200 yıllık gelenek, kokteyl atölyeleri ve hediye mağazası.",
        "description_en": "Interactive museum telling story of iconic Irish whiskey with tasting tours. 200 years of tradition, cocktail workshops, and gift shop."
    },
    "Teeling Whiskey Distillery": {
        "description": "Dublin şehrindeki ilk yeni viski fabrikası, 125 yıl sonra. Craft viski, tadım turları ve liberal servis.",
        "description_en": "First new whiskey distillery in Dublin city in 125 years. Craft whiskey, tasting tours, and liberal serving."
    },
    "EPIC The Irish Emigration Museum": {
        "description": "İrlanda diasporasının hikayesini anlatan interaktif müze. 10 milyon göçmenin hikayesi, aile araştırması ve duygusal yolculuk.",
        "description_en": "Interactive museum telling story of Irish diaspora. Stories of 10 million emigrants, family research, and emotional journey."
    },
    "National Botanic Gardens": {
        "description": "1795'ten beri hizmet veren botanik bahçeleri, Viktorya dönemi seraları. 20.000 bitki türü, ücretsiz giriş ve huzurlu kaçış.",
        "description_en": "Botanical gardens serving since 1795 with Victorian-era glasshouses. 20,000 plant species, free entry, and peaceful escape."
    },
    "Glasnevin Cemetery": {
        "description": "İrlanda'nın en önemli tarihi mezarlığı, ünlü kişilerin anıtları. 1,5 milyon mezar, rehberli turlar ve ulusal tarih.",
        "description_en": "Ireland's most important historic cemetery with monuments of famous people. 1.5 million graves, guided tours, and national history."
    },
    "Little Museum of Dublin": {
        "description": "Dublin'in 20. yüzyıl tarihini anlatan küçük ama etkili müze. U2, JFK ve topluluk hikayeleri.",
        "description_en": "Small but impactful museum telling Dublin's 20th-century history. U2, JFK, and community stories."
    },
    "Chester Beatty": {
        "description": "Orta Doğu, Asya ve Avrupa'dan nadir el yazmaları ve sanat koleksiyonu. Ücretsiz giriş, müze ödülleri ve kültürel hazine.",
        "description_en": "Rare manuscripts and art collection from Middle East, Asia, and Europe. Free entry, museum awards, and cultural treasure."
    },
    "St Stephen's Green": {
        "description": "Şehir merkezinde Viktorya dönemi parkı, heykeller ve göletler. Öğle yemeği molası, piknik ve yeşil vaha.",
        "description_en": "Victorian-era park in city center with sculptures and ponds. Lunch break, picnic, and green oasis."
    },
    "Merrion Square": {
        "description": "Oscar Wilde heykeliyle ünlü Gürcü dönemi meydanı, renkli kapılar. Hafta sonu sanat pazarı, parklar ve mimari.",
        "description_en": "Georgian-era square famous for Oscar Wilde statue with colorful doors. Weekend art market, parks, and architecture."
    },
    "National Gallery of Ireland": {
        "description": "Caravaggio ve Vermeer dahil Avrupa ustalarının eserleri. Ücretsiz giriş, 800 yıllık sanat ve özel sergiler.",
        "description_en": "Works of European masters including Caravaggio and Vermeer. Free entry, 800 years of art, and special exhibitions."
    },
    "Science Gallery Dublin": {
        "description": "Trinity College'daki sanat ve bilim kesişim noktası müzesi. Genç hedef kitle, interaktif sergiler ve düşünceli provokasyon.",
        "description_en": "Art and science intersection museum at Trinity College. Young audience, interactive exhibitions, and thought-provoking content."
    },
    "Hugh Lane Gallery": {
        "description": "Francis Bacon'ın stüdyosu ve empresyonist koleksiyon. Ücretsiz giriş, İrlanda modern sanatı ve kültürel merkez.",
        "description_en": "Francis Bacon's studio and Impressionist collection. Free entry, Irish modern art, and cultural center."
    },
    "GPO Witness History": {
        "description": "1916 Paskalya Ayaklanması'nın başladığı Genel Postane müzesi. İrlanda bağımsızlık hikayesi, interaktif sergiler.",
        "description_en": "General Post Office museum where 1916 Easter Rising began. Irish independence story, interactive exhibitions."
    },
    "The Brazen Head": {
        "description": "İrlanda'nın en eski pub'ı, 1198'den beri hizmet veriyor. Canlı müzik, traditional Irish session ve tarih.",
        "description_en": "Ireland's oldest pub, serving since 1198. Live music, traditional Irish session, and history."
    },
    "The Cobblestone": {
        "description": "Otantik İrlanda müzik pub'ı, tradisyonel session'ların kalbi. Yerel müzisyenler, Smithfield'de gerçek İrlanda deneyimi.",
        "description_en": "Authentic Irish music pub, heart of traditional sessions. Local musicians, real Irish experience in Smithfield."
    },
    "O'Donoghue's": {
        "description": "The Dubliners grubunun doğduğu efsanevi pub, canlı folk müzik. Merrion Row'da, Irish session ve nostalji.",
        "description_en": "Legendary pub where The Dubliners were born with live folk music. On Merrion Row, Irish session, and nostalgia."
    },
    "Grogan's": {
        "description": "Sanatçı ve yazarların favori pub'ı, duvarlarda sanat eserleri. Toasted sandwich, pint ve Dublin bohemliği.",
        "description_en": "Favorite pub of artists and writers with art on walls. Toasted sandwich, pint, and Dublin bohemianism."
    },
    "Kehoe's": {
        "description": "Viktorya dönemi dekorasyonlu geleneksel pub, orijinal mahogany bar. Grafton Street yakını, pint ve atmosfer.",
        "description_en": "Traditional pub with Victorian-era decor and original mahogany bar. Near Grafton Street, pint, and atmosphere."
    },
    "The Long Hall": {
        "description": "1871'den kalma muhteşem Viktorya barı, aynalar ve antik dekor. Dublin'in en güzel pub'ı, Guinness ve whiskey.",
        "description_en": "Magnificent Victorian bar from 1871 with mirrors and antique decor. Dublin's most beautiful pub, Guinness, and whiskey."
    },
    "Porterhouse Temple Bar": {
        "description": "İrlanda'nın ilk craft bira pub'ı, 10+ ev yapımı bira. Temple Bar'da alternatif, canlı müzik ve tadım.",
        "description_en": "Ireland's first craft beer pub with 10+ house-brewed beers. Alternative in Temple Bar, live music, and tasting."
    },
    "Gallagher's Boxty House": {
        "description": "Geleneksel İrlanda patates yemeği boxty sunan restoran. Temple Bar'da, Irish stew ve ulusal mutfak.",
        "description_en": "Restaurant serving traditional Irish potato dish boxty. In Temple Bar, Irish stew, and national cuisine."
    },
    "Queen of Tarts": {
        "description": "El yapımı tartlar ve pastalarla ünlü butik kafe. Brunch, kahve ve Dublin'in tatlı durağı.",
        "description_en": "Boutique cafe famous for handmade tarts and pastries. Brunch, coffee, and Dublin's sweet stop."
    },
    "Brother Hubbard": {
        "description": "Orta Doğu esintili brunch ve kahve mekanı. Shakshuka, falafel ve Dublin'in en iyi brunch'ı.",
        "description_en": "Middle East-inspired brunch and coffee venue. Shakshuka, falafel, and Dublin's best brunch."
    },
    "Bewley's Grafton Street": {
        "description": "1927'den beri hizmet veren ikonik kafe, vitray pencereler ve Harry Clarke sanatı. Afternoon tea ve Dublin geleneği.",
        "description_en": "Iconic cafe serving since 1927 with stained glass windows and Harry Clarke art. Afternoon tea and Dublin tradition."
    },
    "Murphy's Ice Cream": {
        "description": "İrlanda süt ve yaratıcı tatlarla el yapımı dondurma. Irish coffee, Dingle gin ve yerel lezzetler.",
        "description_en": "Handmade ice cream with Irish milk and creative flavors. Irish coffee, Dingle gin, and local flavors."
    },
    "Bunsen": {
        "description": "Dublin'in en iyi burgeri, sade ve kaliteli malzemeler. Küçük menü, büyük lezzet ve yerel favorisi.",
        "description_en": "Dublin's best burger with simple, quality ingredients. Small menu, big flavor, and local favorite."
    },
    "777": {
        "description": "Meksika sokak yemekleri ve margaritalar, canlı atmosfer. Taco, tequila ve George's Street'te Latin enerjisi.",
        "description_en": "Mexican street food and margaritas with lively atmosphere. Tacos, tequila, and Latin energy on George's Street."
    },
    "The Winding Stair": {
        "description": "Eski kitapçıda nehir manzaralı restoran, modern İrlanda mutfağı. Yerel malzemeler, romantik yemek ve köprü görünümü.",
        "description_en": "Restaurant in old bookshop with river views serving modern Irish cuisine. Local ingredients, romantic dining, and bridge view."
    },
    "Chapter One": {
        "description": "Michelin yıldızlı fine-dining, çağdaş İrlanda mutfağı. Dublin'in en prestijli restoranlarından, tadım menüleri.",
        "description_en": "Michelin-starred fine-dining with contemporary Irish cuisine. One of Dublin's most prestigious restaurants, tasting menus."
    },
    "L. Mulligan Grocer": {
        "description": "Gastropub konseptiyle craft bira ve İrlanda yemekleri. Stoneybatter'da, peynir tabağı ve yerel üreticiler.",
        "description_en": "Gastropub concept with craft beer and Irish dishes. In Stoneybatter, cheese board, and local producers."
    },
    "Marsh's Library": {
        "description": "İrlanda'nın ilk halka açık kütüphanesi, 1701. Zincirli kitaplar, nadir koleksiyon ve tarihi atmosfer.",
        "description_en": "Ireland's first public library, 1701. Chained books, rare collection, and historic atmosphere."
    },
    "Dublin Zoo": {
        "description": "Phoenix Park'taki tarihi hayvanat bahçesi, 1831'den beri. Afrika düzlükleri, Asya ormanları ve koruma çalışmaları.",
        "description_en": "Historic zoo in Phoenix Park since 1831. African plains, Asian forests, and conservation work."
    },
    "Croke Park Stadium Tour": {
        "description": "GAA'nın efsanevi stadı, Gaelic futbolu ve hurling tarihi. Skyline turu, müze ve İrlanda spor kültürü.",
        "description_en": "GAA's legendary stadium, Gaelic football and hurling history. Skyline tour, museum, and Irish sports culture."
    },
    "Aviva Stadium": {
        "description": "Irlanda milli takımının evi, rugby ve futbol maçları. Modern mimari, konserler ve spor atmosferi.",
        "description_en": "Home of Irish national team for rugby and football matches. Modern architecture, concerts, and sports atmosphere."
    },
    "IMMA": {
        "description": "Kilmainham'daki İrlanda Modern Sanat Müzesi, çağdaş sergiler. Tarihi hastane binası, bahçeler ve ücretsiz giriş.",
        "description_en": "Irish Museum of Modern Art in Kilmainham with contemporary exhibitions. Historic hospital building, gardens, and free entry."
    },
    "Whelan's": {
        "description": "Dublin'in efsanevi canlı müzik mekanı, yeni yetenekler ve ünlü sanatçılar. İrlanda rock sahnesinin kalbi.",
        "description_en": "Dublin's legendary live music venue for new talents and famous artists. Heart of Irish rock scene."
    },
    "Vicar Street": {
        "description": "Konser ve komedi mekanı, samimi atmosferle ünlü isimler. Dublin gece hayatı ve canlı performanslar.",
        "description_en": "Concert and comedy venue with famous names in intimate atmosphere. Dublin nightlife and live performances."
    },
    "Iveagh Gardens": {
        "description": "Dublin'in gizli bahçesi, St Stephen's Green'in arkasında sakin vaha. Şelaleler, labirent ve romantik.",
        "description_en": "Dublin's secret garden, quiet oasis behind St Stephen's Green. Waterfalls, labyrinth, and romantic."
    },
    "Christ Church Cathedral": {
        "description": "Dublin'in en eski katedrali, 1030'dan beri. Viking temelleri, yeraltı kripta ve gotik mimari.",
        "description_en": "Dublin's oldest cathedral since 1030. Viking foundations, underground crypt, and Gothic architecture."
    },
    "Dublinia": {
        "description": "Viking ve ortaçağ Dublin'ini anlatan interaktif müze. Christ Church'e bağlı, aileler için eğlenceli tarih.",
        "description_en": "Interactive museum telling Viking and medieval Dublin. Connected to Christ Church, fun history for families."
    },
    "Ha'penny Bridge": {
        "description": "Dublin'in ikonik 1816 yaya köprüsü, Liffey Nehri üzerinde. Fotoğraf noktası, şehir simgesi ve romantik yürüyüş.",
        "description_en": "Dublin's iconic 1816 pedestrian bridge over River Liffey. Photo point, city symbol, and romantic walk."
    },
    "Samuel Beckett Bridge": {
        "description": "Santiago Calatrava tasarımı harp şekilli modern köprü. Dublin'in yeni simgesi, gece aydınlatması ve mimari.",
        "description_en": "Santiago Calatrava-designed harp-shaped modern bridge. Dublin's new symbol, night lighting, and architecture."
    },
    "Poolbeg Lighthouse": {
        "description": "Dublin Körfezi'ndeki kırmızı deniz feneri, 5 km yürüyüş. Gün batımı, deniz havası ve şehir kaçışı.",
        "description_en": "Red lighthouse in Dublin Bay with 5 km walk. Sunset, sea air, and city escape."
    },
    "Howth Cliff Walk": {
        "description": "Dublin'in kuzeyinde sahil uçurum yürüyüşü, deniz manzarası. Balıkçı köyü, deniz ürünleri ve doğa.",
        "description_en": "Coastal cliff walk north of Dublin with sea views. Fishing village, seafood, and nature."
    },
    "Leo Burdock": {
        "description": "Dublin'in en ünlü fish and chips dükkanı, 1913'ten beri. Christ Church yakını, geleneksel lezzet.",
        "description_en": "Dublin's most famous fish and chips shop since 1913. Near Christ Church, traditional flavor."
    },
    "Beshoff Bros": {
        "description": "100 yılı aşkın fish and chips geleneği, deniz ürünleri. Howth'da taze balık, yerel favorisi.",
        "description_en": "Over 100 years of fish and chips tradition with seafood. Fresh fish in Howth, local favorite."
    },
    "Token": {
        "description": "Retro arcade oyunları ve craft bira barı. Nostalji, pizza ve Dublin'in geek cenneti.",
        "description_en": "Retro arcade games and craft beer bar. Nostalgia, pizza, and Dublin's geek paradise."
    },
    "The Virgin Mary": {
        "description": "Alkolsüz kokteyl barı, düşünceli içecekler ve sosyal ortam. Dublin'in sober curious hareketi.",
        "description_en": "Non-alcoholic cocktail bar with thoughtful drinks and social setting. Dublin's sober curious movement."
    }
}

filepath = 'assets/cities/dublin.json'
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

print(f"\n✅ Manually enriched {count} items (Dublin - COMPLETE).")

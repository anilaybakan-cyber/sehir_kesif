import json

# Manual enrichment data (New York - ALL 51 items)
updates = {
    "The Metropolitan Museum of Art": {
        "description": "Dünyada en büyük sanat müzelerinden biri, 5.000 yıllık sanat tarihini barındırıyor. Mısır tapınağı, Avrupa ustaları ve Central Park manzarası.",
        "description_en": "One of world's largest art museums housing 5,000 years of art history. Egyptian temple, European masters, and Central Park views."
    },
    "MoMA": {
        "description": "Modern sanatın mabedi, Van Gogh'un Yıldızlı Gecesi'nden Picasso'ya efsanevi koleksiyon. 20. yüzyıl sanatının en kapsamlı arşivi.",
        "description_en": "Temple of modern art, legendary collection from Van Gogh's Starry Night to Picasso. Most comprehensive archive of 20th-century art."
    },
    "Solomon R. Guggenheim Museum": {
        "description": "Frank Lloyd Wright'ın spiral tasarımı, hem bina hem koleksiyon başyapıt. Modern ve çağdaş sanat, ikonik mimari.",
        "description_en": "Frank Lloyd Wright's spiral design, masterpiece in both building and collection. Modern and contemporary art, iconic architecture."
    },
    "American Museum of Natural History": {
        "description": "Dünyanın en büyük doğa tarihi müzelerinden biri, dinozor fosilleri ve uzay bölümüyle. Aileler için eğitici, Gece Müzede filmi çekimi.",
        "description_en": "One of world's largest natural history museums with dinosaur fossils and space section. Educational for families, Night at the Museum filming location."
    },
    "The High Line": {
        "description": "Terk edilmiş demiryolundan dönüştürülmüş havada süzülen park. Manhattan manzarası, sanat enstalasyonları ve şehir bahçeciği.",
        "description_en": "Park floating in air converted from abandoned railway. Manhattan views, art installations, and urban gardening."
    },
    "Summit One Vanderbilt": {
        "description": "Manhattan'ın en yeni gökdelen manzara noktası, aynalı odalar ve cam zemin deneyimi. Immersive sanat, gün batımı ve skyline.",
        "description_en": "Manhattan's newest skyscraper observation point with mirrored rooms and glass floor experience. Immersive art, sunset, and skyline."
    },
    "Edge NYC": {
        "description": "Batı yarımkürenin en yüksek açık hava gözlem güvertesi, Hudson Yards'da konumlu. Cam köşeler, cesaret testi ve şehir manzarası.",
        "description_en": "Western Hemisphere's highest outdoor observation deck located in Hudson Yards. Glass corners, courage test, and city views."
    },
    "Little Island": {
        "description": "Hudson Nehri üzerinde yüzen botanik park, amfi tiyatro ve yeşil vaha. Ücretsiz konserler, yürüyüşler ve Manhattan kaçışı.",
        "description_en": "Floating botanical park on Hudson River with amphitheater and green oasis. Free concerts, walks, and Manhattan escape."
    },
    "Chelsea Market": {
        "description": "Eski bisküvi fabrikasında gurme gıda hali, dünyadan lezzetler ve alışveriş. Sokak yemekleri, artisan butikler ve foodie cenneti.",
        "description_en": "Gourmet food hall in old biscuit factory with flavors from around the world. Street food, artisan boutiques, and foodie paradise."
    },
    "Brooklyn Bridge Park": {
        "description": "East River kıyısında park kompleksi, Manhattan skyline manzarası. Carousel, spor alanları ve romantik gün batımları.",
        "description_en": "Park complex on East River shore with Manhattan skyline views. Carousel, sports areas, and romantic sunsets."
    },
    "Washington Square Park": {
        "description": "Greenwich Village'ın kalbi, ikonik kemer ve NYU öğrencileriyle canlı atmosfer. Sokak sanatçıları, satranç oyuncuları ve bohemlik.",
        "description_en": "Heart of Greenwich Village with iconic arch and lively atmosphere with NYU students. Street performers, chess players, and bohemianism."
    },
    "Grand Central Terminal": {
        "description": "Dünyanın en ünlü tren istasyonu, gökyüzü tavan freskleri ve Beaux-Arts mimarisi. Alışveriş, yeme-içme ve mimari harikası.",
        "description_en": "World's most famous train station with sky ceiling frescoes and Beaux-Arts architecture. Shopping, dining, and architectural marvel."
    },
    "New York Public Library": {
        "description": "Beaux-Arts başyapıtı, ünlü aslan heykelleri ve Rose Okuma Salonu. Araştırma, sergiler ve Amerikan kültür mirası.",
        "description_en": "Beaux-Arts masterpiece with famous lion statues and Rose Reading Room. Research, exhibitions, and American cultural heritage."
    },
    "Katz's Delicatessen": {
        "description": "1888'den beri hizmet veren efsanevi deli, pastrami sandviçin doğum yeri. When Harry Met Sally sahnesi, NYC klasiği.",
        "description_en": "Legendary deli serving since 1888, birthplace of the pastrami sandwich. When Harry Met Sally scene, NYC classic."
    },
    "Joe's Pizza": {
        "description": "Greenwich Village'daki New York dilim pizzasının efsanevi adresi. İnce hamur, peynir ve otantik NYC deneyimi.",
        "description_en": "Legendary address for New York slice pizza in Greenwich Village. Thin crust, cheese, and authentic NYC experience."
    },
    "Levain Bakery": {
        "description": "Devasa chocolate chip cookie'leriyle ünlü butik fırın. Sıcak, yumuşak ortası ve kurabiye tutkunları için mabedi.",
        "description_en": "Boutique bakery famous for giant chocolate chip cookies. Warm, soft center, and temple for cookie lovers."
    },
    "Dominique Ansel Bakery": {
        "description": "Cronut'un mucidi, Fransız-Amerikan fusion tatlıları. İnovatif pastacılık, sıra beklemeye değer lezzetler.",
        "description_en": "Inventor of the Cronut, French-American fusion desserts. Innovative pastry, flavors worth waiting in line for."
    },
    "Russ & Daughters": {
        "description": "1914'ten beri tütsülenmiş balık ve bagel sunan efsanevi appetizing dükkanı. Lox, kaviar ve New York Yahudi mutfağı.",
        "description_en": "Legendary appetizing shop serving smoked fish and bagels since 1914. Lox, caviar, and New York Jewish cuisine."
    },
    "Los Tacos No. 1": {
        "description": "Otantik Meksika tacosu için Manhattan'ın en iyi adresi. Taze malzemeler, el yapımı tortillalar ve hızlı servis.",
        "description_en": "Manhattan's best address for authentic Mexican tacos. Fresh ingredients, handmade tortillas, and quick service."
    },
    "Le Bernardin": {
        "description": "Dört onlarca yıldır NYC'nin en iyi restoranlarından biri, deniz ürünleri fine-dining. Michelin yıldızları, şef Eric Ripert.",
        "description_en": "One of NYC's best restaurants for four decades, seafood fine-dining. Michelin stars, chef Eric Ripert."
    },
    "Peter Luger Steak House": {
        "description": "1887'den beri Brooklyn'de hizmet veren efsanevi steakhouse. Porterhouse, geleneksel servis ve Amerikan et kültürü.",
        "description_en": "Legendary steakhouse serving in Brooklyn since 1887. Porterhouse, traditional service, and American meat culture."
    },
    "Eleven Madison Park": {
        "description": "Dünyanın en iyi restoranları listesinde sürekli yer alan fine-dining deneyimi. Vejetaryen menü, sanat ve gastronomi.",
        "description_en": "Fine-dining experience consistently on world's best restaurants list. Vegetarian menu, art, and gastronomy."
    },
    "The Loeb Boathouse": {
        "description": "Central Park'ta göl kenarı restoran ve kayık kiralama. Romantik öğle yemeği, brunch ve park manzarası.",
        "description_en": "Lakeside restaurant and boat rental in Central Park. Romantic lunch, brunch, and park views."
    },
    "Intrepid Sea, Air & Space Museum": {
        "description": "Uçak gemisinde kurulan denizcilik, havacılık ve uzay müzesi. Concorde, uzay mekiği ve askeri tarih.",
        "description_en": "Maritime, aviation, and space museum on aircraft carrier. Concorde, space shuttle, and military history."
    },
    "9/11 Memorial & Museum": {
        "description": "İkiz Kulelerin yerinde anıt havuzlar ve yeraltı müzesi. Duygusal deneyim, Amerikan tarihi ve anma.",
        "description_en": "Memorial pools and underground museum at Twin Towers site. Emotional experience, American history, and remembrance."
    },
    "Whitney Museum": {
        "description": "20. ve 21. yüzyıl Amerikan sanatına odaklanan müze, Meatpacking'deki yeni binasıyla. Çağdaş sergiler ve teras manzarası.",
        "description_en": "Museum focusing on 20th and 21st century American art in new Meatpacking building. Contemporary exhibitions and terrace views."
    },
    "Color Factory": {
        "description": "Interaktif renk ve sanat enstalasyonları deneyimi, Instagram-friendly mekanlar. Yaratıcı fotoğraflar, aileler ve eğlence.",
        "description_en": "Interactive color and art installations experience with Instagram-friendly spaces. Creative photos, families, and fun."
    },
    "Tenement Museum": {
        "description": "Lower East Side'da göçmen tarihini anlatan müze, restore edilmiş apartman daireleri. Amerikan rüyası ve göç hikayeleri.",
        "description_en": "Museum telling immigrant history on Lower East Side with restored apartments. American dream and immigration stories."
    },
    "Morgan Library & Museum": {
        "description": "J.P. Morgan'ın özel koleksiyonu, nadir kitaplar ve el yazmaları. Rönesans sanatı, kütüphane ve kültürel miras.",
        "description_en": "J.P. Morgan's private collection with rare books and manuscripts. Renaissance art, library, and cultural heritage."
    },
    "Spyscape": {
        "description": "Casus ve istihbarat dünyasını keşfeden interaktif müze. James Bond, beceri testleri ve gizli ajanlar.",
        "description_en": "Interactive museum exploring the world of spies and intelligence. James Bond, skill tests, and secret agents."
    },
    "Comedy Cellar": {
        "description": "NYC'nin en ünlü stand-up komedi kulübü, efsanevi komedyenlerin sahnesi. Gece eğlencesi, kahkahalar ve sürpriz konuklar.",
        "description_en": "NYC's most famous stand-up comedy club, stage of legendary comedians. Night entertainment, laughs, and surprise guests."
    },
    "Blue Note Jazz Club": {
        "description": "Dünyanın en ünlü caz kulübü, efsanevi müzisyenler ve canlı performanslar. Greenwich Village'da caz gecesi.",
        "description_en": "World's most famous jazz club with legendary musicians and live performances. Jazz night in Greenwich Village."
    },
    "Sleep No More": {
        "description": "McKittrick Hotel'deki immersive tiyatro deneyimi, Macbeth'in yeniden yorumu. Maske, keşif ve deneysel sanat.",
        "description_en": "Immersive theater experience at McKittrick Hotel, reinterpretation of Macbeth. Masks, exploration, and experimental art."
    },
    "Roosevelt Island Tram": {
        "description": "Manhattan'dan Roosevelt Island'a teleferik yolculuğu. Şehir manzarası, pratik ulaşım ve benzersiz deneyim.",
        "description_en": "Cable car journey from Manhattan to Roosevelt Island. City views, practical transport, and unique experience."
    },
    "Staten Island Ferry": {
        "description": "Ücretsiz feribot seferi, Özgürlük Heykeli ve Manhattan skyline manzarası. Turistler için en iyi bedava aktivite.",
        "description_en": "Free ferry ride with Statue of Liberty and Manhattan skyline views. Best free activity for tourists."
    },
    "Oculus": {
        "description": "Santiago Calatrava tasarımı World Trade Center ulaşım merkezi. Beyaz kaburga mimarisi, alışveriş ve modern sanat.",
        "description_en": "Santiago Calatrava-designed World Trade Center transportation hub. White rib architecture, shopping, and modern art."
    },
    "Flatiron Building": {
        "description": "NYC'nin en ikonik gökdelenlerinden biri, üçgen şekilli 1902 yapısı. Fotoğraf noktası, mimari tarih ve Madison Square.",
        "description_en": "One of NYC's most iconic skyscrapers, triangular 1902 building. Photo point, architectural history, and Madison Square."
    },
    "Bryant Park": {
        "description": "Midtown Manhattan'ın yeşil vahası, kış buz pateni ve yaz filmleri. Ücretsiz etkinlikler, piknik ve şehir molası.",
        "description_en": "Midtown Manhattan's green oasis with winter ice skating and summer movies. Free events, picnics, and city break."
    },
    "SoHo Shopping": {
        "description": "Cast-iron binaları ve butik mağazalarıyla ünlü alışveriş mahallesi. Tasarımcı butikler, sanat galerileri ve moda.",
        "description_en": "Shopping neighborhood famous for cast-iron buildings and boutique stores. Designer boutiques, art galleries, and fashion."
    },
    "Chinatown": {
        "description": "Amerika'nın en büyük Çin mahallelerinden biri, otantik dim sum ve Çin pazarları. Sokak yemekleri ve kültürel keşif.",
        "description_en": "One of America's largest Chinatowns with authentic dim sum and Chinese markets. Street food and cultural discovery."
    },
    "Little Italy": {
        "description": "İtalyan göçmen mirasını yaşatan tarihi mahalle, Mulberry Street'in kafe ve restoranları. Cannoli, pasta ve İtalyan ruhu.",
        "description_en": "Historic neighborhood keeping Italian immigrant heritage alive with Mulberry Street cafes and restaurants. Cannoli, pasta, and Italian spirit."
    },
    "Fifth Avenue": {
        "description": "Dünyanın en ünlü alışveriş caddesi, lüks markalar ve ikonik mağazalar. Tiffany's, Saks ve Empire State Building.",
        "description_en": "World's most famous shopping street with luxury brands and iconic stores. Tiffany's, Saks, and Empire State Building."
    },
    "Radio City Music Hall": {
        "description": "Art deco konser salonu, Rockettes ve Noel gösterisiyle ünlü. Broadway yanında, canlı performanslar ve mimari.",
        "description_en": "Art deco concert hall famous for Rockettes and Christmas show. Next to Broadway, live performances, and architecture."
    },
    "St. Patrick's Cathedral": {
        "description": "Amerika'nın en büyük neo-gotik katedrali, Fifth Avenue'da konumlu. Dini miras, vitray pencereler ve mimari absoluteğum.",
        "description_en": "America's largest neo-Gothic cathedral located on Fifth Avenue. Religious heritage, stained glass windows, and architectural magnificence."
    },
    "Smorgasburg": {
        "description": "Amerika'nın en büyük açık hava yemek pazarı, hafta sonları Brooklyn'de. Dünyadan lezzetler, street food ve gurme.",
        "description_en": "America's largest open-air food market, weekends in Brooklyn. Flavors from around the world, street food, and gourmet."
    },
    "Coney Island": {
        "description": "NYC'nin nostaljik plaj ve lunapark mahallesi, Nathan's hot dog ve roller coaster. Yaz eğlencesi, deniz ve retro atmosfer.",
        "description_en": "NYC's nostalgic beach and amusement park neighborhood with Nathan's hot dog and roller coaster. Summer fun, sea, and retro atmosphere."
    },
    "Bronx Zoo": {
        "description": "Amerika'nın en büyük şehir hayvanat bahçesi, 265 hektar alanda binlerce hayvan. Aileler için eğitici, safari deneyimi.",
        "description_en": "America's largest urban zoo with thousands of animals on 265 hectares. Educational for families, safari experience."
    },
    "New York Botanical Garden": {
        "description": "250 hektar botanik bahçesi, seraları ve mevsimlik sergilerle. Doğa kaçışı, eğitim ve Bronx'un yeşil mücevheri.",
        "description_en": "250-hectare botanical garden with greenhouses and seasonal exhibitions. Nature escape, education, and Bronx's green gem."
    },
    "Apollo Theater": {
        "description": "Harlem'in efsanevi müzik salonu, African-American müzik tarihinin kalbi. Amateur Night, soul ve caz efsaneleri.",
        "description_en": "Harlem's legendary music hall, heart of African-American music history. Amateur Night, soul, and jazz legends."
    },
    "Urban Backyard": {
        "description": "Çatı terası bar ve lounge, Manhattan manzarası ve kokteyller. Gece hayatı, DJ setleri ve sosyal atmosfer.",
        "description_en": "Rooftop terrace bar and lounge with Manhattan views and cocktails. Nightlife, DJ sets, and social atmosphere."
    },
    "Jimmy's Corner": {
        "description": "Times Square'deki otantik dive bar, boks temalı dekorasyon. Yerel halk, ucuz içecekler ve NYC gece hayatı.",
        "description_en": "Authentic dive bar in Times Square with boxing-themed decor. Locals, cheap drinks, and NYC nightlife."
    }
}

filepath = 'assets/cities/newyork.json'
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

print(f"\n✅ Manually enriched {count} items (New York - COMPLETE).")

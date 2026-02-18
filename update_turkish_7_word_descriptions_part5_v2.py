
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # NICE
    "\"Mary's sweeties\" gâteaux sur commande": "Özel günleriniz için sipariş üzerine hazırlanan, estetik ve lezzetli kremalı pastalar.",
    "Au Goût Thé D'antan": "Nostaljik atmosferde, aile tarifleriyle hazırlanan ev yapımı tatlılar ve vintage çay keyfi.",
    "Bakery By Michel Fiori": "Michel Fiori'nin ustalığıyla hazırlanan, şehrin en iyi tereyağlı kruvasanları ve ekmekleri.",
    "Big Boy Coffee": "Şehir atmosferinde renkli ve yaratıcı içecekler sunan, güçlü kahveleriyle ünlü mekan.",
    "Café Marché": "Cours Saleya pazarı yakınında, taze malzemelerle hazırlanan sağlıklı kaseler ve brunç seçenekleri.",
    "Cali Coffee Shop | Brunch Breakfast Lunch |": "Kaliforniya esintili rahat bir ortamda, lezzetli takolar ve tüm gün kahvaltı keyfi.",
    "Coffee shop - La Brioche Chaude - CAFÉ": "Notre-Dame manzaralı, ev yapımı sıcak brioche ve taze hamur işleri sunan kafe.",
    "French Coffee Shop": "Sıcak ve davetkar bir ortamda, klasik Fransız hamur işleri ve kahve molası.",
    "Full Bloom Café": "Bitkilerle dolu huzurlu bir dekorasyonda, tamamen vegan lezzetler ve nitelikli kahve sunumu.",
    "La 36eme chambre": "Kore ve Japon etkilerini buluşturan, Asya füzyon brunch menüsüyle yaratıcı bir deneyim.",
    "Le comptoir des frères": "Kardeşlerin işlettiği, kaliteli şarküteri tabakları ve geniş şarap kavı sunan samimi bar.",
    "Les Agitateurs - restaurant gastronomique": "Mevsimsel ve yerel malzemelerle sanatsal tabaklar hazırlayan, yaratıcı Fransız gastronomisi restoranı.",
    "Original Pub Crawl Nice": "Nice'in en iyi barlarını ve gece kulüplerini keşfedebileceğiniz, eğlenceli ve sosyal bir tur.",
    "Umi Cafe": "Japon esintileri taşıyan huzurlu bir ortamda, ev yapımı lezzetlerle brunch keyfi.",
    "V and B Nice Vauban": "Hem şarap mahzeni hem bira barı konseptiyle, geniş içki seçenekleri sunan canlı mekan.",
    "Zitto Speakeasy.": "1920'lerin gizli bar ruhunu yaşatan, yaratıcı kokteyller sunan şık ve loş mekan.",
    "l'Antidote - Restaurant - Bar à cocktails - Cuisine locale de saison": "Mevsimsel yerel malzemelerle hazırlanan modern Fransız yemekleri ve şık atmosferde kokteyl keyfi.",
    "ÉBURNIE COFFEE CULTURE": "Fildişi Sahili'nden gelen nitelikli kahve çekirdekleriyle, özenle hazırlanan özel kahve deneyimi.",

    # OSLO
    "Huk Plajı": "Bygdøy yarımadasının güney ucunda, hem kumluk hem kayalık alanları olan popüler plaj.",
    "Illegal Burger": "Kömür ateşinde pişen, şehrin en lezzetli ve popüler burgerlerini sunan rahat mekan.",
    "Kulturhuset": "Konserler, etkinlikler ve barlarla dolu, şehrin kalbinin attığı çok katlı kültür merkezi.",
    "Paradisbukta Plajı": "Bygdøy'da, aileler için uygun, sakin ve kumlu bir sahil şeridi olan Cennet Koyu.",
    "Åpent Bakeri - Barcode": "Modern Barcode bölgesinde, organik unla yapılan ekşi mayalı ekmekler ve taze hamur işleri.",

    # NEW YORK
    "Altair Restaurant NYC": "Kozmik temalı şık dekorasyonuyla, modern Amerikan mutfağı ve fine dining deneyimi.",
    "Blue Dove Coffee": "Şehrin karmaşasında huzurlu bir mola sunan, taze kruvasanları ve kaliteli kahvesiyle ünlü.",
    "Brickyard Craft Kitchen & Bar": "Endüstriyel şık dekorasyona sahip, craft biralar ve özenli gastropub yemekleri sunan mekan.",
    "Cozymeal Cooking Classes NYC": "Deneyimli şeflerle birlikte dünya mutfaklarını öğrenebileceğiniz, interaktif ve keyifli yemek atölyeleri.",
    "Drinkology NYC": "Kokteyl sanatını bilimsel bir yaklaşımla sunan, modern ve sofistike bir bar deneyimi.",
    "La Cabra Bakery": "Danimarka kökenli, ödüllü kakuleli çörekleri ve hafif kavrulmuş kahvesiyle ünlü fırın.",
    "Le Parisien Bakery": "New York'ta Paris havası estiren, otantik kruvasanlar ve Fransız lezzetleri sunan fırın.",
    "MOE EATS NYC": "Hızlı ve lezzetli atıştırmalıklar arayanlar için ideal, konforlu yemekler sunan durak.",
    "Noise NYC": "Enerji dolu atmosferi ve canlı müziğiyle dikkat çeken, şehrin hareketli noktalarından biri.",
    "Paper Sons Cafe": "Asya esintili dekorasyonuyla, sakin bir çalışma ortamı ve kaliteli kahve sunan kafe.",
    "Sixty Three Clinton": "Modern Amerikan mutfağını yaratıcı dokunuşlarla sunan, Lower East Side'daki şık restoran.",
    "Somm Time": "Sommelier rehberliğinde şarap tadımları ve eşleşmeli lezzetler sunan, samimi şarap barı.",
    "Sote Coffee Roasters": "Taze kavrulmuş çekirdeklerle hazırlanan nitelikli kahveler ve sıcak, davetkar bir kafe ortamı.",
    "Sokağı Bites NYC": "New York sokak lezzetlerini hızlı ve pratik bir şekilde sunan lezzet durağı.",
    "Sweet Cats Union Meydanı": "Sanrio karakter temalı dondurmaları ve oyun makineleriyle eğlenceli ve renkli bir kafe.",
    "Tara Mor | NYC": "Geleneksel İrlanda misafirperverliğini modern New York tarzıyla buluşturan keyifli bir pub.",
    "The Townhouse Cafe": "Çiçekli avlusu ve ışıklı tavanıyla, çalışmak veya dinlenmek için ideal huzurlu kafe.",
    "Tiny Tapas and Bites": "Latin Amerika ve İspanyol esintili minik atıştırmalıklar sunan, samimi ve modern mekan.",

    # MILAN FIXES
    "Cortinovis Specialty Coffee roasters Milano": "Şehrin ilk mikro kavurucusu, nitelikli kahve çekirdekleri ve leziz fıstıklı kruvasanlar sunuyor.",
    "Daimyo Restaurant Milano": "Samuray estetiğiyle tasarlanmış şık bir mekanda, geleneksel ile moderni buluşturan Japon mutfağı.",
    "Il Cafetero Specialty Coffee Milan": "Latin Amerika kökenli çekirdeklerle hazırlanan kahveler ve ev yapımı tatlılar sunan samimi kafe.",
    "Insula Sardinia Experiences - Milano": "Sardunya adasının otantik lezzetlerini modern sunumlarla birleştiren, şarap ve yemek deneyimi.",
    "LUCKY COCKTAIL BAR MILANO": "Gündüz keyifli bir kafe, akşam ise DJ performanslarıyla canlanan şık bir kokteyl bar.",
    "Luma Cocktail Bar": "Aydınlık ve ferah atmosferinde, yaratıcı ve özenle hazırlanmış kokteyller sunan modern bar.",
    "Remedy Wine & Spirits Milano": "Puro odası ve deri koltuklarıyla, kulüp havasında premium şarap ve içki deneyimi.",
    "SAMI : Specialty Coffee from Perù in Milan. Organic Direct Import Roastery.": "Peru'dan doğrudan ithal edilen organik kahveler ve ev yapımı atıştırmalıklar sunan sıcak mekan.",
    "Sciuma Radical Wines - Enoteca Naturale": "Doğal şaraplar ve onlara eşlik eden özenli atıştırmalıklarla, sakin ve samimi şarap barı.",
    "Tin - Cocktail Pub Milano": "Endüstriyel dekorlu rahat ortamında, canlı caz müziği ve yaratıcı kokteyller sunan pub.",
    "Venchi": "1878'den gelen İtalyan geleneğiyle üretilen efsanevi çikolatalar ve lezzetli dondurma çeşitleri.",
    "Verso Ristorante, Capitaneo": "İki Michelin yıldızlı, açık mutfak konseptiyle şefin yaratıcı tabaklarını izleyebileceğiniz restoran.",
    "Vineria Cardenzia #diversamente buoni": "Eski sinema koltuklarıyla dekore edilmiş, özel reçeller ve şaraplar sunan nostaljik mekan.",
    "Viro Steak Restaurant Milano": "Dünyanın farklı bölgelerinden gelen kuru dinlendirilmiş etleri sunan, şık ve zarif steakhouse.",

    # NAPLES FIXES
    "Caffè Belle Arti": "Güzel sanatlar akademisinin yakınında, sanatçıların buluşma noktası olan kültürel ve keyifli kafe.",
    "Ecce Homo Bar Napoli": "Tarihi merkezde, plastik kullanmayan ve samimi sokak atmosferi sunan popüler bar.",
    "Esto Es Mezcaleria": "Meksika ruhunu Napoli'ye taşıyan, geniş mezcal ve agave içkileri koleksiyonuna sahip bar.",
    "Gran Caffè Cimmino": "Napoli körfezi manzaralı, şık dekorasyonu ve premium espresso servisiyle ünlü tarihi kafe.",
    "Il rifugio Wine bar PEPPE MASIELLO. SPRITZ": "Peppe'nin işlettiği, zengin Spritz çeşitleri ve canlı öğrenci ortamıyla bilinen şarap barı.",
    "Joseph Restaurant": "Modern sunumlarla hazırlanan şef yemekleri ve şık atmosferiyle, özel akşamlar için ideal.",
    "Mosto - Birra Artigianale & Distillati": "Geniş craft bira ve viski seçkisi sunan, samimi ve rahat bir mahalle pub'ı.",
    "Pasticceria Anna 1987": "1987 yılından beri hizmet veren, geleneksel Napoli tatlıları ve hamur işleri sunan pastane.",
    "Pasticceria Tizzano® dal 1960 - Unica Sede": "1960'tan beri aynı adreste, şehrin en iyi babà tatlısını yapan tarihi pastane.",
    "Tappò Coctél Bar": "Şarabın olmadığı yerde eğlence olmaz mottosuyla, yaratıcı kokteyller sunan keyifli mekan.",
    "Trattoria Pizzeria Bella Napoli Centro - Chef dal 1990": "1990'dan beri aile işletmesi sıcaklığında, otantik pizza ve deniz ürünleri sunan trattoria.",
    "Zero - Healthy Bar & Specialty Coffee - Napoli": "Sağlıklı smoothie kaseleri ve nitelikli kahve sunan, çalışmaya uygun modern ve ferah kafe.",
    "al Ruotino - Pizzeria Ristorante": "Geleneksel tavada pişen 'ruoto' pizzaları ve ev sıcaklığında bir atmosfer sunan restoran."
}

def main():
    source_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"
    json_files = glob.glob(os.path.join(source_dir, "*.json"))
    json_files.sort()
    
    total_updated = 0
    print(f"Applying updates to {len(json_files)} city files...")
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get('city', 'Unknown')
            highlights = data.get('highlights', [])
            file_changed = False
            
            for place in highlights:
                name = place.get('name', '').strip()
                
                if name in UPDATES:
                    place['description'] = UPDATES[name]
                    file_changed = True
                    total_updated += 1
            
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Saved updates to {city_name}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal Turkish descriptions updated: {total_updated}")

if __name__ == "__main__":
    main()

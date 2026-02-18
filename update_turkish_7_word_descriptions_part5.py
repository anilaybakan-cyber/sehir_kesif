
import json
import os
import glob

# Dictionary of updates: Key = Place Name, Value = New Turkish Description
UPDATES = {
    # NICE
    "\"Mary's sweeties\" gâteaux sur commande": "Özel gün pastaları! Kremalı layer cakes, yumuşak kurabiyeler.",
    "Au Goût Thé D'antan": "Eski zaman çay tadı! Vintage salon, aile tarifleri.",
    "Bakery By Michel Fiori": "Michel Fiori fırını! Eşsiz kruvasanlar, Fransız ustalığı.",
    "Big Boy Coffee": "Büyük çocuk kahvesi! Renkli içecekler, şehir atmosferi.",
    "Café Marché": "Pazar kafesi! Taze lezzetler, sağlıklı kaseler, granola.",
    "Cali Coffee Shop | Brunch Breakfast Lunch |": "Kaliforniya kahve dükkanı! Rahat brunch, leziz tacos.",
    "Coffee shop - La Brioche Chaude - CAFÉ": "Sıcak brioche kafesi! Ev yapımı hamur işleri.",
    "French Coffee Shop": "Fransız kahve dükkanı! Sıcak ortam, kahve molası.",
    "Full Bloom Café": "Tam çiçeklenme kafesi! Vegan lezzetler, bitkili dekor.",
    "La 36eme chambre": "36. oda! Asya füzyon brunch, yaratıcı lezzetler.",
    "Le comptoir des frères": "Kardeşler tezgahı! Samimi şarap barı, kaliteli şarküteri.",
    "Les Agitateurs - restaurant gastronomique": "Kışkırtıcılar restoranı! Yaratıcı Fransız mutfağı, mevsimsel sanat.",
    "Original Pub Crawl Nice": "Orijinal Nice bar turu! Gece hayatı, eğlence.",
    "Umi Cafe": "Japon esintili kafe! Huzurlu brunch, ev yapımı.",
    "V and B Nice Vauban": "Şarap ve bira Nice Vauban! Canlı ortam.",
    "Zitto Speakeasy.": "Zitto gizli bar! 1920'ler ruhu, yaratıcı kokteyller.",
    "l'Antidote - Restaurant - Bar à cocktails - Cuisine locale de saison": "Panzehir restoran! Şık ortam, modern Fransız lezzetleri.",
    "ÉBURNIE COFFEE CULTURE": "Fildişi kahve kültürü! Nitelikli çekirdekler, özenli sunum.",

    # OSLO
    "Huk Plajı": "Huk plajı! Bygdøy yarımadası, popüler yüzme noktası.",
    "Illegal Burger": "Yasadışı burger! Kömür ateşi, şehrin en iyisi.",
    "Kulturhuset": "Kültür evi! Konserler, barlar, canlı sosyal mekan.",
    "Paradisbukta Plajı": "Cennet koyu plajı! Kumlu sahil, aile dostu.",
    "Åpent Bakeri - Barcode": "Açık fırın Barcode! Organik ekmekler, leziz brunch.",

    # NEW YORK
    "Altair Restaurant NYC": "Altair yıldızı restoran! Kozmik şıklık, modern Amerikan.",
    "Blue Dove Coffee": "Mavi güvercin kahvesi! Huzurlu mola, taze kruvasan.",
    "Brickyard Craft Kitchen & Bar": "Zanaat mutfak ve bar! Endüstriyel atmosfer, lezzetler.",
    "Cozymeal Cooking Classes NYC": "Rahat yemek kursları! Şeflerle pratik, dünya mutfağı.",
    "Drinkology NYC": "İçki bilimi NYC! Kokteyl sanatı, modern bar.",
    "La Cabra Bakery": "Keçi fırını! Danimarka kökenli, kardamomlu çörek, kahve.",
    "Le Parisien Bakery": "Parisli fırın! Otantik kruvasanlar, Fransız atmosferi.",
    "MOE EATS NYC": "Moe yemekleri! Rahat atıştırmalıklar, hızlı lezzet durağı.",
    "Noise NYC": "Gürültü NYC! Canlı atmosfer, enerji dolu mekan.",
    "Paper Sons Cafe": "Kağıt oğullar kafesi! Asya esintili, sakin ortam.",
    "Sixty Three Clinton": "Clinton 63! Modern Amerikan mutfağı, şık restoran.",
    "Somm Time": "Sommelier zamanı! Şarap barı, leziz eşleşmeler.",
    "Sote Coffee Roasters": "Sote kahve kavurucusu! Taze çekirdekler, sıcak ortam.",
    "Sokağı Bites NYC": "Sokak lezzetleri NYC! Hızlı, pratik ve lezzetli.",
    "Sweet Cats Union Meydanı": "Tatlı kediler kafe! Sanrio temalı dondurma, eğlence.",
    "Tara Mor | NYC": "Tara Mor İrlanda barı! Modern Kelt misafirperverliği.",
    "The Townhouse Cafe": "Şehir evi kafesi! Işıklı avlu, rahat çalışma.",
    "Tiny Tapas and Bites": "Minik tapas ve lokmalar! Füzyon lezzetler, rahat.",

    # MILAN FIXES
    "Cortinovis Specialty Coffee roasters Milano": "Cortinovis specialty kavurucu! Antep fıstıklı kruvasan, espresso.",
    "Daimyo Restaurant Milano": "Daimyo restoran! Japon füzyon, samuray estetiği şıklık.",
    "Il Cafetero Specialty Coffee Milan": "Cafetero specialty kahve! Samimi ortam, bölgesel lezzetler.",
    "Insula Sardinia Experiences - Milano": "Sardunya adası deneyimi! Modern Sardunya mutfağı, şarap.",
    "LUCKY COCKTAIL BAR MILANO": "Şanslı kokteyl barı! Gündüz kafe, gece lounge.",
    "Luma Cocktail Bar": "Işık kokteyl barı! Aydınlık atmosfer, yaratıcı içkiler.",
    "Remedy Wine & Spirits Milano": "İlaç şarap ve içkiler! Puro odalı kulüp.",
    "SAMI : Specialty Coffee from Perù in Milan. Organic Direct Import Roastery.": "Peru'dan SAMI kahve! Organik çekirdekler, ev yapımı.",
    "Sciuma Radical Wines - Enoteca Naturale": "Köpük radikal şaraplar! Doğal şarap, yerel atıştırmalık.",
    "Tin - Cocktail Pub Milano": "Kalay kokteyl pub! Caz geceleri, craft bira.",
    "Venchi": "Venchi çikolata! 1878 geleneği, İtalyan dondurma mirası.",
    "Verso Ristorante, Capitaneo": "Verso restoran! İki Michelin yıldızlı, açık mutfak.",
    "Vineria Cardenzia #diversamente buoni": "Cardenzia şarap evi! Eski sinema koltukları, nostalji.",
    "Viro Steak Restaurant Milano": "Viro et restoranı! Kuru dinlendirilmiş, şık atmosfer.",

    # NAPLES FIXES
    "Caffè Belle Arti": "Güzel sanatlar kafesi! Sanatsal ortam, keyifli mola.",
    "Ecce Homo Bar Napoli": "İşte İnsan bar! Plastiksiz, samimi sokak barı.",
    "Esto Es Mezcaleria": "Bu mezcal evi! Meksika ruhu, agave içkileri.",
    "Gran Caffè Cimmino": "Büyük Cimmino kafesi! Körfez manzaralı, şık mola.",
    "Il rifugio Wine bar PEPPE MASIELLO. SPRITZ": "Peppe'nin şarap sığınağı! Spritz çeşitleri, canlı ortam.",
    "Joseph Restaurant": "Joseph restoran! Modern lezzetler, şık akşam yemeği.",
    "Mosto - Birra Artigianale & Distillati": "Şıra craft bira! Viski çeşitleri, samimi pub.",
    "Pasticceria Anna 1987": "1987'den beri Anna pastanesi! Geleneksel tatlılar.",
    "Pasticceria Tizzano® dal 1960 - Unica Sede": "Tek adres Tizzano! 1960'tan beri babà uzmanı.",
    "Tappò Coctél Bar": "Tıpa kokteyl barı! Yaratıcı içkiler, keyifli ortam.",
    "Trattoria Pizzeria Bella Napoli Centro - Chef dal 1990": "Güzel Napoli trattoria! 1990'dan beri otantik pizza.",
    "Zero - Healthy Bar & Specialty Coffee - Napoli": "Sıfır sağlıklı bar! Wellness kaseleri, laptop dostu.",
    "al Ruotino - Pizzeria Ristorante": "Tekerlek pizzeria! Tavada pişen pizza, ev sıcaklığı."
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

import json
import os
import csv

def update_from_revize_csv(csv_path):
    # Mapping for new content
    new_content = {
        "Ksamil": {
            "Dimas Caffe Bar & Swimming Pool": {
                "description": "Ksamil'in en popüler dinlenme noktalarından biri olan Dimas, masmavi havuzu ve ferah bahçesiyle kentsel koşturmacadan uzaklaşmak isteyenler için mükemmel bir sığınaktır. Yerel meyvelerle hazırlanan kokteylleri ve samimi atmosferiyle kentin en neşeli duraklarından biridir.",
                "description_en": "One of Ksamil's most popular relaxation spots, Dimas is a perfect refuge with its deep blue pool and airy garden. With its cocktails prepared with local fruits and sincere atmosphere, it's one of the city's most cheerful stops.",
                "tips": "Havuz başında yer bulmak için erken gelin; pizza çeşitleri oldukça doyurucu ve lezzetlidir.",
                "tips_en": "Arrive early for a spot by the pool; their pizza varieties are quite filling and delicious.",
                "category": "Sosyal"
            },
            "Dolphins Cafe-Bar": {
                "description": "Ksamil sahilinde denize sıfır konumuyla Dolphins Cafe-Bar, İyon Denizi'nin turkuaz manzarasına karşı kahvenizi yudumlayabileceğiniz en keyifli noktalardan biridir. Modern tasarımı ve kentin deniz esintisini içine çeken terasıyla günün her saati canlıdır.",
                "description_en": "With its beachfront location on Ksamil coast, Dolphins Cafe-Bar is one of the most pleasant spots to sip your coffee against the turquoise view of the Ionian Sea. It is vibrant at all hours with its modern design and terrace that breathes in the city's sea breeze.",
                "tips": "Gün batımı saatlerinde terasa çıkın; dondurmalı buzlu kahveleri kentin en iyisidir.",
                "tips_en": "Go to the terrace at sunset; their iced coffees with ice cream are the best in town.",
                "category": "Sosyal"
            },
            "Poseidon Hotel, Trident Bar & Coffee Lounge": {
                "description": "Ksamil'in girişinde yer alan bu şık lounge, modern ve minimalist tasarımıyla kentsel estetiği deniz havasıyla buluşturuyor. Hem otel misafirlerine hem de dışarıdan gelenlere kaliteli bir mola imkanı sunan mekan, kentin en prestijli kahve duraklarından biridir.",
                "description_en": "Located at the entrance of Ksamil, this stylish lounge blends urban aesthetics with sea air through its modern and minimalist design. Offering a high-quality break for both hotel guests and visitors, it is one of the city's most prestigious coffee stops.",
                "tips": "Taze yapılmış sandviçleri kahvaltı için idealdir; iç mekandaki sanat eserlerini incelemeyi unutmayın.",
                "tips_en": "Their freshly made sandwiches are ideal for breakfast; don't forget to examine the artworks in the interior.",
                "category": "Sosyal"
            },
            "Te GERI Hotel&PizzaBar": {
                "description": "Ksamil'in en iyi odun ateşinde pişmiş pizzalarını sunan Te GERI, İtalyan mutfak kültürünü Arnavut misafirperverliğiyle harmanlıyor. Samimi bahçesi ve kentin enerjisini yansıtan neşeli dekorasyonuyla akşam yemeklerinin vazgeçilmez adresidir.",
                "description_en": "Offering Ksamil's best wood-fired pizzas, Te GERI blends Italian culinary culture with Albanian hospitality. With its cozy garden and cheerful decoration reflecting the city's energy, it is an indispensable address for dinners.",
                "tips": "Deniz mahsüllü pizzasını mutlaka deneyin; ev yapımı acı sosları pizzaya harika bir derinlik katıyor.",
                "tips_en": "Be sure to try the seafood pizza; their homemade spicy sauce adds a wonderful depth to the pizza.",
                "category": "Restoran"
            },
            "Azora Beach": {
                "description": "Ksamil'in saklı kalmış koylarından birinde yer alan Azora Beach, beyaz kumsalı ve turkuaz sularıyla tam bir Arktik-Akdeniz rüyası sunar. Şık şezlongları ve havadar beach-barı ile kentsel kalabalıktan kaçıp denizin tadını çıkarabileceğiniz en kaliteli duraktır.",
                "description_en": "Located in one of Ksamil's hidden coves, Azora Beach offers a true Arctic-Mediterranean dream with its white sandy beach and turquoise waters. With its stylish sun loungers and airy beach-bar, it is the highest quality stop where you can escape urban crowds and enjoy the sea.",
                "tips": "Hafta sonları DJ performansları olur, enerji çok yükselir; deniz botunuzla karşıdaki küçük adacığa yüzmeyi deneyin.",
                "tips_en": "There are DJ performances on weekends, and the energy gets very high; try swimming to the small islet across with your sea boots.",
                "category": "Sosyal"
            }
        },
        "Bari": {
            "Regional Directorate of Museums": {
                "description": "Bari'nin kültürel mirasını yöneten bu merkez, kentin binlerce yıllık tarihine ışık tutan paha biçilemez koleksiyonları koordine eder. Puglia bölgesinin sanatsal ve arkeolojik değerlerini koruyan bu kurum, kentin tarihsel hafızasının en prestijli kalesidir.",
                "description_en": "Coordinating priceless collections that shed light on the city's millennia-old history, this center manages Bari's cultural heritage. This institution, preserving the artistic and archaeological values of the Puglia region, is the most prestigious fortress of the city's historical memory.",
                "tips": "Güncel sergi takvimini kapıdaki panodan kontrol edin; kütüphane bölümünde kentin tarihine dair nadir kitaplar bulabilirsiniz.",
                "tips_en": "Check the current exhibition schedule on the board at the entrance; you can find rare books on the city's history in the library section.",
                "category": "Kültür"
            },
            "Museo della Fotografia": {
                "description": "Bari Politeknik Üniversitesi bünyesinde yer alan bu müze, kentin görsel tarihini ve modern fotoğraf sanatını bir araya getiren estetik bir duraktır. Yerel ve uluslararası fotoğrafçıların gözünden kentin ve dünyanın değişimini yansıtan sergiler sunar.",
                "description_en": "Part of the Polytechnic University of Bari, this museum is an aesthetic stop bringing together the city's visual history and modern photography art. It offers exhibitions reflecting the change of the city and the world through the eyes of local and international photographers.",
                "tips": "Süreli sergiler her ay değişir, gitmeden önce web sitesini kontrol edin; siyah beyaz Puglia fotoğrafları koleksiyonu büyüleyicidir.",
                "tips_en": "Temporary exhibitions change every month, check the website before going; the collection of black and white Puglia photos is fascinating.",
                "category": "Müze"
            },
            "Hotel Majesty Bari": {
                "description": "Bari'nin girişinde, yeşillikler içinde yer alan Hotel Majesty, kentin klasik zarafetini modern konforla birleştiren köklü bir konaklama merkezidir. Geniş bahçeleri, kapalı havuzu ve kentin gastronomi zenginliğini sunan restoranıyla kentsel koşturmacadan uzaklaşmak için idealdir.",
                "description_en": "Located in lush greenery at the entrance of Bari, Hotel Majesty is a long-established accommodation center combining the city's classic elegance with modern comfort. With its large gardens, indoor pool, and restaurant offering the city's gastronomic richness, it's ideal for escaping urban hustle.",
                "tips": "Otelin fitness ve spa merkezi oldukça kapsamlıdır; pazar brunchları kentin yerel halkı arasında da popülerdir.",
                "tips_en": "The hotel's fitness and spa center is quite comprehensive; Sunday brunches are also popular among the city's locals.",
                "category": "Deneyim"
            }
        }
    }

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            city = row.get('City')
            name = row.get('Place Name')
            revize = row.get('Revize')
            
            if revize == 'x' and city in new_content and name in new_content[city]:
                # Update JSON
                city_file = f'assets/cities/{city.lower()}.json'
                if os.path.exists(city_file):
                    with open(city_file, 'r') as jf:
                        data = json.load(jf)
                    
                    changed = False
                    highlights = data if isinstance(data, list) else data.get('highlights', [])
                    for h in highlights:
                        if h.get('name') == name:
                            upd = new_content[city][name]
                            h['description'] = upd['description']
                            h['description_en'] = upd['description_en']
                            h['tips'] = upd['tips']
                            h['tips_en'] = upd['tips_en']
                            h['category'] = upd['category']
                            changed = True
                    
                    if changed:
                        with open(city_file, 'w') as jf:
                            json.dump(data, jf, indent=2, ensure_ascii=False)
                        print(f"Updated {name} in {city_file}")

update_from_revize_csv('/Users/anilebru/Desktop/revize_özet_final.csv')
print("Batch update completed.")

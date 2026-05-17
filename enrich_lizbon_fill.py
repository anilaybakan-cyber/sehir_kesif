from dotenv import load_dotenv
load_dotenv()
import os
#!/usr/bin/env python3
"""
Lizbon için eksik kalan ~50 mekanı tamamlayan script.
Google Places API kullanarak fotoğraf ve detayları çeker.
Silinen önemli yerleri (Belem, Tram 28 vb.) geri getirir.
"""

import json
import requests
import time
from pathlib import Path

# Google Places API Key
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
CITY_FILE = Path("assets/cities/lizbon.json")

# Eklenecek/Geri Getirilecek 50+ Mekan
NEW_PLACES = [
    {"name": "Belém Tower", "category": "Tarihi", "desc": "Tejo Nehri kıyısında, Manuelin mimarisinin en güzel örneği olan ikonik kule."},
    {"name": "Jerónimos Monastery", "category": "Tarihi", "desc": "Vasco da Gama'nın mezarına ev sahipliği yapan, UNESCO listesindeki muazzam manastır."},
    {"name": "Castelo de S. Jorge", "category": "Tarihi", "desc": "Şehrin en yüksek tepesinde, muhteşem manzaralara sahip tarihi kale."},
    {"name": "Praça do Comércio", "category": "Meydan", "desc": "Nehir kıyısında, sarı binalarıyla ünlü Avrupa'nın en büyük meydanlarından biri."},
    {"name": "Rossio Square", "category": "Meydan", "desc": "Dalgalı mozaik zemini ve canlı atmosferiyle Lizbon'un kalbi."},
    {"name": "LX Factory", "category": "Kültür Merkezi", "desc": "Eski sanayi bölgesinde kurulan, tasarım dükkanları ve restoranlarla dolu yaratıcı alan."},
    {"name": "Time Out Market", "category": "Yeme İçme", "desc": "Şehrin en iyi şeflerinin yemeklerini tadabileceğiniz devasa yemek pazarı."},
    {"name": "Tram 28", "category": "Deneyim", "desc": "Dar sokaklardan geçerek tarihi bölgeleri turlayan nostaljik sarı tramvay."},
    {"name": "Santa Justa Lift", "category": "Manzara", "desc": "Şehir merkezini kuşbakışı gören, neo-gotik tarzdaki tarihi asansör."},
    {"name": "Padrão dos Descobrimentos", "category": "Anıt", "desc": "Portekizli kaşiflere adanmış, nehir kıyısındaki heybetli anıt."},
    {"name": "MAAT Museum", "category": "Müze", "desc": "Fütüristik mimarisiyle dikkat çeken Sanat, Mimari ve Teknoloji Müzesi."},
    {"name": "Oceanário de Lisboa", "category": "Akvaryum", "desc": "Avrupa'nın en büyük ve etkileyici kapalı akvaryumlarından biri."},
    {"name": "Alfama", "category": "Semt", "desc": "Fado müziğinin doğduğu, dar sokaklı ve merdivenli en eski semt."},
    {"name": "Bairro Alto", "category": "Semt", "desc": "Gündüz sakin, gece hareketli barlarıyla ünlü bohem semt."},
    {"name": "Miradouro da Senhora do Monte", "category": "Manzara", "desc": "Şehrin en yüksek noktasında, gün batımını izlemek için en iyi manzara terası."},
    {"name": "Miradouro de Santa Catarina", "category": "Manzara", "desc": "Gençlerin ve sokak müzisyenlerinin buluşma noktası olan popüler seyir terası."},
    {"name": "Miradouro das Portas do Sol", "category": "Manzara", "desc": "Alfama'nın kırmızı çatılarını ve nehir manzarasını izleyebileceğiniz balkon."},
    {"name": "Pasteis de Belem", "category": "Kafe", "desc": "Meşhur Portekiz tartı Pastel de Nata'nın doğduğu tarihi pastane."},
    {"name": "Manteigaria", "category": "Kafe", "desc": "Sadece Pastel de Nata yapan ve bu konuda şehrin en iyilerinden biri olan mekan."},
    {"name": "A Ginjinha", "category": "Deneyim", "desc": "Meşhur vişne likörü Ginjinha'yı ayakta tadabileceğiniz tarihi büfe."},
    {"name": "Park Bar", "category": "Bar", "desc": "Bir otoparkın çatısında yer alan, yeşillikler içindeki gizli teras bar."},
    {"name": "Ponto Final", "category": "Restoran", "desc": "Nehrin karşı kıyısında, gün batımı manzarasıyla ünlü restoran."},
    {"name": "Cervejaria Ramiro", "category": "Restoran", "desc": "Deniz ürünleriyle meşhur, her zaman kalabalık ve canlı restoran."},
    {"name": "Pink Street", "category": "Gece Hayatı", "desc": "Pembe boyalı zemini ve barlarıyla ünlü, Instagramlık bir sokak."},
    {"name": "Calouste Gulbenkian Museum", "category": "Müze", "desc": "Antik çağdan moderne uzanan muazzam bir sanat koleksiyonuna sahip müze."},
    {"name": "National Tile Museum", "category": "Müze", "desc": "Portekiz'in ünlü Azulejo çini sanatının tarihini anlatan müze."},
    {"name": "National Coach Museum", "category": "Müze", "desc": "Dünyanın en zengin kraliyet arabaları koleksiyonuna sahip müze."},
    {"name": "Carmo Convent", "category": "Tarihi", "desc": "1755 depreminde çatısı yıkılan ve gökyüzüne açık kalan gotik kilise kalıntısı."},
    {"name": "Lisbon Cathedral", "category": "Tarihi", "desc": "Şehrin en eski kilisesi, kale benzeri görünümüyle dikkat çeker."},
    {"name": "Chiado", "category": "Semt", "desc": "Alışveriş, tiyatro ve tarihi kafeleriyle ünlü zarif semt."},
    {"name": "Mercado da Ribeira", "category": "Pazar", "desc": "Geleneksel pazar yeri ve modern yemek alanının buluştuğu nokta."},
    {"name": "Jardim da Estrela", "category": "Park", "desc": "Egzotik ağaçları ve sakin atmosferiyle şehrin en sevilen parklarından biri."},
    {"name": "Parque Eduardo VII", "category": "Park", "desc": "Şehrin merkezinde, geometrik çalılarıyla ünlü devasa park."},
    {"name": "Amoreiras 360 Panoramic View", "category": "Manzara", "desc": "Şehri 360 derece görebileceğiniz en yüksek noktalardan biri."},
    {"name": "Feira da Ladra", "category": "Pazar", "desc": "Salı ve Cumartesi günleri kurulan, her türlü antikanın bulunduğu ünlü bit pazarı."},
    {"name": "Embaixada", "category": "Alışveriş", "desc": "Eski bir Arap sarayında yer alan, konsept mağazalarla dolu alışveriş galerisi."},
    {"name": "Village Underground Lisboa", "category": "Kültür Merkezi", "desc": "Konteyner ve otobüslerden oluşan, yaratıcı ofis ve etkinlik alanı."},
    {"name": "Pensão Amor", "category": "Bar", "desc": "Eski bir genelevden dönüştürülen, teatral dekoruyla ünlü bar."},
    {"name": "Chapitô à Mesa", "category": "Restoran", "desc": "Kalenin altında, harika manzaralı ve sirk okulu içindeki restoran."},
    {"name": "Casa do Alentejo", "category": "Mimar", "desc": "Mağribi avlusu ve balo salonuyla gizli kalmış bir mimari mücevher."},
    {"name": "Ler Devagar", "category": "Kitapçı", "desc": "LX Factory içinde, uçan bisiklet heykeliyle ünlü büyüleyici kitapçı."},
    {"name": "Fábrica Coffee Roasters", "category": "Kafe", "desc": "Kendi kavurdukları çekirdeklerle şehrin en iyi kahvelerinden birini sunar."},
    {"name": "Copenhagen Coffee Lab", "category": "Kafe", "desc": "Minimalist İskandinav tarzı ve lezzetli hamur işleriyle ünlü kafe."},
    {"name": "Dear Breakfast", "category": "Kafe", "desc": "Şık dekorasyonu ve tüm gün kahvaltı konseptiyle popüler mekan."},
    {"name": "Tease", "category": "Kafe", "desc": "Kaya gibi sert cupcake'leri ve sıra dışı dekoruyla bilinen kafe."},
    {"name": "Landeau Chocolate", "category": "Kafe", "desc": "'Dünyanın en iyi çikolatalı keki'ni yaptığını iddia eden mekan."},
    {"name": "O Trevo", "category": "Yeme İçme", "desc": "Anthony Bourdain'in ziyaret ettiği, en iyi Bifana sandviçini yapan yerel büfe."},
    {"name": "Casa da Índia", "category": "Restoran", "desc": "Geleneksel Portekiz yemekleri sunan, her zaman hareketli ve otantik restoran."},
    {"name": "Bonjardim", "category": "Restoran", "desc": "Piri-piri tavuğu ile ünlü, turistlerin ve yerlilerin uğrak noktası."},
    {"name": "Pena Palace", "category": "Tarihi", "desc": "Sintra'da, masallardan fırlamış gibi duran rengarenk romantik saray."},
    {"name": "Quinta da Regaleira", "category": "Tarihi", "desc": "Gizli tünelleri, inisiyasyon kuyusu ve bahçeleriyle mistik bir malikane."},
    {"name": "Cabo da Roca", "category": "Manzara", "desc": "Avrupa kıtasının en batı ucu, 'karanın bittiği ve denizin başladığı yer'."},
    {"name": "Cascais", "category": "Semt", "desc": "Lizbon'a yakın, plajları ve marinasıyla ünlü şık sahil kasabası."}
]

def get_place_details(place_name):
    """Google Places API'den fotoğraf, lokasyon ve rating al."""
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"{place_name} Lisbon",
        "inputtype": "textquery",
        "fields": "place_id,photos,geometry,rating,user_ratings_total,formatted_address",
        "key": API_KEY
    }
    
    try:
        resp = requests.get(search_url, params=params)
        data = resp.json()
        
        if data.get("status") == "OK" and data.get("candidates"):
            candidate = data["candidates"][0]
            
            result = {
                "lat": candidate["geometry"]["location"]["lat"],
                "lng": candidate["geometry"]["location"]["lng"],
                "rating": candidate.get("rating", 4.5),
                "reviewCount": candidate.get("user_ratings_total", 100),
                "address": candidate.get("formatted_address", "Lisbon, Portugal")
            }
            
            if "photos" in candidate:
                photo_ref = candidate["photos"][0]["photo_reference"]
                result["imageUrl"] = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
            else:
                result["imageUrl"] = "" # Fotoğraf yoksa boş bırak
                
            return result
    except Exception as e:
        print(f"  ❌ Hata ({place_name}): {e}")
        
    return None

def main():
    print(f"🚀 Lizbon zenginleştirme başlatılıyor... ({len(NEW_PLACES)} mekan)")
    
    with open(CITY_FILE, 'r', encoding='utf-8') as f:
        city_data = json.load(f)
        
    existing_names = {p["name"].lower() for p in city_data["highlights"]}
    added_count = 0
    
    for place in NEW_PLACES:
        if place["name"].lower() in existing_names:
            print(f"  ⚠️ Zaten var: {place['name']}")
            continue
            
        print(f"  🔍 İşleniyor: {place['name']}...")
        details = get_place_details(place["name"])
        
        if details:
            new_place = {
                "id": f"lis_{int(time.time())}_{added_count}",
                "name": place["name"],
                "description": place["desc"],
                "category": place["category"],
                "imageUrl": details["imageUrl"],
                "lat": details["lat"],
                "lng": details["lng"],
                "rating": details["rating"],
                "address": details["address"],
                "expense": "€€",
                "distanceFromCenter": 0.0
            }
            city_data["highlights"].append(new_place)
            added_count += 1
            print(f"  ✅ Eklendi: {place['name']}")
            time.sleep(0.5) 
        else:
            print(f"  ❌ Detaylar alınamadı: {place['name']}")
            
    # Kaydet
    with open(CITY_FILE, 'w', encoding='utf-8') as f:
        json.dump(city_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n💾 Toplam {added_count} yeni mekan eklendi. Yeni toplam: {len(city_data['highlights'])}")

if __name__ == "__main__":
    main()

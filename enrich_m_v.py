import json
import os

def enrich_mallorca_valencia():
    # --- MALLORCA ---
    m_path = "assets/cities/mallorca.json"
    if os.path.exists(m_path):
        with open(m_path, "r", encoding="utf-8") as f:
            m_data = json.load(f)
        
        m_enrich = {
            "ChIJVY-vfUWSlxIRqoH9muibDFQ": {
                "tr": "Palma de Mallorca'nın silüetini belirleyen bu görkemli Gotik katedral, denize bakan eşsiz konumuyla büyüleyicidir. Gaudí'nin renovasyon çalışmaları ve dünyanın en büyük gül pencerelerinden biriyle tanınan katedral, adanın dini ve mimari merkezidir.",
                "en": "Dominating the skyline of Palma, this majestic Gothic cathedral stands impressively right by the sea. Famous for Gaudí's interior renovations and one of the largest rose windows in the world, it is the spiritual and architectural heart of the island."
            },
            "ChIJd7Q-FHGSlxIRof_ZMNOu1sg": {
                "tr": "14. yüzyıldan kalma bu nadir dairesel kale, Palma şehrini kuşbakışı gören bir çam ormanı tepesinde yer alır. Eskiden kraliyet ikametgahı ve ardından hapishane olarak kullanılan kale, günümüzde şehrin en iyi restorasyon parklarından ve müzelerinden biridir.",
                "en": "This rare 14th-century circular castle sits atop a pine-forested hill with panoramic views of Palma. Formerly a royal residence and later a prison, it now serves as a history museum and one of the most distinctive landmarks in the Mediterranean."
            },
            "ChIJ_8aKugPulxIRPhKWi-dSSJI": {
                "tr": "Tramuntana Dağları'nın kalbinde yer alan Valldemossa, taş evleri ve dar sokaklarıyla Mallorca'nın en romantik köyüdür. Besteci Chopin ve George Sand'ın bir kışı geçirdiği tarihi Kartujyalı Manastırı ile ünlüdür.",
                "en": "Nestled in the heart of the Tramuntana Mountains, Valldemossa is Mallorca's most romantic village, featuring stone houses and narrow alleys. It is famous for the Royal Charterhouse, where composer Frédéric Chopin and George Sand spent a winter."
            },
            "ChIJ_aPTXrBGlhIRHXI-HoVfGpI": {
                "tr": "Doğu kıyısındaki Porto Cristo'da bulunan Drach Mağaraları, dünyanın en büyük yeraltı göllerinden birine ev sahipliği yapar. Ziyaretçiler, devasa sarkıtlar arasında bir sandal gezintisi yaparken canlı klasik müzik dinletisiyle büyüleyici bir deneyim yaşarlar.",
                "en": "Located in Porto Cristo, the Caves of Drach house one of the world's largest underground lakes. Visitors enjoy a magical experience with classical music concerts performed on illuminated boats while drifting through spectacular stalactites."
            }
        }
        
        for h in m_data["highlights"]:
            if h["id"] in m_enrich:
                h["description"] = m_enrich[h["id"]]["tr"]
                h["description_en"] = m_enrich[h["id"]]["en"]
        
        with open(m_path, "w", encoding="utf-8") as f:
            json.dump(m_data, f, ensure_ascii=False, indent=2)

    # --- VALENCIA ---
    v_path = "assets/cities/valencia.json"
    if os.path.exists(v_path):
        with open(v_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
            
        v_enrich = {
            "ChIJgUOb0elIYA0RlPjrpQdE62I": {
                "tr": "Valencia'nın fütüristik sembolü olan bu bilim ve sanat kompleksi, Santiago Calatrava ve Félix Candela tarafından tasarlanmıştır. Dev bir göz şeklindeki Hemisfèric ve Avrupa'nın en büyük akvaryumu ile modern mimarinin dünyadaki en görkemli örneklerinden biridir.",
                "en": "Valencia's futuristic masterpiece, this science and art complex was designed by Santiago Calatrava and Félix Candela. Featuring a giant eye-shaped cinema and Europe's largest aquarium, it is a global landmark of cutting-edge modern architecture."
            },
            "ChIJG-bUp05PYA0RjV0kiVYDQxI": {
                "tr": "Avrupa'nın halen aktif olan en büyük pazarlarından biri olan Mercado Central, muazzam bir Art Nouveau binasında yer alır. Renkli seramikleri ve demir kubbesiyle sadece alışveriş için değil, kentin gastronomi kültürünü solumak için de eşsizdir.",
                "en": "One of Europe's largest active marketplaces, the Central Market is housed in a stunning Art Nouveau building. With its vibrant ceramics and iconic iron dome, it is the perfect place to experience Valencia's rich gastronomic heritage."
            },
            "ChIJ8_5rwk1PYA0RxMucY8qxErc": {
                "tr": "İpek Borsası anlamına gelen La Lonja de la Seda, Gotik sivil mimarinin dünyadaki en önemli örneklerinden biridir ve UNESCO mirasıdır. Sarmal sütunlarıyla ünlü ana salonu, kentin Orta Çağ'daki ticari gücünü temsil eden görkemli bir yapıdır.",
                "en": "The Silk Exchange (La Lonja de la Seda) is a UNESCO World Heritage site and a masterpiece of Gothic civil architecture. Its spectacular main hall with spiral columns represents Valencia's immense commercial power during the late Middle Ages."
            },
            "ChIJrbJpyXNIYA0R9GvWIvnsO2A": {
                "tr": "Valencia'nın en geniş ve popüler plajı olan Malvarrosa, kentin tarihi merkezine çok yakın konumda yer alır. Sahil boyunca uzanan restoranlarda meşhur 'Paella'nın tadına bakabilir ve geniş kumsalın keyfini çıkarabilirsiniz.",
                "en": "Valencia's widest and most popular beach, Malvarrosa, is located just minutes from the historic center. The long promenade is famous for its authentic restaurants serving traditional Valencian Paella with stunning views of the Mediterranean."
            }
        }
        
        for h in v_data["highlights"]:
            if h["id"] in v_enrich:
                h["description"] = v_enrich[h["id"]]["tr"]
                h["description_en"] = v_enrich[h["id"]]["en"]
        
        with open(v_path, "w", encoding="utf-8") as f:
            json.dump(v_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    enrich_mallorca_valencia()

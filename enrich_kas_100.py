from enrich_venues import enrich_venues

# FINAL SWEEP: KAŞ 100%

kas_last_fix = {
    "Antalya kaş": {
        "desc_tr": "Kaş'ın girişini simgeleyen bu nokta, masmavi bir denizin ve dik kayalıkların arasından kente süzülen büyüleyici bir yolculuğun son durağıdır. Akdeniz'in en güzel sahil yollarından birinin üzerinde yer alan bu bölge, kente ilk 'merhaba' dediğiniz yerdir.",
        "desc_en": "Marking the entrance to Kaş, this spot is the final stop of a magical journey through turquoise waters and steep cliffs. Located on one of the Mediterranean's most beautiful coastal roads, it's where you first say 'hello' to the town."
    },
    "بداية اوزون شارشيه": {
        "desc_tr": "Kaş'ın dünyaca ünlü Uzun Çarşı'sının başlangıç noktası olan bu kentsel alan, tarihle modern alışverişin buluştuğu yerdir. Likya lahitlerinin gölgesindeki bu renkli cadde, kentin en canlı ve fotografik yürüyüş rotasının ilk adımıdır.",
        "desc_en": "The starting point of Kaş's world-famous Uzun Çarşı, this urban area is where history meets modern shopping. This colorful street, in the shadow of Lycian sarcophagi, is the first step of the town's most vibrant and photographic walking route."
    }
}

enrich_venues("kas", kas_last_fix)
print("✅ Kaş is now 100% complete.")

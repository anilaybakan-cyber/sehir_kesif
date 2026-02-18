#!/bin/bash
# Tüm şehirleri sırayla zenginleştirir.

CITY_FILES=assets/cities/*.json

echo "🌍 KAPSAMLI ZENGİNLEŞTİRME BAŞLATILIYOR (36 ŞEHİR)..."

for f in $CITY_FILES
do
  city_name=$(basename "$f" .json)
  echo "--------------------------------------------------"
  echo "⏩ İşlenen Şehir: $city_name"
  python3 mass_enrich_city.py "$city_name"
  
  # API Rate limit'e takılmamak için şehirler arası kısa bekleme
  echo "⏳ Bekleniyor..."
  sleep 2
done

echo "🎉 TÜM ŞEHİRLER TAMAMLANDI!"

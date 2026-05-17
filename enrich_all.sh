#!/bin/bash
# Tüm şehirleri sırayla zenginleştirir.
# ⚠️ DİKKAT: Bu script çalıştırılırsa Google Places API üzerinden ON BİNLERCE istek
#    ve kolayca ON BİNLERCE TL / yüzlerce USD tutarında fatura doğurabilir.
#
# mass_enrich_city.py artık çalışmadan önce bilinçli onay ister:
#   export I_ACCEPT_GOOGLE_PLACES_BILLING_RISK=1
# veya her çağrıda:  python3 mass_enrich_city.py --i-accept-billing-risk <şehir>

echo "🛑 GÜVENLİK UYARISI: Toplu zenginleştirme işlemi binlerce TL tutabilir."
echo "Eğer gerçekten tüm şehirleri (90+) işlemek istiyorsanız script'i düzenleyip kilidi açmalısınız."
echo "Önce TEK şehirle test edin; Maps Platform fiyatlandırmasını okuyun."

# Güvenlik Kilidi:
echo "Mevcut maliyet riskleri nedeniyle bu script devre dışı bırakıldı."
echo "Tek şehir: export I_ACCEPT_GOOGLE_PLACES_BILLING_RISK=1 && python3 mass_enrich_city.py <şehir_adı>"
exit 1

# Kilidi açmak için aşağıdaki satırların yorumunu kaldırın ve önce export edin:
# export I_ACCEPT_GOOGLE_PLACES_BILLING_RISK=1
# CITY_FILES=assets/cities/*.json
# for f in $CITY_FILES
# do
#   city_name=$(basename "$f" .json)
#   python3 mass_enrich_city.py --i-accept-billing-risk "$city_name"
#   sleep 2
# done

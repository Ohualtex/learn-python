# 01_sayi_tahmin_oyunu.py
# Bu örnekte şu ana kadar işlenen şu konular kullanılmıştır:
# - Değişkenler ve Tür Dönüşümleri (int, input)
# - Akış Kontrolü (if, elif, else)
# - Döngüler (while, continue)

import random

print("--- Sayı Tahmin Oyununa Hoş Geldiniz ---")
print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misiniz?")

gizli_sayi = random.randint(1, 100)
tahmin_hakki = 5
oyun_bitti_mi = False

while tahmin_hakki > 0 and not oyun_bitti_mi:
    print(f"\nKalan tahmin hakkınız: {tahmin_hakki}")
    
    # Kullanıcıdan girdi alırken tip dönüşümü yapıyoruz (Tuzak: string'i int'e çevirmeyi unutmamak)
    tahmin_str = input("Tahmininiz nedir? ")
    
    # Eğer kullanıcı harf girerse program çökmesin diye basit bir kontrol
    if not tahmin_str.isdigit():
        print("Lütfen sadece sayı giriniz!")
        continue

    tahmin = int(tahmin_str)
    
    if tahmin == gizli_sayi:
        # f-string kullanımı
        print(f"TEBRİKLER! Sayıyı {6 - tahmin_hakki}. denemede doğru bildiniz: {gizli_sayi}")
        oyun_bitti_mi = True
    elif tahmin > gizli_sayi:
        print("Daha KÜÇÜK bir sayı girin.")
    else:
        print("Daha BÜYÜK bir sayı girin.")
        
    tahmin_hakki -= 1  # Python'da tahmin_hakki-- yoktur

if not oyun_bitti_mi:
    print(f"\nMaalesef tahmin hakkınız bitti. Tuttuğum sayı: {gizli_sayi}")

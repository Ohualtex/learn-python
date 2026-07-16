"""
Örnek 02: Fonksiyonel Modüler Hesap Makinesi

Bu program kullanıcıdan alınan sayılarla temel 4 işlem yapar.

Bu örnekte fonksiyonlar, modüler yapı ve hata kontrolleri kullanılmıştır.
"""

def topla(a: float, b: float) -> float:
    return a + b

def cikar(a: float, b: float) -> float:
    return a - b

def carp(a: float, b: float) -> float:
    return a * b

def bol(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Sıfıra bölme hatası: İkinci sayı 0 olamaz!")
    return a / b

def menuyu_goster():
    print("\n--- HESAP MAKİNESİ ---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

def main():
    while True:
        menuyu_goster()
        secim = input("İşlem seçiniz (1-5): ").strip()
        
        if secim == '5':
            print("Hesap makinesinden çıkılıyor. İyi günler!")
            break
            
        if secim not in ('1', '2', '3', '4'):
            print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")
            continue
            
        try:
            sayi1 = float(input("1. Sayı: "))
            sayi2 = float(input("2. Sayı: "))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")
            continue

        try:
            if secim == '1':
                sonuc = topla(sayi1, sayi2)
                islem = "+"
            elif secim == '2':
                sonuc = cikar(sayi1, sayi2)
                islem = "-"
            elif secim == '3':
                sonuc = carp(sayi1, sayi2)
                islem = "*"
            elif secim == '4':
                sonuc = bol(sayi1, sayi2)
                islem = "/"
                
            print(f"\n>>> Sonuç: {sayi1} {islem} {sayi2} = {sonuc}")
        except ValueError as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    main()

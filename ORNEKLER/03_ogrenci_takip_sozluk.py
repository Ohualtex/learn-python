"""
Örnek 03: Sözlük ve Listeler ile Öğrenci Takip Sistemi

Bu örnekte dict, list, fonksiyonlar ve temel döngüler kullanılarak 
öğrenci ekleme, not güncelleme ve ortalama hesaplama işlemleri yapılır.
"""

ogrenciler = {}

def ogrenci_ekle(numara: str, ad: str):
    if numara in ogrenciler:
        print(f"Hata: {numara} numaralı öğrenci zaten kayıtlı!")
        return
    ogrenciler[numara] = {
        "ad": ad,
        "notlar": []
    }
    print(f"Öğrenci eklendi: {ad} ({numara})")

def not_ekle(numara: str, ders_notu: float):
    if numara not in ogrenciler:
        print("Hata: Öğrenci bulunamadı!")
        return
    if not (0 <= ders_notu <= 100):
        print("Hata: Not 0 ile 100 arasında olmalıdır!")
        return
    ogrenciler[numara]["notlar"].append(ders_notu)
    print(f"{ogrenciler[numara]['ad']} adlı öğrenciye {ders_notu} notu eklendi.")

def ortalama_hesapla(numara: str) -> float:
    if numara not in ogrenciler or not ogrenciler[numara]["notlar"]:
        return 0.0
    notlar = ogrenciler[numara]["notlar"]
    return sum(notlar) / len(notlar)

def ogrencileri_listele():
    print("\n--- ÖĞRENCİ LİSTESİ ---")
    if not ogrenciler:
        print("Henüz kayıtlı öğrenci yok.")
        return
    for numara, bilgi in ogrenciler.items():
        ort = ortalama_hesapla(numara)
        notlar_str = ", ".join(map(str, bilgi["notlar"])) if bilgi["notlar"] else "Henüz not yok"
        print(f"No: {numara} | İsim: {bilgi['ad']} | Notlar: [{notlar_str}] | Ort: {ort:.2f}")

def main():
    # Örnek test verileri
    ogrenci_ekle("101", "Ali Yılmaz")
    ogrenci_ekle("102", "Ayşe Kaya")
    
    not_ekle("101", 85.0)
    not_ekle("101", 90.0)
    not_ekle("102", 70.0)
    not_ekle("102", 100.0)
    
    ogrencileri_listele()

if __name__ == "__main__":
    main()

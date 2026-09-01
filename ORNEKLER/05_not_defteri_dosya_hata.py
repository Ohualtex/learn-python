"""
Örnek 05: Dosya İşlemleri ve Hata Yönetimi ile Not Defteri Uygulaması

Bu örnekte dosya okuma/yazma (JSON), dosya varlığı kontrolü,
`try-except` ile hata yönetimi ve menülü CLI yapısı gösterilmiştir.
"""

import json
import os
import sys

DOSYA_ADI = "notlar_veritabani.json"


def notlari_yukle(dosya_yolu: str = DOSYA_ADI) -> list:
    """JSON dosyasından notları güvenli şekilde okur."""
    if not os.path.exists(dosya_yolu):
        return []

    try:
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Uyarı: Not dosyası bozuk veya geçersiz JSON formatında. Boş liste başlatılıyor.")
        return []
    except Exception as e:
        print(f"Dosya okuma sırasında beklenmedik bir hata oluştu: {e}")
        return []


def notlari_kaydet(notlar: list, dosya_yolu: str = DOSYA_ADI) -> bool:
    """Not listesini JSON dosyasına güvenli şekilde yazar."""
    try:
        with open(dosya_yolu, "w", encoding="utf-8") as f:
            json.dump(notlar, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Hata: Dosyaya yazma işlemi başarısız oldu: {e}")
        return False


def not_ekle(notlar: list, baslik: str, icerik: str):
    """Yeni bir not oluşturup listeye ekler ve kaydeder."""
    yeni_not = {
        "id": len(notlar) + 1,
        "baslik": baslik.strip(),
        "icerik": icerik.strip()
    }
    notlar.append(yeni_not)
    if notlari_kaydet(notlar):
        print(f"'{baslik}' başlıklı not başarıyla kaydedildi.")


def notlari_listele(notlar: list):
    """Kayıtlı tüm notları ekrana basar."""
    if not notlar:
        print("\nHenüz kaydedilmiş bir not bulunmuyor.")
        return

    print("\n--- KAYITLI NOTLAR ---")
    for n in notlar:
        print(f"[{n['id']}] {n['baslik']}")
        print(f"    İçerik: {n['icerik']}")
    print("-----------------------")


def not_sil(notlar: list, not_id: int) -> bool:
    """Belirtilen ID'ye sahip notu listeden siler."""
    for index, n in enumerate(notlar):
        if n["id"] == not_id:
            silinen = notlar.pop(index)
            # Kalan notların ID'lerini yeniden sırala
            for i, item in enumerate(notlar, start=1):
                item["id"] = i
            notlari_kaydet(notlar)
            print(f"'{silinen['baslik']}' başlıklı not silindi.")
            return True

    print(f"Hata: {not_id} numaralı not bulunamadı!")
    return False


def demo_calistir():
    """Örnek akışını otomatik olarak test eder."""
    test_dosyasi = "test_notlar.json"
    print("=== Not Defteri Demo Modu Başlatılıyor ===")
    notlar = []

    print("\n1. Notlar ekleniyor...")
    not_ekle(notlar, "Alışveriş Listesi", "Süt, Yumurta, Kahve")
    not_ekle(notlar, "Python Çalışma", "OOP ve Dosya Yönetimi tekrar edilecek")
    notlari_kaydet(notlar, test_dosyasi)

    print("\n2. Notlar listeleniyor...")
    notlari_listele(notlar)

    print("\n3. Bir not siliniyor (ID: 1)...")
    not_sil(notlar, 1)

    print("\n4. Güncel liste:")
    notlari_listele(notlar)

    # Test dosyasını temizle
    if os.path.exists(test_dosyasi):
        os.remove(test_dosyasi)
    print("\n=== Demo başarıyla tamamlandı. ===")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        demo_calistir()
        return

    notlar = notlari_yukle()

    while True:
        print("\n--- KİŞİSEL NOT DEFTERİ ---")
        print("1. Notları Listele")
        print("2. Yeni Not Ekle")
        print("3. Not Sil")
        print("4. Demo Testini Çalıştır")
        print("5. Çıkış")

        secim = input("Seçiminiz (1-5): ").strip()

        if secim == "1":
            notlari_listele(notlar)
        elif secim == "2":
            baslik = input("Not Başlığı: ")
            icerik = input("Not İçeriği: ")
            if baslik and icerik:
                not_ekle(notlar, baslik, icerik)
            else:
                print("Uyarı: Başlık veya içerik boş bırakılamaz!")
        elif secim == "3":
            try:
                silinecek_id = int(input("Silinecek Not ID: "))
                not_sil(notlar, silinecek_id)
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı girin!")
        elif secim == "4":
            demo_calistir()
        elif secim == "5":
            print("Programdan çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim, lütfen 1-5 arasında bir değer giriniz.")


if __name__ == "__main__":
    main()

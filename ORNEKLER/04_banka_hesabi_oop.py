"""
Örnek 04: Nesne Yönelimli Programlama (OOP) ile Banka Hesabı Simülasyonu

Bu örnekte sınıf (class), kapsülleme (encapsulation), bakiye kontrolü 
ve metot kullanımı gösterilmiştir.
"""

class BankaHesabi:
    def __init__(self, hesap_sahibi: str, bakiye: float = 0.0):
        self.hesap_sahibi = hesap_sahibi
        self.__bakiye = max(0.0, bakiye) # Kapsüllenmiş gizli bakiye

    def para_yatir(self, miktar: float):
        if miktar <= 0:
            print("Hata: Yatırılacak miktar pozitif olmalıdır!")
            return
        self.__bakiye += miktar
        print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.__bakiye:.2f} TL")

    def para_cek(self, miktar: float) -> bool:
        if miktar <= 0:
            print("Hata: Çekilecek miktar pozitif olmalıdır!")
            return False
        if miktar > self.__bakiye:
            print(f"Hata: Yetersiz bakiye! Mevcut bakiye: {self.__bakiye:.2f} TL")
            return False
        self.__bakiye -= miktar
        print(f"{miktar} TL çekildi. Kalan bakiye: {self.__bakiye:.2f} TL")
        return True

    def bakiye_sorgula(self):
        print(f"Hesap Sahibi: {self.hesap_sahibi} | Bakiye: {self.__bakiye:.2f} TL")

    def __str__(self):
        return f"BankaHesabi({self.hesap_sahibi}, {self.__bakiye:.2f} TL)"


def main():
    hesap = BankaHesabi("Ahmet Yılmaz", 1000.0)
    hesap.bakiye_sorgula()
    
    hesap.para_yatir(500.0)
    hesap.para_cek(200.0)
    hesap.para_cek(2000.0) # Yetersiz bakiye uyarısı verir
    
    print(hesap)

if __name__ == "__main__":
    main()

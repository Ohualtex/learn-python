"""
Örnek 06: OOP Kalıtım (Inheritance), super() ve Çok Biçimlilik (Polymorphism)
ile Personel Yönetim Sistemi

Bu örnekte temel sınıf (Base Class), türetilmiş sınıflar (Subclasses),
`super()` kullanımı, metot ezme (method overriding) ve polimorfizm gösterilmiştir.
"""

from typing import List


class Calisan:
    """Tüm çalışanlar için temel sınıf (Base Class)."""

    def __init__(self, ad: str, soyad: str, maas: float, departman: str = "Genel"):
        self.ad = ad
        self.soyad = soyad
        self.maas = max(0.0, float(maas))
        self.departman = departman

    @property
    def tam_isim(self) -> str:
        return f"{self.ad} {self.soyad}"

    def bilgileri_goster(self):
        print(f"Çalışan: {self.tam_isim} | Departman: {self.departman} | Maaş: {self.maas:.2f} TL")

    def zam_yap(self, yuzde: float):
        """Maaşa yüzde oranında zam uygular."""
        if yuzde > 0:
            artis = self.maas * (yuzde / 100)
            self.maas += artis
            print(f"{self.tam_isim} için %{yuzde} zam uygulandı. Yeni maaş: {self.maas:.2f} TL")
        else:
            print("Hata: Zam oranı pozitif olmalıdır!")

    def maas_hesapla(self) -> float:
        """Net aylık hakedişi döndürür."""
        return self.maas

    def __str__(self):
        return f"[{self.departman}] {self.tam_isim} ({self.maas:.2f} TL)"


class Yazilimci(Calisan):
    """Calisan sınıfından türetilen Yazılımcı sınıfı."""

    def __init__(self, ad: str, soyad: str, maas: float, bildigi_diller: List[str]):
        # Üst sınıfın (Calisan) __init__ metodunu çağırıyoruz
        super().__init__(ad, soyad, maas, departman="Yazılım Geliştirme")
        self.bildigi_diller = bildigi_diller

    # Metot Ezme (Method Overriding)
    def bilgileri_goster(self):
        diller_str = ", ".join(self.bildigi_diller)
        print(f"💻 Yazılımcı: {self.tam_isim} | Diller: [{diller_str}] | Maaş: {self.maas:.2f} TL")

    def kod_yaz(self, proje_adi: str):
        print(f"{self.tam_isim}, '{proje_adi}' projesi için kod yazıyor...")


class Yonetici(Calisan):
    """Calisan sınıfından türetilen Yönetici sınıfı."""

    def __init__(self, ad: str, soyad: str, maas: float, prim_orani: float = 15.0):
        super().__init__(ad, soyad, maas, departman="Yönetim")
        self.prim_orani = prim_orani
        self.yonetilenler: List[Calisan] = []

    def ekip_uyesi_ekle(self, calisan: Calisan):
        if calisan not in self.yonetilenler:
            self.yonetilenler.append(calisan)
            print(f"{calisan.tam_isim}, {self.tam_isim}'in ekibine eklendi.")

    # Metot Ezme (Method Overriding) - Yöneticinin maaşına prim eklenir
    def maas_hesapla(self) -> float:
        prim = self.maas * (self.prim_orani / 100)
        return self.maas + prim

    def bilgileri_goster(self):
        toplam_maas = self.maas_hesapla()
        print(
            f"👔 Yönetici: {self.tam_isim} | Ekip Sayısı: {len(self.yonetilenler)} "
            f"| Taban: {self.maas:.2f} TL | Toplam Hakediş (Primli): {toplam_maas:.2f} TL"
        )


def maas_bordrosu_yazdir(calisanlar: List[Calisan]):
    """
    Polimorfizm (Çok Biçimlilik) Örneği:
    Farklı tiplerdeki (Calisan, Yazilimci, Yonetici) nesneler aynı döngü içinde,
    aynı metot çağrısıyla (`maas_hesapla`) kendi özel hesaplamalarını yapar.
    """
    print("\n" + "=" * 50)
    print("           AYLIK MAAŞ BORDROSU")
    print("=" * 50)

    toplam_butce = 0.0
    for kisi in calisanlar:
        hakedis = kisi.maas_hesapla()
        toplam_butce += hakedis
        print(f"- {kisi.tam_isim:<20} ({kisi.departman:<18}): {hakedis:>10.2f} TL")

    print("-" * 50)
    print(f"Şirket Toplam Maaş Maliyeti: {toplam_butce:.2f} TL")
    print("=" * 50 + "\n")


def main():
    # 1. Nesnelerin Oluşturulması
    yazilimci1 = Yazilimci("Can", "Demir", 35000, ["Python", "Go", "Docker"])
    yazilimci2 = Yazilimci("Elif", "Yıldız", 40000, ["Python", "TypeScript", "React"])
    yonetici1 = Yonetici("Bora", "Öztürk", 55000, prim_orani=20.0)

    # 2. Yöneticiye Ekip Üyeleri Ekleme
    print("--- Ekip Yapılandırması ---")
    yonetici1.ekip_uyesi_ekle(yazilimci1)
    yonetici1.ekip_uyesi_ekle(yazilimci2)

    # 3. Bilgileri Gösterme
    print("\n--- Personel Bilgileri ---")
    yazilimci1.bilgileri_goster()
    yazilimci2.bilgileri_goster()
    yonetici1.bilgileri_goster()

    # 4. İşlemler
    print("\n--- İşlemler ---")
    yazilimci1.kod_yaz("E-Ticaret Backend API")
    yazilimci1.zam_yap(15)

    # 5. Polimorfik Bordro Listeleme
    personel_listesi = [yazilimci1, yazilimci2, yonetici1]
    maas_bordrosu_yazdir(personel_listesi)


if __name__ == "__main__":
    main()

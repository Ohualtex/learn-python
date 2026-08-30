# 08. İleri Seviye Python Kavramları

## Kavramlar

### 1. Magic (Dunder) Metotlar
Başında ve sonunda çift alt çizgi (`__`) bulunan özel metotlara "Dunder" (Double Underscore) veya sihirli metotlar denir. Python'ın yerleşik davranışlarını nesnelerimize kazandırırlar.

- `__str__(self)`: Kullanıcı dostu metin temsili (`print(nesne)` veya `str(nesne)` çağrıldığında çalışır).
- `__repr__(self)`: Geliştiriciye yönelik resmi gösterim (hata ayıklama için).
- `__len__(self)`: `len(nesne)` çağrıldığında dönecek uzunluğu belirler.
- `__eq__(self, diger)`: `nesne1 == nesne2` karşılaştırmasını özelleştirir.

```python
class Kitap:
    def __init__(self, baslik: str, yazar: str, sayfa_sayisi: int):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return f"'{self.baslik}' - {self.yazar}"

    def __len__(self):
        return self.sayfa_sayisi

kitap = Kitap("1984", "George Orwell", 328)
print(kitap)       # '1984' - George Orwell
print(len(kitap))  # 328
```

### 2. Dekoratörler (Decorators - `@`)
Bir fonksiyonun davranışını değiştirmeden veya koduna dokunmadan ona ek özellikler (loglama, süre ölçümü, yetki kontrolü vb.) kazandıran fonksiyon sarmalayıcılardır.

```python
import time

def sure_olc(fonksiyon):
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] çalışma süresi: {bitis - baslangic:.4f} sn")
        return sonuc
    return sarmalayici

@sure_olc
def buyuk_hesaplama():
    toplam = sum(i**2 for i in range(1_000_000))
    return toplam

buyuk_hesaplama()
```

### 3. Üreteçler (Generators) ve `yield`
Tüm veriyi bir anda RAM belleğe yüklemek yerine, ihtiyaç duyuldukça tek tek değer üreten yapılardır. Bellek (Memory) optimizasyonunda hayati öneme sahiptir.

```python
# Normal Liste (1 Milyon sayıyı RAM'de tutar)
# sayilar = [x for x in range(1_000_000)]

# Generator Fonksiyon (Sadece sıradaki sayıyı üretir)
def sayac(maksimum):
    sayi = 1
    while sayi <= maksimum:
        yield sayi
        sayi += 1

for s in sayac(3):
    print(s) # 1, 2, 3
```

---

## Tuzaklar & Sık Yapılan Hatalar

1. **Decorator'da `*args, **kwargs` Unutmak:**
   Dekoratörün içindeki sarmalayıcı fonksiyona `*args, **kwargs` vermezseniz, parametre alan hedef fonksiyonlar çalıştırıldığında `TypeError` alırsınız.

2. **Tüketilen Generator'ı Tekrar Okumaya Çalışmak:**
   Generator'lar bir kez tüketildiğinde (örneğin döngü ile bitirildiğinde) boşalırlar; ikinci kez döngüye sokulduğunda hiçbir değer üretmezler.

---

## Ezber Cümleler / Altın Kurallar

- *"Ekrana basılacak metin için `__str__`, geliştirici detayı için `__repr__` tanımlanır."*
- *"Büyük verilerde belleği şişirmemek için `return` yerine `yield` (Generator) kullanılır."*
- *"Dekoratör, fonksiyonu girdi olarak alıp geliştirilmiş yeni bir fonksiyon döndüren fonksiyondur."*

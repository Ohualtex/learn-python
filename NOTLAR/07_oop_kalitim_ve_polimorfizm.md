# 07. Nesne Yönelimli Programlama (OOP) - Kalıtım ve Çok Biçimlilik

## Kavramlar

### 1. Kalıtım (Inheritance)
Bir sınıfın (türetilmiş / child class), başka bir sınıfın (üst / parent / base class) tüm özelliklerini ve metotlarını miras almasıdır. Kod tekrarını önler ve hiyerarşik yapılar kurmayı sağlar.

```python
class Hayvan:
    def __init__(self, isim: str):
        self.isim = isim

    def beslen(self):
        print(f"{self.isim} besleniyor.")

# Hayvan sınıfından türeyen Kopek sınıfı
class Kopek(Hayvan):
    def havla(self):
        print(f"{self.isim} havlıyor: Hav hav!")

k = Kopek("Karabaş")
k.beslen() # Üst sınıftan miras alındı
k.havla()  # Kendi özel metodu
```

### 2. `super()` Fonksiyonu
Türetilmiş sınıfın `__init__` veya diğer metotları içerisinde, üst sınıfın orijinal metodunu çağırmak için `super()` kullanılır.

```python
class Calisan:
    def __init__(self, ad: str, maas: float):
        self.ad = ad
        self.maas = maas

class Yazilimci(Calisan):
    def __init__(self, ad: str, maas: float, diller: list):
        super().__init__(ad, maas) # Üst sınıfın init metodunu çalıştırır
        self.diller = diller
```

### 3. Metot Ezme (Method Overriding)
Türetilmiş sınıfın, üst sınıftan miras aldığı bir metodu kendi ihtiyacına göre yeniden tanımlamasıdır.

```python
class Kus(Hayvan):
    def beslen(self):
        # Üst sınıftaki beslen metodunu ezdik (override ettik)
        print(f"{self.isim} tohum yiyerek besleniyor.")
```

### 4. Çok Biçimlilik (Polymorphism)
Farklı sınıflara ait nesnelerin aynı isimdeki metodu çağırarak kendi sınıflarına özgü davranışı sergilemesidir.

```python
def hayvan_besle(hayvan_nesnesi: Hayvan):
    hayvan_nesnesi.beslen()

h1 = Hayvan("Kedi")
h2 = Kus("Maviş")

hayvan_besle(h1) # Kedi besleniyor.
hayvan_besle(h2) # Maviş tohum yiyerek besleniyor. (Overridden)
```

### 5. `isinstance()` ve `issubclass()`
- `isinstance(nesne, Sinif)`: Nesnenin o sınıftan (veya üst sınıflarından) üretilip üretilmediğini sorgular.
- `issubclass(AltSinif, UstSinif)`: Bir sınıfın diğerinden türeyip türemediğini sorgular.

```python
print(isinstance(k, Kopek))  # True
print(isinstance(k, Hayvan)) # True (Kopek bir Hayvan'dır)
```

---

## Tuzaklar & Sık Yapılan Hatalar

1. **`super().__init__()` Çağırmayı Unutmak:**
   Alt sınıfta `def __init__(self, ...):` tanımlandığında, eğer `super().__init__(...)` çağrılmazsa üst sınıfın nitelikleri ilklendirilmez ve `AttributeError` alınır.

2. **Gereksiz Derin Kalıtım Hiyerarşisi:**
   Aşırı katmanlı kalıtım ağaçları kodu karmaşıklaştırır. Python'da *"Kompozisyon kalıtımdan evladır"* (Composition over inheritance) prensibi gözetilmelidir (nesneyi miras almak yerine nesne içinde nitelik olarak tutmak).

---

## Ezber Cümleler / Altın Kurallar

- *"Türetilmiş sınıfın `__init__`'inde mutlaka `super().__init__(...)` çağrılmalıdır."*
- *"Alt sınıfta aynı isimde metot yazmak üst sınıfın metodunu ezer (override eder)."*
- *"Aynı metot adının farklı nesnelerde farklı davranması Polimorfizm'dir."*

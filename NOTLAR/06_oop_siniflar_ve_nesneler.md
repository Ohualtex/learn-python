# 06. Nesne Yönelimli Programlama (OOP) - Sınıflar ve Nesneler

## Kavramlar

### Sınıf (`class`) ve Nesne (`object`)
Sınıf, bir nesnenin taslağı (blueprint); nesne ise o taslaktan üretilmiş somut örnektir.

```python
class Araba:
    # Yapıcı Metot (Constructor)
    def __init__(self, marka: str, model: str, hiz: int = 0):
        self.marka = marka
        self.model = model
        self.hiz = hiz

    def hizlan(self, miktar: int):
        self.hiz += miktar
        print(f"{self.marka} {self.model} hızlandı. Yeni hız: {self.hiz} km/s")

# Nesne Üretme
araba1 = Araba("Toyota", "Corolla")
araba1.hizlan(30)
```

### Self Parametresi
`self`, oluşturulan o anki nesnenin kendisine işaret eder. Sınıf içindeki özniteliklere (attributes) ve metotlara erişmek için kullanılır.

### Kapsülleme (Encapsulation) & Gizli Değişkenler
Dışarıdan doğrudan değiştirilmesini istemediğimiz niteliklerin önüne tek alt çizgi `_` (öneri) veya çift alt çizgi `__` (name mangling / gizli) konur.

```python
class Hesap:
    def __init__(self, bakiye: float):
        self.__bakiye = bakiye # Gizli nitelik

    def bakiye_goster(self):
        return self.__bakiye
```

## Tuzaklar & Sık Yapılan Hatalar

1. **Metotlarda `self` Parametresini Unutmak:**
   Unutulduğunda Python `TypeError: method takes X positional arguments but Y was given` hatası fırlatır.
   Sınıf içi metotların ilk parametresi her zaman `self` olmalıdır (`def hizlan(self, miktar):`). Aksi takdirde `TypeError: method takes X positional arguments but Y was given` hatası alınır.

2. **Class Attribute ile Instance Attribute Karıştırmak:**
   `__init__` dışında tanımlanan değişkenler tüm nesneler tarafından paylaşılır. Nesneye özel veriler `__init__` içinde `self.degisken` şeklinde atanmalıdır.

## Ezber Cümleler / Altın Kurallar

- *"Sınıf taslaktır, nesne evdir."*
- *"Sınıf içindeki her metodun ilk parametresi `self`'dir."*
- *"Nesneye özel veriler `self.` ile `__init__` içinde tanımlanır."*

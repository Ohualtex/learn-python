# 03. Fonksiyonlar ve Modüller

## Kavramlar

### Fonksiyon Tanımlama ve Çağırma (`def`)
Tekrarlayan kod bloklarını bir araya getirip tekrar kullanılabilir hale getirmek için `def` anahtar kelimesi kullanılır.

```python
def selamla(isim="Ziyaretçi"):
    return f"Merhaba {isim}!"

print(selamla("Ahmet")) # Merhaba Ahmet!
print(selamla())        # Merhaba Ziyaretçi!
```

### Parametreler: `*args` ve `**kwargs`
Fonksiyona esnek sayıda argüman göndermek gerektiğinde kullanılır:
- `*args`: Değişken sayıda konum tabanlı (positional) argümanı bir `tuple` olarak alır.
- `**kwargs`: Değişken sayıda isimli (keyword) argümanı bir `dict` olarak alır.

```python
def topla(*sayilar):
    return sum(sayilar)

print(topla(1, 2, 3, 4, 5)) # 15
```

### Lambda (Anonim) Fonksiyonlar
Tek satırlık pratik fonksiyonlar tanımlamak için `lambda` kullanılır.

```python
kare_al = lambda x: x ** 2
print(kare_al(4)) # 16
```

### Modül Kullanımı (`import`)
Python'ın dahili kütüphanelerini veya kendi yazdığımız `.py` dosyalarını projemize dahil etmek için `import` kullanılır.

```python
import math
from random import randint

print(math.sqrt(16))     # 4.0
print(randint(1, 10))   # 1 ile 10 arasında rastgele tamsayı
```

## Tuzaklar & Sık Yapılan Hatalar

1. **Varsayılan Parametrelerde Değiştirilebilir (Mutable) Tipler Kullanmak:**
   ```python
   # HATALI: Liste varsayılan değer olarak verilirse tüm çağrılarda aynı liste kullanılır.
   def ekle(eleman, liste=[]):
       liste.append(eleman)
       return liste
   ```
   **Doğrusu:**
   ```python
   def ekle(eleman, liste=None):
       if liste is None:
           liste = []
       liste.append(eleman)
       return liste
   ```

2. **`return` ve `print` Karıştırması:**
   Bir fonksiyon veri döndürmüyorsa varsayılan olarak `None` döndürür. `print()` ekrana basar, `return` değeri çağrıldığı yere iletir.

## Ezber Cümleler / Altın Kurallar

- *"Fonksiyon veri döndürmüyorsa cevabı `None`'dır."*
- *"Varsayılan parametrelere asla boş liste (`[]`) veya sözlük (`{}`) atama; `None` kullan."*

# ✍️ ALIŞTIRMALAR 05: Nesne Yönelimli Programlama (OOP)

Konular kavram, mimari ve tuzak odaklıdır. Her sorunun cevabı **hemen altında gizli** — önce kendin çöz, sonra "Cevap"a tıkla.
Konu anlatımları için → [`NOTLAR/06_oop_siniflar_ve_nesneler.md`](../NOTLAR/06_oop_siniflar_ve_nesneler.md) ve [`NOTLAR/07_oop_kalitim_ve_polimorfizm.md`](../NOTLAR/07_oop_kalitim_ve_polimorfizm.md)

---

**1. Soru** (Sınıf değişkeni vs Örnek değişkeni tuzağı)
```python
class Sepet:
    urunler = []  # Sınıf değişkeni (Class attribute)

    def ekle(self, urun):
        self.urunler.append(urun)

s1 = Sepet()
s2 = Sepet()

s1.ekle("Elma")
s2.ekle("Armut")

print("s1:", s1.urunler)
print("s2:", s2.urunler)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
s1: ['Elma', 'Armut']
s2: ['Elma', 'Armut']
```
**Açıklama:** `urunler = []`, `__init__` dışında tanımlandığı için bir **Sınıf Değişkenidir** (Class Attribute). Sınıftan türetilen tüm nesneler bellekte aynı liste nesnesini paylaşır. Her nesneye özel sepet olması için değişken `__init__` içerisinde `self.urunler = []` şeklinde tanımlanmalıdır.
</details>

---

**2. Soru** (Kapsülleme ve Name Mangling tuzağı)
```python
class Kasa:
    def __init__(self, sifre):
        self.__sifre = sifre

k = Kasa("1234")

try:
    print(k.__sifre)
except AttributeError:
    print("HATA")

print(k._Kasa__sifre)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
HATA
1234
```
**Açıklama:** Python'da başında iki alt çizgi olan değişkenler (`__sifre`) gerçekte tamamen özel/gizli (private) yapılamaz; bunun yerine **Name Mangling** uygulanır. Python bu değişkenin adını otomatik olarak `_SinifAdi__degiskenAdi` (`_Kasa__sifre`) olarak yeniden adlandırır. Bu yüzden `k.__sifre` `AttributeError` verirken `k._Kasa__sifre` doğrudan değeri okur.
</details>

---

**3. Soru** (`super()` ve Method Resolution Order - MRO)
```python
class A:
    def calis(self):
        print("A", end=" ")

class B(A):
    def calis(self):
        super().calis()
        print("B", end=" ")

class C(A):
    def calis(self):
        super().calis()
        print("C", end=" ")

class D(B, C):
    def calis(self):
        super().calis()
        print("D", end=" ")

d = D()
d.calis()
# Konsol çıktısı ne olur?
```
<details><summary>Cevap</summary>

```
A C B D 
```
**Açıklama:** Python'da çoklu kalıtımda (Multiple Inheritance) metodun aranma sırası **C3 Linearization (MRO)** algoritması ile belirlenir (`D.__mro__` sırası: `D -> B -> C -> A -> object`).
`super()` her zaman bir üstteki sınıfı değil, MRO zincirindeki bir sonraki sınıfı çağırır:
1. `D.calis()`, `B.calis()`'i çağırır.
2. `B`'deki `super()`, MRO'da sıradaki `C.calis()`'i çağırır.
3. `C`'deki `super()`, `A.calis()`'i çağırır.
4. `A` `"A "` basar.
5. Çağrı yığını geri çözülürken sırasıyla `"C "`, `"B "` ve `"D "` basılır.
</details>

---

**4. Soru** (Dunder Metotlar: `__str__` vs `__repr__`)
```python
class Nokta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Nokta({self.x}, {self.y})"

p = Nokta(3, 4)
print(str(p))
print([p])
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
Nokta(3, 4)
[Nokta(3, 4)]
```
**Açıklama:**
- Bir sınıfta `__str__` tanımlanmamışsa Python otomatik olarak `__repr__` metoduna geri döner (fallback).
- Koleksiyonlar (liste, sözlük vb.) içindeki nesneleri ekrana basarken her zaman `__repr__` metodunu çağırırlar. Bu nedenle her iki satırda da `Nokta(3, 4)` çıktısı alınır.
</details>

---

**5. Soru** (Polimorfizm ve Duck Typing)
```python
class Kopek:
    def ses_cikar(self):
        return "Hav hav"

class Ordek:
    def ses_cikar(self):
        return "Vak vak"

class Araba:
    def ses_cikar(self):
        return "Düt düt"

def cal(nesneler):
    for n in nesneler:
        print(n.ses_cikar(), end=", ")

cal([Kopek(), Ordek(), Araba()])
# Konsol çıktısı ne olur?
```
<details><summary>Cevap</summary>

```
Hav hav, Vak vak, Düt düt, 
```
**Açıklama:** Python dinamik tipli bir dildir ve **Duck Typing** ("Ördek gibi yürüyorsa ve ördek gibi ses çıkarıyorsa ördektir") felsefesini benimser. Ortak bir kalıtım üst sınıfı olmasa dahi, nesneler aynı isim ve imzaya sahip `ses_cikar()` metoduna sahip olduğu sürece `cal()` fonksiyonu sorunsuz polimorfik olarak çalışır.
</details>

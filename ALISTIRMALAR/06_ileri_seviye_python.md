# ✍️ ALIŞTIRMALAR 06: İleri Seviye Python (Dekoratörler ve Jeneratörler)

Konular kavram, mekanizma ve tuzak odaklıdır. Her sorunun cevabı **hemen altında gizli** — önce kendin çöz, sonra "Cevap"a tıkla.
Konu anlatımı için → [`NOTLAR/08_ileri_seviye_python.md`](../NOTLAR/08_ileri_seviye_python.md)

---

**1. Soru** (Dekoratör zincirleme ve yürütme sırası)
```python
def d1(func):
    def sarmalayici():
        return f"[{func()}]"
    return sarmalayici

def d2(func):
    def sarmalayici():
        return f"<{func()}>"
    return sarmalayici

@d1
@d2
def selam():
    return "merhaba"

print(selam())  # ?
```
<details><summary>Cevap</summary>

`[<merhaba>]`.

**Açıklama:** Dekoratörler **aşağıdan yukarıya (içten dışa)** uygulanır.
1. İlk olarak `d2` uygulanır: `selam = d2(selam)` -> çıktı `<merhaba>` olur.
2. Ardından `d1` uygulanır: `selam = d1(d2(selam))` -> çıktı `[<merhaba>]` olur.
</details>

---

**2. Soru** (`functools.wraps` eksikliğinin getirdiği metaveri kaybı)
```python
def basit_dekorator(f):
    def sarmalayici(*args, **kwargs):
        """Bu sarmalayıcı fonksiyondur."""
        return f(*args, **kwargs)
    return sarmalayici

@basit_dekorator
def kare_al(x):
    """Verilen sayının karesini alır."""
    return x ** 2

print(kare_al.__name__)
print(kare_al.__doc__.strip())
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
sarmalayici
Bu sarmalayıcı fonksiyondur.
```
**Açıklama:** Bir fonksiyon dekore edildiğinde, aslında geriye dönen içteki `sarmalayici` fonksiyonudur. Eğer `functools.wraps(f)` kullanılmazsa, hedef fonksiyonun adı (`__name__`), docstring'i (`__doc__`) ve imza bilgileri sarmalayıcının bilgileriyle ezilir ve kaybolur.
</details>

---

**3. Soru** (Parametreli Dekoratör: 3 Katmanlı Fonksiyon Mimarisi)
```python
def carp(katsayi):
    def dis(f):
        def ic(x):
            return f(x) * katsayi
        return ic
    return dis

@carp(katsayi=3)
def sayi(x):
    return x + 2

print(sayi(4))  # ?
```
<details><summary>Cevap</summary>

`18`.

**Açıklama:** Dekoratörün kendisine argüman göndermek (`@carp(katsayi=3)`), aslında dekoratör üreten bir fabrika fonksiyonu (3 katmanlı closure) oluşturur:
1. `carp(3)` çalışır ve geriye `dis` dekoratörünü döner.
2. `@dis` uygulanarak `sayi` fonksiyonu `ic` ile sarmalanır.
3. `sayi(4)` çağrıldığında `(4 + 2) * 3 = 18` elde edilir.
</details>

---

**4. Soru** (Jeneratörün tek kullanımlık / tüketilebilir olması tuzağı)
```python
def say_bakalim():
    yield 1
    yield 2
    yield 3

gen = say_bakalim()

print("Birinci:", list(gen))
print("İkinci:", list(gen))
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
Birinci: [1, 2, 3]
İkinci: []
```
**Açıklama:** Jeneratörler (Generators) durum bilgisi tutan (stateful) tek yönlü akışlardır (one-time iterators). İlk `list(gen)` çağrısıyla jeneratör tamamen tükenir (`exhausted`). İkinci çağrıda baştan başlamaz, doğrudan boş liste `[]` döner. Yeniden okumak için jeneratör fonksiyonunun tekrar çağrılması gerekir.
</details>

---

**5. Soru** (Jeneratörde `yield` ile ara durum saklama ve `next()`)
```python
def adimlar():
    print("A", end="")
    yield 1
    print("B", end="")
    yield 2
    print("C", end="")

it = adimlar()
print(" Başla -> ", end="")
val1 = next(it)
print(f"[{val1}] -> ", end="")
val2 = next(it)
print(f"[{val2}]")
# Konsol çıktısı ne olur?
```
<details><summary>Cevap</summary>

```
 Başla -> A[1] -> B[2]
```
**Açıklama:** 
1. `it = adimlar()` çağrıldığında fonksiyonun gövdesi hemen çalışmaz; sadece bir generator nesnesi döner.
2. `next(it)` ilk kez çağrıldığında kod ilk `yield` ifadesine kadar koşar: `"A"` basılır ve `1` döner. Fonksiyon bellekte o noktada dondurulur (pause).
3. İkinci `next(it)` çağrıldığında fonksiyon kaldığı yerden devam eder: `"B"` basılır ve `2` döner. `"C"` ise jeneratör bir sonraki `next()` çağrılmadığı sürece asla basılmaz.
</details>

# ✍️ ALIŞTIRMALAR 03: Fonksiyonlar ve Modüller

Konular kavram ve tuzak odaklıdır. Her sorunun cevabı **hemen altında gizli** — önce kendin çöz, sonra "Cevap"a tıkla.
Konu anlatımı için → [`NOTLAR/03_fonksiyonlar_ve_moduller.md`](../NOTLAR/03_fonksiyonlar_ve_moduller.md)

---

**1. Soru** (klasik tuzak: mutable default argument)
```python
def listeye_ekle(eleman, liste=[]):
    liste.append(eleman)
    return liste

print(listeye_ekle(1))
print(listeye_ekle(2))
print(listeye_ekle(3, []))
print(listeye_ekle(4))
# Çıktı (4 satır)?
```
<details><summary>Cevap</summary>

```
[1]
[1, 2]
[3]
[1, 2, 4]
```
Python'da varsayılan argümanlar (`liste=[]`) **fonksiyon tanımlandığı anda (derleme/yükleme anında) bir kez oluşturulur**. Her çağrıda yeni liste oluşturulmaz, aynı liste referansı paylaşılır. 3. çağrıda açıkça `[]` verildiği için yeni liste kullanılır, ancak 4. çağrıda yine varsayılan liste kullanıldığı için `[1, 2, 4]` olur.
</details>

**2. Soru** (`*args` ve `**kwargs` paketleme / açma)
```python
def topla(a, b, *args, carpan=1):
    return (a + b + sum(args)) * carpan

degerler = [2, 3, 4, 5]
print(topla(*degerler, carpan=2))  # ?
```
<details><summary>Cevap</summary>

`28`. `*degerler` listeyi konumsal olarak açar: `a=2`, `b=3`, `args=(4, 5)`. Toplam: `2 + 3 + 4 + 5 = 14`. `carpan=2` ile çarpılınca `14 * 2 = 28`.
</details>

**3. Soru** (Scope: `global` ve `nonlocal` farkı)
```python
x = 10

def dis():
    x = 20
    def ic():
        nonlocal x
        x = 30
    ic()
    print("dis:", x)

dis()
print("global:", x)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
dis: 30
global: 10
```
`nonlocal x`, en yakın kapsayıcı (enclosing) fonksiyondaki `x` değişkenini hedefler (`dis()` içindeki `x=20` olanı `30` yapar). Global `x` ise etkilenmez, `10` kalır.
</details>

**4. Soru** (zor: Lambda & Late Binding / Geç Bağlama Tuzağı)
```python
fonksiyonlar = [lambda x: x + i for i in range(3)]

sonuclar = [f(10) for f in fonksiyonlar]
print(sonuclar)  # ?
```
<details><summary>Cevap</summary>

`[12, 12, 12]`. Python'da closure içindeki değişkenler (`i`) fonksiyon tanımlandığında değil, **çağrıldığında aranır (late binding)**. Döngü bittiğinde `i=2` olduğu için tüm lambda'lar `x + 2` çalıştırır: `10 + 2 = 12`. (Bunu önlemek için: `lambda x, i=i: x + i` varsayılan argüman ile o anki değer kilitlenir).
</details>

**5. Soru** (`return` ve `finally` akışı)
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())  # ?
```
<details><summary>Cevap</summary>

`2`. `try` bloğundaki `return 1` çalışsa bile fonksiyon sonlanmadan önce `finally` bloğu mutlaka devreye girer. `finally` içindeki `return 2`, önceki dönüş değerini ezer.
</details>

**6. Soru** (boşlukları doldur: Decorator şablonu)
```python
def log_decorator(func):
    def wrapper(*(1)__, **__(2)__):
        print(f"{func.__name__} calisiyor...")
        sonuc = func(*(1)__, **__(2)__)
        return sonuc
    return __(3)__
```
<details><summary>Cevap</summary>

(1) `args`  (2) `kwargs`  (3) `wrapper`
Dekoratör, her türlü parametre yapısını karşılamak için `*args, **kwargs` ile sarmalamalı ve iç fonksiyonun referansını (`wrapper`) döndürmelidir.
</details>

**7. Soru** (Parametre aktarımı: Mutable vs Immutable)
```python
def guncelle(sayi, liste, sozluk):
    sayi += 10
    liste.append(99)
    sozluk["durum"] = "aktif"

x = 5
l = [1, 2]
d = {"durum": "pasif"}

guncelle(x, l, d)
print(x, l, d["durum"])  # ?
```
<details><summary>Cevap</summary>

`5 [1, 2, 99] aktif`. Python'da parametreler "pass-by-assignment" ile aktarılır:
- `int` (x) **immutable (değiştirilemez)** olduğundan fonksiyon içi işlem yeni bir yerel nesne üretir, dıştaki `x` değişmez (`5`).
- `list` (l) ve `dict` (d) **mutable (değiştirilebilir)** olduğundan yerinde güncellenir.
</details>

**8. Soru** (`*` ile Keyword-Only Parametreler)
```python
def kaydet(kullanici, *, rol="uye", onay=False):
    return f"{kullanici}-{rol}-{onay}"

# 1) kaydet("Ahmet", "admin", True)  --> Çalışır mı?
# 2) kaydet("Ahmet", rol="admin", onay=True)  --> Çıktı?
```
<details><summary>Cevap</summary>

(1) **TypeError verir.** Tek başına `*` işaretinden sonraki parametreler yalnızca isimle (`rol=...`, `onay=...`) geçilebilir; konumsal olarak geçilemez.
(2) `Ahmet-admin-True`
</details>

**9. Soru** (`__name__` ve Modül Yükleme)
```python
# matematik.py dosyasında:
print(f"Modul calisti: {__name__}")

def kare(n):
    return n * n

# main.py dosyasında:
# import matematik
# print(matematik.kare(4))
# 'python main.py' komutuyla çalıştırıldığında ekrana basılan ilk satır ne olur?
```
<details><summary>Cevap</summary>

`Modul calisti: matematik`. Bir dosya `import` edildiğinde Python o dosyanın kodunu bir kez çalıştırır ve o esnada `__name__` modülün adı (`"matematik"`) olur. Doğrudan `python matematik.py` çalıştırılsaydı `"__main__"` olurdu.
</details>

**10. Soru** (First-Class Functions & Fonksiyon Listesi)
```python
def arti_bir(x): return x + 1
def iki_kat(x): return x * 2
def kare(x): return x ** 2

adimlar = [arti_bir, iki_kat, kare]

deger = 2
for f in adimlar:
    deger = f(deger)

print(deger)  # ?
```
<details><summary>Cevap</summary>

`36`. Adım adım:
1. `arti_bir(2)` = 3
2. `iki_kat(3)` = 6
3. `kare(6)` = **36**.
Python'da fonksiyonlar nesnedir; listelere eklenebilir ve döngüde çağrılabilir.
</details>

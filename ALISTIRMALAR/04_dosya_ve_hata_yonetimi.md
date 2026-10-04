# ✍️ ALIŞTIRMALAR 04: Dosya İşlemleri ve Hata Yönetimi

Konular kavram ve tuzak odaklıdır. Her sorunun cevabı **hemen altında gizli** — önce kendin çöz, sonra "Cevap"a tıkla.
Konu anlatımı için → [`NOTLAR/05_dosya_ve_hata_yonetimi.md`](../NOTLAR/05_dosya_ve_hata_yonetimi.md)

---

**1. Soru** (`try - except - else - finally` akış sırası ve `return` tuzağı)
```python
def test():
    try:
        print("A")
        return 1
    except Exception:
        print("B")
        return 2
    else:
        print("C")
    finally:
        print("D")

sonuc = test()
print("Sonuc:", sonuc)
# Konsol çıktısı ne olur?
```
<details><summary>Cevap</summary>

```
A
D
Sonuc: 1
```
**Açıklama:**
1. `try` bloğu çalışır ve `"A"` yazdırılır.
2. `return 1` çalıştırılmak istenir ancak `finally` bloğu **her halükarda** (fonksiyon return etmeden önce bile) çalışmak zorundadır.
3. Bu nedenle `"D"` yazdırılır.
4. `try` içinde hata çıkmadığı için `except` atlanır. Ancak `try` içinde erken `return` olduğu için `else` bloğu çalışmaz (`else` sadece `try` hatasız tamamlanıp return etmediğinde çalışır).
5. Son olarak saklanan return değeri olan `1` döner.
</details>

---

**2. Soru** (`finally` içinde `return` bulunması durumu)
```python
def gizemli_fonksiyon():
    try:
        return "TRY"
    finally:
        return "FINALLY"

print(gizemli_fonksiyon())  # ?
```
<details><summary>Cevap</summary>

`FINALLY`.

**Açıklama:** `finally` bloğu içindeki bir `return` veya fırlatılan bir `exception`, `try` veya `except` bloğunda bekletilen önceki `return` değerlerini veya istisnaları **ezer (override eder)**. Bu durum hata ayıklamayı zorlaştırdığı için `finally` içinde `return` kullanmaktan kaçınılmalıdır.
</details>

---

**3. Soru** (İstisna yakalama hiyerarşisi sırası)
```python
def bolme(a, b):
    try:
        return a / b
    except ArithmeticError:
        return "Aritmetik Hata"
    except ZeroDivisionError:
        return "Sıfıra Bölme Hatası"

print(bolme(10, 0))  # ?
```
<details><summary>Cevap</summary>

`"Aritmetik Hata"`.

**Açıklama:** Python'da `ZeroDivisionError`, `ArithmeticError` sınıfından türemiştir (`issubclass(ZeroDivisionError, ArithmeticError) == True`). `except` blokları yukarıdan aşağıya doğru ilk eşleşende durduğu için üst sınıflar alt sınıflardan önce yazılırsa alttaki spesifik bloklar asla çalışmaz. Spesifik hatalar daima en üstte yakalanmalıdır.
</details>

---

**4. Soru** (Dosya kipleri: `w` vs `r+` vs `a`)
```python
# 'deneme.txt' içinde önceden '123456789' yazdığı varsayılsın.
with open("deneme.txt", "r+", encoding="utf-8") as f:
    f.write("ABC")

with open("deneme.txt", "r", encoding="utf-8") as f:
    print(f.read())  # ?
```
<details><summary>Cevap</summary>

`ABC456789`.

**Açıklama:**
- `w` kipi dosyayı açtığı anda içeriği sıfırlar (`truncate`).
- `a` kipi imleci daima dosyanın sonuna koyar.
- `r+` kipi ise dosyayı sıfırlamaz, imleç `0.` bayt konumundan başlar ve yazılan karakterler mevcut karakterlerin üzerine yazar (overwrite). `ABC` ilk 3 karakter olan `123`'ün üzerine yazılmış, geriye kalan `456789` korunmuştur.
</details>

---

**5. Soru** (Özel İstisnalar ve Exception Chaining)
```python
class VeriTabaniHatasi(Exception):
    pass

def veri_cek():
    try:
        int("gecersiz_sayi")
    except ValueError as e:
        raise VeriTabaniHatasi("Kayıt okunamadı") from e

try:
    veri_cek()
except VeriTabaniHatasi as h:
    print("Yakalanan:", type(h).__name__)
    print("Kök Neden:", type(h.__cause__).__name__)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
Yakalanan: VeriTabaniHatasi
Kök Neden: ValueError
```
**Açıklama:** `raise YeniHata from eski_hata` sözdizimi, Python'da **Exception Chaining** mekanizmasını tetikler ve orijinal hatayı yeni hatanın `__cause__` niteliğine bağlar. Böylece traceback incelendiğinde hatanın asıl kök nedeni kaybolmaz.
</details>

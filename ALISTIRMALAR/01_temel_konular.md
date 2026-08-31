# ✍️ ALIŞTIRMALAR 01: Temel Konular & Akış Kontrolü

Konular kavram ve tuzak odaklıdır. Her sorunun cevabı **hemen altında gizli** — önce kendin çöz, sonra "Cevap"a tıkla.
Konu anlatımı için → [`NOTLAR/01_giris_ve_degiskenler.md`](../NOTLAR/01_giris_ve_degiskenler.md) & [`NOTLAR/02_akis_kontrolu_ve_donguler.md`](../NOTLAR/02_akis_kontrolu_ve_donguler.md)

---

**1. Soru** (Boolean & Truthiness / Falsy Değerler)
```python
a = []
b = "0"
c = 0
d = None

print(bool(a), bool(b), bool(c), bool(d))
# Çıktı?
```
<details><summary>Cevap</summary>

`False True False False`. Python'da boş veri yapıları (`[]`, `""`, `{}`), `0`, `0.0` ve `None` değeri `False` (falsy) kabul edilir. Ancak `"0"` boş olmayan bir string olduğu için `True` (truthy) döner.
</details>

**2. Soru** (`is` vs `==` & Small Integer Caching)
```python
x = 256
y = 256
print(x == y, x is y)

a = 1000
b = 1000
print(a == b, a is b)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
True True
True False
```
`==` değer eşitliğini, `is` ise nesne kimliğini (bellekte aynı adres / `id`) kontrol eder. CPython -5 ile 256 arasındaki tam sayıları bellekte önceden önbelleğe alır; bu yüzden `x is y` `True` olur, ancak 1000 için ayrı nesneler oluşturulduğundan `a is b` `False` döner.
</details>

**3. Soru** (String Slicing & Adım Parametresi)
```python
s = "PythonProgramlama"
print(s[::2])
print(s[::-1])
print(s[6:1:-1])
# Çıktı (3 satır)?
```
<details><summary>Cevap</summary>

```
PtoPormaa
amalmargorPnohtyP
norty
```
- `s[::2]`: Baştan sona 2'şer atlayarak alır (`PtoPormaa`).
- `s[::-1]`: Metni ters çevirir.
- `s[6:1:-1]`: İndeks 6'dan (`'n'`) başlar, geriye doğru 1'e kadar (1 hariç) gider (`"norty"`).
</details>

**4. Soru** (`for - else` Döngü Mekanizması)
```python
sayilar = [2, 4, 6, 7, 8]

for s in sayilar:
    if s % 2 != 0:
        print("Tek sayı bulundu:", s)
        break
else:
    print("Tüm sayılar çift")
# Çıktı?
```
<details><summary>Cevap</summary>

`Tek sayı bulundu: 7`. Python'da döngünün `else` bloğu, döngü `break` ile kırılmadan normal şekilde tamamlandığında çalışır. Burada `break` çalıştığı için `else` bloğu atlanır.
</details>

**5. Soru** (Ternary Operator & Kısa Devre Değerlendirmesi)
```python
x = 10
y = 0

sonuc = x / y if y != 0 else -1
print(sonuc)

deger = "Varsayilan" or "Alternatif"
bosluk = "" or "Yedek"
print(deger, bosluk)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
-1
Varsayilan Yedek
```
1. satır: `y != 0` False olduğundan `else` kısmı (`-1`) çalışır, `ZeroDivisionError` oluşmaz.
2. satır: `or` operatörü ilk truthy değeri döndürür. `"Varsayilan"` dolu olduğu için doğrudan döner; `""` falsy olduğu için `"Yedek"` döner.
</details>

**6. Soru** (Boşluk Doldurma: `range()` ve negatif adım)
```python
# 10'dan 2'ye kadar (2 dahil) çift sayıları azalan sırada ekrana bas
for i in range(__(1)__, __(2)__, __(3)__):
    print(i, end=" ")
# Beklenen Çıktı: 10 8 6 4 2 
```
<details><summary>Cevap</summary>

(1) `10`  (2) `1` (veya `0`)  (3) `-2`
`range(start, stop, step)`: Stop değeri dahil edilmediği için 2'nin dahil olması adına `stop` en az `1` (veya `0`) olmalıdır.
</details>

**7. Soru** (Döngüde `continue` ve `pass` Farkı)
```python
toplam = 0
for i in range(5):
    if i == 2:
        pass
    if i == 3:
        continue
    toplam += i

print("toplam:", toplam)  # ?
```
<details><summary>Cevap</summary>

`toplam: 7`. Adım adım:
- `i=0` -> toplam=0
- `i=1` -> toplam=1
- `i=2` -> `pass` hiçbir şey yapmaz, toplam=3
- `i=3` -> `continue` adımı atlar (eklenmez)
- `i=4` -> toplam=7
</details>

**8. Soru** (Değişken Değer Değişimi & Tuple Unpacking)
```python
a = 10
b = 20

a, b = b, a + b
print(a, b)  # ?
```
<details><summary>Cevap</summary>

`20 30`. Sağ taraf (`b, a + b`) önce demet (tuple) olarak değerlendirilir: `(20, 10 + 20) = (20, 30)`. Ardından sol tarafa atanır: `a = 20`, `b = 30`.
</details>

**9. Soru** (String İmmutability & Metot Yanılgısı)
```python
metin = "python"
metin.upper()
metin.replace("p", "j")
print(metin)  # ?
```
<details><summary>Cevap</summary>

`python`. String'ler **immutable (değiştirilemez)** olduğundan `upper()` ve `replace()` orijinal metni yerinde değiştirmez; yeni bir string üretip döndürür. Değişkene atanmadığı için `metin` `"python"` olarak kalır.
</details>

**10. Soru** (Float Hassasiyeti Tuzağı)
```python
x = 0.1 + 0.2
print(x == 0.3)
print(round(x, 1) == 0.3)
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
False
True
```
İkili (binary) kayan noktalı sayı aritmetiğinde `0.1 + 0.2` tam olarak `0.3` değil, `0.30000000000000004` olarak saklanır. Bu yüzden doğrudan `==` ile karşılaştırıldığında `False` döner. `round()` veya `math.isclose()` ile kontrol edilmelidir.
</details>

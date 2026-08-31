# ✍️ ALIŞTIRMALAR 02: Veri Yapıları (List, Dict, Set, Tuple)

Konular kavram ve tuzak odaklıdır. Her sorunun cevabı **hemen altında gizli** — önce kendin çöz, sonra "Cevap"a tıkla.
Konu anlatımı için → [`NOTLAR/04_veri_yapilari_list_dict_tuple_set.md`](../NOTLAR/04_veri_yapilari_list_dict_tuple_set.md)

---

**1. Soru** (klasik tuzak: liste çoğaltma ve referans paylaşımı)
```python
matris = [[]] * 3
matris[0].append(1)
print(matris)  # ?
```
<details><summary>Cevap</summary>

`[[1], [1], [1]]`. `* 3` operatörü içteki listeyi kopyalamaz; aynı liste nesnesinin referansını 3 kez çoğaltır. Bu yüzden birine yapılan ekleme hepsine yansır. Doğru yol: `[[] for _ in range(3)]`.
</details>

**2. Soru** (Liste `extend()` vs `append()`)
```python
l1 = [1, 2]
l2 = [3, 4]
l1.append(l2)
l2.extend([5, 6])
print(l1)  # ?
```
<details><summary>Cevap</summary>

`[1, 2, [3, 4, 5, 6]]`. `append(l2)` doğrudan `l2` listesini alt liste referansı olarak ekler. `l2.extend([5, 6])` ile `l2` yerinde genişletildiğinde, `l1` içindeki alt liste referansı da güncellenmiş olur.
</details>

**3. Soru** (Sözlük `get()` ve `setdefault()`)
```python
d = {"a": 1}
x = d.get("b", 0)
y = d.setdefault("c", 2)
print(x, y, d)  # ?
```
<details><summary>Cevap</summary>

`0 2 {'a': 1, 'c': 2}`. `get("b", 0)` anahtar yoksa varsayılan `0` döndürür ancak sözlüğü değiştirmez. `setdefault("c", 2)` ise anahtar yoksa hem `2` döndürür hem de `"c": 2` olarak sözlüğe kaydeder.
</details>

**4. Soru** (Tuple İmmutability & İçteki Değiştirilebilir Nesne)
```python
t = ([1, 2], "python")
t[0].append(3)
# 1) t[0].append(3) çalışır mı?
# 2) t[0] = [1, 2, 3] çalışır mı?
```
<details><summary>Cevap</summary>

(1) **Çalışır.** `t` tuple'ı içindeki referanslar sabittir ancak referans gösterilen listenin içeriği yerinde değiştirilebilir (`t` artık `([1, 2, 3], "python")` olur).
(2) **TypeError verir.** Tuple elemanının referansı başka bir nesneye bağlanamaz.
</details>

**5. Soru** (Set ve Hashability / Küme Elemanı Olabilme Kuralı)
```python
s = set()
s.add((1, 2))
# s.add([3, 4])   --> Hata verir mi? Neden?
# s.add({"a": 1}) --> Hata verir mi? Neden?
```
<details><summary>Cevap</summary>

`(1, 2)` **eklenir** çünkü tuple immutable ve hashable'dır.
`[3, 4]` ve `{"a": 1}` **TypeError (unhashable type: 'list' / 'dict') verir.** Bir nesnenin `set` elemanı veya `dict` anahtarı olabilmesi için `immutable` (değiştirilemez) ve `hashable` (özetlenebilir) olması zorunludur.
</details>

**6. Soru** (Boşluk Doldurma: Slicing ile Eleman Değiştirme)
```python
l = [10, 20, 30, 40, 50]
l[1:4] = __(1)__  # Listeyi [10, 99, 50] yap
print(l)
```
<details><summary>Cevap</summary>

(1) `[99]` (veya `(99,)`)
`l[1:4]` dilimi `[20, 30, 40]` elemanlarını kapsar. Buraya tek elemanlı `[99]` listesi atandığında 3 elemanın yerine tek `99` geçer ve liste `[10, 99, 50]` olur.
</details>

**7. Soru** (List Comprehension vs Generator Expression / Tembel Değerlendirme)
```python
a = [x * 2 for x in range(3)]
b = (x * 2 for x in range(3))

print(type(a), a)
print(type(b), next(b), next(b))
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
<class 'list'> [0, 2, 4]
<class 'generator'> 0 2
```
Köşeli parantez `[...]` list comprehension üretir ve tüm elemanları bellekte anında hesaplayıp saklar. Yay ayraç `(...)` ise generator ifadesidir; elemanları bellekte tutmaz, `next()` ile istendikçe tek tek üretir (lazy evaluation).
</details>

**8. Soru** (Sözlük Anahtarları & Eşitlik / Hash Çakışması)
```python
d = {}
d[1] = "bir"
d[1.0] = "bir nokta sifir"
d[True] = "dogru"

print(len(d))
print(d[1])
# Çıktı (2 satır)?
```
<details><summary>Cevap</summary>

```
1
dogru
```
Python'da `1 == 1.0 == True` eşitliği geçerlidir ve hepsinin hash değeri aynıdır (`hash(1) == hash(1.0) == hash(True) == 1`). Bu yüzden sözlükte aynı anahtar kabul edilirler ve her atama bir önceki değeri ezer. Sonuçta tek bir anahtar (`1`) ve değeri `"dogru"` kalır.
</details>

**9. Soru** (Shallow Copy vs Deep Copy)
```python
import copy

o = [[1, 2], [3, 4]]
s = list(o)        # veya o.copy()
d = copy.deepcopy(o)

o[0].append(99)
print(s[0], d[0])
# Çıktı?
```
<details><summary>Cevap</summary>

`[1, 2, 99] [1, 2]`. `list(o)` veya `.copy()` yüzeysel kopyalama (shallow copy) yapar; içteki alt liste referansları paylaşılır. `copy.deepcopy()` ise iç içe tüm nesneleri sıfırdan kopyalar, bu nedenle `o`'daki değişiklik `d`'yi etkilemez.
</details>

**10. Soru** (Küme Operatörleri: `&`, `|`, `-`, `^`)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)  # Kesişim
print(A - B)  # Fark
print(A ^ B)  # Simetrik Fark
# Çıktı (3 satır)?
```
<details><summary>Cevap</summary>

```
{3, 4}
{1, 2}
{1, 2, 5, 6}
```
- `A & B`: Her ikisinde de ortak olanlar (`{3, 4}`).
- `A - B`: A'da olup B'de olmayanlar (`{1, 2}`).
- `A ^ B`: Yalnızca birinde bulunanlar (kesişim dışındakiler: `{1, 2, 5, 6}`).
</details>

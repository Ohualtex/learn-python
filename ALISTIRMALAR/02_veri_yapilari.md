# Alıştırmalar 02: Veri Yapıları (List, Dict, Set, Tuple)

---

### Soru 1: Benzersiz Elemanlar
Verilen bir listedeki tekrarlayan elemanları temizleyip sonucu alfabetik sıralı bir liste olarak döndüren bir fonksiyon yazınız.

<details>
<summary>Cevabı Göster</summary>

```python
def benzersiz_sirala(liste):
    return sorted(list(set(liste)))

ornek = ["elma", "armut", "elma", "muz", "armut", "çilek"]
print(benzersiz_sirala(ornek)) # ['armut', 'elma', 'muz', 'çilek']
```
</details>

---

### Soru 2: Kelime Sayacı (Frekans Sözlüğü)
Bir cümledeki her kelimenin kaç kez geçtiğini sayan ve bir sözlük olarak döndüren program yazınız.

<details>
<summary>Cevabı Göster</summary>

```python
cumle = "python harika bir dil python öğrenmek çok eğlenceli"
kelimeler = cumle.split()
sayac = {}

for kelime in kelimeler:
    sayac[kelime] = sayac.get(kelime, 0) + 1

print(sayac)
# {'python': 2, 'harika': 1, 'bir': 1, 'dil': 1, 'öğrenmek': 1, 'çok': 1, 'eğlenceli': 1}
```
</details>

# Alıştırmalar 01: Temel Konular & Akış Kontrolü

Bu bölümde Değişkenler, Koşullu İfadeler ve Döngüler ile ilgili pratik sorular bulunmaktadır.

---

### Soru 1: Çift Sayı Toplamı
1'den 100'e kadar olan çift sayıların toplamını bulan bir Python programı yazınız.

<details>
<summary>Cevabı Göster</summary>

```python
toplam = 0
for i in range(2, 101, 2):
    toplam += i

print("1-100 arası çift sayıların toplamı:", toplam) # 2550
```
</details>

---

### Soru 2: Faktöriyel Hesabı
Kullanıcıdan alınan pozitif bir tamsayının faktöriyelini hesaplayan bir program yazınız.

<details>
<summary>Cevabı Göster</summary>

```python
sayi = int(input("Bir sayı girin: "))
faktoriyel = 1

if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
else:
    for i in range(1, sayi + 1):
        faktoriyel *= i
    print(f"{sayi}! = {faktoriyel}")
```
</details>

---

### Soru 3: Asal Sayı Kontrolü
Girilen bir sayının asal sayı olup olmadığını kontrol eden bir fonksiyon yazınız.

<details>
<summary>Cevabı Göster</summary>

```python
def asal_mi(sayi):
    if sayi <= 1:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

print(asal_mi(17)) # True
print(asal_mi(20)) # False
```
</details>

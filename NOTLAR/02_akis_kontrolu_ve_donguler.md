# 02. Akış Kontrolü ve Döngüler

## Kavramlar

### If - Elif - Else
Python'da koşullu ifadeler `if`, `elif` (else if kısaltması) ve `else` ile kontrol edilir. Şartın sonuna her zaman iki nokta üst üste (`:`) konur ve alt satırdan girinti (indentation) ile devam edilir.

```python
yas = 20

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
elif yas == 17:
    print("Sadece bir senen kaldı.")
else:
    print("Henüz reşit değilsiniz.")
```

### For Döngüsü ve `range()`
Bir dizinin (liste, metin vb.) veya belirli bir aralığın üzerinde gezinmek için kullanılır.

```python
# 0'dan 4'e kadar (5 dahil değil) sayar
for i in range(5):
    print(i)

# Bir liste içinde gezinmek
isimler = ["Ali", "Ayşe", "Veli"]
for isim in isimler:
    print(isim)
```

### While Döngüsü
Koşul `True` olduğu sürece çalışmaya devam eder. Sonsuz döngülere girmemek için koşulu değiştiren bir işlem yapıldığından emin olunmalıdır.

```python
sayac = 0
while sayac < 3:
    print(sayac)
    sayac += 1
```

---

## Tuzaklar (Sık Yapılan Hatalar)

### 1. `else if` Tuzağı
Birçok dilde var olan `else if` kalıbı Python'da **yoktur**. Bunun yerine her zaman `elif` kullanılmalıdır. Aksi halde hata alırsınız.

### 2. Artırma/Azaltma Operatörü (`++` / `--`) Tuzağı
Python'da `sayac++` veya `sayac--` gibi operatörler bulunmaz. Değeri 1 artırmak için `sayac += 1` kullanmak zorundasınız.

```python
sayi = 10
# sayi++  # HATA!
sayi += 1 # DOĞRU
```

### 3. İndeksle Uğraşma Tuzağı
Diğer dillerde bir listede gezerken genellikle `for(int i=0; i<uzunluk; i++)` tarzı kod yazılır. Python'da `for i in range(len(liste)):` yazmak çoğu zaman "kötü" (pythonic olmayan) bir koddur. Eğer elemanın kendisine ihtiyacınız varsa doğrudan `for eleman in liste:` şeklinde döngü kurmalısınız.

---

## Ezber Cümlesi
> "Python'da `else if` yerine `elif`, `i++` yerine `i += 1` kullanılır!"

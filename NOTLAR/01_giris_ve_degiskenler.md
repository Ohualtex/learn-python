# 01. Python'a Giriş, Değişkenler ve Veri Tipleri

## Kavramlar

### Python Felsefesi
Python, sadeliği ve okunabilirliği merkezine alan bir dildir. Kod yazarken karmaşıklıktan kaçınmak ve diğer yazılımcıların kolayca okuyabileceği "temiz kod" (clean code) yazmak ana hedeftir.

### Değişken Tanımlama (Dinamik Türleme)
Python'da bir değişken oluştururken veri tipini (`int`, `String` vb.) belirtmenize gerek yoktur. Değer atandığı anda Python tipi kendi anlar.

```python
isim = "Ahmet"      # str (Metin)
yas = 25            # int (Tam sayı)
boy = 1.75          # float (Ondalıklı sayı)
ogrenci_mi = True   # bool (Mantıksal - Doğru/Yanlış)
```

### Temel Giriş / Çıkış İşlemleri
Ekrana bir şey yazdırmak için `print()`, kullanıcıdan veri almak için `input()` fonksiyonları kullanılır.

```python
ad = input("Lütfen adınızı girin: ")
# f-string (formatlanmış metin) kullanımı Python'da çok popülerdir:
print(f"Hoş geldin {ad}!") 
```

---

## Tuzaklar (Sık Yapılan Hatalar)

### 1. Indentation (Girinti) Tuzağı
Diğer dillerde (Java, C, C# vb.) kod bloklarını ayırmak için süslü parantez `{}` kullanılır. Python'da ise bu işlem **boşluklar (girintiler)** ile yapılır.
Aynı seviyede olması gereken kodlar tam olarak aynı hizada olmalıdır (genellikle 4 boşluk veya 1 Tab, fakat ikisi aynı dosyada karıştırılmamalıdır).

```python
# YANLIŞ KULLANIM (IndentationError verir)
if yas > 18:
print("Reşitsiniz")

# DOĞRU KULLANIM
if yas > 18:
    print("Reşitsiniz")
```

### 2. Tip Dönüşümü Tuzağı
`input()` fonksiyonu kullanıcıdan aldığı veriyi her zaman **`string` (metin)** olarak kabul eder. Eğer sayılarla matematiksel bir işlem yapacaksanız, önce tür dönüşümü (casting) yapmalısınız.

```python
# TUZAK: Kullanıcı 10 girerse, sonuc "105" olur (metin birleştirme yapar)
sayi = input("Bir sayı girin: ")
sonuc = sayi + 5  # HATA VERİR (str ile int toplanamaz)

# DOĞRU:
sayi = int(input("Bir sayı girin: "))
sonuc = sayi + 5
```

### 3. Boolean Harf Tuzağı
Java veya C dillerinden gelenler mantıksal değerleri `true` veya `false` olarak küçük harfle yazmaya alışkındır. Python bunu kabul etmez. Baş harfler her zaman büyük olmalıdır.

```python
# YANLIŞ:
durum = true

# DOĞRU:
durum = True
```

---

## Ezber Cümlesi
> "Python'da noktalı virgül (;) ve süslü parantez ({}) aranmaz; kodun çalışması için hizalamaya (girintiye) sadık kalınır!"

# 04. Veri Yapıları: Listeler, Sözlükler, Demetler ve Kümeler

## Kavramlar

### 1. Liste (`list`)
Sıralı, değiştirilebilir (mutable) ve tekrarlanan elemanlara izin veren veri yapısıdır.

```python
meyveler = ["elma", "muz", "çilek"]
meyveler.append("portakal")
meyveler[0] = "armut" # Değiştirilebilir
```

### 2. Demet (`tuple`)
Sıralı fakat değiştirilemez (immutable) veri yapısıdır. `list`'e göre daha hafiftir ve sabittir.

```python
koordinat = (41.0082, 28.9784)
# koordinat[0] = 40.0 # TypeError! Değiştirilemez.
```

### 3. Sözlük (`dict`)
Anahtar-Değer (Key-Value) çiftleriyle çalışan, çok hızlı erişim sağlayan veri yapısıdır.

```python
ogrenci = {"ad": "Ali", "numara": 101, "notlar": [85, 90]}
print(ogrenci["ad"])       # Ali
print(ogrenci.get("yas"))  # None (Hata vermez, güvenli erişim)
```

### 4. Küme (`set`)
Sırasız ve benzersiz (unique) elemanlardan oluşur. Kümeler matematikteki küme işlemlerini (kesişim, birleşim vb.) destekler.

```python
sayilar = {1, 2, 3, 3, 2, 1}
print(sayilar) # {1, 2, 3} (Tekrarlar silinir)
```

### List Comprehension (Pratik Liste Oluşturma)
```python
kareler = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
# Sözdizimi: [ifadeler for eleman in liste if kosul]
```

## Tuzaklar & Sık Yapılan Hatalar

1. **Sözlükten Olmayan Key Okumak (`KeyError`):**
   `sozluk["olmayan_key"]` hata fırlatır. Bunun yerine `sozluk.get("olmayan_key", varsayilan_deger)` kullanılmalıdır.

2. **Liste Kopyalama Hatası (Referans Ataması):**
   ```python
   a = [1, 2, 3]
   b = a # b ile a aynı listeyi gösterir!
   b.append(4)
   print(a) # [1, 2, 3, 4] -> a da değişti!
   ```
   **Doğrusu:** `b = a.copy()` veya `b = a[:]`

## Ezber Cümleler / Altın Kurallar

- *"Köşeli parantez `[]` Liste, Normal parantez `()` Tuple, Süslü parantez `{}` Sözlük veya Kümeydir."*
- *"Sözlükten değer okurken `[]` değil `.get()` kullan ki program çökmesin."*
- *"Tekrarlayan elemanları temizlemenin en hızlı yolu `list(set(dizi))` yapmaktır."*

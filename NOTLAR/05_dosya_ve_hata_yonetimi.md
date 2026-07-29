# 05. Dosya İşlemleri ve Hata Yönetimi

## Kavramlar

### Hata Yönetimi (`try - except - else - finally`)
Programın beklenmedik durumlarda çökmesini engellemek için kullanılır.

```python
try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 10 / sayi
except ValueError:
    print("Geçerli bir sayı girmediniz!")
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
else:
    print("İşlem başarılı, sonuç:", sonuc)
finally:
    print("İşlem tamamlandı (Hata olsa da olmasa da çalışır).")
```

### Dosya Okuma ve Yazma (`with open`)
Dosyaları açarken `with` bloğu kullanmak, işlem bittiğinde dosyanın otomatik kapanmasını sağlar (`close()` çağırmaya gerek kalmaz).

```python
# Dosyaya Yazma ('w' modu sıfırlar, 'a' modu sonuna ekler)
with open("notlar.txt", "w", encoding="utf-8") as f:
    f.write("Python ile dosya işlemleri\n")

# Dosyadan Okuma
with open("notlar.txt", "r", encoding="utf-8") as f:
    icerik = f.read()
    print(icerik)
```

## Tuzaklar & Sık Yapılan Hatalar

1. **Çıplak `except:` Kullanımı:**
   ```python
   # HATALI: Tüm hataları (Ctrl+C durdurması dahil) yakalar ve hatanın sebebini gizler.
   try:
       islem()
   except:
       print("Bir hata oldu")
   ```
   **Doğrusu:** Her zaman spesifik hata türü belirtilmelidir (`except ValueError:` gibi).

2. **Dosya Açarken `encoding="utf-8"` Unutmak:**
   Windows ortamında Türkçe karakterler (`ş, ğ, ı, İ, ç, ö`) okunurken veya yazılırken karakter bozulmalarına yol açar.

## Ezber Cümleler / Altın Kurallar

- *"Dosya açıyorsan her zaman `with open(..., encoding='utf-8')` kullan."*
- *"Asla tek başına `except:` yazma; ne hatası yakaladığını açıkça belirt."*

- *'Dosya kiplerinde `w` dosyayı sıfırlar, var olan veriyi korumak için `a` (append) kullan.'*
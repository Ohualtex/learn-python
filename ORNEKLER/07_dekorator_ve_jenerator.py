"""
Örnek 07: Dekoratörler (Decorators) ve Jeneratörler (Generators)

Bu örnekte:
1. `functools.wraps` ile parametreli ve parametresiz dekoratör mantığı (@zaman_olcer, @loglayici)
2. `yield` anahtar kelimesi ile bellek dostu (lazy evaluation) jeneratör fonksiyonları
3. Jeneratör ifadesi ile liste üreteci arasındaki bellek (RAM) farkı gösterilmiştir.
"""

import functools
import sys
import time
from typing import Any, Callable, Generator


# ============================================================================
# 1. DEKORATÖRLER (DECORATORS)
# ============================================================================

def zaman_olcer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyonun çalışma süresini milisaniye cinsinden ölçen dekoratör."""

    @functools.wraps(func)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        sure_ms = (bitis - baslangic) * 1000
        print(f"⏱️  [{func.__name__}] {sure_ms:.3f} ms sürdü.")
        return sonuc

    return sarmalayici


def loglayici(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyon çağrısını, aldığı argümanları ve dönüş değerini konsola loglayan dekoratör."""

    @functools.wraps(func)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        imza = ", ".join(args_repr + kwargs_repr)
        print(f"📝 [LOG] Çağrılıyor: {func.__name__}({imza})")
        
        sonuc = func(*args, **kwargs)
        print(f"📝 [LOG] {func.__name__} döndürdü: {sonuc!r}")
        return sonuc

    return sarmalayici


# ============================================================================
# 2. JENERATÖRLER (GENERATORS & LAZY EVALUATION)
# ============================================================================

def buyuk_veri_akisi(adet: int) -> Generator[dict, None, None]:
    """
    Bellekte milyonlarca satır tutmak yerine her seferinde tek bir
    kayıt üreten (yield) bellek dostu jeneratör fonksiyonu.
    """
    for i in range(1, adet + 1):
        yield {
            "id": i,
            "veri": f"Kayit_{i}",
            "kare": i ** 2
        }


def fibonacci_jenerator(limit: int) -> Generator[int, None, None]:
    """Belirli bir sınıra kadar Fibonacci sayıları üreten jeneratör."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


# ============================================================================
# 3. UYGULAMA VE KARŞILAŞTIRMA
# ============================================================================

@zaman_olcer
@loglayici
def sayi_topla(a: int, b: int, carpan: int = 1) -> int:
    """Dekoratör zincirleme örneği."""
    time.sleep(0.05)  # İşlem simülasyonu
    return (a + b) * carpan


@zaman_olcer
def liste_ile_uret(adet: int) -> int:
    """Tüm veriyi belleğe (RAM) liste olarak alır."""
    veri_listesi = [x ** 2 for x in range(adet)]
    return len(veri_listesi)


@zaman_olcer
def jenerator_ile_tuket(adet: int) -> int:
    """Veriyi belleğe almadan tek tek (lazy) tüketir."""
    jenerator_ifadesi = (x ** 2 for x in range(adet))
    sayac = sum(1 for _ in jenerator_ifadesi)
    return sayac


def main():
    print("=" * 60)
    print("1. Dekoratör Zincirleme Örneği:")
    print("=" * 60)
    sonuc = sayi_topla(15, 25, carpan=3)
    print(f"Nihai Sonuç: {sonuc}\n")

    print("=" * 60)
    print("2. Jeneratör (yield) ile Fibonacci Üretimi:")
    print("=" * 60)
    print("100'e kadar olan Fibonacci sayıları:")
    for fib in fibonacci_jenerator(100):
        print(fib, end=" ")
    print("\n")

    print("=" * 60)
    print("3. Bellek (RAM) ve Performans Karşılaştırması:")
    print("=" * 60)
    eleman_sayisi = 1_000_000

    # Bellek tüketim ölçümü
    liste = [x for x in range(eleman_sayisi)]
    jenerator = (x for x in range(eleman_sayisi))

    print(f"{eleman_sayisi:,} Eleman İçin Bellek Kullanımı:")
    print(f"👉 Liste boyutu:       {sys.getsizeof(liste):>10,} bayt (~{sys.getsizeof(liste)/(1024*1024):.2f} MB)")
    print(f"👉 Jeneratör boyutu:   {sys.getsizeof(jenerator):>10,} bayt (~{sys.getsizeof(jenerator)/1024:.2f} KB)")
    print("Fark: Jeneratör sadece üretici kuralı tutar, tüm veriyi RAM'e doldurmaz!\n")

    print("İşlem Süreleri Ölçülüyor:")
    liste_ile_uret(eleman_sayisi)
    jenerator_ile_tuket(eleman_sayisi)
    print("=" * 60)


if __name__ == "__main__":
    main()

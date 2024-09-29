s={"bir":1,"iki":2,"üç":3,"dört":4}
s.get("bir","bulunamadı")

print(s.get("bir"))        # bir kelimesine tanımladığımız rakamı verir

print(s.get("beş","bulunamadı"))  # bulunamadı diye ekleme yaparsak girilen değer yoksa o cevabı verir.

s.pop("üç")         # üç anahtarını sözlükten silmiş olduk.
print(s)

print(s.keys())     # sözlüğümüzdeki anahtar kelimeleri bize verir.

print(s.values())    # sözlükteki değerleri bize verir.

print(s["iki"])       # anahtar kelimenin değerini verir.

print(s.items())    # fonksiyonu kurduğumuz haliyle bize verir.






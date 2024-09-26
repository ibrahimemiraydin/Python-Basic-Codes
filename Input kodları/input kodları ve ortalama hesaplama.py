#input komutunu öğrenelim

isim=(str(input("Ad Soyad giriniz:")))         # input komutu kullanıcıların veri girmesini sağlar.
print("Girilen isim -->",isim)
print(type(isim))

yaş=(int(input("Yaşınızı giriniz:")))     # input komutuna girilen değeri int'e çevirmek için inputtan önce int kodunu ekliyoruz.
print("Girilen yaş -->",yaş)
print(type(yaş))

print("Bir numara giriniz", end=("..:"))    # Burdaki end komutu input girişini normalde bir alt satırdan yapmamız gerekirken aynı satırdan değer girmeyi sağlar.
numara=input()

Y1=int(input("1. Yazılı notu:"))            # Ortalama hesaplama uygulaması
Y2=int(input("2. Yazılı notu"))
Ortalama=(Y1+Y2)/2
print("Ortalamanız:", Ortalama)
if Ortalama>=50:
    print("Başarılı")
else:
    print("Başarısız")
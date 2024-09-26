# sonsuz döngü oluşturmak için "while True" komutu kullanılır.
# sonsuz döngüden çıkman için ise "break" kodu kullanılır.

print("Çıkmak için 0 yazınız")
while True:
    d=int(input("Sayı giriniz:"))
    print("Karesi=",d*d)
    if (d==0):
        break    # döngüden çıkış

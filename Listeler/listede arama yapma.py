
L=[1,2,3,4,5,6,7,8]

a=1 in L
print(a)

b=10 in L
print(b)

c=15 not in L
print(c)

deger=int(input("Sayı giriniz:"))       #aranan değeri bulma
if deger in L:
    indis=L.index(deger)
    print("Aranan index",indis,"index değerinde bulundu")
else:
    print("Değer Bulunamadı")


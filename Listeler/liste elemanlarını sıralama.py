#sıralama için "sort" kullanılır

L=[12,24,345,434,512,99,10]
L.sort()
print(L)

L=L[::-1]       # ters çevirip büyükten küçüğe yaptık.
print(L)

#Uygulama

liste=[]
for a in range (0,6):
    sayi=int(input("Sayı giriniz:"))
    liste.append(sayi)

liste.sort()
print("Listenin medyanı=",(liste[2]+liste[3])/2)
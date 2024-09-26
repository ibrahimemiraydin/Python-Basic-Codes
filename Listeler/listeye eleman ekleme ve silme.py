#appent komutu ile listeye yeni bir değer ekliyoruz.
#remove ile listeden eleman silebiliriz.
L=[1,2,3,4,5,6]

L.append(7)         # 7 değerini listeye eklemiş olduk
L.append(8)
L.append(9)
L.insert(2,10)
print(L)

L.remove(2)         # remove fonksiyonu ile silebiliriz.
print(L)
L.remove(1)
print(L)

L.pop(1)        #1. index'tekini siler
print(L)

L.clear()          # tamamını siler
print(L)

liste=[]
for a in range(0,5):
    sayi=int(input("Sayı gir:"))
    liste.append(sayi)

for a in range(0,5):
    print("liste[",a,"]",liste[a])


liste=[10,24,23,132,54,87]
a=min(liste)    # en küçük değeri gösterir.
print(a)
b=max(liste)    # en büyük değeri gösterir.
print(b)


l=[]
topla=0
for i in range(0,5):
    sayi=int(input("Sayı giriniz:"))
    l.append(sayi)
    topla+=sayi
print("En küçük ve en büyük sayıların toplamı=",max(l)+min(l))

print("aritmetik ortalama=",topla/len(l))




l=[1,2,3,4,5,6]
a=l[::-1]
print(a)        # ters çevirip a'ya eşitlemek listeyi sadece print a'yaptığımzda ters gösterir.
print(l)        # l'yi gösterdiğimizde listenin aslında ters olmadığını görüyoruz.
    
l.reverse()     #bunun yerine reverse ile ters çevirdiğimizde listeyi tekrar yazdırıp listenin ters çevrildiğini görüyoruz.
print(l)

b=l[::-2]       #ters çevirip 2'şer 2'şer aldı.
print(b)
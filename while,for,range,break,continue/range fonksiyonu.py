# istenilen aralıkta sayı dizisi oluşturmak için kullanılır.
# ayrıca for fonksiyonunda tekrar sayısını belirmek içinde kullanılır.

range(5)  # 0,1,2,3,4     0'dan 4'e kadar sayıları alır. 5 Dahil değil

range(1,9,2)  # 1,3,5,7,   1'den 9'a kadar 2şer 2şer alır. 9 Dahil olmaz.

range(10,3,-2)  # 10,8,6     10 dan geriye 2şer eksilterek verir.

for a in range(1,5):            # 1,2,3,4 sayıları alınır.
    print(a)

for b in range (12,3,-3):       # 12,9,6     12 ilk sayı olur 3 eksilterek alır. 3 Dahil olmaz.
    print(b)

for c in range(1,10,2):         # 1,3,5,7,9
    print(c)


for d in [0,1,2,3,9]:        # range komutu olmasaydıda bu şekilde sayıları yazdırabilirdik.
    print(d)

e=list (range(12,3,-3))
print(e)


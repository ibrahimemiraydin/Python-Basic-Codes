#kümeler
K={1,"hg","*",325}

print(K)

K=set("emir123")        #yeni elemanlar ekledik ve küme değişti.

print(K)

print(type(K))

k1={1,2,3,4,5}          # 1 , 3 ve 5 ortak
k2={1,3,5,7,9}
print(k1|k2)            # birleşim kümesi , elemanları ortak olsada 1 kere yazılır.

print(k1&k2)            # & işareti ile kesişen elemanları (ortak) gösterir.


#birbirinde olmayan değerleri öğrenmek için kullanılır.
print(k1-k2)            # k1'in k2'den farkı
print(k2-k1)            # k2'nin k1'den farkı



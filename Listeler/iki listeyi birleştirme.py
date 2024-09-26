l1=[1,2,3,4]
l2=[5,6,7,8]
l3=l1+l2

print(l3)       # l3'de birleştirdik.

print(l1+l2)    #l2 ile l1i birleştirdik

l1.extend(l2)   # l2'yi l1'e ekledik
print(l1)

l2.extend(l1)   # l2'nin üstüne l2'yi birdaha ekledik.
print(l2)
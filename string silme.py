yazi="python"
print(yazi[:-1])    # sondan bir index'i silindi.


metin="Merhaba Dünya"
print(metin)
for x in range (1,13):
    print(metin[:-x])

for x in range (13,0,-1):   # baştan eksilterek başlar ve metni tamamlar.
    print(metin[:-x])

print(metin)


#stringleri bölme

s="python"

print(s[3:])    #  s[3:] komutu ile 3. indexten sonrasını bize vermiş oldu.

print(s[:3])    #   ilk 3 indexi alır

print(s[1:5])   #   1. index'ten 4'e kadar alır. 5 dahil değildir

print(s[1::2])  #   1. index'ten başlayıp 2'şer 2şer alır.

print(s[1:6:3]) #   1.index'ten 6.cıya kadar 2şer 2şer al.

print(s[::-1])  #   tersten yazma

s2=s[:3] + "t" + s[4:]  # h'yi t ye çevirme
print(s2)
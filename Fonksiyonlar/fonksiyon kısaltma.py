#lambda

def dolar(TL):             # def dolar üzerinde fonksiyon tanımladık.
    return(TL/34)

dolar=lambda TL: TL/34    # yukardaki fonksiyonla aynı şeydir.

TL=int(input("Türk Lirası Giriniz:"))
print(TL,"Türk Lirası=",dolar(TL) ,"Dolar")

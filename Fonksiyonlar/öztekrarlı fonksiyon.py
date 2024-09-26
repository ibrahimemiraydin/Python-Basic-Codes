# bir fonksiyonun içinde yine aynı fonksiyonu çağırmaya öztekrarlı fonksiyon adı verilir

def ustel(a,b):
    if b == 0:
        return 1
    else:
        return a*ustel(a,b-1)   # örnek 2 üzeri 4 için = 2*2*2*2*1


a=int(input("Taban değerini giriniz:"))
b=int(input("Üs Değerini Giriniz:"))
print(ustel(a,b))
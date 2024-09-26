# muayeneye gelen tc'leri ile kayıt olanların olduğu bir uygulama
L=[]
while True:
    TC=int(input("TC numarası giriniz:"))
    if TC in L:
        i=L.index(TC)
        print("Muayene sırası:",i+1)
    elif TC==0:
        print(L[0],"TC nolu hasta doktorun odasına girebilir.")
        L.pop(0)
    else:
        L.append(TC)
        print("TC nolu hasta sıraya alındı.")

    
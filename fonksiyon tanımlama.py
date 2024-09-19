# fonksiyon tanımlamak için def kullanılır

def topla():    #fonksiyonumuz topla().                  
    print("toplama işlemi.")
    print("örneğin 5 + 7 = 13")

topla()

def selamlama(isim):
    print("Sayın",isim,"restoranımıza hoşgeldiniz.")
while True:
    ad=input("İsminiz nedir?")
    if (ad=="dur"):
        break
    selamlama(ad)
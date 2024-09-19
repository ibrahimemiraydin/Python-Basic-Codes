#fonksiyonun çıktılarını return() komutuyla erişiriz.

def alan(u,g):
    A=u*g
    return A
def cevre(u,g):
    C=2*(u+g)
    return C
    

u=int(input("Dikdörtgenin uzun kenar değeri:"))
g=int(input("Dikdörtgenin kısa kenar değeri:"))
print("Diktörgenin Alanı=",alan(u,g) ,"m2")
print("Diktörgenin Çevresi=",cevre(u,g),"metre")


# Loop in python

# "for" ve "while" olmak üzere 2 adet kodumuz var.
# "for" döngü sayısı önceden bilinir
# "while" ise döngü sayısı koşula bağlıdır.

 

# list, içinde birden çok değişken tutabilir.
# in ve not in  kodu listenin içinde olup omladığını sorgulamak için kullanılır 


liste=["ali","can","mehmet","emir"]
print("ali" in liste)       # ali listedemi ? demek gibi birşey cevap evet olduğu için true yanıtını alacagız.

masano=0
rezerveisim=input("Rezarvasyon ismini giriniz:")
if rezerveisim=="ali":
    masano=1
if rezerveisim=="can":
    masano=2
if rezerveisim=="mehmet":
    masano=3
if rezerveisim=="emir":
    masano=4

if rezerveisim in liste:
    print(masano,"numaralı masa size aittir.")
if rezerveisim not in liste:
    print("Rezervasyon bulunamamıştır.")
#Python Eğitimine Giriş

print("Hello World")    # Print yazdırma komutunun içine (" ") şekildeki gibi yazı yazdırılabilir. class'ı "str"'dir yani yazı türüdür açılımı "string"ten gelir. 

print("P","y")          # Bu şekilde yazarak "," sayesinde iki harfin arasında boşluk bırakmış olduk.
print("P","y",sep="5")  # sep komutu boşlukların arasına istediğimiz str değeri girmemizi sağlar
print("Hello\nWorld")   # \n kodu new line anlamına gelir ve bir satır aşağıya geçer
print("P\tY")           # \t kodu bir tab'lık boşluk bırakır.
print(" ___\n/* *\\\n \\./")   # \n kodu ile köpek simgesi " \ "bu şekli göstermek için "\\"" şeklinde yazılmalıdır.
print(" /\n/\\/\n\\/\\\n \\")  # \n kodu ile balık simgesi

# int = Tam sayı 
# float = Ondalık sayı  
# bool = Doğru Yanlış 
# str = Yazı , karakter      type komutu ile bir verinin clasını öğrenebiliriz

print(type("Hello World"))   


print( 2+2 )            # Bu şekilde sayısal verilere matematiksel işlemler yaptıralabilir.



a=5+5                   
b=7+7
print(a+b)            # a ve b değişkenlerine değer atanarak print komutu ile işlemler yaptırılabilir.

print(a, "+",  b, "=", a+b )   # Print'te komutu görsel olarak göstermek gibi değerleri ekrana yazdırmış olduk.

print(a*(b+b))          #  Matematikteki öncelik kuralları uygulaması

x=(2**2+3/5)/(3**2-2*5)  # Biraz daha  karmaşık bir işlem ** üslü sayıları ifade ediyor.
print(x)


for a in range (3):     # 5 defa print içindeki veriyi yazdırır.
    print("Python")


A=10                
B=5
A,B=B,A             # A'ya 10 B'ye 5 değerini verdik ama bu satırda A ve B 'yi tek bir komutla yer değiştirdik.
print(A,B)          # A = 5 , B =10  oldu.
 
 
 
_1A= "1A gibi bir değişkeni oluşturmak için _ kullanmak zorundasin."       #  1A gibi bir değişken yapmak istiyorsak _ kullanmak zorundayız.
print(_1A)




print("Python Keywords")
import keyword       # Python içindeki anahtar kelimeli gösterir. Kullanıcağımız kodlar ...
print(keyword.kwlist)

Cep=0
Cep=Cep+10
Cep=Cep+20
print(Cep , "TL")          # İşlemler sırayla olduğu için bi önceki değere yeni bir değer eklersek örnekteki gibi katlanarak Cebimizde 30 TL olur.



# Boolean yani True ve False'lar ["and" , "or" "not"]
 
print((3<5) and (4<1))          # "and" kodu her iki durumunda doğru olması gerekir. Bir tanesi yanlışsa False olur.
print((3<5) or (4<1))           # "or" ise tek bir şartın dolru olması yeterdir sonuç true olur.
print(not(5<10))                # "not" kodu durumu tam tersine çevirir. True olması gerekirken False verecektir.

# if 
if 5==4:                        # if kodu ile koşul sağlanırsa bir sonraki kodu çalıştıracak.
    print("Koşul Sağlandı")
else:
    print("Koşul Başarısız")    # 5 4'e eşit olmadığı için else kodu çalışacak.
    




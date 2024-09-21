#stringteki bir harfe erişim

a=""
s=0
index=int(input("Index değerini gir:"))
for d in "merhaba dünya":
    
    if s==index:
        a=d
    s+=1    
print(a)
# continue komutu her seferinde komutu yeniden başlatır.

for a in range(100): 
    if (a%5==0):      # burda 5 e bölünenlere sıra gelince işlem yapmadan  kodu tekrar çalıştırır.
        continue
    print(a)
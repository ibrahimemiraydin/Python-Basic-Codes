
sifre="1234"
kullanici="emir"

giris_id=input("Kullanıcı Adı Giriniz:")
if giris_id==kullanici:
    giris=input("Şifre Giriniz:")
    if giris==sifre:
        print("Hoşgeldiniz")
    
    else:
        print("Şifre Hatalı")
else:
    print("Kullanıcı adı veritabanımızda kayıtlı değil.")

    




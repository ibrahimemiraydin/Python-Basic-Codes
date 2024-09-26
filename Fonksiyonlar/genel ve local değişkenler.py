def topla():
    global a            # a değerini global yaptırdığımız için 8. satırdaki print kodu çalışacaktır.
    a=5
    b=6
    return(a+b)

print(topla())
print(a)
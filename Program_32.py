while(True):
    a=int(input("Podaj a: "))
    b=int(input("Podaj b: "))

    while r>0:
        a=((a/b)*b)+r
        a=r
        r=b%a
        b=((b/a)*a)+r
        print(int(r))
        

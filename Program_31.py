def czy_pierwsza(x):
    while x > 2:
        w = x % 2
        if w == 0:
            print("Liczba złożona")
            break
        elif w != 0:
            print("Liczba pierwsza")
            break
       
        
y = int(input("Podaj liczbe"))
czy_pierwsza(y)

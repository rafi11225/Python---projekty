n = int(input("Podaj liczbę elementów: "))
a = int(input("Podaj liczbę pierwszego elemnetu: "))
r = int(input("Podaj różnicę: "))
i = 0
while i  < n:
    i+=1
    b = a + r
    a = b + r
    print(str(b))
    print(str(a))
    

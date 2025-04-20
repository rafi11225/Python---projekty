def pole_kwadratu(x):
    return x**2
def pole_prostokata(x, y):
    return x*y
def pole_kola(r):
    import math
    return (r**2) * math.pi
def pole_trapezu(a, b, h):
    return 0.5 * (a + b) * h

def pole_trojkata(a, h):
    return (a * h) / 2

while(True):
    wybor = int(input("""Czego pole chcesz obliczyć?
    1) kwadratu
    2) prostokąta
    3) koła
    4) trapezu
    5) trójkąta
    (aby wyjść kliknij cokolwiek innego)
    Twój wybór: """))

    if( wybor == 1):
        x = int(input("Wprowadź bok kwadratu: "))
        print("Pole:", pole_kwadratu(x))
    elif( wybor == 2):
        x = int(input("Wprowadź  pierwszy bok prostokąta: "))
        y = int(input("Wprowadź drugi bok prostokąta: "))
        print("Pole:", pole_prostokata(x, y))
    elif( wybor == 3):
        r = int(input("Wprowadź promień okręgu: "))
        print("Pole:", pole_kola(r))
    elif(wybor == 4):
        a = int(input("Wprowadź pierwszy bok trapezu: "))
        b = int(input("Wprowadź drugi bok trapezu: "))
        h = int(input("Wprowadź wysokość trapezu: "))
        print("Pole: ", pole_trapezu(a, b, h))
    elif(wybor == 5):
        a = int(input("Wprowadź bok trójkąta: "))
        h = int(input("Wprowadź wysokość trójkąta: "))
        print("Pole:", pole_trojkata(a, h))
    else:
        exit()

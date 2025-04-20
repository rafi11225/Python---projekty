import time
def czas(func, arg1, arg2, czas):
   for i in range (0, czas):
    start = time.perf_counter()
    func(arg1, arg2)
    end = time.perf_counter()
    sum = 0
    sum = sum + (end - start)
    return sum
    
def szukaj(x, lista):
    if x in lista:
        print("Jest")
    else:
        print("Nie ma")

kontener = [ w for w in range(100) if w % 3 != 0 and w % 2 == 0]
zbior = { w for w in range(100) if w % 3 != 0 and w % 2 == 0}

x = int(input("wprowadź wartość: "))
print(czas(szukaj, x, kontener, czas = 100000))
print(czas(szukaj, x, zbior, czas = 100000))

if(czas(szukaj, x, kontener, czas = 100000) > czas(szukaj, x, zbior, czas = 100000)):
    print("Praca na zbiorach jest szybsza")
elif(czas(szukaj, x, kontener, czas = 100000) == czas(szukaj, x, zbior, czas = 100000)):
    print("Praca na listach i zbiorach jest tak samo szybka")
else:
    print("Praca na listach jest szybsza")
             
             
     

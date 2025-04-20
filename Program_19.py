import random
def losuj (lista, maximum):
   liczba = random.randint(1, maximum)
   if liczba not in lista:
       lista.append(liczba)
   else:
       lista.pop()
       
       
       
   
     
    
listaa = []

maks = 49

i = 0
while i < 6:
     i+=1
     losuj(listaa, maks)
print(listaa)
 


import random
y = random.randint(1, 10)
i = 0
while  i < 5:
    x = int(input( "Zgadnij liczbe: " ))
    i+=1
    if ( x > y ):
        print( "Podaj mniejsza liczbe" )
        continue
    elif ( x < y ):
        print( "Podaj wieksza liczbe" )
        continue
    else:
        print( "Brawo odgadles liczbe!!!" )
        
  
       
   

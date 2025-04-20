i = 0
wynik = 0
while i < 5:
    x = int(input("Podaj liczbe dodatnia: "))
    if ( x >= 0 ):
            wynik += x
            
    else:
        print ("""Miala byc liczba dodatnia,
               masz tu szanse i napisz liczbe dodatnia""" )
        continue ###jesli byłby tutaj "break" przerwałby pętlę, a "continueją powtarza, bo nie zwraca uwagi na resztę pętli
        
    print ("Twoj wynik:", wynik)       
    i += 1
    

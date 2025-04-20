imiona = [ "Rafal" , "Wojciech" , "Zenon" ]
################################
wybor = int(input("""Wybierz:
                  1) wyszukaj po id
                  2) zmien imie w liscie
                  3) dodaj imie do listy
                  wybor: """))
if( wybor == 1 ):
    id = int(input("Podaj id (1-3), aby znalezc swoje imie: "))
    if( id <= 3):
        i = id - 1
        print( imiona[i] )
    else:
        print("Error")
        exit()
    
elif( wybor == 2 ):
    ID = int(input("Podaj id (1-3), aby znalezc imie do zamiany: "))
    if( ID <= 3 ):
        k = ID - 1
        zamiana = str(input("Podaj imie do zamiany: "))
        imiona[k] = zamiana
        imiona.sort()
        for imie in imiona:
           print(imie) 
    else:
        print( "Error" )
        exit()
elif( wybor == 3 ):
    Imie = str(input("Wprowadz imie do dodania: "))
    Imie = Imie.capitalize()
    imiona.append(Imie)
    ##imiona.insert(0, Imie)
    imiona.sort() #można dać w tym nawiasie reverse == True/False, wtedy decydujemy czy to ma być rosnące czy malejące
    for godnosc in imiona:
        print(godnosc)
    
else:
    print( "Error" )
    exit()
    

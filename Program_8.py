imiona = [ "Rafal" , "Damian" , "Arkadiusz" ]
imie = str(input("Wprowadz imie do sprawdzenia: "))

if( imie in imiona ):
    print("Masz dostep")
    
elif ( imie not in imiona ):
    print("Brak dostepu")

print("Podaj swoj wiek") 
wiek = int(input())
if ( wiek > 18 ):
    pelnoletnosc = True
    

elif ( wiek == 18 ):
    pelnoletnosc = True
    
    
else:
    pelnoletnosc = False;
    
if ( pelnoletnosc == True ):
    print("pelnoletni")
else:
    print("niepelnoletni");


if ( pelnoletnosc == True ):
    print("Podaj swoje imie")
    imie = input()
    if ( imie[-1] == "a" ):
        print("twoja plec to kobieta")
        plec = "kobieta"
            
    else:
        print("twoja plec to mezczyzna");
        plec = "mezczyzna";
            
    print("imie:" + " " + imie.capitalize())
    #######################
    print("wiek:" + " " + str(wiek))
    #######################
    print("plec:" + " " + plec)

    
else:
    print("BLAD! JESTES DZIECIAKIEM!!")
    exit();
    
  
 

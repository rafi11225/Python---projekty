slownik = {}
while(True):
    wybor = int(input("1)dodaj definicje 2)znajdz definicje 3)usun definicje 4)dodaj cos do istniejacego slownika 5)wyswietl slownik 6)wyswietl slownik w stanie surowym 7)zakoncz wybor: "))

    if(wybor == 1):
     
        klucz = input("Wprowadz klucz: ")
        definicja = input("Wprowadz wartosc: ")
        slownik[klucz] = definicja
        print("Dodano definicje i klucz")
        
    elif(wybor == 2):
        print("Czego szukasz?: ")
        klucz = input("Wprowadz szukany klucz: ")
        if klucz in slownik:
            print(slownik[klucz])
        else:
            print("Nie ma tutaj czegos takiego")
            

    elif(wybor == 3):
        klucz = input("Podaj klucz, aby go usunac: ")
        if klucz in slownik:
            del(slownik[klucz])
            print(slownik)
        else:
            print("Podales zly klucz")
        
        
    elif(wybor == 4):
       klucz = input("Wprowadz klucz: ")
       definicja = input("Wprowadz definicje: ")
       slownik.update({klucz : definicja})
       print("Wprowadzono definicje domyslnie")


    elif(wybor == 5):
       for key in slownik:
          print(key, slownik[key])
    elif(wybor == 6):
         print(slownik)
         
    elif(wybor == 7):
        exit()
    

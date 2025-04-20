def plik(nazwa_pliku):
    
    with open (nazwa_pliku ,"r" , encoding = "UTF-8") as file:
        try:
          return file.read()
        except FileNotFoundError:
            print("Nie znaleziono pliku!") 



nazwa_pliku = input("Wprowadź nazwę pliku: ")
czytaj = plik(nazwa_pliku)

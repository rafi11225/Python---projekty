imiona = {1: "Rafał Brzozowski", 2: "Julia Preczewska", 3: "Kamil Kamiński"} ##słownik


i = int(input("Podaj ID gościa: "))
print(imiona[i])
wybor = int(input("Chcesz usunąć gościa z listy(1) czy wyjść z programu(2)?: "))
if( wybor == 1 ):
    del(imiona[i])
    print("Usunieto")
    
elif( wybor == 2 ):
    print("Wychodze...")
    exit()
    
else:
    print("Wychodze...")
    exit()



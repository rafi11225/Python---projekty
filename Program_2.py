liczba = 7
LiczbaProb = 0
while liczba >= 6:
 liczba = int(input("Podaj  liczbe: "))
 if ( liczba >= 6 ):
     LiczbaProb += 1
 elif( liczba <= 6 ):
     print("Uzyto petli " + str(LiczbaProb) + " razy")

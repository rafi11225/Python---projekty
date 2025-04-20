imiona = ["Rafal" , "Bartek" , "Kacper" , "Jakub", "Michal"]

ID = int(input("Podaj ID (liczone od 'jeden')imienia: "))
i = ID - 1

  
if( i > 0 ):
  imie = print(imiona[i])
elif( i <= 0 ):
  print("Miales podac ID > 0")
  exit()
  
for m in imiona:
  print(m)
              

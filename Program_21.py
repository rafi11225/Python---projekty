


lista = []
with open ("imionanazwiska.txt" , "r" , encoding = "UTF-8") as file:
    for line in file:   
      lista.append (tuple(line.replace("\n", "").split(" ")))
      

with open ("imiona.txt" , "w" , encoding = "UTF-8") as file:
    for items in lista:
        file.write(items[0] + "\n")

with open ("nazwiska.txt" , "w", encoding = "UTF-8") as file:
    for items in lista:
        """if(len(items) == 2):
            file.write(items[1] + "\n")
        else:
            file.write("\n")"""##tak można albo:
        try:
            file.write(items[1] + "\n")
        except IndexError:
            file.write("\n")
            

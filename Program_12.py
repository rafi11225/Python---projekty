
ludzie = [ ("iohaoiahidaoihdai" , {"name": "Rafał", "surname": "Brzozowski" , "age": 20})]

for ID , slownik in ludzie:
    for keys in slownik:
        print(keys, slownik[keys])

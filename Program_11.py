ludzie = {

  "hdiahhdoahdihaohda":{"name": "Rafal" , "surname": "Brzozowski" , "age": 20},
  "gfhiuhflihgloidhga":{"name": "Karol" , "surname": "Boguś" , "age": 15}

          }
for key in ludzie:
    print("ID:", key)
    for klucz in ludzie[key]:
        print(klucz, ludzie[key][klucz])
        

ludzie2 = [



   {"ID": "hafiahohiohaf", "name": "Kacper", "age": 19}

        ]
for keys in ludzie2:
    
    for wartosci in keys:
        print(wartosci, keys[wartosci])



for ID , slownik in ludzie.items():
      for key in slownik:
          print(key, slownik[key])
        


import requests
import json
import webbrowser
##ilosc = int(input("Wprowadz ilosc tresci(max 500)"))
##params = {
###"animal_type":"cat",
##"amount":ilosc


  ##  }
r = requests.get("https://meowfacts.herokuapp.com/")

try:
    wynik = r.json()

except json.decoder.JSONDecodeError:
    print("Cos poszlo nie tak")
    
else:
    print("Your fact about cats:", wynik["data"])
    

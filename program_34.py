import webbrowser
import requests
import json

from pprint import pprint

animal_type = string(input("Type an animal type what you want: "))
amount = int(input("Type an amount: "))
 params = {
     "animal_type" : animal_type
     "amount" : amount
 }
 
 r = requests.get("https://meowfacts.herokuapp.com/", params)
 
 try:
     wynik  = r.json()
except json.decoder.JSONDecodeError:
    print("Something is wrong...")
    continue
else:
    print("It's your fact about ", animal_type, " ", wynik["data"])
    
     
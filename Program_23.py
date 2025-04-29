import requests

##for url in link:
  ##  wynik = requests.get(url)
wynik = requests.get(#URL) 
if(wynik.status_code == 200):
    print("Link działa")
else:
    print("Link nie działa")
    
  

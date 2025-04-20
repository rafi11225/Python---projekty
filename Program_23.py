import requests
##link = ( "https://www.pornhub.com", "https://www.uzumymw.com", "https://www.GTA-SITE.pl")
##for url in link:
  ##  wynik = requests.get(url)
wynik = requests.get("https://www.pornhub.com") 
if(wynik.status_code == 200):
    print("Link działa")
else:
    print("Link nie działa")
    
  

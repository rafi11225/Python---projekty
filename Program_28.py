import requests
import pprint
import json
import webbrowser
from datetime import datetime, timedelta
timeBefore = timedelta(days = 7)
searchtime = datetime.today() - timeBefore
print(searchtime)
params = {
"site": "stackoverflow",
"sort":"votes",
"order":"desc",
"fromdate":int(searchtime.timestamp()),
"tagged":"python"
    }
api = requests.get("https://api.stackexchange.com/2.3/questions", params)
try:
    questions = api.json()
except json.decoder.JSONDecodeError:
    print("Nieprawidłowy format")
else:
    for question in questions["items"]:
        webbrowser.open(question["link"])
        
    

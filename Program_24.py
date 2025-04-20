import requests
##import json
import pprint
from collections import defaultdict
response = requests.get("https://jsonplaceholder.typicode.com/todos")
##tasks = json.loads(response.text)
tasks = response.json()
for text in tasks:
    CompletedTasks = defaultdict(int)   
    if(text["completed"] == True):
        try:
            CompletedTasks[text["userId"]] +=1
        except KeyError:
            CompletedTasks[text["userId"]] = 1
UserIdWithMaxCompletedTasks = []            
MaxAmountOfCompletedTasks = max(CompletedTasks.values())            
for userId , NumberOfCompletedTasks in CompletedTasks.item():
    if(NumberOfCompletedTasks == MaxAmountOfCompletedTasks):
        UserIdWithMaxCompletedTasks.append(userId)
    
      

import requests
u = requests.get("https://jsonplaceholder.typicode.com/users")
users = u.json()
for user in users:
    for keys in user:
        print(keys, user[keys])    

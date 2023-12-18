#!/usr/bin/python3

import json
import sys
import urllib.request

url_todos = "https://jsonplaceholder.typicode.com/todos"
url_users = "https://jsonplaceholder.typicode.com/users"


with urllib.request.urlopen(url_todos) as response:
    data_todos = response.read()
with urllib.request.urlopen(url_users) as response:
    data_users = response.read()
todos = json.loads(data_todos)
users = json.loads(data_users)

for user in users:
    if user['id'] == int(sys.argv[1]):
        username = user['username']
todo_list = []
for todo in todos:
    dico = {}
    if todo['userId'] == int(sys.argv[1]):
        dico['task'] = todo['title']
        dico['completed'] = str(todo['completed'])
        dico['username'] = username
        todo_list.append(dico)
dictionary = {}
dictionary[str(sys.argv[1])] = todo_list

# Nom du fichier json
json_filename = f'{sys.argv[1]}.json'
# Écrire les données dans le fichier CSV
with open(json_filename, mode='w') as json_file:
    json.dump(dictionary, json_file)
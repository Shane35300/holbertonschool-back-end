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

users_dico = {}
users_list = []
for user in users:
    if user['id'] not in users_list:
        users_list.append(user['id'])
        username = user['username']
        todo_list = []
        for todo in todos:
            if todo['userId'] == user['id']:
                dico = {}
                dico['username'] = username
                dico['task'] = todo['title']
                dico['completed'] = str(todo['completed'])
                todo_list.append(dico)
    users_dico[user['id']] = todo_list

# Écrire les données dans le fichier CSV
with open('todo_all_employees.json', mode='w') as json_file:
    json.dump(users_dico, json_file)

#!/usr/bin/python3
"""This script fetches and displays the TODO list progress for a
given employee ID."""

import csv
import json
import sys
import urllib.request


if __name__ == '__main__':
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
            dico['id'] = str(sys.argv[1])
            dico['username'] = username
            dico['completed'] = str(todo['completed'])
            dico['title'] = todo['title']
            todo_list.append(dico)
    # Définir les noms de colonnes pour le fichier CSV
    fields = ['id', 'username', 'completed', 'title']
    # Nom du fichier CSV
    csv_filename = f'{sys.argv[1]}.csv'
    # Écrire les données dans le fichier CSV
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        # Écrire les lignes de données
        for todo in todo_list:
            writer.writerow([todo[field] for field in fields])

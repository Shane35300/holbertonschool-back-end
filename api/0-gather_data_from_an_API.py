#!/usr/bin/python3
"""This script fetches and displays the TODO list progress for a
given employee ID."""

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
            user_name = user['name']
            tasks = 0
            total_tasks = 0
            for todo in todos:
                if (todo['userId'] == int(sys.argv[1]) and
                        todo['completed'] is True):
                    tasks += 1
                if todo['userId'] == int(sys.argv[1]):
                    total_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          tasks, total_tasks))
    for todo in todos:
        if (todo['userId'] == int(sys.argv[1]) and todo['completed'] is True):
            print(f"\t {todo['title']}")

#!/usr/bin/env python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        users = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
        name = users.json()['name']
        for_todos = {
            'userId': argv[1]
        }
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params=for_todos)
        doneTodos = [todo for todo in todos.json() if todo.get('completed')]
        lenTodos = len(todos.json())
        lenDone = len(doneTodos)
        print("Employee {} is done".format(name), end="")
        print(" with tasks({}/{}):".format(lenDone, lenTodos))
        for done in doneTodos:
            print("\t {}".format(done.get('title')))

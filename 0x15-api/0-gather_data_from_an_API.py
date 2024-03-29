#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        users = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id))
        name = users.json()['name']
        for_todos = {
            'userId': id
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

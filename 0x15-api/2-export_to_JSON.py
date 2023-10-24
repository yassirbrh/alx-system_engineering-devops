#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress and save the result
    as JSON File.
'''
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        users = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id))
        for_todos = {
            'userId': id
        }
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params=for_todos)
        file = str(id) + ".json"
        with open(file, "w", newline="") as f:
            output_arr = []
            for todo in todos.json():
                data = {}
                username = users.json()['username']
                title = todo.get('title')
                completed = todo.get('completed')
                data['task'] = title
                data['completed'] = completed
                data['username'] = username
                output_arr.append(dict(data))
            json.dump({str(id): output_arr}, f)

#!/usr/bin/python3
'''
    Python script that, using this REST API, for each employee,
    returns information about his/her TODO list progress and save the result
    as JSON File.
'''
import json
import requests
import sys


if __name__ == '__main__':
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    with open("todo_all_employees.json", "w", newline="") as f:
        final_output = {}
        for user in users.json():
            id = user['id']
            for_todos = {
                'userId': id
            }
            todos = requests.get(url_todos, params=for_todos)
            output_arr = []
            for todo in todos.json():
                data = {}
                username = user['username']
                title = todo.get('title')
                completed = todo.get('completed')
                data['username'] = username
                data['task'] = title
                data['completed'] = completed
                output_arr.append(dict(data))
            final_output[str(id)] = output_arr
        json.dump(final_output, f)

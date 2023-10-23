#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress and save the result
    as CSV File.
'''
import csv
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
        file = str(id) + ".csv"
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            for todo in todos.json():
                username = users.json()['username']
                completed = todo.get('completed')
                title = todo.get('title')
                writer.writerow([id, username, completed, title]) 

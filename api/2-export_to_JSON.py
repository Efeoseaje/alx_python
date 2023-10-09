#!/usr/bin/python3

"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress and
    converts to JSON.
"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    # getting user
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url)
    user_data = user.json()

    # getting todos
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos = requests.get(todo_url)
    todos_data = todos.json()

    # exporting to a json
    json_file = "{}.json".format(user_id)

    user_info = {
        f"{user_id}": [
            {
                "task": items['title'],
                "completed": items['completed'],
                "username": user_data['username'],
            }

            for items in todos_data
        ]
    }

    # write data to json file
    with open(json_file, 'w') as json_files:
        json.dump(user_info, json_files)

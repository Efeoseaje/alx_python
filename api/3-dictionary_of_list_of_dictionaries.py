"""Python script to export data in the JSON format
"""

import json
import requests
import sys


def fetch_user_data(user_id):
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url)
    user.raise_for_status()
    return user.json()


def fetch_todo_data(user_id):
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos = requests.get(todo_url)
    todos.raise_for_status()
    return todos.json()


if __name__ == '__main__':
    try:
        # Create a dictionary to store data for all users
        all_user_data = {}

        # Iterate through user IDs
        for user_id in range(1, 11):  # Assuming user IDs range from 1 to 10
            user_data = fetch_user_data(user_id)
            todos_data = fetch_todo_data(user_id)

            # Create a list to store todo data for the current user
            user_info = []

            for todo in todos_data:
                user_info.append({
                    "username": user_data['username'],
                    "task": todo['title'],
                    "completed": todo['completed']
                })

            # Add the user's data to the dictionary
            all_user_data[str(user_id)] = user_info

        # Write all_user_data to a JSON file
        json_file = "todo_all_employees.json"
        with open(json_file, 'w') as json_files:
            json.dump(all_user_data, json_files)  # Format JSON for readability

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from the API: {str(e)}")

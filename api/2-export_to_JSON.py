#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
exports it to JSON format
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print(f"Failed to retrieve employee details for ID {employee_id}.")
        return

    employee_data = employee_response.json()
    employee_username = employee_data["username"]

    # Fetch employee's TODO list
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee {employee_username}.")
        return

    todo_data = todo_response.json()

    # Export data to JSON format
    json_filename = f"{employee_id}.json"

    json_data = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_username
            }
            for task in todo_data
        ]
    }

    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"JSON file '{json_filename}' has been created with TODO list data for employee {employee_username}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

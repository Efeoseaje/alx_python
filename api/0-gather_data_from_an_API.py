#!/usr/bin/python3

""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

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
    employee_name = employee_data["name"]

    # Fetch employee's TODO list
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee {employee_name}.")
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks \
          ({num_completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

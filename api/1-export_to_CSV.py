import csv
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

    # Create a CSV file and write the data
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            task_completed_status = "True" if task["completed"] else "False"
            csv_writer.writerow([employee_id, employee_name, task_completed_status, task["title"]])

    print(f"CSV file '{csv_filename}' has been created with TODO list data for employee {employee_name}.")


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

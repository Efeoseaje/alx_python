import csv
import requests
import sys


def main():
    user_id = sys.argv[1]

    # user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {user_id} not found.")
        return
    user_data = user_response.json()

    #  todos data
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch todos for user {user_data['name']}.")
        return
    todos_data = todos_response.json()

    # CSV file
    csv_file = f"{user_id}.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow(
                [user_id, user_data['username'], task['completed'], task['title']])

    print(f"Data exported to {csv_file}.")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to fetch info """
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    # Fetch employee data
    user_url = '{}users/{}'.format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list
    todos_url = '{}todos?userId={}'.format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task['completed'])

    # Print progress information
    print("Employee {} is done with tasks ({}/{}):".format(user_data['name'], completed_tasks, total_tasks))
    for task in todos_data:
        if task['completed']:
            print("\t{}".format(task['title']))


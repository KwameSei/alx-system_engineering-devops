import requests
from sys import argv
"""Gathering information from an API"""


if __name__ == '__main__':
    Base_url = 'https://jsonplaceholder.typicode.com'
    # Getting user by putting user id from the command line

    user = requests.get(f'{Base_url}/users/{argv[1]}').json()
    todos = requests.get(f'\
            {Base_url}/todos', params={'userId': argv[1]}).json()

    total_tasks = len(todos)
    completed = 0
    completed_tasks = []

    for todo in todos:
        if todo['completed']:
            completed += 1
            completed_tasks.append(todo["title"])
    output = f'Employee {user["name"]} is done with tasks \
            ({completed}/{total_tasks}): '

    print(output)
    for task in completed_tasks:
        print(f'\t {task}')

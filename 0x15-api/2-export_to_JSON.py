#!/usr/bin/python3
"""Saving employees' TODO list information
    in CSV file
"""
from json import dump
from requests import get
from sys import argv


def todo_json(emp_id):
    """Send request for employee's TODO list to API"""
    filename = '{}.json'.format(emp_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    # check if user exists
    user = get(user_url + emp_id).json().get('username')

    if user:
        params = {'userId': emp_id}
        #  get all tasks
        tasks = get(todo_url, params=params).json()

        #  create list of dictionaries
        #  with info about each task
        task_list = []
        for task in tasks:
            task_list.append({"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": user})

        #  open file in write mode and jsonify
        with open(filename, 'w', encoding='utf8') as f:
            dump({emp_id: task_list}, f)


if __name__ == '__main__':
    if len(argv) > 1:
        todo_json(argv[1])

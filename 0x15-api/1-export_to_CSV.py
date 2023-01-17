#!/usr/bin/python3
"""
Gathering information from an API
"""
import csv
import requests
from sys import argv


Base_url = 'https://jsonplaceholder.typicode.com'
"""REST API url"""


if __name__ == "__main__":
    user = requests.get('{}/users/{}'.format(Base_url, argv[1])).json()
    todos = requests.get('\
            {}/todos'.format(Base_url), params={'userId': argv[1]}).json()

    with open('{}.csv'.format(argv[1]), 'w', encoding='utf8') as f:

        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow(['{}'.format(argv[1]), '{}'.format(user['name']),
                            '{}'.format(str(todo['completed'])),
                             '{}'.format(todo['title'])])

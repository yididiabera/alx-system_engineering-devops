#!/usr/bin/python3
"""This script uses a REST API to get information about a given employee ID
and returns information about his/her TODO list progress.
It then exports the data in the CSV format."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    print(user)
    name = user.get("username")
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()
    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, name, task.get(
                "completed"), task.get("title")])

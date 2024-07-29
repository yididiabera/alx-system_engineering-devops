#!/usr/bin/python3
"""This script uses a REST API to get information about a given employee ID
and returns information about his/her TODO list progress.
It then exports the data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    name = user.get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response = requests.get(url)
    todos = response.json()

    tasks = []
    for task in todos:
        if task.get("userId") == int(user_id):
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = name
            tasks.append(task_dict)

    data = {}
    data[user_id] = tasks

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)

#!/usr/bin/python3
"""This script uses a REST API to get information about a given employee ID
and returns information about his/her TODO list progress.
It then exports the data in the JSON format. recording all tasks from
all employees to a file named todo_all_employees.json."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    data = {}
    for user in users:
        url = "https://jsonplaceholder.typicode.com"
        todo_url = url + "/users/{}/todos".format(user.get("id"))
        todo_response = requests.get(todo_url)
        todos = todo_response.json()
        user_id = user.get("id")
        name = user.get("username")
        tasks = []
        for task in todos:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = name
            tasks.append(task_dict)
        data[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)

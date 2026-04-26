import json
import os
from task import Task

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                tasks = [Task.from_dict(t) for t in data]
        except:
            print("Error loading tasks file.")
    return tasks

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump([t.to_dict() for t in tasks], file)
    except:
        print("Error saving tasks file.")
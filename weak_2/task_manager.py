from task import Task
from utils import get_valid_priority

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks else []
        self.next_id = self.get_next_id()

    def get_next_id(self):
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add_task(self):
        title = input("Enter task title: ")
        priority = get_valid_priority()

        task = Task(self.next_id, title, priority)
        self.tasks.append(task)
        self.next_id += 1

        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for t in self.tasks:
            status = "Complete" if t.completed else "Incomplete"
            print(f"ID: {t.id} | Title: {t.title} | Priority: {t.priority} | Status: {status}")

    def find_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def update_task(self):
        task_id = int(input("Enter task ID: "))
        task = self.find_task(task_id)

        if not task:
            print("Task not found!")
            return

        new_title = input("Enter new title (leave blank to keep same): ")
        if new_title:
            task.title = new_title

        print("Do you want to change priority? (y/n)")
        if input().lower() == "y":
            task.priority = get_valid_priority()

        print("Task updated!")

    def mark_complete(self):
        task_id = int(input("Enter task ID: "))
        task = self.find_task(task_id)

        if task:
            task.completed = True
            print("Task marked as complete!")
        else:
            print("Task not found!")

    def delete_task(self):
        task_id = int(input("Enter task ID: "))
        task = self.find_task(task_id)

        if task:
            self.tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task not found!")

    def filter_tasks(self):
        print("\n1. By Status")
        print("2. By Priority")
        choice = input("Choose filter: ")

        filtered = []

        if choice == "1":
            print("\n1. Complete")
            print("2. Incomplete")

            status_choice = input("Choose status: ")

            if status_choice == "1":
                filtered = [t for t in self.tasks if t.completed]
            elif status_choice == "2":
                filtered = [t for t in self.tasks if not t.completed]
            else:
                print("Invalid status choice!")
                return

        elif choice == "2":
            print("\n1. Low")
            print("2. Medium")
            print("3. High")

            priority_choice = input("Choose priority: ")

            priority_map = {
                "1": "Low",
                "2": "Medium",
                "3": "High"
            }

            if priority_choice in priority_map:
                selected_priority = priority_map[priority_choice]

                filtered = [
                    t for t in self.tasks
                    if t.priority == selected_priority
                ]
            else:
                print("Invalid priority choice!")
                return

        else:
            print("Invalid filter choice!")
            return

        if not filtered:
            print("No matching tasks.")
            return

        for t in filtered:
            status = "Complete" if t.completed else "Incomplete"
            print(f"ID: {t.id} | Title: {t.title} | Priority: {t.priority} | Status: {status}")
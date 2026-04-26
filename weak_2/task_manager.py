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

        new_priority = input("Enter new priority (Low/Medium/High or blank): ")
        if new_priority:
            if new_priority in ["Low", "Medium", "High"]:
                task.priority = new_priority
            else:
                print("Invalid priority!")

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
        print("1. By Status\n2. By Priority")
        choice = input("Choose filter: ")

        if choice == "1":
            status = input("Complete or Incomplete: ").lower()
            filtered = [t for t in self.tasks if (t.completed and status=="complete") or (not t.completed and status=="incomplete")]

        elif choice == "2":
            priority = input("Low/Medium/High: ")
            filtered = [t for t in self.tasks if t.priority == priority]

        else:
            print("Invalid choice!")
            return

        if not filtered:
            print("No matching tasks.")
            return

        for t in filtered:
            status = "Complete" if t.completed else "Incomplete"
            print(f"ID: {t.id} | Title: {t.title} | Priority: {t.priority} | Status: {status}")
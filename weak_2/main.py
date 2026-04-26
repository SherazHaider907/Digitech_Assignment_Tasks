from task_manager import TaskManager
from file_handler import load_tasks, save_tasks

def main():
    tasks = load_tasks()
    manager = TaskManager(tasks)

    while True:
        print("\n===== Task Manager =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Mark a task as complete")
        print("5. Delete a task")
        print("6. Filter tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.mark_complete()
        elif choice == "5":
            manager.delete_task()
        elif choice == "6":
            manager.filter_tasks()
        elif choice == "7":
            save_tasks(manager.tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
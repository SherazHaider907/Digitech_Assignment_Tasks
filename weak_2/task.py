class Task:
    def __init__(self, task_id, title, priority, completed=False):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["id"],
            data["title"],
            data["priority"],
            data["completed"]
        )
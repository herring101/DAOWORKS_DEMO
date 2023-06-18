class Task:
    def __init__(self, name, status="未完了"):
        self.name = name
        self.status = status


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))

    def remove_task(self, name):
        self.tasks = [task for task in self.tasks if task.name != name]

    def toggle_task_status(self, name):
        for task in self.tasks:
            if task.name == name:
                task.status = "完了" if task.status == "未完了" else "未完了"

import tkinter as tk
from tkinter import messagebox
from task import Task, TodoList


class TodoApp:
    def __init__(self, root):
        self.todo_list = TodoList()
        self.root = root
        self.task_listbox = tk.Listbox(root)
        self.task_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="タスク追加", command=self.add_task)
        self.remove_button = tk.Button(root, text="タスク削除", command=self.remove_task)

        # ウィジェットの配置
        self.task_listbox.pack()
        self.task_entry.pack()
        self.add_button.pack()
        self.remove_button.pack()

        # ダブルクリックでタスクのステータスを切り替える
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task_status)

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.todo_list.add_task(task_name)
            self.task_entry.delete(0, "end")
            self.update_task_listbox()
        else:
            messagebox.showinfo("エラー", "タスク名を入力してください")

    def remove_task(self):
        selected_task = self.task_listbox.get(self.task_listbox.curselection())
        selected_task = self.displayname_to_taskname(selected_task)
        self.todo_list.remove_task(selected_task)
        self.update_task_listbox()

    def toggle_task_status(self, event):  # event引数を追加
        selected_task = self.task_listbox.get(self.task_listbox.curselection())
        selected_task = self.displayname_to_taskname(selected_task)
        self.todo_list.toggle_task_status(selected_task)
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, "end")
        for task in self.todo_list.tasks:
            self.task_listbox.insert("end", task.name + " (" + task.status + ")")

    def displayname_to_taskname(self, displayname):
        if "(未完了)" in displayname:
            return displayname.replace(" (未完了)", "")
        else:
            return displayname.replace(" (完了)", "")


if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image
from task import Task, TodoList


class TodoApp:
    def __init__(self, root):
        # initialize widgets
        self.todo_list = TodoList()
        self.root = root

        # set background image
        self.background_image = PhotoImage(file="images/daoworks.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # set widgets
        self.task_listbox = tk.Listbox(root)
        self.task_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="タスク追加", command=self.add_task)
        self.remove_button = tk.Button(root, text="タスク削除", command=self.remove_task)

        # place widgets
        self.task_listbox.pack()
        self.task_entry.pack()
        self.add_button.pack()
        self.remove_button.pack()

        # bind events
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

    def toggle_task_status(self, event):
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

    img = Image.open("images/daoworks.png")
    width, height = img.size
    root.geometry(f"{width}x{height}")

    todo_app = TodoApp(root)
    root.mainloop()

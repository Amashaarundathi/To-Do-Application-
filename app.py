import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Todo App")
root.geometry('400x500')
root.resizable(False, False)

# Try to set icon, ignore if not found
try:
    root.iconbitmap('icon.ico')
except Exception:
    pass

task_list = []

def add_task(event=None):
    task = task_entry.get().strip()
    task_entry.delete(0, tk.END)
    if task:
        with open('tasklist.txt', 'a') as file:
            file.write(task + '\n')
        listbox.insert(tk.END, task)
        task_list.append(task)

def delete_task():
    task = listbox.get(tk.ANCHOR)   # Get selected task
    if task in task_list:
        listbox.delete(tk.ANCHOR)
        task_list.remove(task)
        # Rewrite file after deletion
        with open('tasklist.txt', 'w') as file:
            for t in task_list:
                file.write(t + '\n')

def open_tasks():
    try:
        with open('tasklist.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                task = task.strip()
                if task:
                    listbox.insert(tk.END, task)
                    task_list.append(task)
    except FileNotFoundError:
        # Create file if not exists
        with open('tasklist.txt', 'w') as file:
            pass

# heading
heading = tk.Label(root, text='ALL TASKS', font=('Arial', 20, 'bold'))
heading.pack()

# entry box
frame = tk.Frame(root, width=400, height=50)
frame.pack(pady=20)

task_entry = tk.Entry(frame, font=('Arial', 14), width=27)
task_entry.pack()
task_entry.bind("<Return>", add_task)

# task list
frame1 = tk.Frame(root, width=100, height=250)
frame1.pack()

listbox = tk.Listbox(frame1, font=('Arial', 12), width=40, height=16)
listbox.pack()

# load existing tasks
open_tasks()

# delete button
s = ttk.Style()
s.configure('TButton', font=('Arial', 12))

delete_btn = ttk.Button(root, text='Delete', style='TButton', command=delete_task)
delete_btn.pack(side='bottom', pady=12, ipadx=10, ipady=5)

root.mainloop()
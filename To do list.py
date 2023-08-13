import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(frame, text="Remove", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(frame, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)

root.mainloop()

import tkinter as tk
import os
from tkinter import filedialog
import subprocess

def list_files(directory):
    file_list.delete(0, tk.END)  # Clear the current list
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            info = f"[DIR] {item}"
        else:
            size = os.path.getsize(item_path)
            info = f"[FILE] {item} ({size} bytes)"
        file_list.insert(tk.END, info)

def select_directory():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        list_files(selected_directory)

def open_item(event):
    selected_item = file_list.get(file_list.curselection()[0])
    item_path = os.path.join(os.getcwd(), selected_item[6:])  # Remove "[DIR] " or "[FILE] "
    if os.path.isdir(item_path):
        list_files(item_path)
    else:
        if os.name == 'nt':
            # On Windows, open using the default program
            os.startfile(item_path)
        else:
            # On macOS and Linux, modify this for your preferred opener
            subprocess.Popen(["open", item_path], shell=True)

root = tk.Tk()
root.title("Directory and File List")

file_list = tk.Listbox(root, height=10, width=60)  # Increase height and width
file_list.pack()
file_list.bind("<Double-1>", open_item)  # Bind double-click event

list_button = tk.Button(root, text="List Files", command=select_directory)
list_button.pack()

run_button = tk.Button(root, text="Run Python File")
run_button.pack()

root.mainloop()
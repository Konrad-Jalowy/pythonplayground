import tkinter as tk
import os
import subprocess

def list_files():
    file_list.delete(0, tk.END)  # Clear the current list
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)
        if os.path.isdir(item_path):
            info = f"[DIR] {item}"
        else:
            size = os.path.getsize(item_path)
            info = f"[FILE] {item} ({size} bytes)"
        file_list.insert(tk.END, info)

def run_python_file():
    selected_item = file_list.get(tk.ACTIVE)
    if selected_item.startswith("[FILE] ") and selected_item.endswith(".py"):
        script_name = selected_item[7:-10]  # Extract the Python script name
        subprocess.Popen(["python", script_name], shell=True)

root = tk.Tk()
root.title("Directory and File List")

file_list = tk.Listbox(root, height=10, width=60)  # Increase height and width
file_list.pack()

list_button = tk.Button(root, text="List Files", command=list_files)
list_button.pack()

run_button = tk.Button(root, text="Run Python File", command=run_python_file)
run_button.pack()

root.mainloop()
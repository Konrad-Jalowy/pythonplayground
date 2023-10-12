import tkinter as tk
import os

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

root = tk.Tk()
root.title("Directory and File List")

file_list = tk.Listbox(root)
file_list.pack()

list_button = tk.Button(root, text="List Files", command=list_files)
list_button.pack()

root.mainloop()
import tkinter as tk
import os

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

def open_item(event):
    selected_item = file_list.get(file_list.curselection()[0])
    item_path = os.path.join(os.getcwd(), selected_item[6:])  # Remove "[DIR] " or "[FILE] "
    if os.path.isdir(item_path):
        list_files(item_path)

root = tk.Tk()
root.title("Directory and File List")

file_list = tk.Listbox(root, height=10, width=60)  # Increase height and width
file_list.pack()
file_list.bind("<Double-1>", open_item)  # Bind double-click event

list_files(os.getcwd())  # List the current directory initially

root.mainloop()






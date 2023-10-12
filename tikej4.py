import tkinter as tk
import os

def list_files():
    file_list.delete(0, tk.END)  # Clear the current list
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        file_list.insert(tk.END, filename)

root = tk.Tk()
root.title("File List")

file_list = tk.Listbox(root)
file_list.pack()

list_button = tk.Button(root, text="List Files", command=list_files)
list_button.pack()

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
root.geometry("400x300") 
root.mainloop()
import tkinter as tk

def copy_text():
    text_widget.clipboard_clear()
    text_widget.clipboard_append(text_widget.get("1.0", "end"))
    text_widget.update()

root = tk.Tk()
root.title("Hello Tkinter")

# Set the initial window size (width x height)
root.geometry("400x300")

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack()

# Insert the text
text_widget.insert("1.0", "Hello, Tkinter!")

# Create a button to copy the text
copy_button = tk.Button(root, text="Copy Text", command=copy_text)
copy_button.pack()

root.mainloop()
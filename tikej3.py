import tkinter as tk

def copy_text(event=None):
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

# Bind the "Ctrl+C" shortcut to the copy_text function
text_widget.bind("<Control-c>", copy_text)

root.mainloop()
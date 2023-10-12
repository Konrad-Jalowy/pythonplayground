import tkinter as tk

class MyTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My tkinter App")

        self.label = tk.Label(self.root, text="Hello, tkinter!")
        self.button = tk.Button(self.root, text="Click Me", command=self.on_button_click)

        self.label.pack()
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyTkinterApp(root)
    root.mainloop()
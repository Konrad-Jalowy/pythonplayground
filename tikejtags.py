import tkinter as tk


def wrap_with_html_tag(tag):
    # Check if there is selected text
    if text_widget.tag_ranges(tk.SEL):
        # Get the selected text and its position
        sel_start, sel_end = text_widget.tag_ranges(tk.SEL)
        selected_text = text_widget.get(sel_start, sel_end)

        # Wrap the selected text with the specified HTML tag
        wrapped_text = f"<{tag}>{selected_text}</{tag}>"

        # Replace the selected text with the wrapped text
        text_widget.delete(sel_start, sel_end)
        text_widget.insert(sel_start, wrapped_text)

        # Restore the selection
        text_widget.tag_add(tk.SEL, sel_start, f"{sel_start}+{len(wrapped_text)}c")


# Create a Tkinter window
root = tk.Tk()
root.title("Text to HTML Tag")

# Create a Text widget for input
text_widget = tk.Text(root)
text_widget.pack()

# Create buttons for wrapping text with HTML tags
button_p = tk.Button(root, text="Wrap with <p>", command=lambda: wrap_with_html_tag("p"))
button_h1 = tk.Button(root, text="Wrap with <h1>", command=lambda: wrap_with_html_tag("h1"))

button_p.pack()
button_h1.pack()

# Start the Tkinter main loop
root.mainloop()
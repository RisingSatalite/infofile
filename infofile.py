import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import shlex

def on_drop(event):
    # Print the path(s) of the dropped files
    print("Dropped files path:", event.data)
    fileType = event.data.split(".")[-1]
    print("It is a: ", fileType)
    filePath = event.data.split("/")[-1]
    print("Name: ", filePath)
    file_path = event.data
    print(file_path[-1])

    if os.path.exists(file_path):
        print("File name:", os.path.basename(file_path))
        print("Directory:", os.path.dirname(file_path))
        print("Size (bytes):", os.path.getsize(file_path))
        print("Last modified:", os.path.getmtime(file_path))
        print("Created:", os.path.getctime(file_path))
    else:
        print("File does not exist.")
        print(file_path)

# Create a special TkinterDnD window
root = TkinterDnD.Tk()
root.title("Drag and Drop Files")
root.geometry("400x200")

# Create a label to drop files onto
drop_label = tk.Label(root, text="Drag and drop files here", relief="ridge", width=40, height=10)
drop_label.pack(padx=10, pady=10)

# Register the label as a drop target
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()

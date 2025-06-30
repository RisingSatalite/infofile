import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import shlex

def on_drop(event):
    raw_data = event.data
    files = shlex.split(raw_data)
    print("Dropped files:")
    for f in files:
        print(f)
        
        if os.path.exists(f):
            print("File name:", os.path.basename(f))
            print("Directory:", os.path.dirname(f))
            print("Size (bytes):", os.path.getsize(f))
            print("Last modified:", os.path.getmtime(f))
            print("Created:", os.path.getctime(f))
        else:
            print("File does not exist.")
            print(f)

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

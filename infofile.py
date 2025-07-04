import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import re

def on_drop(event):
    print("== Dropped files ==")

    print(event.data)

    # Extract strings inside curly brackets and save to a list
    curly_contents = re.findall(r'\{([^}]*)\}', event.data)
    print("Strings inside curly brackets:", curly_contents)
    files = curly_contents

    print(files)
    for file in files:
        if os.path.isfile(file):
            print("File name:", os.path.basename(file))
            print("Directory:", os.path.dirname(file))
            print("Size (bytes):", os.path.getsize(file))
            print("Last modified:", os.path.getmtime(file))
            print("Created:", os.path.getctime(file))
        else:
            print(f"File does NOT exist: {file}")

# Create the DnD-enabled window
root = TkinterDnD.Tk()
root.title("Drag and Drop")
root.geometry("400x200")

drop_area = tk.Label(root, text="Drop files here", relief="groove", width=40, height=10)
drop_area.pack(padx=10, pady=10)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

root.mainloop()

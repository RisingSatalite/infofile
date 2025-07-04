import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import re

def on_drop(event):
    print("== Dropped files ==")

    #print(event.data)

    # Extract strings inside curly brackets and save to a list
    curly_contents = re.findall(r'\{([^}]*)\}', event.data)
    #print("Strings inside curly brackets: ", curly_contents)

    # Replace everything inside curly braces (including braces) with a space
    new_data = re.sub(r'\{[^}]*\}', ' ', event.data).split(' ')
    #print("Other data not in brakets: ", new_data)

    files = [item for item in curly_contents if item.strip()] + [item for item in new_data if item.strip()]

    print(files, '\n')
    for file in files:
        if os.path.isfile(file):
            print("File name:", os.path.basename(file))
            print("Directory:", os.path.dirname(file))
            print("Size (bytes):", os.path.getsize(file))
            print("Last modified:", os.path.getmtime(file))
            print("Created:", os.path.getctime(file))
            print("\n")
        else:
            print(f"File does NOT exist: {file}")
            print("\n")

# Create the DnD-enabled window
root = TkinterDnD.Tk()
root.title("Drag and Drop")
root.geometry("400x200")

drop_area = tk.Label(root, text="Drop files here", relief="groove", width=40, height=10)
drop_area.pack(padx=10, pady=10)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

root.mainloop()

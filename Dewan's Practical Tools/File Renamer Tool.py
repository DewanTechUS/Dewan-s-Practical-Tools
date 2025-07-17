# File Renamer Tool GUI using Python Tkinter
# With clear step-by-step comments for your GitHub and practice

import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Step 1: Create the main application window
root = tk.Tk()
root.title("File Renamer Tool")
root.geometry("500x300")

# Step 2: Variables to store directory and prefix/suffix
selected_folder = tk.StringVar()
entry_prefix = tk.StringVar()
entry_suffix = tk.StringVar()

# Step 3: Function to select the folder
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        selected_folder.set(folder)

# Step 4: Function to rename files in the selected folder
def rename_files():
    folder = selected_folder.get()
    prefix = entry_prefix.get()
    suffix = entry_suffix.get()

    if not folder:
        messagebox.showerror("Error", "Please select a folder.")
        return

    try:
        files = os.listdir(folder)
        count = 0
        for file_name in files:
            old_path = os.path.join(folder, file_name)
            if os.path.isfile(old_path):
                name, ext = os.path.splitext(file_name)
                new_name = f"{prefix}{name}{suffix}{ext}"
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                count += 1
        messagebox.showinfo("Success", f"Renamed {count} files successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Step 5: UI Elements

# Folder selection
frame_folder = tk.Frame(root)
frame_folder.pack(pady=10)
tk.Label(frame_folder, text="Folder:").grid(row=0, column=0, padx=5)
tk.Entry(frame_folder, textvariable=selected_folder, width=40).grid(row=0, column=1)
tk.Button(frame_folder, text="Browse", command=select_folder).grid(row=0, column=2, padx=5)

# Prefix entry
frame_prefix = tk.Frame(root)
frame_prefix.pack(pady=5)
tk.Label(frame_prefix, text="Prefix:").grid(row=0, column=0, padx=5)
tk.Entry(frame_prefix, textvariable=entry_prefix, width=30).grid(row=0, column=1)

# Suffix entry
frame_suffix = tk.Frame(root)
frame_suffix.pack(pady=5)
tk.Label(frame_suffix, text="Suffix:").grid(row=0, column=0, padx=5)
tk.Entry(frame_suffix, textvariable=entry_suffix, width=30).grid(row=0, column=1)

# Rename button
tk.Button(root, text="Rename Files", command=rename_files, width=20, height=2).pack(pady=20)

# Step 6: Run the main loop
root.mainloop()

# Text Editor GUI using Python Tkinter
# With clear step-by-step comments for your GitHub and practice

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# Step 1: Create the main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("600x500")

# Step 2: Create the text area with scroll
text_area = ScrolledText(root, font=("Arial", 14), undo=True, wrap='word')
text_area.pack(expand=True, fill='both')

# Step 3: Define file operations

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Text Editor - New File")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
            root.title(f"Text Editor - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"Text Editor - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot save file: {e}")

def exit_editor():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# Step 4: Create the menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Step 5: Run the main loop
root.mainloop()

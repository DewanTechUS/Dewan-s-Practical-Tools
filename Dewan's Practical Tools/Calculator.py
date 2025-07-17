# Basic Calculator GUI with Python Tkinter (Step-by-step guide)

import tkinter as tk

# Step 1: Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Step 2: Create entry for display
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Step 3: Function to insert numbers/operators
def button_click(value):
    entry.insert(tk.END, value)

# Step 4: Function to clear the entry
def button_clear():
    entry.delete(0, tk.END)

# Step 5: Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Step 6: Create buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0, 4)
]

# Step 7: Place buttons on the window
for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1

    if text == 'Clear':
        tk.Button(root, text=text, width=32, height=3, command=button_clear).grid(row=row, column=col, columnspan=colspan)
    elif text == '=':
        tk.Button(root, text=text, width=7, height=3, command=button_equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=7, height=3, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Step 8: Run the application
root.mainloop()

# Unit Converter (temperature, weight, length) GUI with Python Tkinter
# Step-by-step structured with clear notes for your resume and GitHub

import tkinter as tk
from tkinter import ttk

# Step 1: Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x400")

# Step 2: Define conversion functions
def convert():
    try:
        value = float(entry.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()
        result = 0

        if category.get() == "Temperature":
            if unit_from == "Celsius" and unit_to == "Fahrenheit":
                result = (value * 9/5) + 32
            elif unit_from == "Fahrenheit" and unit_to == "Celsius":
                result = (value - 32) * 5/9
            elif unit_from == "Celsius" and unit_to == "Kelvin":
                result = value + 273.15
            elif unit_from == "Kelvin" and unit_to == "Celsius":
                result = value - 273.15
            else:
                result = value

        elif category.get() == "Weight":
            if unit_from == "Kilograms" and unit_to == "Pounds":
                result = value * 2.20462
            elif unit_from == "Pounds" and unit_to == "Kilograms":
                result = value / 2.20462
            else:
                result = value

        elif category.get() == "Length":
            if unit_from == "Meters" and unit_to == "Feet":
                result = value * 3.28084
            elif unit_from == "Feet" and unit_to == "Meters":
                result = value / 3.28084
            else:
                result = value

        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(round(result, 4)))
    except:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Error")

# Step 3: Category selection
tk.Label(root, text="Select Category:").pack(pady=5)
category = tk.StringVar()
category.set("Temperature")
category_menu = ttk.Combobox(root, textvariable=category, values=["Temperature", "Weight", "Length"])
category_menu.pack(pady=5)

# Step 4: Entry for value
tk.Label(root, text="Enter Value:").pack(pady=5)
entry = tk.Entry(root, width=20, font=('Arial', 18), justify='center')
entry.pack(pady=5)

# Step 5: From and To unit selection
frame_units = tk.Frame(root)
frame_units.pack(pady=5)

combo_from = ttk.Combobox(frame_units, values=["Celsius", "Fahrenheit", "Kelvin", "Kilograms", "Pounds", "Meters", "Feet"])
combo_from.set("Celsius")
combo_from.grid(row=0, column=0, padx=10)

tk.Label(frame_units, text="to").grid(row=0, column=1)

combo_to = ttk.Combobox(frame_units, values=["Celsius", "Fahrenheit", "Kelvin", "Kilograms", "Pounds", "Meters", "Feet"])
combo_to.set("Fahrenheit")
combo_to.grid(row=0, column=2, padx=10)

# Step 6: Convert button
tk.Button(root, text="Convert", command=convert, width=15, height=2).pack(pady=10)

# Step 7: Result display
tk.Label(root, text="Result:").pack(pady=5)
entry_result = tk.Entry(root, width=20, font=('Arial', 18), justify='center')
entry_result.pack(pady=5)

# Step 8: Run the main loop
root.mainloop()

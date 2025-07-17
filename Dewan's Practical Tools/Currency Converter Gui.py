# Currency Converter (Real-Time API) GUI using Python Tkinter
# Step-by-step with clear notes for learning, GitHub, and resume projects

import tkinter as tk
from tkinter import ttk
import requests

# Step 1: Create the main application window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")

# Step 2: Function to fetch real-time exchange rates using the exchangerate.host free API
def get_rate(from_currency, to_currency):
    try:
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
        response = requests.get(url)
        data = response.json()
        return data['result']
    except:
        return None

# Step 3: Function to perform the conversion and show the result
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()
        rate = get_rate(from_curr, to_curr)

        if rate is not None:
            converted = amount * rate
            entry_result.delete(0, tk.END)
            entry_result.insert(0, str(round(converted, 4)))
        else:
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Error")
    except:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Error")

# Step 4: UI Elements

# Amount entry
tk.Label(root, text="Enter Amount:").pack(pady=5)
entry_amount = tk.Entry(root, width=20, font=('Arial', 18), justify='center')
entry_amount.pack(pady=5)

# From and To currency selection
currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "INR", "CNY"]
frame_curr = tk.Frame(root)
frame_curr.pack(pady=10)

combo_from = ttk.Combobox(frame_curr, values=currencies)
combo_from.set("USD")
combo_from.grid(row=0, column=0, padx=10)

tk.Label(frame_curr, text="to").grid(row=0, column=1)

combo_to = ttk.Combobox(frame_curr, values=currencies)
combo_to.set("EUR")
combo_to.grid(row=0, column=2, padx=10)

# Convert button
tk.Button(root, text="Convert", command=convert_currency, width=15, height=2).pack(pady=20)

# Result display
tk.Label(root, text="Converted Amount:").pack(pady=5)
entry_result = tk.Entry(root, width=20, font=('Arial', 18), justify='center')
entry_result.pack(pady=5)

# Step 5: Run the main application loop
root.mainloop()

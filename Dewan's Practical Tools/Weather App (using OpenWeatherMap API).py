# Weather App (using OpenWeatherMap API) GUI in Python with Tkinter
# Clean, beginner-friendly, job-practice ready code
# You need to sign up at https://openweathermap.org/api to get your API key first

import requests
import tkinter as tk
from tkinter import messagebox

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'

# Function to fetch and display weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        city_name = weather_data['name']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        result_label.config(text=f"City: {city_name}\nTemperature: {temp}°C\nDescription: {description.capitalize()}")

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or API limit reached.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
root.resizable(False, False)

# City entry
city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

def clear_placeholder(event):
    if city_entry.get() == "Enter city name":
        city_entry.delete(0, tk.END)

def add_placeholder(event):
    if not city_entry.get():
        city_entry.insert(0, "Enter city name")

city_entry.bind("<FocusIn>", clear_placeholder)
city_entry.bind("<FocusOut>", add_placeholder)

# Search button
search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
search_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

# Run the app
root.mainloop()

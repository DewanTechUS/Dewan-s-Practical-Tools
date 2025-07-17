# Stopwatch & Timer GUI using Python Tkinter
# With clear step-by-step comments for learning, GitHub, and practice

import tkinter as tk
from tkinter import messagebox
import time

# Step 1: Create the main application window
root = tk.Tk()
root.title("Stopwatch & Timer")
root.geometry("300x300")

# Step 2: Global variables for stopwatch
running = False
start_time = 0
elapsed_time = 0

# Step 3: Function to update the stopwatch display
def update_stopwatch():
    if running:
        global elapsed_time
        elapsed_time = time.time() - start_time
        time_str = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
        label_stopwatch.config(text=time_str)
        root.after(500, update_stopwatch)

# Step 4: Start, Stop, and Reset functions for stopwatch
def start():
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        update_stopwatch()

def stop():
    global running
    running = False

def reset():
    global running, elapsed_time
    running = False
    elapsed_time = 0
    label_stopwatch.config(text="00:00:00")

# Step 5: Timer functionality
def start_timer():
    try:
        total_seconds = int(entry_timer.get())
        countdown(total_seconds)
    except:
        messagebox.showerror("Invalid Input", "Please enter the time in seconds.")

def countdown(seconds_left):
    if seconds_left >= 0:
        mins, secs = divmod(seconds_left, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        label_timer.config(text=timeformat)
        root.after(1000, countdown, seconds_left - 1)
    else:
        messagebox.showinfo("Time's up!", "The countdown has finished.")

# Step 6: Create UI elements
# Stopwatch section
tk.Label(root, text="Stopwatch", font=("Arial", 14)).pack(pady=5)
label_stopwatch = tk.Label(root, text="00:00:00", font=("Arial", 24))
label_stopwatch.pack()

frame_sw = tk.Frame(root)
frame_sw.pack(pady=5)
tk.Button(frame_sw, text="Start", command=start, width=8).grid(row=0, column=0, padx=5)
tk.Button(frame_sw, text="Stop", command=stop, width=8).grid(row=0, column=1, padx=5)
tk.Button(frame_sw, text="Reset", command=reset, width=8).grid(row=0, column=2, padx=5)

# Timer section
tk.Label(root, text="\nTimer (seconds)", font=("Arial", 14)).pack()
entry_timer = tk.Entry(root, width=10, font=('Arial', 18), justify='center')
entry_timer.pack(pady=5)
tk.Button(root, text="Start Timer", command=start_timer, width=15).pack(pady=5)
label_timer = tk.Label(root, text="00:00", font=("Arial", 24))
label_timer.pack(pady=5)

# Step 7: Run the main application loop
root.mainloop()

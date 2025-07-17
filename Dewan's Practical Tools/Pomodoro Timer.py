# Pomodoro Timer GUI using Python Tkinter
# With clear, structured step-by-step comments for your GitHub and learning

import tkinter as tk
from tkinter import messagebox
import time

# Step 1: Create the main application window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("300x250")

# Step 2: Initialize variables
work_time = 25 * 60  # 25 minutes
break_time = 5 * 60   # 5 minutes
is_running = False
current_time = work_time
on_break = False

# Step 3: Update timer display
def update_timer():
    global current_time, is_running, on_break
    if is_running:
        if current_time > 0:
            mins, secs = divmod(current_time, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label_timer.config(text=time_format)
            current_time -= 1
            root.after(1000, update_timer)
        else:
            if not on_break:
                messagebox.showinfo("Time's up!", "Work session completed. Time for a break!")
                start_break()
            else:
                messagebox.showinfo("Break Over", "Break time is over. Back to work!")
                start_work()

# Step 4: Start work session
def start_work():
    global current_time, is_running, on_break
    current_time = work_time
    on_break = False
    is_running = True
    update_timer()

# Step 5: Start break session
def start_break():
    global current_time, is_running, on_break
    current_time = break_time
    on_break = True
    is_running = True
    update_timer()

# Step 6: Pause the timer
def pause_timer():
    global is_running
    is_running = False

# Step 7: Reset the timer
def reset_timer():
    global is_running, current_time, on_break
    is_running = False
    current_time = work_time
    on_break = False
    label_timer.config(text="25:00")

# Step 8: Create UI Elements
tk.Label(root, text="Pomodoro Timer", font=("Arial", 16)).pack(pady=10)
label_timer = tk.Label(root, text="25:00", font=("Arial", 36))
label_timer.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Start", command=start_work, width=8).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Pause", command=pause_timer, width=8).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Reset", command=reset_timer, width=8).grid(row=0, column=2, padx=5)

# Step 9: Run the main loop
root.mainloop()

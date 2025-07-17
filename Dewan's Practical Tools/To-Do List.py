import tkinter as tk  # Import tkinter for creating GUI
from tkinter import messagebox, simpledialog  # Import message boxes and simple dialogs

# Create the main To-Do List Application class
class TodoApp:
    def __init__(self, root):
        self.root = root  # Main window
        self.root.title("To-Do List")  # Window title

        self.tasks = []  # List to store tasks

        # Frame to hold the listbox and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, padx=10)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(self.frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link scrollbar to the listbox
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Entry field to add new tasks
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)

        # Frame for the buttons below the entry field
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        # Button to add a new task
        add_button = tk.Button(button_frame, text="Add Task", width=12, command=self.add_task)
        add_button.grid(row=0, column=0, padx=5)

        # Button to edit the selected task
        edit_button = tk.Button(button_frame, text="Edit Task", width=12, command=self.edit_task)
        edit_button.grid(row=0, column=1, padx=5)

        # Button to delete the selected task
        delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=self.delete_task)
        delete_button.grid(row=0, column=2, padx=5)

        # Button to mark a task as complete
        complete_button = tk.Button(button_frame, text="Mark Complete", width=12, command=self.mark_complete)
        complete_button.grid(row=0, column=3, padx=5)

    # Method to add a task to the list
    def add_task(self):
        task = self.entry.get().strip()  # Get text from entry
        if task:  # Check if not empty
            self.tasks.append(task)  # Add to task list
            self.update_listbox()  # Refresh the listbox display
            self.entry.delete(0, tk.END)  # Clear entry field
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")  # Warning if empty

    # Method to edit a selected task
    def edit_task(self):
        selected = self.task_listbox.curselection()  # Get selected index
        if selected:
            current_task = self.tasks[selected[0]]  # Get current task
            new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=current_task)  # Ask for new task text
            if new_task:
                self.tasks[selected[0]] = new_task.strip()  # Update task
                self.update_listbox()  # Refresh display
        else:
            messagebox.showwarning("Select Task", "Please select a task to edit.")  # Warning if nothing selected

    # Method to delete a selected task
    def delete_task(self):
        selected = self.task_listbox.curselection()  # Get selected index
        if selected:
            del self.tasks[selected[0]]  # Delete from list
            self.update_listbox()  # Refresh display
        else:
            messagebox.showwarning("Select Task", "Please select a task to delete.")  # Warning if nothing selected

    # Method to mark a task as completed
    def mark_complete(self):
        selected = self.task_listbox.curselection()  # Get selected index
        if selected:
            task = self.tasks[selected[0]]
            if not task.startswith("✔️ "):  # Check if not already marked
                self.tasks[selected[0]] = "✔️ " + task  # Add checkmark
                self.update_listbox()  # Refresh display
        else:
            messagebox.showwarning("Select Task", "Please select a task to mark as complete.")  # Warning if nothing selected

    # Method to refresh the listbox with current tasks
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear current listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Insert each task

# Run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = TodoApp(root)  # Create the To-Do app object
    root.mainloop()  # Run the event loop

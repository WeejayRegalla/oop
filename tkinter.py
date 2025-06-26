import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Task class
class Task:
    def __init__(self, title, due_date, category):
        self.title = title
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️ Done" if self.completed else "❗ Pending"
        return f"{self.title} | {self.category} | {self.due_date.date()} | {status}"

# StudySession class
class StudySession(Task):
    def __init__(self, title, due_date, subject, duration_hours):
        super().__init__(title, due_date, "Study Session")
        self.subject = subject
        self.duration_hours = duration_hours

    def __str__(self):
        base = super().__str__()
        return f"{base} | Subject: {self.subject} | Duration: {self.duration_hours} hr(s)"

# GUI App
class StudyBuddyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📘 StudyBuddy GUI")

        self.tasks = []

        # Input Fields
        tk.Label(root, text="Task Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        tk.Label(root, text="Due Date (YYYY-MM-DD)").grid(row=1, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1)

        # Dropdown for task type
        tk.Label(root, text="Type").grid(row=2, column=0)
        self.task_type = tk.StringVar(value="Task")
        tk.OptionMenu(root, self.task_type, "Task", "Study Session", command=self.toggle_inputs).grid(row=2, column=1)

        # Category (for Task)
        self.category_label = tk.Label(root, text="Category")
        self.category_label.grid(row=3, column=0)
        self.category = tk.StringVar(value="Assignment")
        self.category_menu = tk.OptionMenu(root, self.category, "Assignment", "Quiz", "Exam", "Other")
        self.category_menu.grid(row=3, column=1)

        # Subject (for Study Session)
        self.subject_label = tk.Label(root, text="Subject")
        self.subject_entry = tk.Entry(root)
        self.duration_label = tk.Label(root, text="Duration (hr)")
        self.duration_entry = tk.Entry(root)

        # Buttons
        tk.Button(root, text="➕ Add", command=self.add_task).grid(row=6, column=0, pady=10)
        tk.Button(root, text="📋 View All Tasks", command=self.refresh_task_list).grid(row=6, column=1)
        tk.Button(root, text="✅ Mark as Done", command=self.mark_done).grid(row=6, column=2)
        tk.Button(root, text="🗑️ Delete", command=self.delete_task).grid(row=6, column=3)

        # Task List Display
        self.task_listbox = tk.Listbox(root, width=90)
        self.task_listbox.grid(row=7, column=0, columnspan=4, pady=10)

        self.toggle_inputs("Task")  # Initial layout setup

    def toggle_inputs(self, task_type):
        if task_type == "Task":
            # Show category
            self.category_label.grid(row=3, column=0)
            self.category_menu.grid(row=3, column=1)
            # Hide study session fields
            self.subject_label.grid_forget()
            self.subject_entry.grid_forget()
            self.duration_label.grid_forget()
            self.duration_entry.grid_forget()
        else:
            # Hide category
            self.category_label.grid_forget()
            self.category_menu.grid_forget()
            # Show study session fields
            self.subject_label.grid(row=3, column=0)
            self.subject_entry.grid(row=3, column=1)
            self.duration_label.grid(row=4, column=0)
            self.duration_entry.grid(row=4, column=1)

    def add_task(self):
        title = self.title_entry.get().strip()
        due = self.date_entry.get().strip()
        task_type = self.task_type.get()

        if not title or not due:
            messagebox.showwarning("Missing Info", "Please fill in all required fields.")
            return

        try:
            if task_type == "Task":
                category = self.category.get()
                task = Task(title, due, category)
            else:
                subject = self.subject_entry.get().strip()
                duration = self.duration_entry.get().strip()
                if not subject or not duration:
                    messagebox.showwarning("Missing Info", "Subject and Duration required for study session.")
                    return
                if not duration.isdigit():
                    messagebox.showerror("Invalid Duration", "Duration must be a number.")
                    return
                task = StudySession(title, due, subject, int(duration))
            self.tasks.append(task)
            self.refresh_task_list()
        except ValueError:
            messagebox.showerror("Invalid Date", "Date must be in YYYY-MM-DD format.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("No Selection", "Select a task to mark as done.")
            return
        index = selected[0]
        self.tasks[index].mark_completed()
        self.refresh_task_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("No Selection", "Select a task to delete.")
            return
        index = selected[0]
        deleted = self.tasks.pop(index)
        self.refresh_task_list()
        messagebox.showinfo("Deleted", f"Deleted: {deleted.title}")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

# Run the GUI
root = tk.Tk()
app = StudyBuddyApp(root)
root.mainloop()

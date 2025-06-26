from datetime import datetime

class Task:
    def __init__(self, title, due_date, category):
        self.title = title
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.category = category
        self.completed = False

# kapag tapos na ang task
    def mark_completed(self): 
        self.completed = True

# object string dito mapupunta ang nasa class task

    def __str__(self):
        status = "✔️ Done" if self.completed else "❗ Pending"
        return f"[{status}] {self.title} ({self.category}) - Due: {self.due_date.date()}"
    
# Studdy session
class StudySession(Task):
    def __init__(self, title, due_date, subject, duration_hours):
        super().__init__(title, due_date, "Study Session")
        self.subject = subject
        self.duration_hours = duration_hours

    def __str__(self):
        object = super().__str__()
        return f"{object} | Subject: {self.subject} | Duration: {self.duration_hours} hr(s)"
    
# User 
class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for number, task in enumerate(self.tasks, 1):
            print(f"{number}. {task}")
    
    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

# Main App 
def main():
    print("🎓 Welcome to StudyBuddy!")

    while True:
        print("🔔 Reminder: it should have your name.")
        name = input("Enter your name: ").strip()
        if not name:
            print("❌ Provide your name.")
            continue

        user = User(name)

        while True:
            print(f"\nHi {user.name}! What would you like to do?")
            print("1. Add Task")
            print("2. Add Study Session")
            print("3. View All Tasks")
            print("4. Mark Task as Done")
            print("5. Delete Task")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == "1":
                print("🔔 Reminder: it should have a title.")
                title = input("Enter task title: ").strip()
                if not title:
                    print("❌ Provide title of your task.")
                    continue
                print("🔔 Reminder: it should have a due date.")
                due = input("Enter due date (YYYY-MM-DD): ").strip()
                if not due:
                    print("❌ Provide due date of your task.")
                    continue
                print("🔔 Reminder: it should have a category.")
                category = input("Enter category (Assignment/Quiz/Exam/Other): ").strip()
                if not category:
                    print("❌ You did not put category.")
                    continue

                task = Task(title, due, category)
                user.add_task(task)
                print("✅ Task added!")

            elif choice == "2":
                print("🔔 Reminder: it should have a title.")
                title = input("Enter session title: ")
                print("🔔 Reminder: it should have a due date.")
                due = input("Enter session date (YYYY-MM-DD): ")
                print("🔔 Reminder: it should have a subject.")
                subject = input("Enter subject: ")
                print("🔔 Reminder: It can have a duration of time or it may not.")
                duration = int(input("Enter duration in hours: "))
                session = StudySession(title, due, subject, duration)
                user.add_task(session)
                print("✅ Study session added!")

            elif choice == "3":
                print("\n📋 Your Tasks:")
                user.list_tasks()
                input("\n⏪ Press enter to go back to menu...")

            elif choice == "4":
                user.list_tasks()
                user_input = input("\nEnter task number to mark as done or type 'back' to return in menu: ").strip().lower()
                if user_input == "back":
                    pass  
                else:
                    try:
                        index = int(user_input) - 1
                        user.mark_task_done(index)
                    except ValueError:
                        print("❌ Please enter a valid number.")
            elif choice == "5":
                user.list_tasks()
                user_input = input("\Enter task number to delete or type 'back' to return in menu ").strip().lower()
                if user_input == "back":
                    pass
                else:
                    try:
                        index = int(user_input) - 1
                        if 0 <= index < len(user.tasks):
                            task_to_delete = user.tasks[index]
                            confirm = input(f"❓ Are you sure you want to delete this task'{task_to_delete.title}'? (yes/no): ").lower()
                            if confirm == "yes":
                                deleted_task = user.tasks.pop(index)
                                print(f"🗑️ Succesfully deleted: {deleted_task.title}")
                            else:
                                print("❌ Deleting task was denied.")
                        else:
                            print("⚠️ Invalid task number.")
                    except ValueError:
                        print("❌ Please enter a valid number.")


            elif choice == "6":
                print("👋 Goodbye! Happy studying!")
                return  # ← this will exit the whole program

            else:
                print("Invalid choice. Try again.")

main()
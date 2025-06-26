from datetime import datetime, timedelta

class Task:
    def __init__(self, title, due_date, category):
        self.title = title
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d %I:%M %p')
        self.category = category
        self.completed = False

# kapag tapos na ang task
    def mark_completed(self): 
        self.completed = True

# object string dito mapupunta ang nasa class task

    def __str__(self):
        status = "✔️ Done" if self.completed else "❗ Pending"
        return f"[{status}] {self.title} ({self.category}) - Due: {self.due_date.strftime('%Y-%m-%d %I:%M %p')}"
    
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

    def check_upcoming_tasks(self):
        now = datetime.now()
        found = False
        print("\n🔔 Upcoming Deadlines:")
        for task in self.tasks:
            if not task.completed:
                time_left = task.due_date - now
                if timedelta(minutes=0) <= time_left <= timedelta(minutes=15):
                    print(f"⚠️ Due soon (within 15 mins): {task.title} at {task.due_date.strftime('%I:%M %p')}")
                    found = True
                elif time_left < timedelta(minutes=0):
                    print(f"❌ OVERDUE: {task.title} (was due at {task.due_date.strftime('%Y-%m-%d %I:%M %p')})")
                    found = True
                elif task.due_date.date() == now.date():
                    print(f"📅 Due today: {task.title} at {task.due_date.strftime('%I:%M %p')}")
                    found = True
                elif task.due_date.date() == (now.date() + timedelta(days=1)):
                    print(f"🕑 Due tomorrow: {task.title} at {task.due_date.strftime('%I:%M %p')}")
                    found = True
        if not found:
            print("✅ No upcoming tasks.")

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
            print(f"\nHi {user.name}!")
            user.check_upcoming_tasks()
            print("\nWhat would you like to do?")
            print("1. Add Task")
            print("2. Add Study Session")
            print("3. View All Tasks")
            print("4. Mark Task as Done")
            print("5. Delete Task")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == "1":
                title = input("Enter task title: ").strip()
                if not title:
                    print("❌ Title is required.")
                    continue
                due = input("Enter due date and time (YYYY-MM-DD HH:MM AM/PM): ").strip()
                if not due:
                    print("❌ Due date is required.")
                    continue
                category = input("Enter category (Assignment/Quiz/Exam/Other): ").strip()
                if not category:
                    print("❌ Category is required.")
                    continue

                try:
                    task = Task(title, due, category)
                    user.add_task(task)
                    print("✅ Task added!")
                except ValueError:
                     print("❌ Format must be: YYYY-MM-DD HH:MM AM/PM")

            elif choice == "2":
                title = input("Enter session title: ").strip()
                due = input("Enter session date and time (YYYY-MM-DD HH:MM AM/PM): ").strip()
                subject = input("Enter subject: ").strip()
                try:
                    duration = int(input("Enter duration in hours: "))
                    session = StudySession(title, due, subject, duration)
                    user.add_task(session)
                    print("✅ Study session added!")
                except ValueError:
                    print("❌ Duration must be a number.")

            elif choice == "3":
                print("\n📋 Your Tasks:")
                user.list_tasks()
                input("\n⏪ Press enter to go back to menu...")

            elif choice == "4":
                user.list_tasks()
                user_input = input("\nEnter task number to mark as done or type 'back' to return in menu: ").strip().lower()
                if user_input == "back":
                    continue
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
                    continue
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

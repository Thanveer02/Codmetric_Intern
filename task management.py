# File to store tasks
TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = {}
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                if "|" in line:
                    name, status = line.strip().split(" | ")
                    tasks[name] = status == "True"
    except FileNotFoundError:
        pass  # No tasks yet
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for name, completed in tasks.items():
            file.write(f"{name} | {completed}\n")

# Add a new task
def add_task(tasks, name):
    if name in tasks:
        print("⚠️ Task already exists.")
    else:
        tasks[name] = False
        print("✅ Task added.")

# Delete a task
def delete_task(tasks, name):
    if name in tasks:
        del tasks[name]
        print("🗑️ Task deleted.")
    else:
        print("❌ Task not found.")

# Mark a task as completed
def complete_task(tasks, name):
    if name in tasks:
        tasks[name] = True
        print("✔️ Task marked as completed.")
    else:
        print("❌ Task not found.")

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📝 Task List:")
    for i, (name, done) in enumerate(tasks.items(), 1):
        status = "✅" if done else "❌"
        print(f"{i}. {name} [{status}]")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Show Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            add_task(tasks, name)
        elif choice == "2":
            name = input("Enter task name to delete: ")
            delete_task(tasks, name)
        elif choice == "3":
            name = input("Enter task name to mark as completed: ")
            complete_task(tasks, name)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

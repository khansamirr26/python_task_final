tasks = []

def add_task():
    print("\n--- Add New Task ---")
    title = input("Enter Task Title: ")
    tasks.append({"title": title, "status": "New"})
    print(f"\nTask '{title}' added successfully with status 'New'.\n")

def list_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n--- Task List ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['status']}")
    print()

def edit_task():
    list_tasks()
    try:
        task_num = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            new_title = input("Enter the new title for the task: ")
            tasks[task_num]["title"] = new_title
            print("\nTask updated successfully.\n")
        else:
            print("\nInvalid task number!\n")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.\n")

def remove_task():
    list_tasks()
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"\nTask '{removed_task['title']}' removed successfully.\n")
        else:
            print("\nInvalid task number!\n")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.\n")

def main():
    while True:
        print("\n--- To-Do List App ---")
        print("1. Add New Task")
        print("2. List All Tasks")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.\n")

if __name__ == "__main__":
    main()

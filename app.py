from database import init_db, add_task, get_tasks, delete_task

def display_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    tasks = get_tasks()
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTasks:")
        for task in tasks:
            print(f"{task['id']}. {task['title']} - {task['description']}")

def add_new_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    add_task(title, description)
    print("\nTask added successfully!")

def remove_task():
    task_id = input("Enter task ID to delete: ")
    delete_task(task_id)
    print("\nTask deleted successfully!")

def main():
    init_db()  # Initialize the database

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_new_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
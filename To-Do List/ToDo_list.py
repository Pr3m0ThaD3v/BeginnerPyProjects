# A simple to do list

# create an empty list to store task

tasks = []


# define a function to add task to a list

def add_task():
    task = input("Enter task:")
    tasks.append(task)
    print("Task added successfully!")


# Define a function to view task in a list
def view_tasks():
    if not tasks:
        print("No tasks in the list.")

    else:
        print("Tasks in the list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Define a function to remove task from a list

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the number of the task to remove: "))
            if 1 <= task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                print(f"Task '{remove_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("No tasks to remove.")


# Main loop for the To-Do List application
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting the To-Do List Application. Peace!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

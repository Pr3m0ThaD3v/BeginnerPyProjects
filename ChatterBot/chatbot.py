# Building a Python app with CRUD (Create, Read, Update, Delete)

import sqlite3


# CREATE
# Function to create a new task

def create_task(conn, task):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (task['title'], task['description']))
    conn.commit()
    print("Task created successfully.")


# READ
# Function to read all tasks
def read_all_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task")
    rows = cursor.fetchall()

    if not rows:
        print("No task found")
    else:
        print("Task:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}")


# UPDATE
# Function to update a task
def update_task(conn, task_id, new_title, new_description):
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?", (new_title, new_description, task_id))
    conn.commit()
    print("Task updated successfully.")


# DELETE
# Function to delete a task
def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully.")


# Main function to manage the app
def main():
    # Connect to SQLite database (creates a new file 'tasks.db' if it doesn't exist)
    conn = sqlite3.connect('task.db')

    # Create task table if it does not exist
    conn.execute('''
        CREATE TABLE IF IT DOES NOT EXIST tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
                
        )
    ''')

    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. Read All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5)")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = {'title': title, 'description': description}
            create_task(conn, task)
        elif choice == '2':
            read_all_tasks(conn)
        elif choice == '3':
            task_id = input("Enter task ID to create update: ")
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            update_task(conn, task_id, new_title, new_description)
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(conn, task_id)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    # Clos the database connection when exiting the program
    conn.close()


if __name__ == "__main__":
    main()

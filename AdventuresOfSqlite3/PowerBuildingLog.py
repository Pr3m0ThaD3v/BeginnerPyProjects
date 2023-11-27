# Sqlite3 workout log

import sqlite3

# Setup SQKite database

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('workout_tracker.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store workout data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT, 
    year INTEGER,
    exercise_type TEXT,
    weight INTEGER,
    reps INTEGER,
    sets INTEGER
    )

''')


# Commit changes and close connections
# End

# User input and Data Insertion
# Prompt users to input data
def add_workout():
    # Connect to the database
    conn = sqlite3.connect('workout_tracker.db')
    cursor = conn.cursor()

    # Prompt user for workout details
    month = input("Enter the month:  ")
    year = input("Enter the year:")
    exercise_type = input("Enter the type of exercise: ")
    weight = int(input("Enter the number of reps: "))
    reps = int(input("Enter the number of reps: "))
    sets = int(input("Enter the number of sets: "))

    # Insert data into the database
    cursor.execute('''
        INSERT INTO workouts (month, year, exercise_type, weight,
        reps,
        sets,
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (month, year, exercise_type, weight, reps,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Call the function to add a workout
add_workout()


# End

# Retrieve and Display Data
# create a function to retrieve and display workout data from the database.
# Step 3: Retrieve and Display Data
def display_workouts():
    # Connect to the database
    conn = sqlite3.connect('workout_tracker.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM workouts')
    workouts = cursor.fetchall()

    if not workouts:
        print("No workout data found.")
    else:
        print("\nWorkout Data:")
        print("ID | Month | Year | Exercise Type | Weight (lbs) | Reps | Sets")
        print("-" * 60)
        for workout in workouts:
            print(
                f"{workout[0]} | {workout[1]} | {workout[2]} | {workout[3]} | {workout[4]} | {workout[5]} | {workout[6]}")

    conn.close()


# Call the function to display workout data
display_workouts()

# End of script

# Exspence tracker SQLite3 backend

import sqlite3
from datetime import datetime

# Function to create new expense
# Create
def add_expense(conn, expense):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?,?,?)", (expense['category'],expense['amount'],expense['date']))
    conn.commit()
    print("Expense added successfully.")
    

# Function to view all expenses
# Read
def view_expenses(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    if not rows:
        print("No expenses found.")
    else:
        print("Expenses:")
        for row in rows:
            print(f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Date: {row[3]}")


# Function to analyze expenses by category
def analyze_expenses(conn):
    cursor = conn.cursor()  
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    
    if not rows:
        print("No expenses found.")
    else:
        print("Expense Analysis:")
        for row in rows:
            print(f"Category: {row[0]}, Total Amount: {row[1]}")
            
            
# Main function to manage the expense tracker
def main():
    # Connect to SQLite database (create a new file 'expenses.db' if it doesn't exist)
    conn = sqlite3.connect('expenses.db')
    
    # Create expenses table if not exists
    conn.execute('''
                 CREATE TABLE IF NOT EXISTS expenses (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     category TEXT NOT NULL,
                     amount REAL NOT NULL,
                     date TEXT NOT NULL
                )
            ''')           

            
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Analyze Expenses by Category")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            expense = {'category': category, 'amount': amount, 'date': date}
            add_expense(conn, expense)
        elif choice == '2':
            view_expenses(conn)
        elif choice == '3':
            analyze_expenses(conn)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. PLease enter a number between 1 and 4.")
    
    
    # Close the databse connection when exiting the program
    conn.close()
    

if __name__ == "__main__":
    main()    
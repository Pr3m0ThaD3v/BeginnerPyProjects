# Script for UA management

import subprocess


# Function to create a new user account

def create_user():
    # prompt for username and password
    uname = input("Enter the new username: ")

    passwd = input(f"Enter the password for the new user {uname}: ")

    try:

        # Create new user account
        command = f"net user {uname} {passwd} /add"

        # Use subprocess to run the command
        subprocess.run(command, shell=True)

        # Print a message indicating the success of the operation
        print(f"User account '{uname}' created successfully.")
    except subprocess.CalledProcessError as e:
        # Print and message if the command fails
        print(f"Error creating username account: {e}")


# Function to delete an existing user account
def delete_user():
    # Prompt the user for the username to be deleted
    uname = input("Enter the username to delete")

    try:
        # Command to delete an existing user account
        command = f"net user {uname} /delete"

        # Use subprocess to run the command
        subprocess.run(command, shell=True, check=True)

        # Print a message indicating the success of the operation
        print(f"User account '{uname}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        # Print an error message if the command fails
        print(f"Error deleting user account: {e}")


# Main script

while True:
    # Prompt the user to choose an action
    print("\nChoose an action:")
    print("1. Create user account")
    print("2. Delete user account")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3):")

    if choice == '1':
        create_user()
    elif choice == '2':
        delete_user()
    elif choice == '3':
        print("Exiting the script. Goodbye!")

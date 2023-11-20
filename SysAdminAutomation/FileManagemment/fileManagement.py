# Automate File Managment (Windows)
# A script that organizes files in a directory by moving them to specific 
# folders based on their file types.


import os
import shutil

# Making the automation interactive
def get_user_input():
    print("Choose the source directory: ")
    print("1. Home Directory")
    print("2. List available directories")
    print("3. Enter a custom path")
    
    choice = (input("Enter the number of your choice: "))
    if choice == '1':
        return os.path.expanduser("~") # User's home dir
    elif choice == "2":
        print("Available directories")
        available_dirs = [d for d in os.listdir() if os.path.isdir(d)]
        for i, directory in enumerate(available_dirs, start=1):
            print(f"{i}. {directory}")
        dir_choice = input("Enter the number of the directory: ")
        return os.path.abspath(available_dirs[int(dir_choice) - 1])
    elif choice == "3":
        custom_path = input("Enter the custom path: ")
        return os.path.abspath(custom_path)
    else:
        print("Invalid choice. Using the home directory.")
        return os.path.expanduser(".")
    
# End of user interaction script

# Code for file management
def organize_files(source_dir):
    source_dir = os.path.abspath(source_dir) # Ensure source_dir is a strin
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(file_path):
            # Determine the file type based on the file extension
            file_type = filename.split('.')[-1].lower()
            
            # Create directories if they don't exist
            target_dir = os.path.join(source_dir, file_type)
            os.makedirs(target_dir, exist_ok=True)
            
            # Move the file to the corresponding directory
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved {filename} to {file_type} directory.")
        

if __name__ == "__main__":
    # Call user input function
    source_directory = get_user_input()
    organize_files(source_directory)

           
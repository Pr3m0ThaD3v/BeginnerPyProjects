# Simple backup script

import shutil, os, datetime, transformers, certifi
from transformers import pipeline

# Load the text generation model
generator = pipeline("text-generation")


def generate_prompt():
    prompt = """
     Hello Aakeem,
     I am a helpful assistant that organizes files. Given a source directory, you can create a backup.
     - To start, tell me the path to the directory you want to back up.
     - Next, let me know where you'd like to store the backup.
    """
    return generator(prompt, max_length=100, num_return_sequences=1, temperature=0.7)[0]['generated_text']


# End

# Backup Script
def backup_directory(source_directory, backup_location):
    # timestamp to distinguish backups
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Backup dir path
    backup_path = os.path.join(source_directory, f"backup+{timestamp}")

    try:
        # Copy source dir to destination
        shutil.copytree(source_directory, backup_path)
        print(f"Backup created successfully at: {backup_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Generate prompts using AI
    source_directory = input(generate_prompt())
    backup_location = input(generate_prompt())

    # Call the backup function
    backup_directory(source_directory, backup_location)

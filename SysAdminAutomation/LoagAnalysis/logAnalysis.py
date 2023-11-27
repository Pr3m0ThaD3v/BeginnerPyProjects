# A script for system event logging

import re


def analyze_log(log_file_path):
    try:
        # Open the log file in read mode
        with open(log_file_path, 'r', encoding='utf-16-le', errors='replace') as log_file:
            log_lines = log_file.readlines()

            # Define a regular expression pattern for extracting log levels
            log_level_pattern = re.compile(r'\[([A-Za-z]+)]')

            # Dictionary to store log level counts
            log_level_counts = {}

            # Iterate through each log line
            for line in log_lines:
                # Use the regular expression to extract the log level
                match = log_level_pattern.search(line)
                if match:
                    log_level = match.group(1)

                    # Update the log level count in the dictionary
                    log_level_counts[log_level] = log_level_counts(log_level, 0) + 1

                # Print the log level counts
                print("Log Level Counts")
                for level, count in log_level_counts.items():
                    print(f"{level}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
    except Exception as e:
        print(f"Error analyzing log file: {e}")

# Run with admin
# C:\Windows\System32\winevt\Logs\Application.evtx
# Provide the path to a log file
log_file_path = input("path/to/your/log/file.log: ")
analyze_log(log_file_path)

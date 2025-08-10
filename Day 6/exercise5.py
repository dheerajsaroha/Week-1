# Write a program to log messages with the timestamps into file
from datetime import datetime

def log_message(filename, message):
    try:
        with open(filename, "a") as file:  # "a" for append mode
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")
        print("Message logged successfully.")
    except PermissionError:
        print("Permission denied: Cannot write to the file.")

# Example usage
log_message("logfile.txt", "Application started")
log_message("logfile.txt", "User logged in")
log_message("logfile.txt", "Error occurred while processing data")
with open("logfile.txt","r") as file:
    content = file.read()
    print(content)

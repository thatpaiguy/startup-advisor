import sys
import atexit

class Logger:
    def __init__(self, log_file_path):
        self.terminal = sys.stdout
        self.log = open(log_file_path, "w")

    def write(self, message):
        self.log.write(message)
    
    def flush(self):
        try:
            self.log.flush()
        except ValueError:
            pass  # The file is already closed


# Redirect all stdout to a file
sys.stdout = Logger("output.log")

# Optional: Close log file on exit
@atexit.register
def close_log():
    sys.stdout.log.close()

# Function to print to both console and file
def print_to_console_also(*args, **kwargs):
    print(*args, **kwargs)  # Goes to file
    print(*args, **kwargs, file=sys.__stdout__)  # Goes to console


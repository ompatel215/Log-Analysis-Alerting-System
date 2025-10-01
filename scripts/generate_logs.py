import random
import datetime
import os


#Possible severity levels for log entries
SEVERITIES = ["INFO", "DEBUG", "NOTICE", "EMERGENCY", "WARNING", "ERROR", "TRACE", "CRITICAL"]

#Generates a list of 1000 random log entries
def generate_logs(num=1000):
    logs = []
    for _ in range(num):

        #Randomly pick how long ago the log occurred (0 - 30 days)
        days_ago = random.randint(0, 30)

        #Random offset (in seconds) within the day
        seconds_offset = random.randint(0, 86400)

        #Computes the actual timestamp by subtracting days and seconds from now
        timestamp = (datetime.datetime.now() - datetime.timedelta(days=days_ago, seconds=seconds_offset))
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        #Randomly picks a severity level for the log
        severity = random.choice(SEVERITIES)

        #Creates a random system event message
        message = f"System event {random.randint(1000, 9999)}"
        logs.append(f"{timestamp} | {severity} | {message}")
    return logs

#Saves a list of log entries to a directory called 'logs'
def save_logs(logs, filename="logfiles.log", folder="../logs"):

    #Ensures that the directory 'logs' exist before writing a new directory
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as f:
        f.write("\n".join(logs))
        return filepath

#Generates 1000 log entries
logs = generate_logs(1001)

#Saves the logs to a file and gets the file path
path = save_logs(logs)

#Prints a confirmation message that the logs has been saved
print(f"Logs saved to {path}")

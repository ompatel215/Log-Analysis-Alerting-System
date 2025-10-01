import os
from datetime import datetime

LOG_FILE = "../logs/logfiles.log"

def parse_log_line(line):
    """
    Parses a single log line of the format:
    YYYY-MM-DD HH:MM:SS | SEVERITY | MESSAGE
    """
    try:
        timestamp_str, severity, message = [part.strip() for part in line.split("|", 2)]
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return {
            "timestamp": timestamp,
            "severity": severity,
            "message": message
        }
    except ValueError as e:
        print(f"Failed to parse line: {line.strip()} | Error: {e}")
        return None


def parse_log_file(filepath=LOG_FILE):
    """
    Parses the entire log file and returns a list of structured logs.
    """
    parsed_logs = []
    if not os.path.exists(filepath):
        print(f"Log file not found at {filepath}")
        return parsed_logs

    with open(filepath, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                parsed_logs.append(parsed)

    return parsed_logs


if __name__ == "__main__":
    logs = parse_log_file(LOG_FILE)
    print(f"Parsed {len(logs)} logs successfully.")

    # Example: Print first 5 parsed logs
    for log in logs[:5]:
        print(log)

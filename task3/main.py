import sys
import re
from typing import Dict, Any

from display import display_counts, display_logs
from enums.LogLevel import LogLevel

def parse_log_line(line: str) -> Dict[str, Any]:
    # regexp where the first group is a date, second is a debug level, third group is a message
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|ERROR|DEBUG|WARNING) (.+)'
    match = re.match(pattern, line)
    if match:
        return {'date': match.group(1), 'level': LogLevel(match.group(2)), 'message': match.group(3)}    
    else:
        print(f"Invalid log: {line}")
        return None

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:
            logs = [parse_log_line(line.strip()) for line in file]
    except FileNotFoundError:
        print("Log file not found!")
        return []

    # filter if not None, because parse_log_line migth return it
    return list(filter(lambda log: log is not None, logs))

def group_logs_by_level(logs: list) -> Dict[LogLevel, list]:
    # create empty dict from enum
    grouped_logs = {level: [] for level in LogLevel}

    for log in logs:        
        grouped_logs[log['level']].append(log)
    return grouped_logs

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path> [<log_level>]")
        return
    
    log_file_path = sys.argv[1]
    level = None
    if len(sys.argv) == 3:
        level = LogLevel(sys.argv[2].upper())        

    logs = load_logs(log_file_path)

    grouped_logs = group_logs_by_level(logs)
    display_counts(grouped_logs)
    if level:
        display_logs(level, grouped_logs[level])

if __name__ == "__main__":
    main()

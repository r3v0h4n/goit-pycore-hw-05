from enums.LogLevel import LogLevel

def display_counts(grouped_logs: list):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, logs in grouped_logs.items():
        print(f"{level.name.ljust(17)}| {len(logs)}")

def display_logs(level: LogLevel, logs: list):
    print(f"\nДеталі логів для рівня '{level.name}':")
    for log in logs:
        print(f"{log["date"]} - {log["message"]}") 
    
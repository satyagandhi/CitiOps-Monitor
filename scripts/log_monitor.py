log_files = ["logs/app_log.txt", "logs/server_log.txt"]

error_count = 0
warning_count = 0
info_count = 0

common_issues = {
    "database": 0,
    "kafka": 0,
    "memory": 0,
    "cpu": 0,
    "disk": 0,
    "api": 0
}

for log_file in log_files:
    with open(log_file, "r") as file:
        for line in file:
            text = line.lower()

            if "error" in text:
                error_count += 1
            elif "warning" in text:
                warning_count += 1
            elif "info" in text:
                info_count += 1

            for keyword in common_issues:
                if keyword in text:
                    common_issues[keyword] += 1

print("=== Log Monitoring Summary ===")
print("Total INFO messages:", info_count)
print("Total WARNING messages:", warning_count)
print("Total ERROR messages:", error_count)

print("\n=== Common Issues Found ===")
for issue, count in common_issues.items():
    if count > 0:
        print(issue.capitalize() + " issues:", count)

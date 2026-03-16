from datetime import datetime

report_lines = []
report_lines.append("Application Support Incident Summary")
report_lines.append("-----------------------------------")
report_lines.append("Generated on: " + str(datetime.now()))
report_lines.append("")

report_lines.append("Detected Issues:")
report_lines.append("- Kafka broker timeout in application log")
report_lines.append("- Database connection lost in server log")
report_lines.append("- High memory usage warning")
report_lines.append("- CPU and disk utilization warning")
report_lines.append("")

report_lines.append("Recommended Actions:")
report_lines.append("- Restart Kafka broker service")
report_lines.append("- Validate database connectivity")
report_lines.append("- Review memory consumption trend")
report_lines.append("- Check server resource allocation")
report_lines.append("")

report_lines.append("Priority: Medium to High")
report_lines.append("Status: Open for investigation")

with open("output/support_summary.txt", "w") as file:
    for line in report_lines:
        file.write(line + "\n")

print("Incident report created successfully in output/support_summary.txt")

SupportPulse – Application Support Monitoring System

SupportPulse is a medium-sized project that simulates real-world application support workflows.  
It demonstrates how support engineers monitor logs, perform service health checks, and generate incident reports to identify operational issues.

---

## Features

- Monitors application and server logs
- Detects ERROR and WARNING events
- Performs basic service health checks
- Generates incident summary reports
- Uses shell scripting for automation

---

## Technologies

- Python
- Shell Scripting
- Log Monitoring
- Incident Reporting
- Application Support Concepts

---

## Project Structure

```
CitiOps-Monitor
├── README.md
├── requirements.txt
├── logs
│   ├── app_log.txt
│   └── server_log.txt
├── scripts
│   ├── log_monitor.py
│   ├── health_check.py
│   └── incident_report.py
├── automation
│   └── run_monitor.sh
└── output
    └── support_summary.txt
```

---

## How to Run

Run individual scripts:

```
python scripts/log_monitor.py
```

```
python scripts/health_check.py
```

```
python scripts/incident_report.py
```

Or run the full monitoring workflow:

```
bash automation/run_monitor.sh
```

---

## Purpose

This project demonstrates monitoring, troubleshooting, and reporting tasks commonly performed in an application support role.  
It simulates production support activities such as log monitoring, service health validation, and incident documentation.

---

## Example Use Cases

- Identify recurring application errors from logs
- Monitor system warnings and operational alerts
- Perform service health verification
- Generate incident summaries for support teams
- Automate operational monitoring workflows

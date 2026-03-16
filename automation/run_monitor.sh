echo "Starting CitiOps Monitor..."
echo

echo "Running log monitor"
python scripts/log_monitor.py
echo

echo "Running health check"
python scripts/health_check.py
echo

echo "Generating incident report"
python scripts/incident_report.py
echo

echo "Monitoring run completed"

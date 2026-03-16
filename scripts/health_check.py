services = {
    "Application Server": "UP",
    "Database": "UP",
    "Kafka Broker": "DOWN",
    "API Gateway": "UP",
    "Monitoring Service": "UP"
}

print("=== Service Health Check ===")
for service, status in services.items():
    print(f"{service}: {status}")

print("\n=== Failed Services ===")
for service, status in services.items():
    if status == "DOWN":
        print(f"{service} requires attention")

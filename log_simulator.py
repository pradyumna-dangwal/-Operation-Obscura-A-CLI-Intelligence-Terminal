import time

def simulate_logs():
    logs = [
        "Satellite ping received. Location: REDACTED.",
        "Agent Echo failed check-in. Status: Unknown.",
        "Encrypted message intercepted from node 14X.",
        "Unusual energy readings near Site-Δ."
    ]
    print("\nSimulating Surveillance Feed:\n")
    for log in logs:
        print(f"[LOG] {log}")
        time.sleep(1.5)
from loader import load_logs
from detector import detect_response_time_anomalies

def run():
    logs = load_logs("data/sample_logs.csv")
    anomalies = detect_response_time_anomalies(logs)

    if anomalies.empty:
        print("No anomalies detected")
    else:
        print("Anomalies found:")
        print(anomalies)

if __name__ == "__main__":
    run()

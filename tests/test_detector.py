import pandas as pd
from src.detector import detect_response_time_anomalies

def test_anomaly_detection():
    data = {
        "response_time": [100, 110, 95, 1000]
    }
    df = pd.DataFrame(data)
    anomalies = detect_response_time_anomalies(df)

    assert len(anomalies) == 1

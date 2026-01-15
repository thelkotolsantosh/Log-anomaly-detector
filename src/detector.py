import numpy as np

def detect_response_time_anomalies(df, threshold=2.5):
    mean = df["response_time"].mean()
    std = df["response_time"].std()

    upper_limit = mean + threshold * std

    anomalies = df[df["response_time"] > upper_limit]
    return anomalies

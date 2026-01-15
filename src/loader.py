import pandas as pd

def load_logs(path):
    if not path.endswith(".csv"):
        raise ValueError("Only CSV files are supported")

    df = pd.read_csv(path)
    required_cols = {"timestamp", "ip", "status_code", "response_time"}

    if not required_cols.issubset(df.columns):
        raise ValueError("Missing required log fields")

    return df

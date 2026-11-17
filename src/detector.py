import numpy as np

def detect_response_time_anomalies(df, threshold=2.5):
    """Flag slow responses using a median and scaled absolute deviation."""
    if not np.isfinite(threshold) or threshold <= 0:
        raise ValueError("threshold must be finite and greater than zero")
    values = df["response_time"]
    if values.empty:
        return df.copy()
    median = values.median()
    mad = (values - median).abs().median()
    upper_limit = median + threshold * 1.4826 * mad
    return df[values > upper_limit]

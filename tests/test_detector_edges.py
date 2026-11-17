import pandas as pd
from src.detector import detect_response_time_anomalies


def test_constant_and_empty_series_have_no_alerts():
    for values in ([], [100, 100, 100]):
        assert detect_response_time_anomalies(pd.DataFrame({'response_time': values})).empty


def test_spike_above_a_constant_baseline_is_flagged():
    result = detect_response_time_anomalies(pd.DataFrame({'response_time': [100, 100, 100, 1000]}))
    assert result['response_time'].tolist() == [1000]

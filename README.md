Log Anomaly Detector
This project demonstrates a simple approach to detecting abnormal response times
in server access logs.

The goal is not advanced machine learning, but clarity and correctness.

How it works:
- Load structured access logs
- Calculate the median and median absolute deviation (scaled by 1.4826)
- Flag unusually slow responses

The default cutoff is median + 2.5 × scaled deviation. This keeps a single
large spike from inflating its own threshold. When the deviation is zero,
values above the median are flagged; a constant series produces no alerts.

Use cases:
- SOC triage
- Performance monitoring
- Learning baseline anomaly detection

Run:
python src/main.py

TREE of Program
log-anomaly-detector/
│
├── data/
│   └── sample_logs.csv
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── detector.py
│   └── main.py
│
├── tests/
│   └── test_detector.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE

from analytics.anomaly_detection import AnomalyDetector

detector = AnomalyDetector()

test_values = [300, 750, 1200, 1800]

for power in test_values:
    if detector.is_high_consumption(power):
        print(f"⚠️ High consumption detected: {power} W")
    else:
        print(f"Normal consumption: {power} W")

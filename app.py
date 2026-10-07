"print('Base AI Project Setup Ready')" 

import numpy as np

# Mock machine sensor temperature data
sensor_readings = np.array([22.5, 23.2, 21.8, 24.1, 98.4, 22.0, 23.5])

# Calculate core metrics
avg_temp = np.mean(sensor_readings)
max_temp = np.max(sensor_readings)
std_dev = np.std(sensor_readings)

# Simple anomaly threshold (e.g., tracking abnormal spikes)
anomalies = sensor_readings[sensor_readings > 50]

print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Maximum Pressure/Temp Spike: {max_temp:.2f}°C")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Abnormal Spikes Detected: {anomalies}")


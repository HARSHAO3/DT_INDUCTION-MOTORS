import numpy as np
import pandas as pd

# Define simulation time (300 seconds)
timestamps = np.arange(0, 300, 1)  # 1-second intervals
num_samples = len(timestamps)

# Voltage - gradual rise in first 15s, then stable
voltage = np.concatenate([
    np.linspace(0, 230, 15),  
    np.full(num_samples - 15, 230)  
])
voltage += np.random.uniform(-2, 2, size=num_samples)  # Small deviations

# Current - inrush peak, then stabilizing
current = np.concatenate([
    np.linspace(0, 8, 5),  
    np.linspace(8, 4.2, 10),  
    np.full(num_samples - 15, 4.2)  
])
current += np.random.uniform(-0.1, 0.1, size=num_samples)

# Power Factor - gradual increase
power_factor = np.concatenate([
    np.linspace(0, 0.6, 5),  
    np.linspace(0.6, 0.92, 10),  
    np.full(num_samples - 15, 0.92)  
])
power_factor += np.random.uniform(-0.02, 0.02, size=num_samples)

# Power Calculation P = VIcos(phi)
power = voltage * current * power_factor

# Speed - gradual acceleration to 1470 RPM
speed = np.concatenate([
    np.linspace(0, 1470, 20),  
    np.full(num_samples - 20, 1470)  
])
speed += np.random.uniform(-5, 5, size=num_samples)

# Torque Calculation
torque = np.zeros(num_samples)
for i in range(1, num_samples):
    if speed[i] > 0:
        torque[i] = power[i] / (speed[i] * (2 * np.pi / 60))  # P = T * ω
torque += np.random.uniform(-0.2, 0.2, size=num_samples)

# Temperature - slow increase over time
temperature = np.linspace(45, 55, num_samples) + np.random.uniform(-0.5, 0.5, size=num_samples)

# Vibration - low but slightly varying
vibration = np.concatenate([
    np.linspace(0, 0.2, 15),  
    np.full(num_samples - 15, 0.2)  
]) + np.random.uniform(-0.05, 0.05, size=num_samples)

# Create DataFrame
motor_data_realistic = pd.DataFrame({
    "Time (s)": timestamps,
    "Voltage (V)": voltage,
    "Current (A)": current,
    "Power (W)": power,
    "Power Factor": power_factor,
    "Speed (RPM)": speed,
    "Torque (Nm)": torque,
    "Temperature (°C)": temperature,
    "Vibration (m/s²)": vibration
})

# Save dataset
csv_filename = "healthy_motor_data_300s.csv"
motor_data_realistic.to_csv(csv_filename, index=False)

print("✅ Dataset generated successfully!")

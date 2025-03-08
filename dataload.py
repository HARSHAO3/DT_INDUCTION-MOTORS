import numpy as np
import pandas as pd

# Define simulation time (300 seconds)
timestamps = np.arange(0, 300, 1)  # 1-second intervals
num_samples = len(timestamps)

# Voltage remains at 230V after startup (small deviations)
voltage = np.concatenate([
    np.linspace(0, 230, 15),  # Startup ramp (0-15s)
    np.full(num_samples - 15, 230)  
])
voltage += np.random.uniform(-2, 2, size=num_samples)  

# Current behavior for different load levels
current = np.concatenate([
    np.linspace(0, 2, 10),  # No-load startup (0-10s)
    np.full(50, 2),  # No-load stable (10-60s)
    np.linspace(2, 6, 20),  # Partial load transition (60-80s)
    np.full(100, 6),  # Partial load (80-180s)
    np.linspace(6, 8, 20),  # Full load transition (180-200s)
    np.full(100, 8)  # Full load stable (200-300s)
])
current += np.random.uniform(-0.1, 0.1, size=num_samples)

# Power Factor behavior
power_factor = np.concatenate([
    np.linspace(0.2, 0.3, 10),  # No-load startup
    np.full(50, 0.3),  # No-load
    np.linspace(0.3, 0.7, 20),  # Partial load transition
    np.full(100, 0.75),  # Partial load
    np.linspace(0.75, 0.9, 20),  # Full load transition
    np.full(100, 0.9)  # Full load
])
power_factor += np.random.uniform(-0.02, 0.02, size=num_samples)

# Power Calculation P = VIcos(phi)
power = voltage * current * power_factor

# Speed behavior based on load
speed = np.concatenate([
    np.linspace(0, 1490, 20),  # No-load acceleration
    np.full(40, 1490),  # No-load steady
    np.linspace(1490, 1480, 20),  # Partial-load transition
    np.full(100, 1480),  # Partial-load stable
    np.linspace(1480, 1470, 20),  # Full-load transition
    np.full(100, 1470)  # Full-load stable
])
speed += np.random.uniform(-2, 2, size=num_samples)  # Small fluctuations

# Torque Calculation (P = T * ω, ω = 2πN/60)
torque = np.zeros(num_samples)
for i in range(num_samples):
    if speed[i] > 0:
        torque[i] = power[i] / (speed[i] * (2 * np.pi / 60))  # Torque in Nm
torque += np.random.uniform(-0.5, 0.5, size=num_samples)  # Small variations

# Temperature increase over time
temperature = np.concatenate([
    np.linspace(45, 48, 60),  # No-load phase
    np.linspace(48, 52, 120),  # Partial load heating
    np.linspace(52, 60, 120)  # Full load heating
]) + np.random.uniform(-0.5, 0.5, size=num_samples)

# Vibration behavior (low at no-load, increasing at full-load)
vibration = np.concatenate([
    np.linspace(0.1, 0.2, 60),  # No-load phase
    np.linspace(0.2, 0.4, 120),  # Partial load
    np.linspace(0.4, 0.6, 120)  # Full load
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
csv_filename = "healthy_motor_load_variations_300s.csv"
motor_data_realistic.to_csv(csv_filename, index=False)

print("✅ Dataset generated successfully with load variations!")

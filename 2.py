import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Load the cleaned dataset
df = pd.read_csv("cleaned_healthy_motor_data_300s.csv")  

# Display basic dataset information
print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Statistical Summary:")
print(df.describe())

# Plot Voltage, Current, and Temperature over Time
plt.figure(figsize=(10, 5))
plt.plot(df["Time (s)"], df["Voltage (V)"], label="Voltage", color="blue")
plt.plot(df["Time (s)"], df["Current (A)"], label="Current", color="red")
plt.plot(df["Time (s)"], df["Temperature (°C)"], label="Temperature", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Sensor Readings")
plt.title("Motor Parameters Over Time")
plt.legend()
plt.grid()
plt.show()

# Feature Engineering
df["Power (W)"] = df["Voltage (V)"] * df["Current (A)"]  # Calculate Power
df["Temp_Change"] = df["Temperature (°C)"].diff()  # Temperature rate of change

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Save the dataset with new features
df.to_csv("processed_motor_data.csv", index=False)
print("\n✅ Processed data saved as 'processed_motor_data.csv'")

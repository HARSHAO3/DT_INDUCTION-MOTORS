import pandas as pd

def clean_motor_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Strip spaces from column names
    df.columns = df.columns.str.strip()

    # Automatically detect the correct column names
    voltage_col = next((col for col in df.columns if "Voltage" in col), None)
    current_col = next((col for col in df.columns if "Current" in col), None)
    temp_col = next((col for col in df.columns if "Temperature" in col), None)

    # Ensure all required columns are found
    if not all([voltage_col, current_col, temp_col]):
        raise KeyError("Missing required columns in CSV. Found: ", df.columns.tolist())

    # Normalize each column
    for col in [voltage_col, current_col, temp_col]:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    # Save cleaned data
    output_file = "cleaned_" + file_path
    df.to_csv(output_file, index=False)
    print(f"✅ Data cleaned and saved as {output_file}")

# Run the cleaning function on your dataset
clean_motor_data("healthy_motor_data_300s.csv")

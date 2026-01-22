import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSV files
csv_files = list(data_path.glob("*.csv"))

# Empty list to store dataframes
dfs = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only Pink Morsel
    df = df[df["product"] == "Pink Morsel"]

    # Create sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns to match requirement
    df.columns = ["Sales", "Date", "Region"]

    dfs.append(df)

# Combine all data into one dataframe
final_df = pd.concat(dfs, ignore_index=True)

# Save output file
final_df.to_csv("processed_sales_data.csv", index=False)

print("Data processing complete. Output saved as processed_sales_data.csv")

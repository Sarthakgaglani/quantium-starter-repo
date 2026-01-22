import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSV files
files = list(data_path.glob("*.csv"))
df_list = [pd.read_csv(file) for file in files]

# Combine all CSVs
df = pd.concat(df_list, ignore_index=True)

# Filter only Pink Morsels
df = df[df["product"] == "Pink Morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep required columns
final_df = df[["sales", "date", "region"]]

# Save output
final_df.to_csv("processed_sales.csv", index=False)

print("Data processing complete ✅")
